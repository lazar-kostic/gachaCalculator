import streamlit as st

st.title("Gacha pull calculator")
game = st.selectbox("Select game",("Genshin Impact", "Honkai: Star Rail", "Wuthering Waves",
                                    "Zenless Zone Zero"),)
st.write(f'Selected game: {game}')

if game == "Genshin Impact": 
    result = 0 
    current_chance = 0
    hard_pity = [90, 80, 90]
    chances = [0.6, 0.6, 0.6]
    chance_per_pull = [0.6, 1.196, 1.788, 2.379, 2.965, 3.547, 4.126, 4.701, 5.272, 5.84, 6.405, 6.966, 7.524, 8.078, 8.63, 9.179, 9.724, 10.265, 10.804, 11.34, 11.871, 12.399, 12.924, 13.447, 13.966, 14.483, 14.996, 15.507, 16.014, 16.517, 17.018, 17.516, 18.011, 18.502, 18.991, 19.477, 19.96, 20.44, 20.917, 21.392, 21.863, 22.332, 22.799, 23.263, 23.724, 24.181, 24.637, 25.09, 25.538, 25.985, 26.43, 26.872, 27.311, 27.748, 28.182, 28.612, 29.04, 29.466, 29.889, 30.309, 30.727, 31.143, 31.556, 31.966, 32.374, 32.78, 33.184, 33.585, 33.984, 34.38, 34.773, 35.165, 35.553, 35.94, 36.324, 56.951, 70.897, 80.326, 86.701, 91.007, 93.921, 95.891, 97.223, 98.124, 98.732, 99.143, 99.421, 99.608, 99.734, 99.999]

    banner_type = st.selectbox("Select banner type", ("Character banner", "Weapon banner", "Standard banner"),)
    current_pity = st.number_input("Current pity", min_value=0)
    guarantee = st.checkbox("Guarantee?")
    if guarantee:
        result = 90 - current_pity
        if current_pity >= 89:
            current_chance = 100
        else:
            current_chance = chance_per_pull[current_pity]
    else:
        result = 180 - current_pity
        if current_pity >= 89:
            current_chance = 50
        else:
            current_chance = chance_per_pull[current_pity] / 2

    st.header(f'Pulls remaining for desired 5 star: {result}')
    st.progress(current_pity / (current_pity + result))
    st.header(f'Chance of desired 5 star at next pull: {current_chance}%')

    st.write("Chance of 5 star per pull")
    if banner_type == "Character banner":
        st.line_chart(chance_per_pull, x_label="Pull", y_label="Chance (%)")

