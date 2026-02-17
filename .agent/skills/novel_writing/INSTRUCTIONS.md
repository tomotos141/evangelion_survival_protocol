# Novel Writing Skill

## 前提

執筆前に以下を必ず `Read` で読み込むこと:
- `.agent/author_profile.md` — Author DNA（散文密度 §3、Natural Prose §4 を含む全ルール）
- `.agent/profiles/<project>.md` — Story Profile（作品固有のトーン・キャラ・ルール）

## Technical Constraints（技術的制約）

- **File Encoding**: Pixiv用ファイルは **UTF-8 with BOM** で出力すること。日本語の文字化けに厳重注意。
- **File Overwrite Safety (CRITICAL)**: 既存ファイルを `Write` で上書きする前に、必ず `Read` で現在の内容を確認する。追記が必要な場合は `Edit` ツールを使う。

## Writing Rules（執筆ルール）

- **メタ発言禁止**: 「脚本」「演出」「フラグ」等のメタ的比喩、ゲーム用語は厳禁。
- **エピソード番号参照禁止（CRITICAL）**: 地の文で `Ep.5の夜` のようなエピソード番号参照を使わない。`あの夜`、`ラミエル戦`、`あの白い部屋` 等の作中表現で参照する。
- **Show, Don't Tell**: 感情を直接語らず、身体反応・行動・五感で表現する。
- **散文密度・Natural Prose**: → Author DNA §3, §4 を遵守。

## Common Workflows

### Starting a New Project

1. ジャンルとコアとなるアイデアをヒアリングする。
2. ディレクトリ構造を提案する（例：`docs/characters`, `docs/world`, `drafts/`, `dist/pixiv/`）。
3. ログライン（一行あらすじ）やあらすじの作成を支援する。

### Character Creation

1. 基本的なアーキタイプや役割を聞く。
2. Q&Aを通じて詳細を肉付けする。
3. プロフィールを `docs/characters/[name].md` に保存する。

### Episode Design

1. 全体プロット（`docs/overall_plot.md`）と前回の引き継ぎを確認する。
2. シーン構成を設計し、`docs/episodes/ep##_title.md` に保存する。
3. ユーザーの承認を得てから執筆に進む。

### Scene Writing

1. シーンの目的（Goal）を定義する。
2. 誰の視点（POV）かを決定する（Story Profile の視点定義に従う）。
3. **シーン骨格の選択**:
   - 戦闘シーン → Battle Tempo（Author DNA §6）
   - 非戦闘シーン → Scene & Sequel（Author DNA §2）
4. **設定の参照**: `docs/world/` 配下の関連設定ファイルを参照する。
5. 本文を執筆する。MRU順序（刺激→感情→反射→理性的行動）を守る。`***` でシーンを区切る。

### Post-Drafting（脱稿後の処理）

エピソードの執筆が完了したら、以下を**自動的に**実行または提案する：

1. **キャプション作成**: ドラフト末尾の `[caption]...[/caption]` ブロックとして作成する。
2. **Pixiv版生成**: `dist/pixiv/XX_title_pixiv.txt` を生成する。変換ルールは `.claude/agents/publisher.md` を参照。
3. **キャプション追記**: `dist/pixiv/caption.txt` に `[第X話キャプション]` を追記する。
4. **メタ参照チェック**: `Grep` で `Ep.\d` パターンの残存を確認する。
5. **ドキュメント更新**: `docs/overall_plot.md`, `docs/foreshadowing.md` を更新する。
