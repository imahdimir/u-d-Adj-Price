"""
    remarks:
    - some TSETMC_IDs don't have data in res_text. I checked for "آبادا" manually, it has two TSETMS_IDs both with the same firm ticker only one of them has data. the other one is one the bazarpaye and never traded. so having no data makes sense.

    """

import pandas as pd
from mirutil.df import save_df_as_prq
from mirutil.jdate import gen_iso_jdate_fr_jdate_in_df
from mirutil.jdate import gen_jdate_fr_date_in_df

from main import c
from main import cn
from main import fp

def make_price_df_of_a_row(res_text) :
    df = pd.DataFrame(res_text.split(';'))
    return df[0].str.split(',' , expand = True)

def make_price_df(df_raw) :
    # this should be done in parallel, \TODO

    df = pd.DataFrame()

    for ind , s in df_raw.iterrows() :
        _df = make_price_df_of_a_row(s[cn.res_txt])

        _df[c.ftic] = s[c.ftic]
        _df[c.tse_id] = s[c.tse_id]

        df = pd.concat([df , _df])

    return df

def rename_cols(df) :
    cns = {
            '0' : c.d ,
            '1' : c.ahi ,
            '2' : c.alow ,
            '3' : c.aopen ,
            '4' : c.aclose ,
            '5' : c.vol ,
            '6' : c.alast ,
            }

    df = df.rename(columns = cns)

    return df

def drop_empty_date_rows(df) :
    pat = r'\d{4}\d{2}\d{2}'
    msk = ~ df[c.d].str.fullmatch(pat)

    _df = df[msk]

    df = df[~ msk]

    return df

def assert_no_na_after_dropping_no_date_rows(df) :
    msk = df.isna().any(axis = 1)
    _df = df[msk]
    assert _df.empty , "There are NaNs in the data!"

def assert_no_duplicates_on_date_firmticker_pair(df) :
    msk = df.duplicated(subset = [c.d , c.ftic] , keep = False)
    _df = df[msk]
    assert _df.empty , "There are duplicated rows"

def reorder_cols_and_drop_vol(df) :
    cns = {
            c.ftic   : None ,
            c.tse_id : None ,
            c.d      : None ,
            c.jd     : None ,
            c.aopen  : None ,
            c.ahi    : None ,
            c.alow   : None ,
            c.alast  : None ,
            c.aclose : None ,
            }

    df = df[cns.keys()]

    return df

def main() :
    pass

    ##

    # read downloaded(raw) data
    dfr = pd.read_parquet(fp.t0)

    ##

    df = make_price_df(dfr)
    save_df_as_prq(df , fp.t1_0)

    ##

    df = pd.read_parquet(fp.t1_0)

    ##

    df = rename_cols(df)

    ##

    df = drop_empty_date_rows(df)
    assert_no_na_after_dropping_no_date_rows(df)

    ##

    df[c.d] = pd.to_datetime(df[c.d] , format = '%Y%m%d')
    df[c.d] = df[c.d].dt.strftime('%Y-%m-%d')

    ##

    df = gen_jdate_fr_date_in_df(df , c.d , c.jd , date_fmt = '%Y-%m-%d')
    df = gen_iso_jdate_fr_jdate_in_df(df , c.jd , c.jd)

    ##

    assert_no_duplicates_on_date_firmticker_pair(df)

    ##

    df = reorder_cols_and_drop_vol(df)

    ##

    save_df_as_prq(df , fp.t1_1)

##
if __name__ == "__main__" :
    main()
