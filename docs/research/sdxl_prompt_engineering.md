# Research Report: SDXL Prompt Engineering Best Practices

**Date**: 2026-02-19
**Type**: Subject
**Query**: Stable Diffusion XL (SDXL) image generation prompt engineering -- structure, syntax, techniques, sampler interaction, subject-specific strategies

---

## 1. SDXL Architecture: What Makes It Different

### Dual CLIP Encoder System

SDXL uses two text encoders simultaneously, a fundamental departure from SD1.5's single encoder.

- **CLIP-ViT/L (text_l)**: OpenAI's `clip-vit-large-patch14`。768次元の埋め込みベクトルを出力。**キーワード/タグ型**の短い記述に強い。
- **OpenCLIP-ViT/G (text_g)**: `laion/CLIP-ViT-bigG-14-laion2B-39B-b160k`。1,280次元の埋め込みベクトルを出力。**自然言語の文章記述**に強い。

両者の出力を結合(concatenate)して2,048次元の埋め込みを構成する。SD1.5の768次元と比較して約2.7倍の情報量。

### ComfyUI での分離入力

ComfyUI の `CLIPTextEncodeSDXL` ノードでは `text_g` と `text_l` を別々に入力できる。

- **text_g**: 画像の内容記述（被写体、構図、形容詞、名詞）
- **text_l**: スタイル記述（画風、メディウム、雰囲気）

実験結果として、スタイル指定を `text_l` に限定すると、より忠実で動的な出力が得られる。逆（スタイルを `text_g`、内容を `text_l`）にするとスタイルの反映が弱くなる。

**注意**: A1111 WebUI 等でプロンプト欄が1つの場合、同一のテキストが両方のエンコーダに送られる。この場合は自然言語とキーワードの**混合記述**が最も効果的。

### SD1.5 との根本的な違い

| 項目 | SD1.5 | SDXL |
|------|-------|------|
| プロンプトスタイル | タグ/キーワード列挙（カンマ区切り） | 自然言語の文章記述 |
| 例 | `1 boy, futuristic suit, neon background, cityscape, evening sky` | `A young boy wearing a futuristic suit, standing against a neon-lit cityscape with an evening sky in the background` |
| ネガティブプロンプト | 長大なリストが必要 | 短く焦点を絞る |
| 品質タグの必要性 | ほぼ必須 | モデル依存（基本不要） |
| 解像度 | 512x512 | 1024x1024 |
| CLIP トークン上限 | 75トークン/チャンク | 75トークン/チャンク（ただし2エンコーダ分） |

---

## 2. Prompt Structure（プロンプトの構造）

### 推奨構造テンプレート

```
[Subject] — [Action/Pose] — [Environment/Location] — [Lighting] — [Camera/Lens] — [Style/Medium] — [Details/Mood]
```

前方に配置した要素ほど優先度が高い。75トークンで1チャンクとして処理され、76トークン目以降は新しいチャンクとなり影響力が変化する。

### 構造の具体例

**フォトリアル**:
```
Cinematic portrait of a Scandinavian woman with freckles, soft studio lighting,
85mm lens photography, film look, ultra detailed skin texture, sharp depth of field,
magazine editorial style
```

**風景**:
```
A mist-covered mountain valley at dawn, crepuscular rays breaking through pine forest,
wet rocks in the foreground, golden hour light, wide angle landscape photography,
atmospheric perspective
```

**スタイライズド**:
```
cinnamon bun on the plate, watercolor painting, detailed, brush strokes,
light palette, light, cozy
```

### 自然言語 vs タグ -- 使い分け

SDXLは自然言語を理解する。だが、場面によってハイブリッドが有効。

- **シーン記述** → 自然言語（文章形式で空間関係、動作、雰囲気を記述）
- **属性・ディテール** → カンマ区切りタグ（髪色、服装、特定のスタイル名）
- **品質/技術指定** → タグ（後述の品質タグセクション参照）

日本語コミュニティでの推奨：「なるべくカンマで区切った単語を入力する。単語で細かく分けたほうが、それぞれの要素に対して変化を付けやすく整理しやすい」。ただしこれは Danbooru タグ系のファインチューンモデル（Illustrious XL、Pony 等）に限った話で、ベース SDXL 1.0 では自然言語が優位。

