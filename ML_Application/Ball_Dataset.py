from sklearn import tree

def MarvellousML(weight,surface):


    BallsFeature = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1], [96,0],[43,1],[110,0],[35,1],[95,0]]

    Names = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2]

    # Algorithm use to test datasets is DecisionTreeClassifier
    clf = tree.DecisionTreeClassifier()

    # Training model(pass all feature,label for i.e.feature- weight &Surface ,label-Tennis,Cricket )
    clf = clf.fit(BallsFeature,Names)

    # Testing model(pass only feature without (label/Target) i.e. Weight & Surface)
    result = clf.predict([[weight,surface]])

    if result == 1:
        print("Your object looks like Tennis ball")
    elif result == 2:
        print("Your object looks like Cricket ball")



def main():
    print("-----Machine Learning Script-----")
    print("Enter weight of object")
    weight = input()
    print("Whats is surface type of your object Rough or smooth")
    surface = input()
    if surface.lower() =="rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0
    else:
        print("Error:wrong input")
        exit()
    MarvellousML(weight,surface)

if __name__ =="__main__":
    main()