import streamlit as st

st.title("Choose your favorite star")

col1, col2 = st.columns(2)

with col1:
    st.header("Babar Azam")
    vote1 = st.button("Vote for Babar")
    st.image("https://www.behance.net/gallery/118715821/Babar-Azam?tracking_source=search_projects|babar+azam&l=7")
with col2:
    st.header("Virat Kohli")
    vote2 = st.button("Vote for Virat")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDN_x3qsMAqlbRhBpGwv44hqQphdGCvCQkGD4hTuAww4EhMOVJyT2l55-hj2WMNBfit5ExLhwCdozA9eD-Ae2yCsqtFAoTvzu23yt80uCWrQ&s=10")

# Voting result
if vote1:
    st.success("Thanks for voting for Babar Azam!")

elif vote2:
    st.success("Thanks for voting for Virat Kohli!")

# Sidebar input
name = st.sidebar.text_input("Enter Your Name")
choice = st.sidebar.selectbox("Select one:", ["Babar Azam", "Virat Kohli"])

st.write(f"Your name is {name} and you chose {choice}")

# Expander (FIXED)
with st.expander("See Details"):
    st.write("""
    1. Babar Azam is one of the best batsmen in the world.
    2. Virat Kohli is one of the best batsmen in the world.
    """)

st.markdown("### Thank you for participating in the poll!")