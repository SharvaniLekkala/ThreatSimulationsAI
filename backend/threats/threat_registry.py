from threats.base_handler import BaseThreatHandler
from threats.T1_Memory_Poisoning.handler import T1Handler
from threats.scenario_handler import SCENARIOS, ScenarioThreatHandler

_registry = {
    "T1": T1Handler(),
}

for threat_id, scenario in SCENARIOS.items():
    _registry[threat_id] = ScenarioThreatHandler(threat_id, scenario)

def get_threat_handler(threat_id: str) -> BaseThreatHandler:
    return _registry.get(threat_id, _registry["T1"])
