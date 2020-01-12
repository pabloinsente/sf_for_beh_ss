import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.regularizers import l2
import wandb
from wandb.keras import WandbCallback
from datetime import date

# logging code
wandb.init(project="my-awesome-project")
config = wandb.config # Config is a variable that holds and saves hyperparameters and inputs
config.epochs = 100
config.dropout = 0.2
config.test_size = 0.3
config.activation = 'relu'
config.optimizer = 'adam'
config.seed = 100
config.hidden_layer_size = 128

# import dataset
tech = pd.read_csv('../data/mental_health_tech_data_post.csv')
 
# split training and testing data
X = tech.drop(['treatment'], axis=1)
y = tech['treatment']
y = y.replace({'No':0, 'Yes':1})

X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=config.test_size, 
    random_state=config.seed)

# transform features to dummy variables
cat_cols = X_train.columns # get col names

# create one-hot encoder object to transform all features at once
preprocessor = ColumnTransformer([  
    ("one_hot", OneHotEncoder(sparse=False, handle_unknown='ignore'), cat_cols)
    ]) 

# fit and save preprocessor
transform = preprocessor.fit(X_train)

# one-hot encode for training and testing
X_train_transform = transform.transform(X_train)
X_test_transform = transform.transform(X_test)
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

# define Keras Model
model = tf.keras.Sequential()
# Adds a densely-connected layer with 32 units
model.add(Dense(config.hidden_layer_size, 
                input_dim=X_train_transform.shape[1], 
                kernel_regularizer=l2(0.01)))
# Add a relu layer hidden layer
model.add(Dense(config.hidden_layer_size, 
                       activation=config.activation,
                       kernel_regularizer=l2(0.01)))
# Add dropout 
model.add(Dropout(config.dropout))
# Add a sigmoid layer with a single output unit
model.add(layers.Dense(1, activation='sigmoid'))

# compile Keras model
model.compile(loss='binary_crossentropy', 
              optimizer=config.optimizer,
              metrics=['accuracy'])

# fit the model
model.fit(X_train_transform, 
          y_train, 
          epochs=config.epochs, 
          validation_data=(X_test_transform, y_test),
          callbacks=[WandbCallback()])


# save model 
filepath = '../results/'
date_stamp = date.today().strftime('%Y-%b-%d')

model.save(f'{filepath}/neural_net_{date_stamp}.h5')