---

## 3. Prompt Weighting（重み付け構文）

### 基本構文

| 構文 | 効果 | 備考 |
|------|------|------|
| `(keyword)` | 注目度 x1.1 | `(keyword:1.1)` と同義 |
| `((keyword))` | 注目度 x1.21 | 入れ子で累乗 |
| `(keyword:1.4)` | 注目度 x1.4 | 数値で直接指定 |
| `[keyword]` | 注目度 x0.9 | 減衰。`(keyword:0.9)` と同義 |
| `[[keyword]]` | 注目度 x0.81 | 入れ子で累乗 |

**実用範囲**: `(token:0.5)` 〜 `(token:1.6)`。これを超えると画像が破綻しやすい。SDXLは SD1.5 よりも重みに敏感で、**1.4 を超えることはほぼ不要**。

### BREAK トークン

```
beautiful landscape, mountains, lake BREAK
dramatic sunset, orange and purple sky BREAK
foreground wildflowers, detailed grass
```

- **大文字**でなければ認識されない
- 現在のチャンク（75トークン）をパディング文字で埋め、次のチャンクを新規開始する
- 効果: `BREAK` の直後に置いた要素が新チャンクの先頭となり、強い影響力を持つ
- 長いプロンプトの意味的セクション分離に有効
- Regional Prompter と組み合わせると、画面領域ごとに異なるプロンプトを割り当てられる

### AND 演算子

```
a cat sitting on a chair AND oil painting style, thick brushstrokes
```

- 2つのプロンプトを**独立に処理**してから結合する（Composable Diffusion）
- カンマ区切りよりも概念の混合が明確になる場合がある
- プラットフォームによっては未対応（PixAI 等）

### Prompt Scheduling（プロンプトスケジューリング）

生成ステップの途中でプロンプトを切り替える高度技法。A1111/ComfyUI で使用可能。

| 構文 | 意味 |
|------|------|
| `[from:to:0.5]` | ステップ50%で `from` を `to` に切り替え |
| `[to:0.3]` | ステップ30%以降に `to` を追加 |
| `[from::0.7]` | ステップ70%で `from` を除去 |
| `[cat\|dog]` | 奇数ステップで `cat`、偶数ステップで `dog`（交互） |

用途: 序盤で構図を決め、後半でディテールを変更する等。

---

## 4. Negative Prompts（ネガティブプロンプト）

### SDXL における基本方針

SD1.5 と異なり、**SDXLのネガティブプロンプトは短く焦点を絞る**。500語超のネガティブプロンプトは重要な項目の効果を希釈する。50〜150語が実用的な上限。

### ミニマル・テンプレート（汎用）

```
low quality, blurry, pixelated, distorted, extra limbs, watermark, text, deformed hands
```

### フォトリアル用テンプレート

```
(worst quality, low quality:1.4), (low resolution, blurry, blur:1.2),
jpeg artifacts, compression artifacts, poorly drawn, bad anatomy,
wrong anatomy, deformed, mutated, disfigured, ugly, disgusting,
text, watermark, signature, logo, username, artist name,
(cartoon, anime, illustration, painting, drawing, sketch:1.3),
3d render, cgi, digital art, unrealistic, artificial
```

### イラスト/アニメ用テンプレート

```
nsfw, low quality, normal quality, worst quality, jpeg artifacts,
cropped, monochrome, lowres, low saturation, watermark, white letters
```

### 状況別の追加項目

| 状況 | 追加するネガティブ |
|------|---------------------|
| 手の破綻が出る | `(mutated hands:1.4), extra fingers, fused fingers` |
| 顔が崩れる | `bad face, ugly face, asymmetric face` |
| フォトリアルなのにアニメ調になる | `(cartoon, anime, illustration:1.3)` |
| テキストが混入する | `text, lettering, words, numbers, watermark` |
| 過度な彩度 | `oversaturated, neon colors, vibrant colors` |

### 反復的な使い方

