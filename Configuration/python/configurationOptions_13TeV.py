#!/usr/bin/env python

config_file = "standardConfig_cfg.py"

###### 2015A = 961 pb-1
###### 2012B = 4.9 fb-1
###### 2012B = 4.9 fb-1
###### 2012B = 4.9 fb-1

#intLumi = 19040.  # DoubleMu
#intLumi = 19741.  # DoubleMu_22Jan2013
#intLumi = 18380.  # DoublePhoton
#intLumi = 18260.  # MuEG
intLumi = 19680.  # MuEG 22Jan ReReco

datasets = [

   #data
   'DoubleMu_2015',
   'SingleMu_2015',
   'DoubleEG_2015',
   'MuonEG_2015',

   #MiniAOD not stored on T3.
   'DYJetsToLL_50_MiniAOD',
   'DYJetsToLL_10to50_MiniAOD',
   'WJetsToLNu_MiniAOD',
   'TTJets_MiniAOD',
   'Diboson_MiniAOD',  
   
   'DYJetsToLL_50_50ns_MiniAOD',
   'DYJetsToLL_10to50_50ns_MiniAOD',
   'WJetsToLNu_50ns_MiniAOD',
   'TTJets_50ns_MiniAOD',
   'Diboson_50ns_MiniAOD',  
 
    #QCD MuEnriched
   'QCD_MuEnriched_20toInf_MiniAOD', 
   'QCD_MuEnriched_15to20_MiniAOD', 
   'QCD_MuEnriched_20to30_MiniAOD', 
   'QCD_MuEnriched_30to50_MiniAOD', 
   'QCD_MuEnriched_50to80_MiniAOD', 
   'QCD_MuEnriched_80to120_MiniAOD', 
   'QCD_MuEnriched_120to170_MiniAOD', 
   'QCD_MuEnriched_170to300_MiniAOD',  
   'QCD_MuEnriched_300to470_MiniAOD', 
   'QCD_MuEnriched_470to600_MiniAOD',  
   'QCD_MuEnriched_600to800_MiniAOD', 
   'QCD_MuEnriched_800to1000_MiniAOD', 
   'QCD_MuEnriched_1000toInf_MiniAOD',  
   
   #QCD EMEnriched
   'QCD_EMEnriched_15to20_MiniAOD',    
   'QCD_EMEnriched_20to30_MiniAOD',    
   'QCD_EMEnriched_30to50_MiniAOD',    
   'QCD_EMEnriched_50to80_MiniAOD',    
   'QCD_EMEnriched_80to120_MiniAOD',   
   'QCD_EMEnriched_120to170_MiniAOD',  
   'QCD_EMEnriched_170to300_MiniAOD',  
   'QCD_EMEnriched_300toInf_MiniAOD', 
  
   #QCD bcToE
   'QCD_bcToE_15to20_MiniAOD',       
   'QCD_bcToE_20to30_MiniAOD',       
   'QCD_bcToE_30to80_MiniAOD',       
   'QCD_bcToE_80to170_MiniAOD',      
   'QCD_bcToE_170to250_MiniAOD',     
   'QCD_bcToE_250toInf_MiniAOD',     

   #Sum of all backgrounds
   'Background',
   #Signal MC MiniAOD
   'stop200_1mm_MiniAOD',
   'stop200_10mm_MiniAOD',
   'stop200_100mm_MiniAOD',
   'stop200_1000mm_MiniAOD',


]

