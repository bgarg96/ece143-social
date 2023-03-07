from typing import List, Set

import pandas as pd

MONTHS: List[str] = ['Sep', 'Oct', 'Nov', 'Dec']
PRIMARY_KEY: str = 'AccountName'
MONTHS_DTYPE: pd.CategoricalDtype = pd.CategoricalDtype(
    categories=MONTHS, ordered=True)
NUMERIC_COLUMNS: Set[str] = {'Subscribers', 'AuthenticEngagement',
                             'EngagementAverage',
                             'Views', 'Likes', 'Comments', 'Shares'}
NAME: str = 'Name'
FILTERS: Set[str] = {'Country','Category_1'}
