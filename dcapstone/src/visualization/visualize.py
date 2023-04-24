For Age Models

Linear Regression 
    Training data 
        plt.scatter(x_train,y_train, color = "pink")
        plt.plot(x_train, regressor.predict(x_train), color="green")
        plt.title ("Age vs Amount Spent (Training Set)")
        plt.xlabel("Age")
        plt.ylabel("Amount Spent")
        plt.show()
    Test data
        plt.scatter(x_test,y_test, color = "pink")
        plt.plot(x_test, regressor.predict(x_test), color="green")
        plt.title ("Age vs Amount Spent (Test Set)")
        plt.xlabel("Age")
        plt.ylabel("Amount Spent")
        plt.show()

Random Forest Regressor
    fig = plt.figure(figsize=(15, 10))
    plot_tree(regr.estimators_[0], 
              feature_names=x2_test,
              class_names=y2_test, 
              filled=True, impurity=True, 
              rounded=True)   
Gradient Boosting Regressor
    plt.figure (figsize=(12,6))
    plt.title ("Gradient Boosting Model")
    plt.scatter(x4_test,y4_test)
    plt.plot(x4_test,model.predict(x4_test),color="black")
    plt.show()
    
    
    
    
For Gender Models

Linear Regression
    Training Data
        plt.scatter(x1_train,y1_train, color = "pink")
        plt.plot(x1_train, regressor.predict(x1_train), color="green")
        plt.title ("Gender vs Amount Spent (Training Set)")
        plt.xlabel("Gender")
        plt.ylabel("Amount Spent")
        plt.show()
    Test Data 
        plt.scatter(x1_test,y1_test, color = "pink")
        plt.plot(x1_test, regressor.predict(x1_test), color="green")
        plt.title ("Gender vs Amount Spent (Test Set)")
        plt.xlabel("Gender")
        plt.ylabel("Amount Spent")
        plt.show()
        
Random Forest Regressor
    fig = plt.figure(figsize=(15, 10))
    plot_tree(regr.estimators_[0], 
              feature_names=x3_test,
              class_names=y3_test, 
              filled=True, impurity=True, 
              rounded=True)
    
Gradient Boosting Regressor
    plt.figure (figsize=(12,6))
    plt.title ("Gradient Boosting Model")
    plt.scatter(x5_test,y5_test)
    plt.plot(x5_test,model.predict(x5_test),color="black")
    plt.show()