composite_dataset_definitions = {
    'DYJetsToLL_MiniAOD' : [
        'DYJetsToLL_50_MiniAOD',
        'DYJetsToLL_10to50_MiniAOD',
    ],
    'DYJetsToLL_50ns_MiniAOD' : [
        'DYJetsToLL_50_50ns_MiniAOD',
        'DYJetsToLL_10to50_50ns_MiniAOD',
    ],
    'Diboson_MiniAOD' : [
        'WW_MiniAOD',
        'WZ_MiniAOD',
        'ZZ_MiniAOD',
    ],
    'Diboson_50ns_MiniAOD' : [
        'WW_50ns_MiniAOD',
        'WZ_50ns_MiniAOD',
        'ZZ_50ns_MiniAOD',
    ],
    'QCD_MuEnriched_MiniAOD' : [
        'QCD_MuEnriched_20toInf_MiniAOD', 
        'QCD_MuEnriched_15to20_MiniAOD', 
        'QCD_MuEnriched_20to30_MiniAOD', 
        'QCD_MuEnriched_30to50_MiniAOD', 
        'QCD_MuEnriched_50to80_MiniAOD', 
        'QCD_MuEnriched_80to120_MiniAOD', 
        'QCD_MuEnriched_120to170_MiniAOD', 
        'QCD_MuEnriched_170to300_MiniAOD',  
        'QCD_MuEnriched_300to470_MiniAOD', 
        'QCD_MuEnriched_470to600_MiniAOD',  
        'QCD_MuEnriched_600to800_MiniAOD', 
        'QCD_MuEnriched_800to1000_MiniAOD', 
        'QCD_MuEnriched_1000toInf_MiniAOD',  
    ],  
   
    'QCD_EMEnriched_MiniAOD' : [
        'QCD_EMEnriched_15to20_MiniAOD',    
        'QCD_EMEnriched_20to30_MiniAOD',    
        'QCD_EMEnriched_30to50_MiniAOD',    
        'QCD_EMEnriched_50to80_MiniAOD',    
        'QCD_EMEnriched_80to120_MiniAOD',   
        'QCD_EMEnriched_120to170_MiniAOD',  
        'QCD_EMEnriched_170to300_MiniAOD',  
        'QCD_EMEnriched_300toInf_MiniAOD', 
    ],  
    
    'QCD_bcToE_MiniAOD' : [
        'QCD_bcToE_15to20_MiniAOD',       
        'QCD_bcToE_20to30_MiniAOD',       
        'QCD_bcToE_30to80_MiniAOD',       
        'QCD_bcToE_80to170_MiniAOD',      
        'QCD_bcToE_170to250_MiniAOD',     
        'QCD_bcToE_250toInf_MiniAOD',     
    ],
    'DoubleMu_2015' : [
        'DoubleMu_2015B',
        'DoubleMu_2015C',
        'DoubleMu_2015D',
    ],
    'SingleMu_2015' : [
        'SingleMu_2015B',
        'SingleMu_2015C',
        'SingleMu_2015D',
    ],
    'DoubleEG_2015' : [
        'DoubleEG_2015B',
        'DoubleEG_2015C',
        'DoubleEG_2015D',
    ],
    'MuonEG_2015' : [
        'MuonEG_2015B',
        'MuonEG_2015C',
        'MuonEG_2015D',
    ],
}


############################################################################################################
#########  DATASET-SPECIFIC OPTIONS  ########################################################################
############################################################################################################

dataset_names = {
    #MiniAOD not stored on T3.
    'DYJetsToLL_50_MiniAOD'     : "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM",
    'DYJetsToLL_10to50_MiniAOD' : "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'WJetsToLNu_MiniAOD'        : "/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'TTJets_MiniAOD'            : "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    'ZZ_MiniAOD'                : "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM", 
    'WW_MiniAOD'                : "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'WZ_MiniAOD'                : "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    
    'DYJetsToLL_50_50ns_MiniAOD'     : "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2/MINIAODSIM",
    'DYJetsToLL_10to50_50ns_MiniAOD' : "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM",
    'WJetsToLNu_50ns_MiniAOD'        : "/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM",
    'TTJets_50ns_MiniAOD'            : "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM",
    'ZZ_50ns_MiniAOD'                : "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2/MINIAODSIM",
    'WW_50ns_MiniAOD'                : "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM",
    'WZ_50ns_MiniAOD'                : "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2/MINIAODSIM",
    #QCD MuEnriched
    'QCD_MuEnriched_20toInf_MiniAOD'        : "/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_MuEnriched_15to20_MiniAOD'         : "/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_MuEnriched_20to30_MiniAOD'         : "/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    'QCD_MuEnriched_30to50_MiniAOD'         : "/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_MuEnriched_50to80_MiniAOD'         : "/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_MuEnriched_80to120_MiniAOD'        : "/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_MuEnriched_120to170_MiniAOD'       : "/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    'QCD_MuEnriched_170to300_MiniAOD'       : "/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    'QCD_MuEnriched_300to470_MiniAOD'       : "/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    'QCD_MuEnriched_470to600_MiniAOD'       : "/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    'QCD_MuEnriched_600to800_MiniAOD'       : "/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    'QCD_MuEnriched_800to1000_MiniAOD'      : "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    'QCD_MuEnriched_1000toInf_MiniAOD'      : "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    #QCD EMEnriched
    'QCD_EMEnriched_15to20_MiniAOD'         : "/QCD_Pt-15to20_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_EMEnriched_20to30_MiniAOD'         : "/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_EMEnriched_30to50_MiniAOD'         : "/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_EMEnriched_50to80_MiniAOD'         : "/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_EMEnriched_80to120_MiniAOD'        : "/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM",
    'QCD_EMEnriched_120to170_MiniAOD'       : "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_EMEnriched_170to300_MiniAOD'       : "/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_EMEnriched_300toInf_MiniAOD'       : "/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    #QCD bcToE
    'QCD_bcToE_15to20_MiniAOD'              : "/QCD_Pt_15to20_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_bcToE_20to30_MiniAOD'              : "/QCD_Pt_20to30_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_bcToE_30to80_MiniAOD'              : "/QCD_Pt_30to80_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    'QCD_bcToE_80to170_MiniAOD'             : "/QCD_Pt_80to170_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    'QCD_bcToE_170to250_MiniAOD'            : "/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'QCD_bcToE_250toInf_MiniAOD'            : "/QCD_Pt_250toInf_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM",
    #Signal MC MiniAOD
    'stop200_1mm_MiniAOD'    : "/DisplacedSUSY_StopToBL_M-200_CTau-1_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'stop200_10mm_MiniAOD'   : "/DisplacedSUSY_StopToBL_M-200_CTau-10_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'stop200_100mm_MiniAOD'  : "/DisplacedSUSY_StopToBL_M-200_CTau-100_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    'stop200_1000mm_MiniAOD' : "/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM",
    

   'DoubleMu_2015B'       : "/DoubleMuon/Run2015B-PromptReco-v1/MINIAOD",
   'DoubleMu_2015C'       : "/DoubleMuon/Run2015C-PromptReco-v1/MINIAOD",
   'DoubleMu_2015D'       : "/DoubleMuon/Run2015D-PromptReco-v3/MINIAOD",
   
   'SingleMu_2015B'       : "/SingleMuon/Run2015B-PromptReco-v1/MINIAOD",
   'SingleMu_2015C'       : "/SingleMuon/Run2015C-PromptReco-v1/MINIAOD",
   'SingleMu_2015D'       : "/SingleMuon/Run2015D-PromptReco-v3/MINIAOD",
   
   'DoubleEG_2015B'       : "/DoubleEG/Run2015B-PromptReco-v1/MINIAOD",
   'DoubleEG_2015C'       : "/DoubleEG/Run2015C-PromptReco-v1/MINIAOD",
   'DoubleEG_2015D'       : "/DoubleEG/Run2015D-PromptReco-v3/MINIAOD",
   
   'MuonEG_2015B'       : "/MuonEG/Run2015B-PromptReco-v1/MINIAOD",
   'MuonEG_2015C'       : "/MuonEG/Run2015C-PromptReco-v1/MINIAOD",
   'MuonEG_2015D'       : "/MuonEG/Run2015D-PromptReco-v3/MINIAOD",
}

