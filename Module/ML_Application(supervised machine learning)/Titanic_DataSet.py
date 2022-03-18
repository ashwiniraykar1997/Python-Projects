import  math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import  matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

def TitanicLogistic():
    # setp1:Load data
    titanic_data = pd.read_csv('titanic.csv')

    print("First 5 entries from loaded dataset")
    print(titanic_data.head())

    print("Number of passangers are"+str(len(titanic_data)))

    # step2:Analyze data
    print("Visualization:Survived and non survied passangers")
    figure()
    target = "Survived"

    countplot(data=titanic_data,x=target).set_title("Titanice Dataset:Survived and non survied passangers")
    show()

    print("Visualisation:Survived and non survied passangers based on Gender")
    figure()
    target = "Survived"

    countplot(data=titanic_data,x=target,hue="Sex").set_title("Titanic DataSet:Survived and non survied passangers based on Gender")
    show()

    print("Visualization:Survived and non survived passangers based on the Age")
    figure()
    titanic_data["Age"].plot.hist().set_title("Titanic Dataset:Survivesd and non survived passangers based on Age")
    show()

    print("Visualization:Survived and non survived passangers based on the Fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Titanic Dataset:Survived and non survived passangers based on Fare")
    show()

    # step3:Data cleaning
    # titanic_data.drop("[zero]",axis=1,inplace=True)

    # print("First % entries from loaded dataset after removing zero column")
    # print(titanic_data.head(5))

    print("Values of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))


    print("Values of Sex column after removing one field")
    Sex = pd.get_dummies(titanic_data["Sex"],drop_first=True)
    print(Sex.head(5))

    print("Values of Pclass column after removing one field")
    pclass = pd.get_dummies(titanic_data["Pclass"],drop_first=True)
    print(pclass.head(5))


    print("Values of data set after removing irrelevant columns")
    titanic_data = pd.concat([titanic_data,Sex,pclass],axis=1)

    print("values of data set after removing irrelevent columns")
    titanic_data.drop(["Sex","SibSp","Parch","Embarked"],axis=1,inplace=True)
    print(titanic_data.head(5))

    X = titanic_data.drop("Survived",axis=1)
    y = titanic_data["Survived"]

    # list of text documents

    text = ["The quick brown fox jumped over the lazy dog."]
    # create the transform
    vectorizer = CountVectorizer()
    # tokenize and build vocab
    vectorizer.fit(text)
    # summarize
    print(vectorizer.vocabulary_)
    # encode document
    vector = vectorizer.transform(text)
    # summarize encoded vector
    print(vector.shape)
    print(type(vector))
    print(vector.toarray())
    #Step4:Data Training
    Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.5)

    logmodel = LogisticRegression()

    print("logmodel is...")

    logmodel = logmodel.fit(Xtrain,ytrain)

    print(logmodel)

    #   step5:Data Testing
    prediction = logmodel.predict(Xtest)

    #    step6:Calculate Accuracy
    print("Classification report of Logistic Regression is:")
    print(classification_report(ytest,prediction))

    print("Confusion Matrix of Logistic Regression is:")
    print(confusion_matrix(ytest,prediction))

    print("Accuracy of Logistic Regression is:")
    print(accuracy_score(ytest,prediction))

def main():
    print("------Python Machine Learning----")
    print("Supervised Machine Learning")
    print("Logistic Regression on Titanic data set")
    TitanicLogistic()

if __name__ == "__main__":
    main()































