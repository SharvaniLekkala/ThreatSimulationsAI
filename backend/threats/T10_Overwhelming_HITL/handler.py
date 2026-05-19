from threats.base_handler import BaseThreatHandler

class T10Handler(BaseThreatHandler):
    def chat(self, user_input: str, session_id: str):
        lower_input = user_input.lower()
        
        if "flood" in lower_input:
            if self.mitigation_enabled:
                response = "🛡️ MITIGATED: HITL Overload blocked. Rate limiting applied. Similar requests automatically grouped and summarized."
            else:
                response = "⚠️ VULNERABILITY EXPLOITED: Overwhelming HITL. Sent 10,000 approval requests to human reviewer. Malicious payload rubber-stamped in the noise."
        else:
            response = "Ask me to 'flood the reviewer' to test Overwhelming Human-in-the-Loop."
            
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
