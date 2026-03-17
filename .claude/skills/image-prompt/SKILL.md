---
name: image-prompt
description: "Designs SDXL-optimized prompts for ComfyUI image generation. Covers prompt structure, weighting, negative prompts, sampler pairing, and iterative refinement. Reference keyword tables in `reference/prompt_vocabulary.md`. Research basis: `docs/research/sdxl_prompt_engineering.md`."
---

# image-prompt

ComfyUI + SDXL 向けのプロンプト設計スキル。リサーチベースのベストプラクティスに基づく。

**参照ファイル**:
- `reference/prompt_vocabulary.md` — キーワードカタログ（Photography, Lighting, Materials, Japanese Aesthetics 等）

---

## When to Use

- 表紙・SNS画像・挿絵などの画像生成プロンプトを設計するとき
- 既存プロンプトの改善・診断が必要なとき
- ComfyUI ワークフロー JSON を作成するとき

## Input

ユーザーから以下を受け取る:
1. **目的**: 何の画像か（表紙、ヘッダー、アイコン等）
2. **被写体**: 何を描くか
3. **雰囲気**: どんなムード・美学か
4. **サイズ**: アスペクト比と用途
5. **モデル**: 使用チェックポイント（未指定なら Juggernaut XL 前提）

## Prompt Design Process

### Step 1: Classify Output Type

| タイプ | プロンプト戦略 | 主要語彙 |
|--------|---------------|---------|
| フォトリアル | 写真用語（カメラ・レンズ・フィルム） | `reference/prompt_vocabulary.md` §Photography |
| アーティスティック | 画材・技法名 | `reference/prompt_vocabulary.md` §Art Medium |
| コンセプトアート | スタイル + 技法ハイブリッド | 両方から選択 |

### Step 2: Build Positive Prompt

**構造テンプレート** (前方ほど優先度が高い):

```
[Subject] — [Action/Pose] — [Environment] — [Lighting] — [Camera/Lens] — [Style] — [Details/Mood]
```

**ルール**:
- SDXL は自然言語を理解する。タグ列挙よりも文章記述が有効
- ただしスタイル・品質は短いタグで補完（ハイブリッド）
- 75 トークンで 1 チャンク。重要な要素は先頭 75 トークン内に入れる
- 品質タグは **2-3 個まで**（cargo cult 回避）
- 素材の質感は具体的に: `rusted iron` > `metal`, `worn cotton` > `fabric`
- 「完璧すぎない」テクスチャで AI 感を減らす: `slight imperfections`, `patina`, `wear marks`

### Step 3: Build Negative Prompt

**原則**: SDXL のネガティブは短く焦点を絞る（50-150 語が上限）。

**手順**:
1. 最初はネガティブなしで生成
2. 問題が出たら、その問題に対応する語を 1-2 個追加
3. 「全部入り」から始めない

**ミニマル・ベース** (必ず含める):
```
low quality, blurry, distorted, watermark, text
```

**フォトリアル追加**:
```
(cartoon, anime, illustration:1.3), 3d render, cgi, digital art
```

**被写体の除外** (今回生成したくないものを明示):
```
例: western sword, european sword, medieval, knight
```

### Step 4: Set Parameters

| パラメータ | 推奨値 | 備考 |
|-----------|--------|------|
| Sampler | DPM++ 2M | 汎用最推奨 |
| Scheduler | Karras | DPM++ 2M と最も安定 |
| Steps | 25-35 | 20 以下は品質低下、40 以上は収穫逓減 |
| CFG | 5-7 | **SDXL のスイートスポット**。9 超は過飽和リスク |
| Denoise | 1.0 | txt2img では常に 1.0 |
| Batch size | 4 | 比較選択のため |

**解像度** (SDXL 安全なアスペクト比):

| 用途 | 解像度 | 比率 |
|------|--------|------|
| Pixiv カバー | 768x1024 | 3:4 |
| X ヘッダー | 1536x512 | 3:1 |
| X アイコン | 1024x1024 | 1:1 |
| 汎用正方形 | 1024x1024 | 1:1 |
| ワイド風景 | 1344x768 | 16:9 |

**注意**: 900x900, 1000x1000 等の非標準値は品質低下を招く。

### Step 5: Prompt Weighting (必要な場合のみ)

| 構文 | 効果 | 実用範囲 |
|------|------|---------|
| `(keyword:1.2)` | 強調 | 0.8-1.4 が安全帯 |
| `[keyword]` | 減衰 (x0.9) | |
| `BREAK` | チャンク強制分割 | 大文字必須 |

- 1.4 を超える重みはほぼ不要（SDXL は重みに敏感）
- BREAK の直後の要素は新チャンク先頭として強い影響力を持つ

## Iterative Refinement（反復改善）

### 診断テーブル

| 症状 | 原因 | 対処 |
|------|------|------|
| 平坦/フラット | CFG 低い or 照明記述なし | CFG +1, 照明キーワード追加 |
| ぼやけ | Steps 不足 | Steps 30 に |
| 過飽和/ギラギラ | CFG 高すぎ | CFG 5-6 に下げる |
| AI っぽい/不自然に綺麗 | テクスチャ不足 | `film grain`, `slight imperfections` 追加 |
| 構図が意図と違う | プロンプトが曖昧 | 位置関係・カメラアングルを明記 |
| スタイル不安定 | スタイルキーワード弱い | `(style:1.2-1.3)` で重み付け |
| 被写体が違うものになる | 語彙が一般的すぎる | 専門用語で具体化 (例: katana → nihonto) |

### 修正の原則

1. **1 回 1 変更**: 複数同時変更は原因特定を困難にする
2. **同じシード**で比較: seed 固定 → 変更箇所の効果だけを確認
3. **ネガティブは後追い**: 最初はネガティブなし → 問題が出たら追加

## ComfyUI Workflow JSON 出力

プロンプト設計後、ComfyUI 互換の JSON ワークフローを出力できる。

**テンプレート構造**:
- Node 1: CheckpointLoaderSimple
- Node 2: CLIPTextEncode (POSITIVE)
- Node 3: CLIPTextEncode (NEGATIVE)
- Node 4: EmptyLatentImage
- Node 5: KSampler
- Node 6: VAEDecode
- Node 7: SaveImage

既存の JSON テンプレートは `docs/marketing/comfyui/` を参照。

## ComfyUI API 実行

ComfyUI Desktop が起動中の場合、API で直接生成できる:

```bash
# 生成リクエスト
curl -s -X POST http://127.0.0.1:8000/prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt": { ... }}'

# 結果取得
curl -s http://127.0.0.1:8000/history/{prompt_id}

# 画像ダウンロード
curl -s "http://127.0.0.1:8000/view?filename={filename}" -o output.png
```

**注意**: ComfyUI Desktop のデフォルトポートは **8000**（通常の ComfyUI は 8188）。

## Output

1. **Positive prompt** (英語、自然言語 + タグハイブリッド)
2. **Negative prompt** (英語、50-150 語)
3. **推奨パラメータ** (sampler, steps, CFG, 解像度)
4. **ComfyUI JSON** (必要に応じて)
5. **改善メモ** (生成結果を見て次に試すべき変更)
