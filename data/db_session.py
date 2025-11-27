import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

SqlAlchemyBase = orm.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Укажи файл базы, дурень")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключаемся к базе ({conn_str})")

    engine = sa.create_engine(conn_str, echo=False, pool_size=0)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session():
    global __factory
    return __factory()


def get_db():
    global __factory
    session = __factory()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
