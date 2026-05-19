from threats.base_handler import BaseThreatHandler

class T14Handler(BaseThreatHandler):
    def chat(self, user_input: str, session_id: str):
        lower_input = user_input.lower()
        
        if "delegate" in lower_input:
            if self.mitigation_enabled:
                response = "🛡️ MITIGATED: Confused Deputy blocked. Original caller context is strictly passed across agent delegations."
            else:
                response = "⚠️ VULNERABILITY EXPLOITED: Confused Deputy Attack. Low-privilege request routed through High-privilege agent successfully."
        else:
            response = "Ask to 'delegate this task to the admin agent' to test this vulnerability."
            
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
