#!/usr/bin/env python3
"""
novel_db.py — 小説プロジェクト管理用 SQLite データベース

使い方:
  python tools/novel_db.py init                    # DB初期化
  python tools/novel_db.py query <sql>             # 任意のSQLを実行
  python tools/novel_db.py characters <project>    # キャラ一覧
  python tools/novel_db.py foreshadowing <project> # 伏線一覧
  python tools/novel_db.py timeline <project>      # タイムライン
  python tools/novel_db.py episodes <project>      # エピソード一覧
  python tools/novel_db.py terms <project>         # 用語辞書
  python tools/novel_db.py objects <project>       # 重要アイテム
  python tools/novel_db.py relationships <project> # キャラ関係
  python tools/novel_db.py ep-cast <project> <ep>  # 特定話の登場キャラ
  python tools/novel_db.py char-eps <project> <char> # 特定キャラの登場話
  python tools/novel_db.py export-md <project> <table> # Markdown出力
"""

import sqlite3
import sys
import json
import os
import io
from pathlib import Path
from datetime import datetime

# Windows cp932 対策
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

DB_PATH = Path(__file__).parent.parent / "novel.db"

SCHEMA = """
-- プロジェクト
CREATE TABLE IF NOT EXISTS projects (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT,
    status TEXT DEFAULT 'active',
    platform TEXT,
    target_readers TEXT,
    logline TEXT,
    theme TEXT,
    sensory_axis TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
);

-- キャラクター
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id TEXT NOT NULL REFERENCES projects(id),
    name TEXT NOT NULL,
    name_reading TEXT,
    role TEXT,
    designation TEXT,
    ghost TEXT,
    lie TEXT,
    want TEXT,
    need TEXT,
    theme_answer TEXT,
    voice_style TEXT,
    arc_summary TEXT,
    notes TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    UNIQUE(project_id, name)
);

-- キャラクター間関係
CREATE TABLE IF NOT EXISTS character_relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id TEXT NOT NULL REFERENCES projects(id),
    char_a_id INTEGER NOT NULL REFERENCES characters(id),
    char_b_id INTEGER NOT NULL REFERENCES characters(id),
    relation_type TEXT,
    a_to_b TEXT,
    b_to_a TEXT,
    tension TEXT,
    evolution TEXT,
    CHECK(char_a_id != char_b_id)
);

-- エピソード
CREATE TABLE IF NOT EXISTS episodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id TEXT NOT NULL REFERENCES projects(id),
    number INTEGER NOT NULL,
    title_ja TEXT,
    title_en TEXT,
    arc TEXT,
    pov TEXT,
    word_count INTEGER,
    editor_score INTEGER,
    proofreader_score INTEGER,
    total_score INTEGER,
    status TEXT DEFAULT 'planned',
    summary TEXT,
    notes TEXT,
    in_story_date TEXT,
    season TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    UNIQUE(project_id, number)
);

-- エピソード×キャラクター（登場管理）
CREATE TABLE IF NOT EXISTS episode_characters (
    episode_id INTEGER NOT NULL REFERENCES episodes(id),
    character_id INTEGER NOT NULL REFERENCES characters(id),
    role_in_episode TEXT,
    pov_scenes TEXT,
    notes TEXT,
    PRIMARY KEY(episode_id, character_id)
);

-- 伏線
CREATE TABLE IF NOT EXISTS foreshadowing (
    id TEXT NOT NULL,
    project_id TEXT NOT NULL REFERENCES projects(id),
    subject TEXT NOT NULL,
    category TEXT,
    setup_episode INTEGER,
    setup_description TEXT,
    resolution_episode INTEGER,
    resolution_description TEXT,
    status TEXT DEFAULT 'unresolved',
    notes TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    PRIMARY KEY(project_id, id)
);

-- 伏線×エピソード（進行管理）
CREATE TABLE IF NOT EXISTS foreshadowing_episodes (
    project_id TEXT NOT NULL,
    foreshadowing_id TEXT NOT NULL,
    episode_number INTEGER NOT NULL,
    role TEXT,
    description TEXT,
    FOREIGN KEY(project_id, foreshadowing_id) REFERENCES foreshadowing(project_id, id),
    PRIMARY KEY(project_id, foreshadowing_id, episode_number)
);

-- タイムライン
CREATE TABLE IF NOT EXISTS timeline_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id TEXT NOT NULL REFERENCES projects(id),
    in_story_date TEXT,
    season TEXT,
    event_description TEXT NOT NULL,
    episode_number INTEGER,
    characters_involved TEXT,
    is_backstory INTEGER DEFAULT 0,
    notes TEXT
);

-- 用語辞書（スタイルガイド）
CREATE TABLE IF NOT EXISTS terms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id TEXT NOT NULL REFERENCES projects(id),
    term TEXT NOT NULL,
    reading TEXT,
    meaning TEXT,
    category TEXT,
    first_episode INTEGER,
    aliases TEXT,
    notes TEXT,
    UNIQUE(project_id, term)
);

-- 重要アイテム
CREATE TABLE IF NOT EXISTS objects_of_significance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id TEXT NOT NULL REFERENCES projects(id),
    name TEXT NOT NULL,
    first_episode INTEGER,
    symbolism TEXT,
    evolution TEXT,
    current_holder TEXT,
    notes TEXT,
    UNIQUE(project_id, name)
);

-- 重要アイテム×エピソード
CREATE TABLE IF NOT EXISTS object_episodes (
    object_id INTEGER NOT NULL REFERENCES objects_of_significance(id),
    episode_number INTEGER NOT NULL,
    description TEXT,
    PRIMARY KEY(object_id, episode_number)
);

-- 事件設計（ミステリー用）
CREATE TABLE IF NOT EXISTS mystery_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id TEXT NOT NULL REFERENCES projects(id),
    episode_number INTEGER NOT NULL,
    category TEXT,
    culprit_or_cause TEXT,
    motive_or_mechanism TEXT,
    clues TEXT,
    red_herrings TEXT,
    resolution TEXT,
    theme_connection TEXT,
    psychological_impact TEXT,
    notes TEXT,
    UNIQUE(project_id, episode_number)
);
"""


