---
description: 新しい小説プロジェクトのディレクトリ構造、Story Profile、設定ファイルを作成するワークフロー
---

# Create New Project Workflow

新しいプロジェクトを開始するための標準的なディレクトリ構造と設定ファイルを作成する。
プロジェクトタイプに応じて構造が変わる。

## Usage

```
/new_novel_project [project_name] [type: novel | short_story_collection | original]
```

- `type` 省略時は `novel` をデフォルトとする。

---

## Steps

### 1. プロジェクトタイプの確認

ユーザーにプロジェクトタイプを確認する:
- **novel**: 連載小説（二次創作など、世界観・キャラが既存の場合）
- **original**: オリジナル作品（ゼロから世界構築・キャラ創造を行う。`team-create-original` パイプラインと連携）
- **short_story_collection**: 短編集（独立したSSを集約）

### 2. プロジェクトディレクトリの作成

#### novel の場合

```
projects/[project_name]/
├── docs/
│   ├── characters/
│   ├── episodes/
│   ├── world/
│   └── templates/
├── drafts/
└── dist/
    └── pixiv/
```

#### original の場合

```
projects/[project_name]/
├── docs/
│   ├── characters/
│   ├── episodes/
│   ├── world/
│   ├── research/       # リサーチ出力置き場
│   └── templates/
├── drafts/
└── dist/
    └── pixiv/
```

#### short_story_collection の場合

```
projects/[project_name]/
├── docs/
│   ├── plans/          # 各SSのプランファイル置き場
│   └── templates/
├── drafts/             # SS_*.md を直接配置
└── dist/
    └── pixiv/
```

### 3. Story Profile の作成

`.agent/profiles/[project_name].md` に Story Profile のひな形を作成する。

#### novel の場合

ユーザーと対話しながら以下を埋める:

- 作品の美学（世界の質感、色彩、感覚）
- トーンと語り（文体、視点、人称）
- テーマ
- 世界設定のルール
- キャラクター・ダイナミクス
- 作品固有の禁止事項

#### original の場合

ひな形のみ作成する。実際の内容は `team-create-original` パイプラインの Phase 4（Story Profile 結晶化）で埋める。

- `skill_ref: novel_writing` をデフォルトで記載
- 各セクションは空欄のまま（パイプラインで結晶化される旨の注記を入れる）

#### short_story_collection の場合

- `skill_ref: short_story_writing` を記載する
- コレクション共通のトーン指針を定義する
- 各SSは独立した世界・キャラを持つことを明記する

### 4. 設定ファイルのひな形作成

#### novel の場合

- `docs/overall_plot.md`: 全体プロットの構成案
- `docs/foreshadowing.md`: 伏線管理表

#### original の場合

- `docs/overall_plot.md`: 全体プロットの構成案（パイプライン Phase 3 で記入）
- `docs/foreshadowing.md`: 伏線管理表（パイプライン Phase 3 で記入）
- `docs/research/` ディレクトリのみ作成（内容はリサーチフェーズで生成）

#### short_story_collection の場合

- `docs/collection_index.md`: SS一覧と状態管理

### 5. テンプレートのコピー

`.agent/templates/` 配下のテンプレートを `docs/templates/` にコピーする。

#### novel の場合
- `character_template.md`
- `threat_template.md`
- `world_rule_template.md`

#### original の場合
- `character_template_generic.md`
- `world_building_template.md`
- `conflict_template.md`

#### short_story_collection の場合
- `short_story_template.md`

### 6. 初期ファイル作成スクリプト

