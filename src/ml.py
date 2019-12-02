import wandb
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from joblib import dump
from datetime import date

# initialize wandb
wandb.init(project='my-awesome-project')

# set and save hyperparameters
# wandb.config is a variable that holds and saves hyperparameters and inputs
wandb.config.penalty = 'l1' # l1 for sparse matrix
wandb.config.C = 1 # penalty for the error term
wandb.config.test_size = 0.3 # proportion for test set
wandb.config.seed = 100 # random seed for reproducibility

# import dataset
tech = pd.read_csv('../data/mental_health_tech_data_post.csv')
 
# split training and testing data
X = tech.drop(['treatment'], axis=1)
y = tech['treatment']

X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=wandb.config.test_size, 
    random_state=wandb.config.seed)

# transform features to dummy variables
cat_cols = X_train.columns # get col names

# create one-hot encoder object to transform all features at once
def preprocessor():
    preprocessor = ColumnTransformer([  
        ("one_hot", OneHotEncoder(sparse=False, handle_unknown='ignore'), cat_cols)
        ]) 
    return preprocessor

# fit and save preprocessor
transform = preprocessor().fit(X_train)

# one-hot encode for training and testing
X_train_transform = transform.transform(X_train)
X_test_transform = transform.transform(X_test)

# fit model
LogR = LogisticRegression(penalty=wandb.config.penalty, 
                          C=wandb.config.C,
                          random_state=wandb.config.seed)
LogR.fit(X_train_transform, y_train.values.ravel())

# save metrics to wand
wandb.log({"Train Accuracy": LogR.score(X_train_transform, y_train.values.ravel()),
           "Test Accuracy":LogR.score(X_test_transform, y_test.values.ravel())})

# save model 
filepath = '../results/'
date_stamp = date.today().strftime('%Y-%b-%d')

dump(LogR, f'{filepath}/linear_regression_{date_stamp}.joblib')