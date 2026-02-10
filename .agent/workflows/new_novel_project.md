---
description: 新しい小説プロジェクトのディレクトリ構造と設定ファイルを作成するワークフロー
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

### 2. 設定ファイルのひな形作成

- `docs/project_profile.md`: 世界観やトーンを定義するファイル
- `docs/overall_plot.md`: 全体プロットの構成案
- `docs/foreshadowing.md`: 伏線管理表
- `docs/characters/`: キャラクター設定置き場
- `drafts/01_prologue.md`: 原稿の書き出し用ファイル

### 3. テンプレートのコピー

`.agent/templates/` 配下の以下のテンプレートを `docs/templates/` にコピーする:
- `character_template.md`
- `threat_template.md`
- `world_rule_template.md`

### 4. 初期ファイル作成スクリプト

```python
import os
import shutil

project_name = "[project_name]"  # 置き換えてください
base_dir = f"projects/{project_name}"

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

# テンプレートコピー
templates = ["character_template.md", "threat_template.md", "world_rule_template.md"]
for t in templates:
    src = f".agent/templates/{t}"
    if os.path.exists(src):
        shutil.copy2(src, f"{base_dir}/docs/templates/{t}")

# project_profile.md
with open(f"{base_dir}/docs/project_profile.md", "w", encoding="utf-8") as f:
    f.write(f"""# Project Profile: {project_name}

## Overview (概要)
この作品のあらすじ、ジャンル、ターゲット読者層を記述してください。

## Specific Tone (この作品独自のトーン)
共通の Author Profile をベースにしつつ、この作品で特に意識すべき点があれば記述してください。
参照: `.agent/author_profile.md`
""")

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
```

### 5. 著者プロファイルの確認

新プロジェクト開始時に `.agent/author_profile.md` を読み、この作品に適用する美学を確認する。プロジェクト固有の調整は `docs/project_profile.md` に記載する。
