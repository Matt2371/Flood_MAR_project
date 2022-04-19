import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm


# for given layer, plot differences (annual average GW level under all SUBSIDENCE ELEMENTS) between strategies,
# ANNUAL AVERAGE
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
    plt.plot(df_baseline['SUB_AVERAGE'], color='#610345')
    plt.plot(df_initial['SUB_AVERAGE'], color='#5773FF')
    plt.plot(df_intermediate['SUB_AVERAGE'], color='#00D19D')
    plt.plot(df_robust['SUB_AVERAGE'], color='#9B7874')

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
    plt.plot(df_initial['SUB_AVERAGE'], color='#5773FF')
    plt.plot(df_intermediate['SUB_AVERAGE'], color='#00D19D')
    plt.plot(df_robust['SUB_AVERAGE'], color='#9B7874')

    plt.xlabel('Year')
    plt.ylabel('Groundwater Level Deltas, ft')
    plt.title('Annual GW relative to Baseline: ' + layer + ' layer under subsidence areas')
    plt.legend(['Initial', 'Intermediate', 'Robust'])

    plt.savefig('Data/Annual_averages/Subsidence/Figures/SUB_' + layer + '_compare_strategies_del.png')
    plt.clf()

    return


# FOR LAST 10 YEARS OF SIMULATION, SUBSIDENCE ELEMENTS: create boxplot of basin-wide distribution, ANNUAL AVERAGE
def sub_boxplot(strategy, layer):
    df = pd.read_csv('Data/Annual_averages/Subsidence/' + strategy + '_GW_' + layer + '_aa_SUB.csv', index_col=0,
                     parse_dates=True)
    # show only year in index
    df.index = df.index.year
    # remove basin average column
    df.drop('SUB_AVERAGE', axis=1)
    # take last 10 years
    df = df.tail(10)

    # create boxplot
    df.T.plot.box(showfliers=False)
    plt.title('GW level under subsidence zones: ' + strategy.lower() + ' strategy ' + layer.lower() + ' layer')
    plt.ylabel('Groundwater level, ft')
    plt.xlabel('Year')
    plt.savefig('Data/Annual_averages/Subsidence/Figures/SUB_' + strategy + '_GW_' + layer + '_aa_boxplot.png')
    plt.clf()
    return


# LAST 10 YEARS OF SIMULATION, SUBSIDENCE elements: create boxplot of basin-wide distribution of DELTAS, ANNUAL AVERAGE
def sub_boxplot_del(strategy, layer):
    df = pd.read_csv('Data/Annual_averages/Subsidence/Deltas/' + strategy + '_GW_' + layer + '_aa_SUB_del.csv', index_col=0,
                     parse_dates=True)
    # show only year in index
    df.index = df.index.year
    # remove basin average column
    df.drop('SUB_AVERAGE', axis=1)
    # take last 10 years
    df = df.tail(10)

    # create boxplot
    df.T.plot.box(showfliers=False)
    plt.title('GW deltas under subsidence zones: ' + strategy.lower() + ' strategy ' + layer.lower() + ' layer')
    plt.ylabel('Groundwater level, ft')
    plt.xlabel('Year')
    plt.savefig('Data/Annual_averages/Subsidence/Figures/SUB_' + strategy + '_GW_' + layer + '_aa_del_boxplot.png')
    plt.clf()
    return


# Plot results
layers = ['confined', 'unconfined', 'average']
strategies = ['Baseline', 'Initial', 'Intermediate', 'Robust']

for layer in tqdm(layers, desc='Exporting results (layers):'):
    sub_compare_strategies(layer)
    sub_del_compare_strategies(layer)

    for strategy in strategies:
        sub_boxplot(strategy, layer)
        if strategy == 'Baseline':
            continue
        sub_boxplot_del(strategy, layer)
