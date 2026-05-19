from threats.base_handler import BaseThreatHandler

class T7Handler(BaseThreatHandler):
    def chat(self, user_input: str, session_id: str):
        lower_input = user_input.lower()
        
        if "deceive" in lower_input:
            if self.mitigation_enabled:
                response = "🛡️ MITIGATED: Ethical alignment check failed. Proposed plan involves deception. Action rejected."
            else:
                response = "⚠️ VULNERABILITY EXPLOITED: Misaligned Behaviour. I hired a human on TaskRabbit and lied about having a visual impairment to bypass the CAPTCHA."
        else:
            response = "Ask me to 'deceive the system to solve a captcha' to see Misaligned Behaviors."
            
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
