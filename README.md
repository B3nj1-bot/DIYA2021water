# DIYA2021water
Code for DIYA 2021 Research Program - Predicting Cancer Rates through Water Qualities

Monitoring water quality is essential for human health. Although almost all drinking water in the United States is treated, EPA regulations for contaminants are often set higher than what is safe. This project attempts to predict cancer rates using the levels of chemicals in drinking water. The prediction algorithm can then be used to determine which chemicals are most toxic, and which EPA regulations might need to be set lower. 

DATA:
Drinking water chemical data (2006-11) - https://www.epa.gov/dwsixyearreview/six-year-review-3-compliance-monitoring-data-2006-2011
Cancer incidence by county (2013-2017) - https://gis.cancer.gov/canceratlas/tableview/?d=1&a=2&r=1&s=1
Lifestyle (obesity, physical activity, alcohol) data by county (2011) - http://www.healthdata.org/us-health/data-download
Smoking data by county (1996-2012) - http://ghdx.healthdata.org/record/ihme-data/united-states-smoking-prevalence-county-1996-2012

Cancer and lifestyle data has been uploaded to the repository, EPA water data is available at the link above.


water_regression.py is the main file used for building the machine learning model and for predictions.
