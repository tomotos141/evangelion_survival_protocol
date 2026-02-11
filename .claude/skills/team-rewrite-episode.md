---
name: team-rewrite-episode
description: エージェントチームによるエピソードリライトパイプライン。既存原稿を Editor と Proofreader が並列診断し、Writer がリライトを実施する。「チームでリライト」「チーム推敲」「team rewrite」で発動する。
---

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

## Phase 2: Diagnostic（並列診断）— Editor + Proofreader

以下の2つのサブエージェントを **並列で** 起動する。

### editor サブエージェント
- 対象: リライト対象のドラフト
- 診断観点:
  - 文体チェック（Story Profile のトーン維持）
  - ペース配分と描写密度
  - **散文密度チェック**: 一文一行のスタッカートがないか、段落が3〜5文で構成されているか、文長にバリエーションがあるか、余白が厳選されているか
  - **文字数チェック**: 7,000文字未満の場合は「肉付け不足」として報告
  - 読者没入度（引き、ツイスト、不穏さ）
  - Natural Prose Check（AI臭の排除）
  - 伏線管理状況の確認

### proofreader サブエージェント
- 対象: 同じドラフト
- 診断観点:
  - 設定整合性（キャラ・世界観・時系列）
  - 著者美学チェック（Author DNA + Story Profile の美学）
  - Story Profile 禁止事項チェック
  - キャプションの有無・内容確認

両方の完了を待つ。

## Phase 3: Proposal（修正案提示）— Team Lead

1. Editor と Proofreader のレポートを統合する
2. Before/After 形式で修正案をリストアップする
3. 修正の優先順位を付ける:
   - **Critical**: 設定矛盾、キャラ口調の矛盾、Story Profile禁止事項の違反
   - **High**: AI臭い文章、描写密度の不足
   - **Medium**: ペース配分、伏線の強化
   - **Low**: 微細な表現の推敲
4. ユーザーに提示し、どの修正を適用するか決定する

## Phase 4: Rewrite（リライト実行）— Writer Agent

承認された修正に基づき、**writer** サブエージェントに委任する。

指示に含める情報:
- 承認された修正案の全リスト
- 対象ファイルのパス
- 修正の範囲（部分修正 or 全面書き直し）
- 部分修正の場合: `Edit` ツールで対象箇所を修正
- 全面書き直しの場合: `Write` ツールで全体を再生成
- キャプションの更新が必要な場合は `[caption]` ブロックも修正

## Phase 5: Post-processing（事後処理）— Publisher Agent

**publisher** サブエージェントに委任する:
- Pixiv版の再生成または部分修正
- キャプションの更新
- `Ep.\d` の残存チェック
- ドキュメント更新（伏線管理表、設定ファイル等）
- **Note**: リライトで構造的な変更（シーン追加・削除、キャラクターの行動変更等）があった場合、`sync-story-profile` スキルで Story Profile への反映要否を確認できる。

## Phase 6: Completion（完了）

1. 変更内容のサマリーを提示する
2. コミットの要否をユーザーに確認する
3. コミットが指示された場合のみ実行する
