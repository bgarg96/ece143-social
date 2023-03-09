import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
import pandas as pd
import platforms as pt
from config import MONTHS, MONTHS_DTYPE, NAME, PRIMARY_KEY, PLATFORMS, TOP_N, FILTERS, METRICS
import numpy as np
import seaborn as sns

# line chart
def line_chart(df_social_medias_time, requested_media='Instagram'):
    '''
    display line chart of top N influencers per social media platform requested over time based on a METRIC
    param:
    df_medias_time (type: pd.DataFrame) : Dataframe where columns include...
        0. Influencer Name --> string of TOP_N influencer
        1. sep-2022 --> number of METRIC in sep
        2. oct-2022 --> number of METRIC in oct
        3. nov-2022 --> number of METRIC in nov
        4. dec-2022 --> number of METRIC in dec
    if FILTER is specified, df_medias_time will be a subset of the COUNTRY or CATEGORY_1 with the same information
    platform (type: string): platform selected
    month (type: string): month selected
    df_filter (type: string): filter selected, if any. df_filter must be a specific country/category if COUNTRY/CATEGORY_1 is chosen
    metric (type: string): metric selected

    output:
    matplotlib line chart
    '''
    assert isinstance(df_social_medias_time, pd.DataFrame)
    assert isinstance(requested_media, str)
    platform_options = ['Instagram', 'TikTok', 'Youtube']
    if '&' in requested_media:
        and_idx = requested_media.index('&')
        first_media = requested_media[0:and_idx-1]
        second_media = requested_media[and_idx+2:]
        platform_options = [i for i in platform_options if i == first_media or i == second_media]
    elif requested_media != 'All':
        platform_options = requested_media
    palette = plt.get_cmap('Set1')
    fig_count = 0
    figs = {}
    for platform in platform_options:
        df_platform = df_social_medias_time.loc[df_social_medias_time['social media'] == platform]
        num = 0
        figs[fig_count] = plt.figure(fig_count)
        for influencer_name in df_platform['Influencer Name']:
            all_influencer_subs = df_platform.loc[df_platform['Influence Name'] == influencer_name]
            subs_vals = df_platform[list(all_influencer_subs.iloc[:, 2:]).to_numpy()][0]
            months = np.array(df_platform.iloc[:, 2:].keys())
            num+=1
            figs[fig_count] = plt.subplot(5,2,num) # hard-coded 10
            plt.plot(months, subs_vals, marker='o', markersize=12, color=palette(num), linewidth=2.0, alpha=0.9)
            plt.xticks(range(len(subs_vals)), months)
            plt.title(influencer_name + ' Following in 2022', loc='left', fontsize=12, fontweight=0, color=palette(num))
        plt.suptitle(platform + 'Top Influencers Following in 2022')
        plt.text(0.5, 0.02, 'Time', ha='center', va='center')
        plt.text(0.06, 0.5, 'Number of Followers', ha='center', va='center', rotation='vertical')
        fig_count += 1
    return figs

def venn_diagram(df_instagram, df_youtube, months=MONTHS[0],df_filter: str='Country'):
    '''
    display venn diagram comparing and contrasting countries for instagram and youtube
    param:
    df_instagram (type: pd.DataFrame) : non-dated DataFrame of instagram data
    df_youtube (type: pd.DataFrame) : non-dated DataFrame of youtube data
    df_filter (type: str) : filter to compare
    output:
    matplotlib_venn venn diagram
    '''
    assert isinstance(df_instagram, pd.DataFrame)
    assert isinstance(df_youtube, pd.DataFrame)
    instagram_countries = df_instagram[df_filter].unique()
    youtube_countries = df_youtube[df_filter].unique()

    # get rid of nan values
    for i in range(len(instagram_countries)):
      if pd.isnull(instagram_countries[i]) == True:
         instagram_countries_new = np.delete(instagram_countries,i)
    if 'instagram_countries_new' in locals(): instagram_countries = instagram_countries_new
    for i in range(len(youtube_countries)):
      if pd.isnull(youtube_countries[i]) == True:
         youtube_countries_new = np.delete(youtube_countries,i)
    if 'youtube_countries_new' in locals(): youtube_countries = youtube_countries_new

    # determine common countries for middle of venn
    common_countries = np.intersect1d(instagram_countries, youtube_countries)
    insta_unique = len(instagram_countries) - len(common_countries)
    assert insta_unique >= 0
    youtube_unique = len(youtube_countries) - len(common_countries)
    assert youtube_unique >= 0
    figs = plt.figure()
    venn2(subsets=(insta_unique, youtube_unique, len(common_countries)), set_labels=('Instagram', 'Youtube'), set_colors=('b', 'r'), alpha = 0.5)
    venn2_circles(subsets=(insta_unique, youtube_unique, len(common_countries))) # remove if not wanted
    plt.title('Instagram vs Youtube Number of different ' + df_filter+ "'s in "+ months + ' 2022')
    return figs




