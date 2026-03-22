**Cancer Nanoparticle Therapy Optimization via PhysiCell Agent-Based Simulation**

This project uses pc4nanobio, an agent-based modeling framework built on PhysiCell, to simulate four distinct NP therapy strategies on a 3D tumor spheroid over 30 days. The core simulation logic — including therapy scheduling, pharmacodynamic modeling, and adaptive dosing triggers — was implemented by directly modifying nanobio.cpp and PhysiCell_Settings.xml in the pc4nanobio source.

Central question: Which NP delivery schedule achieves the greatest tumor suppression while minimizing regrowth?

<img width="1273" height="723" alt="image" src="https://github.com/user-attachments/assets/abe66c96-2590-425b-ac77-127cc7b769c3" />
Figure 1. Tumor spheroid snapshots across four nanoparticle therapy strategies simulated over 30 days using pc4nanobio (PhysiCell v1.10.4). Each row represents one therapeutic strategy; columns correspond to Days 3, 10, 15, 18, 21, and 30. Blue: viable tumor cells. Orange/Brown: drug-stressed or apoptotic cells. Pill icons indicate active dosing events. In the Adaptive strategy (bottom row), ON/OFF labels denote dynamic therapy activation based on live cell count thresholds (activate at >850 cells, deactivate at <600 cells). Metronomic therapy achieves the greatest tumor reduction by Day 30; Single High Dose shows rapid early kill followed by strong regrowth.

Central question: Which NP delivery schedule achieves the greatest tumor suppression while minimizing regrowth?
