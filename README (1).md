# Cancer Nanoparticle Therapy Optimization via PhysiCell Agent-Based Simulation

**Author:** Sanyukta Chapagain · M.S. Bioinformatics, Indiana University Bloomington  
**Collaborators:** Emily Morley, Evanka Amin · **Supervisor:** Prof. Mary Loveless  
**Framework:** [pc4nanobio](https://nanohub.org/tools/pc4nanobio) · PhysiCell v1.10.4 · C++ / Python

---

## Overview

Nanoparticle (NP)-based drug delivery offers targeted cancer treatment with reduced systemic toxicity — but **optimal dosing schedules remain an open problem** due to tumor heterogeneity and complex NP pharmacokinetics.

This project uses **pc4nanobio**, an agent-based modeling framework built on PhysiCell, to simulate four distinct NP therapy strategies on a 3D tumor spheroid over 30 days. The core simulation logic — including therapy scheduling, pharmacodynamic modeling, and adaptive dosing triggers — was implemented by **directly modifying `nanobio.cpp` and `PhysiCell_Settings.xml`** in the pc4nanobio source.

**Central question:** Which NP delivery schedule achieves the greatest tumor suppression while minimizing regrowth?

---

## Simulation Snapshots

The figures below show tumor spheroid evolution across all four strategies at Days 3, 10, 15, 18, 21, and 30.

> **Legend:** 🔵 Blue = viable tumor cells · 🟠 Orange/Brown = drug-stressed or apoptotic cells

![Tumor spheroid snapshots across four therapy strategies](simulation_snapshots.png)

*Each row shows one strategy over 30 days. Metronomic therapy (row 2) achieves the most complete tumor clearance by Day 30. Single High Dose (row 3) shows rapid early cell death but strong late regrowth. Adaptive therapy (row 4) cycles ON/OFF based on live cell count thresholds, maintaining dynamic control.*

---

## Therapeutic Strategies

Four strategies were implemented by modifying the C++ source and XML configuration:

| Strategy | Dose Strength | Timing | Duration | Effect Model |
|---|---|---|---|---|
| **Baseline** | 1.0 | Day 5 & Day 10 | 4 hr each | AUC-based |
| **Metronomic** | 0.5 (low) | Days 3, 7, 11, 15, 19, 23 | 4 hr each | AUC-based |
| **Single High Dose** | 15.0 | Day 5 only | 12 hr | Concentration-based |
| **Adaptive** | 5.0 | Dynamic ON/OFF | Continuous | AUC-based |

**Adaptive therapy logic:** Treatment activates when live tumor cells exceed **850 agents** and deactivates when the count drops below **600 agents** — implemented via a live-cell counter in `apply_therapies()`.

---

## Pharmacodynamic Modeling

Drug-induced apoptosis was modeled using two formulations depending on the strategy:

**AUC-based model** (Baseline, Metronomic, Adaptive):
```
Drug Effect = (AUC ^ HillPower) / (AUC ^ HillPower + EC50 ^ HillPower)
```

**Instantaneous concentration model** (Single High Dose):
```
Drug Effect = (C ^ HillPower) / (C ^ HillPower + EC50 ^ HillPower)
```

### Key Parameters by Strategy

| Parameter | Baseline | Metronomic | Single High Dose | Adaptive |
|---|---|---|---|---|
| EC50 | 0.1 | 0.15 | 0.15 | 0.025 |
| Hill Power | 1.5 | 1.5 | 1.8 | 1.5 |
| Initial Tumor Size | ~571 cells | ~571 cells | ~571 cells | ~1,285 cells |
| Simulation Duration | 25 days | 25 days | 25 days | 40 days |

---

## Microenvironment

The tumor microenvironment tracked two diffusible substrates governing cell viability and drug response:

| Substrate | Role | Diffusion Coeff. (μm²/min) | Decay Rate (/min) | Boundary Condition |
|---|---|---|---|---|
| Oxygen (O₂) | Supports viability | 1×10⁵ | 0.1 | Constant Dirichlet |
| Nanoparticle (NP1) | Triggers apoptosis via internalization | 1×10³ | 0.001 | Dirichlet during therapy events |

Hypoxia in the spheroid core triggers necrosis; NP internalization drives apoptosis through the `advance_internalization()` function using a bin-based transit model for intracellular drug release.

---

## Results

| Strategy | Outcome |
|---|---|
| **Metronomic** ✅ | **Lowest final tumor burden.** Sustained low-dose exposure prevented regrowth most effectively. |
| **Adaptive** | Largest initial tumor (~1,285 cells), greatest % reduction, but stabilized at a higher residual size. |
| **Baseline** | Moderate suppression with some regrowth between doses. |
| **Single High Dose** | Rapid initial kill followed by **strong tumor regrowth** — worst long-term outcome. |

**Key finding:** Frequent low-dose metronomic scheduling outperformed a single aggressive dose, consistent with the hypothesis that sustained NP circulation maintains higher intracellular drug accumulation over time.

---

## Repository Structure

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

---

## How to Run

### Prerequisites
- Linux/macOS environment
- C++ compiler (g++ recommended)
- PhysiCell v1.10.4 dependencies: OpenMP, libxml2

### Setup

```bash
# Clone the pc4nanobio base repository
git clone https://github.com/MathCancer/pc4nanobio.git
cd pc4nanobio

# Replace core files with modified versions from this repo
cp path/to/Cancer-nanoparticle-optimization/baseline/nanobio.cpp custom_modules/
cp path/to/Cancer-nanoparticle-optimization/baseline/PhysiCell_Settings.xml ./

# Compile
make

# Run simulation
./project
```

Switch between therapy strategies by replacing `nanobio.cpp` and `PhysiCell_Settings.xml` with the corresponding files from each strategy folder (`metronomic/`, `single_high_dose/`, `adaptive_therapy/`).

---

## Future Work

- Integrate **cancer stem cell dynamics** to model therapy resistance
- Apply **genetic algorithms** to evolve optimal NP therapy schedules automatically
- Explore longer simulation windows (60–90 days) to assess late-stage tumor evolution
- Extend to heterogeneous tumors with mixed cell phenotypes

---

## References

1. Y. Wang et al., "Drug-loaded nanoparticles for cancer therapy: a high-throughput multicellular agent-based modeling study," *bioRxiv*, 2024. [doi:10.1101/2024.04.09.588498](https://doi.org/10.1101/2024.04.09.588498)
2. A. Makrooni, P. Macklin, D. Romano, "An evolutionary computational platform for the automatic discovery of nanocarriers for cancer treatment," *Comput. Mater. Sci.*, 2021. [doi:10.1016/j.commatsci.2021.110506](https://doi.org/10.1016/j.commatsci.2021.110506)
3. A. Ghaffarizadeh et al., "PhysiCell: an open source physics-based cell simulator for 3-D multicellular systems," *PLoS Comput. Biol.*, 2018. [doi:10.1371/journal.pcbi.1005991](https://doi.org/10.1371/journal.pcbi.1005991)

---

## Acknowledgments

Special thanks to [Prof. Paul Macklin](https://mathcancer.org/) (Indiana University) for developing PhysiCell and the pc4nanobio framework, and to Prof. Mary Loveless for project supervision.
