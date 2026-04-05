---
name: team-write-episode
description: Agent team episode writing pipeline. Orchestrates Writer, Editor, Proofreader, and Publisher for new episodes. Use when writing a new episode from an episode design.
---

# team-write-episode

Agent team episode writing pipeline. Orchestrates Writer, Editor, Proofreader, and Publisher for new episodes.

**スキルの場所**: `.claude/skills/team-write-episode/`
**参照ファイル**:
- `reference/quality-gate.md` — Quality Gate v3 採点仕様（5軸 100pt）
- `reference/actionlog-template.md` — ACTIONLOG 記録テンプレート
- `reference/actions.jsonl` — 実行ログ（自動蓄積）

**データベース**: `tools/novel_db.py` — SQLite CLI。エピソード・キャラ・伏線・タイムラインの構造化データ管理。

---

## Phase 1: Preparation（準備）— Team Lead が実施

1. プロジェクトディレクトリを特定する
2. **Story Profile を特定する**:
   - 対象エピソードのパスからプロジェクト名を取得（例: `projects/angel_return/drafts/...` → `angel_return`）
   - `.agent/profiles/{project_name}.md` を `Read` で読み込む
   - 存在しない場合はユーザーに確認する
3. 以下の資料を `Read` で確認する:
   - `docs/overall_plot.md` — 全体プロットと進捗
   - `docs/foreshadowing.md` — 未回収の伏線
   - 直前エピソードのドラフト末尾 — 感情・身体状態の引き継ぎ
   - `docs/world/` 配下の設定ファイル
   - `docs/episodes/ep##_title.md`（エピソードデザイン）
   - `docs/timeline.md` — タイムライン（存在する場合。連載で日付矛盾を防ぐ）
   - `docs/style_guide.md` — スタイルガイド（存在する場合。表記統一）
4. エピソードデザインが未作成なら、ユーザーと相談して作成する
   - ミステリー/事件回の場合: `.agent/templates/mystery_design_template.md` を参照し、犯人/原因視点からの逆算で手がかりを配置する
5. ユーザーの承認を得てから Phase 2 へ進む

### Phase 1 チェックリスト
- [ ] Story Profile 読み込み完了
- [ ] エピソードデザイン確認済み
- [ ] 直前エピソードの末尾状態を把握
- [ ] ユーザー承認済み

## Phase 2: Drafting（執筆）— Writer Agent

**writer** サブエージェントに委任する。

指示に含める情報:
- **Story Profile のパス**: `.agent/profiles/{project_name}.md`
- エピソードデザインの全文
- 関連設定ファイルのパス一覧
- 直前エピソードの末尾状態（引き継ぎ情報）
- 出力先ファイルパス: `drafts/XX_english_title.md`
- **散文密度の指示**: 1話 7,000〜10,000文字。一文一行のスタッカート禁止。3〜5文で段落を構成し、文長のバリエーションを意識すること。想定読者は30代男性。

Writer の完了を待つ。

### Phase 2 チェックリスト
- [ ] Writer の出力が 7,000〜10,000字の範囲内
- [ ] ドラフトファイル保存済み

## Phase 3: Quality Gate — 5軸評価ループ

Writer の出力が完了したら、品質ゲートに入る。

→ 採点仕様の詳細は `reference/quality-gate.md` (v3) を参照。

### ループ設定
- **通過閾値**: 80/100（5軸合計）
- **最大試行回数**: 3回
- **試行回数のカウント**: 最初の評価を第1回とする

### 3a. 5軸並列評価

以下のサブエージェントを **全て並列で** 起動する。各エージェントは**自分の専門軸のみ**を採点する（重複なし）。

#### editor サブエージェント（25点満点）
- 対象: 現在のドラフト
- 採点軸: Engagement & Emotion /10, Plot & Pacing /8, Prose & Voice /7
- **必ず 25点満点のスコアを含めること**

#### proofreader サブエージェント（25点満点）
- 対象: 同じドラフト
- 採点軸: Character Integrity /10, World & Continuity /8, Author Rules & Aesthetics /7
- 参照: `docs/characters/`, `docs/world/`, `docs/foreshadowing.md`
- **必ず 25点満点のスコアを含めること**

#### first-reader サブエージェント（20点満点）
- 対象: 同じドラフト（**設定資料は読まない**）
- 採点軸: Hook /8, Retention /6, Next-want /6
- **必ず 20点満点のスコアを含めること**

#### mystery-auditor サブエージェント（15点満点）— ミステリー要素がある場合のみ
- 対象: 同じドラフト
- 採点軸: Clue Fairplay /5, Rule Consistency /5, Secret Management /5
- 参照: `docs/mystery_design.md`, `docs/world/core_rules.md`
- **ミステリー要素がない場合はスキップし、15pt を Editor(+8) と Proofreader(+7) に再配分**
- **必ず 15点満点のスコアを含めること**

#### freshness-checker サブエージェント（15点満点）
- 対象: 同じドラフト
- 採点軸: Pattern /5, Template /5, Explanation Economy /5
- **必ず 15点満点のスコアを含めること**

全員の完了を待つ。

### 3b. スコア判定

1. 5軸のスコアを合算する（合計 /100）
2. 合計スコアとイテレーション番号をユーザーに提示する

