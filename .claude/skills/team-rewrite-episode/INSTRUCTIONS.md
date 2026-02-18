# Team Episode Rewrite Pipeline

エージェントチームを使用して既存エピソードをリライトするオーケストレーション手順。

## Phase 1: Preparation（準備）— Team Lead

1. 対象ファイルを `Read` で全文読み込む
2. **Story Profile を特定する**:
   - 対象ファイルのパスからプロジェクト名を取得（例: `projects/angel_return/drafts/...` → `angel_return`）
   - `.agent/profiles/{project_name}.md` を `Read` で読み込む
   - 存在しない場合はユーザーに確認する
3. リライトの重点をユーザーに確認する:
   - **Logic Fix**: 設定矛盾や時系列の修正
   - **Style Polish**: 文体の統一、五感描写の強化
   - **Foreshadowing**: 伏線の追加・整理
   - **Full Rewrite**: プロットごと書き直し
   - **All**: 上記すべて（推奨）
4. 関連する設定ファイルを確認する:
   - 直前・直後のエピソード
   - `docs/foreshadowing.md`
   - 関連するキャラクター・世界観設定
5. **Note**: 必要に応じて `check-arc-consistency` スキルを実行し、対象エピソードのキャラクターアーク不整合を事前に把握できる。

### Phase 1 チェックリスト
- [ ] 対象ドラフト全文読み込み完了
- [ ] Story Profile 読み込み完了
- [ ] リライトの重点をユーザーと確認済み
- [ ] 関連設定ファイル確認済み

## Phase 2: Diagnostic（並列診断）— Editor + Proofreader

以下の2つのサブエージェントを **並列で** 起動する。**スコアも必須**（ベースラインとして記録）。各エージェントは**自分の専門軸のみ**を採点する（重複なし）。

### editor サブエージェント（50点満点）
- 対象: リライト対象のドラフト
- 採点軸: Engagement & Emotion /20, Plot & Pacing /15, Prose & Voice /15
- 診断観点:
  - 文体チェック（Story Profile のトーン維持）
  - ペース配分と描写密度
  - **散文密度チェック**: 一文一行のスタッカートがないか、段落が3〜5文で構成されているか、文長にバリエーションがあるか、余白が厳選されているか
  - **文字数チェック**: 7,000文字未満の場合は「肉付け不足」として報告
  - 読者没入度（引き、ツイスト、不穏さ）
  - Natural Prose Check（AI臭の排除）
- **必ず 50点満点のスコアを含めること**（editor.md の Quality Gate スコア参照）

### proofreader サブエージェント（50点満点）
- 対象: 同じドラフト
- 採点軸: Character Integrity /20, World & Continuity /15, Author Rules & Aesthetics /15
- 診断観点:
  - 設定整合性（キャラ・世界観・時系列）
  - 著者美学チェック（Author DNA + Story Profile の美学）
  - Story Profile 禁止事項チェック
  - 伏線管理状況の確認
  - キャプションの有無・内容確認
- **必ず 50点満点のスコアを含めること**（proofreader.md の Quality Gate スコア参照）

両方の完了を待つ。ベースラインスコア（合計）を記録する。

### Phase 2 チェックリスト
- [ ] Editor レポート + スコア受領
- [ ] Proofreader レポート + スコア受領
- [ ] ベースラインスコア記録: Editor XX/50 + Proofreader XX/50 = 合計 XX/100

## Phase 3: Proposal（修正案提示）— Team Lead

1. Editor と Proofreader のレポートを統合する
2. Before/After 形式で修正案をリストアップする
3. 修正の優先順位を付ける:
   - **Critical**: 設定矛盾、キャラ口調の矛盾、Story Profile禁止事項の違反
   - **High**: AI臭い文章、描写密度の不足
   - **Medium**: ペース配分、伏線の強化
   - **Low**: 微細な表現の推敲
4. ユーザーに提示し、どの修正を適用するか決定する

### Phase 3 チェックリスト
- [ ] レポート統合・優先順位付け完了
- [ ] Before/After 形式で修正案リスト化
- [ ] ユーザーが適用する修正を決定

## Phase 4: Rewrite（リライト実行）— Writer Agent

承認された修正に基づき、**writer** サブエージェントに委任する。

指示に含める情報:
- 承認された修正案の全リスト
- 対象ファイルのパス
- 修正の範囲（部分修正 or 全面書き直し）
- 部分修正の場合: `Edit` ツールで対象箇所を修正
- 全面書き直しの場合: `Write` ツールで全体を再生成
- キャプションの更新が必要な場合は `[caption]` ブロックも修正

