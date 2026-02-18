# SNS運用 + 表紙 実装計画

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 濁刃（battousai）の表紙画像3点を制作し、X創作アカウントの設計ドキュメントと初動告知テンプレート一式を整備する

**Architecture:** 画像生成（ComfyUI）→ 文字入れ（Canva/Photopea）→ ドキュメント整備（告知テンプレ4〜6話追加、固定ポスト、Xセットアップガイド）→ 運用スケジュール作成。画像制作はユーザー側の手作業だが、プロンプトとガイドをClaude側で用意する

**Tech Stack:** ComfyUI (Stable Diffusion), Canva/Photopea (typography), Markdown docs

**Design doc:** `docs/plans/2026-02-19-sns-cover-design.md`

---

## Task 1: ComfyUI用プロンプトガイド作成

表紙画像3点（Pixivシリーズ表紙・Xヘッダー・Xアイコン）をComfyUIで生成するためのプロンプトとパラメータを記載したガイドを作成する。

**Files:**
- Create: `docs/marketing/cover_art_guide.md`

**Step 1: プロンプトガイドを作成**

以下の内容を含むガイドを書く:

- 3点それぞれの推奨プロンプト（positive/negative）
- 推奨モデル（SDXL系リアリスティックモデル: Juggernaut XL, RealVisXL 等）
- 推奨パラメータ（解像度、steps、CFG scale、sampler）
- 色彩設計の参照（設計書 §1 の色彩設計に準拠）
- 文字入れ手順（Canva/Photopea での手順概要）
- 推奨フォント（筆書き風: 衡山毛筆フォント、源界明朝）

**プロンプト設計方針:**
- Pixivシリーズ表紙（1200×1600 縦長）: `japanese katana hilt in rain, rusty iron texture, dark atmospheric, blood stains on blade, traditional japanese aesthetic, moody lighting, cinematic, dark color palette` 系
- Xヘッダー（1500×500 横長）: `rainy kyoto alley at night, edo period, dark atmospheric, lantern light, wet cobblestone, cinematic wide shot` 系
- Xアイコン（400×400 正方形）: `extreme close-up of japanese sword tsuba guard, rusty iron texture, dark patina, centered composition` 系
- Negative共通: `text, watermark, signature, anime, cartoon, illustration, person, face, hands, bright colors, cheerful`

**Step 2: 確認**

ガイドを読み返し、3点の画像の方向性が「染み鉄」美学（錆・血潮・灰の色彩）と一致しているか確認する。

**Step 3: コミット**

```bash
git add docs/marketing/cover_art_guide.md
git commit -m "docs: Add ComfyUI cover art prompt guide for battousai"
```

---

## Task 2: SNS告知テンプレート 4〜6話追加

既存の `sns_announcement_guide.md` に第4話「同居」〜第6話「傷痕」の告知テンプレートを追加する。

**Files:**
- Modify: `docs/marketing/sns_announcement_guide.md`

**Step 1: 4〜6話の告知テンプレートを追加**

既存の1〜3話テンプレートの直後に追加する。フック文は `caption.txt` の各話キャプションから最もインパクトのある1〜2文を抽出する。

```
### 第4話「同居」
```
飯を焦がす手、箸を強く握りすぎる指。
人の骨を断てる手が、薪一本割れない。

濁刃 第4話「同居」
https://www.pixiv.net/novel/show.php?id=XXXXXXXX

#るろうに剣心 #二次創作小説
```

### 第5話「灰刃」
```
殺気のない空虚。音のない刀。完璧に美しく、そして空。
鏡の中の未来が、人間の形をしていなかった。

濁刃 第5話「灰刃」
https://www.pixiv.net/novel/show.php?id=XXXXXXXX

#るろうに剣心 #二次創作小説
```

### 第6話「傷痕」
```
仇の男と暮らして幾日。文の紙が柔らかくなっていた。
何も起きない夜が、一番遠くまで連れていく。

濁刃 第6話「傷痕」
https://www.pixiv.net/novel/show.php?id=XXXXXXXX

#るろうに剣心 #二次創作小説
```
```

**Step 2: 確認**

テンプレートが既存の1〜3話と同じフォーマット・トーンで揃っているか確認する。

**Step 3: コミット**

```bash
git add docs/marketing/sns_announcement_guide.md
git commit -m "docs: Add SNS announcement templates for Ep.04-06"
```

---

## Task 3: Xアカウントセットアップガイド作成

Xアカウントの作成から初期設定までの手順書を作成する。ユーザーが迷わず設定できるように具体的に書く。

**Files:**
- Create: `docs/marketing/x_account_setup.md`

**Step 1: セットアップガイドを作成**

以下の内容を含む:

1. **アカウント作成手順**
   - 新規Xアカウントを作成（メールアドレス or 電話番号で登録）
   - ID（@ハンドル）の選び方のガイドライン: 短く、覚えやすく、作者名ベース
   - 表示名: `[ペンネーム]@濁刃 連載中`

2. **プロフィール設定**
   - プロフィール文（設計書 §2 のテキストをそのまま使用）:
     ```
     剣が冴えるほど人間が消える——
     幕末剣劇『濁刃（だくじん）』連載中。るろうに剣心 追憶編を下敷きにした全10話。
     [Pixivシリーズ URL]
     ```
   - アイコン画像: ComfyUIで生成した正方形画像（Task 1 参照）
   - ヘッダー画像: ComfyUIで生成した横長画像（Task 1 参照）
   - Web: PixivプロフィールURL

