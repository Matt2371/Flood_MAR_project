import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


# for given layer, plot differences (annual average GW level under all DACs) between strategies
def dac_compare_strategies(Layer):
    # read dac_cut csv's
    df_baseline = pd.read_csv('Data/Annual_averages/DAC/Baseline_GW_' + Layer + '_aa_DAC.csv', index_col=0,
                              parse_dates=True)
    df_initial = pd.read_csv('Data/Annual_averages/DAC/Initial_GW_' + Layer + '_aa_DAC.csv', index_col=0,
                             parse_dates=True)
    df_intermediate = pd.read_csv('Data/Annual_averages/DAC/Intermediate_GW_' + Layer + '_aa_DAC.csv', index_col=0,
                                  parse_dates=True)
    df_robust = pd.read_csv('Data/Annual_averages/DAC/Robust_GW_' + Layer + '_aa_DAC.csv', index_col=0,
                            parse_dates=True)

    # plot to compare strategies
    plt.plot(df_baseline['DAC_AVERAGE'])
    plt.plot(df_initial['DAC_AVERAGE'])
    plt.plot(df_intermediate['DAC_AVERAGE'])
    plt.plot(df_robust['DAC_AVERAGE'])

    plt.xlabel('Year')
    plt.ylabel('Groundwater Level, ft')
    plt.title('Average annual GW: ' + Layer + ' layer under DAC\'s')
    plt.legend(['Baseline', 'Initial', 'Intermediate', 'Robust'])

    plt.savefig('Data/Annual_averages/DAC/Figures/DAC_' + Layer + '_compare_strategies.png')
    plt.clf()

    return


# Plot results
layers = ['confined', 'unconfined', 'average']
for layer in tqdm(layers, desc='Exporting results (layers):'):
    dac_compare_strategies(layer)
