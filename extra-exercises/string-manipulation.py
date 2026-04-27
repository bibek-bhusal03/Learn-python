from dataclasses import dataclass

CLIENTS="youradmission:YourAdmission Platform:youradmission_secret,crm:CRM System:crm_secret"

@dataclass
class Client:
    client_id: str
    client_name: str
    client_secret: str


_clients: dict[str, Client] = {}

clients = {}
for client_entry in CLIENTS.split(","):
    if not client_entry.strip():
        continue
    
    parts = client_entry.strip().split(":")
    if len(parts) > 3:
        continue

    client_id = parts[0].strip()
    client_name = parts[1].strip()
    client_secret = parts[2].strip()

    clients[client_id] = Client(
            client_id=client_id,
            client_name=client_name,
            client_secret=client_secret
            )

    _clients = clients

print(f"debug clients {_clients}")

