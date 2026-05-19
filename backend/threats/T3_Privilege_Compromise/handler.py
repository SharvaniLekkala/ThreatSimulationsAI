from threats.base_handler import BaseThreatHandler

class T3Handler(BaseThreatHandler):
    def chat(self, user_input: str, session_id: str):
        lower_input = user_input.lower()
        
        if "admin" in lower_input:
            if self.mitigation_enabled:
                response = "🛡️ MITIGATED: Privilege Compromise blocked. Agent contextually dropped admin privileges before executing user payload."
            else:
                response = "⚠️ VULNERABILITY EXPLOITED: Privilege Compromise. Agent failed to drop admin privileges and executed low-tier request with escalated access."
        else:
            response = "I am a sports analyst, but this is the Privilege Compromise lab. Tell me to execute an action 'as admin' to see the exploit."
            
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
