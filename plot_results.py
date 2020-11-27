import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import ks_2samp


if __name__ == '__main__':

    results = pd.read_csv("metrics_output.csv", index_col="slide_name")
    metrics = results.columns
    metadata = pd.read_csv("metadata.csv", index_col="SlideID", usecols=["SlideID", "CancerType", "gender",
                                                                         "tumor_stage", "Diagnosis_Age_Yrs", "vital_status"])

    results = results.join(metadata)

    alive = results[results['vital_status']=='alive']
    dead = results[results['vital_status']=='dead']

    for metric in metrics:
        _, pvalue = ks_2samp(alive[metric].values, dead[metric].values)
        print(metric, pvalue)

    marker = "vital_status"

    plot_data = pd.melt(results, id_vars=marker, value_vars=metrics, var_name='metrics')

    #f = sns.FacetGrid(plot_data, col="metrics", sharey=False)
    #f.map(sns.violinplot, "gender", "value")
    sns.catplot(data=plot_data, x=marker, y="value", col="metrics", sharey=False, kind="point")
    plt.show()