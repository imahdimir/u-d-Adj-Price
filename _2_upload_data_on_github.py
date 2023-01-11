"""

    """

import time
from pathlib import Path

import pandas as pd
from persiantools.jdatetime import JalaliDateTime
from githubdata import GitHubDataRepo
from giteasy.githubb import add_overwrite_a_file_2_repo

import ns
from _0_get_adj_prices import ColName as PCN

gdu = ns.GDU()
c = ns.Col()

def main() :
    pass

    ##
    fp = Path('Adj-Prices.prq')

    msg = 'Updated on ' + JalaliDateTime.now().strftime('%Y-%m-%d')
    msg += ' by ' + gdu.slf

    ##

    ##

    ##

    ##

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##

# noinspection PyUnreachableCode
if False :
    pass

    ##

##
