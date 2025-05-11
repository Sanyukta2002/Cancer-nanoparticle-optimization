
# Cancer Nanoparticle Therapy Optimization

**Author:** Sanyukta Chapagain  
**Affiliation:** MS in Bioinformatics, Indiana University  
**Collaborators:** Emily Morley, Evanka Amin, Prof. Mary Loveless

---

##  Overview

This project simulates nanoparticle-based cancer therapy using **PhysiCell** and the **pc4nanobio** framework. The simulations investigate four drug delivery strategies over a 30-day period on a 3D tumor spheroid model.

Simulations were conducted entirely through the **Linux CLI** by cloning and modifying the open-source `pc4nanobio` repository. 

---

##  Objective

To explore biologically realistic nanoparticle drug therapies and determine which delivery schedules offer optimal tumor suppression while minimizing regrowth.

---

## ⚙️ Methods

Implemented using `pc4nanobio`, a high-throughput cancer nanotherapy simulator built on PhysiCell. The model tracks nanoparticle internalization, drug release inside tumor cells, and phenotypic effects on proliferation and apoptosis.The logic for each of the four therapy experiments had to be implemented by editing the exisiting nanobio.cpp and PhysiCell_Settings.xml file from the **pc4nanobio** repository. 

### Therapeutic Strategies Simulated:

1. **Baseline Therapy**: Two moderate drug doses (Day 5 & 10)
2. **Metronomic Therapy**: Repeated low doses (every ~4 days)
3. **Single High-Dose Therapy**: One strong pulse on Day 5
4. **Adaptive Therapy**: Therapy ON if tumor ≥ 850 cells; OFF if ≤ 600

Drug effects were modeled either by:
- **AUC-based pharmacodynamics**, or
- **Instantaneous extracellular drug concentration**

---

##  Results Summary

- **Metronomic Therapy**: Lowest final tumor burden, best suppression
- **Adaptive Therapy**: Largest initial tumor, best % reduction, stable control
- **Baseline**: Moderate suppression
- **Single High-Dose**: Quick drop, but strong regrowth

---

##  Poster

This project culminated in an academic poster presentation. View below:

![Poster Preview](POSTER.png)

---

##  Repository Structure

| Folder             | Description                                 |
|--------------------|---------------------------------------------|
| `baseline/`         | Baseline therapy simulation files          |
| `metronomic/`       | Metronomic therapy setup & outputs         |
| `single_high_dose/` | Single-dose simulation & outputs           |
| `Advance_therapu/`  | Adaptive therapy simulation code & data    |
| `Paul.pdf`          | Framework documentation reference          |

---

##  Framework Info

Simulations were run using the [pc4nanobio](https://nanohub.org/tools/pc4nanobio) simulator, a cloud-deployable, open-source PhysiCell extension for nanoparticle therapy optimization.

More details: [https://nanohub.org/resources/pc4nanobio/about](https://nanohub.org/resources/pc4nanobio/about)

---

##  Technical Details

- Language: C++ / Python / POV-Ray
- Base: PhysiCell v1.10.4
- Internalization modeled via `advance_internalization()`
- NP drug release uses bin-based transit model
- Therapy schedules applied via `apply_therapies()`

---

##  Future Work

- Integrate cancer stem cell dynamics
- Evolve smarter therapies using genetic algorithms
- Explore longer-term therapy impacts on tumor evolution

---

##  Acknowledgments

Special thanks to [Prof. Paul Macklin](https://mathcancer.org/) for the development of PhysiCell and the pc4nanobio project.

---
