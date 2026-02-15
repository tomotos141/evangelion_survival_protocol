# 濁刃（だくじん）Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 『濁刃』プロジェクトの基盤構築から第1話執筆完了までを実行する。

**Architecture:** デザインドキュメント (`docs/plans/2026-02-15-battousai-design.md`) に基づき、二層プロファイルシステム（Author DNA + Story Profile）とエージェントチーム体制で執筆する。angel_return プロジェクトのファイル構造・命名規則に準拠。

**Tech Stack:** Claude Code エージェントチーム（Writer / Editor / Proofreader / Publisher）、novel_writing スキル、Markdown、UTF-8 with BOM（Pixiv用）

**Design Reference:** `docs/plans/2026-02-15-battousai-design.md`

---

### Task 1: ディレクトリ構造の作成

**Files:**
- Create: `projects/battousai/docs/characters/.gitkeep`
- Create: `projects/battousai/docs/world/.gitkeep`
- Create: `projects/battousai/docs/episodes/.gitkeep`
- Create: `projects/battousai/drafts/.gitkeep`
- Create: `projects/battousai/dist/pixiv/.gitkeep`

**Step 1: ディレクトリを作成**

```bash
mkdir -p projects/battousai/docs/characters
mkdir -p projects/battousai/docs/world
mkdir -p projects/battousai/docs/episodes
mkdir -p projects/battousai/drafts
mkdir -p projects/battousai/dist/pixiv
touch projects/battousai/docs/characters/.gitkeep
touch projects/battousai/docs/world/.gitkeep
touch projects/battousai/docs/episodes/.gitkeep
touch projects/battousai/drafts/.gitkeep
touch projects/battousai/dist/pixiv/.gitkeep
```

**Step 2: コミット**

```bash
git add projects/battousai/
git commit -m "feat: Scaffold battousai project directory structure"
```

---

### Task 2: Story Profile の作成

**Files:**
- Create: `.agent/profiles/battousai.md`
- Reference: `.agent/profiles/angel_return.md`（構造を踏襲）
- Reference: `docs/plans/2026-02-15-battousai-design.md`（設計源）

**Step 1: Story Profile を作成**

デザインドキュメントの §1〜§5, §7〜§9, §11 を Story Profile フォーマットに結晶化する。angel_return.md のセクション構成に合わせる:

1. 作品の美学: Stained Steel（染まった鋼）
2. トーンと語り
3. テーマ
4. 世界設定（世界観ルール §9 を含む）
5. キャラクター・ダイナミクス（口調・Arc を含む）
6. 構造設計原則
7. 戦闘描写の設計（Battle Writing — 剣術版）
8. 禁止事項（本作品固有）

**重要**: デザインドキュメントのコピペではなく、Writer/Editor が執筆時に参照する運用ドキュメントとして再構成する。冗長な背景説明は削ぎ落とし、ルールと判断基準を明確にする。

**Step 2: コミット**

```bash
git add .agent/profiles/battousai.md
git commit -m "feat: Create Story Profile for battousai (濁刃)"
```

---

### Task 3: キャラクターファイル作成（4ファイル並列可）

**Files:**
- Create: `projects/battousai/docs/characters/battousai.md`
- Create: `projects/battousai/docs/characters/tomoe.md`
- Create: `projects/battousai/docs/characters/kaidou.md`
- Create: `projects/battousai/docs/characters/katsura.md`
- Reference: `projects/angel_return/docs/characters/shinji_ikari.md`（フォーマット踏襲）

**Step 1: キャラクターファイルを作成**

angel_return のキャラクターファイル構造に準拠:

```markdown
# キャラクター設定: [名前] ([英語タグ])

## 1. Basic Info (基本情報)
- 名前、年齢、所属、役割

## 2. Core Concept (核心)
> 一行で本質を表す

## 3. Personality & Voice (性格・口調)
- 性格
- 口調サンプル（台詞例2〜3個）
- Behavioral Rules: DO / DON'T

## 4. Theme Answer (テーマへの回答)
> Design §5 から転記・深化

## 5. Arc (変化の軌跡)
> 話数ごとの段階

## 6. Relationships (人間関係)
- 他キャラクターとの関係を具体的に

## 7. Combat Style (戦闘スタイル) ※戦闘キャラのみ
- 流派、身体性、剣の質感
```

各キャラの注意点:
- **抜刀斎**: 口調サンプルに「任務中」と「巴の前」の二面を必ず書く。侵食の段階×話数の対応表を Arc に含める
- **巴**: 台詞例は少なめ（寡黙なキャラ）。沈黙の質の変容を Arc に明記。DO/DON'T で「感情を直接語る台詞」を禁止
- **灰堂**: 名前の由来・流派名を確定する。「空虚な丁寧語」の口調サンプルを3例以上
- **桂**: 歴史上の人物としての最低限の考証。政治家としての台詞と、抜刀斎への個人的な声かけの温度差

**Step 2: コミット**

```bash
git add projects/battousai/docs/characters/
git commit -m "feat: Create character files for battousai (4 characters)"
```

