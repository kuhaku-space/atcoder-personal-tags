from setting import Base, engine
from sqlalchemy import Column, Integer, String


class Tag(Base):
    __tablename__ = "tags"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    problem_id = Column("problem_id", String(100))
    contest_id = Column("contest_id", String(100))
    tag = Column("tag", String(200))


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