```python
import os
import shutil

project_name = "[project_name]"  # 置き換えてください
project_type = "novel"  # "novel", "original", or "short_story_collection"
base_dir = f"projects/{project_name}"
profile_path = f".agent/profiles/{project_name}.md"

# ディレクトリ作成
if project_type in ("novel", "original"):
    dirs = [
        f"{base_dir}/docs/characters",
        f"{base_dir}/docs/episodes",
        f"{base_dir}/docs/world",
        f"{base_dir}/docs/templates",
        f"{base_dir}/drafts",
        f"{base_dir}/dist/pixiv",
    ]
    if project_type == "original":
        dirs.append(f"{base_dir}/docs/research")
else:  # short_story_collection
    dirs = [
        f"{base_dir}/docs/plans",
        f"{base_dir}/docs/templates",
        f"{base_dir}/drafts",
        f"{base_dir}/dist/pixiv",
    ]
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Story Profile 作成
os.makedirs(".agent/profiles", exist_ok=True)
if not os.path.exists(profile_path):
    if project_type == "novel":
        with open(profile_path, "w", encoding="utf-8") as f:
            f.write(f"""# Story Profile: {project_name}

> 本ファイルは本作品固有の美学・トーン・キャラクター・ルールを定義する。
> 著者の共通美学は `.agent/author_profile.md` を参照。

---

## 1. 作品の美学
（世界の質感、色彩、感覚を定義する）

---

## 2. トーンと語り
- **文体**: （例: ハードボイルド、叙情的、軽妙 等）
- **視点**: （例: 一人称・過去形、三人称限定視点 等）
- **想定読者**: （例: 30代男性、10代女性 等）

---

## 3. テーマ
（作品の中心的な問いを定義する）

---

## 4. 世界設定
（作品固有の世界ルール、制約を定義する）

---

## 5. キャラクター・ダイナミクス
（主要キャラクターの造形、口調、テーマへの回答を定義する）

---

## 6. 禁止事項（本作品固有）
（この作品で避けるべき表現、展開を定義する）
""")
    elif project_type == "original":
        with open(profile_path, "w", encoding="utf-8") as f:
            f.write(f"""# Story Profile: {project_name}

> 本ファイルは本作品固有の美学・トーン・キャラクター・ルールを定義する。
> 著者の共通美学は `.agent/author_profile.md` を参照。
>
> ※ このプロファイルは team-create-original パイプラインの Phase 4 で結晶化される。

---

## skill_ref: novel_writing

---

## 1. 作品の美学
（team-create-original Phase 2 の世界構築で導出）

---

## 2. トーンと語り
- **文体**:
- **視点**:
- **想定読者**: 30代男性

---

## 3. テーマ
（team-create-original Phase 0 のシードから発展）

---

## 4. 世界設定
（詳細は docs/world/ を参照）

---

## 5. キャラクター・ダイナミクス
（詳細は docs/characters/ を参照。各キャラクターのテーマへの回答を要約）

---

## 6. 禁止事項（本作品固有）
（この作品で避けるべき表現、展開を定義する）
""")
    else:  # short_story_collection
        with open(profile_path, "w", encoding="utf-8") as f:
            f.write(f"""# Story Profile: {project_name}（短編集）

> 独立した短編小説の集約プロジェクト。各SSは個別の世界・キャラクター・ジャンルを持つ。
> 著者の共通美学は `.agent/author_profile.md` を参照。

---

## skill_ref: short_story_writing

---

## 1. プロジェクトの性質

- **形態**: 短編集（アンソロジー）。各作品に連続性はない。
- **命名規則**: `drafts/SS_<Title>.md`
- **プロット管理**: 各SSの構想は `docs/plans/SS_<Title>_plan.md` または原稿冒頭の HTML コメントに記載する。
- **公開先**: Pixiv（`dist/pixiv/SS_<Title>_pixiv.txt`）

---

## 2. トーンと語り（コレクション共通）

- **文体の幅**: ジャンルに応じて文体は変える。ただし Author DNA の核心技法は全作品に適用する。
- **視点**: 作品ごとに自由。一人称/三人称の制約はない。
- **想定読者**: （例: 30代男性）

---

## 3. 短編固有の美学

- **Unity of Effect**: 全ての文が一つの感情的効果に奉仕する。
- **Economy**: 説明ではなく示唆で語る。
- **The Hook**: 冒頭一文で読者を掴む。
- **The Exit**: 結末は余韻で閉じる。

---

## 4. 禁止事項（コレクション共通）

- Author DNA §7 の共通禁止事項を適用する。
""")

# テンプレートコピー
if project_type == "novel":
    templates = ["character_template.md", "threat_template.md", "world_rule_template.md"]
elif project_type == "original":
    templates = ["character_template_generic.md", "world_building_template.md", "conflict_template.md"]
else:
    templates = ["short_story_template.md"]
for t in templates:
    src = f".agent/templates/{t}"
    if os.path.exists(src):
        shutil.copy2(src, f"{base_dir}/docs/templates/{t}")

# 設定ファイル
if project_type in ("novel", "original"):
    with open(f"{base_dir}/docs/overall_plot.md", "w", encoding="utf-8") as f:
        f.write(f"""# Overall Plot: {project_name}

## Core Concept
（作品の核となるコンセプトを1-2行で）

## Themes
-

## Story Arc (構成案)

### Act 1: [Title]
- Episode 1:
- Episode 2:

### Key Mysteries (未解決の伏線)
1.
""")
    with open(f"{base_dir}/docs/foreshadowing.md", "w", encoding="utf-8") as f:
        f.write(f"""# Foreshadowing Tracker: {project_name}

| # | 伏線 | 設置 | 状態 | 回収予定 |
|---|------|------|------|---------|
| 1 |      |      | 🔴   |         |
""")
    if project_type == "novel":
        with open(f"{base_dir}/drafts/01_prologue.md", "w", encoding="utf-8") as f:
            f.write("# Episode 1: Title\n\nここに書き出しを入力...\n")
    # original の場合は drafts にファイルを作らない（パイプライン完了後に team-write-episode で作成）
else:
    with open(f"{base_dir}/docs/collection_index.md", "w", encoding="utf-8") as f:
        f.write(f"""# Collection Index: {project_name}

| # | タイトル | ジャンル | 文字数 | 状態 | Pixiv |
|---|---------|---------|--------|------|-------|
| 1 |         |         |        | 🔴   |       |
""")

print(f"Project '{project_name}' ({project_type}) created at {base_dir}")
print(f"Story Profile created at {profile_path}")
```

### 7. 確認事項

1. `.agent/author_profile.md`（Author DNA）を読み、全作品共通の美学を確認する
2. `.agent/profiles/[project_name].md`（Story Profile）をユーザーと対話しながら具体化する
3. Story Profile が完成してから執筆フェーズに進む
4. **short_story_collection の場合**: Story Profile に `skill_ref: short_story_writing` が含まれていることを確認する
5. **original の場合**: 次のステップとして `team-create-original` パイプラインを実行するようユーザーに案内する
