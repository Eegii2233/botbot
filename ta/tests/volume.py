import pandas as pd

from ta.tests.utils import TestIndicator
from ta.volume import (AccDistIndexIndicator, EaseOfMovementIndicator,
                       ForceIndexIndicator, OnBalanceVolumeIndicator,
                       acc_dist_index, ease_of_movement, force_index,
                       on_balance_volume, sma_ease_of_movement)


class TestOnBalanceVolumeIndicator(TestIndicator):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:on_balance_volume_obv
    """

    _filename = 'ta/tests/data/cs-obv.csv'

    def test_obv(self):
        target = 'OBV'
        result = on_balance_volume(close=self._df['Close'], volume=self._df['Volume'], fillna=False)
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)

    def test_obv2(self):
        target = 'OBV'
        result = OnBalanceVolumeIndicator(
            close=self._df['Close'], volume=self._df['Volume'], fillna=False).on_balance_volume()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)


class TestForceIndexIndicator(TestIndicator):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:force_index
    """

    _filename = 'ta/tests/data/cs-fi.csv'

    def test_fi(self):
        target = 'FI'
        result = force_index(close=self._df['Close'], volume=self._df['Volume'], n=13, fillna=False)
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)

    def test_fi2(self):
        target = 'FI'
        result = ForceIndexIndicator(
            close=self._df['Close'], volume=self._df['Volume'], n=13, fillna=False).force_index()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)


class TestEaseOfMovementIndicator(TestIndicator):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:ease_of_movement_emv
    """

    _filename = 'ta/tests/data/cs-easeofmovement.csv'

    def test_ease_of_movement(self):
        target = 'EMV'
        result = ease_of_movement(
            high=self._df['High'], low=self._df['Low'], volume=self._df['Volume'], n=14, fillna=False)
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)

    def test_ease_of_movement2(self):
        target = 'EMV'
        result = EaseOfMovementIndicator(
            high=self._df['High'], low=self._df['Low'], volume=self._df['Volume'], n=14, fillna=False
        ).ease_of_movement()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)

    def test_sma_ease_of_movement(self):
        target = 'SMA_EMV'
        result = sma_ease_of_movement(
            high=self._df['High'], low=self._df['Low'], volume=self._df['Volume'], n=14, fillna=False)
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)

    def test_sma_ease_of_movement2(self):
        target = 'SMA_EMV'
        result = EaseOfMovementIndicator(
            high=self._df['High'], low=self._df['Low'], volume=self._df['Volume'], n=14, fillna=False
        ).sma_ease_of_movement()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)


class TestAccDistIndexIndicator(TestIndicator):
    """
    https://school.stockcharts.com/doku.php?id=technical_indicators:accumulation_distribution_line
    """

    _filename = 'ta/tests/data/cs-accum.csv'

    def test_adl(self):
        target = 'ADLine'
        result = acc_dist_index(
            high=self._df['High'], low=self._df['Low'], close=self._df['Close'], volume=self._df['Volume'],
            fillna=False)
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)

    def test_adl2(self):
        target = 'ADLine'
        result = AccDistIndexIndicator(
            high=self._df['High'], low=self._df['Low'], close=self._df['Close'], volume=self._df['Volume'],
            fillna=False).acc_dist_index()
        pd.testing.assert_series_equal(self._df[target].tail(), result.tail(), check_names=False)