nJobs = {
   #MiniAOD not stored on T3.
   'DYJetsToLL_50_MiniAOD'        : 671,
   'DYJetsToLL_10to50_MiniAOD'    : 753,
   'WJetsToLNu_MiniAOD'        : 569,
   'TTJets_MiniAOD'        : 325,
   'WW_MiniAOD'        : 44,
   'ZZ_MiniAOD'        : 36,
   'WZ_MiniAOD'        : 45,
   
   'DYJetsToLL_50_50ns_MiniAOD'        : 491,
   'DYJetsToLL_10to50_50ns_MiniAOD'    : 396,
   'WJetsToLNu_50ns_MiniAOD'        : 634,
   'TTJets_50ns_MiniAOD'        : 150,
   'WW_50ns_MiniAOD'        : 44,
   'ZZ_50ns_MiniAOD'        : 36,
   'WZ_50ns_MiniAOD'        : 45,
   
   #QCD MuEnriched
   'QCD_MuEnriched_20toInf_MiniAOD'        : 347, 
   'QCD_MuEnriched_15to20_MiniAOD'         : 78,
   'QCD_MuEnriched_20to30_MiniAOD'         : 129,
   'QCD_MuEnriched_30to50_MiniAOD'         : 178,
   'QCD_MuEnriched_50to80_MiniAOD'         : 165,
   'QCD_MuEnriched_80to120_MiniAOD'        : 139,
   'QCD_MuEnriched_120to170_MiniAOD'       : 93,
   'QCD_MuEnriched_170to300_MiniAOD'       : 102,
   'QCD_MuEnriched_300to470_MiniAOD'       : 115,
   'QCD_MuEnriched_470to600_MiniAOD'       : 52,
   'QCD_MuEnriched_600to800_MiniAOD'       : 67,
   'QCD_MuEnriched_800to1000_MiniAOD'      : 80,
   'QCD_MuEnriched_1000toInf_MiniAOD'      : 48,
   
   #QCD EMEnriched
   'QCD_EMEnriched_15to20_MiniAOD'         : 69,
   'QCD_EMEnriched_20to30_MiniAOD'         : 261,
   'QCD_EMEnriched_30to50_MiniAOD'         : 135,
   'QCD_EMEnriched_50to80_MiniAOD'         : 145,
   'QCD_EMEnriched_80to120_MiniAOD'        : 201,
   'QCD_EMEnriched_120to170_MiniAOD'       : 233,
   'QCD_EMEnriched_170to300_MiniAOD'       : 130,
   'QCD_EMEnriched_300toInf_MiniAOD'       : 114,
   
   #QCD bcToE
   'QCD_bcToE_15to20_MiniAOD'              : 21, 
   'QCD_bcToE_20to30_MiniAOD'              : 123,
   'QCD_bcToE_30to80_MiniAOD'              : 129,
   'QCD_bcToE_80to170_MiniAOD'             : 153,
   'QCD_bcToE_170to250_MiniAOD'            : 98,
   'QCD_bcToE_250toInf_MiniAOD'            : 99,
   
    #Signal MC MiniAOD
   'stop200_1mm_MiniAOD'    : 1, 
   'stop200_10mm_MiniAOD'   : 1,
   'stop200_100mm_MiniAOD'  : 1,
   'stop200_1000mm_MiniAOD' : 1,
   

   'DoubleMu_2015B'   :  40,
   'DoubleMu_2015C'   : 187,
   'DoubleMu_2015D'   : 40,
   
   'SingleMu_2015B'   :  57,
   'SingleMu_2015C'   : 220,
   'SingleMu_2015D'   : 60,
   
   'DoubleEG_2015B'   :  100,
   'DoubleEG_2015C'   :  298,
   'DoubleEG_2015D'   :  78,
   
   'MuonEG_2015B'   :  30,
   'MuonEG_2015C'   :  82,
   'MuonEG_2015D'   :  21,
   
}

