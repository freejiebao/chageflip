import ROOT
from ROOT import gROOT, gStyle
import collections
import numpy as np
import math
import sys

#rbins=np.array([ 0. , 0.5 , 1. , 1.5 , 2.5])
#rbins=[ 0.0 , 0.5 , 1.0 , 1.5 , 2.5 ]
rbins=[ [0.0 , 1.0] , [1.0 , 1.5] , [1.5 , 2.5] ]

sdict = collections.OrderedDict()

sdict={
    '2016': {
        'lowpt' :
        {
            'qDATA' : [5.97346e-05,4.50053e-04,2.71803e-03],
            'qeDATA' : [2.13220e-05,6.21353e-05,1.18489e-04],
            'qMC' : [3.80635e-05,7.95344e-04,2.58133e-03],
            'qeMC' : [1.19801e-05,4.14558e-05,1.15744e-04],
        },
        'highpt' :
        {
            'qDATA' : [5.18214e-05,5.88700e-04,2.89841e-03],
            'qeDATA' : [4.84606e-06,2.46388e-05,5.90500e-05],
            'qMC' : [5.10800e-05,5.95868e-04,2.82961e-03],
            'qeMC' : [3.59336e-06,2.33829e-05,5.74847e-05],
        },
    },
    '2017': {
        'lowpt' :
        {
            'qDATA' : [6.29275e-05,3.36315e-04,1.57616e-03],
            'qeDATA' : [2.52126e-05,4.36791e-05,7.78224e-05],
            'qMC' : [1.70719e-05,2.92561e-04,1.36443e-03],
            'qeMC' : [1.22951e-05,2.78110e-05,7.28185e-05],
        },
        'highpt' :
        {
            'qDATA' : [4.23166e-05,3.91721e-04,1.73369e-03],
            'qeDATA' : [4.69006e-06,1.80013e-05,3.55432e-05],
            'qMC' : [2.44625e-05,3.98080e-04,1.20569e-03],
            'qeMC' : [2.45881e-06,8.86756e-07,4.13339e-06],
        },
    },
    '2018' : {
        'lowpt':
        {
            'qDATA' : [5.65976e-05,4.31496e-04,1.38770e-03],
            'qeDATA' : [2.19571e-05,6.17224e-05,6.62863e-05],
            'qMC' : [4.20301e-05,3.14053e-04,1.39838e-03],
            'qeMC' : [1.01149e-05,3.06287e-05,4.67098e-05],
        },
        'highpt':
        {
            'qDATA' : [4.92374e-05,3.89759e-04,1.69138e-03],
            'qeDATA' : [3.45322e-06,1.70624e-05,2.76075e-05],
            'qMC' : [5.09476e-05,2.82226e-04,1.37402e-03],
            'qeMC' : [2.45205e-06,1.10011e-05,1.85509e-05],
        },
    },
}

with open('out.txt', 'w') as f:
    for year in sdict:
        print year
        print >> f, "dataset: ",year
        for pt in [ 'lowpt' , 'highpt' ]:
            if pt=='lowpt':
                ptbin=['12','35']
            else:
                ptbin=['35','inf']
            print >> f, "|eta| bin    pT bin  \t  DATA  \t  ERR  \t  MC  \t  ERR  \t  SF  \t  ERR"
            for ix, ixbin in enumerate(rbins):
                x=(sdict[year][pt]['qeDATA'][ix]/sdict[year][pt]['qDATA'][ix])
                y=(sdict[year][pt]['qeMC'][ix]/sdict[year][pt]['qMC'][ix])
                sf=sdict[year][pt]['qDATA'][ix]/sdict[year][pt]['qMC'][ix]
                SFErr= math.sqrt( (sf**2)*(x**2) + (sf**2)*(y**2) )
                print >> f, "%s , %s , %s , %s , %s , %s , %s , %s , %s , %s"\
                    %(ixbin[0] , ixbin[1] , ptbin[0] , ptbin[1] ,\
                      sdict[year][pt]['qDATA'][ix] , sdict[year][pt]['qeDATA'][ix] ,\
                      sdict[year][pt]['qMC'][ix] , sdict[year][pt]['qeMC'][ix] ,\
                      sdict[year][pt]['qDATA'][ix]/sdict[year][pt]['qMC'][ix] , SFErr )
                
'''
SF0 = 1.01451 +- 0.118719
SF1 = 0.987972 +- 0.0566822
SF2 = 1.02431 +- 0.0294708
SF3 = 1.56934 +- 0.493933
SF4 = 0.565859 +- 0.0294943
SF5 = 1.05296 +- 0.0658493

SF0 = 1.715 +- 0.255666
SF1 = 0.983985 +- 0.0452716
SF2 = 1.43468 +- 0.0386529
SF3 = 3.75708 +- 2.75799
SF4 = 1.15076 +- 0.109507
SF5 = 1.1556 +- 0.0840359


SF0 = 0.966432 +- 0.0822046
SF1 = 1.38102 +- 0.0809496
SF2 = 1.23097 +- 0.0260753
SF3 = 1.3466 +- 0.324069
SF4 = 1.37396 +- 0.133999
SF5 = 0.992366 +- 0.0578425
'''