def bar_InfluencersvFollowers(df_top_instagram, df_top_youtube, df_top_tiktok, requested_media='Instagram'):
    '''
    display bar graph of top influencers and number of followers/subscribers for given social media platform
    param:
    df_top_instagram (type: pd.DataFrame) : non-dated DataFrame of top influencers on instagram data
    df_youtube (type: pd.DataFrame) : non-dated DataFrame of top influencers on youtube data
    df_tiktok (type: pd.DataFrame) : non-dated DataFrame of top influencers on tiktok data
    requested_media (type: string): which social media platform's information to display

    output:
    matplotlib bar chart
    '''
    assert isinstance(df_top_instagram, pd.DataFrame)
    assert isinstance(df_top_youtube, pd.DataFrame)
    assert isinstance(df_top_tiktok, pd.DataFrame)
    assert isinstance(requested_media, str)
    platform_options = ['Instagram', 'TikTok', 'Youtube']
    all_dfs = [df_top_instagram, df_top_tiktok, df_top_youtube]
    if '&' in requested_media:
        and_idx = requested_media.index('&')
        first_media = requested_media[0:and_idx-1]
        second_media = requested_media[and_idx+2:]
        all_dfs = [all_dfs[platform_options.index(i)] for i in platform_options if i == first_media or i == second_media]
        platform_options = [i for i in platform_options if i == first_media or i == second_media]
    elif requested_media != 'All':
        all_dfs = [all_dfs[platform_options.index(requested_media)]]
        platform_options = [requested_media]
    fig_count = 0
    figs = {}
    for platform in platform_options:
        figs[fig_count] = plt.figure(fig_count)
        df_platform = all_dfs[fig_count][['Influencer name', 'Subscribers']].sort_values(by='Subscribers', ascending=False)
        influencer_names = df_platform['Influencer name'].values
        subscribers = df_platform['Subscribers'].values
        plt.bar(influencer_names, subscribers)
        plt.title('Total Followers/Subscribers for Top Influencers on ' + platform + ' in 2022', loc='center', fontsize=12)
        plt.xlabel('Top ' + platform + ' Influencers')
        fig_count += 1
    return figs

