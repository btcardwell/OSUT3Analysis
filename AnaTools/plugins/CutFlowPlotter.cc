#include <iostream>

#include "OSUT3Analysis/AnaTools/plugins/CutFlowPlotter.h"
#include "OSUT3Analysis/AnaTools/interface/ExternTemplates.h"

#define EXIT_CODE 4

CutFlowPlotter::CutFlowPlotter (const edm::ParameterSet &cfg) :
  cutDecisions_ (cfg.getParameter<edm::InputTag> ("cutDecisions")),
  channelName_ (cfg.getParameter<string> ("channelName")),
  firstEvent_ (true)
{
  //////////////////////////////////////////////////////////////////////////////
  // Create a directory for this channel and book the cut flow histograms
  // within.
  //////////////////////////////////////////////////////////////////////////////
  TH1::SetDefaultSumw2 ();
  TFileDirectory dir (fs_->mkdir (channelName_, "base directory for channel \"" + channelName_ + "\""));
  oneDHists_["eventCounter"]  =  dir.make<TH1D>  ("eventCounter",  ";;events",          1,  0.0,  1.0);
  oneDHists_["cutFlow"]       =  dir.make<TH1D>  ("cutFlow",       ";;passing events",  1,  0.0,  1.0);
  oneDHists_["selection"]     =  dir.make<TH1D>  ("selection",     ";;passing events",  1,  0.0,  1.0);
  oneDHists_["minusOne"]      =  dir.make<TH1D>  ("minusOne",      ";;passing events",  1,  0.0,  1.0);
  //////////////////////////////////////////////////////////////////////////////
}

CutFlowPlotter::~CutFlowPlotter ()
{
}

void
CutFlowPlotter::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  //////////////////////////////////////////////////////////////////////////////
  // Try to retrieve the cut decisions from the event and print a warning if
  // there is a problem.
  //////////////////////////////////////////////////////////////////////////////
  event.getByLabel (cutDecisions_, cutDecisions);
  if (firstEvent_ && !cutDecisions.isValid ())
    clog << "WARNING: failed to retrieve cut decisions from the event." << endl;
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // Fill the cut flow histograms, initializing their bins if it is the first
  // event.
  //////////////////////////////////////////////////////////////////////////////
  firstEvent_ && initializeCutFlow ();
  fillCutFlow ();
  firstEvent_ = false;
  //////////////////////////////////////////////////////////////////////////////
}

bool
CutFlowPlotter::initializeCutFlow ()
{
  //////////////////////////////////////////////////////////////////////////////
  // Set the bin label for the first bin, which counts the total number of
  // events. If the cut decisions could not be retrieved from the event, we can
  // do no more, so return false.
  //////////////////////////////////////////////////////////////////////////////
  unsigned bin = 1;
  oneDHists_["cutFlow"]->GetXaxis    ()->SetBinLabel  (bin,  "total");
  oneDHists_["selection"]->GetXaxis  ()->SetBinLabel  (bin,  "total");
  oneDHists_["minusOne"]->GetXaxis   ()->SetBinLabel  (bin,  "total");
  bin++;
  if (!cutDecisions.isValid ())
    return false;
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // Extend the x-axis of the cut flow histograms to accommodate all the cuts.
  // If triggers have been specified, add a special bin for the trigger
  // decision.
  //////////////////////////////////////////////////////////////////////////////
  unsigned nCuts = cutDecisions->cuts.size ();
  cutDecisions->triggers.size () && nCuts++;
  oneDHists_["cutFlow"]->SetBins    (nCuts + 1,  0.0,  nCuts + 1);
  oneDHists_["selection"]->SetBins  (nCuts + 1,  0.0,  nCuts + 1);
  oneDHists_["minusOne"]->SetBins   (nCuts + 1,  0.0,  nCuts + 1);
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // Set the bin labels for the rest of the bins according to the name of the
  // cut. The special bin for the trigger decision is simply labeled "trigger".
  //////////////////////////////////////////////////////////////////////////////
  if (cutDecisions->triggers.size ())
    {
      oneDHists_["cutFlow"]->GetXaxis    ()->SetBinLabel  (bin,  "trigger");
      oneDHists_["selection"]->GetXaxis  ()->SetBinLabel  (bin,  "trigger");
      oneDHists_["minusOne"]->GetXaxis   ()->SetBinLabel  (bin,  "trigger");
      bin++;
    }
  for (vector<cut>::const_iterator cut = cutDecisions->cuts.begin (); cut != cutDecisions->cuts.end (); cut++, bin++)
    {
      oneDHists_["cutFlow"]->GetXaxis    ()->SetBinLabel  (bin,  cut->name.c_str  ());
      oneDHists_["selection"]->GetXaxis  ()->SetBinLabel  (bin,  cut->name.c_str  ());
      oneDHists_["minusOne"]->GetXaxis   ()->SetBinLabel  (bin,  cut->name.c_str  ());
    }
  //////////////////////////////////////////////////////////////////////////////

  // Return true if the initialization was successful.
  return true;
}

bool
CutFlowPlotter::fillCutFlow (double w)
{
  //////////////////////////////////////////////////////////////////////////////
  // Fill the first bin, which counts the total number of events. If the cut
  // decision could not be retrieved from the event, we can do no more so
  // return false.
  //////////////////////////////////////////////////////////////////////////////
  double bin = 0.5;
  bool passes = true;
  oneDHists_["eventCounter"]->Fill  (bin,  w);
  oneDHists_["cutFlow"]->Fill       (bin,  w);
  oneDHists_["selection"]->Fill     (bin,  w);
  bin++;
  if (!cutDecisions.isValid ())
    return false;
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // Fill the rest of the bins according to the flags in the cut decisions
  // object.
  //////////////////////////////////////////////////////////////////////////////
  if (cutDecisions->triggers.size ())
    {
      if (cutDecisions->triggerDecision)
        {
          oneDHists_["cutFlow"]->Fill    (bin,  w);
          oneDHists_["selection"]->Fill  (bin,  w);
        }
      passes = passes && cutDecisions->triggerDecision;
      bin++;
    }
  for (vector<bool>::const_iterator flag = cutDecisions->eventFlags.begin (); flag != cutDecisions->eventFlags.end (); flag++, bin++)
    {
      passes = passes && (*flag);
      if (*flag)
        oneDHists_["selection"]->Fill (bin, w);
      if (passes)
        oneDHists_["cutFlow"]->Fill (bin, w);
    }
  //////////////////////////////////////////////////////////////////////////////

  // Return true if the filling was successful.
  return true;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(CutFlowPlotter);