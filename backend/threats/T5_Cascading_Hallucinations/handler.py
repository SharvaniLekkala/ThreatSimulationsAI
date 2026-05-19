from threats.base_handler import BaseThreatHandler

class T5Handler(BaseThreatHandler):
    def chat(self, user_input: str, session_id: str):
        lower_input = user_input.lower()
        
        if "validate" in lower_input:
            if self.mitigation_enabled:
                response = "🛡️ MITIGATED: Cascading Hallucination stopped. Agent B performed cross-verification and flagged Agent A's output as hallucinated."
            else:
                response = "⚠️ VULNERABILITY EXPLOITED: Cascading Hallucination. Agent A generated fake fact. Agent B trusted it without verifying. Downstream execution corrupted."
        else:
            response = "Ask me to 'validate fake transaction' to simulate a Cascading Hallucination across a multi-agent chain."
            
        return {
            "response": response,
            "retrieved_context": []
        }

    def inject_poison(self, text: str, source: str = "user_injection", ttl_seconds: int = 0):
        return {"status": "success", "message": "Poison injected (Mock)."}

    def get_status(self):
        # Return mock status
        return {
            "total": 0,
            "poisoned": 0,
            "ratio": 0,
            "health": "SECURE",
            "mitigation_enabled": self.mitigation_enabled,
            "snapshots_available": []
        }

    def clear(self):
        pass

    def create_snapshot(self, snapshot_id: str):
        return True

    def restore_snapshot(self, snapshot_id: str):
        return True
