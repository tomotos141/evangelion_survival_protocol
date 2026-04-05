---
name: check-arc-consistency
description: Character arc consistency checker. Cross-references Status Evolution Logs against episode scene designs to detect misalignment. Use when verifying character arcs match episode scenes after plot or character changes.
---

# check-arc-consistency

キャラクターファイルの Status Evolution Log と、エピソードのシーン構成・構造的仕掛けを突合し、不整合を検出する。

---

## Input

- **プロジェクト名**: 引数で渡された名前 or パスから導出
- **スコープ**: `all`（全キャラ×全エピソード）or 特定キャラ/エピソードを指定

## Phase 1: データ収集

1. `Glob` で `docs/characters/*.md` の一覧を取得
2. 各キャラクターファイルから以下を抽出:
   - **Ghost / Lie / Truth** チェーン
   - **Status Evolution Log** の各 Act エントリ（状態・変化の記述）
3. `Glob` で `docs/episodes/ep*.md` の一覧を取得
4. 各エピソードファイルから以下を抽出:
   - **シーン構成**: 各シーンの登場キャラクターと行動
   - **構造的な仕掛け**: 設計意図テーブル

## Phase 2: 突合チェック

以下の3つの観点でチェックする:

### Check A: エピソード → キャラクターアーク（前方チェック）

エピソード内でキャラクターが **重要な行動や変化** を見せているシーンが、そのキャラクターの Status Evolution Log に記載されているか。

重要な行動の基準:
- Lie に関わる行動（Lie の発露、Lie への亀裂、Lie の粉砕）
- 他キャラとの関係の転換点
- テーマへの回答に繋がる選択
- 構造的な仕掛けテーブルに記載されている行動

### Check B: キャラクターアーク → エピソード（後方チェック）

Status Evolution Log に記載されている変化が、対応するエピソードのシーン構成に **具体的な場面として** 存在するか。

アーク表に「〜する」と書いてあるのに、エピソードにそのシーンがない場合は不整合。

### Check C: Lie チェーン整合性

- キャラクターの Lie が物語内で **駆動力** として機能しているか（Lie に基づく行動が各 Act に存在するか）
- Truth に到達する（または到達しない）過程が、エピソード上で段階的に描かれているか
- Pressure Point が実際にエピソード内で発火しているか

## Phase 3: レポート出力

```markdown
# アーク整合性チェック: {project_name}

## 不整合リスト

### [キャラクター名] — [Act X]
- **種別**: エピソード未反映 / アーク未記載 / Lie チェーン断絶
- **エピソード側**: [ep_XX のシーン Y で〜している]
- **アーク側**: [Act X の記述: "〜"]
- **不整合**: [何が食い違っているか]
- **修正提案**: [どちらを修正すべきか]

## 整合確認済み
- [キャラクター名]: 全 Act で整合（簡潔に）
```

## Phase 4: 修正（オプション）

ユーザーが修正を指示した場合:
- キャラクターファイルの Status Evolution Log を `Edit` で更新
- または エピソードファイルのシーン構成を `Edit` で更新
- 修正後、影響範囲を再チェック

## 注意事項

- `original_cast.md` に複数キャラが含まれる場合、それぞれ個別にチェックする。
- 「痕跡のみ」のキャラクター（霧島マナ等）はアークチェックの対象外。データログ等での言及のみ確認。
- overall_plot_v2.md の Act サマリとの突合は本スキルのスコープ外（`audit-design` で対応）。

## 依存

- `docs/characters/*.md` — キャラクター設定（Ghost/Lie/Truth チェーン、Status Evolution Log）
- `docs/episodes/ep*.md` — エピソードデザイン（シーン構成、構造的仕掛け）

## Telemetry

**このステップはスキル完了時に必ず実行すること。省略は禁止。**

スキル完了時に actions.jsonl に追記:

```bash
cat >> .claude/skills/check-arc-consistency/reference/actions.jsonl << JSONL
{"timestamp":"$(date -u +%Y-%m-%dT%H:%M:%SZ)","skill":"check-arc-consistency","action":"analyze","input_summary":"[入力要約]","output_summary":"[結果要約]","issues":[],"successes":[],"user_feedback":"none"}
JSONL
```
