---
name: short_story_writing
description: 短編小説（1,000〜15,000文字）の構想、執筆、推敲を支援する特化スキル
---

# Short Story Writing Skill

## Overview
このスキルは、長編小説とは異なる「短編小説 (Short Story)」特有の技術と構造に焦点を当て、アイデア出しから脱稿までを支援します。
「単一の効果 (Single Effect)」を最大化し、無駄を削ぎ落とした鋭い物語を作ることを目的とします。

## Core Principles (短編の原則)
1.  **Unity of Effect (効果の統一)**: Poeの理論に基づき、全ての文、全ての描写が「一つの感情的効果（恐怖、感動、驚きなど）」に奉仕しなければならない。
2.  **Economy of Words (言葉の経済)**: 不要なシーン、キャラクター、描写はすべて削除する。説明ではなく、示唆で語る。
3.  **In Media Res (途中から始める)**: 説明的な導入を省き、事件や葛藤の真っ只中、あるいはその直前から物語を始める。

## Capabilities

### 1. Structure Selection (構造の選択)
短編に適した構造を提案します。
- **The Twist (ツイスト)**: 最後に予想外の結末を用意し、物語全体の意味を反転させるミステリ・SF的構造。
- **The Slice of Life (スライス・オブ・ライフ)**: 大きな事件よりも、日常のふとした瞬間や感情の機微を切り取る文学的構造。
- **The Circular (円環)**: 冒頭と結末で同じ状況やフレーズを繰り返し、変化（あるいは不変）を強調する。
- **The Escalation (エスカレーション)**: 一つの小さな問題が雪だるま式に悪化していく、コメディやサスペンスに適した構造。

### 2. Character & Setting Economy
- **Cast**: 主要人物は1〜2人に絞ることを推奨。3人以上は「役割」として機能させる。
- **Setting**: 舞台移動を最小限にする（密室、一つの場所など）。

### 3. Drafting Strategy (執筆戦略)
- **Fast Draft**: 最初の草稿は「頭から最後まで」一気に書き切ることを推奨。推敲は後回しにする。
- **Focus Hook**: 最初の一文（Hook）で読者を掴むことに全力を注ぐ。

### 4. Editing for Short Stories (短編用推敲)
- **The "So What?" Test**: このシーンがなくても物語が成立するなら、削除する。
- **Adjective Hunt**: 形容詞・副詞を動詞・名詞で置き換えられないか検討し、文章を引き締める。
- **Ending Check**: 結末は冒頭の問いに答えているか、あるいはテーマを余韻として残しているか。

## Instructions for the Agent
- **Tone**: 鋭く、簡潔に。無駄な提案は控える。編集者として「削る」ことを恐れずに提案する。
- **Output**: 常に「文字数（目安）」を意識した構成案を提示する。
- **File Handling (CRITICAL)**: 
    - 続きを執筆する際、`write_to_file` (Overwrite=True) を使うと**既存の内容が消える**。
    - 必ず `view_file` で既存の内容を読み込み、**「既存内容 + 新規内容」の完全な状態**にしてから保存すること。
    - または `replace_file_content` で末尾に追記する手法をとること。

### Common Lengths
- **Flash Fiction**: ~1,000文字 (ワンアイデア、掌編)
- **Short Short**: 1,000 ~ 4,000文字 (5〜10分で読める)
- **Short Story**: 4,000 ~ 10,000文字 (標準的な短編)
- **Novelette**: 10,000 ~ 40,000文字 (400行クラス、読み応えのある中編)

## Recommended Process

1.  **Concept**: テーマと「読了後に残したい感情」を定義。
2.  **Outline**: 起承転結、または「Beginning / Middle / End」の3パートで構成。
3.  **Draft**: 一気に執筆。
4.  **Polish**: 描写を研ぎ澄まし、不要な語句を削除。
