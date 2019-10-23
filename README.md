# chageflip
### Skim the tree
cmsrel CMSSW_10_2_15

cd CMSSW_10_2_15/src

git clone git@github.com:cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools

pushd PhysicsTools/NanoAODTools/python/postprocessing/

git clone https://github.com/freejiebao/chargeflip.git

popd

cmsenv

scram b

pushd PhysicsTools/NanoAODTools/

sh python/postprocessing/chargeflip/skim0_data_2016.sh

sh python/postprocessing/chargeflip/skim0_mc_2016_new.sh

### Fit

cd CMSSW_10_2_15/src/PhysicsTools/NanoAODTools/python/postprocessing/chargeflip

python chargeflip_plot.py -y 2016 -p -f -r -pt highpt

