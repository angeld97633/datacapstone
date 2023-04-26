For Age Models

Linear Regressor 
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()

    x = data["Age"]
    y = data ["Amount_spent"]
    y = scaler.fit_transform(pd.DataFrame(y))
    x = scaler.fit_transform(pd.DataFrame(x))

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

    from sklearn.linear_model import LinearRegression

    regressor = LinearRegression()
    regressor.fit(x_train,y_train)

    
Random Forest Regressor  
    x2 = data["Age"]
    y2 = data ["Amount_spent"]
    y2 = scaler.fit_transform(pd.DataFrame(y2))
    x2 = scaler.fit_transform(pd.DataFrame(x2))

    x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, test_size = 0.25, random_state = 101)

    regr = RandomForestRegressor(n_estimators = 10, random_state = 101)
    regr.fit(x2_train, y2_train.ravel())    
    
Random Forest Regressor -- After hyperparameter tuning
    params1 = {'n_estimators': 200,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'max_features': 'sqrt',
    'max_depth': 10,
    'bootstrap': True}
    
    regr2 = RandomForestRegressor(**params1)
    regr2.fit(x2_train, y2_train.ravel())


Gradient Boosting Regressor
    x4 = data["Age"]
    y4 = data["Amount_spent"]
    y4 = scaler.fit_transform(pd.DataFrame(y4))
    x4 = scaler.fit_transform(pd.DataFrame(x4))

    x4_train, x4_test, y4_train, y4_test = train_test_split(x4, y4, test_size=0.30, random_state=100)

    params = {
        "n_estimators": 500,
        "max_depth": 4,
        "min_samples_split": 5,
        "learning_rate": 0.01,
        "loss": "squared_error",
    }


    model = GradientBoostingRegressor(**params)
    model.fit(x4_train, y4_train)
                                  






For Gender Models

Linear Regressor
    x1 = data["Gender F=1,M=0"]
    y1 = data ["Amount_spent"]
    y1 = scaler.fit_transform(pd.DataFrame(y1))
    x1 = scaler.fit_transform(pd.DataFrame(x1))

    x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size= 0.2, random_state=0)

    regressor = LinearRegression()
    regressor.fit(x1_train,y1_train)
 

Random Forest Regressor
    x3 = data["Gender F=1,M=0"]
    y3 = data ["Amount_spent"]
    y3 = scaler.fit_transform(pd.DataFrame(y3))
    x3 = scaler.fit_transform(pd.DataFrame(x3))

    x3_train, x3_test, y3_train, y3_test = train_test_split(x3, y3, test_size = 0.25, random_state = 101)

    regr1 = RandomForestRegressor(n_estimators = 10, random_state = 101)
regr1.fit(x3_train, y3_train.ravel())   

Random Forest Regressor -- After hyperparameter tuning
    params2 = {'n_estimators': 200,
     'min_samples_split': 10,
     'min_samples_leaf': 2,
     'max_features': 'sqrt',
     'max_depth': 50,
     'bootstrap': True}
    regr3 = RandomForestRegressor(**params2)
    regr3.fit(x3_train, y3_train.ravel())


Gradient Boosting Regressor
    x4 = data["Gender F=1,M=0"]
    y4 = data["Amount_spent"]
    y4 = scaler.fit_transform(pd.DataFrame(y4))
    x4 = scaler.fit_transform(pd.DataFrame(x4))

    x4_train, x4_test, y4_train, y4_test = train_test_split(x4, y4, test_size=0.30, random_state=100)

    params = {
        "n_estimators": 500,
        "max_depth": 4,
        "min_samples_split": 5,
        "learning_rate": 0.01,
        "loss": "squared_error",
    }

    from sklearn.ensemble import GradientBoostingRegressor

    model = GradientBoostingRegressor(**params)
    model.fit(x4_train, y4_train)
                                  
    model.fit(x4_train,y4_train)   
    
    