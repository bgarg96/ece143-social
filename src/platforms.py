from collections import Counter
from pathlib import Path
from typing import Set

import numpy as np
import pandas as pd

from config import MONTHS, MONTHS_DTYPE, NAME, METRICS, PRIMARY_KEY
from uts import weighted_average


class Social:

    def __init__(self, platform: str):
        '''
        initialize instance of platform
        '''
        # list of filter categories
        self.metrics: Set[str] = set()
        # TODO(PRASAD): approve these calls
        self.df = self.load_dfs(platform)
        self.poularity = weighted_average(self.df, 'Subscribers')

    def get_categories(self):
        '''
        Returns the categories in a dataframe
        '''
        return list(self.df.columns)

    def preprocess_frame(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        clean up dataframe
        '''
        # remove nan
        df.fillna('other', axis=0, inplace=True)

        # converts string numerics to floats
        for column in df.columns:
            if column in METRICS:
                df[column] = df[column].apply(
                    self.value_to_float)
                self.metrics.add(column)

        return df

    def load_dfs(self, media: str) -> pd.DataFrame:
        assert media in ['Instagram', 'TikTok', 'Youtube']
        dir_path: Path = Path(__file__).absolute(
        ).parent.parent / 'data' / media
        dfs = {str: pd.DataFrame}
        for mnth in MONTHS:
            dfs[mnth] = self.preprocess_frame(
                pd.read_csv(dir_path / f"{media}_{mnth}.csv",
                            encoding='utf-8'))
            dfs[mnth]['Month'] = mnth
            # drop duplicate columns
            dfs[mnth] = dfs[mnth].drop_duplicates(subset=[PRIMARY_KEY])

        df: pd.DataFrame = pd.concat([dfs[mnth]
                                     for mnth in MONTHS], ignore_index=True)
        df['Month'] = df['Month'].astype(MONTHS_DTYPE)
        print(f"A Data Frame of shape {df.shape} formed!!")
        return df

    def get_influencer_fromdf(self, df):
        '''
        pass a dataframe and extract influencer names
        '''
        return list(df[NAME])

    def get_category_items(self, category):
        '''
        gets items pertaining to a category
        param:
        path (type: string) : file name
        output:
        df (type: pd.dataframe) : output data frame column
        '''

        assert(category in self.get_categories()), "inavlid category"
        assert(isinstance(self.df, pd.DataFrame)), "inavlid dataframe"

        # remove nans
        self.df[category] = self.df[category].replace(np.nan, 'other')

        # get entries in category
        subcategories = list(self.df[category])

        # get subcategories
        subcategories = Counter(subcategories)

        return list(subcategories.keys())

    def get_subcategory_items(self, df, category, subcategory):
        '''
        gets items pertaining to a sub-category
        param:
        category (type: string) : main category
        subcategory (type: string) : subcategory under the specific category
        output:
        items (type: pd.dataframe) : output data frame
                column filtered by subcategory
        '''

        return df[df[category].str.contains(subcategory)]
    
    def filter_by_month(self, df, month):
        '''
        gets items pertaining to a sub-category
        param:
        category (type: string) : main category
        subcategory (type: string) : subcategory under the specific category
        output:
        items (type: pd.dataframe) : output data frame
                column filtered by subcategory
        '''
        assert((month,str) and month in MONTHS),"invalid month"

        return df[df['Month'].str.contains(month)]

    def find_topn_influencers(self, dataframe, N):
        '''
        returns dataframe pertaining to top N influencers
        param:
        dataframe (type: pd.DataFrame) : dataframe
        N (type: int) : number of influencer data needed
        output:
        dictionary of dataframe (type: pd.DataFrame):
                sorted top N influencer data
        '''
        top = {}
        # return top N influencers based on each metric
        for metric in self.metrics:
            df = dataframe.sort_values(by=[metric], ascending=False)
            top[metric] = df.head(N)

        return top

    def get_topn_influencers_categorical(self,criteria, metric, month=MONTHS[0],N=1):
        '''
        Pass a criteria(category) and get info of
            top influencers in each subcategory
        '''
        products = self.get_category_items(criteria)
        
        m_df= self.filter_by_month(self.df,month)

        for i, product in enumerate(products):
            if(i == 0):
                filtered_df = self.find_topn_influencers(
                    self.get_subcategory_items(m_df, criteria, product),
                    1)[metric]
            else:
                filtered_df = pd.concat([filtered_df,
                                         self.find_topn_influencers(
                                             self.get_subcategory_items(
                                                m_df, criteria, product),
                                             1)[metric]], axis=0)

        return filtered_df

    # helper functions
    def value_to_float(self, x):
        if type(x) == float or type(x) == int:
            return float(x)
        if 'K' in x:
            if len(x) > 1:
                return float(x.replace('K', '')) * 1000
            return 1000.0
        if 'M' in x:
            if len(x) > 1:
                return float(x.replace('M', '')) * 1000000
            return 1000000.0