3. **固定ポスト**
   - シリーズ紹介文 + Pixivシリーズページへのリンク + 表紙画像を添付
   - テキスト案:
     ```
     剣が冴えるほど人間が消える。

     幕末の京都。長州の影の刃として名前のない仕事を重ねる少年。振るうほど鋭くなる刀——けれど、掌から鉄錆の匂いだけが消えない。

     るろうに剣心 追憶編を下敷きにした幕末剣劇『濁刃（だくじん）』全10話・連載中。

     [Pixivシリーズ URL]

     #るろうに剣心 #二次創作小説
     ```

4. **初期フォロー戦略**
   - 検索キーワード: `るろうに剣心 二次創作`, `追憶編 小説`, `るろ剣 SS`
   - 創作者を優先的にフォロー（10〜20人目安）
   - フォロー後、相手のPixiv作品をブックマークすると相互認知が発生しやすい

**Step 2: 確認**

ガイドが上から順に読めば設定が完了する構成になっているか確認する。

**Step 3: コミット**

```bash
git add docs/marketing/x_account_setup.md
git commit -m "docs: Add X account setup guide for battousai"
```

---

## Task 4: Phase 1 運用スケジュール作成

初動1週間の具体的な投稿スケジュールを作成する。

**Files:**
- Create: `docs/marketing/phase1_schedule.md`

**Step 1: スケジュールを作成**

アカウント作成日を Day 0 として、1週間の行動を日ごとに記載する:

| Day | 時間帯 | アクション |
|---|---|---|
| 0 | 午前 | アカウント作成・プロフィール設定・画像設定 |
| 0 | 23:00 | 固定ポスト投稿（シリーズ紹介） |
| 1 | 23:00 | 第1話「夜雨」告知（テンプレ使用） |
| 1 | 随時 | 同ジャンル創作者5人フォロー + 作品ブックマーク |
| 2 | -- | 休み。他の人のポストにいいねするだけ |
| 3 | 23:00 | 第2話「残心」告知 |
| 3 | 随時 | 追加フォロー5人 |
| 4 | -- | 休み。交流のみ |
| 5 | 23:00 | 第3話「白梅」告知 |
| 6 | -- | 休み。交流のみ |
| 7 | 23:00 | 第4話「同居」告知 |

以降、2日おきに第5話・第6話を告知。

**注意事項:**
- 23:00投稿は30代男性読者のピーク時間帯に合わせている
- 休みの日は「沈黙」ではなく「他の人との交流」に充てる
- 創作進捗ツイートはPhase 1 では不要（まだフォロワーが少ないため効果が薄い）
- Phase 2（定常運用）への移行は、6話分の告知が終わった後

**Step 2: 確認**

スケジュールが既存の `sns_announcement_guide.md` の基本ルール（投稿タイミング、頻度）と矛盾していないか確認する。

**Step 3: コミット**

```bash
git add docs/marketing/phase1_schedule.md
git commit -m "docs: Add Phase 1 SNS launch schedule (7-day plan)"
```

---

## Task 5: 既存ドキュメントの整合性更新

既存のマーケティングドキュメントに今回の設計を反映し、相互参照を追加する。

**Files:**
- Modify: `docs/marketing/pixiv_optimization.md`
- Modify: `docs/marketing/sns_announcement_guide.md`

**Step 1: pixiv_optimization.md に表紙画像セクションを追加**

`## 4. 運用チェックリスト（新話投稿時）` の前に以下を追加:

```markdown
## 3.5 表紙画像

シリーズ表紙にComfyUIで生成した雰囲気画像を使用する。詳細は `docs/marketing/cover_art_guide.md` を参照。

- 表紙画像は1200×1600（縦長）で生成し、Pixiv側でリサイズさせる
- キャラクターは描かない。風景・小物・テクスチャで「染み鉄」の世界観を視覚化する
- タイトル文字を筆書き風フォントで重ねる
```

**Step 2: sns_announcement_guide.md の画像ルールを更新**

基本ルールの「画像」の行を更新:

変更前:
```
- **画像**: 可能であれば作品イメージに合った画像を添付（横長推奨）
```

変更後:
```
- **画像**: 表紙画像を添付。詳細は `docs/marketing/cover_art_guide.md` 参照
```

**Step 3: 確認**

相互参照が壊れていないか、新ファイルへのパスが正しいか確認する。

**Step 4: コミット**

```bash
git add docs/marketing/pixiv_optimization.md docs/marketing/sns_announcement_guide.md
git commit -m "docs: Cross-reference cover art guide from existing marketing docs"
```

---

## 依存関係

```
Task 1 (プロンプトガイド)  ──────────────────────→ [ユーザー: ComfyUIで画像生成]
Task 2 (告知テンプレ4-6)  ─┐                            ↓
Task 3 (Xセットアップ)    ─┤→ 並列実行可能        [ユーザー: 文字入れ]
Task 4 (運用スケジュール) ─┘                            ↓
Task 5 (整合性更新)       ─→ Task 1, 2 完了後     [ユーザー: X開設 + Phase 1 開始]
```

Task 1〜4 は互いに独立しているため並列実行が可能。Task 5 は Task 1, 2 の完了を待つ。
