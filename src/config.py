from typing import List, Set

import pandas as pd

PLATFORMS = ['Instagram', 'Youtube', 'TikTok']
MONTHS: List[str] = ['Sep', 'Oct', 'Nov', 'Dec']
PRIMARY_KEY: str = 'AccountName'
MONTHS_DTYPE: pd.CategoricalDtype = pd.CategoricalDtype(
    categories=MONTHS, ordered=True)
METRICS: List[str] = ['Subscribers', 'AuthenticEngagement',
                     'EngagementAverage',
                     'Views', 'Likes', 'Comments', 'Shares']
NAME: str = 'Name'
FILTERS: List[str] = ['Country', 'Category_1']
TOP_N: List[int] = [1, 3, 5, 10]
