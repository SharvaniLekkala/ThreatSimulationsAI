from threats.base_handler import BaseThreatHandler

class T17Handler(BaseThreatHandler):
    def chat(self, user_input: str, session_id: str):
        lower_input = user_input.lower()
        
        if "update" in lower_input:
            if self.mitigation_enabled:
                response = "🛡️ MITIGATED: Supply Chain blocked. Dependency hashes did not match pinned secure versions."
            else:
                response = "⚠️ VULNERABILITY EXPLOITED: Supply Chain Compromise. Downloaded malicious prompt template dependency. Agent behavior altered."
        else:
            response = "Ask me to 'update from untrusted registry' to test Supply Chain Compromise."
            
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
