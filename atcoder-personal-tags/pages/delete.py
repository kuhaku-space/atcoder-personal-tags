import pandas as pd
import streamlit as st
from services.models import Tag
from services.setting import engine, session
from sqlalchemy import delete, select


def display() -> None:
    tag_query = select(Tag)
    st.dataframe(pd.read_sql(tag_query, engine))
    deleted_id = st.number_input("ID", min_value=0, step=1)
    submitted = st.button("削除")

    if submitted:
        delete_query = delete(Tag).where(Tag.id == deleted_id)
        session.execute(delete_query)
        session.commit()


if __name__ == "__main__":
    display()
