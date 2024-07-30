from models import Base
from setting import engine


class Migration(object):
    def __init__(self):
        self.engine = engine

    def create(self):
        Base.metadata.create_all(bind=self.engine)


if __name__ == "__main__":
    Migration().create()
