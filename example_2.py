import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_autorefresh import st_autorefresh

# Autorefresh every 10 seconds (10000 milliseconds)
count = st_autorefresh(interval=1000, limit=100, key="fizzbuzzcounter")

# Function to generate new data
def get_new_data():
    data = np.random.randn(10, 2)
    df = pd.DataFrame(data, columns=['x', 'y'])
    return df

# Title of the app
st.title("Auto-updating Graph Example")

# Get new data
df = get_new_data()

# Create the plot
fig, ax = plt.subplots()
ax.plot(df['x'], df['y'], 'o-')

# Display the plot
st.pyplot(fig)