import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_theme(context="paper", style="ticks")

from scipy.stats import ks_2samp


def plot_vital_status(data, output_path, statistics):

    alive = data[data['vital_status']=='alive']
    dead = data[data['vital_status']=='dead']

    significant_statistics = []
    pvalues = []

    for metric in statistics:
        _, pvalue = ks_2samp(alive[metric].values, dead[metric].values)
        if pvalue < 0.01:
            significant_statistics.append(metric)
            pvalues.append(pvalue)

    titles = []
    for i in range(0,len(significant_statistics)):
        titles.append(f'{significant_statistics[i]}, p={pvalues[i]:.3f}')

    plot_data = pd.melt(data, id_vars="vital_status", value_vars=significant_statistics, var_name='metrics')

    g = sns.catplot(data=plot_data, x="vital_status", y="value", sharex=False, col="metrics",col_wrap=3,
                    sharey=False, kind="point", linestyles=["--"], capsize=.2, color='black')
    for ax, title in zip(g.axes.flat, titles):
        ax.set_title(title, fontsize=15)
    g.set_xlabels("")
    g.set_ylabels("")
    plt.subplots_adjust(top=0.9)
    g.fig.suptitle("Significant differences of the graph metrics by survival", fontsize=30)
    plt.savefig(output_path, dpi=200)


def plot_gender(data, output_path, statistics):

    male = data[data['gender']=='Male']
    female = data[data['gender']=='Female']

    significant_statistics = []
    pvalues = []

    for metric in statistics:
        _, pvalue = ks_2samp(male[metric].values, female[metric].values)
        if pvalue < 0.01:
            significant_statistics.append(metric)
            pvalues.append(pvalue)

    titles = []
    for i in range(0,len(significant_statistics)):
        titles.append(f'{significant_statistics[i]}, p={pvalues[i]:.3f}')

    plot_data = pd.melt(data, id_vars="gender", value_vars=significant_statistics, var_name='metrics')

    g = sns.catplot(data=plot_data, x="gender", y="value", sharex=False, col="metrics",col_wrap=3,
                    sharey=False, kind="point", linestyles=["--"],capsize=.2, color='black')
    for ax, title in zip(g.axes.flat, titles):
        ax.set_title(title, fontsize=15)
    g.set_xlabels("")
    g.set_ylabels("")
    plt.subplots_adjust(top=0.9)
    g.fig.suptitle("Significant differences of the graph metrics by gender", fontsize=30)
    plt.savefig(output_path, dpi=200)


if __name__ == '__main__':

    results = pd.read_csv("metrics_output_additional.csv", index_col="slide_name")
    metrics = results.columns.to_list()
    metadata = pd.read_csv("metadata.csv", index_col="SlideID", usecols=["SlideID", "CancerType", "gender",
                                                                         "tumor_stage", "Diagnosis_Age_Yrs", "vital_status"])

    results = results.join(metadata)

    plot_vital_status(results, 'results/vital_status.png', metrics)
    plot_gender(results, 'results/gender.png', metrics)
