import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame({
    "first column": [1,2,3,4],
    "second column": [10, 20, 30, 40]
})

st.title("My First App")

st.write("First attempt using data on Streamlit!")
st.write(pd.DataFrame({
    "first column": [1,2,3,4],
    "second column": [10, 20, 30, 40]
}))

# Draw a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ["a", "b", "c"]
)
st.line_chart(chart_data)

# Plot a map
map_data = pd.DataFrame(
    np.random.randn(1000, 2)/[50, 50] + [37.76, -122.4],
    columns = ["lat", "lon"]
)
st.map(map_data)

####### Add Interactivity ###########

# Checkbox to show/hide data
if st.checkbox("Show Dataframe"):
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ["a", "b", "c"]
    )
    st.line_chart(chart_data)

# Selectbox for options
option = st.selectbox(
    "Which number do you like best?",
    df["first column"])
"You selected: ", option

left_column, right_column = st.beta_columns(2)
pressed = left_column.button("Press me?")
if pressed:
    right_column.write("Wohooo!")

expander = st.beta_expander("FAQ")
expander.write("Long explanations here!")

######## Show Progress ###########
"Starting a long computation"

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update progress bar with each iteration
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"... and now we're done! Yay!"
