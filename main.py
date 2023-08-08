"""

    """

from pathlib import Path

from modules import _0_get_adj_prices
from modules import _1_data_cleaning
from modules import _2_upload_data_on_github

def main() :
    pass

    ##
    _0_get_adj_prices.main()

    ##
    _1_data_cleaning.main()

    ##
    _2_upload_data_on_github.main()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
