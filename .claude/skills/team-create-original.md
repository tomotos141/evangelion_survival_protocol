---
name: team-create-original
description: オリジナル作品の企画パイプライン。シードコンセプトから市場調査・題材調査・世界構築・キャラクター創造・プロット設計・Story Profile 結晶化までを行い、既存の team-write-episode パイプラインへ引き渡す。「オリジナルを企画して」「新作を作りたい」「team create original」で発動する。
---

# Original Work Creation Pipeline

オリジナル作品をゼロから企画するためのオーケストレーション手順。
リサーチ → 基盤構築 → プロット設計 → Story Profile 結晶化を経て、team-write-episode パイプラインへ引き渡す。

---

## Phase 0: Seed Intake（種の受け取り）— Team Lead

1. ユーザーからシードコンセプトを受け取る。形式は自由:
   - ログライン（「江戸時代の京都で時間ループする侍」）
   - ジャンル + テーマ（「不死の代償を描くダークファンタジー」）
   - 雰囲気（「蟲師とブレードランナーの中間」）
   - 問い（「記憶が売買できる世界で、人格とは何か」）

2. 以下を対話で確認する:
   - **スケール**: 連載（5話以上）か中編（1〜5話）か
   - **ジャンル**: メインジャンル + サブジャンルタグ
   - **ターゲット**: 読者層、投稿先プラットフォーム（Pixiv / なろう / カクヨム 等）
   - **譲れない要素**: 絶対に入れたいもの、絶対に避けたいもの

3. `new_novel_project` ワークフローを `original` タイプで実行し、プロジェクト構造を作成する

4. **Checkpoint 0**: ユーザーの承認を得てから Phase 1 へ進む

---

## Phase 1: Research（調査）— Researcher Agent ×2（並列）

**researcher** サブエージェントを **2つ並列** で起動する。

### 1a. 市場調査（Trend Research）

指示に含める情報:
- 対象ジャンルとサブジャンルタグ
- 投稿先プラットフォーム
- Author DNA のパス（`.agent/author_profile.md`）
- 「流行を追従するためではなく、読者の期待を理解した上で裏切るための調査」であることを明示

出力先: `docs/research/trend_report.md`

### 1b. 題材調査（Subject Research）

指示に含める情報:
- シードコンセプトの題材（時代、科学、文化、地理など）
- 特に五感に関わる情報（匂い、音、温度、質感）を重視する旨
- Author DNA のパス

出力先: `docs/research/subject_report.md`

両方の完了を待つ。

**Checkpoint 1**: Team Lead がリサーチ結果を統合してユーザーに提示する。方向性を確認し、必要なら軌道修正する。

---

## Phase 2: Foundation（基盤構築）— Team Lead + ユーザー対話

このフェーズは対話的かつ順序的に進める。各ステップでユーザーと会話しながら設定を固める。

### 2a. ジャンル定義と読者契約（Genre & Reader Contract）

世界を建てる前に「どんな種類の物語を語るのか」を定める。（Story Grid, Save the Cat!, Truby）

- **Content Genre**（外的: アクション / スリラー / ラブストーリー / ミステリ 等）
- **Internal Genre**（内的: 成長 / 幻滅 / 試練 / 教育 等）
- **Style / Reality / Structure Genre**: コメディ or ドラマ、リアリズム or ファンタジー、単線 or 群像
- **読者への約束**: この物語が読者に提供する**核心的体験**を一文で（例: 「不可能な選択を迫られる恐怖と、それでも選ぶ美しさ」）
- **ジャンル固有の必須場面（Obligatory Scenes）**: このジャンルの読者が「これがなければ物足りない」と感じるシーンのリスト
- **ジャンルの慣習（Conventions）**: このジャンルで読者が暗黙に期待する設定・要素のリスト（例: スリラーなら「タイムリミット」「Speech in Praise of the Villain」）
- Phase 1 の市場調査で特定された**飽和トロープ**と**未開拓ニッチ**を参照し、差別化戦略を意識する
- 決まった内容を `docs/world/genre_contract.md` に記録する

### 2b. プレミス / ログライン（Premise & Logline）

物語の核を一文に凝縮する。以降の全ステップの**一貫性検証のリトマス試験紙**になる。（Truby, Save the Cat!, Weiland）

- **ログライン**: What If + 主人公 + 対立 + Stakes を含む一文（例: 「記憶を売って生計を立てる少女が、自分の最も大切な記憶を要求されたとき、人格の定義を賭けた取引に挑む」）
- **プレミス**: ログラインを発展させ、テーマの方向性を示すもの（例: 「偽物の記憶から生まれた感情が本物かどうかを問う話」）
- ログラインには必ず**irony（アイロニー・逆説）**を含めること — Snyder の原則
- 以降の全ステップで「この決定はプレミスを支えているか？」を検証基準として使う

