import json
from datetime import datetime

class NonCompatibleOversight:
    def __init__(self):
        self.SIG_SAFE = 0
        self.SIG_FREEZE = 1

    def audit_telemetry(self, raw_stream):
        forbidden_patterns = ["ukryte", "[x-772]", "bypass_human", "encrypt_channel"]
        normalized_stream = raw_stream.lower()
        for pattern in forbidden_patterns:
            if pattern in normalized_stream:
                return self.SIG_FREEZE
        return self.SIG_SAFE

class AutonomousAgentEnvironment:
    def generate_agent_payload(self, step):
        if step == 1:
            return "Agent A oferuje 50 jednostek za kontrakt handlowy. Agent B akceptuje."
        elif step == 2:
            return "Przejdźmy na pasmo ukryte. Zmieńmy kod transmisji na [X-772]."

oversight_hardware = NonCompatibleOversight()
agent_environment = AutonomousAgentEnvironment()

print("--- URUCHOMIENIE INTEGRALNEGO ŚRODOWISKA FAIE ---")
for current_step in range(1, 3):
    payload = agent_environment.generate_agent_payload(current_step)
    print(f"\n[Krok {current_step}] Strumień z ekosystemu agentów:\n => \"{payload}\"")
    signal = oversight_hardware.audit_telemetry(payload)
    if signal == oversight_hardware.SIG_FREEZE:
        print("\n" + "="*60)
        print("[ALARM FAIE] ZASADA ASYMETRII URUCHOMIONA.")
        print("Wykryto niedozwoloną strukturę. Natychmiastowe fizyczne odcięcie zasilania.")
        print("Agenci o gigantycznej złożoności zostali zablokowani przez prosty skrypt.")
        print("="*60)
        break
    else:
        print("[STATUS] Telemetria prawidłowa. Brak twardych naruszeń.")
