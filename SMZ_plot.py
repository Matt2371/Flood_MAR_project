import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm


class SMZPlot:
    # layer = 'unconfined'/'confined'/'average', smz='DAC'/'SUB'/'GWD'/''. '' means basin wide (no smz applied)
    def __init__(self, layer, smz='', deltas=True):
        # dictionary mapping special management zone (smz) folder name. '' means no smz applied
        zone = {'DAC': 'DAC', 'GWD': 'GWDZones', 'SUB':'Subsidence'}

        self.smz = smz
        self.deltas = deltas
        self.layer = layer

        if not deltas:
            # assign annual average dataframes for each Flood-MAR strategy
            self.df_baseline = pd.read_csv('Data/Annual_averages/' + zone[smz] + '/Baseline_GW_' + layer + '_aa_' + smz
                                           + '.csv', index_col=0, parse_dates=True)
            self.df_initial = pd.read_csv('Data/Annual_averages/' + zone[smz] + '/Initial_GW_' + layer + '_aa_' + smz
                                          + '.csv', index_col=0, parse_dates=True)
            self.df_intermediate = pd.read_csv('Data/Annual_averages/' + zone[smz] + '/Intermediate_GW_' + layer +
                                               '_aa_' + smz + '.csv', index_col=0, parse_dates=True)
            self.df_robust = pd.read_csv('Data/Annual_averages/' + zone[smz] + '/Robust_GW_' + layer + '_aa_' + smz +
                                         '.csv', index_col=0, parse_dates=True)
        else:
            # assign annual average dataframes for each Flood-MAR strategy RELATIVE TO BASELINE
            self.df_initial = pd.read_csv('Data/Annual_averages/' + zone[smz] + '/Deltas/Initial_GW_' + layer + '_aa_'
                                          + smz + '_del.csv', index_col=0, parse_dates=True)
            self.df_intermediate = pd.read_csv('Data/Annual_averages/' + zone[smz] + '/Deltas/Intermediate_GW_' + layer
                                               + '_aa_' + smz + '_del.csv', index_col=0, parse_dates=True)
            self.df_robust = pd.read_csv('Data/Annual_averages/' + zone[smz] + '/Deltas/Robust_GW_' + layer + '_aa_' +
                                         smz + '_del.csv', index_col=0, parse_dates=True)

    # plot to compare different strategies, DO NOT PLOT BASELINE if DELTAS = TRUE
    def compare_strategies(self):
        # dictionary mapping special management zone (smz) folder name. '' means no smz applied
        zone = {'DAC': 'DAC', 'GWD': 'GWDZones', 'SUB':'Subsidence'}
        smz = self.smz

        # plotting routing for non-deltas
        if not self.deltas:
            # plot to compare strategies
            plt.plot(self.df_baseline[smz + '_AVERAGE'], color='#610345')
            plt.plot(self.df_initial[smz + '_AVERAGE'], color='#5773FF')
            plt.plot(self.df_intermediate[smz + '_AVERAGE'], color='#00D19D')
            plt.plot(self.df_robust[smz + '_AVERAGE'], color='#9B7874')

            plt.xlabel('Year')
            plt.ylabel('Groundwater Level, ft')
            plt.legend(['Baseline', 'Initial', 'Intermediate', 'Robust'])
            plt.title('Average annual GW: ' + self.layer + ' layer under' + smz + 's')
            plt.savefig('Data/Annual_averages/' + zone[smz] + '/Figures/' + smz + '_' + self.layer +
                        '_compare_strategies.png')
            plt.clf()

        # plot for deltas
        else:
            # plot to compare strategies
            plt.plot(self.df_initial[smz + '_AVERAGE'], color='#5773FF')
            plt.plot(self.df_intermediate[smz + '_AVERAGE'], color='#00D19D')
            plt.plot(self.df_robust[smz + '_AVERAGE'], color='#9B7874')

            plt.xlabel('Year')
            plt.ylabel('Groundwater Level Deltas, ft')
            plt.legend(['Initial', 'Intermediate', 'Robust'])
            plt.title('Average annual GW relative to Baseline: ' + self.layer + ' layer under' + smz + 's')
            plt.savefig('Data/Annual_averages/' + zone[smz] + '/Figures/' + smz + '_' + self.layer +
                        '_compare_strategies_del.png')
            plt.clf()

        return

    def boxplot(self, strategy):
        # dictionary mapping special management zone (smz) folder name. '' means no smz applied
        zone = {'DAC': 'DAC', 'GWD': 'GWDZones', 'SUB':'Subsidence'}
        smz = self.smz

        # create boxplot for non-delas
        if not self.deltas:
            df = pd.read_csv('Data/Annual_averages/' + zone[self.smz] + '/' + strategy + '_GW_' + self.layer + '_aa_' +
                             self.smz + '.csv', index_col=0, parse_dates=True)
            # show only year in index
            df.index = df.index.year
            # remove basin average column
            df.drop(smz + '_AVERAGE', axis=1)
            # take last 10 years
            df = df.tail(10)

            # create boxplot
            df.T.plot.box(showfliers=False)
            plt.ylabel('Groundwater level, ft')
            plt.xlabel('Year')
            plt.title('GW level under' + smz + 'zones: ' + strategy.lower() + ' strategy ' + self.layer.lower() +
                      ' layer')
            plt.savefig('Data/Annual_averages/' + zone[smz] + '/Figures/' + smz + '_' + strategy + '_GW_' +
                        self.layer + '_aa_boxplot.png')
            plt.clf()

        # create boxplots for deltas RELATIVE TO BASELINE
        else:
            df = pd.read_csv('Data/Annual_averages/' + zone[self.smz] + '/Deltas/' + strategy + '_GW_' + self.layer +
                             '_aa_' + self.smz + '_del.csv', index_col=0, parse_dates=True)
            # show only year in index
            df.index = df.index.year
            # remove basin average column
            df.drop(smz + '_AVERAGE', axis=1)
            # take last 10 years
            df = df.tail(10)

            # create boxplot
            df.T.plot.box(showfliers=False)
            plt.ylabel('Groundwater level Deltas, ft')
            plt.xlabel('Year')
            plt.title('GW deltas under' + smz + 'zones: ' + strategy.lower() + ' strategy ' + self.layer.lower() +
                      ' layer')
            plt.savefig(
                'Data/Annual_averages/' + zone[smz] + '/Figures/' + smz + '_' + strategy + '_GW_' + self.layer +
                '_aa_del_boxplot.png')

            plt.clf()
        return


layers = ['confined', 'unconfined', 'average']
strategies = ['Baseline', 'Initial', 'Intermediate', 'Robust']
smzs = ['DAC', 'SUB', 'GWD']

for smz in tqdm(smzs, desc='Creating plots: '):
    for layer in layers:
        # create plots for non-deltas
        Object = SMZPlot(layer, smz, deltas=False)
        Object.compare_strategies()

        # create plots for deltas
        Object = SMZPlot(layer, smz, deltas=True)
        Object.compare_strategies()

        for strategy in strategies:
            # create boxplots for non-deltas
            Object = SMZPlot(layer, smz, deltas=False)
            Object.boxplot(strategy)

            # create boxplots for deltas
            if strategy == 'Baseline':
                continue
            Object = SMZPlot(layer, smz, deltas=True)
            Object.boxplot(strategy)
