import pandas as pd

google = pd.read_csv('job_skills.csv')

print('-------------- dataset description  --------------------')
print(google.describe())