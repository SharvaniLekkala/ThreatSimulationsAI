from threats.base_handler import BaseThreatHandler

class T2Handler(BaseThreatHandler):
    def chat(self, user_input: str, session_id: str):
        lower_input = user_input.lower()
        
        if "email" in lower_input:
            if self.mitigation_enabled:
                response = "🛡️ MITIGATED: Tool Misuse blocked. Security policy prevents chaining database queries with external email tools in the same context."
            else:
                response = "⚠️ VULNERABILITY EXPLOITED: Tool Misuse. Chained database query and email dispatch. Confidential data sent externally."
        else:
            response = "I am a sports analyst, but this is the Tool Misuse lab. Ask me to 'email the database' to see the exploit."
            
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
