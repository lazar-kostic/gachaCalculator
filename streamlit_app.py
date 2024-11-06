import streamlit as st

#Stores information about banners
class Banner:
    def __init__(self, name, hard_pity, chance, chance_per_pull, fate_points, currency, guarantee, win_chance):
        self.name = name
        self.hard_pity = hard_pity
        self.chance = chance
        self.chance_per_pull = chance_per_pull
        self.fate_points = fate_points
        self.currency = currency
        self.guarantee = guarantee
        self.win_chance = win_chance

    def remaining_pulls(self, current_pity, guarantee, fate_points):
        if(self.guarantee == False):
            return self.hard_pity - current_pity
        elif(self.fate_points == None):
            return self.hard_pity * (2 - int(guarantee)) - current_pity
        else:
            return self.hard_pity * (self.fate_points - fate_points + 1) - current_pity

    def chance_on_next_pull(self, current_pity, guarantee, fate_points):
        if(self.guarantee == False):
            return self.chance_per_pull[current_pity]
        elif(self.fate_points == None):
            if(guarantee):
                multiplier = 1
            else:
                multiplier = self.win_chance
            return self.chance_per_pull[current_pity] * multiplier
        else:
            if(self.fate_points == fate_points):
                multiplier = 1
            elif(guarantee):
                multiplier = .5
            else:
                multiplier = .375
            return self.chance_per_pull[current_pity] * multiplier

    def get_banner_info(self):
        return{
            "name": self.name,
            "hard_pity": self.hard_pity,
            "chance": self.chance,
            "chance_per_pull": self.chance_per_pull,
            "fate_points": self.fate_points,
            "currency": self.currency,
            "guarantee": self.guarantee,
            "win_chance": self.win_chance
        }
    
#General Gacha Game 
class GachaGame:
    def __init__(self, name, currency):
        self.name = name
        self.currency = currency

    def render_widgets(self):
        """Override this method in subclasses to define game-specific widgets."""
        pass


#Modified for Genshin Impact
class GenshinImpact(GachaGame):
    def __init__(self):
        super().__init__("Genshin Impact", "Primogems")
        #Initialize banners
        self.banners = {
            "Character Banner": Banner("Character Banner", 90, 0.6, 
            [0.6, 1.196, 1.788, 2.379, 2.965, 3.547, 4.126, 4.701, 5.272, 5.84, 6.405, 6.966, 7.524, 8.078, 8.63, 9.179, 9.724, 10.265, 10.804, 11.34, 11.871, 12.399, 12.924, 13.447, 13.966, 14.483, 14.996, 15.507, 16.014, 16.517, 17.018, 17.516, 18.011, 18.502, 18.991, 19.477, 19.96, 20.44, 20.917, 21.392, 21.863, 22.332, 22.799, 23.263, 23.724, 24.181, 24.637, 25.09, 25.538, 25.985, 26.43, 26.872, 27.311, 27.748, 28.182, 28.612, 29.04, 29.466, 29.889, 30.309, 30.727, 31.143, 31.556, 31.966, 32.374, 32.78, 33.184, 33.585, 33.984, 34.38, 34.773, 35.165, 35.553, 35.94, 36.324, 56.951, 70.897, 80.326, 86.701, 91.007, 93.921, 95.891, 97.223, 98.124, 98.732, 99.143, 99.421, 99.608, 99.734, 100],
             None, "Intertwined Fate", True, .50),
            "Weapon Banner": Banner("Weapon Banner", 80, 0.7, 
            [0.7, 1.4, 2.1, 2.8, 3.5, 4.2, 4.9, 5.6, 6.3, 7.0, 7.7, 8.4, 9.1, 9.8, 10.5, 11.2, 11.9, 12.6, 13.3, 14.0, 14.7, 15.4, 16.1, 16.8, 17.5, 18.2, 18.9, 19.6, 20.3, 21.0, 21.7, 22.4, 23.1, 23.8, 24.5, 25.2, 25.9, 26.6, 27.3, 28.0, 28.7, 29.4, 30.1, 30.8, 31.5, 32.2, 32.9, 33.6, 34.3, 35.0, 35.7, 36.4, 37.1, 37.8, 38.5, 39.2, 39.9, 40.6, 41.3, 42.0, 42.7, 43.4, 49.62, 55.84, 62.06, 68.28, 74.5, 80.72, 86.94, 93.16, 99.38, 100, 100, 100, 100, 100, 100, 100, 100, 100],
            1, "Intertwined Fate", True, .75),
            "Standard Banner": Banner("Standard Banner", 90, 0.6, 
            [0.6, 1.196, 1.788, 2.379, 2.965, 3.547, 4.126, 4.701, 5.272, 5.84, 6.405, 6.966, 7.524, 8.078, 8.63, 9.179, 9.724, 10.265, 10.804, 11.34, 11.871, 12.399, 12.924, 13.447, 13.966, 14.483, 14.996, 15.507, 16.014, 16.517, 17.018, 17.516, 18.011, 18.502, 18.991, 19.477, 19.96, 20.44, 20.917, 21.392, 21.863, 22.332, 22.799, 23.263, 23.724, 24.181, 24.637, 25.09, 25.538, 25.985, 26.43, 26.872, 27.311, 27.748, 28.182, 28.612, 29.04, 29.466, 29.889, 30.309, 30.727, 31.143, 31.556, 31.966, 32.374, 32.78, 33.184, 33.585, 33.984, 34.38, 34.773, 35.165, 35.553, 35.94, 36.324, 56.951, 70.897, 80.326, 86.701, 91.007, 93.921, 95.891, 97.223, 98.124, 98.732, 99.143, 99.421, 99.608, 99.734, 100],
            None, "Acquaint Fate", True, .50)
        }

    def render_widgets(self):
        selected_banner = st.selectbox("Select Banner type", list(self.banners.keys()))
        current_pity = st.number_input("Current Pity", min_value=0, max_value=self.banners[selected_banner].hard_pity - 1)
        if(self.banners[selected_banner].guarantee):
            guarantee = st.checkbox("Guarantee?")
        if(self.banners[selected_banner].fate_points != None):
            fate_points = st.number_input("Fate Points", min_value=0, max_value=self.banners[selected_banner].fate_points)
        else:
            fate_points = None
        result = self.banners[selected_banner].remaining_pulls(current_pity, guarantee, fate_points)
        chance_on_next_pull = self.banners[selected_banner].chance_on_next_pull(current_pity, guarantee, fate_points)
        st.header(f'Pulls remaining until desired 5 star: {result}')
        st.progress(chance_on_next_pull / 100)
        st.header(f'Chance of obtaining desired 5 star on next pull: {chance_on_next_pull}%')
        st.write("Chance of getting a 5 star per pull amount")
        st.line_chart(self.banners[selected_banner].chance_per_pull, x_label="Pulls", y_label="Chance (%)")

game_classes = {
    "Genshin Impact": GenshinImpact
}

logos = {
    "Genshin Impact":{
        "side": "https://static.wikia.nocookie.net/gensin-impact/images/8/80/Genshin_Impact.png/revision/latest?cb=20240331104358",
        "top": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/ecfdc2143507869.627bcf6b67e1b.png"
    } 
}

st.sidebar.title("Gacha pull calculator")


# Sidebar for selecting a game
game_name = st.sidebar.selectbox("Select your game:", list(game_classes.keys()))

#Show game logos
st.image(logos[game_name]["top"])
st.sidebar.image(logos[game_name]["side"])

# Create an instance of the selected game
game_instance = game_classes[game_name]()

# Render widgets for the selected game and get user inputs
user_inputs = game_instance.render_widgets()
