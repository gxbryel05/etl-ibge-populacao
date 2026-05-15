from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

def carregar(df):
    print("Carregando dados no PostgreSQL...")
    url = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    engine = create_engine(url)

    df.to_sql(
        name='municipios',
        con=engine,
        if_exists='replace',
        index=False
    )
    print(f"{len(df)} registros carregados no PostgreSQL!")