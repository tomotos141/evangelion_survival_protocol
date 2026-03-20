# ACTIONLOG 記録テンプレート

## 記録タイミング

Quality Gate 判定完了後（通過・不通過いずれも）、以下の JSONL エントリを追記する。
ログ記録の失敗は生成フローを止めない（サイレント無視）。

## 記録先

- team-write-episode: `.claude/skills/team-write-episode/reference/actions.jsonl`
- team-rewrite-episode: `.claude/skills/team-rewrite-episode/reference/actions.jsonl`

## JSONL フォーマット

```bash
python -c "
import json
from datetime import datetime

entry = json.dumps({
    'date': datetime.now().isoformat(),
    'skill': '${SKILL_NAME}',
    'project': '${PROJECT}',
    'episode': '${EPISODE}',
    'word_count': ${WORD_COUNT},
    'editor_score': ${EDITOR_SCORE},
    'proofreader_score': ${PROOFREADER_SCORE},
    'first_reader_score': ${FIRST_READER_SCORE},
    'mystery_auditor_score': ${MYSTERY_AUDITOR_SCORE},
    'freshness_score': ${FRESHNESS_SCORE},
    'total_score': ${TOTAL_SCORE},
    'retries': ${RETRY_COUNT},
    'outcome': '${OUTCOME}',
    'rewrite_focus': '${REWRITE_FOCUS}',
}, ensure_ascii=False)

p = '.claude/skills/${SKILL_NAME}/reference/actions.jsonl'
open(p, 'a', encoding='utf-8').write(entry + '\n')
print(f'Logged: {entry}')
"
```

## フィールド説明

| フィールド | 型 | 説明 |
|-----------|---|------|
| date | string | ISO 8601 タイムスタンプ |
| skill | string | `team-write-episode` or `team-rewrite-episode` |
| project | string | プロジェクト名（例: `battousai`, `angel_return`） |
| episode | string | エピソードファイル名（例: `07_intersection`） |
| word_count | number | 最終ドラフトの文字数 |
| editor_score | number | Editor スコア（/25） |
| proofreader_score | number | Proofreader スコア（/25） |
| first_reader_score | number | First Reader スコア（/20） |
| mystery_auditor_score | number | Mystery Auditor スコア（/15、スキップ時は null） |
| freshness_score | number | Freshness Check スコア（/15） |
| total_score | number | 合計スコア（/100） |
| retries | number | Quality Gate リトライ回数（0 = 一発通過） |
| outcome | string | `pass` / `fail` / `manual_override` |
| rewrite_focus | string | リライト時のみ: `logic_fix` / `style_polish` / `full_rewrite` / `all`。新規執筆時は空文字 |

## 注意事項

- `.jsonl` ファイルは `.gitignore` 済み（テレメトリは git 管理不要）
- `/evolve` スキルおよび `/writing-report` スキルが分析に使用する
