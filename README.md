# paytext

[![Build Status](https://scrutinizer-ci.com/g/yhoiseth/paytext/badges/build.png?b=master)](https://scrutinizer-ci.com/g/yhoiseth/paytext/build-status/master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/yhoiseth/paytext/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/yhoiseth/paytext/?branch=master)
[![Code Coverage](https://scrutinizer-ci.com/g/yhoiseth/paytext/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/yhoiseth/paytext/?branch=master)

Python package to generalize texts from payment card transactions.

As an example, consider the following texts.
 - `*1234 01.07 NOK 215.00 ITUNES.COM/BILL Kurs: 1.0000`
 - `*4321 29.06 USD 50.00 ITUNES.COM/BILL Rate: 1.0000`
 
Most of the information in these strings are specific to the transaction. But `ITUNES.COM/BILL` is common to multiple transactions. Therefore, we want to _clean_ everything but `ITUNES.COM/BILL` from the string. That is what this package does.

## Known limitations

I've mostly had strings from transactions with Norwegian merchants and banks to work with, so this package probably won't work as well with other languages. If you find strings that it doesn't handle well, please [open an issue on GitHub](https://github.com/yhoiseth/payment-card-text/issues/new).

## Running tests

`nosetests`
