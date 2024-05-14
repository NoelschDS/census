import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code

def rent_demographics() -> None:

    #Collect Rent Data
    rent = pd.read_csv('rent_data.csv', index_col=2).drop(["Unnamed: 0", 'state'], axis=1)
    rent["year"] = pd.to_datetime(rent.year, format='%Y')
    rent["variable"]=rent["variable"].str.replace("PEDIS", "")
    rent["variable"]=rent["variable"].str.replace("DRS", "Difficulty Dressing")
    rent["variable"]=rent["variable"].str.replace("EYE", "Difficulty Seeing")
    rent["variable"]=rent["variable"].str.replace("EAR", "Difficulty Hearing")
    rent["variable"]=rent["variable"].str.replace("OUT", "Difficulty Doing Errands")
    rent["variable"]=rent["variable"].str.replace("PHY", "Difficulty Walking")
    rent["variable"]=rent["variable"].str.replace("REM", "Difficulty Remembering")
    
    rent_yes = rent[rent["variable"].str.contains("Yes")]
    rent_yes["variable"] = rent_yes["variable"].str.replace("_Yes", "")
    cats = st.multiselect(
        "Choose Disability of Interest", list(rent_yes.variable.unique())
    )

    if not cats:
        st.error("Please select a disability")
    else:
        data=rent_yes[rent_yes["variable"].isin(cats)]
        cities = st.multiselect(
            "Choose Cities of Interest", list(rent_yes.index.unique())
        )
        all_options = st.checkbox("Select All Cities")

        if all_options:
            cities = list(rent_yes.index.unique())

        if not cities:
            st.error("Please select a combination of cities")
        else:    
            data=data.loc[cities]
            summed=data.groupby(["HETENURE", "year"], as_index=False).sum("value")

            fig = alt.Chart(summed).mark_line().encode(
            x='year',
            y='value',
            color=alt.Color('HETENURE', legend=alt.Legend(orient='top', labelLimit = 400,direction = 'horizontal', title='Tenure')))

            st.altair_chart(fig, use_container_width=True)

            st.write(data)

    # Interactive Streamlit elements, like these sliders, return their value.
    # This gives you an extremely simple interaction model.
    #iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)

    # Non-interactive elements return a placeholder to their location
    # in the app. Here we're storing progress_bar to update it later.
    #progress_bar = st.sidebar.progress(0)

    # These two elements will be filled in later, so we create a placeholder
    # for them using st.empty()
    #frame_text = st.sidebar.empty()
    #image = st.empty()


    # We clear elements by calling empty on them.
    #progress_bar.empty()
    #frame_text.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


st.set_page_config(page_title="Rent Demographics", page_icon="")
st.markdown("# Rent")
st.sidebar.header("Rent")
st.write(
    """This summary displays total persons with disabilities by their rental status."""
)

rent_demographics()
