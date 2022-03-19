PURPOSE:

Analyze 100 year simulation of groundwater (GW) levels for 4 Flood_MAR strategies and 6466 simulation elements to select the strategy with the best improvement in:
1. Basin-wide water supply
2. GW supply to disadvantaged communities (DAC's)
3. Distance to GW table for GW dependent ecosystems (is the GW table within reach of the max rooting depth, 30ft?)

INCLUDED SCRIPTS:

process_csv.py: *RUN FIRST TO GET NECESSARY FILES*
separate_csv(strategy), separates layer type (confined/unconfined/average) from given data and exports into 3 separate csv's
annual_average(strategy, layer), takes water year average (OCT-OCT) from separated data (see above) given the strategy and layer
dac_cut(strategy, layer), cuts DAC elements out of annual averaged data (see above) and exports as new csv's given the strategy and layer
deltas(strategy, layer), calculates differences of GW level relative to Baseline for each strategy

initial_analysis.py: make plots/tables of basin-wide time evolution of GW levels
compare_layers(strategy), plot each layer type for given strategy (reads annual average results)
compare_strategies(layer), plot each strategy for given layer type(reads annual average results)
** Planned **
Plot deltas of each strategy compared to baseline
Generate table of min/max/average/std at simulation end (or other years) to study distribution of GW levels for each strategy

DACs.py: compare Flood-MAR strategies under DAC's
dac_compare_strategies(layer), plot each strategy for given layer (under DAC's)
** Planned **
Plot deltas of each strategy compared to baseline
Generate table of min/max/average/std at simulation end (or other years) to study distribution of GW levels for each strategy

GW_ecosystems.py:
** Planned **
Find distance to GW table given element elevation under GWD ecosystems


DEFINITION OF TERMS/FILENAMING CONVENTION:
"annual average" / "aa" - monthly data (orignial) averaged by water year (OCT to OCT), temporal average
"basin average" / "DAC average" - time evolution of averages for all elements under identified zone (basin-wide/DAC), spatial average
"baseline delta" / "del" - GW level change relative to the baseline
"layer type" - refers to the location of recharge (unconfined/confined/average)
"unconfined" / "uc" - GW levels in unconfined layer
"confined" / "c" - GW levels in confined layer
"average" / "a" - average GW levels in unconfined/confined layer

PROJECT FOLDER CONTENTS:
Data/ - given groundwater level data from DWR
Data/Separated/ - given GW level data separated into lyaer type: unconfined/confined/average csv's
Data/Annual_Averages/ - csv's of annually-averaged data (OCT-OCT) from separated data csv's (all elements)
Data/Annual_Averages/Figures/ - plots from initial analysis, time evolution of GW level for each strategy, etc..
Data/Annual_Averages/DAC/ - csv's of annual averaged GW level for DAC elements
Data/Annual_Averages/DAC/Figures/ - Figures for the DAC analysis
Data/Annual_Averages/Deltas/ - csv's of GW data RELATIVE to baseline scenario





