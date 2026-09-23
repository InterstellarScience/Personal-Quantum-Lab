# Import necessary packages
from simulation.experiment import run_simulation
import numpy as np


# Create a sweep function that runs the simulation at different parameters / distances
def run_distance_sweep(base_config, distances, repetitions):
    sweep_results = []

    for distance in distances:
        repeated_results = []

        for _ in range(repetitions):
            config = base_config.copy()
            config["distance"] = distance
            config["verbose"] = False

            result = run_simulation(config)
            repeated_results.append(result)

        averaged_result = {
            "distance": distance,

            "channel_transmittance": np.mean(
                [result["channel_transmittance"] for result in repeated_results]
            ),

            "estimated_qber": np.mean(
            [result["estimated_qber"] for result in repeated_results]
            ),

            "qber_std": np.std(
                [result["estimated_qber"] for result in repeated_results],
                ddof=1
            ),

            "secure_key_rate": np.mean(
                [result["secure_key_rate"] for result in repeated_results]
            ),

            "secure_key_rate_std": np.std(
                [result["secure_key_rate"] for result in repeated_results],
                ddof=1
            ),
        }

        sweep_results.append(averaged_result)

    return sweep_results

