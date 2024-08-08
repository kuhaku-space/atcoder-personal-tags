import streamlit as st
from services.models import Tag
from services.setting import session
from services.url_parse import (
    get_contest_id_from_problem_url,
    get_problem_id_from_problem_url,
)


def display() -> None:
    problem_url = st.text_input("問題URL")
    contest_id = get_contest_id_from_problem_url(problem_url)
    problem_id = get_problem_id_from_problem_url(problem_url)
    st.markdown(f"コンテストID : {contest_id}")
    st.markdown(f"問題ID : {problem_id}")
    tag_name = st.text_input("タグ名")
    submitted = st.button("追加")

    if submitted:
        if contest_id and problem_id and tag_name:
            session.add(Tag(problem_id=problem_id, contest_id=contest_id, tag=tag_name))
            session.commit()


if __name__ == "__main__":
    display()
