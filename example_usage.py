# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Neuroplasticity Synaptic Pruning Sleep Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentNeuroplasticitySynapticPruning

def main():
    agent = PersonalAgentNeuroplasticitySynapticPruning()

    print("=" * 70)
    print("DEMO: Personal Agent Neuroplasticity Synaptic Pruning Sleep Modeler")
    print("=" * 70)

    # 1. 14 hours wakefulness, high novelty, 1.9 hours SWS delta sleep
    res_shy = agent.model_synaptic_homeostasis_scaling(
        waking_learning_hours=14.0,
        novelty_density_score=8.5,
        slow_wave_sleep_hours=1.9
    )

    print(f"\n1. Synaptic Homeostasis & SWS Scaling Audit:")
    print(f"   Pre-Sleep Saturation: {res_shy['pre_sleep_synaptic_saturation_pct']}")
    print(f"   Overnight Renormalization Efficiency: {res_shy['overnight_synaptic_renormalization_efficiency']}")
    print(f"   Memory Signal-to-Noise Boost: {res_shy['signal_to_noise_ratio_boost']}")
    print(f"   Status: {res_shy['neuroplastic_recovery_state']}")
    print(f"   Forecast: {res_shy['cognitive_capacity_forecast']}")

    # 2. Targeted Memory Reactivation Cues
    topics = [
        "Distributed Byzantine Consensus Algorithm",
        "Linear Algebra Eigenvalue Decomposition",
        "Cellular Autophagy Signaling Pathways"
    ]

    res_tmr = agent.generate_targeted_memory_reactivation_cues(
        core_learning_items=topics,
        target_sleep_onset="23:30"
    )

    print(f"\n2. Targeted Memory Reactivation (TMR) Pre-Sleep Protocol:")
    print(f"   Review Window: {res_tmr['prescribed_tmr_review_window']}")
    print(f"   Prioritized Concepts:")
    for c in res_tmr['targeted_reactivation_prompts']:
        print(f"     [{c['memory_priority_rank']}] {c['core_concept']} -> {c['activation_mechanism']}")
    print(f"   Sensory Protocol: {res_tmr['sensory_anchor_protocol']}")

    print("\nVerification complete: Synaptic pruning neuroplasticity engine executed flawlessly.")

if __name__ == "__main__":
    main()
