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


# Take separated csv's and take ANNUAL AVERAGES for all elements (water year, OCT to OCT), also adds 'BASIN_AVERAGE' col
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


## CUT OUT SPECIAL MANAGEMENT ZONES

# From ANNUAL AVERAGE exports, cut out SPECIAL MANAGEMENT ZONES, adds SPATIAL AVERAGES
# special_management_zone, str = ['DAC', 'GWDZones', 'Subsidence', 'EconSR1', 'EconSR2&3']
def smz_cut(special_management_zone, strategy, layer):
    # create dictionary of file naming conventions for special management zone types
    zone = {'DAC': 'DAC', 'GWDZones': 'GWD', 'Subsidence': 'SUB', 'EconSR1': 'SR1', 'EconSR2&3': 'SR23'}

    # read DWR special management zones
    special_zones = pd.read_csv('Data/SpecialManagementZones_Elements.csv')
    # pull element names of specified special management zone
    zone_list = special_zones[special_management_zone].dropna().to_list()
    # convert elements to int then str
    zone_list = [str(entry) for entry in [int(element) for element in zone_list]]

    # read annual average GW data
    df = pd.read_csv('Data/Annual_averages/' + strategy + '_GW_' + layer + '_annual_avg.csv', index_col=0,
                     parse_dates=True)

    # separate special management zones
    df = df[zone_list].copy()

    # add spatial averages
    df[zone[special_management_zone] + '_AVERAGE'] = df.mean(axis=1)

    # export results, aa denotes "annual averaged"
    df.to_csv('Data/Annual_averages/' + special_management_zone + '/' + strategy + '_GW_' + layer + '_aa_' +
              zone[special_management_zone] + '.csv')

    return


## FIND DELTAS FOR BASIN WIDE AND SPECIAL MANAGEMENT ZONES

# Calculate GW level (ANNUAL AVERAGE) relative to the baseline for each Flood-MAR strategy (calculate deltas)
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


# FOR SPECIAL MANAGEMENT ZONE: Calculate GW level (ANNUAL AVERAGE) relative to the baseline
# for each Flood-MAR strategy (calculate deltas)
def smz_deltas(special_management_zone, strategy, layer):
    # create dictionary of file naming conventions for special management zone types
    zone = {'DAC': 'DAC', 'GWDZones': 'GWD', 'Subsidence': 'SUB', 'EconSR1': 'SR1', 'EconSR2&3': 'SR23'}

    if strategy == 'Baseline':
        return
    else:
        # read Baseline data to compare other strategies with
        df_baseline = pd.read_csv('Data/Annual_averages/' + special_management_zone + '/Baseline_GW_' + layer +
                                  '_aa_' + zone[special_management_zone] + '.csv', index_col=0,
                                  parse_dates=True)
        # read data for other strategy
        df = pd.read_csv('Data/Annual_averages/' + special_management_zone + '/' + strategy + '_GW_' + layer +
                         '_aa_' + zone[special_management_zone] + '.csv', index_col=0,
                         parse_dates=True)
        # subtract baseline from baseline
        df = df.subtract(df_baseline)
    # export resulting csv's
    df.to_csv('Data/Annual_averages/' + special_management_zone + '/Deltas/' + strategy + '_GW_' + layer +
              '_aa_' + zone[special_management_zone] + '_del.csv')

    return


## FIND DISTRIBUTIONS (MIN/MAX/MED/MEAN/STDEV) FOR BASIN-WIDE AND SPECIAL MANAGEMENT ZONES


# Create tables of distribution (min/max/med/mean/stdv) of elements for ANNUAL AVERAGE
def distribution(strategy, layer):
    # read data
    df = pd.read_csv('Data/Annual_averages/' + strategy + '_GW_' + layer + '_annual_avg.csv',
                     index_col=0,
                     parse_dates=True)

    # initialize new dataframe with distribution parameters (same index/datetimes as imported file)
    df_distr = pd.DataFrame(index=df.index)
    # populate dataframe
    df_distr['Min'] = df.min(axis=1)
    df_distr['Max'] = df.max(axis=1)
    df_distr['Stdev'] = df.std(axis=1)
    df_distr['Mean'] = df.mean(axis=1)
    df_distr['Median'] = df.median(axis=1)

    # export dataframe
    df_distr.to_csv('Data/Annual_averages/Distributions/Distribution_' + strategy + '_GW_' + layer +
                    '_aa.csv')

    return


