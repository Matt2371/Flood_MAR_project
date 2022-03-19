import pandas as pd
from tqdm import tqdm


# PURPOSE: clean/process/create raw csv's for further analysis and plotting in other scripts


# Separates layer type (unconfined/confined/average) for all elements in the given DWR data
# Flood-MAR Strategy, str: ['Baseline', 'Initial', 'Intermediate', 'Robust']
def separate_csv(strategy):
    filename = strategy + '_FM2Sim_GW_HeadAll_Elements'
    path = 'Data/' + filename + '.csv'

    # import target csv as dataframe
    df = pd.read_csv(path, index_col=0, parse_dates=True)

    # select unconfined and export results
    df_unconf = df[df['LAYER'] == '0U']
    df_unconf.to_csv('Data/Separated/' + strategy + '_GW_unconfined.csv')

    # select confined and export results
    df_conf = df[df['LAYER'] == '1C']
    df_conf.to_csv('Data/Separated/' + strategy + '_GW_confined.csv')

    # select average and export results
    df_avg = df[df['LAYER'] == '2A']
    df_avg.to_csv('Data/Separated/' + strategy + '_GW_average.csv')

    return


# Take separated csv's and take annual averages for all elements (water year, OCT to OCT), also adds 'BASIN_AVERAGE' col
# strategy, str: ['Baseline', 'Initial', 'Intermediate', 'Robust']
# layer, str = ['confined', 'unconfined', 'average']
def annual_avg(strategy, layer):
    # read separated csv
    df = pd.read_csv('Data/Separated/' + strategy + '_GW_' + layer + '.csv', index_col=0, parse_dates=True)

    # calculate annual averages for all elements
    df = df.resample('AS-OCT').mean()

    # add AVERAGE for all elements (basin-wide average)
    df['BASIN_AVERAGE'] = df.mean(axis=1)

    # export results
    df.to_csv('Data/Annual_averages/' + strategy + '_GW_' + layer + '_annual_avg.csv')
    return


# From annual average exports, cut out DAC elements, also adds 'DAC_AVERAGE' col
def dac_cut(strategy, layer):
    # read DWR special management zones
    special_zones = pd.read_csv('Data/SpecialManagementZones_Elements.csv')
    # pull DAC names (n=36), also drop NaN's
    dac_list = special_zones['DAC'].dropna().to_list()

    # convert elements to int then str
    dac_list = [str(entry) for entry in [int(element) for element in dac_list]]

    # read annual average GW data
    df = pd.read_csv('Data/Annual_averages/' + strategy + '_GW_' + layer + '_annual_avg.csv', index_col=0,
                     parse_dates=True)

    # separate DAC's
    df = df[dac_list].copy()

    # add annual averages
    df['DAC_AVERAGE'] = df.mean(axis=1)

    # export results, aa denotes "annual averaged"
    df.to_csv('Data/Annual_averages/DAC/' + strategy + '_GW_' + layer + '_aa_DAC.csv')

    return


# Calculate GW level (annual average) relative to the baseline for each Flood-MAR strategy (calculate deltas)
def deltas(strategy, layer):
    if strategy == 'Baseline':
        return
    else:
        # read Baseline data to compare other strategies with
        df_baseline = pd.read_csv('Data/Annual_averages/Baseline_GW_' + layer + '_annual_avg.csv', index_col=0,
                                  parse_dates=True)
        # read data for other strategy
        df = pd.read_csv('Data/Annual_averages/' + strategy + '_GW_' + layer + '_annual_avg.csv', index_col=0,
                         parse_dates=True)
        # subtract baseline from baseline
        df = df.subtract(df_baseline)
    # export resulting csv's
    df.to_csv('Data/Annual_averages/Deltas/' + strategy + '_GW_' + layer + '_aa_del.csv')

    return


# Export separated csv's for all strategies
strategies = ['Baseline', 'Initial', 'Intermediate', 'Robust']
layers = ['confined', 'unconfined', 'average']
for strategy in tqdm(strategies, desc='Exporting csv'):
    # separate layer type from given data
    separate_csv(strategy)

    for layer in layers:
        # take and export annual averages
        annual_avg(strategy, layer)
        # cut out and export DAC elements (annual average)
        dac_cut(strategy, layer)
        # export csv's of deltas against baseline
        deltas(strategy, layer)


