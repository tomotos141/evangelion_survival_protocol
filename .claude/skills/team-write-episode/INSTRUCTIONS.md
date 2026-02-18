# Team Episode Writing Pipeline

エージェントチームを使用してエピソードを執筆するオーケストレーション手順。

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
4. エピソードデザインが未作成なら、ユーザーと相談して作成する
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

## Phase 3: Quality Gate — E+P 評価ループ

Writer の出力が完了したら、品質ゲートに入る。

### ループ設定
- **通過閾値**: 80/100（Editor + Proofreader の平均スコア）
- **最大試行回数**: 3回
- **試行回数のカウント**: 最初の E+P 評価を第1回とする

### 3a. E+P 並列評価

以下の2つのサブエージェントを **並列で** 起動する:

#### editor サブエージェント
- 対象: 現在のドラフト
- レビュー観点: 文体、ペース配分、読者没入度、Natural Prose、Story Profile固有の構造チェック
- **必ず 100点満点のスコアを含めること**（editor.md の Quality Gate スコア参照）

#### proofreader サブエージェント
- 対象: 同じドラフト
- レビュー観点: 設定整合性、キャラクター一貫性、時系列、著者美学
- 参照: `docs/characters/`, `docs/world/`, `docs/foreshadowing.md`
- **必ず 100点満点のスコアを含めること**（proofreader.md の Quality Gate スコア参照）

両方の完了を待つ。

### 3b. スコア判定

1. Editor スコアと Proofreader スコアの平均を算出する
2. スコアとイテレーション番号をユーザーに提示する

**平均 ≥ 80 の場合:**
- E+P レポートの残課題をユーザーに提示する（軽微な修正の承認判断）
- 承認された修正があれば **writer** サブエージェントに委任して適用する
- Phase 4 へ進む

**平均 < 80 かつ 試行回数 < 3 の場合:**
- E+P レポートから **Critical / High** の課題を抽出する
- **writer** サブエージェントに課題リストを渡して修正を委任する
- 試行回数をインクリメントし、**3a へ戻る**

**平均 < 80 かつ 試行回数 = 3 の場合:**
- 全イテレーションのスコア推移を提示する
- ユーザーに判断を仰ぐ:
  - **現状で進む**: Phase 4 へ
  - **手動修正**: ユーザーが具体的な修正を指示
  - **中止**: パイプラインを終了

### Phase 3 チェックリスト
- [ ] スコア ≥ 80 で通過（またはユーザー判断で通過）
- [ ] 最終スコア記録: Editor XX/100 + Proofreader XX/100 = 平均 XX/100
- [ ] 残課題の修正適用完了（該当する場合）

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
   powershell -ExecutionPolicy Bypass -File "d:\VibeWorkspace\novel\copy_to_clip.ps1" "<pixiv_file_absolute_path>" "<draft_file_absolute_path>"
   ```
4. **Note**: エピソードが構造設計原則に影響する変更を含む場合、`sync-story-profile` スキルで Story Profile への反映要否を確認できる。

### Phase 4 チェックリスト
- [ ] Pixiv版の並列生成完了 + Ep.\d チェック通過
- [ ] Hameln版の並列生成完了 + Ep.\d チェック通過
- [ ] キャプション更新完了
- [ ] ドキュメント更新完了
- [ ] クリップボードコピー完了

## Phase 5: Completion（完了）

1. 全成果物の一覧を提示する:
   - `drafts/XX_title.md`（ドラフト）
   - `dist/pixiv/XX_title_pixiv.txt`（Pixiv版）
   - `dist/hameln/XX_title_hameln.txt`（ハーメルン版）
   - `dist/pixiv/caption.txt`（キャプション更新）
   - 更新されたドキュメント類
   - Quality Gate スコア推移（全イテレーション）
2. コミットの要否をユーザーに確認する
3. コミットが指示された場合のみ実行する
