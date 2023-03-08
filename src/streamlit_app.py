import matplotlib.pyplot as plt
import streamlit as st

import platforms as pt
from config import FILTERS, PRIMARY_KEY, TOP_N

# streamlit configuration#

if __name__ == '__main__':

    instagram = pt.Social("Instagram")
    # st.write("Top 10 influencers")
    # st.write(instagram.find_topn_influencers(
    #     instagram.df, 10)[instagram.metrics[0]])

    # st.write("Top 10 influencers in the US")
    # st.write(instagram.find_topn_influencers(instagram.get_subcategory_items(
    #     instagram.df,
    #     'Country',
    #     'United States'),
    #     10)[instagram.metrics[0]])

    option = st.selectbox(
        'Find top Influencers in a category', FILTERS)

    # get top influencers across a sub-category based on subsrcibers
    filter_product = instagram.get_topn_influencers_categorical(
        option, list(instagram.metrics)[0])
    st.write("Top influencers for each product based on subscribers")
    st.write(filter_product)

    option1 = st.selectbox('Choose category', FILTERS)
    option2 = st.selectbox('Find top Influencers in these subcategories',
                           instagram.get_category_items(option1))

    # list of N's for top influencers

    # default value of N to be displayed in selection box
    default_topn = TOP_N.index(3)
    option3 = st.selectbox(
        'Select Number of Influencers to display', TOP_N, index=default_topn)
    option4 = st.selectbox('Select Metric', instagram.metrics)

    # get top influencers across a sub-category based on subsrcibers
    subframe = instagram.get_subcategory_items(instagram.df, option1, option2)
    dfs = instagram.find_topn_influencers(subframe, option3)[option4]
    st.write("Top "+str(option3)+" influencers for "+option2 +
             " under " + option1 + " based on " + option4)

    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = range(len(dfs[PRIMARY_KEY]))
    ax.barh(dfs[PRIMARY_KEY], dfs[option4], align='center')
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel("No. of "+option4)
    st.pyplot(fig)