maxEvents = {
   #MiniAOD not stored on T3.
   'DYJetsToLL_50_MiniAOD'        : -1,
   'DYJetsToLL_10to50_MiniAOD'        : -1,
   'WJetsToLNu_MiniAOD'        : -1,
   'TTJets_MiniAOD'            : -1,
   'WW_MiniAOD'            : -1,
   'ZZ_MiniAOD'            : -1,
   'WZ_MiniAOD'            : -1,
   
   'DYJetsToLL_50_50ns_MiniAOD'        : -1,
   'DYJetsToLL_10to50_50ns_MiniAOD'        : -1,
   'WJetsToLNu_50ns_MiniAOD'        : -1,
   'TTJets_50ns_MiniAOD'            : -1,
   'WW_50ns_MiniAOD'            : -1,
   'ZZ_50ns_MiniAOD'            : -1,
   'WZ_50ns_MiniAOD'            : -1,
   #QCD MuEnriched
   'QCD_MuEnriched_20toInf_MiniAOD'        : -1, 
   'QCD_MuEnriched_15to20_MiniAOD'         : -1,
   'QCD_MuEnriched_20to30_MiniAOD'         : -1,
   'QCD_MuEnriched_30to50_MiniAOD'         : -1,
   'QCD_MuEnriched_50to80_MiniAOD'         : -1,
   'QCD_MuEnriched_80to120_MiniAOD'        : -1,
   'QCD_MuEnriched_120to170_MiniAOD'       : -1,
   'QCD_MuEnriched_170to300_MiniAOD'       : -1,
   'QCD_MuEnriched_300to470_MiniAOD'       : -1,
   'QCD_MuEnriched_470to600_MiniAOD'       : -1,
   'QCD_MuEnriched_600to800_MiniAOD'       : -1,
   'QCD_MuEnriched_800to1000_MiniAOD'      : -1,
   'QCD_MuEnriched_1000toInf_MiniAOD'      : -1,
   
   #QCD EMEnriched
   'QCD_EMEnriched_15to20_MiniAOD'         : -1,
   'QCD_EMEnriched_20to30_MiniAOD'         : -1,
   'QCD_EMEnriched_30to50_MiniAOD'         : -1,
   'QCD_EMEnriched_50to80_MiniAOD'         : -1,
   'QCD_EMEnriched_80to120_MiniAOD'        : -1,
   'QCD_EMEnriched_120to170_MiniAOD'       : -1,
   'QCD_EMEnriched_170to300_MiniAOD'       : -1,
   'QCD_EMEnriched_300toInf_MiniAOD'       : -1,
  
   #QCD bcToE
   'QCD_bcToE_15to20_MiniAOD'              : -1, 
   'QCD_bcToE_20to30_MiniAOD'              : -1,
   'QCD_bcToE_30to80_MiniAOD'              : -1,
   'QCD_bcToE_80to170_MiniAOD'             : -1,
   'QCD_bcToE_170to250_MiniAOD'            : -1,
   'QCD_bcToE_250toInf_MiniAOD'            : -1,
   
   #Signal MC MiniAOD
   'stop200_1mm_MiniAOD'    : -1, 
   'stop200_10mm_MiniAOD'   : -1,
   'stop200_100mm_MiniAOD'  : -1,
   'stop200_1000mm_MiniAOD' : -1,

   'DoubleMu_2015B'       : -1,
   'DoubleMu_2015C'       : -1,
   'DoubleMu_2015D'       : -1,
   
   'SingleMu_2015B'       : -1,
   'SingleMu_2015C'       : -1,
   'SingleMu_2015D'       : -1,
   
   'DoubleEG_2015B'       : -1,
   'DoubleEG_2015C'       : -1,
   'DoubleEG_2015D'       : -1,
   
   'MuonEG_2015B'       : -1,
   'MuonEG_2015C'       : -1,
   'MuonEG_2015D'       : -1,
   
}

