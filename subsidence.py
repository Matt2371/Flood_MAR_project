import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm


# FIXME: ADD DOCUMENTATION FOR SCRIPT

# for given layer, plot differences (annual average GW level under all SUBSIDENCE ELEMENTS) between strategies, ANNUAL AVERAGE
def sub_compare_strategies(layer):
    # read SUB_cut csv's
    df_baseline = pd.read_csv('Data/Annual_averages/Subsidence/Baseline_GW_' + layer + '_aa_SUB.csv', index_col=0,
                              parse_dates=True)
    df_initial = pd.read_csv('Data/Annual_averages/Subsidence/Initial_GW_' + layer + '_aa_SUB.csv', index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/Subsidence/Intermediate_GW_' + layer + '_aa_SUB.csv',
                                  index_col=0,
                                  parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/Subsidence/Robust_GW_' + layer + '_aa_SUB.csv', index_col=0,
                            parse_dates=True)

    # plot to compare strategies
    plt.plot(df_baseline['SUB_AVERAGE'])
    plt.plot(df_initial['SUB_AVERAGE'])
    plt.plot(df_intermediate['SUB_AVERAGE'])
    plt.plot(df_robust['SUB_AVERAGE'])

    plt.xlabel('Year')
    plt.ylabel('Groundwater Level, ft')
    plt.title('Annual GW: ' + layer + ' layer under subsidence areas')
    plt.legend(['Baseline', 'Initial', 'Intermediate', 'Robust'])

    plt.savefig('Data/Annual_averages/Subsidence/Figures/SUB_' + layer + '_compare_strategies.png')
    plt.clf()

    return


# FOR DELTAS UNDER SUBSIDENCE ELEMENTS: plot differences between strategies for each layer, ANNUAL AVERAGE
# layer, str = ['confined', 'unconfined', 'average']
def sub_del_compare_strategies(layer):
    df_initial = pd.read_csv('Data/Annual_averages/Subsidence/Deltas/Initial_GW_' + layer + '_aa_SUB_del.csv',
                             index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/Subsidence/Deltas/Intermediate_GW_' + layer + '_aa_SUB_del.csv',
                                  index_col=0, parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/Subsidence/Deltas/Robust_GW_' + layer + '_aa_SUB_del.csv',
                            index_col=0,
                            parse_dates=True)

    # plot to compare strategies
    plt.plot(df_initial['SUB_AVERAGE'])
    plt.plot(df_intermediate['SUB_AVERAGE'])
    plt.plot(df_robust['SUB_AVERAGE'])

    plt.xlabel('Year')
    plt.ylabel('Groundwater Level Deltas, ft')
    plt.title('Annual GW relative to Baseline: ' + layer + ' layer under subsidence areas')
    plt.legend(['Initial', 'Intermediate', 'Robust'])

    plt.savefig('Data/Annual_averages/Subsidence/Figures/SUB_' + layer + '_compare_strategies_del.png')
    plt.clf()

    return


# Plot results
layers = ['confined', 'unconfined', 'average']
for layer in tqdm(layers, desc='Exporting results (layers):'):
    sub_compare_strategies(layer)
    sub_del_compare_strategies(layer)