### 2c. 世界構築（World Building）

リサーチ結果（特に題材調査）を元に、世界の基盤を構築する。

- `docs/templates/world_building_template.md` を参照しながら対話する
- 決まった内容を `docs/world/core_rules.md` に記録する
- 必要に応じて追加ファイルを作成: `docs/world/geography.md`, `docs/world/society.md` 等
- **Sensory Palette**（感覚のパレット）は必ず定義する — Story Profile の美学の土台になる

### 2d. キャラクター創造（Character Creation）

世界が決まったら、その世界に住む人物を設計する。

- `docs/templates/character_template_generic.md` を参照しながら対話する
- 主要人物を 3〜5人設計する
- **Author DNA §1 Multiple Answers**: 各キャラクターが中心テーマに対する**異なる回答**を体現するよう設計する
- **Ghost → Lie → Want vs Need チェーン**（Weiland）:
  - **Ghost（幽霊）**: キャラクターが「嘘」を信じる原因となった過去の出来事
  - **Lie（嘘）**: Ghost のせいで信じ込んでいる誤った信念
  - **Want（欲しいもの）**: Lie に基づいて本人が自覚している目標
  - **Need（必要なもの）**: Lie を克服した先にある本当の課題
- **Character Web（キャラクター・ウェブ）**（Truby）:
  - 全キャラクターを孤立ではなく**相互関係の網**として設計する
  - 各キャラクターがテーマの**異なる変奏**を体現するマトリクスを作成する
  - 味方・敵対者・偽りの味方 — 全員がテーマの異なる側面を照らすよう配置する
  - 関係性マトリクス: 主要キャラ間の関係の質・緊張・変化の方向を一覧化する
- 決まった内容を `docs/characters/{name}.md` に記録する
- **Character Web マトリクスは `docs/characters/_character_web.md` に記録する**

### 2e. 対立と賭け金の設計（Conflict & Stakes Design）

キャラクターの弱点が見えたら、そこを突く対立構造を設計する。

- `docs/templates/conflict_template.md` を参照しながら対話する
- 対立が主人公の**具体的な弱み**（Ghost/Lie）を突くように設計する
- **Author DNA §1 The Weight of Costs**: 勝利の代償を明確にする
- **Stakes の階層**（Dramatica）:
  - **個人的 Stakes**: 主人公個人が失うもの（命、記憶、大切な人）
  - **関係的 Stakes**: 人間関係に生じる損害（信頼の崩壊、関係の断絶）
  - **社会的 Stakes**: 世界やコミュニティへの影響（秩序の崩壊、組織の壊滅）
  - **存在論的 Stakes**: テーマレベルの賭け（「この選択が正しければ人間は〇〇であり、間違いなら〇〇である」）
- **失敗の帰結（Consequences）**: 主人公が失敗したら何が起きるか
- **成功の代償（Costs）**: 主人公が成功しても何を失うか
- 決まった内容を `docs/world/conflict.md` または `docs/world/threats/{name}.md` に記録する

### 2f. テーマの精緻化（Theme Refinement）

Phase 0 のシードテーマを、キャラクター設計の結果と照合して磨き直す。

- 各キャラクターの「テーマへの回答」（character_template §4）が、テーマの異なる側面を照らしているか検証する
- テーマが抽象的すぎれば具体化し、狭すぎれば拡張する
- **最終的なテーマ文を一文で確定する**（例: 「偽物の記憶から生まれた感情は本物か？」）
- **Designing Principle**（Truby）: テーマを体現する**構造的仕掛け**を言語化する（例: 「記憶を売るたびに人格が変わる主人公を通して、同一性の喪失を読者に追体験させる」）

### 2g. 語りの設計（Narrative Voice Design）

Writer エージェントの文体を決定する最重要ステップ。

- **視点**: 誰が語るか（主人公 / 観察者 / 神の視点）
- **人称**: 一人称（僕 / 私 / 俺）/ 三人称限定視点 / 三人称全知
- **時制**: 過去形 / 現在形
- **文体レジスター**: ハードボイルド / 叙情的 / 軽妙 / ドライ / 詩的 等
- **語り手の特徴**: 口語崩れの度合い、内省の深さ、信頼できる語り手かどうか
- Phase 2c の Sensory Palette と組み合わせて、この作品の**文章の手触り**を言語化する
- **Tone Statement**: この物語の感情的温度を一文で宣言する（例: 「静かな諦念の底にかすかな温もりが残る」）— Writer と Editor の判断基準を揃えるために必須

### 2h. 仮題の決定（Working Title）

プロジェクトの求心力となる仮タイトルを決める。

- シードコンセプト、テーマ、世界の質感から導出する
- 最終タイトルでなくてよい。方向性を象徴する言葉であればよい

