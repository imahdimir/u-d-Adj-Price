"""

    """

from functools import partial

import pandas as pd

from githubdata import GitHubDataRepo
from mirutil.ns import update_ns_module
from mirutil.utils import ret_clusters_indices
from mirutil.async_req import get_resps_async_sync as gras

update_ns_module()
import ns

gdu = ns.GDU()

class Const :
    price_url = 'https://members.tsetmc.com/tsev2/chart/data/Financial.aspx?i={}&t=ph&a={}'

cte = Const()

class ColName :
    url = 'url'
    res_txt = 'res_text'

cn = ColName()

def make_price_df(res) :
    df = pd.DataFrame(res.text.split(';'))
    return df[0].str.split(',' , expand = True)

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
    fu = partial(gras , ssl = False , headers = None)

    ##
    while True :
        try :
            msk = dfi[cn.res_txt].isna()
            df1 = dfi[msk]
            if df1.empty :
                break

            cls = ret_clusters_indices(df1 , 30)

            for se in cls :
                si = se[0]
                ei = se[1]
                print(se)

                inds = df1.index[si : ei]

                urls = dfi.loc[inds , cn.url]
                resps = fu(urls)

                dfi.loc[inds , cn.res_txt] = [x.cont for x in resps]

                # break

            # break

        except KeyboardInterrupt :
            pass

    ##
    msk = dfi[cn.res_txt].notna()
    dfi.loc[msk , cn.res_txt] = dfi.loc[
        msk , cn.res_txt].apply(lambda x : x.decode('utf-8'))

##


if __name__ == "__main__" :
    main()

##

# noinspection PyUnreachableCode
if False :
    pass

    ##
    import requests

    url = 'https://members.tsetmc.com/tsev2/chart/data/Financial.aspx?i={}&t=ph&a=1'
    url.format(1)

    ##
    make_adjusted_price_url(2)

    ##
    id = "2400322364771558"
    url = 'https://members.tsetmc.com/tsev2/chart/data/Financial.aspx?i={}&t=ph&a={}'
    url = url.format(id , 0)
    url
    ##
    r = requests.get(url)

    ##
    r.text

    ##

    ##
    import pandas as pd

    df = pd.DataFrame(r.text.split(';'))
    df = df[0].str.split(',' , expand = True)

##