def bar_CountryvInfluencers(df_instagram, df_youtube, requested_media='Instagram'):
    '''
    display bar graph of number of influencers in each country for given social media platform
    param:
    df_instagram (type: pd.DataFrame) : non-dated DataFrame of influencers on instagram data
    df_youtube (type: pd.DataFrame) : non-dated DataFrame of influencers on youtube data
    requested_media (type: string): which social media platform's information to display

    output:
    matplotlib bar chart
    '''
    assert isinstance(df_instagram, pd.DataFrame)
    assert isinstance(df_youtube, pd.DataFrame)
    assert isinstance(requested_media, str)
    platform_options = ['Instagram', 'Youtube']
    all_dfs = [df_instagram, df_youtube]
    if requested_media == 'All':
        new_df = pd.DataFrame()
        num = 0
        for platform in platform_options:
            ref_df = pd.DataFrame()
            df_platform = all_dfs[num][['Influencer name', 'Audience country']]
            country_count = df_platform['Audience country'].value_counts()
            country_names = country_count.index
            num_influencers = country_count.values
            ref_df['Number of Influencers'] = num_influencers
            ref_df['Country'] = country_names
            ref_df['Social Media'] = [platform]*len(country_names)
            new_df = pd.concat([new_df, ref_df])
            num += 1
        figs = plt.figure()
        new_df.pivot(index='Social Media', columns='Country', values='Number of Influencers').plot.bar(rot=0, stacked=True)
        plt.title('Number of Influencers in a Demographic on ' + platform_options[0] + ' and ' + platform_options[1])
    else:
        all_dfs = all_dfs[platform_options.index(requested_media)]
        df_platform = all_dfs[['Influencer name', 'Audience country']]
        country_count = df_platform['Audience country'].value_counts()
        country_names = country_count.index
        num_influencers = country_count.values
        figs = plt.figure()
        plt.bar(country_names, num_influencers)
        plt.title('Number of Influencers in Each Demographic on ' + platform + ' in 2022', loc='center', fontsize=12)
        plt.xlabel('Audience Country')
        plt.ylabel('Number of Influencers')
    return figs

def bar_CategoryvViews(df_instagram, df_youtube, requested_media='Instagram'):
    '''
    display bar graph of number of views in each category for given social media platform
    param:
    df_instagram (type: pd.DataFrame) : non-dated DataFrame of influencers on instagram data
    df_youtube (type: pd.DataFrame) : non-dated DataFrame of influencers on youtube data
    requested_media (type: string): which social media platform's information to display

    output:
    matplotlib bar chart
    '''
    assert isinstance(df_instagram, pd.DataFrame)
    assert isinstance(df_youtube, pd.DataFrame)
    assert isinstance(requested_media, str)
    platform_options = ['Instagram', 'Youtube']
    all_dfs = [df_instagram, df_youtube]
    if requested_media == 'All':
        new_df = pd.DataFrame()
        num = 0
        for platform in platform_options:
            ref_df = pd.DataFrame()
            df_platform = all_dfs[num][['Category', 'avg views']]
            sum_views = df_platform.groupby('Category')['avg views'].sum()
            num_views = sum_views.values
            category_names = sum_views.index
            ref_df['Views'] = num_views
            ref_df['Category'] = category_names
            ref_df['Social Media'] = [platform]*len(category_names)
            new_df = pd.concat([new_df, ref_df])
            num += 1
        figs = plt.figure()
        new_df.pivot(index='Social Media', columns='Category', values='Views').plot.bar(rot=0, stacked=True)
        plt.title('Number of Avg Views in a Product Category on ' + platform_options[0] + ' and ' + platform_options[1])
    else:
        all_dfs = all_dfs[platform_options.index(requested_media)]
        df_platform = all_dfs[['Category', 'avg views']]
        sum_views = df_platform.groupby('Category')['avg views'].sum()
        num_views = sum_views.values
        category_names = sum_views.index
        figs = plt.figure()
        plt.bar(category_names, num_views)
        plt.title('Total Number of Views in Each Category on ' + requested_media + ' in 2022', loc='center', fontsize=12)
        plt.xlabel('Category')
        plt.ylabel('Views')
    return figs

