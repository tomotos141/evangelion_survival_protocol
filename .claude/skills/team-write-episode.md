---
name: team-write-episode
description: エージェントチームによるエピソード執筆パイプライン。Writer, Editor, Proofreader, Publisher の4エージェントを順次・並列に活用して新規エピソードを執筆する。「チームで書いて」「チーム執筆」「team write」で発動する。
---

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

## Phase 3: Review（並列レビュー）— Editor + Proofreader

Writer の出力が完了したら、以下の2つのサブエージェントを **並列で** 起動する。

### editor サブエージェント
- 対象: Writer が出力したドラフト
- レビュー観点: 文体、ペース配分、読者没入度、Natural Prose、Story Profile固有の構造チェック

### proofreader サブエージェント
- 対象: 同じドラフト
- レビュー観点: 設定整合性、キャラクター一貫性、時系列、著者美学
- 参照: `docs/characters/`, `docs/world/`, `docs/foreshadowing.md`

両方の完了を待つ。

### Phase 3 チェックリスト
- [ ] Editor レポート受領
- [ ] Proofreader レポート受領
- [ ] レポート統合・優先順位付け完了

## Phase 4: Revision（修正）— Team Lead がとりまとめ

1. Editor と Proofreader のレポートを統合する
2. 修正の優先順位を付ける:
   - **Critical**: 設定矛盾、キャラの口調/行動の矛盾、Story Profile禁止事項の違反
   - **High**: 描写密度の不足、AI臭い文章、予定調和
   - **Medium**: ペース配分の改善、伏線の強化
   - **Low**: 微細な表現の推敲
3. 修正案をユーザーに提示し、どれを適用するか承認を得る
4. 承認された修正を **writer** サブエージェントに委任して適用する

### Phase 4 チェックリスト
- [ ] ユーザーが修正案を承認
- [ ] Writer による修正適用完了
- [ ] 修正後のドラフト保存済み

## Phase 5: Publishing（公開準備）— Publisher Agent

修正が完了し、ユーザーの最終OKが出たら:

**publisher** サブエージェントに委任する:
- Pixiv版生成（UTF-8 BOM）
- ハーメルン版生成（UTF-8、BOMなし）
- キャプション更新
- ドキュメント更新（`overall_plot_v2.md`, `foreshadowing.md`）
- 最終検証（`Ep.\d` 残存チェック — Pixiv版・ハーメルン版の両方）
- **Note**: エピソードが構造設計原則に影響する変更を含む場合（新しい伏線の導入、キャラクターの重要な行動追加等）、`sync-story-profile` スキルで Story Profile への反映要否を確認できる。

### Phase 5 チェックリスト
- [ ] Pixiv版生成 (UTF-8 BOM)
- [ ] Hameln版生成 (UTF-8, BOMなし)
- [ ] キャプション更新
- [ ] ドキュメント更新 (foreshadowing.md 等)
- [ ] Ep.\d 残存チェック通過

## Phase 6: Completion（完了）

1. 全成果物の一覧を提示する:
   - `drafts/XX_title.md`（ドラフト）
   - `dist/pixiv/XX_title_pixiv.txt`（Pixiv版）
   - `dist/hameln/XX_title_hameln.txt`（ハーメルン版）
   - `dist/pixiv/caption.txt`（キャプション更新）
   - 更新されたドキュメント類
2. コミットの要否をユーザーに確認する
3. コミットが指示された場合のみ実行する
