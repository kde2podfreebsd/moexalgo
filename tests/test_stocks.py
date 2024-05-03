from moexalgo import Ticker
from moexalgo.stocks import Stock
from datetime import date
import pytest
import pandas as pd


def test_candles_shares():
    ABIO = Stock('ABIO', 'TQBR')
    it = ABIO.candles(start='2024-04-22', end='2024-04-22', use_dataframe=False)
    assert isinstance(next(it), object)
    

    it = ABIO.candles(start='2024-04-22', end='2024-04-22', use_dataframe=True)
    assert isinstance(it, pd.DataFrame)

    it = ABIO.tradestats(start='2024-04-22', end='2024-04-22', use_dataframe=False)
    assert isinstance(next(it), object)
    


def test_shares_ticker():
    ABIO = Ticker('ABIO')
    it = ABIO.candles(start='2024-04-22', end='2024-04-22', use_dataframe=False)
    assert isinstance(next(it), object)
    


def test_shares_tradestats():
    ABIO = Stock('ABIO', 'TQBR')
    ABIO.tradestats(start=date(2024, 4, 22),  end='2024-04-22')
    ABIO.tradestats(start=date(2024, 4, 22), end=date(2024, 4, 22))
    ABIO.tradestats(start='2024-04-22', end='2024-04-22')
    with pytest.raises(Exception):
        ABIO.tradestats(start='2024-04-23', end='2024-04-22')
    with pytest.raises(Exception):
        ABIO.tradestats(start=None, end=None)


def test_shares_orderstats():
    ABIO = Stock('ABIO', 'TQBR')
    ABIO.orderstats(start=date(2024, 4, 22),  end='2024-04-22')
    ABIO.orderstats(start=date(2024, 4, 22), end=date(2024, 4, 22))
    ABIO.orderstats(start='2024-04-22', end='2024-04-22')
    with pytest.raises(Exception):
        ABIO.orderstats(start='2024-04-23', end='2024-04-22')
    with pytest.raises(Exception):
        ABIO.orderstats(start=None, end=None)


def test_shares_obstats():
    ABIO = Stock('ABIO', 'TQBR')
    ABIO.obstats(start=date(2024, 4, 22),  end='2024-04-22')
    ABIO.obstats(start=date(2024, 4, 22), end=date(2024, 4, 22))
    ABIO.obstats(start='2024-04-22', end='2024-04-22')
    with pytest.raises(Exception):
        ABIO.obstats(start='2024-04-23', end='2024-04-22')
    with pytest.raises(Exception):
        ABIO.obstats(start=None, end=None)


def test_shares_hi2():
    ABIO = Stock('ABIO', 'TQBR')
    ABIO.hi2(start=date(2024, 4, 22),  end='2024-04-22')
    ABIO.hi2(start=date(2024, 4, 22), end=date(2024, 4, 22))
    ABIO.hi2(start='2024-04-22', end='2024-04-22')
    with pytest.raises(Exception):
        ABIO.hi2(start='2024-04-23', end='2024-04-22')
    with pytest.raises(Exception):
        ABIO.hi2(start=None, end=None)
