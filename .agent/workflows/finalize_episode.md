---
description: Check consistency, convert format, and commit the finished episode
---

# Finalize Episode Workflow

このワークフローは、執筆が完了したエピソードに対して「最終整合性チェック」「Pixiv形式への変換」「Gitコミット」を一括で行うためのものです。
**執筆中のエピソードが完成し、ユーザーからのOKが出た後に実行してください。**

## Usage

```
/finalize_episode [episode_file_path] [commit_message]
```

Example: `/finalize_episode projects/angel_return/drafts/05_ghost_in_the_shell.md "Add Episode 5"`

## Steps

### 1. Final Consistency Check (最終チェック)
- [ ] 指定されたファイルに対して、`consistency_check` スキルの主要項目（特にCharacter VoiceとHard Mode Rule）を再確認する。
- [ ] 問題があればエラーを出して停止し、修正を促す。

### 2. Convert to Public Format (フォーマット変換)
- [ ] Markdown形式のドラフトを、Pixiv投稿用テキスト形式 (`.txt`) に変換し、`dist/pixiv/` に保存する。
    - **変換ルール**:
        - `## Title` -> `[chapter: Title]`
        - `**Text**` (太字) -> そのまま、あるいは強調表現なしへ
        - `***` (区切り線) -> `[newpage]`
        - ルビ記法: `漢字（よみがな）` -> `[[rb: 漢字 > よみがな ]]` (※自動変換はリスクが高いので、必要なら手動で行うようコメントを残す)

### 3. Git Commit (コミット)
- [ ] 変換されたファイルとドラフトを含めて、git commit する。

## Command Script (Auto-Run)

// turbo
以下のスクリプトは、「フォーマット変換」と「コミット」を自動化するものです。
※ 事前に整合性チェックが完了している前提です。

```powershell
$draftPath = "[episode_file_path]"
$commitMessage = "[commit_message]"

# パスの解決 (絶対パスへ)
$absDraftPath = Resolve-Path $draftPath
$projectDir = Split-Path (Split-Path $absDraftPath -Parent) -Parent
$fileName = Split-Path $absDraftPath -Leaf
$baseName = [System.IO.Path]::GetFileNameWithoutExtension($fileName)
$distPath = "$projectDir\dist\pixiv\${baseName}_pixiv.txt"

# 1. Read Content
$content = Get-Content $absDraftPath -Raw -Encoding UTF8

# 2. Convert Format (Basic Markdown to Pixiv)
# Remove Title Header (# Title)
$content = $content -replace '^#\s+.*$', ''
# Convert Page Breaks
$content = $content -replace '\*\*\*', '[newpage]'
# Convert Chapter Headers
$content = $content -replace '##\s+(.*)', '[chapter: $1]'
# Remove bold/italic markers
$content = $content -replace '\*\*(.*?)\*\*', '$1'
$content = $content -replace '\*(.*?)\*', '$1'

# 3. Save to Dist
Set-Content -Path $distPath -Value $content -Encoding UTF8
Write-Host "Converted file saved to: $distPath"

# 4. Git Commit
git add "$absDraftPath" "$distPath"
git commit -m "$commitMessage"

Write-Host "Committed changes for: $baseName"
```
