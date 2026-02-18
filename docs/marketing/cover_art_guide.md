# カバーアート生成ガイド — 濁刃（だくじん）

> ComfyUI (Stable Diffusion) でシリーズカバー・SNS素材を生成するためのリファレンス。
> キャライラストは使わない。風景・器物・テクスチャで「Stained Steel（染み鉄）」の空気を伝える。

---

## 1. 概要 / Overview

### 目的

以下の3点を生成する:

| 用途 | サイズ | 向き |
|---|---|---|
| Pixiv シリーズカバー | 1200 x 1600 px | 縦 (portrait) |
| X ヘッダー | 1500 x 500 px | 横 (landscape) |
| X アイコン | 400 x 400 px | 正方形 (square) |

### スタイル方針

- **キャライラスト禁止**。人物の顔・手が画面に入らないこと
- 風景、器物（刀・鍔・灯り）、質感（錆・雨・石畳）で構成する
- 色彩は Story Profile §1 準拠: 赤（血）・藍（闇）・白（白梅）。暖色は火と血だけ

---

## 2. 推奨モデル / Recommended Models

### 使うもの

| モデル | 特徴 |
|---|---|
| **Juggernaut XL** | フォトリアル寄り。風景・テクスチャの質が高い |
| **RealVisXL** | リアル系の定番。ライティングの自然さに優れる |
| **SDXL base + refiner** | 上記が合わなければ公式ベースで試す |

### 使わないもの

- Anything XL, CounterfeitXL, AnimagineXL 等のアニメ系モデル
- 理由: アニメ調はテクスチャの「物質感」が出ない。染み鉄の美学と合わない

---

## 3. 画像仕様・プロンプト / Image Specifications & Prompts

---

### 3-1. Pixiv シリーズカバー（1200 x 1600, 縦）

**コンセプト**: 雨に濡れた刀の柄。鉄錆のテクスチャ、暗い空気感。

**Positive prompt**:

```
close-up of japanese katana tsuka (hilt) in heavy rain, water droplets on iron tsuba guard, rust patina, dark atmospheric lighting, blood stains dried on wrapping, traditional japanese aesthetic, cinematic, dark moody color palette, shallow depth of field, 8k detail
```

**Negative prompt**:

```
text, watermark, signature, anime, cartoon, illustration, person, face, hands, bright colors, cheerful, modern, plastic
```

**ポイント**:
- タイトル文字「濁刃」は後から Canva/Photopea で重ねる。画像内にテキストを入れない
- 柄巻き（tsuka-ito）の質感と雨粒の光が主役。ピントは鍔〜柄頭に合わせる
- 背景はボケた暗闇で十分。情報を詰めすぎない

---

### 3-2. X ヘッダー（1500 x 500, 横）

**コンセプト**: 雨の幕末京都、夜の路地。提灯ひとつの暖色。

**Positive prompt**:

```
rainy kyoto narrow alley at night, edo period japan, dark atmospheric, single paper lantern warm glow, wet stone pavement reflections, wooden buildings, fog, cinematic wide shot, film grain, muted color palette, rust and ash tones
```

**Negative prompt**:

```
text, watermark, signature, anime, cartoon, illustration, person, face, bright colors, modern buildings, neon
```

**ポイント**:
- **重要: 主要な要素は画像の上下中央に配置する**。スマートフォン表示では上下がクロップされるため、提灯や路地の消失点が中央帯（上端から150〜350px）に収まること
- 横長なので左右に余白が出やすい。霧や雨で自然に埋める
- 色味は鉄錆色〜暗灰のグラデーション。提灯の暖色だけがアクセント

---

### 3-3. X アイコン（400 x 400, 正方形）

**コンセプト**: 鍔（つば）の超接写。鉄の経年変化、錆の質感。

**Positive prompt**:

```
extreme macro close-up of japanese sword tsuba guard, intricate iron carving, dark rust patina, aged metal texture, centered composition, dark background, dramatic side lighting, 8k detail
```

**Negative prompt**:

```
text, watermark, signature, anime, cartoon, illustration, person, bright colors, modern
```

**ポイント**:
- **重要: 円形にクロップされても成立する構図にする**。鍔を画面中央に配置し、四隅は暗い背景で逃がす
- サイドライティングで鉄の凹凸を強調する。正面光だとテクスチャが潰れる
- テキストは載せない（小さすぎて読めない）

