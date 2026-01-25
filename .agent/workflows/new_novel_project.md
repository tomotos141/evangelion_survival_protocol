---
description: Create a new novel project structure
---

# Create New Novel Project Workflow

このワークフローは、新しい小説プロジェクトを開始するための標準的なディレクトリ構造と設定ファイルを作成します。

## Usage

```
/new_novel_project [project_name]
```

## Steps

1. プロジェクトディレクトリの作成 (Create Directories)
   - 指定されたプロジェクト名のディレクトリを `d:/antigravity/novel/projects/` 配下に作成します。
   - 必要なサブディレクトリ (`docs`, `drafts`, `dist`) を作成します。

2. 設定ファイルのひな形作成 (Create Template Files)
   - `docs/project_profile.md`: 世界観やトーンを定義するファイル。
   - `docs/characters/`: キャラクター設定置き場。
   - `drafts/01_prologue.md`: 原稿の書き出し用ファイル。

## Command Script

以下のスクリプトを実行して、新しいプロジェクトをセットアップします。
※ 実行前に `[project_name]` を実際の英数字のプロジェクト名（例：`space_opera`, `romance_v1`）に置き換えてください。

```powershell
$projectName = "[project_name]"
$baseDir = "d:\antigravity\novel\projects\$projectName"

# 1. Create Directories (with -Force to ignore if exists)
mkdir "$baseDir" -Force
mkdir "$baseDir\docs" -Force
mkdir "$baseDir\docs\characters" -Force
mkdir "$baseDir\docs\world" -Force
mkdir "$baseDir\docs\templates" -Force
mkdir "$baseDir\drafts" -Force
mkdir "$baseDir\dist" -Force

# 2. Copy Templates from .agent/templates
$templateSource = "d:\antigravity\novel\.agent\templates\character_template.md"
if (Test-Path $templateSource) {
    Copy-Item $templateSource -Destination "$baseDir\docs\templates\character_template.md" -Force
} else {
    Write-Warning "Master template not found at $templateSource"
}

# 3. Create project_profile.md
$profileContent = @"
# Project Profile: $projectName

## Overview (概要)
この作品のあらすじ、ジャンル、ターゲット読者層を記述してください。

## Specific Tone (この作品独自のトーン)
共通のAuthor Profile (Hardboiled, Cynical) をベースにしつつ、この作品で特に意識すべき点があれば記述してください。
（例：コメディ要素強め、ジュブナイル、幻想的など）
"@
Set-Content -Path "$baseDir\docs\project_profile.md" -Value $profileContent -Encoding UTF8

# 4. Create overall_plot.md (Adding Plot Template)
$plotContent = @"
# Overall Plot: $projectName

## Story Arc (構成案)

### Act 1: [Title]
- Case/Episode 1:
- Case/Episode 2:

### Act 2: [Title]
- 

### Key Mysteries (未解決の伏線)
1. 
"@
Set-Content -Path "$baseDir\docs\overall_plot.md" -Value $plotContent -Encoding UTF8

# 5. Create initial draft file
$draftContent = @"
# Episode 1: Title

ここに書き出しを入力...
"@
Set-Content -Path "$baseDir\drafts\01_prologue.md" -Value $draftContent -Encoding UTF8

Write-Host "Project '$projectName' created successfully at $baseDir"
```
