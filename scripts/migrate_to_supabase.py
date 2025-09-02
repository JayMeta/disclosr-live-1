#!/usr/bin/env python3
"""Simple migration script: read SQLite DB and insert rows into Postgres via SQLAlchemy.

Usage:
  python scripts/migrate_to_supabase.py --sqlite PATH_TO/sqlite.db --pg "postgresql://..."
"""
import argparse
import os
import sqlite3
from urllib.parse import urlparse

from sqlalchemy import create_engine, MetaData, Table, Column, String, Text, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


def ensure_table(engine):
    meta = MetaData()
    filings = Table(
        'filings', meta,
        Column('id', String, primary_key=True),
        Column('exchange', Text),
        Column('symbol', Text),
        Column('company', Text),
        Column('headline', Text),
        Column('filed_at', DateTime),
        Column('pdf_url', Text),
        Column('pdf_storage_url', Text),
        Column('summary', Text),
        Column('impact_score', Numeric),
        Column('created_at', DateTime, server_default=func.now()),
    )
    meta.create_all(engine)
    return filings


def migrate(sqlite_path, pg_url):
    if not os.path.exists(sqlite_path):
        raise SystemExit(f"SQLite DB not found: {sqlite_path}")

    sconn = sqlite3.connect(sqlite_path)
    sconn.row_factory = sqlite3.Row
    scur = sconn.cursor()
    scur.execute('SELECT * FROM filings')
    rows = scur.fetchall()

    engine = create_engine(pg_url)
    filings = ensure_table(engine)
    ins = filings.insert()
    with engine.begin() as conn:
        count = 0
        for r in rows:
            data = {k: r[k] for k in r.keys()}
            if 'id' not in data or not data['id']:
                import uuid
                data['id'] = str(uuid.uuid4())
            conn.execute(ins.values(**data))
            count += 1
    print(f"Migrated {count} rows")


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--sqlite', required=True)
    p.add_argument('--pg', required=True)
    args = p.parse_args()
    migrate(args.sqlite, args.pg)
