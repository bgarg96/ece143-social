import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
import pandas as pd
import platforms as pt
import numpy as np
import seaborn as sns

# line chart
def line_chart(df_social_medias_time, requested_media='Instagram'):
    '''
    display line chart of top influencers per social media requested over time
    param: 
    df_social_medias_time (type: pd.DataFrame) : Dataframe where columns include... 
        0. Influencer Name --> string of top influencer
        1. social media --> string of corresponding social media platform for top influencer
        2. june-2022 --> number of subscribers/followers in june 
        3. sep-2022 --> number of subscribers/followers in sep 
        4. nov-2022 --> number of subscribers/followers in nov 
        5. dec-2022 --> number of subscribers/followers in dec 
    
    requested_media (type: string): which social media platform's information to display

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
    plt.style.use('seaborn-darkgrid')
    palette = plt.get_cmap('Set1')
    fig_count = 0
    for platform in platform_options:
        df_platform = df_social_medias_time.loc[df_social_medias_time['social media'] == platform]
        num = 0
        plt.figure(fig_count)
        for influencer_name in df_platform['Influencer Name']:
            all_influencer_subs = df_platform.loc[df_platform['Influence Name'] == influencer_name]
            subs_vals = df_platform[list(all_influencer_subs.iloc[:, 2:]).to_numpy()][0]
            months = np.array(df_platform.iloc[:, 2:].keys())
            num+=1
            plt.subplot(5,2,num)
            plt.plot(months, subs_vals, marker='o', markersize=12, color=palette(num), linewidth=2.0, alpha=0.9, label=col)
            plt.xticks(range(len(subs_vals)), months)
            plt.title(influencer_name + ' Following in 2022', loc='left', fontsize=12, fontweight=0, color=palette(num))
        plt.suptitle(platform + 'Top Influencers Following in 2022')
        plt.text(0.5, 0.02, 'Time', ha='center', va='center')
        plt.text(0.06, 0.5, 'Number of Followers', ha='center', va='center', rotation='vertical')
        plt.show()
        fig_count += 1

def venn_diagram(df_instagram, df_youtube):
    '''
    display venn diagram comparing and contrasting countries for instagram and youtube
    param: 
    df_instagram (type: pd.DataFrame) : non-dated DataFrame of instagram data
    df_youtube (type: pd.DataFrame) : non-dated DataFrame of youtube data

    output:
    matplotlib_venn venn diagram
    '''
    assert isinstance(df_instagram, pd.DataFrame)
    assert isinstance(df_youtube, pd.DataFrame)
    instagram_countries = df_instagram['Audience Country'].unique()
    youtube_countries = df_youtube['Audience Country'].unique()
    common_countries = np.intersect1d(instagram_countries, youtube_countries)
    insta_unique = len(instagram_countries) - len(common_countries)
    assert insta_unique >= 0
    youtube_unique = len(youtube_countries) - len(common_countries)
    assert youtube_countries >= 0
    venn2(subsets=(insta_unique, youtube_unique, len(common_countries)), set_labels=('Instagram', 'Youtube'), set_colors=('g', 'r'), alpha = 0.5)
    plt.title('Instagram vs Youtube Audience Country')
    venn2_circles(subsets=(insta_unique, youtube_unique, len(common_countries)), set_labels=('Instagram', 'Youtube'), set_colors=('g', 'r'), alpha = 0.5) # remove if not wanted
    plt.show()

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
        platform_options = requested_media
    fig_count = 0
    for platform in platform_options:
        plt.figure(fig_count)
        df_platform = all_dfs[fig_count][['Influencer name', 'Subscribers']].sort_values(by='Subscribers')
        influencer_names = df_platform['Influencer name']
        subscribers = df_platform['Subscribers']
        plt.bar(influencer_names, subscribers)
        plt.title('Total Followers/Subscribers for Top Influencers on ' + platform + ' in 2022', loc='center', fontsize=12)
        plt.xlabel('Top ' + platform + ' Influencers')
        plt.ylabel('Total Followers/Subscribers')
        plt.show()
        fig_count += 1

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
    if requested_media == 'All':
        new_df = pd.DataFrame()
        all_dfs = [df_instagram, df_youtube]
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
        new_df.pivot(index='Social Media', columns='Country', values='Number of Influencers').plot.bar(rot=0, stacked=True)
        # add title
        return
    elif requested_media == 'Youtube':
        all_dfs = df_youtube
    else:
        all_dfs = df_instagram
    df_platform = all_dfs[['Influencer name', 'Audience country']]
    country_count = df_platform['Audience country'].value_counts()
    country_names = country_count.index
    num_influencers = country_count.values
    plt.bar(country_names, num_influencers)
    plt.title('Number of Influencers in Each Audience Country on ' + platform + ' in 2022', loc='center', fontsize=12)
    plt.xlabel('Audience Country')
    plt.ylabel('Number of Influencers')
    plt.show()

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
    if requested_media != 'All':
        new_df = pd.DataFrame()
        all_dfs = [df_instagram, df_youtube]
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
        new_df.pivot(index='Social Media', columns='Category', values='Views').plot.bar(rot=0, stacked=True)
        # add title
        return
    elif requested_media == 'Youtube':
        all_dfs = df_youtube
    else:
        all_dfs = df_instagram
    df_platform = all_dfs[['Category', 'avg views']]
    sum_views = df_platform.groupby('Category')['avg views'].sum()
    num_views = sum_views.values
    category_names = sum_views.index
    plt.bar(category_names, num_views)
    plt.title('Total Number of Views in Each Category on ' + platform + ' in 2022', loc='center', fontsize=12)
    plt.xlabel('Category')
    plt.ylabel('Views')
    plt.show()

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
    if requested_media == 'All':
        new_df = pd.DataFrame()
        all_dfs = [df_instagram, df_youtube]
        num = 0
        for platform in platform_options:
            ref_df = pd.DataFrame()
            df_platform = all_dfs[num][['Influencer name', 'Category']]
            category_count = df_platform['Category'].value_counts()
            num_influencers = category_count.value
            category_names = category_count.index
            ref_df['Number of Influencers'] = num_influencers
            ref_df['Category'] = category_names
            ref_df['Social Media'] = [platform]*len(category_names)
            new_df = pd.concat([new_df, ref_df])
            num += 1
        new_df.pivot(index='Social Media', columns='Category', values='Number of Influencers').plot.bar(rot=0, stacked=True)
        # add title
        return
    elif requested_media == 'Youtube':
        all_dfs = df_youtube
    else:
        all_dfs = df_instagram
    df_platform = all_dfs[['Influencer name', 'Category']]
    category_count = df_platform['Category'].value_counts()
    num_influencers = category_count.value
    category_names = category_count.index
    plt.bar(category_names, num_influencers)
    plt.title('Total Number of Influencers in Each Category on ' + platform + ' in 2022', loc='center', fontsize=12)
    plt.xlabel('Category')
    plt.ylabel('Number of Influencers')
    plt.show()

def heatmap(df_instagram, df_youtube, requested_media='Instagram'):
    '''
    display heat map of the number of subscribers and top influencer for each category in each country for given social media platform
    param: 
    df_instagram (type: pd.DataFrame) : non-dated DataFrame of influencers on instagram data
    df_youtube (type: pd.DataFrame) : non-dated DataFrame of influencers on youtube data
    requested_media (type: string): which social media platform's information to display

    output:
    seaborn heat map
    '''
    assert isinstance(df_instagram, pd.DataFrame)
    assert isinstance(df_youtube, pd.DataFrame)
    assert isinstance(requested_media, str)
    platform_options = ['Instagram', 'Youtube']
    if requested_media == 'All':
        all_dfs = [df_instagram, df_youtube]
        fig_count = 0
        plt.figure(fig_count)
        for platform in platform_options:
            df_platform = all_dfs[fig_count][['Influencer name', 'Category', 'Audience country', 'Subscribers']]
            all_categories = df_platform['Category'].unique()
            all_countries = df_platform['Audience country'].unique()
            new_df = pd.DataFrame(columns=all_countries, index=all_categories)
            labels = np.empty([len(all_categories), len(all_countries)])
            labels[:] = np.nan
            col = 0
            for country in all_countries:
                df_vals = []
                row = 0
                for category in all_categories:
                    df_filtered_country = df_platform.loc[df_platform['Audience country'] == country]
                    df_filtered_category = df_filtered_country.loc[df_filtered_country['Category'] == category]
                    highest_following = df_filtered_category.loc[df_filtered_category['Followers'].idxmax()]
                    df_vals.append(highest_following['Followers'])
                    labels[row, col] = highest_following['Influencer name']
                    row += 1
                new_df[country] = df_vals
                col += 1
            sns.heatmap(new_df, annot=labels, fmt='')
            plt.title('Number of Subscribers/Followers for Top Influencers in a Category and Country on ' + platform)
            plt.show()
            fig_count += 1
            plt.figure(fig_count)
        return
    elif requested_media == 'Youtube':
        all_dfs = df_youtube
    else:
        all_dfs = df_instagram
    df_platform = all_dfs[['Influencer name', 'Category', 'Audience country', 'Subscribers']]
    all_categories = df_platform['Category'].unique()
    all_countries = df_platform['Audience country'].unique()
    new_df = pd.DataFrame(columns=all_countries, index=all_categories)
    labels = np.empty([len(all_categories), len(all_countries)])
    labels[:] = np.nan
    col = 0
    for country in all_countries:
        df_vals = []
        row = 0
        for category in all_categories:
            df_filtered_country = df_platform.loc[df_platform['Audience country'] == country]
            df_filtered_category = df_filtered_country.loc[df_filtered_country['Category'] == category]
            highest_following = df_filtered_category.loc[df_filtered_category['Followers'].idxmax()]
            df_vals.append(highest_following['Followers'])
            labels[row, col] = highest_following['Influencer name']
            row += 1
        new_df[country] = df_vals
        col += 1
    sns.heatmap(new_df, annot=labels, fmt='')
    plt.title('Number of Subscribers/Followers for Top Influencers in a Category and Country on ' + requested_media)
    plt.show()

def pie_chart(df_instagram, df_youtube, requested_media='Instagram'):
    '''
    display pie chart of the percent of influencers that fall in each categories in each country for given social media platform
    param: 
    df_instagram (type: pd.DataFrame) : non-dated DataFrame of influencers on instagram data
    df_youtube (type: pd.DataFrame) : non-dated DataFrame of influencers on youtube data
    requested_media (type: string): which social media platform's information to display

    output:
    matplotlib pie chart
    '''
    assert isinstance(df_instagram, pd.DataFrame)
    assert isinstance(df_youtube, pd.DataFrame)
    assert isinstance(requested_media, str)
    platform_options = ['Instagram', 'Youtube']
    fig_count = 0
    if requested_media == 'All':
        all_dfs = [df_instagram, df_youtube]
        fig_count = 0
        plt.figure(fig_count)
        for platform in platform_options:
            plt.figure(fig_count)
            df_platform = all_dfs[fig_count][['Influencer name', 'Category','Audience country']]
            all_countries = df_platform['Audience country'].unique()
            plots = len(all_countries)
            row_plots = int(plots/2)
            col_plots = int(plots - row_plots)
            num = 0
            for country in all_countries:
                df_filtered_country = df_platform.loc[df_platform['Audience country'] == country]
                count_categories = df_filtered_country.groupby('Category')['Audience country'].count()
                category_divisions = count_categories.values
                category_labels = count_categories.index
                explode = np.zeros(len(category_labels))
                max_val = max(category_divisions)
                max_idx = np.where(category_divisions == max_val)
                explode[max_idx] = max_val
                plt.subplot(row_plots,col_plots,num)
                plt.pie(category_divisions, labels=category_labels, explode=explode)
                plt.title(country)
                num += 1
            plt.suptitle('Demographic Division of Product Category by Number of Influencers on ' + platform)
            plt.show()
            fig_count += 1
        return
    elif requested_media == 'Youtube':
        all_dfs = df_youtube
    else:
        all_dfs = df_instagram
    df_platform = all_dfs[['Influencer name', 'Category','Audience country']]
    all_countries = df_platform['Audience country'].unique()
    plots = len(all_countries)
    row_plots = int(plots/2)
    col_plots = int(plots - row_plots)
    for country in all_countries:
        df_filtered_country = df_platform.loc[df_platform['Audience country'] == country]
        count_categories = df_filtered_country.groupby('Category')['Audience country'].count()
        category_divisions = count_categories.values
        category_labels = count_categories.index
        explode = np.zeros(len(category_labels))
        max_val = max(category_divisions)
        max_idx = np.where(category_divisions == max_val)
        explode[max_idx] = max_val
        plt.subplot(row_plots,col_plots,fig_count)
        plt.pie(category_divisions, labels=category_labels, explode=explode)
        plt.title(country)
        fig_count += 1
    plt.suptitle('Demographic Division of Product Category by Number of Influencers on ' + requested_media)    
    plt.show()