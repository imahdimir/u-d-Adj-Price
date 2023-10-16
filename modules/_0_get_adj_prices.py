"""

    """

import time

import requests
from githubdata import get_data_wo_double_clone
from mirutil.const import Const
from mirutil.df import save_df_as_prq

from main import c
from main import cn
from main import fp
from main import gdu

k = Const()

def get_all_stock_ids() :
    return get_data_wo_double_clone(gdu.id_2_ftic_s)

def make_adjusted_price_url(id) :
    url_fmt = 'https://members.tsetmc.com/tsev2/chart/data/Financial.aspx?i={}&t=ph&a={}'
    return url_fmt.format(id , 1)

def get_adj_prices(df) :
    # this should be done in async and maybe for remained ones do it sync, \TODO
    msk = df[cn.res_txt].isna()
    msk |= df[cn.res_txt].eq('')

    _df = df[msk]
    print('empty ones:' , len(_df))
    if _df.empty :
        return df

    for indx , ro in _df.iterrows() :
        r = requests.get(ro[cn.url] , headers = k.headers)

        df.loc[indx , cn.res_txt] = r.text
        print(ro[c.ftic] , r.text[:30])

        time.sleep(.5)

    return df

def main() :
    pass

    ##

    df = get_all_stock_ids()

    ##

    df[cn.url] = df[c.tse_id].apply(make_adjusted_price_url)
    df[cn.res_txt] = None

    ##

    # get ajusted prices, try 10 times
    for i in range(10) :
        print(f'\n\t - Round {i} of trying to get adj prices\n')
        df = get_adj_prices(df)

    ##

    save_df_as_prq(df , fp.t0)

##
if __name__ == "__main__" :
    main()
