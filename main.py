"""

    """

from pathlib import Path
import datetime as dt
from dateutil.relativedelta import relativedelta

import pandas as pd
import numpy as np
import statsmodels.api as sm
from persiantools.jdatetime import JalaliDate
import matplotlib.pyplot as plt
from scipy import stats

from mirutil.ns import update_ns_module as unm

unm()
import ns

gdu = ns.GDU()

class Const :
    price_url = 'https://members.tsetmc.com/tsev2/chart/data/Financial.aspx?i={}&t=ph&a={}'

cte = Const()

def make_price_df(res) :
    df = pd.DataFrame(res.text.split(';'))
    return df[0].str.split(',' , expand = True)

def make_adjusted_price_url(id) :
    return cte.price_url.format(id , 1)

def main() :
    pass

    ##

    ##

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
    r = requests.get(url)

    ##
    r.text

    ##
    import pandas as pd

    df = pd.DataFrame(r.text.split(';'))
    df = df[0].str.split(',' , expand = True)

##