# bgMC => background MC process
# signalMC => signal MC process
# data => data
types = {
   #MiniAOD not store on T3.
   'DYJetsToLL_MiniAOD'                : "bgMC",
   'DYJetsToLL_50_MiniAOD'     : "bgMC",   
   'DYJetsToLL_10to50_MiniAOD'     : "bgMC",   
   'WJetsToLNu_MiniAOD'        : "bgMC",   
   'TTJets_MiniAOD'            : "bgMC",
   'Diboson_MiniAOD'            : "bgMC",
   'WW_MiniAOD'            : "bgMC",
   'ZZ_MiniAOD'            : "bgMC",
   'WZ_MiniAOD'            : "bgMC",
  
   'DYJetsToLL_50ns_MiniAOD'                : "bgMC",
   'DYJetsToLL_50_50ns_MiniAOD'     : "bgMC",   
   'DYJetsToLL_10to50_50ns_MiniAOD'     : "bgMC",   
   'WJetsToLNu_50ns_MiniAOD'        : "bgMC",   
   'TTJets_50ns_MiniAOD'            : "bgMC",
   'Diboson_50ns_MiniAOD'            : "bgMC",
   'WW_50ns_MiniAOD'            : "bgMC",
   'ZZ_50ns_MiniAOD'            : "bgMC",
   'WZ_50ns_MiniAOD'            : "bgMC",
   #QCD MuEnriched
   'QCD_MuEnriched_20toInf_MiniAOD'        : "bgMC", 
   'QCD_MuEnriched_15to20_MiniAOD'         : "bgMC",
   'QCD_MuEnriched_20to30_MiniAOD'         : "bgMC",
   'QCD_MuEnriched_30to50_MiniAOD'         : "bgMC",
   'QCD_MuEnriched_50to80_MiniAOD'         : "bgMC",
   'QCD_MuEnriched_80to120_MiniAOD'        : "bgMC",
   'QCD_MuEnriched_120to170_MiniAOD'       : "bgMC",
   'QCD_MuEnriched_170to300_MiniAOD'       : "bgMC",
   'QCD_MuEnriched_300to470_MiniAOD'       : "bgMC",
   'QCD_MuEnriched_470to600_MiniAOD'       : "bgMC",
   'QCD_MuEnriched_600to800_MiniAOD'       : "bgMC",
   'QCD_MuEnriched_800to1000_MiniAOD'      : "bgMC",
   'QCD_MuEnriched_1000toInf_MiniAOD'      : "bgMC",
   
   #QCD EMEnriched
   'QCD_EMEnriched_15to20_MiniAOD'         : "bgMC",
   'QCD_EMEnriched_20to30_MiniAOD'         : "bgMC",
   'QCD_EMEnriched_30to50_MiniAOD'         : "bgMC",
   'QCD_EMEnriched_50to80_MiniAOD'         : "bgMC",
   'QCD_EMEnriched_80to120_MiniAOD'        : "bgMC",
   'QCD_EMEnriched_120to170_MiniAOD'       : "bgMC",
   'QCD_EMEnriched_170to300_MiniAOD'       : "bgMC",
   'QCD_EMEnriched_300toInf_MiniAOD'       : "bgMC",
  
   #QCD bcToE
   'QCD_bcToE_15to20_MiniAOD'              : "bgMC", 
   'QCD_bcToE_20to30_MiniAOD'              : "bgMC",
   'QCD_bcToE_30to80_MiniAOD'              : "bgMC",
   'QCD_bcToE_80to170_MiniAOD'             : "bgMC",
   'QCD_bcToE_170to250_MiniAOD'            : "bgMC",
   'QCD_bcToE_250toInf_MiniAOD'            : "bgMC",
    
   #Signal MC MiniAOD
   'stop200_1mm_MiniAOD'    : "signalMC", 
   'stop200_10mm_MiniAOD'   : "signalMC",
   'stop200_100mm_MiniAOD'  : "signalMC",
   'stop200_1000mm_MiniAOD' : "signalMC",


   'DoubleMu_2015B'   : "data",
   'DoubleMu_2015C'   : "data",
   'DoubleMu_2015D'   : "data",
   'DoubleMu_2015'    : "data",
   
   'SingleMu_2015B'   : "data",
   'SingleMu_2015C'   : "data",
   'SingleMu_2015D'   : "data",
   'SingleMu_2015'    : "data",
   
   'DoubleEG_2015B'   : "data",
   'DoubleEG_2015C'   : "data",
   'DoubleEG_2015D'   : "data",
   'DoubleEG_2015'    : "data",
   
   'MuonEG_2015B'   : "data",
   'MuonEG_2015C'   : "data",
   'MuonEG_2015D'   : "data",
   'MuonEG_2015'    : "data",

}

