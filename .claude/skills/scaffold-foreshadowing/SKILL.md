---
name: scaffold-foreshadowing
description: Generates foreshadowing tracking table from design document with unique IDs and status indicators. Use when creating a foreshadowing tracker from a completed design document.
---

# scaffold-foreshadowing

デザインドキュメントの伏線設計を入力として、執筆・レビュー時に参照する伏線管理表を生成する。

---

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

## 依存

- デザインドキュメント §10（伏線管理セクション）
- `projects/angel_return/docs/foreshadowing.md` — フォーマットテンプレート

## Telemetry

スキル完了時に actions.jsonl に追記:

```bash
cat >> .claude/skills/scaffold-foreshadowing/reference/actions.jsonl << JSONL
{"timestamp":"$(date -u +%Y-%m-%dT%H:%M:%SZ)","skill":"scaffold-foreshadowing","action":"scaffold","input_summary":"[入力要約]","output_summary":"[結果要約]","issues":[],"successes":[],"user_feedback":"none"}
JSONL
```
