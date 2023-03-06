import pandas as pd
import numpy as np
from wordhoard import Synonyms
from collections import Counter
import string
import re

class Social:
      

    def __init__(self,path):
         '''
         initialize instance of platform
         '''
         assert(isinstance(path,str)), "invalid file path "
         self.read_to_dataframe(path)
         self.preprocess_frame()


    def get_categories(self):
        '''
        Returns the categories in a dataframe
        '''
        return self.categories

    def preprocess_frame(self):
        '''
        clean up dataframe
        '''
        self.metrics=[]
        #remove nan
        self.df.dropna(0, inplace=True)

        #get attributes in csv
        headings= self.df.head(0)
        headings=(list(headings.columns))
        data=list(self.df.iloc[1,:])


        #convert numeric suffixes to numeric
        for i,dat in enumerate(data):
            if(isinstance(dat,str) and dat[0].isnumeric()):
                if(dat.lower().endswith('m') or dat.lower().endswith('b') or dat.lower().endswith('k') ):
                    self.df[headings[i]]=self.df[headings[i]].apply(self.value_to_float)
                    self.metrics.append(headings[i])
        
        #drop duplicate columns
        self.df.drop_duplicates(subset=[headings[1],headings[2]],inplace=True)

        self.categories=[heading.strip() for heading in headings]
        self.name_head=headings[2]

       
    def get_influencer_fromdf(self,df):
        '''
        pass a dataframe and extract influencer names
        '''
        return list(df[self.name_head])


    def read_to_dataframe(self,path):
        '''
        Reads a csv into a dataframe.
        param: 
        path (type: string) : file name 
        '''
        self.df=pd.read_csv(path)

    def get_category_items(self, category):
        '''
        gets items pertaining to a category
        param: 
        path (type: string) : file name 
        
        output:
        df (type: pd.dataframe) : output data frame column
        '''

        assert(category in self.categories),"inavlid category"
        assert(isinstance(self.df,pd.DataFrame)),"inavlid dataframe"

        #remove nans
        self.df[category] = self.df[category].replace(np.nan, 'other')

        #get entries in category
        subcategories=list(self.df[category])

        #get subcategories
        subcategories=Counter(subcategories)

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
        items (type: pd.dataframe) : output data frame column filtered by subcategory
        '''

        return df[df[category].str.contains(subcategory)] 
    
    def find_topn_influencers(self, dataframe,N):
        '''
        returns dataframe pertaining to top N influencers
        param: 
        dataframe (type: pd.DataFrame) : dataframe
        N (type: int) : number of influencer data needed
        
        output:
        dictionary of dataframe (type: pd.DataFrame): sorted top N influencer data
        '''
        top={}
        #return top N influencers based on each metric 
        for metric in self.metrics:
            df=dataframe.sort_values(by=[metric],ascending=False)
            top[metric]=df.head(N)
            
        return top


    #helper functions
    def value_to_float(self,x):
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