import matplotlib.pyplot as plt
import streamlit as st

import platforms as pt
from config import FILTERS, MONTHS, PLATFORMS, PRIMARY_KEY, TOP_N

if __name__ == '__main__':

    # streamlit configuration#
    option_platforms = st.selectbox(
        'Select a platform', PLATFORMS)
    option_months = st.selectbox(
        'Select a month', MONTHS)

    platform = pt.Social(option_platforms)

    # example visualization 1
    optionx_combo = FILTERS
    option = st.selectbox(
        'Find top Influencers in a category', optionx_combo)

    # get top influencers across a sub-category based on subsrcibers
    optionx = st.selectbox('Select Metric: ', platform.metrics)
    filter_product = platform.get_topn_influencers_categorical(
        option, optionx, month=option_months)
    st.write("Top influencers for each " + option + " based on subscribers")
    st.write(filter_product)
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.barh(filter_product[option], filter_product[optionx], align='center')
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel("No. of "+optionx)
    plt.xticks(rotation=90)
    st.pyplot(fig)

    # example visualization 2
    option1 = st.selectbox('Choose category', FILTERS)
    option2 = st.selectbox('Find top Influencers in these subcategories',
                           platform.get_category_items(option1))
    # list of N's for top influencers
    # default value of N to be displayed in selection box
    default_topn = TOP_N.index(3)
    option3 = st.selectbox(
        'Select Number of Influencers to display', TOP_N, index=default_topn)
    option4 = st.selectbox('Select Metric', platform.metrics)

    # get top influencers across a sub-category based on subsrcibers
    subframe = platform.filter_by_month(platform.df, option_months)
    subframe = platform.get_subcategory_items(subframe, option1, option2)
    dfs = platform.find_topn_influencers(subframe, option3)[option4]
    st.write("Top "+str(option3)+" influencers for "+option2 +
             " under " + option1 + " based on " + option4)

    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = range(len(dfs[PRIMARY_KEY]))
    ax.barh(dfs[PRIMARY_KEY], dfs[option4], align='center')
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel("No. of "+option4)
    st.pyplot(fig)
