"""

    """

from namespace_mahdimir import tse as tse_ns
from namespace_mahdimir import tse_github_data_url as tgdu
from run_py import DefaultDirs
from run_py import rm_cache_dirs
from run_py import run_modules

class GDU :
    g = tgdu.GitHubDataUrl()

    adj_price_t = g.adj_price

    slf = tgdu.m + 'u-' + adj_price_t

    id_2_ftic_s = g.id_2_ftic

class Dirs :
    dd = DefaultDirs(make_default_dirs = True)

    gd = dd.gd
    t = dd.t

class FPs :
    dyr = Dirs()

    # temp data files
    t0 = dyr.t / 't0.prq'
    t1_0 = dyr.t / 't1_0.prq'
    t1_1 = dyr.t / 't1_1.prq'

class ColName :
    url = 'url'
    res_txt = 'res_text'

# class instances   %%%%%
c = tse_ns.Col()

gdu = GDU()
dyr = Dirs()
fp = FPs()
cn = ColName()

def main() :
    pass

    ##
    run_modules()

    ##
    rm_cache_dirs()

##
if __name__ == "__main__" :
    main()
    print('\n\n\t\t***** main.py Done! *****\n\n')
