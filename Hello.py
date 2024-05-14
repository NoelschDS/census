import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

rent = pd.read_csv('rent_data.csv')
house_type = pd.read_csv('type_data.csv')

def run():
    st.set_page_config(
        page_title="Overview",
        page_icon="👋",
    )

    st.write("# Disability and Housing Realities in America")

    st.sidebar.success("Select a demo above.")

    st.sidebar.header("Home")

    st.markdown(
        """
        This app provides summary statistics to understand the housing realities of people living with disabilities in America.
        **👈 Select a housing variable from the sidebar** to learn more.
        """
    )


if __name__ == "__main__":
    run()
