PURPOSE:

Analyze 100 year simulation of groundwater (GW) levels for 4 Flood_MAR strategies and 6466 simulation elements to select the strategy with the best improvement in:
1. Basin-wide water supply
2. GW supply to disadvantaged communities (DAC's)
3. GW supply to groundwater-dependent communities (GWD's)
4. GW recharge under subsidence zones
5. Pumping costs under SR1, SR2, and SR3 zones (as defined by the Department of Water Resources)

INCLUDED SCRIPTS:

process_csv.py: *RUN FIRST TO GET NECESSARY FILES* Seperates layer type from data, calculates annual averages, cuts out special management zones
calculates deltas (Groundwater level relative to baseline scenario), and creates tables of descriptive statistics. Exports csv's
initial_analysis.py: make plots comparings strategies and boxplots of BASIN-WIDE time evolution of GW levels for deltas and non-deltas
SMZ_plot.py : object-oreinted approach for plots comparing strategies and boxplots for both deltas and non-deltas

GWL_Econ.py: estimate timeseries of pumping costs under SR1/SR2/SR3. Use current hydrograph, ignoring climate change predictions
- Use pumping power equation: specific weight * flow rate * hydraulic head / pump efficiency
- Assume 13.59 cents/kWh: https://findenergy.com/providers/merced-irrigation-district/
- Assume 80% pump efficiency
- Distance to water data (hydraulic head) given by DWR
- Calculate cost to pump at 1 m3/s for 1 hour
pumping_cost(subregion, Q=1, nu=0.8), export and plot timeseires of pumping cost (savings relative to Baseline) given subregion

* archived * DACs.py: compare Flood-MAR strategies under DAC's
* archived * subsidence.py: compare Flood-MAR strategies under subsidence zones
* archived * GWDs.py: compare Flood-MAR strategies under GWD zones



DEFINITION OF TERMS/FILENAMING CONVENTION:
"special management zone" / "SMZ" - model elements delineated by DWR in reference to a particular objective
"Grounwater dependent zone" / "GWDZone" / "GWD" 
"Disadvantaged Community" / "DAC"
"Subsidence zone" / "SUB" - elements with high subsidence risk
"annual average" / "aa" - monthly data (orignial) averaged by water year (OCT to OCT), temporal average
"basin average" / "*SMZ* average" - time evolution of spatail averages for elements under special management zone(DAC/SUB/GWD) or basin wide
"baseline delta" / "del" - GW level change relative to the baseline
"layer type" - refers to the location of recharge (unconfined/confined/average)
"unconfined" / "uc" - GW levels in unconfined layer
"confined" / "c" - GW levels in confined layer
"average" / "a" - average GW levels in unconfined/confined layer
"SR1" / "SR2" / "SR3" - subregions delineated by DWR to compare pumping costs
"flow rate" / "Q" - pump flow rate
"pump efficiency" / "nu" - pump efficiency


PROJECT FOLDER CONTENTS:
Data/ - given groundwater level data from DWR
Data/Separated/ - given GW level data separated into lyaer type: unconfined/confined/average csv's
Data/Annual_Averages/ - csv's of annually-averaged data (OCT-OCT) from separated data csv's (all elements)
Data/Annual_Averages/Deltas/ - csv's of GW data RELATIVE to baseline scenario
Data/Annual_Averages/Figures/ - plots from initial analysis, time evolution of GW level for each strategy, etc..
Data/Annual_Averages/Distiributions/ - timeseries of basin-wide descriptive statistics: min/max/stdv/mean
Data/Annual_Averages/DAC/ - csv's of annual averaged GW level for DAC elements
Data/Annual_Averages/DAC/Deltas/ - csv's of annual averaged GW level for DAC elements RELATIVE to baseline scenario
Data/Annual_Averages/DAC/Distributions/ - timeseries descriptive statistics: min/max/stdv/mean for DAC elements
Data/Annual_Averages/DAC/Figures/ - Figures for the DAC analysis
Data/Annual_Averages/Subsidence/ - csv's of annual averaged GW level for subsidence elements
Data/Annual_Averages/Subsidence/Deltas/ - csv's of annual averaged GW level for subsidence elements RELATIVE to baseline scenario
Data/Annual_Averages/Subsidence/Distributions/ - timeseries descriptive statistics: min/max/stdv/mean for subsidence elements
Data/Annual_Averages/Subsidence/Figures/ - Figures for the subsidence analysis
Data/Annual_Averages/GWDZones/ - csv's of annual averaged GW level for GWD elements
Data/Annual_Averages/GWDZones/Deltas/ - csv's of annual averaged GW level for GWD elements RELATIVE to baseline scenario
Data/Annual_Averages/GWDZones/Distributions/ - timeseries descriptive statistics: min/max/stdv/mean for GWD elements
Data/Annual_Averages/GWDZones/Figures/ - Figures for the GWD analysis
Data/GWL_Econ/ - Given distance to water data (csv) for SR1/SR2/SR3 subregions
Data/GWL_Econ/pumping_cost/ - csv's of pumping cost for each subregion
Data/GWL_Econ/Figures/ - plots of pumping cost analysis





