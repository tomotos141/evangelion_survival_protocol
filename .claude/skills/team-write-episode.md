---
name: team-write-episode
description: エージェントチームによるエピソード執筆パイプライン。Writer, Editor, Proofreader, Publisher の4エージェントを順次・並列に活用して新規エピソードを執筆する。「チームで書いて」「チーム執筆」「team write」で発動する。
---

# Team Episode Writing Pipeline

エージェントチームを使用してエピソードを執筆するオーケストレーション手順。

## Phase 1: Preparation（準備）— Team Lead が実施

1. プロジェクトディレクトリを特定する
2. 以下の資料を `Read` で確認する:
   - `docs/overall_plot_v2.md` — 全体プロットと進捗
   - `docs/foreshadowing.md` — 未回収の伏線
   - 直前エピソードのドラフト末尾 — 感情・身体状態の引き継ぎ
   - `docs/world/hard_mode_guidelines.md`, `docs/world/eva_abilities.md`
   - `docs/episodes/ep##_title.md`（エピソードデザイン）
3. エピソードデザインが未作成なら、ユーザーと相談して作成する
4. ユーザーの承認を得てから Phase 2 へ進む

## Phase 2: Drafting（執筆）— Writer Agent

**writer** サブエージェントに委任する。

指示に含める情報:
- エピソードデザインの全文
- 関連設定ファイルのパス一覧
- 直前エピソードの末尾状態（引き継ぎ情報）
- 出力先ファイルパス: `drafts/XX_english_title.md`

Writer の完了を待つ。

## Phase 3: Review（並列レビュー）— Editor + Proofreader

Writer の出力が完了したら、以下の2つのサブエージェントを **並列で** 起動する。

### editor サブエージェント
- 対象: Writer が出力したドラフト
- レビュー観点: 文体、ペース配分、読者没入度、Natural Prose、二面性の演出

### proofreader サブエージェント
- 対象: 同じドラフト
- レビュー観点: 設定整合性、キャラクター一貫性、時系列、著者美学
- 参照: `docs/characters/`, `docs/world/`, `docs/foreshadowing.md`

両方の完了を待つ。

## Phase 4: Revision（修正）— Team Lead がとりまとめ

1. Editor と Proofreader のレポートを統合する
2. 修正の優先順位を付ける:
   - **Critical**: 設定矛盾、キャラの口調/行動の矛盾、Ep.X参照の残存
   - **High**: 描写密度の不足、AI臭い文章、予定調和
   - **Medium**: ペース配分の改善、伏線の強化
   - **Low**: 微細な表現の推敲
3. 修正案をユーザーに提示し、どれを適用するか承認を得る
4. 承認された修正を **writer** サブエージェントに委任して適用する

## Phase 5: Publishing（公開準備）— Publisher Agent

修正が完了し、ユーザーの最終OKが出たら:

**publisher** サブエージェントに委任する:
- Pixiv版生成（UTF-8 BOM）
- キャプション更新
- ドキュメント更新（`overall_plot_v2.md`, `foreshadowing.md`）
- 最終検証（`Ep.\d` 残存チェック）

## Phase 6: Completion（完了）

1. 全成果物の一覧を提示する:
   - `drafts/XX_title.md`（ドラフト）
   - `dist/pixiv/XX_title_pixiv.txt`（Pixiv版）
   - `dist/pixiv/caption.txt`（キャプション更新）
   - 更新されたドキュメント類
2. コミットの要否をユーザーに確認する
3. コミットが指示された場合のみ実行する
