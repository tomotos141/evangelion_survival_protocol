---
name: scaffold-characters
description: Generates individual character files from design document. Creates Ghost/Lie chains, voice samples, and behavioral rules. Use when scaffolding character files from a completed design document.
---

# scaffold-characters

デザインドキュメントのキャラクター定義を入力として、個別のキャラクター設定ファイルを生成する。

---

## 入力

- **design_doc**: デザインドキュメントのパス
- **project_path**: プロジェクトパス（例: `projects/battousai`）

## 出力

- `{project_path}/docs/characters/{character_name}.md`（キャラクターごとに1ファイル）

## 参照テンプレート

- `.agent/templates/character_template_generic.md` を `Read` で読み込み、Ghost/Lie/Want/Need チェーン含むフォーマットとして使用する
- 二次創作の場合は既存キャラファイル（例: `projects/angel_return/docs/characters/shinji_ikari.md`）も参考にする

## 手順

1. デザインドキュメントの §5（キャラクター・ダイナミクス）を `Read` で確認する
2. テンプレート（shinji_ikari.md）を `Read` で読み込む
3. デザインドキュメントに定義された各キャラクターについて、以下の構成でファイルを作成する

### ファイル構成

```markdown
# キャラクター設定: [名前] ([英語タグ])

## 1. Basic Info (基本情報)
- 名前、年齢（わかる場合）、所属、役割

## 2. Core Concept (核心)
> 一行で本質を表す

## 3. Personality & Voice (性格・口調)
- 性格の概要
- 口調サンプル（台詞例2〜3個。場面ごとに異なる場合は場面を明記）
- **Behavioral Rules**:
  - **DO**: このキャラクターらしい行動・描写
  - **DON'T**: このキャラクターがやってはいけない行動・描写

## 4. Theme Answer (テーマへの回答)
> 中心テーマに対するこのキャラクターの回答

## 5. Arc (変化の軌跡)
> 話数ごとの段階的変化

## 6. Relationships (人間関係)
- 他キャラクターとの関係を具体的に

## 7. Combat Style (戦闘スタイル) ※該当する場合のみ
- 流派、身体性、剣/武器の質感
- 戦い方がキャラクターのテーマ回答をどう体現するか
```

## 作成ルール

- デザインドキュメントの記述を深化・具体化する。コピペではなく、Writer が参照して即座に書けるレベルの具体性を持たせる
- **口調サンプル**: 最低2例。場面や感情状態で口調が変わるキャラクターは、各状態のサンプルを書く
- **DO/DON'T**: このキャラクターの「らしさ」を守るための具体的なガードレール。曖昧な表現（「自然に」「適切に」）ではなく、具体的な行動レベルで書く
- **Arc**: 話数を明記する。ただし `Ep.X` 形式ではなく `第X話` または `(X話)` の形式を使う
- **Relationships**: 他キャラクターとの関係の質（信頼、敵対、共犯、利用 等）と、その関係が物語を通じてどう変化するかを書く
- **Combat Style**: 戦闘に関わらないキャラクターにはこのセクションを作らない
- Ghost / Lie / Want / Need チェーンは全キャラクターに必須（§6 として配置）。デザインドキュメントに未定義の場合はキャラクター設定から推定して作成する

## Character Web の作成

キャラクター個別ファイルに加えて、`{project_path}/docs/characters/_character_web.md` を作成する:
- `.agent/templates/character_web_template.md` を参照
- テーマ回答マトリクス、関係性マトリクス、対比の設計を含む
- 全キャラクターが相互関係の網として機能していることを検証する

## 検証

- 全キャラクターのファイルが作成されていることを確認する
- 各ファイルの Theme Answer が中心テーマと整合していることを確認する
- `Grep` で `Ep.\d` パターンの残存を確認する

## 依存

- `.agent/templates/character_template_generic.md` — キャラクターテンプレート
- `.agent/templates/character_web_template.md` — Character Web テンプレート
- デザインドキュメント §5（キャラクター・ダイナミクス）

## Telemetry

スキル完了時に actions.jsonl に追記:

```bash
cat >> .claude/skills/scaffold-characters/reference/actions.jsonl << JSONL
{"timestamp":"$(date -u +%Y-%m-%dT%H:%M:%SZ)","skill":"scaffold-characters","action":"scaffold","input_summary":"[入力要約]","output_summary":"[結果要約]","issues":[],"successes":[],"user_feedback":"none"}
JSONL
```
