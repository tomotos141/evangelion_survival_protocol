---
description: 小説執筆の標準ワークフロー（構想から初稿執筆、Git管理まで）
---

# Feature Development Workflow - Novel Writing

このワークフローは、新しいエピソードや設定を執筆する際の一連のプロセスを定義したものです。

## 1. Preparation & Concept (準備・構想)
- [ ] **Define Goal**: 書こうとしている章やシーンの目的を明確にする。
    - 誰の視点か？
    - 物語のどの部分か（導入、展開、結末）？
    - 達成すべき感情的なゴールは？
- [ ] **Review Settings**: 既存の設定ファイル (`docs/world/`, `docs/characters/`) を確認し、矛盾がないかチェックする。
- [ ] **Create/Update Settings**: 必要であれば、新しいキャラクターや設定をMarkdownファイルに追加・更新する。

## 2. Drafting (執筆)
- [ ] **Brainstorming**: 必要なら `novel_writing` スキルを使って、プロットやシーンのアイデア出しを行う。
- [ ] **Drafting**: `drafts/` ディレクトリに新しいファイルを作成し、執筆する。
    - ファイル名規則: `XX_title.md` (例: `02_hell_is_here.md`)
    - 執筆中は「五感の描写」「Show, Don't Tell」を意識する。

## 3. Review & Consistency Check (レビュー・整合性チェック)
- [ ] **Check Consistency**: `consistency_check` スキルを使用し、執筆したドラフトが設定と整合しているかを確認する。
    - キャラクターの口調
    - 世界観のルール（能力、技術など）
    - 前後の文脈
- [ ] **Refine**: 指摘事項に基づいて修正を行う。

## 4. Version Control (バージョン管理)
- [ ] **Branching**: 新しいエピソード用のブランチを作成する。
    - `git checkout -b episode-XX`
- [ ] **Commit**: 作業内容をコミットする。
    - `git add .`
    - `git commit -m "Draft Episode XX: Title"`
// turbo
- [ ] **Push/Log**: 必要に応じてリモートへプッシュ、またはログを確認して保存状態を確定する。

## 5. Publishing (公開準備)
- [ ] **Convert Format**: 完成した原稿を投稿サイト（Pixiv/ハーメルン）用のフォーマットに変換する。
    - ルビ変換: `[[rb:漢字 > よみがな]]` (Pixiv) / `|漢字《よみがな》` (Hameln)
    - 本文保存先: `dist/[site]/XX_title.txt`
- [ ] **Create Assets**: 必要に応じて表紙画像やキャプション（あらすじ）を作成する。
    - 表紙: `generate_image` ツールを使用
    - あらすじ: 本文の内容とタイトルに合わせて作成

## 6. Version Control & Cleanup (終了処理)
- [ ] **Commit**: 公開用ファイルも含めてすべてコミットする。
- [ ] **Next Steps**: 次に書くべきシーンや、明らかになった設定の穴をメモする。
- [ ] **Merge**: 問題なければメインブランチへマージする（任意）。
