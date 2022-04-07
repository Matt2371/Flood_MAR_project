import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm


# for given layer, plot differences (annual average GW level under all GWDs) between strategies, ANNUAL AVERAGE
def gwd_compare_strategies(layer):
    # read GWD_cut csv's
    df_baseline = pd.read_csv('Data/Annual_averages/GWDZones/Baseline_GW_' + layer + '_aa_GWD.csv', index_col=0,
                              parse_dates=True)
    df_initial = pd.read_csv('Data/Annual_averages/GWDZones/Initial_GW_' + layer + '_aa_GWD.csv', index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/GWDZones/Intermediate_GW_' + layer + '_aa_GWD.csv', index_col=0,
                                  parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/GWDZones/Robust_GW_' + layer + '_aa_GWD.csv', index_col=0,
                            parse_dates=True)

    # plot to compare strategies
    plt.plot(df_baseline['GWD_AVERAGE'])
    plt.plot(df_initial['GWD_AVERAGE'])
    plt.plot(df_intermediate['GWD_AVERAGE'])
    plt.plot(df_robust['GWD_AVERAGE'])

    plt.xlabel('Year')
    plt.ylabel('Groundwater Level, ft')
    plt.title('Average annual GW: ' + layer + ' layer under GWD\'s')
    plt.legend(['Baseline', 'Initial', 'Intermediate', 'Robust'])

    plt.savefig('Data/Annual_averages/GWDZones/Figures/GWD_' + layer + '_compare_strategies.png')
    plt.clf()

    return


# FOR DELTAS UNDER GWD ELEMENTS: plot differences between strategies for each layer, ANNUAL AVERAGE
# layer, str = ['confined', 'unconfined', 'average']
def gwd_del_compare_strategies(layer):
    df_initial = pd.read_csv('Data/Annual_averages/GWDZones/Deltas/Initial_GW_' + layer + '_aa_GWD_del.csv',
                             index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/GWDZones/Deltas/Intermediate_GW_' + layer + '_aa_GWD_del.csv',
                                  index_col=0, parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/GWDZones/Deltas/Robust_GW_' + layer + '_aa_GWD_del.csv', index_col=0,
                            parse_dates=True)

    # plot to compare strategies
    plt.plot(df_initial['GWD_AVERAGE'])
    plt.plot(df_intermediate['GWD_AVERAGE'])
    plt.plot(df_robust['GWD_AVERAGE'])

    plt.xlabel('Year')
    plt.ylabel('Groundwater Level Deltas, ft')
    plt.title('Average annual GW relative to Baseline: ' + layer + ' layer under GWD\'s')
    plt.legend(['Initial', 'Intermediate', 'Robust'])

    plt.savefig('Data/Annual_averages/GWDZones/Figures/GWD_' + layer + '_compare_strategies_del.png')
    plt.clf()

    return


# Plot results
layers = ['confined', 'unconfined', 'average']
for layer in tqdm(layers, desc='Exporting results (layers):'):
    gwd_compare_strategies(layer)
    gwd_del_compare_strategies(layer)
