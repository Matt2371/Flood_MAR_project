import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np


# FOR BASIN_WIDE DELTAS: plot differences between strategies for each layer, ANNUAL AVERAGE
# layer, str = ['confined', 'unconfined', 'average']
def del_compare_strategies(layer='confined'):
    df_initial = pd.read_csv('Data/Annual_averages/Deltas/Initial_GW_' + layer + '_aa_del.csv', index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/Deltas/Intermediate_GW_' + layer + '_aa_del.csv', index_col=0,
                                  parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/Deltas/Robust_GW_' + layer + '_aa_del.csv', index_col=0,
                            parse_dates=True)

    fig, ax = plt.subplots(figsize=(8, 5))

    # plot to compare strategies
    ax.plot(df_initial['BASIN_AVERAGE'], color='#5773FF', lw=4)
    ax.plot(df_intermediate['BASIN_AVERAGE'], color='#00D19D', lw=4)
    ax.plot(df_robust['BASIN_AVERAGE'], color='#9B7874', lw=4)

    plt.xlabel('Year', fontsize='x-large')
    plt.ylabel('Groundwater Level Deltas, ft', fontsize='x-large')
    plt.xticks(fontsize='x-large')
    plt.yticks(fontsize='x-large')
    # plt.title('Basin-wide annual average GW relative to Baseline: ' + layer + ' layer')
    plt.legend(['Initial', 'Intermediate', 'Robust'], fontsize='xx-large')
    plt.tight_layout()
    plt.savefig('Poster_figures/hires_confined_compare_strategies_del.png', dpi=600)
    # plt.show()
    plt.clf()

    return


# FOR LAST 10 YEARS OF SIMULATION: create boxplot of basin-wide distribution, ANNUAL AVERAGE
def basin_boxplot(strategy='Baseline', layer='confined'):
    df = pd.read_csv('Data/Annual_averages/' + strategy + '_GW_' + layer + '_annual_avg.csv',
                     index_col=0,
                     parse_dates=True)
    # show only year in index
    df.index = df.index.year
    # remove basin average column
    df.drop('BASIN_AVERAGE', axis=1)
    # take last 10 years
    df = df.tail(10)

    # create boxplot
    fig, ax = plt.subplots(figsize=(12,5))
    bp = ax.boxplot(df.T, showfliers=False)
    for box in bp['boxes']: box.set(linewidth=3)
    for cap in bp['caps']: cap.set(linewidth=3)
    for whisker in bp['whiskers']: whisker.set(linewidth=3)
    for median in bp['medians']: median.set(linewidth=3, c='b')

    # plt.title('GW level, all elements: ' + strategy.lower() + ' strategy ' + layer.lower() + ' layer')
    plt.ylabel('Groundwater level, ft', fontsize='x-large')
    plt.xlabel('Year', fontsize='x-large')
    plt.xticks(fontsize='x-large', ticks = np.arange(1,11), labels=df.index.to_list())
    plt.yticks(fontsize='x-large')
    plt.tight_layout()
    plt.savefig('Poster_figures/hires_' + strategy + '_GW_' + layer + '_aa_boxplot.png', dpi=600)
    plt.clf()
    return


# FOR DELTAS UNDER DAC ELEMENTS: plot differences between strategies for each layer, ANNUAL AVERAGE
# layer, str = ['confined', 'unconfined', 'average']
def dac_del_compare_strategies(layer='confined'):
    df_initial = pd.read_csv('Data/Annual_averages/DAC/Deltas/Initial_GW_' + layer + '_aa_DAC_del.csv', index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/DAC/Deltas/Intermediate_GW_' + layer + '_aa_DAC_del.csv',
                                  index_col=0, parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/DAC/Deltas/Robust_GW_' + layer + '_aa_DAC_del.csv', index_col=0,
                            parse_dates=True)

    # plot to compare strategies
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df_initial['DAC_AVERAGE'], color='#5773FF', lw=4)
    ax.plot(df_intermediate['DAC_AVERAGE'], color='#00D19D', lw=4)
    ax.plot(df_robust['DAC_AVERAGE'], color='#9B7874', lw=4)

    plt.xlabel('Year', fontsize='x-large')
    plt.ylabel('Groundwater Level Deltas, ft', fontsize='x-large')
    # plt.title('Average annual GW relative to Baseline: ' + layer + ' layer under DACs')
    plt.legend(['Initial', 'Intermediate', 'Robust'], fontsize='xx-large')
    plt.xticks(fontsize='x-large')
    plt.yticks(fontsize='x-large')
    plt.tight_layout()
    plt.savefig('Poster_figures/hires_DAC_' + layer + '_compare_strategies_del.png', dpi=600)
    plt.clf()

    return