def bar_CategoryvInfluencers(df_instagram, df_youtube, requested_media='Instagram'):
    '''
    display bar graph of number of influencers in each category for given social media platform
    param:
    df_instagram (type: pd.DataFrame) : non-dated DataFrame of influencers on instagram data
    df_youtube (type: pd.DataFrame) : non-dated DataFrame of influencers on youtube data
    requested_media (type: string): which social media platform's information to display

    output:
    matplotlib bar chart
    '''
    assert isinstance(df_instagram, pd.DataFrame)
    assert isinstance(df_youtube, pd.DataFrame)
    assert isinstance(requested_media, str)
    platform_options = ['Instagram', 'Youtube']
    all_dfs = [df_instagram, df_youtube]
    if requested_media == 'All':
        new_df = pd.DataFrame()
        num = 0
        for platform in platform_options:
            ref_df = pd.DataFrame()
            df_platform = all_dfs[num][['Influencer name', 'Category']]
            category_count = df_platform['Category'].value_counts()
            num_influencers = category_count.values
            category_names = category_count.index
            ref_df['Number of Influencers'] = num_influencers
            ref_df['Category'] = category_names
            ref_df['Social Media'] = [platform]*len(category_names)
            new_df = pd.concat([new_df, ref_df])
            num += 1
        figs = plt.figure()
        new_df.pivot(index='Social Media', columns='Category', values='Number of Influencers').plot.bar(rot=0, stacked=True)
        plt.title('Number of Influencers in a Product Category on ' + platform_options[0] + ' and ' + platform_options[1])
    else:
        all_dfs = all_dfs[platform_options.index(requested_media)]
        df_platform = all_dfs[['Influencer name', 'Category']]
        category_count = df_platform['Category'].value_counts()
        num_influencers = category_count.values
        category_names = category_count.index
        figs = plt.figure()
        plt.bar(category_names, num_influencers)
        plt.title('Total Number of Influencers in Each Category on ' + requested_media + ' in 2022', loc='center', fontsize=12)
        plt.xlabel('Category')
        plt.ylabel('Number of Influencers')
    return figs

def heatmap(df_media: pd.DataFrame, platform: str=PLATFORMS[0], month: str=MONTHS[0]) -> plt.figure():
    '''
    display heat map of the number of subscribers and top influencer for each category in each country for given social media platform
    param:
    df_media (type: pd.DataFrame) : UNFILTERED DataFrame of selected PLATFORM and MONTH
    platform (type: string): platform selected
    month (type: string): month selected

    output:
    seaborn heat map
    '''

    # TODO: Test the code
    # TODO: Allow DataFrame input to not be filtered by a certain metric
    # TODO: Produce 4 plots for all months, if requested
    # TODO: Produce 2 plots for all platforms, if requested

    fig_count = 0
    figs = plt.figure(fig_count)
    df_platform = df_media[[PRIMARY_KEY, 'Category_1', 'Country', 'Subscribers']]
    all_categories = df_platform['Category_1'].unique()
    all_countries = df_platform['Country'].unique()
    new_df = pd.DataFrame(columns=all_countries, index=all_categories)
    labels = [[0 for _ in range(len(all_countries))] for _ in range(len(all_categories))]
    col = 0
    figs = plt.figure(fig_count)
    for country in all_countries:
        df_vals = []
        row = 0
        for category in all_categories:
            df_filtered_country = df_platform.loc[df_platform['Country'] == country]
            df_filtered_category = df_filtered_country.loc[df_filtered_country['Category_1'] == category]
            if len(df_filtered_category) == 0:
                df_vals.append(0)
                labels[row][col] = 'N/A'
                row += 1
                continue
            highest_following = df_filtered_category.loc[df_filtered_category['Subscribers'].idxmax()]
            df_vals.append(highest_following['Subscribers'])
            labels[row][col] = highest_following[PRIMARY_KEY]
            row += 1
        new_df[country] = df_vals
        col += 1
    sns.heatmap(new_df, annot=labels, fmt='')
    plt.title('Number of Subscribers for Top Influencers in a Category and Country on ' + platform + ' in ' + month + ' 2022')
    return figs