colors = {
   #MiniAOD not store on T3.
   'DYJetsToLL_MiniAOD'          : 410,
   'DYJetsToLL_50_MiniAOD'       : 410,
   'DYJetsToLL_10to50_MiniAOD'   : 410,
   'WJetsToLNu_MiniAOD'          : 852,
   'TTJets_MiniAOD'              : 872,
   'Diboson_MiniAOD'             : 393,
   'WZ_MiniAOD'                  : 393,
   'ZZ_MiniAOD'                  : 397,
   'WW_MiniAOD'                  : 390,
   
   'DYJetsToLL_50ns_MiniAOD'          : 410,
   'DYJetsToLL_50_50ns_MiniAOD'       : 410,
   'DYJetsToLL_10to50_50ns_MiniAOD'   : 410,
   'WJetsToLNu_50ns_MiniAOD'          : 852,
   'TTJets_50ns_MiniAOD'              : 872,
   'Diboson_50ns_MiniAOD'             : 393,
   'WZ_50ns_MiniAOD'                  : 393,
   'ZZ_50ns_MiniAOD'                  : 397,
   'WW_50ns_MiniAOD'                  : 390,
   #QCD MuEnriched
   'QCD_MuEnriched_20toInf_MiniAOD'        : 623, 
   'QCD_MuEnriched_15to20_MiniAOD'         : 623,
   'QCD_MuEnriched_20to30_MiniAOD'         : 623,
   'QCD_MuEnriched_30to50_MiniAOD'         : 623,
   'QCD_MuEnriched_50to80_MiniAOD'         : 623,
   'QCD_MuEnriched_80to120_MiniAOD'        : 623,
   'QCD_MuEnriched_120to170_MiniAOD'       : 623,
   'QCD_MuEnriched_170to300_MiniAOD'       : 623,
   'QCD_MuEnriched_300to470_MiniAOD'       : 623,
   'QCD_MuEnriched_470to600_MiniAOD'       : 623,
   'QCD_MuEnriched_600to800_MiniAOD'       : 623,
   'QCD_MuEnriched_800to1000_MiniAOD'      : 623,
   'QCD_MuEnriched_1000toInf_MiniAOD'      : 623,
   
   #QCD EMEnriched
   'QCD_EMEnriched_15to20_MiniAOD'         : 791,
   'QCD_EMEnriched_20to30_MiniAOD'         : 791,
   'QCD_EMEnriched_30to50_MiniAOD'         : 791,
   'QCD_EMEnriched_50to80_MiniAOD'         : 791,
   'QCD_EMEnriched_80to120_MiniAOD'        : 791,
   'QCD_EMEnriched_120to170_MiniAOD'       : 791,
   'QCD_EMEnriched_170to300_MiniAOD'       : 791,
   'QCD_EMEnriched_300toInf_MiniAOD'       : 791,
  
   #QCD bcToE
   'QCD_bcToE_15to20_MiniAOD'              : 794, 
   'QCD_bcToE_20to30_MiniAOD'              : 794,
   'QCD_bcToE_30to80_MiniAOD'              : 794,
   'QCD_bcToE_80to170_MiniAOD'             : 794,
   'QCD_bcToE_170to250_MiniAOD'            : 794,
   'QCD_bcToE_250toInf_MiniAOD'            : 794,
    
   #Signal MC MiniAOD
   'stop200_1mm_MiniAOD'    : 2, 
   'stop200_10mm_MiniAOD'   : 3,
   'stop200_100mm_MiniAOD'  : 4,
   'stop200_1000mm_MiniAOD' : 5,
   
   
   'DoubleMu_2015B'   : 1,
   'DoubleMu_2015C'   : 1,
   'DoubleMu_2015D'   : 1,
   'DoubleMu_2015'   : 1,
   
   'SingleMu_2015B'   : 1,
   'SingleMu_2015C'   : 1,
   'SingleMu_2015D'   : 1,
   'SingleMu_2015'   : 1,
   
   'DoubleEG_2015B'   : 1,
   'DoubleEG_2015C'   : 1,
   'DoubleEG_2015D'   : 1,
   'DoubleEG_2015'   : 1,
   
   'MuonEG_2015B'   : 1,
   'MuonEG_2015C'   : 1,
   'MuonEG_2015D'   : 1,
   'MuonEG_2015'    : 1,
}

