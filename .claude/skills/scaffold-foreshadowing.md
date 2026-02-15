---
name: scaffold-foreshadowing
description: デザインドキュメントから伏線管理表を生成するスキル。team-scaffold-project から呼び出されるほか、単体でも使用可能。
---

# 伏線管理表生成スキル

デザインドキュメントの伏線設計を入力として、執筆・レビュー時に参照する伏線管理表を生成する。

## 入力

- **design_doc**: デザインドキュメントのパス
- **project_path**: プロジェクトパス（例: `projects/battousai`）

## 出力

- `{project_path}/docs/foreshadowing.md`

## 参照テンプレート

- `projects/angel_return/docs/foreshadowing.md` を `Read` で読み込み、フォーマットのテンプレートとして使用する

## 手順

1. デザインドキュメントの伏線管理セクション（§10 等）を `Read` で確認する
2. テンプレート（angel_return の foreshadowing.md）を `Read` で読み込む
3. 以下の構成で伏線管理表を作成する

### ドキュメント構成

```markdown
# Foreshadowing Tracker: [タイトル]（[読み]）

## Status Legend
| Status | Description |
| :--- | :--- |
| 🔴 Unresolved | 提示済みだが未回収 |
| 🟡 In Progress | 進行中・部分的に触れられている |
| 🟢 Resolved | 完全に回収済み |

## 1. Main Themes (テーマ伏線)
| ID | Subject | Setup | Develops | Resolution | Status |
|---|---|---|---|---|---|

## 2. Character Arcs (キャラクター伏線)
| ID | Subject | Setup | Develops | Resolution | Status |
|---|---|---|---|---|---|

## 3. [作品固有のカテゴリ] (例: Erosion, Abilities, Politics)
| ID | Subject | Setup | Develops | Resolution | Status |
|---|---|---|---|---|---|
```

## 作成ルール

- デザインドキュメントの伏線テーブルを展開し、各伏線に一意の ID を付与する（F-001, F-002, ...）
- Setup / Develops / Resolution の各列には話数を `第X話` 形式で記載する
- 初期状態では全て `🔴 Unresolved` とする（まだ執筆前のため）
- カテゴリはデザインドキュメントの伏線の種類に応じて柔軟に設定する
  - テーマ伏線、キャラクター伏線は必須
  - 作品固有の伏線カテゴリ（侵食、能力、政治 等）はデザインに応じて追加
- 伏線の Subject は簡潔に（10文字以内を目安）

## 検証

- デザインドキュメントに定義された全ての伏線ラインがカバーされていることを確認する
- ID が一意であることを確認する
- `Grep` で `Ep.\d` パターンの残存を確認する
