## Free-Space Optical QKD Simulator

A simulator for quantum key distribution over terrestrial and satellite free-space optical channels. 

!!! Status: This project is currently under active development. !!!

## Development Status

The simulator is currently under active development.

### Implemented

- [x] Modular BB84 protocol
- [x] Random bit and basis generation
- [x] Qiskit-based single-qubit simulation
- [x] Fast Monte Carlo simulation mode
- [x] Basis sifting
- [x] Intercept–resend attack with adjustable interception probability
- [x] Exact QBER calculation
- [x] Public-sampling QBER estimation
- [x] QBER-based abort decision
- [x] Removal of publicly disclosed test bits
- [x] Weak coherent pulse source using Poisson statistics
- [x] Vacuum, single-photon and multiphoton classification
- [x] Configurable channel transmittance
- [x] Photon loss through the channel
- [x] Detector efficiency
- [x] Detector dark counts
- [x] Nondetection handling
- [x] Validation against the theoretical relation (QBER)
- [x] Receiver and optical misalignment errors
- [x] Background-light noise

### Core Features Still in Development

- [ ] Distance-dependent geometric channel loss
- [ ] Beam-divergence and receiver-aperture model
- [ ] Atmospheric extinction
- [ ] Sifted-key rate calculation
- [ ] Secure-key rate estimation
- [ ] Error-correction leakage model
- [ ] Privacy-amplification estimate
- [ ] Automated parameter sweeps
- [ ] QBER, detection-rate and key-rate plots
- [ ] Unit and integration tests
- [ ] Configuration file for simulation parameters
- [ ] Complete usage and physics documentation

### Planned Advanced Extensions

- [ ] Decoy-state BB84
- [ ] Photon-number-splitting attack analysis
- [ ] Atmospheric turbulence
- [ ] Beam wandering
- [ ] Pointing and tracking errors
- [ ] Finite-key statistical analysis
- [ ] Time-varying weather conditions
- [ ] Satellite-link geometry and orbital passes
- [ ] Interactive visualization or dashboard


### References

1. C. H. Bennett and G. Brassard,  
   “Quantum Cryptography: Public Key Distribution and Coin Tossing,”  
   *Proceedings of the IEEE International Conference on Computers, Systems and Signal Processing*, pp. 175–179, 1984.  
   [Original manuscript](https://arxiv.org/abs/2003.06557)

2. M. A. Nielsen and I. L. Chuang,  
   *Quantum Computation and Quantum Information*, 10th Anniversary ed.  
   Cambridge University Press, 2010.  
   [Publisher page](https://doi.org/10.1017/CBO9780511976667)

3. N. Gisin, G. Ribordy, W. Tittel, and H. Zbinden,  
   “Quantum Cryptography,”  
   *Reviews of Modern Physics*, vol. 74, no. 1, pp. 145–195, 2002.  
   [DOI](https://doi.org/10.1103/RevModPhys.74.145)

4. P. W. Shor and J. Preskill,  
   “Simple Proof of Security of the BB84 Quantum Key Distribution Protocol,”  
   *Physical Review Letters*, vol. 85, no. 2, pp. 441–444, 2000.  
   [DOI](https://doi.org/10.1103/PhysRevLett.85.441)

5. V. Scarani, H. Bechmann-Pasquinucci, N. J. Cerf, M. Dušek,  
   N. Lütkenhaus, and M. Peev,  
   “The Security of Practical Quantum Key Distribution,”  
   *Reviews of Modern Physics*, vol. 81, no. 3, pp. 1301–1350, 2009.  
   [DOI](https://doi.org/10.1103/RevModPhys.81.1301)

6. H.-K. Lo, X. Ma, and K. Chen,  
   “Decoy State Quantum Key Distribution,”  
   *Physical Review Letters*, vol. 94, no. 23, 230504, 2005.  
   [DOI](https://doi.org/10.1103/PhysRevLett.94.230504)

7. X. Ma, B. Qi, Y. Zhao, and H.-K. Lo,  
   “Practical Decoy State for Quantum Key Distribution,”  
   *Physical Review A*, vol. 72, no. 1, 012326, 2005.  
   [DOI](https://doi.org/10.1103/PhysRevA.72.012326)

8. W. T. Buttler, R. J. Hughes, P. G. Kwiat, G. G. Luther,  
   G. L. Morgan, J. E. Nordholt, C. G. Peterson, and C. M. Simmons,  
   “Free-Space Quantum Key Distribution,” 1998.  
   [arXiv:quant-ph/9801006](https://arxiv.org/abs/quant-ph/9801006)

9. A. Carrasco-Casado, V. Fernández, and N. Denisenko,  
   “Free-Space Quantum Key Distribution,” in  
   *Optical Wireless Communications: System and Channel Modelling with MATLAB*,  
   pp. 589–607, CRC Press, 2016.  
   [arXiv:1611.03529](https://arxiv.org/abs/1611.03529)

10. A. E. Siegman,  
    *Lasers*. University Science Books, 1986.

11. L. C. Andrews and R. L. Phillips,  
    *Laser Beam Propagation Through Random Media*, 2nd ed.  
    SPIE Press, 2005.  
    [DOI](https://doi.org/10.1117/3.626196)

12. H. Kaushal and G. Kaddoum,  
    “Optical Communication in Space: Challenges and Mitigation Techniques,”  
    *IEEE Communications Surveys & Tutorials*, vol. 19, no. 1,  
    pp. 57–96, 2017.  
    [DOI](https://doi.org/10.1109/COMST.2016.2603518)

13. J. Zhang, M. A. Itzler, H. Zbinden, and J.-W. Pan,  
    “Advances in InGaAs/InP Single-Photon Detector Systems for Quantum Communication,”  
    *Light: Science & Applications*, vol. 4, e286, 2015.  
    [DOI](https://doi.org/10.1038/lsa.2015.59)

14. IBM Quantum,  
    “Exact and Noisy Simulation with Qiskit Aer,”  
    *IBM Quantum Documentation*.  
    [Documentation](https://docs.quantum.ibm.com/guides/simulate-with-qiskit-aer)


### Acknowledgements

ChatGPT by OpenAI is used as an AI-assisted mentor for conceptual guidance, physics explanations, code review, and debugging support. All final modelling and implementation decisions remain the responsibility of the author. An image of an experimental example setup was done by AI using prompts of some of the formulae and concepts I have learned and used during the programming sessions.

> [!NOTE]
> This project is an educational and research-oriented simulator. It is not
> intended to represent a certified operational QKD security system.
