**Cancer Nanoparticle Therapy Optimization via PhysiCell Agent-Based Simulation**
##  Note on Codebase & Modifications

This project builds upon the [pc4nanobio](https://github.com/rheiland/pc4nanobio) framework, an agent-based modeling extension of PhysiCell.

Each therapy strategy (`baseline`, `metronomic`, `single_high_dose`, `adaptive_therapy`) retains the original repository structure.  

The primary modifications for each experiment were limited to the following core files:

- `src/custom_modules/nanobio.cpp`  
  → Implemented therapy scheduling logic, dosing strategies, and adaptive ON/OFF control

- `data/PhysiCell_settings.xml`  
  → Tuned simulation parameters including EC50, Hill coefficient, and nanoparticle boundary conditions

All other files follow the standard pc4nanobio implementation.

This project uses pc4nanobio, an agent-based modeling framework built on PhysiCell, to simulate four distinct NP therapy strategies on a 3D tumor spheroid over 30 days. The core simulation logic is including therapy scheduling, pharmacodynamic modeling, and adaptive dosing triggers . This was implemented by directly modifying nanobio.cpp and PhysiCell_Settings.xml in the pc4nanobio source.

 Question: Which NP delivery schedule achieves the greatest tumor suppression while minimizing regrowth?

<img width="1273" height="723" alt="image" src="https://github.com/user-attachments/assets/abe66c96-2590-425b-ac77-127cc7b769c3" />
Figure 1. Tumor spheroid snapshots across four nanoparticle therapy strategies simulated over 30 days using pc4nanobio (PhysiCell v1.10.4). Each row represents one therapeutic strategy; columns correspond to Days 3, 10, 15, 18, 21, and 30. Blue: viable tumor cells. Orange/Brown: drug-stressed or apoptotic cells. Pill icons indicate active dosing events. In the Adaptive strategy (bottom row), ON/OFF labels denote dynamic therapy activation based on live cell count thresholds (activate at >850 cells, deactivate at <600 cells). Metronomic therapy achieves the greatest tumor reduction by Day 30; Single High Dose shows rapid early kill followed by strong regrowth.

## Drug-Induced Apoptosis Modeling

Drug-induced apoptosis was modeled using two formulations depending on the strategy:

### AUC-based model (Baseline, Metronomic, Adaptive)

$$
\text{Drug Effect} = \frac{AUC^{\text{HillPower}}}{AUC^{\text{HillPower}} + EC50^{\text{HillPower}}}
$$

### Instantaneous concentration model (Single High Dose)

$$
\text{Drug Effect} = \frac{C^{\text{HillPower}}}{C^{\text{HillPower}} + EC50^{\text{HillPower}}}
$$

## Key Parameters by Strategy

| Parameter               | Baseline | Metronomic | Single High Dose | Adaptive      |
|------------------------|----------|------------|------------------|--------------|
| EC50                   | 0.1      | 0.15       | 0.15             | 0.025        |
| Hill Power             | 1.5      | 1.5        | 1.8              | 1.5          |
| Initial Tumor Size     | ~571 cells | ~571 cells | ~571 cells       | ~1,285 cells |
| Simulation Duration    | 25 days  | 25 days    | 25 days          | 40 days      |


## Microenvironment

The tumor microenvironment tracked two diffusible substrates governing cell viability and drug response:

| Substrate            | Role                                   | Diffusion Coeff. (μm²/min) | Decay Rate (/min) | Boundary Condition              |
|---------------------|----------------------------------------|----------------------------|-------------------|---------------------------------|
| Oxygen (O₂)         | Supports viability                     | 1×10⁵                      | 0.1               | Constant Dirichlet              |
| Nanoparticle (NP1)  | Triggers apoptosis via internalization | 1×10³                      | 0.001             | Dirichlet during therapy events |


## Results

| Strategy            | Outcome |
|--------------------|--------|
| **Metronomic**  | Lowest final tumor burden. Sustained low-dose exposure prevented regrowth most effectively. |
| **Adaptive**       | Largest initial tumor (~1,285 cells), greatest % reduction, but stabilized at a higher residual size. |
| **Baseline**       | Moderate suppression with some regrowth between doses. |
| **Single High Dose** | Rapid initial kill followed by strong tumor regrowth — worst long-term outcome. |

**Key finding:** Frequent low-dose metronomic scheduling outperformed a single aggressive dose, consistent with the hypothesis that sustained NP circulation maintains higher intracellular drug accumulation over time.


##  Repository Structure

```
Cancer-nanoparticle-optimization/
├── baseline/               # Baseline therapy simulation files & output
├── metronomic/             # Metronomic therapy setup & outputs
├── single_high_dose/       # Single high-dose simulation & outputs
├── adaptive_therapy/       # Adaptive therapy simulation code & data
├── POSTER.pptx             # Academic poster presented at IU Bloomington
├── Therapy_Progress.pdf    # Simulation output analysis report
├── Macklin_pc4nanobio_reference.pdf  # Reference paper (Wang et al., 2024)
└── README.md
```