1. **最初はネガティブなしで生成**する
2. 問題が出たら、その問題に対応するネガティブを1〜2語追加
3. 再生成して確認。改善したら固定、しなかったら別の表現を試す
4. 「全部入り」ネガティブから始めるのは逆効果

---

## 5. Quality Boosters（品質タグ）-- 実効性の検証

### ベース SDXL 1.0 での検証結果

ベース SDXL 1.0 は Danbooru タグではなく自然言語ペアで訓練されている。そのため:

- `masterpiece`, `best quality`, `8k` 等のタグは**訓練データに含まれていない可能性が高い**
- ベースモデルでは「短く、描写的なプロンプト」が最も効果的で、品質タグの追加効果は限定的
- 過剰な品質タグはオーバーシャープニングや細部の歪みを引き起こすことがある

### ファインチューンモデルでの状況

Danbooru ベースのファインチューンモデル（Illustrious XL, Pony Diffusion XL, Animagine XL 等）では事情が異なる:

- `masterpiece, best quality, amazing quality` は品質維持に有効
- 追加で `very aesthetic, newest` を付けると効果がある場合がある
- **モデルのドキュメントに従う**のが最善（モデルカードに推奨タグが記載されていることが多い）

### 品質タグのティア分類

| ティア | タグ | 実効性 |
|--------|------|--------|
| 効果あり（条件付き） | `masterpiece`, `best quality` | Danbooru系ファインチューンでは有効。ベースSDXLでは微妙 |
| 写真系で有効 | `professional photography`, `DSLR`, `8k uhd` | フォトリアル生成で構図・ディテール改善 |
| スタイル指定として有効 | `cinematic`, `photographic`, `film grain` | スタイル方向の誘導として機能 |
| カーゴカルト（効果不明） | `trending on artstation`, `award winning` | SD1.5時代からの慣習。SDXLでの実証なし |
| 逆効果のリスク | 5個以上の品質タグ積み | オーバーシャープニング、不自然な質感 |

### 推奨: 2〜3個に絞る

```
# フォトリアル
professional photography, 8k uhd, sharp focus

# イラスト（Danbooru系モデル）
masterpiece, best quality

# コンセプトアート
concept art, highly detailed
```

---

## 6. Subject-Specific Techniques（被写体別テクニック）

### 6a. Objects / Still Life（静物・武器・道具）

**構成要素**:
- 素材の質感記述: `polished steel`, `weathered leather`, `aged oak wood`, `tarnished brass`
- 光の反射/屈折: `specular highlights`, `subsurface scattering`, `caustics`
- 背景の制御: `plain dark background`, `studio setup`, `floating in void`

**プロンプト例 -- 日本刀**:
```
A Japanese katana resting on a dark wooden stand, folded steel blade with visible hamon line,
ray skin wrapped handle with silk cord, lacquered scabbard beside it,
dramatic side lighting casting long shadows, macro photography, shallow depth of field,
studio product photography
```

**コツ**:
- SDXLは素材の質感描写に強い（leather, fur, fabric, metal, stone を正確にレンダリングする）
- 1024x1024の解像度があるため、テクスチャの微細パターンまで表現可能
- 照明条件を具体的に記述するとリアリティが増す（`side lighting` vs 単なる `lighting`）

### 6b. Landscapes / Environments（風景・環境）

**構成要素**:
- 時間帯: `golden hour`, `blue hour`, `high noon`, `twilight`, `overcast midday`
- 大気: `atmospheric haze`, `morning mist`, `fog rolling in`, `clear sky`
- 前景/中景/背景の層: 奥行きを出すために3層を明示する
- 色温度: `warm tones`, `cool blue palette`, `muted earth tones`

**プロンプト例 -- 霧の山谷**:
```
Mist-covered mountain valley at dawn, crepuscular rays breaking through dense pine forest,
moss-covered boulders in the foreground with a narrow stream,
atmospheric perspective fading into blue distance,
wide angle landscape photography, golden hour warmth on the peaks
```