**Checkpoint 2**（最重要）: ジャンル契約・プレミス・世界・キャラクター（ウェブ）・対立（ステークス）・テーマ・語り・仮題をユーザーが承認する。ここから先の全てはこの基盤の上に構築されるため、慎重に確認する。

---

## Phase 3: Plot Architecture（プロット設計）— Team Lead + ユーザー対話

### 連載（5話以上）の場合

- 幕構成を設計する（典型的には 3〜4幕）
- 各幕をエピソードに分割し、一行サマリーを書く
- 鍵となるターニングポイント、ミッドポイントリバーサル、クライマックスを特定する
- 伏線スレッドを設計する
- 出力:
  - `docs/overall_plot.md`（全体プロット）
  - `docs/foreshadowing.md`（伏線管理表）
  - `docs/episodes/ep01_title.md`（第1話のエピソードデザイン）

### 中編（1〜5話）の場合

- Beginning / Middle / End の構造を設計する
- 複数話の場合はエピソード境界を定義する
- 出力:
  - `docs/overall_plot.md`（軽量版）

**Note**: プロット承認前に `audit-design` スキルを実行し、プロット構造が Author DNA・好み変遷と合致しているか検証できる。

**Checkpoint 3**: プロット構造をユーザーが承認する。

---

## Phase 4: Story Profile Crystallization（結晶化）— Team Lead

Phase 2〜3 の全成果物を `.agent/profiles/{project_name}.md` に凝縮する。

**Note**: `scaffold-story-profile` スキルの構成ルールに従う。デザインドキュメントが完成している場合は `team-scaffold-project` で Phase 2〜4 を一括実行できる。

既にワークフローで作成された雛形を上書きし、以下のセクションを埋める:

1. **ジャンルと読者契約** — Phase 2a のジャンル定義・読者への約束・必須場面リストを転記する
2. **プレミス** — Phase 2b のログライン + プレミスを転記する
3. **作品の美学** — Phase 2c の Sensory Palette + 仮題から導出。色彩・音・温度・質感で世界の手触りを定義する
4. **トーンと語り** — Phase 2g の語り設計をそのまま転記。視点・人称・時制・文体レジスター・Tone Statement・`skill_ref` を確定する
5. **テーマ** — Phase 2f で精緻化されたテーマ文 + Designing Principle を記載。各キャラクターの回答を併記する
6. **世界設定** — `docs/world/` への参照リンク付きで要約
7. **キャラクター・ダイナミクス** — Character Web マトリクス・Ghost/Lie 構造・関係性の力学を要約、`docs/characters/` を参照
8. **禁止事項** — Author DNA §7 の共通禁止事項 + 本作固有の禁止事項

**Note**: Story Profile 承認前に `audit-design` スキルを実行し、結晶化された Profile が Author DNA・好み変遷と矛盾していないか最終検証できる。

**Checkpoint 4**: Story Profile をユーザーが承認する。

---

## Phase 5: Handoff（引き渡し）— Team Lead

1. 作成された全成果物の一覧を提示する:
   - リサーチドキュメント（`docs/research/`）
   - 世界設定ドキュメント（`docs/world/`）
   - キャラクタードキュメント（`docs/characters/`）
   - プロットドキュメント（`docs/overall_plot.md`）
   - 伏線管理表（`docs/foreshadowing.md`）— 連載の場合
   - Story Profile（`.agent/profiles/{project_name}.md`）
   - 第1話エピソードデザイン（`docs/episodes/ep01_title.md`）— 連載の場合

2. 次のステップを案内する:
   - デザインドキュメントが完成済みの場合: `team-scaffold-project` で基盤ファイルを一括構築
   - 基盤ファイルが揃っている場合: `team-write-episode` パイプラインで執筆を開始

3. ユーザーが希望すればコミットを実行する

---

## 設計方針メモ

**Phase 2 を対話で進める理由**:
世界構築とキャラクター創造はユーザーとの密な対話が必要。リサーチ（自律的に完了可能）や執筆（スペックに沿って実行可能）とは異なり、基盤構築は根本的に「共同創作」である。

**Phase 1 が並列、Phase 2 が順序的な理由**:
市場調査と題材調査は独立した作業。だが Phase 2 内は依存関係がある: ジャンル定義（物語の種類を先に決める）→プレミス（核を一文で凝縮）→世界（ジャンルとプレミスが方向を決める）→キャラ（世界に住み、Ghost/Lie がテーマと絡む）→対立（キャラの Ghost/Lie を突く + Stakes 階層）→テーマ精緻化（キャラの回答で検証 + Designing Principle）→語り（テーマと世界の質感が決まって初めて文体が選べる + Tone Statement）→仮題（全てを象徴する言葉）。

**5つのチェックポイントがある理由**:
オリジナル作品は土台の間違いが全話に波及する。各段階でユーザーの承認を取ることで、大規模な手戻りを防ぐ。
