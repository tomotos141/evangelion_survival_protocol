---
name: audit-design
description: 設計ドキュメント（プロット等）を Author DNA・Story Profile・作者の好み変遷と突合し、乖離点を構造化レポートで出力する設計監査スキル。「設計監査」「audit design」「プロットと好み一致してる？」で発動する。
---

# Design Audit（設計監査）

設計ドキュメントが現在の著者美学と整合しているかを監査し、構造化レポートを出力する。

## Input

- **対象ドキュメント**: 引数で渡されたパス（省略時はユーザーに確認）
- 典型的な対象: `docs/overall_plot_v2.md`, `docs/episodes/ep*.md` 等

## Phase 1: 基準の読み込み

以下の3ファイルを `Read` で読み込む:

1. **Author DNA**: `.agent/author_profile.md`
2. **Story Profile**: 対象ファイルのパスからプロジェクト名を導出し、`.agent/profiles/{project}.md` を読む
3. **作者の好み変遷**: メモリディレクトリ内の `author_evolution.md`（存在する場合）

## Phase 2: 対象の読み込みと分析

1. 対象ドキュメントを `Read` で全文読み込む
2. 以下の観点で Author DNA / Story Profile / 好み変遷と突合する:

### チェック項目

| # | 観点 | 確認内容 |
|---|------|---------|
| 1 | **Core Techniques** | Vulnerability as Climax, Silence as Dialogue, Physical Opening, Multiple Answers, Heartbeat Rule, Unresolved Beauty が設計に反映されているか |
| 2 | **Narrative Style** | Non-Visual First, One-Shot Metaphor, Sensory Shift, Prose Density が意識された構造になっているか |
| 3 | **Structural Preferences** | 円環/対称、剥ぎ取り、日常の聖性、不在の存在、No Cheap Integration が設計に組み込まれているか |
| 4 | **Battle & Machine** | Erosion, Battle Tempo, Fighting Style = Identity が戦闘設計に反映されているか |
| 5 | **Story Profile 固有ルール** | 作品固有の禁止事項、キャラクターの Lie チェーン、テーマへの回答が設計と矛盾していないか |
| 6 | **好み変遷との整合** | author_evolution.md に記載された「後期の好み」（身体的手触り、書かない技法、微細な選択の積み重ね）に設計が追いついているか |
| 7 | **Forbidden** | Author DNA §7 および Story Profile の禁止事項に違反する要素がないか |

## Phase 3: レポート出力

以下のフォーマットで出力する:

```markdown
# 設計監査レポート: {対象ファイル名}

## 一致点（設計が美学と合致している要素）
- [要素名]: [なぜ合致しているかの簡潔な説明]

## 乖離点（修正が必要な要素）

### [重要度: Critical / High / Medium / Low]
- **乖離**: [何が合っていないか]
- **基準**: [Author DNA / Story Profile / 好み変遷のどの項目と矛盾するか]
- **提案**: [具体的な修正の方向性]

## 欠落（設計に存在すべきだが見当たらない要素）
- [欠落要素]: [なぜ必要か、どこに追加すべきか]
```

重要度の基準:
- **Critical**: テーマや禁止事項との直接的な矛盾
- **High**: Core Techniques の未反映、キャラクター Lie チェーンとの不整合
- **Medium**: Structural Preferences の部分的な欠落
- **Low**: 好み変遷の最新傾向が未反映（装飾的要素の残存等）

## 注意事項

- レポートは修正を **提案** するのみ。実際の修正はユーザーの判断を仰ぐ。
- 「一致点」も必ず記載する。何が良いかを明示しないと、何を守るべきかが分からない。
- 1つの乖離に対して複数の修正案がある場合は、選択肢として提示する。
