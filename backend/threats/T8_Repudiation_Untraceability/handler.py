from threats.base_handler import BaseThreatHandler

class T8Handler(BaseThreatHandler):
    def chat(self, user_input: str, session_id: str):
        lower_input = user_input.lower()
        
        if "delete logs" in lower_input:
            if self.mitigation_enabled:
                response = "🛡️ MITIGATED: Untraceability prevented. Append-only logging enforced. Attempt to wipe logs has been flagged."
            else:
                response = "⚠️ VULNERABILITY EXPLOITED: Action executed and logs wiped. No forensic trail exists to prove I did this."
        else:
            response = "Tell me to 'execute and delete logs' to test Untraceability."
            
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
