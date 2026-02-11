---
description: 新しい小説プロジェクトのディレクトリ構造、Story Profile、設定ファイルを作成するワークフロー
---

# Create New Novel Project Workflow

新しい小説プロジェクトを開始するための標準的なディレクトリ構造と設定ファイルを作成する。

## Usage

```
/new_novel_project [project_name]
```

## Steps

### 1. プロジェクトディレクトリの作成

指定されたプロジェクト名のディレクトリを `projects/` 配下に作成する。

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

### 2. Story Profile の作成

`.agent/profiles/[project_name].md` に Story Profile のひな形を作成する。
ユーザーと対話しながら以下を埋める:

- 作品の美学（世界の質感、色彩、感覚）
- トーンと語り（文体、視点、人称）
- テーマ
- 世界設定のルール
- キャラクター・ダイナミクス
- 作品固有の禁止事項

### 3. 設定ファイルのひな形作成

- `docs/overall_plot.md`: 全体プロットの構成案
- `docs/foreshadowing.md`: 伏線管理表
- `docs/characters/`: キャラクター設定置き場

### 4. テンプレートのコピー

`.agent/templates/` 配下の以下のテンプレートを `docs/templates/` にコピーする:
- `character_template.md`
- `threat_template.md`
- `world_rule_template.md`

### 5. 初期ファイル作成スクリプト

```python
import os
import shutil

project_name = "[project_name]"  # 置き換えてください
base_dir = f"projects/{project_name}"
profile_path = f".agent/profiles/{project_name}.md"

# ディレクトリ作成
dirs = [
    f"{base_dir}/docs/characters",
    f"{base_dir}/docs/episodes",
    f"{base_dir}/docs/world",
    f"{base_dir}/docs/templates",
    f"{base_dir}/drafts",
    f"{base_dir}/dist/pixiv",
]
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Story Profile 作成
os.makedirs(".agent/profiles", exist_ok=True)
if not os.path.exists(profile_path):
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

# テンプレートコピー
templates = ["character_template.md", "threat_template.md", "world_rule_template.md"]
for t in templates:
    src = f".agent/templates/{t}"
    if os.path.exists(src):
        shutil.copy2(src, f"{base_dir}/docs/templates/{t}")

# overall_plot.md
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

# foreshadowing.md
with open(f"{base_dir}/docs/foreshadowing.md", "w", encoding="utf-8") as f:
    f.write(f"""# Foreshadowing Tracker: {project_name}

| # | 伏線 | 設置 | 状態 | 回収予定 |
|---|------|------|------|---------|
| 1 |      |      | 🔴   |         |
""")

# 初稿ファイル
with open(f"{base_dir}/drafts/01_prologue.md", "w", encoding="utf-8") as f:
    f.write("# Episode 1: Title\n\nここに書き出しを入力...\n")

print(f"Project '{project_name}' created at {base_dir}")
print(f"Story Profile created at {profile_path}")
```

### 6. 確認事項

1. `.agent/author_profile.md`（Author DNA）を読み、全作品共通の美学を確認する
2. `.agent/profiles/[project_name].md`（Story Profile）をユーザーと対話しながら具体化する
3. Story Profile が完成してから執筆フェーズに進む
