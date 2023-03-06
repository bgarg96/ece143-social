import platforms as pt
import streamlit as st
import pandas as pd

instagram= pt.Social("./data/Instagram/social media influencers - instagram sep-2022.csv")
st.write("Top 10 influencers")
st.write(instagram.find_topn_influencers(instagram.df,10)[instagram.metrics[0]])

st.write("Top 10 influencers in the US")
st.write(instagram.find_topn_influencers(instagram.get_subcategory_items(instagram.df,'Audience country', 'United States'),10)[instagram.metrics[0]])


option = st.selectbox('Find top Influencers in a category', instagram.categories)

#get top influencers across a sub-category based on subsrcibers
filter_product=instagram.get_topn_influencers_categorical(option,instagram.metrics[0])
st.write("Top influencers for each product based on subscribers")
st.write(filter_product)