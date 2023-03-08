from typing import List, Optional

import pandas as pd

from config import MONTHS, PRIMARY_KEY


def weighted_average(df: pd.DataFrame,
                     var: str,
                     decay_factor: Optional[float] = 0.9,
                     order_by: Optional[str] = 'Month') -> pd.DataFrame:
    df_listed: dict = df.sort_values([PRIMARY_KEY, order_by]).groupby(
        PRIMARY_KEY).agg(({var: list, order_by: list}))\
        .reset_index()\
        .to_dict('records')
    for row in df_listed:
        row[var + '_TW_averge'] = _weighted_average_helper(
            row[var], row[order_by], decay_factor)

    return pd.DataFrame.from_records(df_listed)[
        [PRIMARY_KEY, var + '_TW_averge']]


def _weighted_average_helper(var_list: List[float],
                             timestamps: List[str],
                             decay_factor: float) -> float:
    assert len(var_list) == len(timestamps) and len(var_list) > 0
    list_average = sum(var_list)/len(var_list)
    avg: float = 0.0
    imputes: dict = {str: float}
    for mnth, val in zip(var_list, timestamps):
        imputes[mnth] = val

    for idx, mnth in enumerate(MONTHS[::-1]):
        avg += pow(decay_factor, idx) * \
            (imputes[mnth] if mnth in imputes else list_average)

    return avg
