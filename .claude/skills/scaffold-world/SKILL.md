---
name: scaffold-world
description: Generates world-building setting files from design document with sensory-rich descriptions.
---

# scaffold-world

デザインドキュメントの世界観定義を入力として、Writer が執筆時に参照する世界観設定ファイルを生成する。

---

## 入力

- **design_doc**: デザインドキュメントのパス
- **project_path**: プロジェクトパス（例: `projects/battousai`）

## 出力

- `{project_path}/docs/world/*.md`（設定領域ごとに1ファイル）

## 手順

1. デザインドキュメントの世界観関連セクション（§7, §9 等）を `Read` で確認する
2. 設定を意味のある単位でファイルに分割する
3. 各ファイルを `Write` で保存する

## ファイル分割の指針

デザインドキュメントの内容に応じて、以下のような分割を行う:

| 設定領域 | ファイル名の例 |
|---|---|
| 舞台の場所・時代 | `bakumatsu_kyoto.md`, `neo_tokyo.md` |
| 能力体系・戦闘システム | `hiten_mitsurugi.md`, `eva_abilities.md` |
| 社会構造・組織 | `society.md`, `nerv_structure.md` |
| コアルール | `core_rules.md`, `hard_mode_guidelines.md` |

ファイル数は2〜5を目安とする。1ファイルに詰め込みすぎず、かといって細分化しすぎない。

## 各ファイルに含めるべき要素

### 舞台設定ファイル

- **場所のリスト**: 物語に登場する場所と、各場所の五感描写素材（匂い、音、温度、質感、光）
- **時間帯と天候**: 物語の時間進行に影響する要素
- **生活描写の素材集**: 食事、衣服、道具、日常動作——Writer が日常シーンを書く際の素材
- **社会状況**: 物語に必要な最小限の社会・政治状況
- **描写ルール**: この舞台に固有の描写上のルールや禁止事項

### 能力/戦闘設定ファイル

- **技・能力のリスト**: 名称、身体描写（どう動くか、何が見えるか、何が聞こえるか）、使用場面の指定
- **身体性**: 能力の使用に伴う身体的制約・代償
- **対比構造**: 主人公 vs ライバルの技の対比ポイント
- **使用ルール**: 技名・能力名の使用頻度と演出ルール

## 参照テンプレート

- `.agent/templates/world_building_template.md` — Sensory Palette（主軸感覚+対比設計）と Objects of Significance を含む

## 作成ルール

- 執筆時の参照資料として使えるよう、**具体的な描写の素材**を豊富に入れる
- 辞書的な説明ではなく、五感で描写できる素材集として構成する
- Author DNA §2 Non-Visual First を意識し、視覚以外の感覚素材を充実させる
- **Sensory Palette**: 主軸感覚（battousai=嗅覚、blind_spot=触覚 等）を定め、対比構造を設計する
- **Objects of Significance**: 物語上で象徴的な意味を持つアイテムを管理する
- 歴史的・科学的考証が必要な場合は「物語の都合で曲げてよい範囲」を明記する
- Story Grid の Inside-Out 原則: 百科事典的情報は不要。**物語機能を果たす設定のみ**構築する

## 検証

- 全ファイルが `{project_path}/docs/world/` に配置されていることを確認する
- Story Profile の世界設定セクション（§4）と矛盾がないことを確認する