def pie_chart(df_media: pd.DataFrame, platform: str=PLATFORMS[0], month: str=MONTHS[0], df_filter: str='Country', metric: str='', category='') -> plt.figure():
    '''
    if filter == 'Country':
        display pie chart of the percent of influencers that fall in each categories for a given country and social media platform
    if filter == 'Category_1':
        display a SINGLE pie chart of the percent each influencer contributes to a METRIC for a given category and social media platform
    param:
    df_media (type: pd.DataFrame) : UNFILTERED DataFrame of influencers of selected PLATFORM and MONTH
    platform (type: string): platform selected
    month (type: string): month selected
    df_filter (type: string): independent variable for pie chart
    metric (type: string): a single country if filter == 'Country', any METRICS value if filter == 'Category_1' (including 'AccountName')
    category (type: string): a single category if filter == 'Category' from the dataframe

    output:
    matplotlib pie chart
    '''

    # TODO: Test the code
    # TODO: Allow DataFrame input to not be filtered by a certain metric
    # TODO: Allow user to select a specific country based on DataFrame and pass that into metric field
    # TODO: Allow user to select a specific category based on DataFrame and pass that into category field
    # TODO: Produce 4 plots for all months, if requested
    # TODO: Produce 2 plots for all platforms, if requested

    figs = plt.figure()
    if df_filter == 'Country':
        df_platform = df_media[['Category_1', df_filter]]
        #all_countries = df_platform[df_filter].unique()
        #plots = len(all_countries)
        #row_plots = int(plots**0.5)
        #col_plots = plots // row_plots
        #col_plots += plots % col_plots
        #num = 1
        df_filtered_country = df_platform.loc[df_platform[df_filter] == metric]
        count_categories = df_filtered_country.groupby('Category_1')[df_filter].count()
        #if len(count_categories) == 0:
        #    continue
        category_divisions = count_categories.values
        category_labels = count_categories.index
        if len(category_labels) > 6:
            sorted_idx = [b[0] for b in sorted(enumerate(category_divisions),key=lambda i:i[1])]
            sorted_labels = []
            for i in sorted_idx:
                sorted_labels.append(category_labels[i])
            category_labels = sorted_labels[-6:]
            category_labels.insert(0, 'Other')
            sort_category_divisions = sorted(category_divisions)
            highest_divisions = sort_category_divisions[-6:]
            other_vals = sum(sort_category_divisions[:-6])
            highest_divisions.insert(0, other_vals)
            category_divisions = highest_divisions
        explode = np.zeros(len(category_labels))
        max_val = max(category_divisions)
        max_idx = np.where(category_divisions == max_val)
        explode[max_idx] = 0.1
        #plt.subplot(row_plots,col_plots,num)
        plt.pie(category_divisions, labels=category_labels, explode=explode)
        plt.title(metric)
        # num += 1
        plt.suptitle('Demographic Division of Product Category by Number of Influencers on ' + platform + ' in ' + month + ' 2022')
    else:
        assert metric in METRICS
        df_platform = df_media[[PRIMARY_KEY, df_filter, metric]]
        # all_categories = df_platform[df_filter].unique()
        # plots = len(all_categories)
        #row_plots = int(plots**0.5)
        #col_plots = plots // row_plots
        #col_plots += plots % col_plots
        #num = 1
        df_filtered_category = df_platform.loc[df_platform[df_filter] == category]
        group = df_filtered_category.groupby(PRIMARY_KEY)
        metric_df = group.apply(lambda x: x[metric].unique())
            # if len(count_metric) == 0:
            #    continue
        metric_divisions = metric_df.values
        metric_labels = metric_df.index
        assert len(metric_labels) == len(metric_divisions)
        explode = np.zeros(len(metric_divisions))
        max_val = max(metric_divisions)
        max_idx = np.where(metric_divisions == max_val)
        explode[max_idx] = 0.1
        #plt.subplot(row_plots,col_plots,num)
        plt.pie(metric_divisions, labels=metric_labels, explode=explode)
        plt.title(category)
        num += 1
        plt.suptitle('Product Category Division of Influencers by ' + metric + ' on ' + platform + ' in ' + month + ' 2022')
    return figs

instagram = pd.read_csv('/Users/nicky/Documents/Github/ece143-social/data/Instagram/Instagram_Dec.csv')
youtube = pd.read_csv('/Users/nicky/Documents/Github/ece143-social/data/Youtube/Youtube_Dec.csv')
# pie_chart(instagram, PLATFORMS[0], 'Dec', 'Country', 'United States').show()
venn_diagram(instagram, youtube, 'Dec','Country').show()
