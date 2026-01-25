---
description: 小説執筆の標準ワークフロー（構想から初稿執筆、Git管理まで）
---

# Feature Development Workflow - Novel Writing

このワークフローは、新しいエピソードや設定を執筆する際の一連のプロセスを定義したものです。
各ステップで必ず「著者の作家性（Hardboiled, Cynical）」に沿っているかを確認してください。

## 1. Preparation & Concept (準備・構想)
- [ ] **Load Skills**: 以下のスキルファイルを必ず `view_file` で読み込み、内容を把握する。
    - `.agent/skills/story_editor/SKILL.md` (文体・演出チェック用)
    - `.agent/skills/novel_writing/SKILL.md` (執筆技法用)
- [ ] **Define Goal**: 書こうとしている章やシーンの目的を明確にする。
    - 誰の視点か？
    - 達成すべき感情的なゴールは（サスペンス、虚無感、安堵など）？
- [ ] **Review Settings**: 既存の設定ファイル (`docs/world/`, `docs/characters/`) を確認し、矛盾がないかチェックする。

## 2. Drafting (執筆)
- [ ] **Plotting**: `novel_writing` スキルを活用し、プロット（構成案）を作成してユーザーの合意を得る。
- [ ] **Drafting**: `drafts/` ディレクトリに新しいファイルを作成し、執筆する。
    - ファイル名規則: `XX_title.md` (例: `02_hell_is_here.md`)
    - **Rule**: 「Show, Don't Tell」、五感の描写、メタ発言の禁止を徹底する。

## 3. Review & Quality Check (品質・整合性チェック) - CRITICAL STEP
このステップをスキップしてはいけません。
- [ ] **Run Story Editor Check**: `story_editor` スキルの手順に従い、ドラフトを自己レビューする。
    - [ ] 文体はハードボイルドでドライか？（幼稚な表現がないか）
    - [ ] 固有名詞や未来知識の不自然な使用はないか？
    - [ ] 「予定調和」になっていないか？（サスペンスや不穏さはあるか）
- [ ] **Propose Fixes**: 問題点があれば修正案を提示し、ユーザーの承認を得てから修正を実行する。

## 4. Version Control (バージョン管理)
- [ ] **Commit**: ドラフト完成版をコミットする。
    - `git add .`
    - `git commit -m "Draft Episode XX: Title"`

## 5. Publishing (公開準備)
- [ ] **Convert Format**: 完成した原稿をPixiv用のフォーマットに変換する。
    - Pixiv用: `dist/pixiv/XX_title_pixiv.txt`
        - ルビ: `[[rb:漢字 > よみがな]]`
        - 改ページ: `[newpage]`
        - 章タイトル: `[chapter: ...]`
- [ ] **Final Check**: 変換後のファイルで、禁止ワード（旧設定の名残など）が入っていないか最終チェックする。

## 6. Cleanup (終了処理)
- [ ] **Commit**: 公開用ファイルも含めてすべてコミットする。
- [ ] **Next Steps**: 次に書くべきシーンや、明らかになった設定の穴をメモする。