---

### Task 4: 世界観設定ファイル作成

**Files:**
- Create: `projects/battousai/docs/world/bakumatsu_kyoto.md`
- Create: `projects/battousai/docs/world/hiten_mitsurugi.md`

**Step 1: 幕末京都設定を作成**

`bakumatsu_kyoto.md`:
- 物語の舞台となる場所の質感リスト（路地裏、鴨川、寺院、長屋、旅籠）
- 時間帯と光源（篝火、月光、行灯、夕凪）
- 生活描写の素材集（食事、衣服、匂い、音）
- 政治状況の最小限の説明（長州藩の立場、新選組の存在、暗殺が日常化した京都）

**Step 2: 飛天御剣流設定を作成**

`hiten_mitsurugi.md`:
- 本作で使用する技のリスト（技名、身体描写、使用場面の指定）
- 流派の身体的特徴（速度の代償、筋肉への負荷、超神速の制約）
- 灰堂の流派（名称・特徴・抜刀斎との対比ポイント）
- 技名の使用ルール（Design §9 準拠: 要所のみ、地の文に溶かす）

**Step 3: コミット**

```bash
git add projects/battousai/docs/world/
git commit -m "feat: Create world setting files (Bakumatsu Kyoto, Hiten Mitsurugi)"
```

---

### Task 5: 全体プロットの作成

**Files:**
- Create: `projects/battousai/docs/overall_plot.md`
- Reference: `docs/plans/2026-02-15-battousai-design.md` §6（幕構成）

**Step 1: 全体プロットを作成**

Design §6 の幕構成をベースに、以下を追加して完全なプロットドキュメントにする:

```markdown
# Overall Plot: 濁刃（だくじん）

## ログライン
（Design より転記）

## 設計原則
（Design §8 構造設計原則を転記）

## 幕構成

### 第一幕「血鉄」（第1話〜第3話）

#### 第1話「夜雨」
- **視点**: 抜刀斎
- **目的**: 世界観・主人公・テーマの確立。侵食第1段階の仕込み
- **シーン構成**: 3〜4シーンの概要（任務→戦闘→事後→桂との会話）
- **伏線の仕込み**: 侵食（匂い）、桂の大義、「美しい剣」の萌芽
- **円環要素**: 雨、血の匂い、一人で刀を拭う

（以下、第2話〜第10話も同様の粒度で）
```

**重要**: 各話の「シーン構成」は、この段階では概要レベル（各シーン1〜2行）でよい。詳細シーン設計は Task 7 の episode design で行う。

**Step 2: コミット**

```bash
git add projects/battousai/docs/overall_plot.md
git commit -m "feat: Create overall plot for battousai (10 episodes, 3 acts)"
```

---

### Task 6: 伏線管理表の作成

**Files:**
- Create: `projects/battousai/docs/foreshadowing.md`
- Reference: `projects/angel_return/docs/foreshadowing.md`（フォーマット踏襲）
- Reference: `docs/plans/2026-02-15-battousai-design.md` §10（伏線管理）

**Step 1: 伏線管理表を作成**

angel_return の foreshadowing.md のフォーマットに準拠:

```markdown
# Foreshadowing Tracker: 濁刃（だくじん）

## Status Legend
| Status | Description |
| :--- | :--- |
| 🔴 Unresolved | 提示済みだが未回収 |
| 🟡 In Progress | 進行中・部分的に触れられている |
| 🟢 Resolved | 完全に回収済み |

## 1. Main Themes (テーマ伏線)
| ID | Subject | Setup | Develops | Resolution | Status |

## 2. Character Arcs (キャラクター伏線)
| ID | Subject | Setup | Develops | Resolution | Status |

## 3. Erosion (侵食の進行)
| ID | Stage | Episode | Description | Status |
```

Design §10 の5つの伏線ラインを上記フォーマットに展開する。

**Step 2: コミット**

```bash
git add projects/battousai/docs/foreshadowing.md
git commit -m "feat: Create foreshadowing tracker for battousai"
```

---

### Task 7: 第1話「夜雨」エピソード設計

**Files:**
- Create: `projects/battousai/docs/episodes/ep01_night_rain.md`
- Reference: `projects/angel_return/docs/episodes/ep05_ghost_in_the_shell.md`（フォーマット踏襲）

**Step 1: エピソード設計を作成**

angel_return のエピソード設計フォーマットに準拠:

```markdown
# 第1話: 夜雨 (Night Rain)

## 位置づけ
- 第一幕「血鉄」の幕開け
- 世界観・抜刀斎・テーマの確立
- 侵食第1段階の仕込み
- 円環構造の起点（雨、血の匂い、一人で刀を拭う）

## テーマ
「美しい剣は、最も多くの血を吸った剣か」の最初の問いかけ

---

## シーン構成

### シーン1: [タイトル]
- 場所、時間帯、天候
- 何が起きるか（3〜5行）
- 視点キャラの内面状態
- 伏線の仕込みポイント
- Battle Tempo の適用（戦闘シーンの場合）

### シーン2: ...
（以下同様）
```

