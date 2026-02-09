---
description: 完成したエピソードの最終チェック、Pixiv変換、キャプション更新、コミットを一括実行するワークフロー
---

# Finalize Episode Workflow

執筆が完了しユーザーのOKが出たエピソードに対して、最終チェック → Pixiv版生成 → キャプション更新 → コミットを行う。

## Usage

```text
/finalize_episode [episode_file_path] [commit_message]
```

Example: `/finalize_episode projects/angel_return/drafts/06_thunderbolt.md "Add Episode 6: Thunderbolt"`

## Steps

### 1. Final Checks (最終チェック)

- [ ] `Read` ツールでドラフト全文を読み込む。
- [ ] `consistency_check` スキルの主要項目（Character Voice, Hard Mode Rule）を再確認する。
- [ ] **Episode Number Check**: `Grep` で `Ep.\d` パターンが地の文に残っていないか確認する。
- [ ] **Natural Prose Check**: 構文の単調さ、抽象語の空回り、同義語連打、括弧・記号の過剰使用がないか最終確認する。
- [ ] ドラフト末尾に `[caption]...[/caption]` ブロックが存在するか確認する。なければ停止して作成を促す。
- [ ] 問題があればユーザーに報告し、修正を促す。

### 2. Generate Pixiv Version (フォーマット変換)

ドラフトを元に、Pixiv投稿用のプレーンテキストを**手動で**生成する。

- **出力先**: `dist/pixiv/XX_title_pixiv.txt`
- **エンコーディング**: UTF-8 with BOM（ファイル先頭に `﻿` を付与）
- **変換ルール**:

| Draft (Markdown) | Pixiv (Plain Text) |
| --- | --- |
| `# タイトル` | 削除 |
| `***` | `　　　　　　　　　　　＊＊＊`（全角スペース11個＋全角＊3個） |
| `**太字**` | `——太字——` または強調なし |
| `——` (ダッシュ) | `――`（全角ダッシュ） |
| `[caption]...[/caption]` | 削除（Pixiv版には含めない） |

- **注意事項**:
    - 丸括弧 `（）` による心理描写はそのまま残す（ドラフトノートと混同しない）
    - 改行は原文をそのまま維持する
    - `[newpage]` や `[chapter:]` タグは使用しない

### 3. Update Caption (キャプション更新)

- [ ] `dist/pixiv/caption.txt` を `Read` で読み込み、該当エピソードのキャプションを追記・更新する。
- **フォーマット**:

```text
--------------------------------------------------

[第X話キャプション]
タイトル：(日本語タイトル) (English Title)

(あらすじ: 3〜5行、読者のフックとなる内容)

「(印象的なセリフの抜粋)」
```

- キャプションの内容はドラフト末尾の `[caption]` ブロックを元にする。

### 4. Final Validation (最終検証)

- [ ] Pixiv版に対して `Ep.\d` の残存チェックを行う。
- [ ] ドラフトとPixiv版の内容が一致していることを確認する（シーン数、キーセリフ）。

### 5. Git Commit (コミット)

ユーザーの指示があった場合のみ実行する。

```bash
git add drafts/XX_title.md dist/pixiv/XX_title_pixiv.txt dist/pixiv/caption.txt
git commit -m "[commit_message]"
```
