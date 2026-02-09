---
description: 既存のエピソードを多角的な視点（整合性、文体、伏線、描写密度）で診断し、リライトするためのワークフロー
---

# Episode Rewrite & Polish Workflow

既存の原稿（Draft）に対して、設定の整合性、作家性、伏線管理、文章品質などのチェックを一括で行い、リライトによって完成度を高めるための手順。

## 1. Preparation (準備)

- [ ] **Select Target**: リライト対象のファイルパス（`drafts/XX_title.md`）を特定する。
- [ ] **Set Focus**: リライトで重視するポイントをユーザーに確認する。
    - **Logic Fix**: 設定矛盾や時系列の修正
    - **Style Polish**: 文体の統一、五感描写の強化
    - **Foreshadowing**: 伏線の追加・整理
    - **Full Rewrite**: プロットごと書き直し（エピソードデザインから再構築）
    - **All**: 上記すべて（推奨）
- [ ] **Read Current Draft**: `Read` ツールで対象ファイルの全文を読み込む。
- [ ] **Read Related Context**: 直前・直後のエピソード、`docs/foreshadowing.md`、関連する設定ファイルを確認する。

## 2. Comprehensive Diagnostic (総合診断)

以下の5つの観点で分析を行う。

- [ ] **Check 1: Logic & Consistency** (`consistency_check` skill)
    - 設定資料 (`docs/`) との矛盾はないか？
    - キャラクターの言動は性格設定や直前の文脈と合致しているか？
    - 時系列や事実関係に誤りはないか？
- [ ] **Check 2: Foreshadowing & Mysteries** (Ref: `docs/foreshadowing.md`)
    - 未回収の伏線（🔴/🟡）が適切に扱われているか？
    - 意図しない「矛盾」が「未回収の伏線」に見えていないか？
    - 新たに伏線として登録すべき要素はあるか？
- [ ] **Check 3: Author Style & Tone** (`author_style_check` skill)
    - "Hardboiled / Cynical" な態度は維持されているか？
    - 不要な感傷、説明過多なセリフ、甘すぎる展開はないか？
    - **Episode Number Check**: `Ep.\d` パターンが地の文に残っていないか？ → 作中表現に置換
- [ ] **Check 4: Sensory Density** (`story_editor` skill)
    - 五感描写は十分か？（視覚・聴覚・嗅覚・触覚・内部感覚）
    - 情景描写は解像度が高く、かつ簡潔か？
- [ ] **Check 4.5: Natural Prose (AI臭の排除)**
    - 同じ構文パターンが3回以上連続していないか？ 短文と長文の緩急があるか？
    - 抽象語だけで押し切っている箇所はないか？ 動詞中心の具体表現に置き換えられるか？
    - 同義語の言い換え連打になっていないか？
    - 括弧・コロン・スラッシュが過剰でないか？ 文脈に溶かせるか？
    - 前置き宣言・安全クッション・締めの定型句が混入していないか？
- [ ] **Check 5: Caption Review (必須)**
    - ドラフト末尾に `[caption]...[/caption]` ブロックが存在するか？ なければ新規作成。
    - キャプションの内容がリライト後の本文と矛盾していないか？

## 3. Proposal (修正案の提示)

- [ ] **Report**: 問題点と修正案（Before/After）をリストアップしてユーザーに提示する。
- [ ] **Approval**: どの修正を適用するか決定する。

## 4. Execution (リライト実行)

- [ ] **Rewrite Draft**: `Edit` ツールで対象箇所を修正する。
    - 大規模な書き直しの場合は `Write` ツールで全体を再生成する。
    - キャプションの更新が必要な場合は `[caption]` ブロックも修正する。
- [ ] **Update Documentation**:
    - `docs/foreshadowing.md` — 伏線の状態変化を反映
    - `docs/characters/`, `docs/world/` — 設定変更があれば更新
- [ ] **Sanity Check**: 修正後の文章を読み、前後の文脈がスムーズに繋がっているか確認する。

## 5. Post-Processing (事後処理)

- [ ] **Regenerate Pixiv Version**: ドラフトの変更を `dist/pixiv/XX_title_pixiv.txt` に反映する。
    - 部分修正の場合: `Edit` ツールでPixiv版の該当箇所も同じ修正を適用する。
    - 全面書き直しの場合: Pixiv版を再生成する（変換ルールは `write_novel_episode.md` §4 を参照）。
- [ ] **Update Caption**: `dist/pixiv/caption.txt` の該当エピソードのキャプションも必要に応じて更新する。
- [ ] **Meta Reference Check**: ドラフト・Pixiv版両方に対して `Ep.\d` の残存チェックを行う。
    ```
    Grep pattern="Ep\.\d" path="drafts/XX_title.md"
    Grep pattern="Ep\.\d" path="dist/pixiv/XX_title_pixiv.txt"
    ```
- [ ] **Commit** (ユーザーの指示があった場合のみ):
    ```
    git add drafts/XX.md dist/pixiv/XX_pixiv.txt dist/pixiv/caption.txt docs/...
    git commit -m "Rewrite Episode XX: [Refinement Type]"
    ```
