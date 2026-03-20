# Quality Gate v3 — 5軸採点仕様

## 概要

5軸・100点満点。閾値 **80/100** で通過。最大 **3回** 自動リトライ。

| 軸 | 配点 | エージェント | フォーカス |
|---|---|---|---|
| Editor | 25 | editor | 技巧と没入 |
| Proofreader | 25 | proofreader | 整合と美学 |
| First Reader | 20 | first-reader | 初読者体験 |
| Mystery Auditor | 15 | mystery-auditor | ミステリー構造 |
| Freshness Check | 15 | freshness-checker | AI臭検出 |
| **合計** | **100** | | |

## 並列起動パターン

5エージェントを **全て並列で** 起動する（依存関係なし）。

**Wave 1（並列）:**
1. editor（25pt）
2. proofreader（25pt）
3. first-reader（20pt）
4. mystery-auditor（15pt）— ミステリー要素がある場合のみ
5. freshness-checker（15pt）

全員の完了を待ってスコアを合算する。

## Editor 担当（25点）— 技巧と没入

| 軸 | 配点 | 観点 |
|---|---|---|
| Engagement & Emotion | /10 | フック、没入度、感情的インパクト、不穏さ、予定調和回避 |
| Plot & Pacing | /8 | シーン構成、テンション曲線、Scene & Sequel、MRU順序 |
| Prose & Voice | /7 | 散文密度、語りの声の一貫性、文長バリエーション |

## Proofreader 担当（25点）— 整合と美学

| 軸 | 配点 | 観点 |
|---|---|---|
| Character Integrity | /10 | 口調、行動指針 DO/DON'T、Arc段階整合、関係性描写、呼称 |
| World & Continuity | /8 | 時系列、設定矛盾、前話接続、固有名詞、地理・天候 |
| Author Rules & Aesthetics | /7 | Author DNA 遵守、Story Profile 美学・禁止事項、伏線管理 |

## First Reader 担当（20点）— 初読者体験

| 軸 | 配点 | 観点 |
|---|---|---|
| Hook（冒頭吸引力） | /8 | 冒頭500字の引き、1話目の「掴み」 |
| Retention（離脱防止） | /6 | 中盤の弛み、退屈ポイントの有無 |
| Next-want（次読み動機） | /6 | ラストの余韻、ブックマーク判定 |

## Mystery Auditor 担当（15点）— ミステリー構造

| 軸 | 配点 | 観点 |
|---|---|---|
| Clue Fairplay | /5 | 手がかり配置、フェアプレイ、ミスリード |
| Rule Consistency | /5 | 世界ルール遵守、後出し設定なし |
| Secret Management | /5 | 開示バランス、論理の穴 |

**ミステリー要素がない場合:** スキップし、15pt を Editor（+8pt → 33pt）と Proofreader（+7pt → 32pt）に再配分。

## Freshness Check 担当（15点）— AI臭検出

| 軸 | 配点 | 観点 |
|---|---|---|
| Pattern | /5 | 構文パターン反復、文体均質性 |
| Template | /5 | テンプレ展開、抽象語空回り |
| Explanation Economy | /5 | 同義語連打、説明過多、AIらしい丁寧さ |

## 採点基準

| 範囲 | 評価 |
|------|------|
| 90%以上 | 卓越。修正不要 |
| 80-89% | 良好。軽微な改善余地 |
| 60-79% | 及第。改善が必要 |
| 40-59% | 不十分。重大な改善が必要 |
| 40%未満 | 要全面書き直し |

## v2 → v3 変更履歴

- **v2**: Editor(50) + Proofreader(50) = 100pt, 2軸並列
- **v3**: Editor(25) + Proofreader(25) + First Reader(20) + Mystery Auditor(15) + Freshness Check(15) = 100pt, 5軸並列
- 変更理由: 読者体験、ミステリー整合性、AI臭検出の独立評価が品質向上に寄与するため
- Mystery Auditor は条件付き（ミステリー要素がある作品のみ）
