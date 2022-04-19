import pandas as pd
import matplotlib.pyplot as plt


## PURPOSE: Analyze cost of groundwater pumping given hydraulic head (depth to water)
## COMPARE AT Q=1m3/s
## ASSUME PUMPING COST: 13.59 cents per kWhr (MID average commercial price:
# https://findenergy.com/providers/merced-irrigation-district/)


# Take g=9.81 m/s, density of water 1000 kg/m3, 1 ft = 0.3048 m

# Export and plot timeseires of pumping cost given subregion
# subregion, str: ['SR1', 'SR2', 'SR3'], Q (flow rate, m3), nu (pump efficiency)
def pumping_cost(subregion, Q=1, nu=0.8):
    # read distance to water data
    head_df = pd.read_csv('Data/GWL_Econ/' + subregion + '.csv', index_col=0, parse_dates=True)

    # create dataframe of pumping power [kW]
    # power_df = head_df [ft] * 0.3048 [m/ft] * 1000 [kg/m3] * 9.81 [m/s2] * Q [m3/s] / nu / 1000 [W/kW]
    power_df = head_df * 0.3048 * 9.81 * Q / nu

    # calculate cost of pumping 1 hour [USD]
    cost_df = power_df * 0.1359

    # export and plot
    cost_df.to_csv('Data/GWL_Econ/pumping_cost/' + subregion + '_pumping_cost.csv')
    # cost_df.plot(colormap='Set2')
    plt.plot(cost_df['Baseline'], color='#610345')
    plt.plot(cost_df['Initial'], color='#5773FF')
    plt.plot(cost_df['Intermediate'], color='#00D19D')
    plt.plot(cost_df['Robust'], color='#9B7874')

    plt.title('Cost of pumping at ' + str(Q) + ' $m^3/s$ for 1 hr for ' + subregion)
    plt.ylabel('Cost, USD')
    plt.xlabel('Year')
    plt.legend(['Baseline', 'Initial', 'Intermediate', 'Robust'])
    plt.savefig('Data/GWL_Econ/Figures/' + subregion + '_pumping_cost.png')
    plt.clf()

    return


# subregion list
sub_list = ['SR1', 'SR2', 'SR3']

for subregion in sub_list:
    pumping_cost(subregion)