# FOR DELTAS UNDER GWD ELEMENTS: plot differences between strategies for each layer, ANNUAL AVERAGE
# layer, str = ['confined', 'unconfined', 'average']
def gwd_del_compare_strategies(layer='confined'):
    df_initial = pd.read_csv('Data/Annual_averages/GWDZones/Deltas/Initial_GW_' + layer + '_aa_GWD_del.csv',
                             index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/GWDZones/Deltas/Intermediate_GW_' + layer + '_aa_GWD_del.csv',
                                  index_col=0, parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/GWDZones/Deltas/Robust_GW_' + layer + '_aa_GWD_del.csv', index_col=0,
                            parse_dates=True)

    # plot to compare strategies
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df_initial['GWD_AVERAGE'], color='#5773FF', lw=4)
    ax.plot(df_intermediate['GWD_AVERAGE'], color='#00D19D', lw=4)
    ax.plot(df_robust['GWD_AVERAGE'], color='#9B7874', lw=4)

    plt.xlabel('Year', fontsize='x-large')
    plt.ylabel('Groundwater Level Deltas, ft', fontsize='x-large')
    # plt.title('Average annual GW relative to Baseline: ' + layer + ' layer under GWDs')
    plt.legend(['Initial', 'Intermediate', 'Robust'], fontsize='xx-large')
    plt.xticks(fontsize='x-large')
    plt.yticks(fontsize='x-large')
    plt.tight_layout()
    plt.savefig('Poster_figures/hires_GWD_' + layer + '_compare_strategies_del.png', dpi=600)
    plt.clf()

    return


# FOR DELTAS UNDER SUBSIDENCE ELEMENTS: plot differences between strategies for each layer, ANNUAL AVERAGE
# layer, str = ['confined', 'unconfined', 'average']
def sub_del_compare_strategies(layer='confined'):
    df_initial = pd.read_csv('Data/Annual_averages/Subsidence/Deltas/Initial_GW_' + layer + '_aa_SUB_del.csv',
                             index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/Subsidence/Deltas/Intermediate_GW_' + layer + '_aa_SUB_del.csv',
                                  index_col=0, parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/Subsidence/Deltas/Robust_GW_' + layer + '_aa_SUB_del.csv',
                            index_col=0,
                            parse_dates=True)

    # plot to compare strategies
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df_initial['SUB_AVERAGE'], color='#5773FF', lw=4)
    ax.plot(df_intermediate['SUB_AVERAGE'], color='#00D19D', lw=4)
    ax.plot(df_robust['SUB_AVERAGE'], color='#9B7874', lw=4)

    plt.xlabel('Year', fontsize='x-large')
    plt.ylabel('Groundwater Level Deltas, ft', fontsize='x-large')
    # plt.title('Annual GW relative to Baseline: ' + layer + ' layer under subsidence areas')
    plt.legend(['Initial', 'Intermediate', 'Robust'], fontsize='xx-large')
    plt.xticks(fontsize='x-large')
    plt.yticks(fontsize='x-large')
    plt.tight_layout()
    plt.savefig('Poster_figures/SUB_' + layer + '_compare_strategies_del.png', dpi=600)
    plt.clf()

    return


# strategies = ['Baseline', 'Initial', 'Intermediate', 'Robust']
#
# layers = ['confined', 'unconfined', 'average']
# for layer in tqdm(layers, desc='Plotting results (layers)'):
#     del_compare_strategies(layer)
#     dac_del_compare_strategies(layer)
#     gwd_del_compare_strategies(layer)
#
# # create boxplots
# for strategy in tqdm(strategies, desc='creating boxplots'):
#     for layer in layers:
#         basin_boxplot(strategy, layer)
#
# # subregion list
# sub_list = ['SR1', 'SR2', 'SR3']
#
# for subregion in sub_list:
#     pumping_cost(subregion)

del_compare_strategies()
dac_del_compare_strategies()
gwd_del_compare_strategies()
sub_del_compare_strategies()
basin_boxplot()
