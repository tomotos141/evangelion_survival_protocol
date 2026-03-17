---
name: writing-report
description: "Analyze writing session logs to produce reports — episode scores, retry rates, word count trends, project progress. Use when explicitly invoked with /writing-report."
argument-hint: "[today|week|all|project-name]"
disable-model-invocation: true
user-invocable: true
---

# /writing-report — 執筆レポート

ACTIONLOG（JSONL）を集計し、執筆セッションの振り返りレポートを出力する。
`/evolve` の入力としても使える。

**参照ファイル**:
- `.claude/skills/team-write-episode/reference/actions.jsonl` — 新規執筆ログ
- `.claude/skills/team-rewrite-episode/reference/actions.jsonl` — リライトログ

---

## Step 1: ログ読み込み

両方の JSONL ファイルを読み込む:

```bash
cat .claude/skills/team-write-episode/reference/actions.jsonl 2>/dev/null
cat .claude/skills/team-rewrite-episode/reference/actions.jsonl 2>/dev/null
```

ファイルが存在しないか空の場合:
> 執筆ログがまだないわ。`/team-write-episode` や `/team-rewrite-episode` でエピソードを書くと自動的に記録されるわよ。

## Step 2: フィルタ

引数に応じてフィルタ:
- **引数なし or "today"**: 今日の日付
- **"week"**: 直近7日間
- **"all"**: 全件
- **プロジェクト名**（例: "battousai"）: そのプロジェクトの全件

## Step 3: 集計・レポート出力

```
📊 執筆レポート（<期間>）

■ サマリー
  - 新規執筆: <N>話（team-write-episode）
  - リライト: <N>話（team-rewrite-episode）

■ プロジェクト別
  - <project>: <n>話（平均スコア <avg>/100）
  - <project>: <n>話（平均スコア <avg>/100）

■ スコア推移
  | エピソード | E | P | 合計 | リトライ | 文字数 | 結果 |
  |-----------|---|---|------|---------|--------|------|
  | <episode> | <editor> | <proofreader> | <total> | <retries> | <words> | <outcome> |

■ 傾向分析
  - 平均スコア: <avg>/100（E: <avg_e>/50, P: <avg_p>/50）
  - 一発通過率: <pct>%（リトライ0回の割合）
  - 平均文字数: <avg_words>字
  - 最高スコア: <max> (<episode>)
  - 最低スコア: <min> (<episode>)

■ 弱点分析
  - Editor で最も低い軸: <axis>（平均 <avg>）
  - Proofreader で最も低い軸: <axis>（平均 <avg>）
```

## Step 4: 改善提案

スコアパターンから自動的に改善提案を生成する:

| パターン | 提案 |
|---------|------|
| Engagement & Emotion が常に低い | フック・クリフハンガーの強化を Writer に指示 |
| Character Integrity が常に低い | キャラ設定ファイルの DO/DON'T を見直す |
| リトライ率が50%超 | Writer の事前参照ファイルを増やす |
| 文字数が7000未満が多い | 散文密度の指示を強化する |
| Prose & Voice が常に低い | Author DNA §4 Natural Prose の見直し |
