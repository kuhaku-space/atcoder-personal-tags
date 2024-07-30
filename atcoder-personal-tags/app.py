import streamlit as st
from models import Tag
from setting import session
from sqlalchemy import distinct, select


def get_tag_list() -> list[str]:
    tag_query = select(distinct(Tag.tag))
    return list(session.scalars(tag_query))


def get_problem_list(selected_tag: str | None):
    problem_query = select(Tag).where(Tag.tag == selected_tag)
    return session.scalars(problem_query)


selected_tag = st.selectbox("selectbox", get_tag_list())
for row in get_problem_list(selected_tag):
    problem_str = str.upper(str(row.problem_id).replace("_", ""))
    link = f"[{problem_str}](https://atcoder.jp/contests/{row.contest_id}/tasks/{row.problem_id})"
    st.markdown(link)
