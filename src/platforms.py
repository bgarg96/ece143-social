import pandas as pd
import numpy as np
from wordhoard import Synonyms
from collections import Counter

import numpy as np
import pandas as pd

from config import MONTHS, MONTHS_DTYPE, NAME, METRICS, PRIMARY_KEY
from uts import weighted_average


class Social:

        '''
        initialize instance of platform
        '''

    def get_categories(self):
        '''
        Returns the categories in a dataframe
        '''

        '''
        clean up dataframe
        '''
        # converts string numerics to floats
        for column in df.columns:
            if column in METRICS:
                df[column] = df[column].apply(
                    self.value_to_float)
                self.metrics.add(column)



        df: pd.DataFrame = pd.concat([dfs[mnth]
                                     for mnth in MONTHS], ignore_index=True)
        df['Month'] = df['Month'].astype(MONTHS_DTYPE)
        print(f"A Data Frame of shape {df.shape} formed!!")
        return df

        '''
        pass a dataframe and extract influencer names
        '''

    def get_category_items(self, category):
        '''
        gets items pertaining to a category
        param:
        path (type: string) : file name

        output:
        df (type: pd.dataframe) : output data frame column
        '''


        self.df[category] = self.df[category].replace(np.nan, 'other')



        return list(subcategories.keys())

    # def process_subcategories(self, subcategories):
    
    #     assert(isinstance(subcategories,list)),"inavlid sub-category list"
    #     synonyms_dict = {}
    #     for word in subcategories:
    #         synonym = Synonyms(word)
    #         synonyms_results = synonym.find_synonyms()
    #         if synonyms_results is not None:
    #             synonyms_dict[word] = synonyms_results
    #         else:
    #             synonyms_dict[word] = 'no synonyms found'


    #     return synonyms_dict
    
    
    def get_subcategory_items(self, df, category, subcategory):
        '''
        gets items pertaining to a sub-category
        param:
        category (type: string) : main category
        subcategory (type: string) : subcategory under the specific category

        output:
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

        '''
        returns dataframe pertaining to top N influencers
        param:
        dataframe (type: pd.DataFrame) : dataframe
        N (type: int) : number of influencer data needed

        output:
        '''
        for metric in self.metrics:

        return top

    def get_topn_influencers_categorical(self,criteria, metric, month=MONTHS[0],N=1):

        '''
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
