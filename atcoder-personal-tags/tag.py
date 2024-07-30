from pathlib import Path

import yaml
from models import Tag
from setting import session


def create_tag_data():
    session.query(Tag).delete()
    tag_dir = Path("tag/")
    for path in tag_dir.iterdir():
        with path.open() as f:
            tag_data: dict[str, list[str]] = yaml.safe_load(f)
            contest_id = str.lower(path.stem)
            for problem, tags in tag_data.items():
                problem_id = contest_id + "_" + str.lower(problem)
                for tag in tags:
                    session.add(
                        Tag(problem_id=problem_id, contest_id=contest_id, tag=tag)
                    )
    session.commit()


if __name__ == "__main__":
    create_tag_data()
