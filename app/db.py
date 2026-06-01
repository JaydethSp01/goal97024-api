import os
import psycopg
from psycopg.rows import dict_row

DATABASE_URL = os.environ.get('DATABASE_URL')

try:
    conn = psycopg.connect(DATABASE_URL, row_factory=dict_row)
except:
    conn = None

if not conn:
    print('Falling back to in-memory database')
    # Memory database setup here