**コツ**:
- `crepuscular rays`（薄明光線/ゴッドレイ）は SDXL が特に得意とする効果
- `atmospheric perspective`（空気遠近法）を入れると遠景が自然に霞む
- 天候要素（sunshine, rain, snow）は劇的にムードを変える
- Golden Hour は SDXL が忠実に再現するキーワード

### 6c. Atmospheric Effects（大気・天候効果）

| 効果 | キーワード | 補強ワード |
|------|-----------|------------|
| 雨 | `rainy`, `rain`, `wet surfaces` | `wet reflections`, `puddles`, `dripping` |
| 霧 | `fog`, `mist`, `haze` | `volumetric fog`, `foggy atmosphere`, `eerie fog` |
| 光線 | `god rays`, `crepuscular rays` | `volumetric lighting`, `light shafts`, `beam of light` |
| ネオン | `neon lights`, `neon glow` | `neon reflections on wet pavement`, `cyberpunk lighting` |
| 煙/蒸気 | `smoke`, `steam`, `vapor` | `wisps of smoke`, `rising steam`, `misty breath` |
| 雪 | `snowfall`, `blizzard`, `frost` | `snow-covered`, `icicles`, `frozen` |
| 夕焼け | `sunset`, `golden hour` | `orange and purple sky`, `warm backlighting` |

**ボリュメトリックライティングの例**:
```
Dark medieval castle corridor, volumetric fog, single torch on the wall casting
warm orange light, dust particles visible in the beam,
stone walls with moisture, dramatic chiaroscuro lighting
```

### 6d. Textures and Materials（質感・素材）

SDXL は素材描写に優れる。具体的に記述するほど正確。

| 素材 | 効果的なキーワード |
|------|---------------------|
| 金属 | `brushed steel`, `hammered copper`, `polished chrome`, `oxidized bronze`, `rusted iron` |
| 木材 | `weathered driftwood`, `polished mahogany`, `rough-hewn oak`, `birch bark`, `charred wood` |
| 布地 | `silk sheen`, `rough linen`, `velvet texture`, `worn cotton`, `embroidered satin` |
| 石 | `marble veining`, `rough granite`, `smooth river stones`, `cracked sandstone` |
| 肌 | `detailed skin texture`, `pores visible`, `freckles`, `subsurface scattering` |
| 水 | `crystal clear water`, `murky depths`, `rippled surface`, `frozen ice` |

**リアリティ向上のコツ**: 「完璧すぎない」テクスチャを指定する。`slight imperfections`, `wear marks`, `patina`, `dust particles` 等を加えると不自然な CG 感が減る。

---

## 7. Photorealistic vs Artistic（フォトリアル vs アーティスティック）

### フォトリアルの戦略

**原則**: 写真用語で記述する。`beautiful picture` ではなく `DSLR photograph, 85mm f/1.4 lens` と書く。

**推奨要素**:
- **カメラ設定**: `Canon EOS R5`, `Sony A7III`, `Nikon Z9`, `Hasselblad`
- **レンズ**: `85mm f/1.4`, `35mm wide angle`, `200mm telephoto`, `macro lens`
- **フィルムストック**: `Kodak Portra 400`, `Fujifilm Pro 400H`, `Ilford HP5`
- **照明**: `studio lighting`, `natural window light`, `golden hour`, `rembrandt lighting`
- **構図**: `rule of thirds`, `leading lines`, `shallow depth of field`, `bokeh`
- **後処理**: `film grain`, `color grading`, `desaturated tones`

**フォトリアル・テンプレート**:
```
[Subject description], professional photography, shot on Canon EOS R5 with 85mm f/1.4 lens,
natural lighting, shallow depth of field, film grain, color graded, 8k uhd
```

**推奨モデル**: ProtoVision XL, JuggernautXL, RealVisXL, NewReality XL

**推奨設定**:
- Sampler: DPM++ 2M SDE Karras
- Steps: 30
- CFG: 5-7
- Refiner: 有効（switch point 0.65-0.80）

### アーティスティック/スタイライズドの戦略

**原則**: 画材・技法・アーティスト名で方向付ける。