labels = {
   #MiniAOD not stored on T3.
   'DYJetsToLL_50_MiniAOD'                 : "Z#rightarrowll M(50) (MiniAOD)",
   'DYJetsToLL_10to50_MiniAOD'             : "Z#rightarrowll M(10to50) (MiniAOD)",
   'WJetsToLNu_MiniAOD'                    : "W#rightarrowl#nu (MiniAOD)",
   'TTJets_MiniAOD'                        : "t#bar{t} (MiniAOD)",
   'Diboson_MiniAOD'                   : "diboson (MiniAOD)",
   'WW_MiniAOD'                        : "WW",
   'WZ_MiniAOD'                        : "WZ",
   'ZZ_MiniAOD'                        : "ZZ",
   
   'DYJetsToLL_50_50ns_MiniAOD'                 : "Z#rightarrowll M(50) 50ns (MiniAOD)",
   'DYJetsToLL_10to50_50ns_MiniAOD'             : "Z#rightarrowll M(10to50) 50ns (MiniAOD)",
   'WJetsToLNu_50ns_MiniAOD'                    : "W#rightarrowl#nu 50ns (MiniAOD)",
   'TTJets_50ns_MiniAOD'                        : "t#bar{t} 50ns (MiniAOD)",
   'Diboson_50ns_MiniAOD'                   : "diboson 50ns (MiniAOD)",
   'WW_50ns_MiniAOD'                        : "WW 50ns",
   'WZ_50ns_MiniAOD'                        : "WZ 50ns",
   'ZZ_50ns_MiniAOD'                        : "ZZ 50ns",
   #QCD MuEnriched
   'QCD_MuEnriched_20toInf_MiniAOD'        : "QCD MuEnriched Pt 20-Inf (MiniAOD)", 
   'QCD_MuEnriched_15to20_MiniAOD'         : "QCD MuEnriched Pt 15-20 (MiniAOD)",
   'QCD_MuEnriched_20to30_MiniAOD'         : "QCD MuEnriched Pt 20-30 (MiniAOD)",
   'QCD_MuEnriched_30to50_MiniAOD'         : "QCD MuEnriched Pt 30-50 (MiniAOD)",
   'QCD_MuEnriched_50to80_MiniAOD'         : "QCD MuEnriched Pt 50-80 (MiniAOD)",
   'QCD_MuEnriched_80to120_MiniAOD'        : "QCD MuEnriched Pt 80-120 (MiniAOD)",
   'QCD_MuEnriched_120to170_MiniAOD'       : "QCD MuEnriched Pt 120-170 (MiniAOD)",
   'QCD_MuEnriched_170to300_MiniAOD'       : "QCD MuEnriched Pt 170-300 (MiniAOD)",
   'QCD_MuEnriched_300to470_MiniAOD'       : "QCD MuEnriched Pt 300-470 (MiniAOD)",
   'QCD_MuEnriched_470to600_MiniAOD'       : "QCD MuEnriched Pt 470-600 (MiniAOD)",
   'QCD_MuEnriched_600to800_MiniAOD'       : "QCD MuEnriched Pt 600-800 (MiniAOD)",
   'QCD_MuEnriched_800to1000_MiniAOD'      : "QCD MuEnriched Pt 800-1000 (MiniAOD)",
   'QCD_MuEnriched_1000toInf_MiniAOD'      : "QCD MuEnriched Pt 1000-Inf (MiniAOD)",
   
   #QCD EMEnriched
   'QCD_EMEnriched_15to20_MiniAOD'         : "QCD EMEnriched Pt 15-20 (MiniAOD)",
   'QCD_EMEnriched_20to30_MiniAOD'         : "QCD EMEnriched Pt 20-30 (MiniAOD)",
   'QCD_EMEnriched_30to50_MiniAOD'         : "QCD EMEnriched Pt 30-50 (MiniAOD)",
   'QCD_EMEnriched_50to80_MiniAOD'         : "QCD EMEnriched Pt 50-80 (MiniAOD)",
   'QCD_EMEnriched_80to120_MiniAOD'        : "QCD EMEnriched Pt 80-120 (MiniAOD)",
   'QCD_EMEnriched_120to170_MiniAOD'       : "QCD EMEnriched Pt 120-170 (MiniAOD)",
   'QCD_EMEnriched_170to300_MiniAOD'       : "QCD EMEnriched Pt 170-300 (MiniAOD)",
   'QCD_EMEnriched_300toInf_MiniAOD'       : "QCD EMEnriched Pt 300-Inf (MiniAOD)",
  
   #QCD bcToE
   'QCD_bcToE_15to20_MiniAOD'              : "QCD bcToE Pt 15-20 (MiniAOD)", 
   'QCD_bcToE_20to30_MiniAOD'              : "QCD bcToE Pt 20-30 (MiniAOD)",
   'QCD_bcToE_30to80_MiniAOD'              : "QCD bcToE Pt 30-80 (MiniAOD)",
   'QCD_bcToE_80to170_MiniAOD'             : "QCD bcToE Pt 80-170 (MiniAOD)",
   'QCD_bcToE_170to250_MiniAOD'            : "QCD bcToE Pt 170-250 (MiniAOD)",
   'QCD_bcToE_250toInf_MiniAOD'            : "QCD bcToE Pt 250-Inf (MiniAOD)",
    
   #Signal MC MiniAOD
   'stop200_1mm_MiniAOD'    : "#tilde{t}#tilde{t} M(200) c#tau(1mm)", 
   'stop200_10mm_MiniAOD'   : "#tilde{t}#tilde{t} M(200) c#tau(10mm)",
   'stop200_100mm_MiniAOD'  : "#tilde{t}#tilde{t} M(200) c#tau(100mm)",
   'stop200_1000mm_MiniAOD' : "#tilde{t}#tilde{t} M(200) c#tau(1000mm)",
   

   'DoubleMu_2015'      : "Double Muon 2015 data",
   'DoubleMu_2015B'     : "DoubleMu 2015B data",
   'DoubleMu_2015C'     : "DoubleMu 2015C data",
   'DoubleMu_2015D'     : "DoubleMu 2015D data",
   
   'SingleMu_2015'      : "Single Muon 2015 data",
   'SingleMu_2015B'     : "SingleMu 2015B data",
   'SingleMu_2015C'     : "SingleMu 2015C data",
   'SingleMu_2015D'     : "SingleMu 2015D data",
   
   'DoubleEG_2015'      : "DoubleEG 2015 data",
   'DoubleEG_2015B'     : "DoubleEG 2015B data",
   'DoubleEG_2015C'     : "DoubleEG 2015C data",
   'DoubleEG_2015D'     : "DoubleEG 2015C data",
   
   'MuonEG_2015'      : "MuonEG 2015 data",
   'MuonEG_2015B'     : "MuonEG 2015B data",
   'MuonEG_2015C'     : "MuonEG 2015C data",
   'MuonEG_2015D'     : "MuonEG 2015D data",
}

