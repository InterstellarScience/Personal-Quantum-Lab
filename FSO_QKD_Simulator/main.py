## Import necessary packages
from config import(DEFAULT_CONFIG)
from simulation.sweep import(run_distance_sweep)
from visualisation.plots import(plot_distance_sweep)

## Different distances and many repetitions
distances = [100, 500, 1000, 2000, 5000]
repetitions = 20

## Carry out experiments
sweep_results = run_distance_sweep(DEFAULT_CONFIG, distances, repetitions)

## Results
for result in sweep_results:
    print(
        f"Distance: {result['distance']} m | "
        f"Transmittance: {result['channel_transmittance']:.4f} | "
        f"QBER: {result['estimated_qber'] * 100:.2f}% "
        f"± {result['qber_std'] * 100:.2f}% | "
        f"Secure-key rate: {result['secure_key_rate']:.2f} "
        f"± {result['secure_key_rate_std']:.2f} bits/s"
    )
    
plot_distance_sweep(sweep_results)