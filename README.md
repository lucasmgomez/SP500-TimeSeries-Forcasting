# SP500 Analysis Model 

Simple Keras model to predict market direction using the weekly changes of the US Federal Reserve, Treasury, and others.

## Disclaimer

This model is not intended to be used as an investment tool. 

### Installing
install [python 3.7](https://www.python.org/downloads/)

Download [model](model_v1.pkl) and [model_test](model_test.py)

install [tensorflow 2.0](https://www.tensorflow.org/install), [scikit-learn](https://scikit-learn.org/stable/install.html), [numpy](https://numpy.org/), and [joblib](https://joblib.readthedocs.io/en/latest/)

## Running a prediction
```
>>> python model_test.py
```
Now enter information as prompted starting with the file path of the model...

EXAMPLE:
```
Enter File Path of Model (Ex: /User/.../model_v1.pkl): 
  Users/lucasgomez/Models/model_v1.pkl
```

Data Value Entry (recommend using values from [this](https://fred.stlouisfed.org/graph/?g=pMHV) data set)
```
Please enter the weekly percentage change of  the Reserve Balance  (as of wednesday)...
  -12.3456

Please enter the weekly percentage change of  the 10-Year Treasury Rate  (as of wednesday)...
  7.8910

Please enter the weekly percentage change of  the 10-Year Treasury Rate  (as of wednesday)...
  11.1213

Please enter the weekly percentage change of  the Treasury General Account Balance  (as of wednesday)...
  14.1516

Please enter the weekly percentage change of  the Bank Credit  (as of wednesday)...
  17.1819

Please enter the weekly percentage change of  the Federal Reserve Coin Value  (as of wednesday)...
  20.2122

Please enter the weekly percentage change of  the Reverse Repurchase Agreements  (as of wednesday)...
  23.2425

Model predicts S&P500 will have changed minimally in 2 weeks
```

## Built With

* [Keras](https://keras.io/) - Machine Learning API
* [Numpy](https://numpy.org/) - Scientific Computing Package
* [Sklearn (sci-kit)](https://scikit-learn.org/) - Data Analysis Tool

## Training Data

* [FRED](https://fred.stlouisfed.org/) - Market Database 

## Authors

* [Lucas Gomez](https://github.com/lucasmgomez)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [ANG Traders](https://angtraders.com/) - Market Research 

