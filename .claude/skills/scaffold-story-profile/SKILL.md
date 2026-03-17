---
name: scaffold-story-profile
description: Generates Story Profile from design document. Distills aesthetics, tone, theme, characters, and constraints.
---

# scaffold-story-profile

デザインドキュメントを入力として、Writer/Editor が執筆時に参照する運用ドキュメントとしての Story Profile を生成する。

---

## 入力

- **design_doc**: デザインドキュメントのパス（例: `docs/plans/2026-02-15-battousai-design.md`）
- **project_name**: プロジェクト名（例: `battousai`）

## 出力

- `.agent/profiles/{project_name}.md`

## 参照テンプレート

- `.agent/profiles/angel_return.md` を `Read` で読み込み、セクション構成のテンプレートとして使用する

## 手順

1. デザインドキュメントを `Read` で全文読み込む
2. テンプレート（angel_return.md）を `Read` で読み込む
3. 以下のセクション構成で Story Profile を作成する:

### セクション構成

```markdown
# Story Profile: {project_name}（日本語タイトル）

> 作品概要（1〜2行）
> 本ファイルは本作品固有の美学・トーン・キャラクター・ルールを定義する。
> 著者の共通美学は `.agent/author_profile.md` を参照。

---

## 1. 作品の美学: [美学名]（英語サブタイトル）
## 2. トーンと語り
## 3. テーマ
## 4. 世界設定
## 5. キャラクター・ダイナミクス
## 6. 構造設計原則
## 7. [作品固有のセクション]（戦闘描写、能力設計 等）
## 8. 禁止事項（本作品固有）

---

## プロジェクト設定
- **skill_ref**: (novel_writing / short_story_writing)
- **project_type**: (novel / original / short_story_collection)
```

## 作成ルール

- デザインドキュメントの**コピペではなく**、運用ドキュメントとして再構成する
- 冗長な背景説明は削ぎ落とし、ルールと判断基準を明確にする
- 幕構成や伏線管理はプロットの領域なので Profile には含めない（`docs/overall_plot.md` や `docs/foreshadowing.md` に配置する）
- キャラクター詳細は `docs/characters/` への参照を明記し、Profile では Theme Answer・Core Conflict・口調・Arc の要約のみ記載する
- `Ep.X` 形式のエピソード番号参照を使わない
- 末尾にプロジェクト設定（skill_ref, project_type）を必ず含める

## 検証

- 作成後、テンプレート（angel_return.md）とセクション数・構成が整合していることを確認する
- `Grep` で `Ep.\d` パターンの残存を確認する