crossSections = {
   #MiniAOD not stored on T3.
   'DYJetsToLL_50_MiniAOD'                 : 6025.2,       # https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV (2008.4 * 3)  
   'WJetsToLNu_MiniAOD'                    : 61526.7,      # https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV (20508.9 * 3) 
   'TTJets_MiniAOD'                        : 831.76,       # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (for top mass = 172.5 GeV)  
    'WW_MiniAOD'                       :                63.21, 
    'WZ_MiniAOD'                       :                22.82, 
    'ZZ_MiniAOD'                       :                10.32,  
   #50ns
   'DYJetsToLL_50_50ns_MiniAOD'                 : 6025.2,       # https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV (2008.4 * 3)  
   'WJetsToLNu_50ns_MiniAOD'                    : 61526.7,      # https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV (20508.9 * 3) 
   'TTJets_50ns_MiniAOD'                        : 831.76,       # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (for top mass = 172.5 GeV)  
    'WW_50ns_MiniAOD'                       :                63.21, 
    'WZ_50ns_MiniAOD'                       :                22.82, 
    'ZZ_50ns_MiniAOD'                       :                10.32,  
############################################################# 
# Cross sections below obatined with crossSectionExtractor.py 
    'DYJetsToLL_10to50_MiniAOD'        :              13638.7,      
    'DYJetsToLL_10to50_50ns_MiniAOD'   :              13638.7,       
    'QCD_MuEnriched_20toInf_MiniAOD'   :  720648000.0*0.00042, 
    'QCD_MuEnriched_15to20_MiniAOD'    :   1273190000.0*0.003, 
    'QCD_MuEnriched_20to30_MiniAOD'    :   558528000.0*0.0053, 
    'QCD_MuEnriched_30to50_MiniAOD'    :  139803000.0*0.01182, 
    'QCD_MuEnriched_50to80_MiniAOD'    :   19222500.0*0.02276, 
    'QCD_MuEnriched_80to120_MiniAOD'   :    2758420.0*0.03844, 
    'QCD_MuEnriched_120to170_MiniAOD'  :     469797.0*0.05362, 
    'QCD_MuEnriched_170to300_MiniAOD'  :     117989.0*0.07335, 
    'QCD_MuEnriched_300to470_MiniAOD'  :      7820.25*0.10196, 
    'QCD_MuEnriched_470to600_MiniAOD'  :      645.528*0.12242, 
    'QCD_MuEnriched_600to800_MiniAOD'  :      187.109*0.13412, 
    'QCD_MuEnriched_800to1000_MiniAOD' :      32.3486*0.14552, 
    'QCD_MuEnriched_1000toInf_MiniAOD' :      10.4305*0.15544, 
# The MC contacts of the EMEnriched samples did not put the
# filter efficiencies in the sample, these efficiencies are 
# took from https://github.com/silviodonato/RateEstimate/blob/
# master/datasetCrossSections/datasetCrossSectionsSpring15.py    
    'QCD_EMEnriched_15to20_MiniAOD'    :1279000000.0*0.001309, 
    'QCD_EMEnriched_20to30_MiniAOD'    : 557600000.0*0.009914, 
    'QCD_EMEnriched_30to50_MiniAOD'    :  136000000.0*0.04988, 
    'QCD_EMEnriched_50to80_MiniAOD'    :    19800000.0*0.1145, 
    'QCD_EMEnriched_80to120_MiniAOD'   :     2800000.0*0.1507, 
    'QCD_EMEnriched_120to170_MiniAOD'  :      477000.0*0.1576, 
# Got from the McM Tool: https://cms-pdmv.cern.ch/mcm/requests?page=0&dataset_name=QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8&
#member_of_campaign=RunIIWinter15GS&shown=163213220927    
    'QCD_EMEnriched_170to300_MiniAOD'  :      114000.0*0.1650, 
    'QCD_EMEnriched_300toInf_MiniAOD'  :        9000.0*0.1500, 
#############################################################    
    'QCD_bcToE_15to20_MiniAOD'         :  1272980000.0*0.0002, 
    'QCD_bcToE_20to30_MiniAOD'         :  557627000.0*0.00059, 
    'QCD_bcToE_30to80_MiniAOD'         :  159068000.0*0.00255, 
    'QCD_bcToE_80to170_MiniAOD'        :    3221000.0*0.01183, 
    'QCD_bcToE_170to250_MiniAOD'       :     105771.0*0.02492, 
    'QCD_bcToE_250toInf_MiniAOD'       :      21094.1*0.03375, 
#############################################################  
    'stop200_1mm_MiniAOD'    : 0.0670476, 
    'stop200_10mm_MiniAOD'   : 0.0670476,
    'stop200_100mm_MiniAOD'  : 0.0670476,
    'stop200_1000mm_MiniAOD' : 0.0670476,

}

