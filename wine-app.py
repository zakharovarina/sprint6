import pandas as pd
import streamlit as st
import plotly.express as px


data = pd.read_csv("wines_SPA.csv")


st.title("Choose your wine!")
st.subheader("Use this app to select great Spanish wine based on your preferences ")


import urllib.request
from PIL import Image

urllib.request.urlretrieve(
    "https://www.realsimple.com/thmb/kMZlkYmZYnfoFt2u4sugYfLVXfE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/red-wine-health-benefits-ce3be96b730b41cc82f128abb75c2395.jpg",
    "gfg.png",
)

img = Image.open("gfg.png")

st.image(img)

st.caption(":red[Choose your parameters here]")


price_range = st.slider("What is your price range?", value=(4, 3200))

actual_range = list(range(price_range[0], price_range[1] + 1))

high_rating = st.checkbox("Only high rating")

if high_rating:
    filtered_data = data[data.price.isin(actual_range)]
    filtered_data = filtered_data[data.rating >= 4.5]
else:
    filtered_data = data[data.price.isin(actual_range)]


st.write("Here are your options with a split by price and rating")

fig = px.scatter(filtered_data, x="price", y="rating")
st.plotly_chart(fig)


st.write("Distribution of acidity of filtered wines")
fig2 = px.histogram(filtered_data, x="acidity")
st.plotly_chart(fig2)


st.write("Here is the list of recommended wines")
st.dataframe(filtered_data.sample(40))
