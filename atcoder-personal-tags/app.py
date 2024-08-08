import streamlit as st
from pages import dashboard


def main():
    st.title("Atcoder Personal Tags")
    dashboard.display()


if __name__ == "__main__":
    main()
