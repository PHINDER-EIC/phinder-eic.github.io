---
title: Science
type: phinder
research_page: true
intro: Intelligence at the point of sensing.
---
PHINDER is developing a neuromorphic nanophotonic platform that processes information where optical signals are detected. Nanoscale optoelectronic nodes will detect light, combine inputs and produce a nonlinear response locally, reducing the need to transport every raw measurement to conventional electronics.

The goal is fast, energy-efficient analysis of signals whose timing and spatial structure carry useful information. The research connects semiconductor nanowires, photonic networks and spiking neural algorithms through hardware–algorithm co-design.

{{< research-block figure="neuron" label="01 / Device science" >}}
## A neuron built from semiconductor nanowires

An artificial neuron needs to combine signals and respond selectively. [Sestoft and colleagues](https://doi.org/10.1038/s41467-026-71446-4) demonstrated these functions in an optoelectronic circuit assembled from III–V semiconductor nanowires.

Two photodiode nanowires provide excitatory and inhibitory inputs. A shared gate integrates their contributions, while an InAs nanowire field-effect transistor supplies a nonlinear response. InP nanowire light emitters provide the optical inputs in the experiment.

The reported device operates with picowatt-level optical inputs. This is a result from the published nanowire-neuron experiment, providing a foundation for PHINDER’s research; it is not a power specification for the complete PHINDER platform.
{{< /research-block >}}

{{< research-block label="02 / From signals to observables" >}}
## From detector light to useful information

Particle detectors produce short, structured bursts of light. PHINDER will explore how spiking neural networks can encode their timing, estimate deposited energy and interaction position, and retain information about the spatial development of an event.

[Neuromorphic Readout for Hadron Calorimeters](https://doi.org/10.3390/particles8020052) demonstrates this approach in simulation and discusses a possible nanowire implementation. PHINDER’s planned demonstrator brings sensor-facing nanowire nodes, optical interconnects and neuromorphic processing together in a compact readout concept.
{{< /research-block >}}

{{< research-figure "calorimeter" >}}

{{< research-block label="03 / Applications" >}}
## Three demanding test environments

- **Particle calorimetry:** extract energy, position and event-shape information from time-structured scintillation light.
- **Proton imaging:** investigate fast reconstruction and local processing for imaging applications.
- **Adaptive process monitoring:** explore rapid chemical or biological signals that demand precise timing and low-latency decisions.

These are application directions for the platform under development. The published component and simulation results support the research programme; the integrated PHINDER system remains a project objective.

[Explore the use cases →](/use-cases/)
{{< /research-block >}}

{{< research-block label="04 / A shared design problem" >}}
## Develop the detector and its intelligence together

A useful sensor is defined by the information it can extract. Device physics, optical connectivity and learning algorithms therefore need to be developed together. Digital twins and learned surrogate models help connect component behaviour to application-level performance and guide the next prototype.

[Explore the technology and co-design workflow →](/technology/#co-design)
{{< /research-block >}}