**メディウム指定**:
- **油絵**: `oil painting, thick impasto brushstrokes, canvas texture`
- **水彩**: `watercolor painting, wet-on-wet technique, transparent washes, paper texture`
- **デジタルアート**: `digital painting, concept art, matte painting`
- **ペン画**: `ink drawing, fine linework, crosshatching`
- **版画**: `woodblock print, ukiyo-e style, limited color palette`

**スタイル強化**:
```
# 油絵
A still life arrangement of autumn fruits on a worn wooden table,
oil painting, thick brushstrokes, warm palette, chiaroscuro lighting,
style of Dutch Golden Age masters, canvas texture visible

# 水彩
A coastal village at sunset, watercolor painting, loose brushwork,
transparent washes bleeding into each other, wet-on-wet technique,
light palette with warm accents, white paper showing through
```

**SDXL スタイルキーワード一覧**（SDXL 公式プリセットベース）:
- `cinematic`, `photographic`, `anime`, `digital art`, `comic book`, `fantasy art`
- `analog film`, `neon punk`, `isometric`, `low poly`, `origami`, `line art`
- `pixel art`, `texture`, `3D model`, `craft clay`

**注意**: `Cinematic` と `Photographic` は過度に使われているため、独自性を出したい場合は避けて具体的なスタイル記述にする。

---

## 8. Sampler & Parameter Pairing（サンプラーとパラメータ）

### SDXL 推奨サンプラー・スケジューラー組み合わせ

| サンプラー | スケジューラー | Steps | CFG | 用途 |
|------------|----------------|-------|-----|------|
| DPM++ 2M | Karras | 20-30 | 5-7 | **汎用最推奨**。シャープで安定 |
| DPM++ 3M | Exponential | 30+ | 5-7 | 大画像（2K+）で安定。ディテール豊富 |
| DPM++ SDE | Karras | 15-20 | 5-7 | ポートレート。柔らかい質感 |
| UniPC | SGM Uniform | 8-10 | ~7 | 高速生成。低ステップで良質 |
| Euler a | Simple/Linear | 20-25 | 6-8 | アニメ系SDXL。創造的なバリエーション |

### 避けるべき組み合わせ

- **Ancestral系サンプラー + Karras**: ノイズ注入とスケジューラーが干渉し、粒状感が出る
- **DPM++ SDE + Karras**: 非収束挙動。15-20ステップのみ安定

### CFG Scale の影響

| CFG | 効果 |
|-----|------|
| 3-5 | 柔らかく、創造的。プロンプトへの忠実度が低い |
| 5-7 | **SDXL のスイートスポット**。バランスが良い |
| 7-9 | プロンプトに忠実。コントラストが強くなる |
| 9+ | 過飽和・アーティファクトのリスク。SDXL では推奨しない |

### Refiner の使い方

SDXL のリファイナーは仕上げパスで、目・肌・影・エッジの品質を向上させる。

- **Switch point**: 0.65-0.80（0.75 が一般的）
- **Base steps + Refiner steps**: 15 + 10 = 25 total が目安
- **Denoising strength**: 0.3-0.6（高すぎると構図が変わる）
- **有効な場面**: ポートレート、フォトリアル、プロダクト写真
- **不要な場面**: 抽象アート、スタイライズドイラスト

### 解像度

SDXL は 1024x1024 で訓練されている。以下の解像度がアスペクト比として安全:

| アスペクト比 | 解像度 |
|-------------|--------|
| 1:1 | 1024x1024 |
| 3:4 (ポートレート) | 832x1216 / 896x1152 |
| 4:3 (ランドスケープ) | 1152x896 / 1216x832 |
| 16:9 (ワイド) | 1344x768 / 1536x640 |

**注意**: 900x900, 1000x1000 等の非標準値は品質低下を招く。

---

## 9. Common Pitfalls（初心者が陥りやすい罠）

### 罠1: SD1.5 のプロンプトスタイルをそのまま使う

SD1.5 の短いタグ列挙は SDXL では機能しにくい。SDXL は文章を理解する。

**悪い例**: `1girl, blue hair, school uniform, cherry blossoms, detailed, 4k`
**良い例**: `A young woman with blue hair in a school uniform, standing under a cherry blossom tree in full bloom, petals falling around her, soft spring sunlight`

