import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm


# plot differences between layers for each strategy, ANNUAL AVERAGE
# strategy, str: ['Baseline', 'Initial', 'Intermediate', 'Robust']
def compare_layers(strategy):
    # read csv's
    df_conf_yravg = pd.read_csv('Data/Annual_averages/' + strategy + '_GW_confined_annual_avg.csv', index_col=0,
                                parse_dates=True)
    df_unconf_yravg = pd.read_csv('Data/Annual_averages/' + strategy + '_GW_unconfined_annual_avg.csv', index_col=0,
                                  parse_dates=True)
    df_avg_yravg = pd.read_csv('Data/Annual_averages/' + strategy + '_GW_average_annual_avg.csv', index_col=0,
                               parse_dates=True)

    # create plots comparing unconfined, confined, and average for each strategy
    # plot confined, unconfined, and average
    plt.plot(df_conf_yravg['BASIN_AVERAGE'])
    plt.plot(df_unconf_yravg['BASIN_AVERAGE'])
    plt.plot(df_avg_yravg['BASIN_AVERAGE'])
    plt.xlabel('Year')
    plt.ylabel('Groundwater Level, ft')
    plt.title('Basin-wide Average Annual GW: ' + strategy + ' Scenario')
    plt.legend(['Confined', 'Unconfined', 'Average'])

    plt.savefig('Data/Annual_averages/Figures/' + strategy + '_average_annual.png')
    plt.clf()

    return


# plot differences between strategies for each layer, ANNUAL AVERAGE
# layer, str = ['confined', 'unconfined', 'average']
def compare_strategies(layer):
    df_initial = pd.read_csv('Data/Annual_averages/' + 'Initial_GW_' + layer + '_annual_avg.csv', index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/' + 'Intermediate_GW_' + layer + '_annual_avg.csv', index_col=0,
                                  parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/' + 'Robust_GW_' + layer + '_annual_avg.csv', index_col=0,
                            parse_dates=True)
    df_baseline = pd.read_csv('Data/Annual_averages/' + 'Baseline_GW_' + layer + '_annual_avg.csv', index_col=0,
                              parse_dates=True)

    # plot to compare strategies
    plt.plot(df_baseline['BASIN_AVERAGE'])
    plt.plot(df_initial['BASIN_AVERAGE'])
    plt.plot(df_intermediate['BASIN_AVERAGE'])
    plt.plot(df_robust['BASIN_AVERAGE'])

    plt.xlabel('Year')
    plt.ylabel('Groundwater Level, ft')
    plt.title('Basin-wide annual average GW: ' + layer + ' layer')
    plt.legend(['Baseline', 'Initial', 'Intermediate', 'Robust'])

    plt.savefig('Data/Annual_averages/Figures/' + layer + '_compare_strategies.png')
    plt.clf()

    return


# compare all features/layers in one graph, ANNUAL AVERAGE
def combine_all():
    df_initial_uc = pd.read_csv('Data/Annual_averages/' + 'Initial_GW_unconfined_annual_avg.csv', index_col=0,
                                parse_dates=True)
    df_intermediate_uc = pd.read_csv('Data/Annual_averages/' + 'Intermediate_GW_unconfined_annual_avg.csv', index_col=0,
                                     parse_dates=True)
    df_robust_uc = pd.read_csv('Data/Annual_averages/' + 'Robust_GW_unconfined_annual_avg.csv', index_col=0,
                               parse_dates=True)
    df_baseline_uc = pd.read_csv('Data/Annual_averages/' + 'Baseline_GW_unconfined_annual_avg.csv', index_col=0,
                                 parse_dates=True)

    df_initial_c = pd.read_csv('Data/Annual_averages/' + 'Initial_GW_confined_annual_avg.csv', index_col=0,
                               parse_dates=True)
    df_intermediate_c = pd.read_csv('Data/Annual_averages/' + 'Intermediate_GW_confined_annual_avg.csv', index_col=0,
                                    parse_dates=True)
    df_robust_c = pd.read_csv('Data/Annual_averages/' + 'Robust_GW_confined_annual_avg.csv', index_col=0,
                              parse_dates=True)
    df_baseline_c = pd.read_csv('Data/Annual_averages/' + 'Baseline_GW_confined_annual_avg.csv', index_col=0,
                                parse_dates=True)

    df_initial_a = pd.read_csv('Data/Annual_averages/' + 'Initial_GW_average_annual_avg.csv', index_col=0,
                               parse_dates=True)
    df_intermediate_a = pd.read_csv('Data/Annual_averages/' + 'Intermediate_GW_average_annual_avg.csv', index_col=0,
                                    parse_dates=True)
    df_robust_a = pd.read_csv('Data/Annual_averages/' + 'Robust_GW_average_annual_avg.csv', index_col=0,
                              parse_dates=True)
    df_baseline_a = pd.read_csv('Data/Annual_averages/' + 'Baseline_GW_average_annual_avg.csv', index_col=0,
                                parse_dates=True)

    # plot to compare strategies
    plt.figure(figsize=(7, 4))
    plt.plot(df_baseline_uc['BASIN_AVERAGE'], c='blue', ls='--')
    plt.plot(df_initial_uc['BASIN_AVERAGE'], c='orange', ls='--')
    plt.plot(df_intermediate_uc['BASIN_AVERAGE'], c='green', ls='--')
    plt.plot(df_robust_uc['BASIN_AVERAGE'], c='red', ls='--')

    plt.plot(df_baseline_c['BASIN_AVERAGE'], c='blue', ls='-.')
    plt.plot(df_initial_c['BASIN_AVERAGE'], c='orange', ls='-.')
    plt.plot(df_intermediate_c['BASIN_AVERAGE'], c='green', ls='-.')
    plt.plot(df_robust_c['BASIN_AVERAGE'], c='red', ls='-.')

    plt.plot(df_baseline_a['BASIN_AVERAGE'], c='blue', ls=':')
    plt.plot(df_initial_a['BASIN_AVERAGE'], c='orange', ls=':')
    plt.plot(df_intermediate_a['BASIN_AVERAGE'], c='green', ls=':')
    plt.plot(df_robust_a['BASIN_AVERAGE'], c='red', ls=':')

    plt.xlabel('Year')
    plt.ylabel('Groundwater Level, ft')
    # plt.title('Flood-MAR effects on basin-wide average annual GW levels')
    plt.legend(['Baseline, unconfined', 'Initial, unconfined', 'Intermediate, unconfined', 'Robust, unconfined',
                'Baseline, confined', 'Initial, confined', 'Intermediate, confined', 'Robust, confined',
                'Baseline, average', 'Initial, average', 'Intermediate, average', 'Robust, average'], loc='center left',
               bbox_to_anchor=(1, 0.5))

    plt.savefig('Data/Annual_averages/Figures/compare_all_strategies.png', bbox_inches='tight')
    # plt.show()
    plt.clf()

    return


