# LSTM SPY Time series forcasting 

Using PyTorch I create a model to predict 14 or 30 days ahead the SPY weekly average. The SPY is the ETF of the S&P500. Model was trained on daily and weekly averages of the following indicators and tickers...

 'MACD',
 'SOMA 1W Delta',
 'TCB 1W Delta',
 '10 Year Treasury Delta',
 'VIX',
 '!AAII Bull',
 'CPCE',
 'CPCE %Delta'

## Disclaimer

This model is not intended to be used as an investment tool. 

## Built With

* [PyTorch](https://pytorch.org/)
* [Numpy](https://numpy.org/) 
* [Pandas](https://pandas.pydata.org/)
* [Sklearn (sci-kit)](https://scikit-learn.org/) 

## Trained With

* [FRED](https://fred.stlouisfed.org/) 
* [ReLu](https://keras.io/activations/) - Activation Function
* [SoftMax](https://keras.io/activations/) - Activation Function
* [Adam](https://keras.io/optimizers/) - Optimizer

## Authors

* [Lucas Gomez](https://github.com/lucasmgomez)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [ANG Traders](https://angtraders.com/) - Market Research 

