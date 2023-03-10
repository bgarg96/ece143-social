import matplotlib.pyplot as plt
import streamlit as st

import platforms as pt
from config import FILTERS, MONTHS, PLATFORMS, PRIMARY_KEY, TOP_N

if __name__ == '__main__':

    st.title('Social Media Influencers Analysis for Businesses')

    # streamlit configuration#
    option_platforms = st.selectbox(
        'Select a platform', PLATFORMS)
    option_months = st.selectbox(
        'Select a month', MONTHS)

    platform = pt.Social(option_platforms)

    # example visualization 1
    st.subheader('Top Influencers across all Categories')
    my_expander1 = st.expander(
        label='Show Top Influencers across all Categories')
    with my_expander1:
        optionx_combo = FILTERS
        option = st.selectbox(
            'Find top Influencers in a category', optionx_combo)

        # get top influencers across a sub-category based on subsrcibers
        optionx = st.selectbox('Select Metric: ', platform.metrics)
        filter_product = platform.get_topn_influencers_categorical(
            option, optionx, month=option_months)

        st.write("Top influencers for each " +
                 option + " based on subscribers")
        st.write(filter_product)
        plt.rcdefaults()
        fig, ax = plt.subplots()
        ax.barh(filter_product[option],
                filter_product[optionx], align='center')
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel("No. of "+optionx)
        plt.xticks(rotation=90)
        ax.set_xscale('log')
        st.pyplot(fig)

    # example visualization 2
    st.subheader('Top Influencers in a Category')
    my_expander2 = st.expander(label='Seacrh Top Influencers in a Category')
    with my_expander2:
        option1 = st.selectbox('Choose category', FILTERS)
        option2 = st.selectbox('Find top Influencers in these subcategories',
                               platform.get_category_items(option1))
        # list of N's for top influencers
        # default value of N to be displayed in selection box
        default_topn = TOP_N.index(3)
        option3 = st.selectbox(
            'Select Number of Influencers to display',
            TOP_N,
            index=default_topn)
        option4 = st.selectbox('Select Metric', platform.metrics)

        # get top influencers across a sub-category based on metric
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
        ax.set_xscale('log')
        st.pyplot(fig)

    # example visualization 3 : Get top categories in a particular country
    st.subheader('Top Categories in a Country')
    my_expander3 = st.expander(label="Search for Top Categories in a Country")
    with my_expander3:
        optionC = st.selectbox(
            'Choose a Country', platform.get_category_items(FILTERS[0]))
        # list of N's for top influencers
        # default value of N to be displayed in selection box
        optionsN = [1, 3, 5, 10, "All"]
        default_topn = TOP_N.index(3)
        optionN = st.selectbox(
            'Select top N categories to display', optionsN, index=default_topn)
        optionM = st.selectbox('Select Aggregated Metric', platform.metrics)
        df_cat = platform.get_N_most_popular_cat(platform.filter_by_month(
            platform.df, option_months), optionM, optionN, optionC)

        st.write("Top categories for "+optionC
                 + " based on Aggregated" + optionM)

        plt.rcdefaults()
        fig, ax = plt.subplots()
        ax.barh(df_cat[FILTERS[1]],
                df_cat['Aggregated '+optionM], align='center')
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel("No. of Aggregated "+optionM)
        ax.set_xscale('log')
        st.pyplot(fig)

    # example visualization 4 : Get top countries in a particular category
    st.subheader('Top Countries in a Category')
    my_expander3 = st.expander(label="Search for Top Countries in a Category")
    with my_expander3:
        optionP = st.selectbox('Choose a Category',
                               platform.get_category_items(FILTERS[1]))
        # list of N's for top influencers
        # default value of N to be displayed in selection box
        optionsN2 = [1, 3, 5, 10, "All"]
        default_topn = TOP_N.index(3)
        optionN2 = st.selectbox(
            'Select the top N categories to display',
            optionsN2,
            index=default_topn)
        optionM2 = st.selectbox(
            'Select an Aggregated Metric', platform.metrics)
        df_cat = platform.get_N_most_popular_country(platform.filter_by_month(
            platform.df, option_months), optionM2, optionN2, optionP)

        st.write("Top categories for "+optionP
                 + " based on Aggregated" + optionM2)

        plt.rcdefaults()
        fig, ax = plt.subplots()
        ax.barh(df_cat[FILTERS[0]],
                df_cat['Aggregated '+optionM2], align='center')
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel("No. of Aggregated "+optionM2)
        ax.set_xscale('log')
        st.pyplot(fig)
