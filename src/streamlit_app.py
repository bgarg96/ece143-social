import platforms as pt
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# streamlit configuration#
PLATFORMS=['Instagram', 'Youtube', 'TikTok']
MONTHS=['Sep','Oct','Nov','Dec']
option_platforms = st.selectbox(
    'Select a platform',PLATFORMS )
option_months=st.selectbox(
    'Select a month', MONTHS )

instagram = pt.Social("../data/"+option_platforms+"/"+option_platforms+"_"+option_months+".csv")
# st.write("Top 10 influencers")
# st.write(instagram.find_topn_influencers(
#     instagram.df, 10)[instagram.metrics[0]])

# st.write("Top 10 influencers in the US")
# st.write(instagram.find_topn_influencers(instagram.get_subcategory_items(
#     instagram.df,
#     'Country',
#     'United States'),
#     10)[instagram.metrics[0]])

# example visualization 1
optionx_combo=instagram.filters
option = st.selectbox(
    'Find top Influencers in a category',optionx_combo )

# get top influencers across a sub-category based on subsrcibers
optionx = st.selectbox('Select Metric: ', instagram.metrics)
filter_product = instagram.get_topn_influencers_categorical(
    option, optionx)
st.write("Top influencers for each "+ option +" based on subscribers")
st.write(filter_product)
plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(filter_product[option], filter_product[optionx], align='center')
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel("No. of "+optionx)
plt.xticks(rotation=90)
st.pyplot(fig)



# example visualization 2
option1 = st.selectbox('Choose category', instagram.filters)
option2 = st.selectbox('Find top Influencers in these subcategories',
                       instagram.get_category_items(option1))
# list of N's for top influencers
topn= [1, 3, 5, 10]
# default value of N to be displayed in selection box
default_topn=topn.index(3)
option3 = st.selectbox(
    'Select Number of Influencers to display',topn,index=default_topn)
option4 = st.selectbox('Select Metric', instagram.metrics)

# get top influencers across a sub-category based on subsrcibers
subframe = instagram.get_subcategory_items(instagram.df, option1, option2)
dfs = instagram.find_topn_influencers(subframe, option3)[option4]
st.write("Top "+str(option3)+" influencers for "+option2 +
         " under " + option1 + " based on " + option4)
# st.write(pd.DataFrame(zip(dfs['AccountName'],dfs[option4]),columns=['Account Name',option4]))

plt.rcdefaults()
fig, ax = plt.subplots()
y_pos=range(len(dfs['AccountName']))
ax.barh(dfs['AccountName'], dfs[option4], align='center')
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel("No. of "+option4)
st.pyplot(fig)