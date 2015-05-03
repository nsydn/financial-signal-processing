# data_handling.py
from pyalgotrade.tools import yahoofinance
import pandas as pd
from datetime import date


def log_business_years(instrument, years):
    df = pd.read_csv(
        './data/historical/daily_company_years.csv', index_col='instrument')
    df.loc[instrument] = years
    df = df.sort(['first-year'], ascending=False)
    df.to_csv(
        './data/historical/daily_company_years.csv', index_label='instrument')


def acquire_daily_data(instrument, year):
    if year == 'all':
        this_year = date.today().year  # Get current year
        final_year = this_year
        in_business = True
        while in_business:
            try:
                yahoofinance.build_feed(
                    [instrument], this_year, this_year,
                    './data/historical/daily-atrader',
                    frequency=86400, skipErrors=False)
            except:
                in_business = False
                log_business_years(instrument, [this_year + 1, final_year])
            else:
                this_year -= 1
    else:
        yahoofinance.build_feed([instrument], year[0], year[1],
                                './data/historical/daily-atrader',
                                frequency=86400, skipErrors=False)


def build_complete_dataset(instruments):
    for instrument in instruments:
        acquire_daily_data(instrument, 'all')


def build_stock_feed(instruments, years):
    return yahoofinance.build_feed(instruments, years[0], years[1],
                                   './data/historical/daily-atrader',
                                   frequency=86400, skipErrors=False)


def find_instruments_by_year(start_year):
    df = pd.read_csv(
        './data/historical/daily_company_years.csv', index_col='instrument')
    existing_companies = df[df['first-year'] < start_year]
    return existing_companies.index.values.tolist()


def main():
    instrumentstoget = ['A', 'AA', 'AAL', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACE', 'ACN', 'ACT', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'ADT', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AIG', 'AIV', 'AIZ', 'AKAM', 'ALL', 'ALLE', 'ALTR', 'ALXN', 'AMAT', 'AME', 'AMG', 'AMGN', 'AMP', 'AMT', 'AMZN', 'AN', 'ANTM', 'AON', 'APA', 'APC', 'APD', 'APH', 'ARG', 'ATI', 'AVB', 'AVGO', 'AVY', 'AXP', 'AZO', 'BA', 'BAC', 'BAX', 'BBBY', 'BBT', 'BBY', 'BCR', 'BDX', 'BEN', 'BF.B', 'BHI', 'BIIB', 'BK', 'BLK', 'BLL', 'BMY', 'BRCM', 'BRK-B', 'BSX', 'BWA', 'BXP', 'C', 'CA', 'CAG', 'CAH', 'CAM', 'CAT', 'CB', 'CBG', 'CBS', 'CCE', 'CCI', 'CCL', 'CELG', 'CERN', 'CF', 'CHK', 'CHRW', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNP', 'CNX', 'COF', 'COG', 'COH', 'COL', 'COP', 'COST', 'CPB', 'CRM', 'CSC', 'CSCO', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVC', 'CVS', 'CVX', 'D', 'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DLPH', 'DLTR', 'DNB', 'DO', 'DOV', 'DOW', 'DPS', 'DRI', 'DTE', 'DTV', 'DUK', 'DVA', 'DVN', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMC', 'EMN', 'EMR', 'ENDP', 'EOG', 'EQIX', 'EQR', 'EQT', 'ES', 'ESRX', 'ESS', 'ESV', 'ETFC', 'ETN', 'ETR', 'EW', 'EXC', 'EXPD', 'EXPE', 'F', 'FAST', 'FB', 'FCX', 'FDO', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOSL', 'FOXA', 'FSLR', 'FTI', 'FTR', 'GAS', 'GCI', 'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GMCR', 'GME', 'GNW', 'GOOG', 'GOOGL', 'GPC', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAR', 'HAS', 'HBAN', 'HBI', 'HCA', 'HCBK', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HOG', 'HON', 'HOT', 'HP', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSIC', 'HSP', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IFF', 'INTC', 'INTU', 'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'ITW', 'IVZ', 'JCI',
                        'JEC', 'JNJ', 'JNPR', 'JOY', 'JPM', 'JWN', 'K', 'KEY', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR', 'KRFT', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH', 'LLL', 'LLTC', 'LLY', 'LM', 'LMT', 'LNC', 'LO', 'LOW', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MA', 'MAC', 'MAR', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MHFI', 'MHK', 'MJN', 'MKC', 'MLM', 'MMC', 'MMM', 'MNK', 'MNST', 'MO', 'MON', 'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTB', 'MU', 'MUR', 'MWV', 'MYL', 'NAVI', 'NBL', 'NDAQ', 'NE', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NOV', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWSA', 'O', 'OI', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PBI', 'PCAR', 'PCG', 'PCL', 'PCLN', 'PCP', 'PDCO', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKI', 'PLD', 'PLL', 'PM', 'PNC', 'PNR', 'PNW', 'POM', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'QCOM', 'QEP', 'R', 'RAI', 'RCL', 'REGN', 'RF', 'RHI', 'RHT', 'RIG', 'RL', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBUX', 'SCG', 'SCHW', 'SE', 'SEE', 'SHW', 'SIAL', 'SJM', 'SLB', 'SLG', 'SNA', 'SNDK', 'SNI', 'SO', 'SPG', 'SPLS', 'SRCL', 'SRE', 'STI', 'STJ', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SWN', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDC', 'TE', 'TEG', 'TEL', 'TGT', 'THC', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSO', 'TSS', 'TWC', 'TWX', 'TXN', 'TXT', 'TYC', 'UA', 'UHS', 'UNH', 'UNM', 'UNP', 'UPS', 'URBN', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT', 'WBA', 'WDC', 'WEC', 'WFC', 'WFM', 'WHR', 'WM', 'WMB', 'WMT', 'WU', 'WY', 'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YHOO', 'YUM', 'ZION', 'ZMH', 'ZTS']
    build_complete_dataset(instrumentstoget)


if __name__ == '__main__':
    main()
