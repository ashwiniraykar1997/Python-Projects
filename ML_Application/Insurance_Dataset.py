import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from  sklearn.metrics import accuracy_score


def MarvellousLogistic(Path):
    df = pd.read_csv(Path)
    print(" "*50)
    print("First few entries of dataset")
    print(df.head())
    print(" "*50)
    plt.scatter(df.age,df.bought_insurance,marker='+',color='red')
    plt.show()

    X_train,X_test,y_train,y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.5)
    print("Independent variables for training:")
    print(X_train)

    print("_"*50)
    print("Dependant variables for training")
    print(y_train)

    print("_"*50)
    print("Dependant variables for testing:")
    print(y_test)

    model = LogisticRegression()
    model.fit(X_train,y_train)
    print("_"*50)
    y_predicted = model.predict(X_test)
    print("Predicted dependant variables")
    print(y_predicted)

    print("_"*50)
    print("Expected dependant variables")
    print(y_test)


    print("_"*50)
    data = model.predict_proba(X_test)
    print("Probablity of above model is:")
    print(data)

    print("_"*50)
    print("Classification report of logistic Regression is:")
    print(classification_report(y_test,y_predicted))

    print("-"*50)
    print("confusion matrix of Logistic Regression is:")
    print(confusion_matrix(y_test,y_predicted))

    print("_"*50)
    print("Accuracy of Logistic Regression is:")
    print(accuracy_score(y_test,y_predicted))
    print("_"*50)



def main():
    print(""*50)
    print("____Python MachineLearning Script------")
    print(" "*50)
    print("Supervised Machine Learning")

    print("Logistic Regression on Insuarance set")

    print(" "*50)

    MarvellousLogistic("Insurance_data.csv")


if __name__ == "__main__":
    main()