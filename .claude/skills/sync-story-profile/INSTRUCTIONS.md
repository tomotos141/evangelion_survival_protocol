# Story Profile Sync（設計変更のProfile同期）

設計ドキュメントの変更内容を Story Profile に反映する。

## Input

- **プロジェクト名**: 引数で渡されたパス or 直近の作業から推定
- **変更の範囲**: 引数で指定 or `git diff` から自動検出

## Phase 1: 変更内容の把握

1. `git diff --stat` と `git diff` で直近の変更ファイルと差分を確認する
2. 変更を以下のカテゴリに分類する:
   - **プロット変更**: `docs/overall_plot_v2.md` 等
   - **キャラクター変更**: `docs/characters/*.md`
   - **エピソード変更**: `docs/episodes/*.md`
   - **Author DNA 変更**: `.agent/author_profile.md`
   - **その他**: テンプレート、スキル等

## Phase 2: Story Profile の読み込みと差分分析

1. `.agent/profiles/{project}.md` を `Read` で読み込む
2. 変更カテゴリごとに、Story Profile の該当セクションを特定する:

| 変更カテゴリ | Story Profile の影響セクション |
|-------------|-------------------------------|
| プロット（テーマ・設計原則） | §3 テーマ, §6 構造設計原則 |
| プロット（結末・恋愛） | §3 テーマ（該当部分） |
| キャラクター（Lie/Truth変更） | §5 キャラクター・ダイナミクス |
| キャラクター（新規追加） | §5 に項目追加 |
| エピソード（新シーン追加） | §6 構造設計原則（該当する場合のみ） |
| エピソード（禁止事項違反） | §8 禁止事項 |
| Author DNA | §1-§4 の該当箇所 |

3. 各変更について「Story Profile に反映が必要か」を判定する:
   - **必要**: テーマ・Lie・禁止事項・構造原則の変更
   - **不要**: エピソード内の細部変更、表現レベルの修正

## Phase 3: 更新案の提示

Before/After 形式で更新案を提示する:

```markdown
# Story Profile 同期提案: {project_name}

## 変更元
- [変更ファイル1]: [変更の要約]
- [変更ファイル2]: [変更の要約]

## 更新案

### §X [セクション名]
**Before**:
> [現在の記述]

**After**:
> [提案する記述]

**理由**: [なぜこの変更が必要か]
```

## Phase 4: 適用

ユーザーが承認した更新案のみ `Edit` ツールで Story Profile に反映する。

## 注意事項

- Story Profile は Writer/Editor エージェントが執筆時に参照する。冗長な情報は入れず、**行動指針として使える粒度** を維持する。
- キャラクターの詳細は `docs/characters/` に委任し、Story Profile には Lie と Theme Answer の要約のみ記載する。
- `git diff` がない場合（未コミットの変更）は、ユーザーに変更内容を確認する。