# Create tables of distribution (min/max/med/mean/stdv) of elements for ANNUAL AVERAGE DELTAS
def distribution_deltas(strategy, layer):
    # read annual average deltas data
    if strategy == 'Baseline':
        return
    else:
        df = pd.read_csv('Data/Annual_averages/Deltas/' + strategy + '_GW_' + layer + '_aa_del.csv',
                         index_col=0,
                         parse_dates=True)

        # initialize new dataframe with distribution parameters (same index/datetimes as imported file)
        df_distr = pd.DataFrame(index=df.index)
        # populate dataframe
        df_distr['Min'] = df.min(axis=1)
        df_distr['Max'] = df.max(axis=1)
        df_distr['Stdev'] = df.std(axis=1)
        df_distr['Mean'] = df.mean(axis=1)
        df_distr['Median'] = df.median(axis=1)

    df_distr.to_csv('Data/Annual_averages/Deltas/Distributions/Distribution_' + strategy + '_GW_' + layer +
                    '_aa_del.csv')

    return


# Create tables of distribution (min/max/med/mean/stdv) of elements for ANNUAL AVERAGE for SPECIAL MANAGEMENT ZONES
# special_management_zone, str = ['DAC', 'GWDZones', 'Subsidence', 'EconSR1', 'EconSR2&3']
def smz_distribution(special_management_zone, strategy, layer):
    # create dictionary of file naming conventions for special management zone types
    zone = {'DAC': 'DAC', 'GWDZones': 'GWD', 'Subsidence': 'SUB', 'EconSR1': 'SR1', 'EconSR2&3': 'SR23'}
    # read data
    df = pd.read_csv('Data/Annual_averages/' + special_management_zone + '/' + strategy + '_GW_' + layer + '_aa_' +
                     zone[special_management_zone] + '.csv',
                     index_col=0,
                     parse_dates=True)

    # initialize new dataframe with distribution parameters (same index/datetimes as imported file)
    df_distr = pd.DataFrame(index=df.index)
    # populate dataframe
    df_distr['Min'] = df.min(axis=1)
    df_distr['Max'] = df.max(axis=1)
    df_distr['Stdev'] = df.std(axis=1)
    df_distr['Mean'] = df.mean(axis=1)
    df_distr['Median'] = df.median(axis=1)

    df_distr.to_csv(
        'Data/Annual_averages/' + special_management_zone + '/Distributions/Distribution_' + strategy + '_GW_' + layer +
        '_aa_' + zone[special_management_zone] + '.csv')
    return


# Export separated csv's for all strategies
strategies = ['Baseline', 'Initial', 'Intermediate', 'Robust']
layers = ['confined', 'unconfined', 'average']
for strategy in tqdm(strategies, desc='Exporting csv'):
    # separate layer type from given data
    separate_csv(strategy)

    for layer in layers:
        # take and export ANNUAL AVERAGE
        annual_avg(strategy, layer)
        # cut out and export DAC elements
        smz_cut('DAC', strategy, layer)
        # cut out and export GWD elements
        smz_cut('Subsidence', strategy, layer)
        # cut out and export Subsidence elements
        smz_cut('GWDZones', strategy, layer)

        # export csv's of deltas against baseline
        deltas(strategy, layer)
        # export csv's of deltas
        # dac_deltas(strategy, layer)
        smz_deltas('DAC', strategy, layer)
        smz_deltas('Subsidence', strategy, layer)
        smz_deltas('GWDZones', strategy, layer)

        # create tables of distribution parameters for deltas
        distribution_deltas(strategy, layer)

        # Find basin-wide and special management zone distributions
        distribution(strategy, layer)
        smz_distribution('DAC', strategy, layer)
        smz_distribution('Subsidence', strategy, layer)
        smz_distribution('GWDZones', strategy, layer)
        smz_distribution('EconSR1', strategy, layer)
        smz_distribution('EconSR2&3', strategy, layer)
