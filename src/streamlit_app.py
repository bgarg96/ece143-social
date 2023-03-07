import platforms as pt
import streamlit as st

'''
This file contains the front end code for
visualization on a webpage using Streamlit
'''

# streamlit configuration#


instagram = pt.Social(
    "./data/Instagram/social media influencers - instagram sep-2022.csv")
st.write("Top 10 influencers")
st.write(instagram.find_topn_influencers(
    instagram.df, 10)[instagram.metrics[0]])

st.write("Top 10 influencers in the US")
st.write(instagram.find_topn_influencers(instagram.get_subcategory_items(
    instagram.df,
    'Audience country',
    'United States'),
    10)[instagram.metrics[0]])


option = st.selectbox(
    'Find top Influencers in a category', instagram.categories)

# get top influencers across a sub-category based on subsrcibers
filter_product = instagram.get_topn_influencers_categorical(
    option, instagram.metrics[0])
st.write("Top influencers for each product based on subscribers")
st.write(filter_product)

option1 = st.selectbox('Choose category', instagram.categories)
option2 = st.selectbox('Find top Influencers in these subcategories',
                       instagram.get_category_items(option1))
option3 = st.selectbox(
    'Select Number of Influencers to display', (1, 3, 5, 10))
option4 = st.selectbox('Select Metric', instagram.metrics)

# get top influencers across a sub-category based on subsrcibers
subframe = instagram.get_subcategory_items(instagram.df, option1, option2)
dfs = instagram.find_topn_influencers(subframe, option3)[option4]
st.write("Top "+str(option3)+" influencers for "+option2 +
         " under " + option1 + " based on " + option4)
st.write(dfs)
