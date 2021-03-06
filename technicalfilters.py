import numpy as np
from pyalgotrade import technical
from pyalgotrade import dataseries

from scipy import signal


class EMAEventWindow(technical.EventWindow):

    def __init__(self, flen, alpha):
        technical.EventWindow.__init__(self, flen)
        self.__alpha = alpha

    def EMAfilter(self, data, flen):
        bcoeffs = []
        for i in xrange(flen):
            bcoeffs.append((1 - self.__alpha) ** i)
        b = np.asarray(bcoeffs).astype(np.float64)
        a = np.asarray([sum(bcoeffs)]).astype(np.float64)
        out = signal.lfilter(b, a, data)
        return out

    def getValue(self):
        ret = None
        if self.windowFull():
            these_vals = self.getValues()
            filt = self.EMAfilter(these_vals, self.getWindowSize())
            ret = filt[-1]
        return ret


class EMA(technical.EventBasedFilter):

    """Exponential Moving Average filter.
    """

    def __init__(self, dataSeries, flen, alpha, maxLen=dataseries.DEFAULT_MAX_LEN):
        technical.EventBasedFilter.__init__(
            self, dataSeries, EMAEventWindow(flen, alpha), maxLen)


class TRIXEventWindow(technical.EventWindow):

    def __init__(self, flen, alphas):
        technical.EventWindow.__init__(self, flen * 3)
        self.__alpha1 = alphas[0]
        self.__alpha2 = alphas[1]
        self.__alpha3 = alphas[2]
        self.__flen = flen

    def EMAfilter(self, data, flen, alpha):
        bcoeffs = []
        for i in xrange(flen):
            bcoeffs.append((1 - alpha) ** i)
        b = np.asarray(bcoeffs).astype(np.float64)
        a = np.asarray([sum(bcoeffs)]).astype(np.float64)
        out = signal.lfilter(b, a, data)
        return out

    def getValue(self):
        ret = None
        if self.windowFull():
            these_vals = self.getValues()
            windowsize = self.getWindowSize()
            filta = self.EMAfilter(these_vals, self.__flen, self.__alpha1)
            filtb = self.EMAfilter(
                filta, self.__flen, self.__alpha2)
            filtc = self.EMAfilter(
                filtb, self.__flen, self.__alpha3)
            # print windowsize
            # print these_vals
            # print filta
            # print filtb
            # print filtc
            ret = filtc[-1]
        return ret


class TRIX(technical.EventBasedFilter):

    """Exponential Moving Average filter.
    """

    def __init__(self, dataSeries, flen, alphas, maxLen=dataseries.DEFAULT_MAX_LEN):
        technical.EventBasedFilter.__init__(
            self, dataSeries, TRIXEventWindow(flen, alphas), maxLen)


class DerivativeEventWindow(technical.EventWindow):

    def __init__(self):
        technical.EventWindow.__init__(self, 2)

    def Derivativefilter(self, data):
        bcoeffs = [1, -1]
        b = np.asarray(bcoeffs).astype(np.float64)
        a = np.asarray([1]).astype(np.float64)
        out = signal.lfilter(b, a, data)
        return out

    def getValue(self):
        ret = None
        if self.windowFull():
            these_vals = self.getValues()
            filt = self.Derivativefilter(these_vals)
            ret = filt[-1]
        return ret


class Derivative(technical.EventBasedFilter):

    """Exponential Moving Average filter.
    """

    def __init__(self, dataSeries, maxLen=dataseries.DEFAULT_MAX_LEN):
        technical.EventBasedFilter.__init__(
            self, dataSeries, DerivativeEventWindow(), maxLen)


class ZeroSeriesEventWindow(technical.EventWindow):

    def __init__(self):
        technical.EventWindow.__init__(self, 2)

    def ZeroSeriesfilter(self, data):
        bcoeffs = [0]
        b = np.asarray(bcoeffs).astype(np.float64)
        a = np.asarray([1]).astype(np.float64)
        out = signal.lfilter(b, a, data)
        return out

    def onNewValue(self, dateTime, value):
        technical.EventWindow.onNewValue(self, dateTime, value)

    def getValue(self):
        ret = None
        if self.windowFull():
            these_vals = self.getValues()
            filt = self.ZeroSeriesfilter(these_vals)
            ret = filt[-1]
        return ret


class ZeroSeries(technical.EventBasedFilter):

    """Exponential Moving Average filter.
    """

    def __init__(self, dataSeries, maxLen=dataseries.DEFAULT_MAX_LEN):
        technical.EventBasedFilter.__init__(
            self, dataSeries, ZeroSeriesEventWindow(), maxLen)

class HullEventWindow(technical.EventWindow):

    def __init__(self, flen, alphas):
        technical.EventWindow.__init__(self, flen * 5)
        self.__alpha1 = alphas[0]
        self.__alpha2 = alphas[1]
        self.__alpha3 = alphas[2]
        self.__flen = flen

    def EMAfilter(self, data, flen, alpha):
        bcoeffs = []
        for i in xrange(flen):
            bcoeffs.append((1 - alpha) ** i)
        b = np.asarray(bcoeffs).astype(np.float64)
        a = np.asarray([sum(bcoeffs)]).astype(np.float64)
        out = signal.lfilter(b, a, data)
        return out

    def getValue(self):
        ret = None
        if self.windowFull():
            these_vals = self.getValues()
            windowsize = self.getWindowSize()
            filta = self.EMAfilter(these_vals, self.__flen, self.__alpha1)
            filtb = self.EMAfilter(
                filta, self.__flen, self.__alpha2)
            filtc = self.EMAfilter(
                filtb, self.__flen, self.__alpha3)
            # print windowsize
            # print these_vals
            # print filta
            # print filtb
            # print filtc
            ret = filtc[-1]
        return ret


class Hull(technical.EventBasedFilter):

    """Exponential Moving Average filter.
    """

    def __init__(self, dataSeries, flen, alphas, maxLen=dataseries.DEFAULT_MAX_LEN):
        technical.EventBasedFilter.__init__(
            self, dataSeries, HullEventWindow(flen, alphas), maxLen)
