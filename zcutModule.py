import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class zcutProducer(Module):
    def __init__(self, zmass=91.1876, isData="MC", year='2016', trig='MC'):
        self.zmass = zmass
        self.isData=isData
        self.year=year
        self.trig=trig
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("lep1_pt",  "F")
        self.out.branch("lep1_eta",  "F")
        self.out.branch("lep1_pdgId",  "I")
        self.out.branch("lep2_pt",  "F")
        self.out.branch("lep2_eta",  "F")
        self.out.branch("lep2_pdgId",  "I")
        self.out.branch("mll",  "F")
        self.out.branch("genmatch","B")
        self.out.branch("trigger",  "B")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        leptons = Collection(event, "Lepton")
        #muons = Collection(event, "Muon")
        #jets = Collection(event, "Jet")
        # eventSum = ROOT.TLorentzVector()
        if len(leptons) < 2:
            return False
        elif len(leptons) >= 3:
            if leptons[2].pt> 10.:
                return False
        if leptons[0].pt<20 or leptons[1].pt<20:
            return False
        # mumu channel
        if not abs(leptons[0].pdgId*leptons[1].pdgId) == 13*13:
            return False
        # ee channel
        # if not abs(leptons[0].pdgId*leptons[1].pdgId) == 11*11:
        #   return False
        if abs(event.mll-self.zmass)>15:
            return False

        trigger=True
        genmatch=True
        if self.trig=='MC':
            genmatch=leptons[0].promptgenmatched*leptons[1].promptgenmatched
        elif self.trig=='MuonEG':
            trigger=event.Trigger_ElMu
        elif self.trig=='DoubleMuon':
            trigger=((not event.Trigger_ElMu) and event.Trigger_dblMu)
        elif self.trig=='SingleMuon':
            trigger=((not event.Trigger_ElMu) and (not event.Trigger_dblMu) and event.Trigger_sngMu)
        elif self.year=='2018':
            if self.trig=='EGamma':
                trigger=(not event.Trigger_ElMu) and (not event.Trigger_dblMu) and (not event.Trigger_sngMu) and (event.Trigger_dblEl or event.Trigger_sngEl)
        else:
            if self.trig=='DoubleEG':
                trigger=((not event.Trigger_ElMu) and (not event.Trigger_dblMu) and (not event.Trigger_sngMu) and event.Trigger_dblEl)
            elif self.trig=='SingleElectron':
                trigger=((not event.Trigger_ElMu) and (not event.Trigger_dblMu) and (not event.Trigger_sngMu) and (not event.Trigger_dblEl) and event.Trigger_sngEl)

        self.out.fillBranch("lep1_pt",leptons[0].pt)
        self.out.fillBranch("lep1_eta",leptons[0].eta)
        self.out.fillBranch("lep1_pdgId",leptons[0].pdgId)
        self.out.fillBranch("lep2_pt",leptons[1].pt)
        self.out.fillBranch("lep2_eta",leptons[1].eta)
        self.out.fillBranch("lep2_pdgId",leptons[1].pdgId)
        self.out.fillBranch("mll",event.mll)
        self.out.fillBranch("genmatch",genmatch)
        self.out.fillBranch("trigger",trigger)

        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
# only 2018 has different datasets with 2017 and 2016, so no need to change the year from 2016 to 2017
zcutModuleDataMuonEG = lambda : zcutProducer(isData="DATA", year='2016', trig='MuonEG')
zcutModuleDataDoubleMuon = lambda : zcutProducer(isData="DATA", year='2016', trig='DoubleMuon')
zcutModuleDataSingleMuon = lambda : zcutProducer(isData="DATA", year='2016', trig='SingleMuon')
zcutModuleDataDoubleEG = lambda : zcutProducer(isData="DATA", year='2016', trig='DoubleEG')
zcutModuleDataSingleElectron = lambda : zcutProducer(isData="DATA", year='2016', trig='SingleElectron')

zcutModuleDataEGamma = lambda : zcutProducer(isData="DATA", year='2018', trig='EGamma')

zcutModuleMC = lambda : zcutProducer(isData="MC", year='2016')