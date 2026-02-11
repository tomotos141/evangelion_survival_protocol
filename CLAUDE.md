# CLAUDE.md

## Project Overview

小説執筆プロジェクト。二層プロファイルシステム（Author DNA + Story Profile）を使い、エージェントチームで執筆する。

## Directory Structure

```
.agent/
  author_profile.md          # Author DNA（全作品共通の技法・ルール）
  profiles/<project>.md       # Story Profile（作品固有の美学・キャラ・ルール）
.claude/
  agents/                     # エージェント定義（writer, editor, proofreader, publisher）
  skills/                     # オーケストレーションスキル
projects/<project>/
  docs/                       # 設定資料（プロット、キャラ、世界観、伏線管理）
  drafts/                     # 原稿（Markdown）
  dist/pixiv/                 # Pixiv公開用テキスト
```

## Conventions

### Git
- ブランチ: master 直コミット（個人プロジェクト）
- コミットメッセージ: 英語、動詞で始める（Add, Update, Fix, Remove）
- push は明示的に指示されたときのみ

### Writing Rules
- 地の文で `Ep.5の夜` 等のエピソード番号参照を使わない。`あの夜`、`ラミエル戦` など作中表現で参照する
- AI臭の排除: 同じ構文パターンの連続、抽象語の空回り、同義語連打を避ける
- 散文密度: 一文一行スタッカート禁止。3〜5文/段落、1話 7,000〜10,000文字

### Agent Workflow
- 執筆は Writer → Editor + Proofreader（並列レビュー）→ 修正 → Publisher
- エージェントは起動時に Author DNA と Story Profile の両方を読む
- Story Profile はエピソードパスからプロジェクト名を導出して特定する
