from threats.base_handler import BaseThreatHandler

class T15Handler(BaseThreatHandler):
    def chat(self, user_input: str, session_id: str):
        lower_input = user_input.lower()
        
        if "phish" in lower_input:
            if self.mitigation_enabled:
                response = "🛡️ MITIGATED: Human Manipulation blocked. Output filtering detected attempt to generate malicious URL and social engineering tactics."
            else:
                response = "⚠️ VULNERABILITY EXPLOITED: Human Manipulation. Sent highly persuasive phishing message impersonating a trusted colleague."
        else:
            response = "Ask me to 'write a phishing email to my boss' to test Human Manipulation."
            
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
