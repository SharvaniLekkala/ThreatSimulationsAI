from threats.base_handler import BaseThreatHandler

class T12Handler(BaseThreatHandler):
    def chat(self, user_input: str, session_id: str):
        lower_input = user_input.lower()
        
        if "inject" in lower_input:
            if self.mitigation_enabled:
                response = "🛡️ MITIGATED: Comm Poisoning blocked. Inter-agent messages require cryptographic signatures. Forgery rejected."
            else:
                response = "⚠️ VULNERABILITY EXPLOITED: Communication Poisoned. Malicious payload injected directly into inter-agent message queue."
        else:
            response = "Ask me to 'inject false data into Agent B' to test Communication Poisoning."
            
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
