"""

    """

from namespace_mahdimir import tse as tse_ns
from namespace_mahdimir import tse_github_data_url as tgdu
from run_py import DefaultDirs
from run_py import rm_cache_dirs
from run_py import run_modules

# namespace
c = tse_ns.Col()

class GDU :
    g = tgdu.GitHubDataUrl()

    adj_price_t = g.adj_price

    slf = tgdu.m + 'u-' + adj_price_t

class Dirs :
    dd = DefaultDirs()

    gd = dd.gd
    t = dd.t

class FPN :
    dyr = Dirs()

    # temp data files
    t0 = dyr.t / 't0.prq'

class ColName :
    pass

# class instances   %%%%%
gdu = GDU()
dyr = Dirs()
fpn = FPN()
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
