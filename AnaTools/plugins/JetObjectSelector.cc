#include "OSUT3Analysis/AnaTools/interface/ObjectSelector.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#if IS_VALID(jets)
  typedef ObjectSelector<osu::Jet> JetObjectSelector;
  DEFINE_FWK_MODULE(JetObjectSelector);
#endif
