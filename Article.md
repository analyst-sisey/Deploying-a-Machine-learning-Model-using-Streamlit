Deploying a Machine learning Model using Streamlit
The last stage of the CRISP-DM model is deployment. Building a machine learning model is important for practical business decision-making. A machine learning model in a jupyter Notebook or other development tools however does not fully deliver value to users. For a machine learning model to be of practical importance and deliver value to decision-makers, it must be deployed to production. This allows non-technical users to interact with the model for practical decision-making. One of the ways to deploy a machine learning model is to embed it into a web app. 

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning. To embed a machine learning model into a web app usually require familiarity with Javascript, HTML, and CSS, or other web frameworks such as Django and Flask. This is not the case with streamlit app. With streamlit, you can create interactive web apps with simple code. Using streamlit is a faster way to build and share data apps using pure python scripts.

This article will explain how to deploy a machine learning model by embedding it into a streamlit app. Deploying a machine-learning model involves the following:
 	Building your model
 	Saving your model and other ML items
 	Install streamlit and Build the app 
 	Loading your model and other items
 	Capturing the user input and making the prediction
A detailed description of the process and the code can be found in the project repository on GitHub

Building your model
Before starting the deployment process, it is important to have a trained regression model ready. This can be done using popular machine learning libraries such as sci-kit-learn. We will not explain how to build a model in this article. We will use the regression model we created earlier that predicts the unit sales for items sold at different Favorita stores. You can read how to create the regression model and have access to the python notebook here.
Saving the model and other ML items
After the model is ready, we need to save it so that we can load it into our app. Other machine learning items such as the feature encoder and scaler. Saving the model and other items to file is known as serialization while accessing or opening it is known as deserialization. There are different methods for saving a model and other ML items (serialization) such as pickle, joblib, JSON, PMML, and others. We will be using pickle for serialization and deserialization.
To save our machine learning model using pickle, we have to import pickle and use the pickle.dump() method. This method takes two arguments: the model you want to save, and a file-like object where the model will be saved. We use this method to save our DecisionTreeRegressor model, OneHotEncoder(), and MinMaxScaler().

Install streamlit and Build the application
Once the regression model is trained and saved, the next step is to install streamlit. This can be done by running the "pip install streamlit" command on the command line. Once streamlit is installed, we can start building the deployment application. The first step is to import the necessary libraries and load our saved DecisionTreeRegressor model, OneHotEncoder(), and MinMaxScaler().

Next, we need to create the user interface for the regression model. Streamlit provides a simple and intuitive syntax for building user interfaces. In this example, we create a simple form where the user can enter the input features for the regression model and submit the form to get the prediction.
Loading your model and other items
After our interface is ready, we import the necessary libraries and load the saved LogisticRegression model, OneHotEncoder(), and MinMaxScaler(). We open our model and other machine learning items that have been saved with pickle using the pickle.load() method. This method takes a file-like object that points to the saved model, and returns the model.
Next, we create a function that accepts the user input, encodes the categorical features by fitting them to the OneHotEncoder(), scaling the features by fitting them to the MinMaxScaler(), and predicting using the LogisticRegression model.
Once the user interface and the function are ready, we run the streamlit application using the "streamlit run applicationName.py" command.
This will start the streamlit server and open the application in the user's default web browser. The user can now enter the input values and get the prediction from the LogisticRegression model.

In conclusion, deploying any model using streamlit is a simple and efficient way to provide users access to ML models for practical business decision-making. The intuitive syntax and user-friendly interface make it a great choice for the deployment of models and other data applications.
