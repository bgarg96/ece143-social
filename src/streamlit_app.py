import platforms as pt
import streamlit as st

instagram= pt.Social("./data/Instagram/social media influencers - instagram sep-2022.csv")
st.write("Top 10 influencers")
st.write(instagram.find_topn_influencers(instagram.df,10)[instagram.metrics[0]])

st.write("Top 10 influencers in the US")
st.write(instagram.find_topn_influencers(instagram.get_subcategory_items(instagram.df,'Audience country', 'United States'),10)[instagram.metrics[0]])