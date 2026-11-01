# -*- coding: utf-8 -*-
"""
Personal Agent Neuroplasticity Synaptic Pruning Sleep Client
Zero-dependency Tononi-Cirelli Synaptic Homeostasis Hypothesis (SHY) modeler, slow-wave
sleep (SWS) down-selection renormalizer, and Targeted Memory Reactivation (TMR) scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentNeuroplasticitySynapticPruning:
    """
    Quantifies wakeful synaptic potentiation energy demands, models Slow-Wave Sleep (SWS)
    down-scaling normalization, and formulates Targeted Memory Reactivation (TMR) consolidation cues.
    """

    def model_synaptic_homeostasis_scaling(
        self,
        waking_learning_hours: float,
        novelty_density_score: float = 7.5,
        slow_wave_sleep_hours: float = 1.8
    ) -> Dict[str, Any]:
        """
        Models the Tononi & Cirelli Synaptic Homeostasis Hypothesis (SHY):
        Wakefulness drives net synaptic potentiation, consuming cellular ATP, space, and protein.
        Slow-Wave Sleep (N3 delta oscillations) renormalizes synaptic weight by ~18-20%,
        pruning noise and consolidating high-value signal into neocortical long-term storage.
        """
        wake_h = max(2.0, min(24.0, float(waking_learning_hours)))
        novelty = max(1.0, min(10.0, float(novelty_density_score)))
        sws_h = max(0.0, min(5.0, float(slow_wave_sleep_hours)))

        # Daytime synaptic potentiation accumulation (0 - 100% capacity)
        potentiation_load = (wake_h * 4.5) * (novelty / 5.0)
        synaptic_saturation_pct = round(min(100.0, potentiation_load), 1)

        # Overnight Slow-Wave Sleep down-selection capacity
        # Each hour of deep SWS delta sleep down-scales ~35% of cumulative daily potentiation
        pruning_capacity = sws_h * 36.0
        net_retained_potentiation = max(0.0, synaptic_saturation_pct - pruning_capacity)
        renormalization_efficiency_pct = round(min(100.0, (pruning_capacity / max(1.0, synaptic_saturation_pct)) * 100.0), 1)

        # Signal-to-noise ratio boost: pruning weak connections sharpens core memories
        snr_boost_pct = round(min(32.0, sws_h * 16.5), 1)

        if renormalization_efficiency_pct >= 90.0:
            status = "Complete Synaptic Reset (Optimal Next-Day Neuroplasticity)"
            guidance = "Synaptic weight fully renormalized. Peak executive working memory and learning capacity available."
        elif renormalization_efficiency_pct >= 60.0:
            status = "Partial Synaptic Down-Selection (Mild Saturation Carry-Over)"
            guidance = "Adequate recovery; however, complex abstract learning capacity slightly diminished by noon."
        else:
            status = "Severe Synaptic Saturation / Insufficient Delta Sleep (Cognitive Gridlock)"
            guidance = "Mitochondrial and synaptic exhaustion. High susceptibility to proactive interference and mental brain fog."

        return {
            "waking_learning_hours": wake_h,
            "novelty_density_score": f"{novelty} / 10",
            "slow_wave_sleep_duration_hours": sws_h,
            "pre_sleep_synaptic_saturation_pct": f"{synaptic_saturation_pct}% of neural capacity",
            "overnight_synaptic_renormalization_efficiency": f"{renormalization_efficiency_pct}%",
            "signal_to_noise_ratio_boost": f"+{snr_boost_pct}% memory consolidation",
            "neuroplastic_recovery_state": status,
            "cognitive_capacity_forecast": guidance
        }

    def generate_targeted_memory_reactivation_cues(
        self,
        core_learning_items: List[str],
        target_sleep_onset: str = "23:00"
    ) -> Dict[str, Any]:
        """
        Prescribes pre-sleep Targeted Memory Reactivation (TMR) review windows and sensory
        anchors to bias hippocampal slow-oscillation sharp-wave ripple replays during deep sleep.
        """
        def parse_h(t_str: str) -> float:
            parts = str(t_str).split(":")
            return float(parts[0]) + (float(parts[1]) / 60.0 if len(parts) > 1 else 0.0)

        def format_h(h_val: float) -> str:
            hh = int(h_val) % 24
            mm = int((h_val - int(h_val)) * 60)
            return f"{hh:02d}:{mm:02d}"

        sleep_h = parse_h(target_sleep_onset)
        review_start_h = (sleep_h - (25.0 / 60.0)) % 24.0 # 25 minutes before bed

        items = core_learning_items if core_learning_items else ["Complex Algorithm Architecture", "New Language Vocabulary"]

        structured_cues = []
        for idx, item in enumerate(items[:5], 1):
            structured_cues.append({
                "memory_priority_rank": idx,
                "core_concept": str(item),
                "activation_mechanism": f"Active retrieval for 90 seconds followed by 10-second visualization of structural hierarchy."
            })

        return {
            "target_sleep_onset_time": target_sleep_onset,
            "prescribed_tmr_review_window": f"{format_h(review_start_h)} - {format_h(sleep_h)} (25-minute calm review)",
            "memory_items_prioritized_count": len(structured_cues),
            "targeted_reactivation_prompts": structured_cues,
            "sensory_anchor_protocol": "Pair pre-sleep review with a subtle distinct natural scent (e.g. lavender or cedarwood). Olfactory cues directly bypass the thalamus and stimulate hippocampal replays without waking the brain.",
            "sleep_architecture_safeguard": "Review must be conducted in dim, warm light (<= 20 lux) with zero blue light or active screen interactions."
        }
