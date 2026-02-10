---
description: 小説執筆の標準ワークフロー（構想から初稿執筆、公開準備まで）。チーム体制を使う場合は `.claude/skills/team-write-episode.md` を参照。
---

# Episode Writing Workflow

新しいエピソードを構想・執筆・公開するための標準ワークフロー。
各ステップで `author_profile.md` の美学に沿っているかを常に確認すること。

> **チーム体制との関係**: `.claude/skills/team-write-episode.md` が Writer/Editor/Proofreader/Publisher の4エージェントを自動でオーケストレーションする上位版。本ワークフローは手動パスとして残す。

## 0. Preparation (環境・前提確認)

- [ ] **Identify Project**: プロジェクトディレクトリ（例：`projects/angel_return/`）を特定する。以降 `docs/`, `drafts/`, `dist/` はすべてこのディレクトリ内を指す。
- [ ] **Review Context**: 以下の資料を `Read` ツールで確認する。
    - `docs/overall_plot_v2.md` — 全体プロットと進捗
    - `docs/foreshadowing.md` — 未回収の伏線（🔴/🟡）
    - 直前エピソードのドラフト末尾 — キャラの感情・身体状態の引き継ぎ
    - `docs/world/hard_mode_guidelines.md`, `docs/world/eva_abilities.md` — 使徒・エヴァの最新設定
    - `.agent/author_profile.md` — 著者の美学と好み変遷（v2）
- [ ] **Define Goal**: 今回のエピソードで達成すべきことを明確にする。
    - 誰の視点か？（基本：一人称シンジ/僕。他キャラPOVは「後から聞いた話」でフレーミング）
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
        - **他キャラPOV**: 「後から聞いた」「後日、〇〇がぽつりと漏らした」等のフレーミングでシンジ一人称に収める。深い内面描写は避け、伝聞形式で簡潔に
        - **Density of Senses**: 1シーンにつき五感のうち3つ以上の描写を組み込む
        - **Anti-Scripting**: 「Scene X: 場所/人物」のような見出しに頼らず、地の文でシームレスに転換する
        - **メタ発言禁止（CRITICAL）**: `Ep.X` 参照は厳禁。`あの夜`、`ラミエル戦`、`あの白い部屋` 等の作中表現で参照する。「この物語」等のメタ表現も禁止
        - **Show, Don't Tell**: 感情を直接語らず、身体反応・行動・五感描写で表現する
        - **Natural Prose（AI臭の排除）**: 短い文と長い文を混ぜてリズムに変化をつける。抽象語だけで押し切らず動詞中心で書く。同義語連打・括弧への逃げ・前置き宣言・安全クッションは使わない
        - **震え/揺れ表現の管理**: 「震えていた」「揺れていた」の同一エピソード内での重複を避ける。「掠れていた」「強張っていた」「硬直していた」等のバリエーションを使う
        - **括弧モノローグ禁止**: `（……ここから始める）` のような括弧書きのモノローグは使わない。地の文に溶かす
        - **テーマの解説禁止**: 作品のテーマや登場人物の行動の意味を地の文で解説しない。描写で示す

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
    - [ ] 「脆さと沈黙」「身体的・沈黙的・余白重視」の美学が反映されているか？
- [ ] **Reader Engagement Check**:
    - [ ] 章のラストに「続きを読みたくなる」引きがあるか？
    - [ ] 期待を裏切るツイストや不穏さが含まれているか？

## 4. Pixiv Conversion (公開用変換)

- [ ] **Generate Pixiv Version**: ドラフトを元にPixiv投稿用テキストを生成する。
    - **出力先**: `dist/pixiv/##_title_pixiv.txt`
    - **変換ルール**:
        | Draft (Markdown) | Pixiv (Plain Text) |
        |---|---|
        | `# タイトル` | 削除（タイトルなし） |
        | `***` | `　　　　　　　　　　　＊＊＊` （全角スペース11個＋全角アスタリスク3個） |
        | `**太字**` | 太字マーカーを削除（テキストのみ残す） |
        | `[caption]...[/caption]` | **削除**（Pixiv版には含めない） |
    - **エンコーディング**: UTF-8 **with BOM** (`﻿` をファイル先頭に付与)
    - **改行**: 原文の改行をそのまま維持
    - **末尾**: 本文末尾に `続く` がない場合は追加する（最終話を除く）
    - **変換スクリプト例** (Python):
        ```python
        import re
        separator = '\u3000' * 11 + '\uff0a' * 3
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'^# [^\n]*\n\n', '', content)           # タイトル削除
        content = re.sub(r'\n\[caption\][\s\S]*', '', content)     # caption削除
        content = content.rstrip()
        if not content.endswith('続く'):
            content = content + '\n\n続く\n'
        content = content.replace('***', separator)                 # シーン区切り変換
        content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)      # 太字マーカー削除
        with open(dst, 'w', encoding='utf-8-sig') as f:
            f.write(content)
        ```

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
