import ROOT
import argparse
from array import array
ROOT.ROOT.EnableImplicitMT(8)

import numpy
from math import sqrt
import math

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-d','--dataset', help='which dataset to use [SingleMuon,SingleElectron,DoubleMuon,DoubleEG,MuonEG,DY...]',default= 'DoubleEG')
parser.add_argument('-t','--type', help='which type of the dataset: data/mc, default is mc',default= 'mc', choices=('data','mc'))
parser.add_argument('-y','--year', help='which year: 2016/2017/2018, default is 2016',default= '2016', choices=('2016','2017','2018'))
#parser.add_argument('-i','--input', help='input path', default= '/home/cmsdas/testuser01/jie/ssww_ntuple/')
#parser.add_argument('-y','--year', help='which year, default is 2016', default= '2016', choices=('2016','2017','2018'))
args = parser.parse_args()

def DropColumns(column_list):
    branchList = ROOT.vector('string')()
    branches_data_2016=['run','luminosityBlock','event','Trigger_sngEl','Trigger_sngMu','Trigger_dblEl','Trigger_dblMu','Trigger_ElMu','LepCut2l__ele_cut_WP_Tight80X__mu_cut_Tight80x','LepCut2l__ele_cut_WP_Tight80X_SS__mu_cut_Tight80x','LepCut2l__ele_mva_90p_Iso2016__mu_cut_Tight80x','METFilter_DATA','LepCut2l__ele_mva_90p_Iso2016_SS__mu_cut_Tight80x','lep1_pt','lep1_eta','lep1_pdgId','lep2_pt','lep2_eta','lep2_pdgId','mll','trigger']
    branches_mc_2016=['run','luminosityBlock','event','PrefireWeight','LepCut2l__ele_cut_WP_Tight80X__mu_cut_Tight80x','LepSF2l__ele_cut_WP_Tight80X_SS__mu_cut_Tight80x','SFweight2l','LepSF2l__ele_cut_WP_Tight80X_SS__Up','LepSF2l__ele_cut_WP_Tight80X__Do','LepSF2l__ele_cut_WP_Tight80X__mu_cut_Tight80x','LepSF2l__ele_mva_90p_Iso2016__Up','LepSF2l__ele_mva_90p_Iso2016__mu_cut_Tight80x','LepSF2l__ele_cut_WP_Tight80X__Up','METFilter_MC','LepCut2l__ele_cut_WP_Tight80X_SS__mu_cut_Tight80x','XSWeight','LepSF2l__mu_cut_Tight80x__Do','LepSF2l__mu_cut_Tight80x__Up','LepCut2l__ele_mva_90p_Iso2016__mu_cut_Tight80x','LepSF2l__ele_mva_90p_Iso2016__Do','LepSF2l__ele_cut_WP_Tight80X_SS__Do','GenLepMatch2l','lep1_pt','lep1_eta','lep1_pdgId','lep2_pt','lep2_eta','lep2_pdgId','mll','genmatch','ptllDYW']

    branches_data_2017=['run','luminosityBlock','event','Trigger_sngEl','Trigger_sngMu','Trigger_dblEl','Trigger_dblMu','Trigger_ElMu','LepCut2l__ele_mvaFall17V1Iso_WP90_SS__mu_cut_Tight_HWWW','LepCut2l__ele_mvaFall17V2Iso_WP90__mu_cut_Tight_HWWW','METFilter_DATA','LepCut2l__ele_mvaFall17V2Iso_WP90_SS__mu_cut_Tight_HWWW','LepCut2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW','lep1_pt','lep1_eta','lep1_pdgId','lep2_pt','lep2_eta','lep2_pdgId','mll','trigger']
    branches_mc_2017=['run','luminosityBlock','event','PrefireWeight','LepCut2l__ele_mvaFall17V1Iso_WP90_SS__mu_cut_Tight_HWWW','LepSF2l__mu_cut_Tight_HWWW__Up','LepSF2l__ele_mvaFall17V2Iso_WP90__Do','LepSF2l__ele_mvaFall17V1Iso_WP90__Do','SFweight2l','LepSF2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW','LepCut2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW','LepCut2l__ele_mvaFall17V2Iso_WP90__mu_cut_Tight_HWWW','LepSF2l__ele_mvaFall17V1Iso_WP90_SS__mu_cut_Tight_HWWW','LepSF2l__mu_cut_Tight_HWWW__Do','LepSF2l__ele_mvaFall17V2Iso_WP90_SS__mu_cut_Tight_HWWW','LepSF2l__ele_mvaFall17V2Iso_WP90__Up','METFilter_MC','LepSF2l__ele_mvaFall17V2Iso_WP90_SS__Up','LepSF2l__ele_mvaFall17V2Iso_WP90__mu_cut_Tight_HWWW','LepSF2l__ele_mvaFall17V1Iso_WP90_SS__Up','LepSF2l__ele_mvaFall17V2Iso_WP90_SS__Do','XSWeight','LepSF2l__ele_mvaFall17V1Iso_WP90_SS__Do','LepCut2l__ele_mvaFall17V2Iso_WP90_SS__mu_cut_Tight_HWWW','LepSF2l__ele_mvaFall17V1Iso_WP90__Up','GenLepMatch2l','lep1_pt','lep1_eta','lep1_pdgId','lep2_pt','lep2_eta','lep2_pdgId','mll','genmatch','ptllDYW']

    branches_data_2018=['run','luminosityBlock','event','Trigger_sngEl','Trigger_sngMu','Trigger_dblEl','Trigger_dblMu','Trigger_ElMu','LepCut2l__ele_mvaFall17V1Iso_WP90_SS__mu_cut_Tight_HWWW','LepCut2l__ele_mvaFall17V2Iso_WP90__mu_cut_Tight_HWWW','METFilter_DATA','LepCut2l__ele_mvaFall17V2Iso_WP90_SS__mu_cut_Tight_HWWW','LepCut2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW','lep1_pt','lep1_eta','lep1_pdgId','lep2_pt','lep2_eta','lep2_pdgId','mll','trigger']
    branches_mc_2018=['run','luminosityBlock','event','LepCut2l__ele_mvaFall17V1Iso_WP90_SS__mu_cut_Tight_HWWW','LepSF2l__mu_cut_Tight_HWWW__Up','LepSF2l__ele_mvaFall17V2Iso_WP90__Do','LepSF2l__ele_mvaFall17V1Iso_WP90__Do','SFweight2l','LepSF2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW','LepCut2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW','LepCut2l__ele_mvaFall17V2Iso_WP90__mu_cut_Tight_HWWW','LepSF2l__ele_mvaFall17V1Iso_WP90_SS__mu_cut_Tight_HWWW','LepSF2l__mu_cut_Tight_HWWW__Do','LepSF2l__ele_mvaFall17V2Iso_WP90_SS__mu_cut_Tight_HWWW','LepSF2l__ele_mvaFall17V2Iso_WP90__Up','METFilter_MC','LepSF2l__ele_mvaFall17V2Iso_WP90_SS__Up','LepSF2l__ele_mvaFall17V2Iso_WP90__mu_cut_Tight_HWWW','LepSF2l__ele_mvaFall17V1Iso_WP90_SS__Up','LepSF2l__ele_mvaFall17V2Iso_WP90_SS__Do','XSWeight','LepSF2l__ele_mvaFall17V1Iso_WP90_SS__Do','LepCut2l__ele_mvaFall17V2Iso_WP90_SS__mu_cut_Tight_HWWW','LepSF2l__ele_mvaFall17V1Iso_WP90__Up','GenLepMatch2l','lep1_pt','lep1_eta','lep1_pdgId','lep2_pt','lep2_eta','lep2_pdgId','mll','genmatch','ptllDYW']
    if args.type=='data':
        if args.year=='2016':
            for i in range(0,len(branches_data_2016)):
                branchList.push_back(branches_data_2016[i])
        elif args.year=='2017':
            for i in range(0,len(branches_data_2017)):
                branchList.push_back(branches_data_2017[i])
        elif args.year=='2018':
            for i in range(0,len(branches_data_2018)):
                branchList.push_back(branches_data_2018[i])
    elif args.type=='mc':
        if args.year=='2016':
            for i in range(0,len(branches_mc_2016)):
                branchList.push_back(branches_mc_2016[i])
        elif args.year=='2017':
            for i in range(0,len(branches_mc_2017)):
                branchList.push_back(branches_mc_2017[i])
        elif args.year=='2018':
            for i in range(0,len(branches_mc_2018)):
                branchList.push_back(branches_mc_2018[i])

    return branchList