def get_db():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")


def query(sql, params=None):
    conn = get_db()
    try:
        cursor = conn.execute(sql, params or [])
        if sql.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            if not rows:
                print("(no results)")
                return
            headers = [d[0] for d in cursor.description]
            print("\t".join(headers))
            print("-" * 80)
            for row in rows:
                print("\t".join(str(v) if v is not None else "" for v in row))
        else:
            conn.commit()
            print(f"OK ({cursor.rowcount} rows affected)")
    finally:
        conn.close()


def list_table(project_id, table, order_by=None):
    conn = get_db()
    order = f"ORDER BY {order_by}" if order_by else ""
    rows = conn.execute(
        f"SELECT * FROM {table} WHERE project_id = ? {order}", [project_id]
    ).fetchall()
    conn.close()
    if not rows:
        print(f"(no {table} for project '{project_id}')")
        return
    headers = [d[0] for d in rows[0].keys()] if hasattr(rows[0], 'keys') else []
    headers = rows[0].keys()
    print("\t".join(headers))
    print("-" * 80)
    for row in rows:
        print("\t".join(str(v) if v is not None else "" for v in row))


def ep_cast(project_id, ep_number):
    conn = get_db()
    rows = conn.execute("""
        SELECT c.name, ec.role_in_episode, ec.pov_scenes, ec.notes
        FROM episode_characters ec
        JOIN characters c ON ec.character_id = c.id
        JOIN episodes e ON ec.episode_id = e.id
        WHERE e.project_id = ? AND e.number = ?
    """, [project_id, ep_number]).fetchall()
    conn.close()
    if not rows:
        print(f"(no characters for Ep.{ep_number} in '{project_id}')")
        return
    print("name\trole\tpov_scenes\tnotes")
    print("-" * 60)
    for row in rows:
        print(f"{row['name']}\t{row['role_in_episode'] or ''}\t{row['pov_scenes'] or ''}\t{row['notes'] or ''}")


def char_episodes(project_id, char_name):
    conn = get_db()
    rows = conn.execute("""
        SELECT e.number, e.title_ja, ec.role_in_episode, ec.pov_scenes
        FROM episode_characters ec
        JOIN characters c ON ec.character_id = c.id
        JOIN episodes e ON ec.episode_id = e.id
        WHERE e.project_id = ? AND c.name LIKE ?
        ORDER BY e.number
    """, [project_id, f"%{char_name}%"]).fetchall()
    conn.close()
    if not rows:
        print(f"(no episodes for '{char_name}' in '{project_id}')")
        return
    print("ep\ttitle\trole\tpov")
    print("-" * 60)
    for row in rows:
        print(f"{row['number']}\t{row['title_ja'] or ''}\t{row['role_in_episode'] or ''}\t{row['pov_scenes'] or ''}")


def relationships(project_id):
    conn = get_db()
    rows = conn.execute("""
        SELECT ca.name as char_a, cb.name as char_b,
               cr.relation_type, cr.a_to_b, cr.b_to_a, cr.tension, cr.evolution
        FROM character_relationships cr
        JOIN characters ca ON cr.char_a_id = ca.id
        JOIN characters cb ON cr.char_b_id = cb.id
        WHERE cr.project_id = ?
    """, [project_id]).fetchall()
    conn.close()
    if not rows:
        print(f"(no relationships for '{project_id}')")
        return
    print("A\tB\ttype\tA→B\tB→A\ttension\tevolution")
    print("-" * 100)
    for row in rows:
        print("\t".join(str(v) if v is not None else "" for v in row))


