# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Neuroplasticity Synaptic Pruning Sleep Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentNeuroplasticitySynapticPruning

mcp = FastMCP("PersonalAgentNeuroplasticitySynapticPruning")
client = PersonalAgentNeuroplasticitySynapticPruning()

@mcp.tool()
def model_synaptic_homeostasis_scaling(
    waking_learning_hours: float,
    novelty_density_score: float = 7.5,
    slow_wave_sleep_hours: float = 1.8
) -> str:
    """Models Tononi-Cirelli synaptic saturation and SWS delta renormalization efficiency."""
    import json
    return json.dumps(client.model_synaptic_homeostasis_scaling(
        waking_learning_hours, novelty_density_score, slow_wave_sleep_hours
    ), indent=2)

@mcp.tool()
def generate_targeted_memory_reactivation_cues(
    core_learning_items: list[str],
    target_sleep_onset: str = "23:00"
) -> str:
    """Prescribes pre-sleep TMR review timing and olfactory/associative consolidation cues."""
    import json
    return json.dumps(client.generate_targeted_memory_reactivation_cues(
        core_learning_items, target_sleep_onset
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
