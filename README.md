# Gacha Pity Calculator

A simple web app built with Streamlit to help players of various gacha games calculate their pity and track pulls. 
With this calculator, users can input their current pity count, track saved currency, and get an estimate on their chances for obtaining a limited reward.
Currently, the calculator supports the following games:
- Genshin Impact
- Honkai: Star Rail
- Zenless Zone Zero
- Wuthering Waves

## Features

- **Game Selection**: Choose from popular gacha games to customize pity calculations.
- **Pity and Pull Calculations**: Input your current pity and saved currency to calculate pulls until the next limited reward.
- **Probability Estimation**: Get an approximate probability of obtaining a 5-star or limited item on the next pull.
- **Progress Bar**: Visual feedback on your progress towards the next pity threshold.
- **Expandable Settings**: Advanced settings available for adjusting soft pity, rates, and pull simulation.

## Screenshots

(To be added)

## Getting Started

Follow these instructions to get a local copy of the project up and running.

### Prerequisites
- Python 3.7+
- [Streamlit](https://streamlit.io/) (Installation instructions below)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/gacha-pity-calculator.git
   cd gacha-pity-calculator
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   *(Ensure `streamlit` is in your `requirements.txt` or install it separately with `pip install streamlit`.)*

3. **Run the App**:
   ```bash
   streamlit run app.py
   ```
4. **Open in Browser**: Streamlit should automatically open the app in your default browser. If not, navigate to `http://localhost:8501`.

## Usage

1. **Select a Game**: Choose a game from the dropdown in the sidebar.

2. **Input Your Data**:

- Enter your current pity count and total saved currency.
- Adjust the slider to set the number of pulls required for guaranteed pity.

3. **View Results**:

- The app will display the remaining pulls until the next guaranteed reward.
- View the probability of getting a reward on your next pull.
- Track your progress visually with the progress bar.

## Roadmap

### Future Features
- **Pull Simulation**: Simulate a series of pulls to predict outcomes.
- **Historical Tracking**: Record past pulls to analyze probabilities over time.
- **Additional Games**: Add more games with specific pity mechanics.
- **User Authentication**: Allow users to save data across sessions.
- **Enhanced Probability Graphs**: Visualize probability curves for different numbers of pulls.
