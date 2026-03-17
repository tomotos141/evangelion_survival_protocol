# Quality Gate v2 — 採点仕様

## 概要

Editor（50点）+ Proofreader（50点）= 100点満点。
閾値 **80/100** で通過。最大 **3回** 自動リトライ。

## Editor 担当（50点）— 技巧と没入

| 軸 | 配点 | 観点 | 根拠 |
|---|---|---|---|
| Engagement & Emotion | /20 | フック、没入度、感情的インパクト、不穏さ、予定調和回避 | Book-Length Study (2025): 主観側で読者満足度と最高相関 |
| Plot & Pacing | /15 | シーン構成、テンション曲線、Scene & Sequel、MRU順序、Battle Tempo | 全フレームワーク横断で最も普遍的な評価軸 |
| Prose & Voice | /15 | 散文密度、Natural Prose、AI臭排除、語りの声の一貫性、文長バリエーション | Mozaffari (2013) で独立軸。ただし実証上差がつきにくいため /15 |

**出力フォーマット（レポート末尾に必須）:**

```
## Editor Score: XX/50
- Engagement & Emotion: XX/20
- Plot & Pacing: XX/15
- Prose & Voice: XX/15
```

## Proofreader 担当（50点）— 整合と美学

| 軸 | 配点 | 観点 | 根拠 |
|---|---|---|---|
| Character Integrity | /20 | 口調、行動指針 DO/DON'T、Arc段階整合、関係性描写、呼称 | Book-Length Study (2025): 客観側で読者満足度と最高相関 |
| World & Continuity | /15 | 時系列、設定矛盾、前話接続、固有名詞、地理・天候 | 全フレームワーク横断で出現する普遍軸 |
| Author Rules & Aesthetics | /15 | Author DNA 遵守、Story Profile 美学・禁止事項、伏線管理 | 著者固有軸（外部フレームワークにない独自次元） |

**出力フォーマット（レポート末尾に必須）:**

```
## Proofreader Score: XX/50
- Character Integrity: XX/20
- World & Continuity: XX/15
- Author Rules & Aesthetics: XX/15
```

## 採点基準

| 範囲 | 評価 |
|------|------|
| 90%以上 | 卓越。修正不要 |
| 80-89% | 良好。軽微な改善余地 |
| 60-79% | 及第。改善が必要 |
| 40-59% | 不十分。重大な改善が必要 |
| 40%未満 | 要全面書き直し |

## 設計根拠

- 重複なし: 各エージェントが自分の専門軸のみ採点
- Engagement + Character に /20: 読者満足度と最高相関（Book-Length Study）
- Prose は /15: 差がつきにくい実証データ（Mozaffari 2013）
- リサーチレポート: `docs/research/fiction_evaluation_rubrics.md`
