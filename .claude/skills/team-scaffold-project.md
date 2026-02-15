---
name: team-scaffold-project
description: デザインドキュメントからプロジェクト基盤を一括構築するオーケストレーション。ディレクトリ・Story Profile・キャラクターファイル・世界観設定・全体プロット・伏線管理表を依存関係に従って作成する。「プロジェクトを構築して」「scaffold」「基盤を作って」で発動する。
---

# Project Scaffold Pipeline

デザインドキュメントが完成した状態から、プロジェクトの基盤ファイル一式を構築するオーケストレーション手順。

## 前提条件

- デザインドキュメント（`docs/plans/YYYY-MM-DD-<project>-design.md`）が存在する
- デザインドキュメントに以下のセクションが含まれている:
  - 作品の美学、トーンと語り、テーマ
  - キャラクター・ダイナミクス（口調・Arc 含む）
  - 幕構成（全話の概要）
  - 戦闘/アクション描写の設計（該当する場合）
  - 世界観ルール
  - 伏線管理
  - 禁止事項
  - プロジェクト設定（プロジェクト名、タイプ、skill_ref）

## 入力の確認 — Team Lead

1. デザインドキュメントのパスを特定する
2. プロジェクト名を確認する（例: `battousai`）
3. プロジェクトパスを確定する: `projects/{project_name}/`
4. ユーザーの承認を得てから Phase 1 へ進む

---

## Phase 1: Directory Scaffold（ディレクトリ作成）— Team Lead 直接実行

```bash
mkdir -p projects/{project}/docs/characters
mkdir -p projects/{project}/docs/world
mkdir -p projects/{project}/docs/episodes
mkdir -p projects/{project}/drafts
mkdir -p projects/{project}/dist/pixiv
```

各ディレクトリに `.gitkeep` を配置し、コミットする。

---

## Phase 2: Foundation Files（基盤ファイル作成）— 3エージェント並列

Phase 1 完了後、以下の3つを **並列で** 起動する。

### 2a. Story Profile — `scaffold-story-profile` スキル

**general-purpose** サブエージェントに委任する。

指示に含める情報:
- デザインドキュメントのパス
- プロジェクト名
- `scaffold-story-profile` スキルの内容（`.claude/skills/scaffold-story-profile.md`）

出力: `.agent/profiles/{project}.md`

### 2b. Character Files — `scaffold-characters` スキル

**general-purpose** サブエージェントに委任する。

指示に含める情報:
- デザインドキュメントのパス
- プロジェクトパス
- `scaffold-characters` スキルの内容（`.claude/skills/scaffold-characters.md`）

出力: `projects/{project}/docs/characters/*.md`

### 2c. World Settings — `scaffold-world` スキル

**general-purpose** サブエージェントに委任する。

指示に含める情報:
- デザインドキュメントのパス
- プロジェクトパス
- `scaffold-world` スキルの内容（`.claude/skills/scaffold-world.md`）

出力: `projects/{project}/docs/world/*.md`

3つ全ての完了を待つ。

---

## Phase 3: Plot & Foreshadowing（プロット構築）— 2エージェント並列

Phase 2 完了後、以下の2つを **並列で** 起動する。

### 3a. Overall Plot — `scaffold-plot` スキル

**general-purpose** サブエージェントに委任する。

指示に含める情報:
- デザインドキュメントのパス
- プロジェクトパス
- Phase 2 で作成された Story Profile のパス
- `scaffold-plot` スキルの内容（`.claude/skills/scaffold-plot.md`）

出力: `projects/{project}/docs/overall_plot.md`

### 3b. Foreshadowing Tracker — `scaffold-foreshadowing` スキル

**general-purpose** サブエージェントに委任する。

指示に含める情報:
- デザインドキュメントのパス
- プロジェクトパス
- `scaffold-foreshadowing` スキルの内容（`.claude/skills/scaffold-foreshadowing.md`）

出力: `projects/{project}/docs/foreshadowing.md`

2つ全ての完了を待つ。

---

## Phase 4: Review & Commit（検証とコミット）— Team Lead

1. 全成果物の一覧を提示する:
   - `.agent/profiles/{project}.md`（Story Profile）
   - `projects/{project}/docs/characters/*.md`（キャラクターファイル）
   - `projects/{project}/docs/world/*.md`（世界観設定）
   - `projects/{project}/docs/overall_plot.md`（全体プロット）
   - `projects/{project}/docs/foreshadowing.md`（伏線管理表）

2. `Grep` で `Ep.\d` パターンの残存を確認する

3. ユーザーに成果物を確認してもらい、コミットの要否を確認する

4. コミットが指示された場合のみ実行する

---

## Phase 5: Handoff（引き渡し）

1. 次のステップとして以下を案内する:
   - `team-write-episode` パイプラインで第1話の執筆を開始
   - 事前に `docs/episodes/ep01_*.md` のエピソード設計が必要
2. `audit-design` スキルで Story Profile とプロットの整合性を検証できることを案内する

---

## 依存関係

```
Phase 1: ディレクトリ作成
  └→ Phase 2（並列）: Story Profile + Characters + World
       └→ Phase 3（並列）: Overall Plot + Foreshadowing
            └→ Phase 4: Review & Commit
                 └→ Phase 5: Handoff → team-write-episode
```
