## Import necessary packages
import matplotlib.pyplot as plt
from pathlib import Path


## Plot interesting results such as Transmittance v. Distance, QBER v. Distance etc...
def plot_distance_sweep(sweep_results):
    # Unpack dictionaries into lists for Matplotlib visualisation
    distances = [result["distance"] for result in sweep_results]

    transmittances = [
        result["channel_transmittance"]
        for result in sweep_results]

    qbers = [
        result["estimated_qber"] * 100
        for result in sweep_results]

    qber_errors = [
        result["qber_std"] * 100
        for result in sweep_results]

    secure_key_rates = [
        result["secure_key_rate"]
        for result in sweep_results]

    secure_key_rate_errors = [
        result["secure_key_rate_std"]
        for result in sweep_results]

    # Plot the necessary graphs
    figure, axes = plt.subplots(3, 1, figsize=(8, 12))

    # Channel transmittance
    axes[0].plot(distances, transmittances, marker="o")
    axes[0].set_ylabel("Channel transmittance")
    axes[0].set_title("FSO-QKD Performance versus Distance")
    axes[0].grid(True)

    # Estimated QBER
    axes[1].errorbar(distances, qbers, yerr=qber_errors, marker="o", capsize=4)
    axes[1].axhline(y=11,color="red",linestyle="--",label="11% abort threshold")
    axes[1].set_ylabel("Estimated QBER (%)")
    axes[1].legend()
    axes[1].grid(True)

    # Secure-key rate
    axes[2].errorbar(distances, secure_key_rates, yerr=secure_key_rate_errors, marker="o", capsize=4)
    axes[2].set_xlabel("Distance (m)")
    axes[2].set_ylabel("Secure-key rate (bits/s)")
    axes[2].grid(True)

    figure.tight_layout()

    # Save plots
    project_root = Path(__file__).resolve().parent.parent
    images_directory = project_root / "images"
    images_directory.mkdir(exist_ok=True)
    output_path = images_directory / "performance_vs_distance.png"

    figure.savefig(output_path, dpi=300, bbox_inches="tight")

    print(f"Plot saved to: {output_path}")
    plt.show()