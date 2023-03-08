import pandas as pd
import numpy as np
from wordhoard import Synonyms
from collections import Counter

import numpy as np
import pandas as pd

from config import MONTHS, MONTHS_DTYPE, NAME, NUMERIC_COLUMNS, PRIMARY_KEY
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

        '''
        returns dataframe pertaining to top N influencers
        param:
        dataframe (type: pd.DataFrame) : dataframe
        N (type: int) : number of influencer data needed

        output:
        '''
        for metric in self.metrics:

        return top

        '''
        '''

            else:

        return filtered_df

        if type(x) == float or type(x) == int:
            return x
        if 'K' in x:
            if len(x) > 1:
                return float(x.replace('K', '')) * 1000
            return 1000.0
        if 'M' in x:
            if len(x) > 1:
                return float(x.replace('M', '')) * 1000000
            return 1000000.0
        if 'B' in x:
            return float(x.replace('B', '')) * 1000000000
        return 0.0
