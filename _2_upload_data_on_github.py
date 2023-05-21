"""

    """

import shutil
from pathlib import Path

from githubdata import GitHubDataRepo
from mirutil.ns import rm_ns_module
from persiantools.jdatetime import JalaliDateTime

import ns
from _0_get_adj_prices import tfp
from _1_data_cleaning import fps

gdu = ns.GDU()

def main() :
    pass

    ##
    gdt = GitHubDataRepo(gdu.adjp)
    gdt.clone_overwrite()

    ##
    if hasattr(gdt , 'data_fp') :
        gdt.data_fp.unlink()

    ##
    tjd = JalaliDateTime.now().strftime('%Y-%m-%d')

    fp = gdt.local_path / f'{fps.stem}-{tjd}.prq'

    shutil.copy2(fps , fp)

    ##
    msg = 'Updated on ' + tjd
    msg += ' by ' + gdu.slf

    ##
    gdt.commit_and_push(msg , branch = 'main')

    ##
    gdt.rmdir()

    ##
    tfp.unlink()
    fps.unlink()
    rm_ns_module()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##
if False :
    pass

    ##
    fp = '/Users/mahdi/Dropbox/GitHub/u-d-Adj-Prices/d-Adj-Prices/Adj-Prices-1401-10-21.prq'

    df = pd.read_parquet(fp)

    ##
