---
description: 既存のエピソードを多角的な視点（整合性、文体、伏線、描写密度）で診断し、リライトするためのワークフロー
---

# Episode Rewrite & Polish Workflow

既存の原稿（Draft）に対して、設定の整合性、作家性、伏線管理、文章品質などのチェックを一括で行い、リライトによって完成度を高めるための手順です。

## 1. Preparation (準備)
- [ ] **Select Target**: リライト対象となるエピソードのファイルパス（`drafts/XX_title.md`）を特定する。
- [ ] **Set Focus**: 今回のリライトで特に重視するポイントをユーザーに確認する。
    - **Logic Fix**: 設定矛盾や時系列の修正。
    - **Style Polish**: 文体の統一、五感描写の強化。
    - **Foreshadowing**: 伏線の追加・整理。
    - **All**: 上記すべて（推奨）。

## 2. Comprehensive Diagnostic (総合診断)
対象ファイルを読み込み、以下の4つの観点で分析を行う。各スキルの指示に従ってチェックを実施する。

- [ ] **Check 1: Logic & Consistency** (by `consistency_check` skill)
    - 設定資料 (`docs/`) との矛盾はないか？
    - キャラクターの言動は性格設定や直前の文脈と合致しているか？
    - 時系列や事実関係に誤りはないか？
- [ ] **Check 2: Foreshadowing & Mysteries** (Reference: `docs/foreshadowing.md`)
    - 伏線管理ファイルにある未回収の伏線 (`🔴/🟡`) が適切に扱われているか？
    - 意図しない「矛盾」が「未回収の伏線」に見えてしまっていないか？
    - 新たに伏線として登録すべき要素はあるか？
- [ ] **Check 3: Author Style & Tone** (by `author_style_check` skill)
    - "Hardboiled / Cynical" な態度は維持されているか？
    - 不要な感傷、説明過多なセリフ、甘すぎる展開はないか？
- [ ] **Check 4: Sensory Density** (by `story_editor` skill)
    - 「五感描写」は十分か？（視覚だけでなく、聴覚、嗅覚、触覚、内部感覚）
    - 情景描写は解像度が高く、かつ簡潔か？
- [ ] **Check 5: Caption Existence & Review (必須)**:
    - ドラフト末尾に `[caption]...[/caption]` ブロックが存在するか確認する。**存在しない場合は必ず新規作成案を提示する。**
    - Pixiv用のキャプションの内容が、リライト後の本文と矛盾していないか確認する。
    - 読者の興味を引く簡潔な導入文になっているか？

## 3. Proposal (修正案の提示)
- [ ] **Report**: 診断で見つかった問題点と、具体的な修正案（Before/Afterの例）をリストアップしてユーザーに提示する。
    - キャプションの修正が必要な場合は、その文案も提示する。
- [ ] **Approval**: どの修正を適用するか決定する。

## 4. Execution (リライト実行)
承認された修正案に基づき、ファイルの内容を更新する。

- [ ] **Rewrite Draft**: 原則として `replace_file_content` または `multi_replace_file_content` を使用し、対象箇所を修正する。
    - 大規模な書き換えが必要な場合は、バックアップを取るか、一度別ファイルに書き出してから統合することを検討する。
    - **Update Caption**: 必要であれば、本文末尾等の `[caption]` タグ内のテキストも更新する。
- [ ] **Update Documentation (Critical)**:
    - **Foreshadowing**: リライトにより伏線の状態が変化した場合、**必ず** `docs/foreshadowing.md` を更新する。
    - **Settings**: キャラクターの心理描写や設定に変更があった場合、**必ず** 関連ドキュメント (`docs/characters/`, `docs/world/`) を更新する。
- [ ] **Sanity Check**: 修正後の文章を読み、前後の文脈がスムーズに繋がっているか確認する。

## 5. Post-Processing (事後処理)
- [ ] **Pixiv Conversion**: **【必須】** Pixiv用フォーマットへの変換 (`.agent/tools/convert_to_pixiv.ps1`) を再実行し、公開用ファイルを最新化する。
- [ ] **Commit**: 変更内容をコミットする。
    - `git add drafts/XX.md dist/pixiv/XX.txt docs/foreshadowing.md ...` (関連ドキュメントも忘れずに含める)
    - `git commit -m "Rewrite Episode XX: [Refinement Type]"`
- [ ] **Pixiv Conversion**: **【必須】** Pixiv用フォーマットへの変換 (`.agent/tools/convert_to_pixiv.ps1`) を再実行し、公開用ファイルを最新化する。
- [ ] **Commit**: 変更内容をコミットする。
    - `git commit -m "Rewrite Episode XX: [Refinement Type]"`
