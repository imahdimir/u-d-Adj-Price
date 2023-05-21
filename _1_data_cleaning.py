"""

    """

from pathlib import Path

import pandas as pd
from persiantools.jdatetime import JalaliDateTime

import ns
from _0_get_adj_prices import ColName as PCN
from _0_get_adj_prices import tfp

gdu = ns.GDU()
c = ns.Col()

fps = Path('Adj-Prices.prq')

class ColName(PCN) :
    get_date = 'GetJDate'

cn = ColName()

def make_price_df(res_text) :
    df = pd.DataFrame(res_text.split(';'))
    return df[0].str.split(',' , expand = True)

def main() :
    pass

    ##
    dfi = pd.read_parquet(tfp)

    ##
    dfp = pd.DataFrame()

    for ind , ro in dfi.iterrows() :
        df1 = make_price_df(ro[cn.res_txt])
        df1[c.ftic] = ro[c.ftic]
        df1[c.tse_id] = ro[c.tse_id]

        dfp = pd.concat([dfp , df1])

    ##
    cns = {
            0 : c.d ,
            1 : c.ahi ,
            2 : c.alow ,
            3 : c.aopen ,
            4 : c.aclose ,
            5 : c.vol ,
            6 : c.alast ,
            }

    dfp = dfp.rename(columns = cns)

    ##
    pat = r'\d{4}\d{2}\d{2}'
    msk = ~ dfp[c.d].str.fullmatch(pat)

    df1 = dfp[msk]

    ##
    dfp = dfp[~ msk]

    ##
    msk = dfp.isna().any(axis = 1)
    df1 = dfp[msk]

    assert df1.empty

    ##
    dfp[c.d] = pd.to_datetime(dfp[c.d] , format = '%Y%m%d')

    ##
    dfp[c.jd] = dfp[c.d].apply(JalaliDateTime.to_jalali)

    ##
    dfp[c.jd] = dfp[c.jd].apply(lambda x : x.strftime('%Y-%m-%d'))

    ##
    dfp[c.d] = dfp[c.d].apply(lambda x : x.strftime('%Y-%m-%d'))

    ##
    tod_date = JalaliDateTime.today().strftime('%Y-%m-%d')
    dfp[cn.get_date] = tod_date

    ##
    msk = dfp.duplicated(subset = [c.ftic , c.d] , keep = False)
    df1 = dfp[msk]

    assert df1.empty

    ##
    col_ord = {
            cn.get_date : None ,
            c.tse_id    : None ,
            c.ftic      : None ,
            c.d         : None ,
            c.jd        : None ,
            c.aopen     : None ,
            c.ahi       : None ,
            c.alow      : None ,
            c.alast     : None ,
            c.vol       : None ,
            c.aclose    : None ,
            }

    dfp = dfp[col_ord.keys()]

    ##
    dfp.to_parquet(fps , index = False)

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
