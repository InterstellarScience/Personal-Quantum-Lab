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

> [!NOTE]
> This project is an educational and research-oriented simulator. It is not
> intended to represent a certified operational QKD security system.
