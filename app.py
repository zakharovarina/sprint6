import pandas as pd
import streamlit as st
import plotly.express as px


data = pd.read_csv("vehicles_us.csv")


st.title("Choose your car!")
st.subheader("Use this app to select a car based on your preferences ")


import urllib.request
from PIL import Image

urllib.request.urlretrieve(
    "https://images.bauerhosting.com/legacy/empire-tmdb/films/920/images/a1MlbLBk5Sy6YvMbSuKfwGlDVlb.jpg?ar=16%3A9&fit=crop&crop=top&auto=format&w=1440&q=80",
    "gfg.png",
)

img = Image.open("gfg.png")

st.image(img)

st.caption(":red[Choose your parameters here]")


price_range = st.slider("What is your price range?", value=(1, 375000))

actual_range = list(range(price_range[0], price_range[1] + 1))

excellent = st.checkbox("Only excellent condition")

if excellent:
    filtered_data = data[data.price.isin(actual_range)]
    filtered_data = filtered_data[filtered_data["condition"] == "excellent"]
else:
    filtered_data = data[data.price.isin(actual_range)]


st.write("Here are your options with a split by price and model year")

fig = px.scatter(filtered_data, x="price", y="model_year")
st.plotly_chart(fig)


st.write("Distribution of acidity of filtered wines")
fig2 = px.histogram(filtered_data, x="odometer")
st.plotly_chart(fig2)


st.write("Here is the list of recommended cars")
st.dataframe(filtered_data.sample(40))
