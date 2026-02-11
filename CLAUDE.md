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

#### コミットメッセージ
Conventional Commits 風の prefix を使う:
- `feat:` 新機能・新エピソード・新設定ファイル
- `fix:` バグ修正・設定矛盾の修正・誤字修正
- `refactor:` リライト・構造変更（機能変化なし）
- `docs:` ドキュメント更新（プロット、伏線管理表、プロファイル等）
- `chore:` ツール設定、gitignore、CI等の雑務

本文は英語。例: `feat: Write Ep.09 first draft`, `refactor: Style pass Act 1 (Ep.01-04)`

#### ブランチ戦略
- **master**: 安定版。公開済み or レビュー済みの原稿
- **feature ブランチ**: 大きな変更時に切る（例: `feat/ep09-rewrite`, `refactor/act1-style-pass`）
  - エピソード単体の修正は master 直コミットで可
  - 複数話にまたがるリライトや構造変更は feature ブランチを使う
- マージは squash merge を推奨（コミット履歴をきれいに保つ）

#### Push タイミング
- **エピソード完成時**: 1話書き上げてレビュー完了したら push
- **大きなドキュメント更新時**: プロファイル変更、プロット改訂など
- 細かい作業中のコミットは push しない。まとまったら push する
- push は明示的に指示されたときのみ実行する

#### Issue 管理
GitHub Issues でタスクを管理する:
- **ラベル**:
  - `episode`: エピソード執筆・リライト
  - `worldbuilding`: 世界設定・キャラ設定
  - `style`: 文体パス・散文密度
  - `tooling`: エージェント定義・スキル・ワークフロー
  - `bug`: 設定矛盾・整合性エラー
- **タイトル**: 日本語 OK。何をするか簡潔に
- **issue テンプレート**: 必要に応じて後で追加

### Writing Rules
- 地の文で `Ep.5の夜` 等のエピソード番号参照を使わない。`あの夜`、`ラミエル戦` など作中表現で参照する
- AI臭の排除: 同じ構文パターンの連続、抽象語の空回り、同義語連打を避ける
- 散文密度: 一文一行スタッカート禁止。3〜5文/段落、1話 7,000〜10,000文字

### Agent Workflow
- 執筆は Writer → Editor + Proofreader（並列レビュー）→ 修正 → Publisher
- エージェントは起動時に Author DNA と Story Profile の両方を読む
- Story Profile はエピソードパスからプロジェクト名を導出して特定する
