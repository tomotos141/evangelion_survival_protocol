---
description: 小説執筆の標準ワークフロー（構想から初稿執筆、Git管理まで）
---

# Feature Development Workflow - Novel Writing

このワークフローは、新しいエピソードや設定を執筆する際の一連のプロセスを定義したものです。
各ステップで必ず「著者の作家性（Hardboiled, Cynical）」に沿っているかを確認してください。

## 0. Project Environment (環境確認)
- [ ] **Identify Project**: 現在作業中のプロジェクトディレクトリ（例：`projects/angel_return/`）を確認し、以降の操作はそのディレクトリ内で行う。
- [ ] **Set Context**: 以下の手順における `docs/` や `drafts/` はすべてプロジェクトディレクトリ内を指す。
- [ ] **Load Skills**: 以下のスキルファイルを必ず `view_file` で読み込み、内容を把握する。
    - `.agent/skills/consistency_check/SKILL.md` (整合性・事実確認用)
    - `.agent/skills/story_editor/SKILL.md` (文体・演出チェック用)
    - `.agent/skills/author_style_check/SKILL.md` (著者の美学チェック用)
    - `.agent/skills/novel_writing/SKILL.md` (執筆技法用)
- [ ] **Define Goal**: 書こうとしている章やシーンの目的を明確にする。
    - 誰の視点か？
    - 達成すべき感情的なゴールは（サスペンス、虚無感、安堵など）？
- [ ] **Review Settings**: 既存の設定ファイル (`docs/world/`, `docs/characters/`) を確認し、矛盾がないかチェックする。
    - 特に **`docs/world/hard_mode_guidelines.md`** および **`docs/world/eva_abilities.md`** を参照し、当該エピソードに登場する使徒やエヴァの能力・形態が「最新の状態」であるか確認する。
- [ ] **Define New Threat (Angels)**: **【重要】** 毎回、そのエピソードに登場する使徒（または脅威）の新規設定ファイルを作成する。
    - **Template**: `docs/templates/angel_template.md` を使用すること。
    - **Policy**: 原作の使徒をそのまま出さず、必ず「オリジナル変異体」または「完全新規使徒」として定義する。
    - 保存先: `docs/world/angel_[name].md`
- [ ] **Context Check**: 直前のエピソードのラストシーン（またはあらすじ）を確認し、**キャラクターの感情状態（Mood）や身体状態（疲労、怪我）** が正しく引き継がれているかメモする。

## 2. Drafting (執筆)
- [ ] **Plotting**: `novel_writing` スキルを活用し、プロット（構成案）を作成する。
    - **【重要】設定の不足確認**: プロット段階で、未定義のキャラクター、場所、ギミックが登場する場合は、**執筆前に設定資料 (`docs/`) の新規作成や追記を提案する**こと。
    - **Pre-Draft Consistency Check**: 作成したプロットが、既存の設定や直前の展開と矛盾していないか簡易チェックする。
- [ ] **Get User Approval**: 以下の要素を明示して、ユーザーにプロットの承認を求める。
    - **今回のテーマ**: 何を描くエピソードか。
    - **前回からの継承**: 主人公の心理状態はどうなっているか。
    - **新しい要素**: 新登場のキャラや設定。
- [ ] **Drafting**: `drafts/` ディレクトリに新しいファイルを作成し、執筆する。
    - ファイル名規則: `XX_title.md` (例: `02_hell_is_here.md`)
    - **Rule: Density of Senses**: 「Show, Don't Tell」を徹底し、最低でも「1シーンにつき五感のうち3つ以上の描写」を組み込む。特に本作の美学である「生理的嫌悪感」「美しい破滅」の描写を一行で済ませない。
    - **Rule: Anti-Scripting**: シナリオ的な「Scene X: 場所/人物」といった見出しに頼りすぎない。地の文によるシームレスな転換と、情景描写を重視し、1話あたりの文章量を200〜250行以上に保つ。
    - **Rule**: メタ発言の禁止を徹底する。

## 3. Review & Quality Check (品質・整合性チェック) - CRITICAL STEP
このステップをスキップしてはいけません。
- [ ] **Run Story Editor Check**: `story_editor` スキルの手順に従い、ドラフトを自己レビューする。
    - [ ] 文体はハードボイルドでドライか？（幼稚な表現がないか）
    - [ ] **Density Check**: 描写が不足し、あらすじ（プロット消化）になっていないか？ 特にキャラクターの心理的な「ため（葛藤、迷い）」や「生理的な反応」が詳細に描かれているか？
    - [ ] 固有名詞や未来知識の不自然な使用はないか？
    - [ ] 「予定調和」になっていないか？（サスペンスや不穏さはあるか）
- [ ] **Run Consistency Check**: `consistency_check` スキルを使用し、事実関係と設定の整合性を厳密に検証する。
    - [ ] **Fact Check**: 年齢（引き算は合っているか）、日付、経過時間（「14年ぶり」ではなく「11年ぶり」など）が正しいか。
    - [ ] **Character Voice**: シンジの独白が「冷徹な工作員」になっておらず、「PTSDサバイバー」として描かれているか。
    - [ ] **Setting**: 魔法や技術のルール違反がないか。
    - **Eva Abilities**: 本文中のエヴァの挙動が `docs/world/eva_abilities.md` で定義された固有能力や変異段階に基づいているか。
- [ ] **Run Author Style Check**: `author_style_check` スキルを使用し、著者の嗜好（美学）に合致しているか判定する。
    - [ ] "Beautiful Ruin"（静寂、廃墟、終わりの予感）の雰囲気はあるか？
    - [ ] "Competence & Mask"（有能な演技、腹の探り合い）が魅力的に描かれているか？
    - [ ] 不要な「甘さ」や「ご都合主義」が混入していないか？
- [ ] **Run Reader Engagement Check**: `story_editor` スキルの「没入度チェック」を行い、以下の点を確認する。
    - [ ] 章のラストは「続きを読みたくなる」引き（クリフハンガー等）になっているか？
    - [ ] 期待を裏切るツイストや、不穏さを残す演出が含まれているか？
- [ ] **Propose Fixes**: 問題点があれば修正案を提示し、ユーザーの承認を得てから修正を実行する。

## 4. Version Control (バージョン管理)
- [ ] **Commit**: ドラフト完成版をコミットする。
    - `git add .`
    - `git commit -m "Draft Episode XX: Title"`

## 5. Publishing (公開準備)
- [ ] **Convert Format**: 完成した原稿をPixiv用のフォーマットに変換する。
    - **Agent Action**: 以下のPowerShellコマンドを実行して、`dist/pixiv/` にテキストファイルを生成する。
    ```powershell
    powershell -ExecutionPolicy Bypass -File .agent/tools/convert_to_pixiv.ps1 -InputPath "drafts/XX_title.md" -OutputPath "dist/pixiv/XX_title_pixiv.txt"
    ```
    - Pixiv用: `dist/pixiv/XX_title_pixiv.txt`

## 6. Cleanup (終了処理)
- [ ] **Update Settings**: **【重要】** 今回のエピソードで発生したキャラクターや機体の変化を記録する。
    - `docs/characters/` 内の各ファイルの **`8. Status Evolution Log`** に追記。
    - **`docs/world/eva_abilities.md`**: エヴァの能力が進化したり、新しい形態（変異段階）が発現した場合は、その内容を追記・更新する。
- [ ] **Commit**: 公開用ファイルおよび更新した設定ファイルも含めてすべてコミットする。
- [ ] **Next Steps**: 次に書くべきシーンや、明らかになった設定の穴をメモする。
