import streamlit as st
from utils.fetch_song import get_song_names, fetch_song
from utils.recommendations import recommend_more

st.set_page_config(
    page_title="Mehfil-e-Gazal"
)

st.title("MEHFIL E GAZAL")
st.caption("A MARVELLOUS COLLECTION OF GAZAL AND QAWWALI")
st.markdown("")
st.markdown("")

with st.form(key="get-song"):
    song = st.selectbox(
        "SELECT THE SONG YOU WANNA GO THROUGH",
        sorted(get_song_names("datasets/songs.json"))
    )
    
    get_song = st.form_submit_button("__GET SONG__", type="primary")

if get_song:
    data = fetch_song("datasets/songs.json", song)
    st.markdown("")
    st.markdown("")

    if data:
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

            st.markdown("##### INITIAL LYRICS")
            with st.container(border=True):
                st.markdown(f"""
                    - {data["Lyrics"][0]}
                    - {data["Lyrics"][1]}
                """.title())
        with col2:
            st.markdown("##### SINGER OF THE SONG")
            try:
                st.image(f"datasets/img/{data["Singer"]}.jpeg")
            except:
                st.error("ERROR - IMAGE NOT AVAILABLE")

        st.markdown("")
        st.markdown("")

        with st.container(border=True):
            st.markdown("#### LISTEN TO SONG")
            st.markdown(f"{song} by {data["Singer"]}")

            try:
                st.audio(f"datasets/audio/{song}.mp3")
            except:
                st.error("ERROR - AUDIO NOT AVAILABLE")

        st.markdown("")
        st.markdown("")

        st.markdown("#### FURTHER RECOMMENDATIONS")
        st.markdown("")
        
        with st.container(border=True):
            recommended_by_singer, recommended_by_category = recommend_more("datasets/songs.json", data["Singer"], data["Category"])
            if (song, data["Singer"]) in recommended_by_singer:
                recommended_by_singer.remove((song, data["Singer"]))

            st.markdown("##### FROM THE SAME SINGER")
            st.markdown("")

            if recommended_by_singer:
                for rec_song in recommended_by_singer:
                    try:
                        st.markdown(f"{rec_song[0]} By {rec_song[1]}")
                        st.audio(f"datasets/audio/{rec_song[0]}.mp3")
                    except:
                        st.error("ERROR - AUDIO NOT AVAILABLE")
            else:
                st.warning("NO MORE SONGS AVAILABLE FROM THIS SINGER")

        st.markdown("")

        with st.container(border=True):
            st.markdown("##### RELATED TO THAT CATEGORY")

            col5, col6 = st.columns(2)
            with col5:
                with st.container(border=True):
                    st.markdown(data["Category"][0])
            with col6:
                with st.container(border=True):
                    st.markdown(data["Category"][1])

            st.markdown("")
            
            if recommended_by_category:
                for rec_song in recommended_by_category:
                    try:
                        st.markdown(f"{rec_song[0]} By {rec_song[1]}")
                        st.audio(f"datasets/audio/{rec_song[0]}.mp3")
                    except:
                        st.error("ERROR - AUDIO NOT AVAILABLE")
            else:
                st.warning("NO MORE SONGS AVAILABLE FROM THESE CATEGORIES")

st.markdown("")
st.markdown("")
st.caption("DEVELOPED BY TANISHK | COOPERATED BY AKSHAY")
