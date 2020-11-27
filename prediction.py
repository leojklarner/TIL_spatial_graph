import pandas as pd
from scipy.stats import ks_2samp
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline


def classify_vital_status(data, metrics):

    alive = data[data['vital_status'] == 'alive']
    dead = data[data['vital_status'] == 'dead']

    significant_statistics = []

    for metric in metrics:
        _, pvalue = ks_2samp(alive[metric].values, dead[metric].values)
        if pvalue < 0.01:
            significant_statistics.append(metric)

    labels = data['vital_status'].map({'alive': 1, 'dead': 0})
    features = data[significant_statistics].fillna(0)


    pipeline = Pipeline([('scaler', StandardScaler()), ('boost', SVC())])
    vital_status_score = cross_val_score(pipeline, features, labels, cv=10)
    return vital_status_score.mean()


def classify_gender(data, metrics):

    male = data[data['gender'] == 'Male']
    female = data[data['gender'] == 'Female']

    significant_statistics = []

    for metric in metrics:
        _, pvalue = ks_2samp(male[metric].values, female[metric].values)
        if pvalue < 0.01:
            significant_statistics.append(metric)

    labels = data['gender'].map({'Female': 1, 'Male': 0})
    features = data[significant_statistics].fillna(0)

    pipeline = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])
    vital_status_score = cross_val_score(pipeline, features, labels, cv=10)
    return vital_status_score.mean()

if __name__ == '__main__':

    results = pd.read_csv("metrics_output_additional.csv", index_col="slide_name")
    metrics = results.columns.to_list()
    metadata = pd.read_csv("metadata.csv", index_col="SlideID", usecols=["SlideID", "CancerType", "gender",
                                                                         "tumor_stage", "Diagnosis_Age_Yrs",
                                                                         "vital_status"])

    results = results.join(metadata)

    print(f'Accuracy vital status {classify_vital_status(results, metrics)}')

