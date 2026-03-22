**Cancer Nanoparticle Therapy Optimization via PhysiCell Agent-Based Simulation**

This project uses pc4nanobio, an agent-based modeling framework built on PhysiCell, to simulate four distinct NP therapy strategies on a 3D tumor spheroid over 30 days. The core simulation logic is including therapy scheduling, pharmacodynamic modeling, and adaptive dosing triggers . This was implemented by directly modifying nanobio.cpp and PhysiCell_Settings.xml in the pc4nanobio source.

 Question: Which NP delivery schedule achieves the greatest tumor suppression while minimizing regrowth?

<img width="1273" height="723" alt="image" src="https://github.com/user-attachments/assets/abe66c96-2590-425b-ac77-127cc7b769c3" />
Figure 1. Tumor spheroid snapshots across four nanoparticle therapy strategies simulated over 30 days using pc4nanobio (PhysiCell v1.10.4). Each row represents one therapeutic strategy; columns correspond to Days 3, 10, 15, 18, 21, and 30. Blue: viable tumor cells. Orange/Brown: drug-stressed or apoptotic cells. Pill icons indicate active dosing events. In the Adaptive strategy (bottom row), ON/OFF labels denote dynamic therapy activation based on live cell count thresholds (activate at >850 cells, deactivate at <600 cells). Metronomic therapy achieves the greatest tumor reduction by Day 30; Single High Dose shows rapid early kill followed by strong regrowth.

Drug-induced apoptosis was modeled using two formulations depending on the strategy:
AUC-based model (Baseline, Metronomic, Adaptive):
Drug Effect = (AUC ^ HillPower) / (AUC ^ HillPower + EC50 ^ HillPower)
Instantaneous concentration model (Single High Dose):
Drug Effect = (C ^ HillPower) / (C ^ HillPower + EC50 ^ HillPower)

Key Parameters by Strategy
ParameterBaselineMetronomicSingle High DoseAdaptiveEC500.10.150.150.025Hill Power1.51.51.81.5Initial Tumor Size~571 cells~571 cells~571 cells~1,285 cellsSimulation Duration25 days25 days25 days40 days

Microenvironment
The tumor microenvironment tracked two diffusible substrates governing cell viability and drug response:
SubstrateRoleDiffusion Coeff. (μm²/min)Decay Rate (/min)Boundary ConditionOxygen (O₂)Supports viability1×10⁵0.1Constant DirichletNanoparticle (NP1)Triggers apoptosis via internalization1×10³0.001Dirichlet during therapy events
Hypoxia in the spheroid core triggers necrosis; NP internalization drives apoptosis through the advance_internalization() function using a bin-based transit model for intracellular drug release.
