from lifelines.statistics import logrank_test
import pandas as pd

data_A = pd.read_csv('csv/3,0_test.csv',  delimiter=',')
data_B = pd.read_csv('csv/2,0_test.csv', delimiter=',')

results = logrank_test(data_A["smr"], data_B["smr"], data_A["surv"], data_B["surv"])
results.print_summary()
