# **Predicting Cancer Rates through Water Qualities**


Monitoring water quality is essential for human health. Although almost all drinking water in the United States is treated, EPA regulations for contaminants are often set higher than what is safe. This project attempts to predict cancer rates using the levels of chemicals in drinking water. The prediction algorithm can then be used to determine which chemicals are most toxic, and which EPA regulations might need to be set lower.  

Presentation of results here [HERE](https://docs.google.com/presentation/d/19mxmMdp2nW6TfFDIm3qp8yS9gvg0RnwA7YEnc0Dng-I/edit#slide=id.ge97a2c2489_1_11955)


**water_regression.py** contains code for building the ML model and predictions. **six_year_all_cancers_obesity_alcohol_smoking.csv** contains the final curated data set.



**Data**

Drinking water chemical data (2006-11) - https://www.epa.gov/dwsixyearreview/six-year-review-3-compliance-monitoring-data-2006-2011  
Cancer incidence by county (2013-2017) - https://gis.cancer.gov/canceratlas/tableview/?d=1&a=2&r=1&s=1   
Lifestyle (obesity, physical activity, alcohol) data by county (2011) - http://www.healthdata.org/us-health/data-download   
Smoking data by county (1996-2012) - http://ghdx.healthdata.org/record/ihme-data/united-states-smoking-prevalence-county-1996-2012  

Cancer and lifestyle data has been uploaded to the repository, EPA water data is available at the link above.
