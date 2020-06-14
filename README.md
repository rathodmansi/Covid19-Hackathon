# Covid19-Hackathon

The Covid-19 pandemic has clutched the entire world for as long as 7 months. This has caused unprecedented damages socially and economically all over the world. 
With the entire force of world leaders and health workers working towards it, there still exist a lot of untested domains. In our efforts to combat this fight, we have selected one particular area and worked to generate insights.

## Problem Statement

We aim to understand how weather changes (more specifically air temperature) influence the rate of infection (R0). We know other coronaviruses like SARS have better stability at lower temperatures (source), but higher temperatures can increase social contact.
For our hypothesis testing, we have considered only King County-level data. The reason for this is that our hypothesis requires localized county level case data, which is lacking.
The case numbers are heavily dependent on government interventions, so we narrowed down out study time frame to only the lockdown period.

## Input Data

- [Seattle Weather Data](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00024233/detail): This dataset is accessed through the weather API and contains daily minimum and maximum temperature

- [King County COVID-19 Dashboard ](https://kingcounty.gov/depts/health/covid-19/data.aspx). This dataset is available through King County, and contains New Cases, Total Tests and Positive Percentages.

## Project Reproducibility
- This hypothesis should be tested for multiple counties all around the world. We would expect counties with similar geography and weather to have similar trend lines in positive percentages.

- Reproducing this test in other counties where there is relaible data  will let us be more confident on which one is closest to the true effects of temperature on transmission 

## Methodology & Metrics

The ideal metric to gauge the growth of the epidemic in a given county would be Rt or the adjusted reproduction rate for the virus. However, access to county level reproduction rate is not accessible as of now, and even the state Rt levels are crude estimates that are not robust enough to account for highly variable testing capacities and targets.
So, the next best metric would be New Percentage Positive (NPP) which represents the fraction of positive antigen test results from all the tests conducted on a specific date. To further insulate from noise caused by testing capacities and temperature anomalies, we used the mean daytime temperature for a given week and compared it to the mean NPP over the following week. This assumes that a newly contracted virus takes one week to show up on the King county case tally.

## Result 

Below are our observations: 

![](https://github.com/rathodmansi/Covid19-Hackathon/blob/master/results/Scatter-Avgs.png)

<b> Pearson Coefficient:</b> -0.6175

![](https://github.com/rathodmansi/Covid19-Hackathon/blob/master/results/Scatter.png)

<b> Pearson Coefficient:</b> -0.4602


## Conclusion & Possible Explanations

We saw a weak correlation that showed a decrease in the NPP following a week of higher temperatures. This initially seems to confirm retrospective studies of the SARS outbreak. However, there is still no clear trend, which could in part be because of:

- Weather does not play a significant role in the change of positive percentage 
- Weather does have a correlation but the other confounding variables play a larger role and and the weather variability is lost
- The data being generated now is not granular enough to assess the true temperature effects
- The change in temperature creates both positive and negative feedback in NPP  that negate each other


## Software used
Python version 3.7  
R version 3.5.3


