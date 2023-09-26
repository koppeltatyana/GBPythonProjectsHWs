# Задача 44:
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import numpy as np
import pandas as pd
from random import shuffle


if __name__ == "__main__":
    lst = ['robot'] * 10 + ['human'] * 10
    shuffle(lst)
    df = pd.DataFrame(
        {
            'whoAmI': lst,
        }
    )

    df['human'] = np.where(df['whoAmI'] == 'human', True, False)
    df['robot'] = np.where(df['whoAmI'] == 'robot', True, False)
    print(df[['human', 'robot']].head())