### 罠2: ネガティブプロンプトの過剰投入

SD1.5 時代の「全部入り」ネガティブリストは SDXL で逆効果になることがある。重要な項目が希釈される。

### 罠3: 品質タグの山盛り

`masterpiece, best quality, ultra detailed, 8k, sharp focus, intricate, elegant, highly detailed, digital painting, concept art, smooth, sharp` のような列挙は、2-3個に絞った方が結果が良い。

### 罠4: CFG の上げすぎ

SD1.5 では CFG 12-15 が使えたが、SDXL では 9 を超えるとコントラスト過剰やアーティファクトが発生しやすい。5-7 が安全帯。

### 罠5: 非標準解像度の使用

900x900 や 768x768（SD1.5 の解像度）は SDXL では品質低下を招く。1024x1024 ベースのアスペクト比を使う。

### 罠6: 過度のプロンプティング

SDXL は構図・照明・技術的実行を自力で処理できる。全てを指示しようとするとかえって不自然になる。被写体と雰囲気を記述し、細部はモデルに委ねる。

### 罠7: 設定の記録を怠る

プロンプト、シード、サンプラー、CFG、モデル名を記録しないと、良い結果が再現できない。生成初日から記録の習慣をつける。

---

## 10. Iterative Refinement（反復改善ワークフロー）

### Phase 1: Rough Generation（粗生成）

1. 被写体とスタイルだけの短いプロンプトで生成
2. ネガティブプロンプトなし
3. CFG 5-6, Steps 20, DPM++ 2M Karras
4. **目的**: モデルの自然な出力傾向を確認

### Phase 2: Diagnose（診断）

生成結果を見て問題を特定する:

| 症状 | 原因 | 対処 |
|------|------|------|
| 画像が平坦/フラット | CFG が低すぎる / 照明記述がない | CFG を 6-7 に。照明キーワード追加 |
| ぼやけている | Steps 不足 / Refiner 未使用 | Steps を 30 に。Refiner 有効化 |
| 過飽和・ギラギラ | CFG が高すぎる | CFG を 5-6 に下げる |
| 手の破綻 | モデル固有の弱点 | ネガティブに `(mutated hands:1.4)` / openpose ControlNet |
| 顔の崩れ | 解像度不足 / 遠景 | ADetailer 使用。顔検出モデル（face_yolov8n.pt）適用 |
| AI っぽい / 不自然に綺麗 | テクスチャ記述不足 | `skin pores`, `slight imperfections`, `film grain` 追加 |
| 構図が意図と違う | プロンプトが曖昧 | 位置関係・カメラアングルを明記 |
| スタイルが安定しない | スタイルキーワード弱い | `(style keyword:1.2-1.3)` で重み付け |

### Phase 3: Targeted Fix（対症修正）

1. 問題ごとに**1つずつ**修正を加える（複数同時変更は原因特定を困難にする）
2. 同じシードで比較生成
3. 改善が確認できたら固定

### Phase 4: Polish（仕上げ）

1. Refiner の適用（switch point 0.70-0.80）
2. Hires Fix でアップスケール（Denoising 0.35-0.45）
3. ADetailer で顔ディテール改善
4. 必要に応じて img2img で局所修正

---

## 11. Advanced Techniques（上級テクニック）

### ControlNet との併用

- **openpose**: ポーズ指定。手の破綻回避にも有効
- **depth**: 奥行きマップで構図制御。風景の前景/中景/背景を安定化
- **SoftEdge**: 被写体の輪郭を維持しつつ照明やスタイルを変更
- **Canny**: エッジ検出ベース。建築物やメカの形状維持

### LoRA の使い方

- SDXL 専用 LoRA のみ使用（SD1.5 用は非互換）
- 推奨強度:
  - キャラクター LoRA: 0.6-0.9
  - スタイル LoRA: 0.4-0.7
  - 衣装/概念 LoRA: 0.3-0.6
- **3つ以下**に制限（安定性のため）
- テクスチャ系 LoRA は極低強度（0.05-0.1）で有機的な質感を付加