#ROOT.gInterpreter.Declare('#include "{}"'.format("zcutModule_rdf.h"))
#ROOT.loadfile()
if args.type=='data':
    if args.year=='2016':
        files='/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv5_Full2016v6/DATAl1loose2016v6__l2loose__l2tightOR2016v6/nanoLatino_'+args.dataset+'*__part*.root'
    elif args.year=='2017':
        files='/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2017_102X_nAODv5_Full2017v6/DATAl1loose2017v6__l2loose__l2tightOR2017v6/nanoLatino_'+args.dataset+'*__part*.root'
    elif args.year=='2018':
        files='/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv5_Full2018v5/DATAl1loose2018v5__l2loose__l2tightOR2018v5/nanoLatino_'+args.dataset+'*__part*.root'
elif args.type=='mc':
    if args.year=='2016':
        files='/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6/nanoLatino_'+args.dataset+'__part*.root'
        # DYJetsToLL_M-10to50-LO DYJetsToLL_M-10to50 DYJetsToLL_M-10to50_ext1  DYJetsToLL_M-50-LO_ext1 DYJetsToLL_M-50-LO_ext2 DYJetsToLL_M-50_ext2
    elif args.year=='2017':
        files='/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6/nanoLatino_'+args.dataset+'__part*.root'
        # DYJetsToLL_M-10to50-LO DYJetsToLL_M-10to50-LO_ext1 DYJetsToLL_M-50-LO DYJetsToLL_M-50-LO_ext1 DYJetsToLL_M-50 DYJetsToLL_M-50_ext1 DYJetsToLL_M-5to50-LO
    elif args.year=='2018':
        files='/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5/nanoLatino_'+args.dataset+'__part*.root'
        # DYJetsToLL_M-10to50-LO DYJetsToLL_M-10to50-LO_ext1 DYJetsToLL_M-50-LO DYJetsToLL_M-50 DYJetsToLL_M-50_ext
