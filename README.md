# chageflip
### Run Z peak cut
i.e.
```
python zcutModule_rdf.py -y 2016 -t data -d SingleElectron
python zcutModule_rdf.py -y 2016 -t data -d DoubleEG
python zcutModule_rdf.py -y 2016 -t mc -d DYJetsToLL_M-10to50
python zcutModule_rdf.py -y 2016 -t mc -d DYJetsToLL_M-50-LO_ext2
```
### Fit to Z peak
i.e.
```
python chargeflip_plot.py -f -p -pt highpt -y 2016 -r
python chargeflip_plot.py -f -p -pt highpt -y 2017 -r 
python chargeflip_plot.py -f -p -pt highpt -y 2018 -r
```
### Fit to charge flip probablity
i.e.
```
$ root -l                     
root [0] .L FittingChargeFlip3.c 
root [1] LeastSquares_PtIndependent("ratio_DYcount_chargeflip_plots_2017_highpt.root","ratio_DATASUBcount_chargeflip_plots_2017_highpt.root")
```

