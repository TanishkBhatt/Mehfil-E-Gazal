import streamlit as st
from utils.fetch_song import get_song_names, fetch_song

st.set_page_config(
    page_title="Mehfil-e-Gazal"
)

st.title("MEHFIL E GAZAL")
st.caption("A WONDERFUL COLLECTION OF GAZHAL AND QAWWALI")
st.markdown("")
st.markdown("")

with st.form(key="get-song"):
    song = st.selectbox("ENTER THE NAME OF SONG YOU WANNA GO THROUGH",
                        get_song_names("datasets/songs.json"))
    get_song = st.form_submit_button("GET SONG", type="primary")

if get_song:
    data = fetch_song("datasets/songs.json", song)
    st.markdown("")
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### ABOUT SONG")
        st.dataframe({
            "SINGER": data["Singer"],
            "WRITER": data["Writer"]
        })

        st.markdown("##### CATEGORIES")
        col3, col4 = st.columns(2)
        with col3:
            with st.container(border=True):
                st.markdown(data["Category"][0])
        with col4:
            with st.container(border=True):
                st.markdown(data["Category"][1])

        st.markdown("##### LYRICS")
        with st.container(border=True):
            st.markdown(f"""
                - {data["Lyrics"][0]}
                - {data["Lyrics"][1]}
            """)
    with col2:
        st.markdown("##### SINGER OF THE SONG")
        try:
            st.image(f"datasets/img/{data["Singer"]}.jpeg")
        except:
            st.error("ERROR - IMAGE NOT FOUND")

    st.markdown("")
    st.markdown("")

    with st.container(border=True):
        st.markdown("#### LISTEN TO SONG")
        try:
            st.audio(f"datasets/audio/{song}.mp3")
        except:
            st.error("ERROR - AUDIO NOT FOUND")

st.markdown("")
st.markdown("")
st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")