#files='/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2016_102X_nAODv4_Full2016v5/DATAl1loose2016v5__l2loose__l2tightOR2016v5/nanoLatino_SingleMuon_Run2016B-Nano14Dec2018_ver2-v1__part10.root'
ptllDYW_NLO = {
'2016':'(0.876979+gen_ptll*(4.11598e-03)-(2.35520e-05)*gen_ptll*gen_ptll)*(1.10211 * (0.958512 - 0.131835*TMath::Erf((gen_ptll-14.1972)/10.1525)))*(gen_ptll<140)+0.891188*(gen_ptll>=140)',
'2017':'(((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))*(abs(gen_mll-90)<3) + (abs(gen_mll-90)>3))',
'2018':'(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll*gen_ptll+9.19509e-05*(gen_ptll*gen_ptll*gen_ptll)-6.0212e-07*(gen_ptll*gen_ptll*gen_ptll*gen_ptll))*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll*gen_ptll-4.29708e-09*gen_ptll*gen_ptll*gen_ptll+3.35791e-11*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'}
ptllDYW_LO  = {
'2016':'(8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140)',
'2017':'((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))',
'2018':'((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'}
# 2018: LO:DYJetsToLL_M-10to50-LO_ext1 NLO:DYJetsToLL_M-50_ext
# 2017: LO:DYJetsToLL_M-10to50-LO_ext1 NLO:DYJetsToLL_M-50_ext1
# 2016: NLO:DYJetsToLL_M-10to50        LO:DYJetsToLL_M-50-LO_ext2
ptllDYW={
'2016':{'DYJetsToLL_M-10to50':ptllDYW_NLO['2016'],'DYJetsToLL_M-50-LO_ext2':ptllDYW_LO['2016']},
'2017':{'DYJetsToLL_M-10to50-LO_ext1':ptllDYW_LO['2017'],'DYJetsToLL_M-50_ext1':ptllDYW_NLO['2017']},
'2018':{'DYJetsToLL_M-10to50-LO_ext1':ptllDYW_LO['2018'],'DYJetsToLL_M-50_ext':ptllDYW_NLO['2018']}
}
print(files)
df=ROOT.ROOT.RDataFrame('Events',files)
print 'year:',args.year,'dataset:',args.dataset,'type:',args.type
if args.type=='data':
    if args.year=='2016':
        if args.dataset=='MuonEG':
            trigger='Trigger_ElMu'
        elif args.dataset=='DoubleMuon':
            trigger='!Trigger_ElMu && Trigger_dblMu'
        elif args.dataset=='SingleMuon':
            trigger='!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu'
        elif args.dataset=='DoubleEG':
            trigger='!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl'
        elif args.dataset=='SingleElectron':
            trigger='!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl'
        else:
            exit(0)

    if args.year=='2017':
        if args.dataset=='MuonEG':
            trigger='Trigger_ElMu'
        elif args.dataset=='DoubleMuon':
            trigger='!Trigger_ElMu &&  Trigger_dblMu'
        elif args.dataset=='SingleMuon':
            trigger='!Trigger_ElMu && !Trigger_dblMu &&  Trigger_sngMu'
        elif args.dataset=='DoubleEG':
            trigger='!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu &&  Trigger_dblEl'
        elif args.dataset=='SingleElectron':
            trigger='!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl &&  Trigger_sngEl'
        else:
            exit(0)

    if args.year=='2018':
        if args.dataset=='MuonEG':
            trigger='Trigger_ElMu'
        elif args.dataset=='DoubleMuon':
            trigger='!Trigger_ElMu && Trigger_dblMu'
        elif args.dataset=='SingleMuon':
            trigger='!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu'
        elif args.dataset=='EGamma':
            trigger='!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)'
        else:
            exit(0)

    df1=df.Filter('nLepton==2 || (nLepton>2 && Lepton_pt[2]<10)','nlepton cut') \
        .Filter('Lepton_pt[0]>25 && Lepton_pt[1]>12','lepton pt cut') \
        .Filter('abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11','ee channel') \
        .Filter('abs(mll-91.2)<15','mll cut')\
        .Define('trigger',trigger)\
        .Define('lep1_pt','Lepton_pt[0]') \
        .Define('lep1_eta','Lepton_eta[0]') \
        .Define('lep1_pdgId','Lepton_pdgId[0]') \
        .Define('lep2_pt','Lepton_pt[1]') \
        .Define('lep2_eta','Lepton_eta[1]') \
        .Define('lep2_pdgId','Lepton_pdgId[1]')

elif args.type=='mc':
    df1=df.Filter('nLepton==2 || (nLepton>2 && Lepton_pt[2]<10)','nlepton cut')\
        .Filter('Lepton_pt[0]>25 && Lepton_pt[1]>12','lepton pt cut') \
        .Filter('abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11','ee channel')\
        .Filter('abs(mll-91.2)<15','mll cut')\
        .Define('lep1_pt','Lepton_pt[0]')\
        .Define('lep1_eta','Lepton_eta[0]')\
        .Define('lep1_pdgId','Lepton_pdgId[0]')\
        .Define('lep2_pt','Lepton_pt[1]')\
        .Define('lep2_eta','Lepton_eta[1]')\
        .Define('lep2_pdgId','Lepton_pdgId[1]')\
        .Define('genmatch','Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]')\
        .Define('ptllDYW',ptllDYW[args.year][args.dataset])


df1.Snapshot("Events",args.year+'_'+args.dataset+".root",DropColumns(df.GetColumnNames()))

allCutsReport = df.Report()
allCutsReport.Print()