### ADetailer ワークフロー

1. 第1モデル: `face_yolov8n.pt`（顔検出）
2. 第2モデル: `mediapipe_face_mesh_eyes_only`（目のディテール）
3. 遠景のキャラクターには `person` モデルを先に適用し、次に `face` モデル
4. **注意**: ADetailer はポートレートでは顔の特徴を変えることがある

### Semantic Guidance

ControlNet なしでシーンの再照明が可能。CD Tuner と組み合わせて Region Prompter 構文で特定領域のみ再照明する技法。

### アップスケール推奨

| アップスケーラー | 用途 |
|-----------------|------|
| 4x-UltraSharp | 汎用最高品質 |
| 4xFaceUpSharpDAT | 顔ポートレートの安全な2x |
| 4x-ClearRealityV1 | 汎用。安定 |
| Latent Bicubic | 内蔵。手軽 |
| DAT / SwinIR | 内蔵。良好 |

---

## 12. 日本語コミュニティ特有の知見

### プロンプトの順序と 75 トークンルール

日本語コミュニティでは、トークンの順序効果が強調されている:

- 先頭に書いた単語ほど優先度が高い
- 75 トークンで 1 グループ。76 トークン目から新グループとなり影響力が変化
- `BREAK` を使ってグループを強制区切り可能

### Danbooru タグ系モデルでの推奨

Illustrious XL, Pony Diffusion XL, Animagine XL 等の Danbooru タグ系ファインチューンでは:

- タグ方式（カンマ区切り）が有効
- `masterpiece, best quality` が品質維持に必要
- キャラクター特徴は Danbooru タグ準拠（`blue_eyes`, `long_hair`, `school_uniform` 等）

### BREAK 構文の活用（日本語コミュニティ）

「BREAK を強調したい特徴の前に挿入する」使い方が一般的:

```
1girl, blue hair, school uniform BREAK
pink hair        # ← 髪色を強調（グループ先頭に配置）
```

複数の BREAK を使って、被写体・背景・スタイルをグループ分けする手法も普及:

```
1girl, detailed face, blue eyes BREAK
cherry blossom background, spring, sunlight BREAK
masterpiece, best quality, detailed
```

### Embedding の活用

ネガティブプロンプトの代わりに Embedding（Textual Inversion）を使う手法。
`negativeXL_D` 等の SDXL 用ネガティブ Embedding は、長いネガティブプロンプトを一語で代替する。

---

## Implications（本プロジェクトへの示唆）

- SDXL のプロンプトエンジニアリングは「記述力」の勝負であり、小説の情景描写と通じる部分がある。五感に基づく具体的なディテール（Author DNA の Non-Visual First に相当）が画像品質を左右する。
- フォトリアルでは「カメラ・レンズ・フィルム」の語彙、アーティスティックでは「画材・技法・アーティスト名」の語彙が鍵となる。
- 「少なく、具体的に」はプロンプトにも文章にも共通する原則。過剰な修飾語は画像でもノイズになる。

---

## Sources（出典）

