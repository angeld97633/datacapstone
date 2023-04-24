For Age Models


Linear Regression 
    y_pred = regressor.predict(x_test)

    r_sq = regressor.score(x, y)
    print('coefficient of determination:', r_sq)
    print('intercept:', regressor.intercept_)
    print('slope:', regressor.coef_) 

    from sklearn.metrics import r2_score
    r2 = r2_score(y_test,y_pred)
    print("r-squared: ",r2)
    from sklearn.metrics import mean_absolute_error
    print("MAE: ",mean_absolute_error(y_test,y_pred))
    from sklearn.metrics import mean_squared_error
    print("MSE: ",mean_squared_error(y_test,y_pred))

Random Forest Regessor
    predictions = regr.predict(x2_test)

    mae = mean_absolute_error(y2_test.ravel(), predictions)

    mse = mean_squared_error(y2_test.ravel(), predictions)

    r2 = r2_score(y2_test.ravel(), predictions)

    print('Mean Absolute Error:', round(mae, 2))
    print('Mean Squared Error:', round(mse, 2))
    print('R-squared scores:', round(r2, 2))
    
Gradient Boosting Regressor
    y4_pred = model.predict(x4_test)


    mae = mean_absolute_error(y4_test.ravel(), y4_pred)
    mse = mean_squared_error(y4_test.ravel(), y4_pred)
    r2 = r2_score(y4_test.ravel(), y4_pred)

    print('Mean Absolute Error:', round(mae, 2))
    print('Mean Squared Error:', round(mse, 2))
    print('R-squared scores:', round(r2, 2))




For Gender Models


Linear Regression 
    y1_pred = regressor.predict(x1_test)

    r_sq = regressor.score(x1, y1)
    print('coefficient of determination:', r_sq)
    print('intercept:', regressor.intercept_)
    print('slope:', regressor.coef_) 

    r2 = r2_score(y1_test,y1_pred)
    print("r-squared: ",r2)
    print("MAE: ",mean_absolute_error(y1_test,y1_pred))
    print("MSE: ",mean_squared_error(y1_test,y1_pred))

Random Forest Regessor
predictions = regr1.predict(x2_test)

    mae = mean_absolute_error(y3_test.ravel(), predictions)
    mse = mean_squared_error(y3_test.ravel(), predictions)
    r2 = r2_score(y3_test.ravel(), predictions)

    print('Mean Absolute Error:', round(mae, 2))
    print('Mean Squared Error:', round(mse, 2))
    print('R-squared scores:', round(r2, 2))

Greadient Boosting Regressor
    y4_pred = model.predict(x4_test)


    mae = mean_absolute_error(y4_test.ravel(), y4_pred)
    mse = mean_squared_error(y4_test.ravel(), y4_pred)
    r2 = r2_score(y4_test.ravel(), y4_pred)


    print('Mean Absolute Error:', round(mae, 2))
    print('Mean Squared Error:', round(mse, 2))
    print('R-squared scores:', round(r2, 2))
    
    
    