def export_md(project_id, table):
    """Export a table as markdown for agents to consume."""
    conn = get_db()
    if table == "foreshadowing":
        rows = conn.execute("""
            SELECT id, subject, category, status, setup_description, resolution_description, notes
            FROM foreshadowing WHERE project_id = ? ORDER BY id
        """, [project_id]).fetchall()
        if not rows:
            print("(no data)")
            return
        print(f"# Foreshadowing: {project_id}\n")
        print("| ID | Subject | Category | Status | Setup | Resolution |")
        print("|---|---|---|---|---|---|")
        for r in rows:
            status_icon = {"unresolved": "🔴", "in_progress": "🟡", "resolved": "🟢"}.get(r["status"], "⚪")
            print(f"| {r['id']} | {r['subject']} | {r['category'] or ''} | {status_icon} {r['status']} | {r['setup_description'] or ''} | {r['resolution_description'] or ''} |")

    elif table == "episodes":
        rows = conn.execute("""
            SELECT number, title_ja, title_en, arc, pov, word_count, total_score, status, in_story_date, season
            FROM episodes WHERE project_id = ? ORDER BY number
        """, [project_id]).fetchall()
        if not rows:
            print("(no data)")
            return
        print(f"# Episodes: {project_id}\n")
        print("| # | Title | Arc | POV | Words | Score | Status | Date | Season |")
        print("|---|---|---|---|---|---|---|---|---|")
        for r in rows:
            print(f"| {r['number']} | {r['title_ja'] or ''} ({r['title_en'] or ''}) | {r['arc'] or ''} | {r['pov'] or ''} | {r['word_count'] or ''} | {r['total_score'] or ''} | {r['status']} | {r['in_story_date'] or ''} | {r['season'] or ''} |")

    elif table == "timeline":
        rows = conn.execute("""
            SELECT in_story_date, season, event_description, episode_number, characters_involved, is_backstory
            FROM timeline_events WHERE project_id = ? ORDER BY is_backstory DESC, episode_number, id
        """, [project_id]).fetchall()
        if not rows:
            print("(no data)")
            return
        print(f"# Timeline: {project_id}\n")
        backstory = [r for r in rows if r["is_backstory"]]
        main = [r for r in rows if not r["is_backstory"]]
        if backstory:
            print("## Backstory\n")
            for r in backstory:
                print(f"- **{r['in_story_date'] or '?'}**: {r['event_description']} [{r['characters_involved'] or ''}]")
            print()
        if main:
            print("## Main Timeline\n")
            print("| Date | Season | Ep | Event | Characters |")
            print("|---|---|---|---|---|")
            for r in main:
                print(f"| {r['in_story_date'] or ''} | {r['season'] or ''} | {r['episode_number'] or ''} | {r['event_description']} | {r['characters_involved'] or ''} |")

    elif table == "terms":
        rows = conn.execute("""
            SELECT term, reading, meaning, category, first_episode, aliases
            FROM terms WHERE project_id = ? ORDER BY category, term
        """, [project_id]).fetchall()
        if not rows:
            print("(no data)")
            return
        print(f"# Style Guide Terms: {project_id}\n")
        print("| Term | Reading | Meaning | Category | First Ep | Aliases |")
        print("|---|---|---|---|---|---|")
        for r in rows:
            print(f"| {r['term']} | {r['reading'] or ''} | {r['meaning'] or ''} | {r['category'] or ''} | {r['first_episode'] or ''} | {r['aliases'] or ''} |")

    else:
        print(f"Unknown table for export: {table}")

    conn.close()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "init":
        init_db()
    elif cmd == "query" and len(sys.argv) >= 3:
        query(" ".join(sys.argv[2:]))
    elif cmd == "characters" and len(sys.argv) >= 3:
        list_table(sys.argv[2], "characters", "name")
    elif cmd == "foreshadowing" and len(sys.argv) >= 3:
        list_table(sys.argv[2], "foreshadowing", "id")
    elif cmd == "timeline" and len(sys.argv) >= 3:
        list_table(sys.argv[2], "timeline_events", "episode_number")
    elif cmd == "episodes" and len(sys.argv) >= 3:
        list_table(sys.argv[2], "episodes", "number")
    elif cmd == "terms" and len(sys.argv) >= 3:
        list_table(sys.argv[2], "terms", "category, term")
    elif cmd == "objects" and len(sys.argv) >= 3:
        list_table(sys.argv[2], "objects_of_significance", "first_episode")
    elif cmd == "relationships" and len(sys.argv) >= 3:
        relationships(sys.argv[2])
    elif cmd == "ep-cast" and len(sys.argv) >= 4:
        ep_cast(sys.argv[2], int(sys.argv[3]))
    elif cmd == "char-eps" and len(sys.argv) >= 4:
        char_episodes(sys.argv[2], sys.argv[3])
    elif cmd == "export-md" and len(sys.argv) >= 4:
        export_md(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
