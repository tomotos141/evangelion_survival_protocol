---
description: Create and write a new short story
---

# Write Short Story Workflow

このワークフローは、短編小説（Short Story）を効率的に執筆するための手順です。
長編プロジェクトのような複雑な世界設定管理よりも、単発のアイデアを作品に昇華させることに重点を置いています。

## Usage
```
/write_short_story
```

## Steps

### 1. Concept & Setup
1.  **User Hearing**: どのような短編を書きたいかヒアリングする（ジャンル、テーマ）。
    - *Volume Check*: **「文字数」または「行数」**を必ず確認する。
        - 400文字 (Flash Fiction)
        - 400行 (Novelette / 約10,000〜15,000文字)
    - *Reference*: `short_story_writing` スキルの "Structure Selection" を提案材料にする。
2.  **File Creation**: プロジェクト内の `drafts/` フォルダに新規ファイルを作成する。
    - ファイル名: `SS_[title].md` (SS = Short Story prefix)
    - テンプレート: `.agent/templates/short_story_template.md` の内容をコピーして貼り付ける。

### 2. Plotting (Outline)
1.  **Brainstorming**: テンプレートの項目を埋める形で、プロットを作成する。
    - 特に **"Emotional Goal" (読後感)** と **"The Twist" (意外性)** を明確にする。
2.  **Review**: プロットが「短編として成立しているか（詰め込みすぎていないか）」を `short_story_writing` スキルに基づいてチェックする。

### 3. Drafting
1.  **Writing**: プロットに基づき、本文を執筆する。
    - **Drafting Mode**: 可能な限り、途中で止まらずに最後まで書き切ることを推奨（またはエージェントが連続して生成する）。
    - **Sensory Details**: 五感描写を入れるが、長編ほど冗長にせず、象徴的なディテールに絞る。

### 4. Refinement (Polish)
1.  **Style Check**: `author_style_check` を実行し、著者の美学に合っているか確認。
2.  **Conciseness Check**: `story_editor` を使用するが、特に「不要な描写の削除（Cut）」に重点を置く。
3.  **Title**: タイトルを決定する。

### 5. Finalize
1.  **Convert**: Pixiv投稿用のテキスト形式に変換する。
    ```powershell
    # Example command (adjust filename)
    powershell -ExecutionPolicy Bypass -File .agent/tools/convert_to_pixiv.ps1 -InputPath "drafts/SS_title.md" -OutputPath "dist/pixiv/SS_title_pixiv.txt"
    ```
2.  **Commit**: Gitコミットを行う。