**注意点**:
- 第1話は戦闘シーンを含む（Design §8: 第一幕は戦闘2/日常1）
- Battle Tempo（静→爆→沈黙→加速→頂点）の各フェーズをシーン設計に明記
- 侵食第1段階（血の匂い）の仕込み箇所を具体的に指定
- 円環構造の起点要素（雨、匂い、一人で刀を拭う）を配置
- 冒頭は Non-Visual First（Author DNA §2）: 視覚以外の感覚から始める

**Step 2: ユーザー承認**

エピソード設計をユーザーに提示し、承認を得てから執筆に進む。

**Step 3: コミット**

```bash
git add projects/battousai/docs/episodes/ep01_night_rain.md
git commit -m "feat: Create episode design for Ep.01 Night Rain"
```

---

### Task 8: 第1話「夜雨」執筆

**Files:**
- Create: `projects/battousai/drafts/01_night_rain.md`
- Reference: `.agent/author_profile.md`（Author DNA）
- Reference: `.agent/profiles/battousai.md`（Story Profile）
- Reference: `projects/battousai/docs/episodes/ep01_night_rain.md`（エピソード設計）

**Step 1: Writer エージェントで執筆**

Writer エージェント (`.claude/agents/writer.md`) を起動し、以下を入力として渡す:
- Author DNA (`.agent/author_profile.md`)
- Story Profile (`.agent/profiles/battousai.md`)
- エピソード設計 (`docs/episodes/ep01_night_rain.md`)
- キャラクターファイル (`docs/characters/battousai.md`, `docs/characters/katsura.md`)
- 世界観設定 (`docs/world/bakumatsu_kyoto.md`, `docs/world/hiten_mitsurugi.md`)

**チェックポイント**:
- 目標文字数: 7,000〜10,000字
- 散文密度ルール準拠（3〜5文/段落、文長バリエーション）
- 冒頭は身体感覚から（Physical Opening）
- 戦闘シーンは Battle Tempo 準拠
- 侵食第1段階の描写を含む
- 円環構造の起点要素を含む
- 禁止事項（§11）に違反していないか

**Step 2: コミット（ドラフト）**

```bash
git add projects/battousai/drafts/01_night_rain.md
git commit -m "feat: Write Ep.01 Night Rain first draft"
```

---

### Task 9: 第1話レビュー（Editor + Proofreader 並列）

**Files:**
- Modify: `projects/battousai/drafts/01_night_rain.md`

**Step 1: Editor + Proofreader を並列起動**

**Editor** (`.claude/agents/editor.md`):
- エンターテインメント性の分析
- 戦闘シーンのテンポ
- 読者を掴むフックの有効性
- Before/After 形式で修正案を提示

**Proofreader** (`.claude/agents/proofreader.md`):
- 設定整合性の検証（世界観・キャラ口調・時代考証）
- Author DNA / Story Profile 準拠チェック
- 散文密度ルール違反の検出
- メタ参照・禁止事項違反の検出

**Step 2: レビュー結果を統合し修正**

Editor と Proofreader のフィードバックを統合し、ドラフトを修正する。

**Step 3: コミット**

```bash
git add projects/battousai/drafts/01_night_rain.md
git commit -m "refactor: Apply Editor/Proofreader feedback to Ep.01"
```

---

### Task 10: 第1話の公開準備

**Files:**
- Create: `projects/battousai/dist/pixiv/01_night_rain_pixiv.txt`
- Create: `projects/battousai/dist/pixiv/caption.txt`
- Modify: `projects/battousai/docs/foreshadowing.md`

**Step 1: Pixiv版を生成**

Publisher エージェント (`.claude/agents/publisher.md`) で:
- Markdown → Pixiv テキスト変換
- UTF-8 with BOM で出力
- キャプション作成

**Step 2: 伏線管理表を更新**

第1話で仕込んだ伏線のステータスを更新:
- 侵食の進行 → 🟡 In Progress
- 桂の大義の空洞化 → 🟡 In Progress

**Step 3: コミット**

```bash
git add projects/battousai/dist/pixiv/ projects/battousai/docs/foreshadowing.md
git commit -m "feat: Publish Ep.01 Night Rain (Pixiv format + foreshadowing update)"
```

---

## 依存関係

```
Task 1 (ディレクトリ)
  └→ Task 2 (Story Profile)  ← 並列可
  └→ Task 3 (キャラファイル) ← 並列可
  └→ Task 4 (世界観設定)     ← 並列可
       └→ Task 5 (全体プロット)
       └→ Task 6 (伏線管理表)
            └→ Task 7 (Ep.1 設計) ← Task 2-6 全て完了後
                 └→ Task 8 (Ep.1 執筆)
                      └→ Task 9 (レビュー)
                           └→ Task 10 (公開準備)
```

**並列化ポイント**: Task 2, 3, 4 は Task 1 完了後に並列実行可能。