---

## 4. 推奨パラメータ / Recommended Parameters

| パラメータ | 推奨値 | 備考 |
|---|---|---|
| **Steps** | 30 - 40 | 20以下だとテクスチャが甘くなる |
| **CFG Scale** | 7 - 8 | 高すぎると不自然。9以上は避ける |
| **Sampler** | DPM++ 2M Karras | 安定して高品質。代替: Euler a |
| **Scheduler** | Karras | DPM++ 2M と組み合わせる |
| **Seed** | -1（ランダム） | 良い構図が出たら seed を固定してプロンプト微調整 |
| **Batch size** | 4 | 一度に4枚生成して選別する |

### アップスケーラ（任意）

最終出力を高解像度化する場合:

| アップスケーラ | 用途 |
|---|---|
| **4x-UltraSharp** | シャープネス重視。金属テクスチャ向き |
| **RealESRGAN_x4plus** | 自然な仕上がり。風景向き |

アップスケール倍率は 1.5x - 2x 程度で十分。4x までやるとファイルサイズが肥大する。

---

## 5. タイポグラフィ重ね（後処理）/ Typography Overlay

### ツール

| ツール | 特徴 |
|---|---|
| **Canva** (無料枠) | 直感的。テンプレートあり。日本語フォント対応 |
| **Photopea** (無料) | ブラウザで動く Photoshop 互換。レイヤー操作が必要な場合はこちら |

### フォント

| フォント名 | 種類 | 入手 |
|---|---|---|
| **衡山毛筆フォント** | 筆書き・力強い | 無料（Google検索で配布元へ） |
| **源界明朝** | 崩れた明朝体・退廃的 | 無料（GitHub配布） |

- タイトル「**濁刃**」を大きく配置
- ルビ「**だくじん**」をタイトル直下に小さく
- 文字色: **白 (#F5F0E8)** または **金 (#C9A82C)**。背景が暗いので白系が安全
- 可読性のためドロップシャドウまたは外側グロウを薄くかける

### 各素材への適用

| 素材 | テキスト処理 |
|---|---|
| **Pixiv カバー** | 「濁刃」を中央または下部1/3に配置。存在感を出す |
| **X ヘッダー** | タイトル文字は控えめに。不透明度 40-60% でブレンドする選択肢もあり |
| **X アイコン** | **テキストなし**。小さすぎて読めず、円形クロップで切れる |

---

## 6. カラーリファレンス / Color Reference

| 名前 | Hex | RGB | 用途 |
|---|---|---|---|
| 鉄錆色 (Iron Rust) | `#8B4513` | 139, 69, 19 | 主調。背景、地面、柄巻きの色味 |
| 暗灰 (Dark Ash) | `#2C2C2C` | 44, 44, 44 | 影、最も深い暗部 |
| 血赤 (Blood Red) | `#8B0000` | 139, 0, 0 | アクセント。乾いた血痕、提灯の反射 |
| 白梅白 (Plum White) | `#F5F0E8` | 245, 240, 232 | まばらなハイライト、タイトル文字 |
| 金 (Gold) | `#C9A82C` | 201, 168, 44 | タイトル文字の代替色 |

### img2img での色味補正

生成画像の色味が明るすぎる・鮮やかすぎる場合:
- img2img に投げて denoising strength 0.2 - 0.3 で再生成
- ネガティブに `vibrant, saturated, colorful` を追加
- または Photopea でトーンカーブを下げる方が早い場合もある

---

## 7. ワークフローまとめ / Workflow Summary

```
1. ComfyUI でモデル・サイズ・プロンプトを設定
2. batch 4 で生成 → 構図とテクスチャで1枚選別
3. seed を固定してプロンプト微調整（2-3回繰り返し）
4. 必要ならアップスケーラで解像度を上げる
5. Canva / Photopea でタイポグラフィを重ねる（カバーとヘッダーのみ）
6. 最終確認: スマホ画面でクロップ状態を確認
```

---

> 参照: `.agent/profiles/battousai.md` §1（Stained Steel 美学）、`docs/marketing/pixiv_optimization.md`（タグ・キャプション設計）
> プロンプト設計スキル: `.claude/skills/image-prompt/` — SDXL プロンプトエンジニアリングのベストプラクティス・語彙辞書
