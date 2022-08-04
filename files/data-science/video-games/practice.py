# import the pandas package
# note that this was specified as a project
# dependency in the pyproject.toml file
import pandas
# import matplotlib
import pathlib

DATASET_PATH = pathlib.Path(r"C:\\Users\\saket\\research-paper-template-saket\\files\\data-science\\video-games\\GamingStudy_data.csv")
validation_data = pandas.read_csv(DATASET_PATH)
df = validation_data

categories = ['GAD1', 'GAD2', 'GAD3', 'GAD4', 'GAD5', 'GAD6', 'GAD7', 'GADE', 'SWL1', 'SWL2', 'SWL3', 'SWL4', 'SWL5', 
              'Game', 'Platform', 'Hours', 'earnings', 'whyplay', 'League', 'highestleague', 'streams', 
              'SPIN1', 'SPIN2', 'SPIN3', 'SPIN4', 'SPIN5', 'SPIN6', 'SPIN7', 'SPIN8', 'SPIN9', 'SPIN10', 'SPIN11', 'SPIN12', 'SPIN13', 'SPIN14', 'SPIN15', 'SPIN16', 'SPIN17', 
              'Narcissism', 'Gender', 'Age', 'Work', 'Degree', 'Birthplace', 'Residence', 'Reference', 'Playstyle', 'accept', 'GAD_T', 'SWL_T', 'SPIN_T', 
              'Residence_ISO3', 'Birthplace_ISO3']



## SUMMARY STATISTICS FOR ALL GAD --> START

# measures of central tendency
gad_means = []
gad_medians = []
gad_modes = []

for i in range(1, 8):
    gad_means.append(df[f"GAD{i}"].mean())

for i in range(1, 8):
    gad_medians.append(df[f"GAD{i}"].median())

for i in range(1, 8):
    gad_modes.append(df[f"GAD{i}"].mode())


# measures of spread
gad_stds = []
gad_range = []
gad_iqr = []

for i in range(1, 8):
    gad_stds.append(df[f"GAD{i}"].std())

for i in range(1, 8):
    q1 = df[f"GAD{i}".quantile(0.25)]
    q3 = df[f"GAD{i}".quantile(0.75)]

    gad_iqr.append(q3 - q1)

for i in range(1, 8):
    max_ = df[f"GAD{i}".max()]
    min_ = df[f"GAD{i}".min()]
    
    range_ = max_ - min_

    gad_range.append(range_)

print(gad_iqr)
print(gad_means)
print(gad_medians)
print(gad_modes)
print(gad_range)
print(gad_stds)