### English Sources
- [SDXL Best Practices: Settings, Prompts & Workflows](https://neurocanvas.net/blog/sdxl-best-practices-guide/) -- Sampler/CFG/Resolution/Refiner の包括的ガイド
- [Stable Diffusion Prompting: Beginner to Pro Guide](https://neurocanvas.net/blog/stable-diffusion-prompting-guide/) -- SD1.5/SDXL比較、構造テンプレート
- [Civitai's Prompt-Crafting Guide: Part 2 - Intermediate](https://education.civitai.com/civitais-prompt-crafting-guide-part-2-intermediate/) -- 重み付け構文の詳細解説
- [Sampler and Scheduler Reference for SDXL](https://civitai.com/articles/16231/sampler-and-scheduler-reference-for-hi-dream-flux-sdxl-illustrious-and-pony) -- サンプラー+スケジューラー組み合わせの体系的比較
- [Two Text Prompts (Text Encoders) in SDXL 1.0](https://mybyways.com/blog/two-text-prompts-text-encoders-in-sdxl-1-0) -- Dual CLIP encoder (text_g/text_l) の実験的検証
- [Ultimate Guide to SDXL: Mastering Photorealism](https://sandner.art/ultimate-guide-to-sdxl-mastering-photorealism-in-generative-art-for-begginers-and-advanced/) -- フォトリアル特化。ControlNet/ADetailer/Upscale
- [Ultimate Guide to Creating Realistic SDXL Prompts](https://civitai.com/articles/11432/ultimate-guide-to-creating-realistic-sdxl-prompts) -- カメラ設定・照明・構図のフォトリアル語彙
- [Prompt Guide for Stable Diffusion XL (SDXL 1.0)](https://blog.segmind.com/prompt-guide-for-stable-diffusion-xl-crafting-textual-descriptions-for-image-generation/) -- SDXL公式寄りのプロンプトガイド
- [Stable Diffusion Negative Prompts: Ultimate Collection](https://freeaipromptmaker.com/blog/2025-11-29-stable-diffusion-negative-prompts-guide) -- ネガティブプロンプトのテンプレート集
- [Understanding Stable Diffusion Samplers](https://civitai.com/articles/7484/understanding-stable-diffusion-samplers-beyond-image-comparisons) -- サンプラーの技術的解説
- [106 styles for Stable Diffusion XL model](https://stable-diffusion-art.com/sdxl-styles/) -- SDXL スタイルキーワード106種の視覚比較
- [33 Fantastic SDXL v1.0 Prompts](https://aituts.com/sdxl-prompts/) -- 実例プロンプト集
- [Stable Diffusion Lighting Prompts](https://www.aiarty.com/stable-diffusion-prompts/stable-diffusion-lighting-prompts.htm) -- 照明キーワードの詳細ガイド
- [SDXL 1.0 Overview](https://education.civitai.com/sdxl-1-0/) -- SDXLアーキテクチャの解説
- [Advanced Prompting Syntax: Composable Diffusion, Scheduling, Alternation](https://civitai.com/articles/15104/advanced-on-site-prompting-syntax-composable-diffusion-prompt-scheduling-and-prompt-alternation) -- AND/スケジューリング/交互構文
- [SDXL Tips for Beginners](https://apatero.com/blog/first-time-using-sdxl-models-beginner-guide-2025) -- 初心者が陥る罠の解説
- [15 Stable Diffusion XL prompts + tips](https://stable-diffusion-art.com/sdxl-prompts/) -- SDXL固有のプロンプトTips

### Japanese Sources
- [SDXL系モデルのプロンプトの書き方](https://romptn.com/article/54452) -- 順序・強調構文・BREAK の解説
- [SDXLのプロンプトの書き方はどうすればいいか](https://piyo-piyo-piyo.com/14546/) -- text_g/text_l の使い分け
- [SDXLの実写系プロンプトの書き方のポイント](https://piyo-piyo-piyo.com/14550/) -- フォトリアル特化テクニック
- [SDXL系の画像生成プロンプトについて](https://note.com/oron1208/n/n84ed6bb31d73) -- 実践的プロンプト構築
- [BREAK構文とは？](https://runrunsketch.net/sd-break/) -- BREAK構文の図解
- [BREAK構文の使い方を完全マスターする](https://itdtm.com/stablediffusion-break/) -- BREAK の詳細解説
- [Stable DiffusionのBREAK構文・強調構文の使い方](https://highreso.jp/edgehub/stablediffusion/break.html) -- 構文リファレンス
- [コピペで使えるネガティブプロンプト一覧](https://romptn.com/article/2905) -- ネガティブプロンプトテンプレート集
- [品質に関する呪文(プロンプト)](https://romptn.com/article/28082) -- 品質タグの検証
- [SDXL効果的なプロンプト作成ガイド](https://futurevolab.com/en/stable-diffusion-xl-sdxl%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%A6%E5%8A%B9%E6%9E%9C%E7%9A%84%E3%81%AA%E3%83%97%E3%83%AD%E3%83%B3%E3%83%97%E3%83%88%E4%BD%9C%E6%88%90%E3%82%AC%E3%82%A4%E3%83%89/) -- 包括的日本語ガイド
