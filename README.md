
# IPL Score Predictor App

In this project we will predict the score in the upcoming over of the innings. In this project we uses the `Linear Regression` Algorithm to predict the Score.

### SOFTWARE REQUIREMENT:
* Python
* Pandas
* NumPy
* Matplotlib
* Scikit Learn
* Jupyter Notebook/Google Colab
* PyCharm

### STEPS INVOLVED IN DATA PROCESSING:
* Feature Selection: We have a lot of unnecessary attributes in our data that we won't use in our project. As a result, we only use the attributes that we need.

* Normalization: The initial step is to normalize the data which we have collected from the internet. Rescaling real-valued numeric attributes into the range between 0 and 1 is referred to as normalization. The data is then normalized after it has been filtered.

* Machine Learning: The method of iteratively refining your prediction equation through looping over the dataset several times by updating the values of weight and bais in the direction suggested by the slope of the gradient(Cost Function) is known as training a model. We consider training to be complete, when we exceed an appropriate error, or when required training iterations(epochs or cycles) fail to reduce our cost.

## To See UI
run a following command in command prompt
```
Streamlit run streamlit_app.py
```
## Deployment
Prepare your dataset:
```
1. Firstly, the data is trained. We will take 15-20% of the data from the data collection to train the model.
2. We will take 15-20% of the data from the data collection to train the model.
3. For the prediction, we will using a Linear Regression algorithm.
4. The project is split into three separate Jupyter Notebooks: one to collect the IPL data, inspect it, and clean it; a second to further refine the features and fit the data to a Linear Regression model to train and evaluate our output.
5. and setup the ui using the streamlit module and the load the model there and then predict the score for the upcoming overs.
```


## Demo

![App Screenshot](https://raw.githubusercontent.com/Franky-Saxena/IPL-Score-Predictor-App/main/Untitled1.png)
![App Screenshot](https://raw.githubusercontent.com/Franky-Saxena/IPL-Score-Predictor-App/main/Untitled2.png)