**合計 ≥ 80 の場合:**
- 残課題をユーザーに提示する（軽微な修正の承認判断）
- 承認された修正があれば **writer** サブエージェントに委任して適用する
- Phase 4 へ進む

**合計 < 80 かつ 試行回数 < 3 の場合:**
- 全レポートから **Critical / High** の課題を抽出する
- **writer** サブエージェントに課題リストを渡して修正を委任する
- 試行回数をインクリメントし、**3a へ戻る**

**合計 < 80 かつ 試行回数 = 3 の場合:**
- 全イテレーションのスコア推移を提示する
- ユーザーに判断を仰ぐ:
  - **現状で進む**: Phase 4 へ
  - **手動修正**: ユーザーが具体的な修正を指示
  - **中止**: パイプラインを終了

### 3c. ACTIONLOG 記録

Quality Gate の判定が確定したら（通過・不通過・手動判断いずれも）:
→ `reference/actionlog-template.md` に従い ACTIONLOG を記録する。

### Phase 3 チェックリスト
- [ ] スコア ≥ 80 で通過（またはユーザー判断で通過）
- [ ] 最終スコア記録: E XX/25 + P XX/25 + FR XX/20 + MA XX/15 + FC XX/15 = 合計 XX/100
- [ ] 残課題の修正適用完了（該当する場合）
- [ ] ACTIONLOG 記録完了

## Phase 4: Publishing（公開準備）— Publisher Agents (並列) + Team Lead

Quality Gate 通過後:

### 4a. Pixiv/Hameln 並列生成

2つの **publisher** サブエージェントを `run_in_background=True` で**並列起動**する:

- **Pixiv Publisher**: 「ドラフト `{path}` からPixiv版を全面再生成してください。出力先: `dist/pixiv/XX_title_pixiv.txt`。`Ep.\d` 残存チェックも実行してください」
- **Hameln Publisher**: 「ドラフト `{path}` からハーメルン版を全面再生成してください。出力先: `dist/hameln/XX_title_hameln.txt`。`Ep.\d` 残存チェックも実行してください」

両方の完了を待つ。

### 4b. 共通処理（Team Lead が実施）

両方の Publisher が完了した後、Team Lead が以下を実行する:

1. **キャプション更新**: `dist/pixiv/caption.txt` を `Read` → `Edit`（フォーマットは `publisher.md` §2 参照）
2. **ドキュメント更新**: `overall_plot.md`, `foreshadowing.md` 等を必要に応じて更新
3. **クリップボードコピー**: `Bash` で以下を実行:
   ```
   powershell -ExecutionPolicy Bypass -File "./copy_to_clip.ps1" "<pixiv_file_absolute_path>" "<draft_file_absolute_path>"
   ```
4. **Note**: エピソードが構造設計原則に影響する変更を含む場合、`sync-story-profile` スキルで Story Profile への反映要否を確認できる。

### Phase 4 チェックリスト
- [ ] Pixiv版の並列生成完了 + Ep.\d チェック通過
- [ ] Hameln版の並列生成完了 + Ep.\d チェック通過
- [ ] キャプション更新完了
- [ ] ドキュメント更新完了
- [ ] クリップボードコピー完了

## Phase 5: Completion（完了）

1. **DB更新**: `Bash` で以下を実行して SQLite DB を更新する:
   ```bash
   python tools/novel_db.py query "UPDATE episodes SET word_count=XXXX, editor_score=XX, proofreader_score=XX, first_reader_score=XX, mystery_auditor_score=XX, freshness_score=XX, total_score=XX, status='completed' WHERE project_id='PROJECT' AND number=NN"
   ```
   - タイムラインに新規イベントがあれば `timeline_events` に INSERT
   - 伏線のステータスが変わったら `foreshadowing` を UPDATE
2. 全成果物の一覧を提示する:
   - `drafts/XX_title.md`（ドラフト）
   - `dist/pixiv/XX_title_pixiv.txt`（Pixiv版）
   - `dist/hameln/XX_title_hameln.txt`（ハーメルン版）
   - `dist/pixiv/caption.txt`（キャプション更新）
   - 更新されたドキュメント類
   - Quality Gate スコア推移（全イテレーション）
3. コミットの要否をユーザーに確認する
4. コミットが指示された場合のみ実行する

## 依存

- `.agent/profiles/{project_name}.md` — Story Profile
- `reference/quality-gate.md` — Quality Gate v3 採点仕様
- `reference/actionlog-template.md` — ACTIONLOG 記録テンプレート
- `docs/overall_plot.md`, `docs/foreshadowing.md` — プロット・伏線管理
- `docs/characters/*.md`, `docs/world/` — 設定ファイル
- `docs/episodes/ep##_title.md` — エピソードデザイン
- `tools/novel_db.py` — SQLite DB CLI（Phase 5 の DB 更新）
- `./copy_to_clip.ps1` — クリップボードコピースクリプト

## Telemetry

**このステップはスキル完了時に必ず実行すること。省略は禁止。**

スキル完了時に actions.jsonl に追記:

```bash
cat >> .claude/skills/team-write-episode/reference/actions.jsonl << JSONL
{"timestamp":"$(date -u +%Y-%m-%dT%H:%M:%SZ)","skill":"team-write-episode","action":"write","input_summary":"[入力要約]","output_summary":"[結果要約]","issues":[],"successes":[],"user_feedback":"none"}
JSONL
```
