# LSTM SPY Time series forcasting 

Using PyTorch I created a LSTM model to predict 14 or 30 days ahead the SPY weekly average. The SPY is the ETF of the S&P500. Model was trained on daily and weekly averages of the following indicators and tickers...

 'MACD',
 'SOMA 1W Delta',
 'TCB 1W Delta',
 '10 Year Treasury Delta',
 'VIX',
 '!AAII Bull',
 'CPCE',
 'CPCE %Delta'

All source code found in the SPYForcast.ipynb Google Collab

## Disclaimer

This model is not intended to be used as an investment tool. 

## Built With

* [PyTorch](https://pytorch.org/)
* [Numpy](https://numpy.org/) 
* [Pandas](https://pandas.pydata.org/)
* [Sklearn (sci-kit)](https://scikit-learn.org/) 

## Trained With

* [FRED](https://fred.stlouisfed.org/) - Data
* [nn.Linear](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html) - Activation Function
* [Adam](entral.carleton.ca) - Optimizer

## Conclusion

Current best model is ~60% accurate on both 14 and 30 day future predictions. I beleive 65-70% is possible with more indicators and more hidden layers. 

## Authors

* [Lucas Gomez](https://github.com/lucasmgomez)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [ANG Traders](https://angtraders.com/) - Market Research 