### Phase 4 チェックリスト
- [ ] 承認された修正の適用完了
- [ ] 修正後のドラフト保存済み

## Phase 5: Quality Gate — 再評価ループ

Writer の修正が完了したら、品質ゲートで修正効果を検証する。

### ループ設定
- **通過閾値**: 80/100（Editor /50 + Proofreader /50 の合計）
- **最大試行回数**: 3回
- **試行回数のカウント**: 最初の再評価を第1回とする

### 5a. E+P 並列再評価

以下の2つのサブエージェントを **並列で** 起動する。各エージェントは**自分の専門軸のみ**を採点する（重複なし）。

#### editor サブエージェント（50点満点）
- 対象: 修正後のドラフト
- 採点軸: Engagement & Emotion /20, Plot & Pacing /15, Prose & Voice /15
- レビュー観点: Phase 2 と同じ + 前回指摘事項の改善確認
- **必ず 50点満点のスコアを含めること**

#### proofreader サブエージェント（50点満点）
- 対象: 同じドラフト
- 採点軸: Character Integrity /20, World & Continuity /15, Author Rules & Aesthetics /15
- レビュー観点: Phase 2 と同じ + 前回指摘事項の改善確認
- **必ず 50点満点のスコアを含めること**

両方の完了を待つ。

### 5b. スコア判定

1. Editor スコア(/50)と Proofreader スコア(/50)を合算する
2. ベースラインからの変化量とともにユーザーに提示する

**合計 ≥ 80 の場合:**
- 残課題があればユーザーに提示（軽微な修正の承認判断）
- 承認された修正があれば **writer** サブエージェントに委任して適用する
- Phase 6 へ進む

**合計 < 80 かつ 試行回数 < 3 の場合:**
- E+P レポートから **Critical / High** の新規課題を抽出する
- **writer** サブエージェントに課題リストを渡して修正を委任する
- 試行回数をインクリメントし、**5a へ戻る**

**合計 < 80 かつ 試行回数 = 3 の場合:**
- ベースライン → 全イテレーションのスコア推移を提示する
- ユーザーに判断を仰ぐ:
  - **現状で進む**: Phase 6 へ
  - **手動修正**: ユーザーが具体的な修正を指示
  - **中止**: パイプラインを終了

### Phase 5 チェックリスト
- [ ] 合計 ≥ 80 で通過（またはユーザー判断で通過）
- [ ] スコア推移記録: ベースライン XX → 最終 XX/100
- [ ] 追加修正の適用完了（該当する場合）

## Phase 6: Post-processing（事後処理）— Publisher Agents (並列) + Team Lead

### 6a. Pixiv/Hameln 並列生成

2つの **publisher** サブエージェントを `run_in_background=True` で**並列起動**する:

- **Pixiv Publisher**: 「ドラフト `{path}` からPixiv版を全面再生成してください。出力先: `dist/pixiv/XX_title_pixiv.txt`。`Ep.\d` 残存チェックも実行してください」
- **Hameln Publisher**: 「ドラフト `{path}` からハーメルン版を全面再生成してください。出力先: `dist/hameln/XX_title_hameln.txt`。`Ep.\d` 残存チェックも実行してください」

両方の完了を待つ。

### 6b. 共通処理（Team Lead が実施）

両方の Publisher が完了した後、Team Lead が以下を実行する:

1. **キャプション更新**: `dist/pixiv/caption.txt` を `Read` → `Edit`（フォーマットは `publisher.md` §2 参照）
2. **ドキュメント更新**: 伏線管理表（`docs/foreshadowing.md`）、設定ファイル等を必要に応じて更新
3. **クリップボードコピー**: `Bash` で以下を実行:
   ```
   powershell -ExecutionPolicy Bypass -File "d:\VibeWorkspace\novel\copy_to_clip.ps1" "<pixiv_file_absolute_path>" "<draft_file_absolute_path>"
   ```
4. **Note**: リライトで構造的な変更（シーン追加・削除、キャラクターの行動変更等）があった場合、`sync-story-profile` スキルで Story Profile への反映要否を確認できる。

### Phase 6 チェックリスト
- [ ] Pixiv版の並列生成完了 + Ep.\d チェック通過
- [ ] Hameln版の並列生成完了 + Ep.\d チェック通過
- [ ] キャプション更新完了
- [ ] ドキュメント更新完了
- [ ] クリップボードコピー完了

## Phase 7: Completion（完了）

1. 変更内容のサマリーを提示する
   - Quality Gate スコア推移（ベースライン → 全イテレーション）
2. コミットの要否をユーザーに確認する
3. コミットが指示された場合のみ実行する
