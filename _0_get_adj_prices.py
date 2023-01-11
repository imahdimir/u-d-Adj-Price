"""

    """

import time
from pathlib import Path

import pandas as pd
import requests
from githubdata import GitHubDataRepo
from mirutil.ns import update_ns_module

update_ns_module()
import ns

gdu = ns.GDU()
c = ns.Col()

class Const :
    price_url = 'https://members.tsetmc.com/tsev2/chart/data/Financial.aspx?i={}&t=ph&a={}'
    headers = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }

cte = Const()

class ColName :
    url = 'url'
    res_txt = 'res_text'

cn = ColName()

def make_adjusted_price_url(id) :
    return cte.price_url.format(id , 1)

def main() :
    pass

    ##

    # Get the list of all stock ids
    gdi = GitHubDataRepo(gdu.ids)
    gdi.clone_overwrite()

    ##
    dfi_fp = gdi.data_fp
    dfi = pd.read_excel(dfi_fp , dtype = str)

    ##
    dfi[cn.url] = dfi[ns.Col.tse_id].apply(make_adjusted_price_url)
    dfi[cn.res_txt] = None

    ##
    for _ in range(10) :
        msk = dfi[cn.res_txt].isna()
        msk |= dfi[cn.res_txt].eq('')

        df1 = dfi[msk]
        print('empty ones:' , len(df1))
        if df1.empty :
            break

        for ind , ro in dfi.iterrows() :
            if not (pd.isna(ro[cn.res_txt]) or ro[cn.res_txt] == '') :
                continue

            r = requests.get(ro[cn.url] , headers = cte.headers)
            dfi.loc[ind , cn.res_txt] = r.text
            print(ro[c.ftic] , r.text[:30])

            time.sleep(.5)

        # break

    ##
    dfi.to_parquet('temp.prq' , index = False)

    ##
    gdi.rmdir()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