# FOR BASIN_WIDE DELTAS: plot differences between strategies for each layer, ANNUAL AVERAGE
# layer, str = ['confined', 'unconfined', 'average']
def del_compare_strategies(layer):
    df_initial = pd.read_csv('Data/Annual_averages/Deltas/Initial_GW_' + layer + '_aa_del.csv', index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/Deltas/Intermediate_GW_' + layer + '_aa_del.csv', index_col=0,
                                  parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/Deltas/Robust_GW_' + layer + '_aa_del.csv', index_col=0,
                            parse_dates=True)

    # plot to compare strategies
    plt.plot(df_initial['BASIN_AVERAGE'])
    plt.plot(df_intermediate['BASIN_AVERAGE'])
    plt.plot(df_robust['BASIN_AVERAGE'])

    plt.xlabel('Year')
    plt.ylabel('Groundwater Level Deltas, ft')
    plt.title('Basin-wide annual average GW relative to Baseline: ' + layer + ' layer')
    plt.legend(['Initial', 'Intermediate', 'Robust'])

    plt.savefig('Data/Annual_averages/Figures/' + layer + '_compare_strategies_del.png')
    plt.clf()

    return


# ## DISCONTINUED
# # Plot MINIMUMS of baseline DELTAS for different strategies, ANNUAL AVERAGE DELTAS
# def del_compare_strategies_mins(layer):
#     # import strategies for given layer
#     df_initial = pd.read_csv('Data/Annual_averages/Deltas/Distributions/Distribution_initial_GW_' + layer +
#                              '_aa_del.csv', index_col=0, parse_dates=True)
#     df_intermediate = pd.read_csv('Data/Annual_averages/Deltas/Distributions/Distribution_intermediate_GW_' + layer +
#                                   '_aa_del.csv', index_col=0, parse_dates=True)
#     df_robust = pd.read_csv('Data/Annual_averages/Deltas/Distributions/Distribution_robust_GW_' + layer +
#                             '_aa_del.csv', index_col=0, parse_dates=True)
#
#     # plot min for initial strategy
#     plt.plot(df_initial['Min'])
#
#     # plot min for intermediate strategy
#     plt.plot(df_intermediate['Min'])
#
#     # plot min for robust strategy
#     plt.plot(df_robust['Min'])
#
#     plt.title('Minimums of GW level deltas for ' + layer + ' layer')
#     plt.xlabel('Year')
#     plt.ylabel('Groundwater level deltas, ft')
#     plt.legend(['Initial', 'Intermediate', 'Robust'])
#
#     plt.savefig('Data/Annual_averages/Figures/' + layer + '_compare_strategies_del_mins.png')
#     plt.clf()
#     return


strategies = ['Baseline', 'Initial', 'Intermediate', 'Robust']

for strategy in tqdm(strategies, desc='Plotting results (strategies)'):
    compare_layers(strategy)

layers = ['confined', 'unconfined', 'average']
for layer in tqdm(layers, desc='Plotting results (layers)'):
    compare_strategies(layer)
    del_compare_strategies(layer)

combine_all()
