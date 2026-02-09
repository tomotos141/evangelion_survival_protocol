---
description: 小説執筆の標準ワークフロー（構想から初稿執筆、公開準備まで）
---

# Episode Writing Workflow

新しいエピソードを構想・執筆・公開するための標準ワークフロー。
各ステップで「著者の作家性（Hardboiled, Cynical）」に沿っているかを常に確認すること。

## 0. Preparation (環境・前提確認)

- [ ] **Identify Project**: プロジェクトディレクトリ（例：`projects/angel_return/`）を特定する。以降 `docs/`, `drafts/`, `dist/` はすべてこのディレクトリ内を指す。
- [ ] **Review Context**: 以下の資料を `Read` ツールで確認する。
    - `docs/overall_plot_v2.md` — 全体プロットと進捗
    - `docs/foreshadowing.md` — 未回収の伏線（🔴/🟡）
    - 直前エピソードのドラフト末尾 — キャラの感情・身体状態の引き継ぎ
    - `docs/world/hard_mode_guidelines.md`, `docs/world/eva_abilities.md` — 使徒・エヴァの最新設定
- [ ] **Define Goal**: 今回のエピソードで達成すべきことを明確にする。
    - 誰の視点か？（基本：一人称シンジ/僕）
    - 感情的なゴール（サスペンス、虚無感、安堵、etc.）
    - 回収する伏線、新規に仕込む伏線

## 1. Episode Design (エピソードデザイン)

- [ ] **Check Existing Design**: `docs/episodes/ep##_title.md` が既に存在するか確認する。
- [ ] **Create/Update Design**: シーン構成を設計し、デザインファイルを作成する。
    - **保存先**: `docs/episodes/ep##_english_title.md`
    - **内容**: シーン一覧（場所・登場人物・目的）、伏線計画、キーとなるセリフ案
    - **設定不足の確認**: 未定義の使徒・ギミック・キャラがあれば、`docs/world/` に設定ファイルを先に作成する。
- [ ] **Get User Approval**: デザインをユーザーに提示し、承認を得る。
    - 提示すべき項目: テーマ、前回からの継承、伏線計画、新要素

## 2. Drafting (執筆)

- [ ] **Write Draft**: `drafts/` にファイルを作成し、本文を執筆する。
    - **ファイル名規則**: `##_english_title.md`（例: `06_thunderbolt.md`）
    - **書式**:
        - 冒頭: `# エピソードタイトル`
        - シーン区切り: `***`
        - 末尾: `[caption]...[/caption]` ブロック（キャプション）
    - **執筆ルール**:
        - **一人称・過去形**: シンジ視点、「僕」語り
        - **Density of Senses**: 1シーンにつき五感のうち3つ以上の描写を組み込む
        - **Anti-Scripting**: 「Scene X: 場所/人物」のような見出しに頼らず、地の文でシームレスに転換する
        - **メタ発言禁止（CRITICAL）**: `Ep.X` 参照は厳禁。`あの夜`、`ラミエル戦`、`あの白い部屋` 等の作中表現で参照する
        - **Show, Don't Tell**: 感情を直接語らず、身体反応・行動・五感描写で表現する
        - **Natural Prose（AI臭の排除）**: 短い文と長い文を混ぜてリズムに変化をつける。抽象語だけで押し切らず動詞中心で書く。同義語連打・括弧への逃げ・前置き宣言・安全クッションは使わない

## 3. Quality Check (品質チェック)

**このステップをスキップしてはいけない。**

- [ ] **Story Editor Check** (`story_editor` skill):
    - [ ] 文体はハードボイルドでドライか？
    - [ ] 描写が「あらすじ」になっていないか？（Density Check）
    - [ ] 固有名詞や未来知識の不自然な使用はないか？
    - [ ] **Episode Number Check**: `Ep.\d` パターンが地の文に残っていないか？
    - [ ] 伏線は効果的に機能しているか？
    - [ ] 「予定調和」になっていないか？
    - [ ] **Natural Prose Check**: 構文の単調さ、抽象語の空回り、同義語連打、括弧・記号の過剰使用はないか？
- [ ] **Consistency Check** (`consistency_check` skill):
    - [ ] 時系列・事実関係に誤りはないか？
    - [ ] キャラの言動が直前エピソードの状態と矛盾していないか？
    - [ ] エヴァの挙動が `eva_abilities.md` の定義に基づいているか？
- [ ] **Author Style Check** (`author_style_check` skill):
    - [ ] "Beautiful Ruin" の雰囲気はあるか？
    - [ ] 不要な「甘さ」「ご都合主義」が混入していないか？
- [ ] **Reader Engagement Check**:
    - [ ] 章のラストに「続きを読みたくなる」引きがあるか？
    - [ ] 期待を裏切るツイストや不穏さが含まれているか？

## 4. Pixiv Conversion (公開用変換)

- [ ] **Generate Pixiv Version**: ドラフトを元にPixiv投稿用テキストを**手動で**生成する。
    - **出力先**: `dist/pixiv/##_title_pixiv.txt`
    - **変換ルール**:
        | Draft (Markdown) | Pixiv (Plain Text) |
        |---|---|
        | `# タイトル` | 削除（タイトルなし） |
        | `***` | `　　　　　　　　　　　＊＊＊` （全角スペース11個＋全角アスタリスク3個） |
        | `**太字**` | `——太字——` または強調なし |
        | `——` (ダッシュ) | `――`（全角ダッシュ） |
        | `[caption]...[/caption]` | **削除**（Pixiv版には含めない） |
    - **エンコーディング**: UTF-8 **with BOM** (`﻿` をファイル先頭に付与)
    - **改行**: 原文の改行をそのまま維持

- [ ] **Update Caption**: `dist/pixiv/caption.txt` を更新する。
    - **フォーマット**:
        ```
        --------------------------------------------------

        [第X話キャプション]
        タイトル：(日本語タイトル) (English Title)

        (あらすじ: 3〜5行、読者のフックとなる内容)

        「(印象的なセリフの抜粋)」
        ```

## 5. Documentation Update (ドキュメント更新)

- [ ] **Update Plot**: `docs/overall_plot_v2.md` にエピソード概要とリンクを追記する。
    - `※詳細: [ep##_title.md](./episodes/ep##_title.md)`
- [ ] **Update Foreshadowing**: `docs/foreshadowing.md` を更新する。
    - 新規の謎 → `🔴 Unresolved` で追加
    - 既存伏線に進展 → `🟡 In Progress` に更新
    - 回収済み → `🟢 Resolved` に変更
- [ ] **Update Settings**: キャラ・機体の変化があれば `docs/characters/`, `docs/world/eva_abilities.md` を更新する。

## 6. Final Validation & Commit

- [ ] **Meta Reference Check**: 全出力ファイルに対して `Ep.\d` パターンの grep を実行し、残存がないことを確認する。
    ```
    Grep pattern="Ep\.\d" path="drafts/##_title.md"
    Grep pattern="Ep\.\d" path="dist/pixiv/##_title_pixiv.txt"
    ```
- [ ] **Commit** (ユーザーの指示があった場合のみ):
    ```
    git add drafts/##.md dist/pixiv/##_pixiv.txt dist/pixiv/caption.txt docs/...
    git commit -m "Add Episode ##: Title"
    ```
