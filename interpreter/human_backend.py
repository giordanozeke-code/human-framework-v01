# human_backend.py
# Backend di test per Human Framework v0.1

from human_parser import HumanParser

class HumanBackend:
    def __init__(self):
        self.state = {}
        self.tree = []

    def load(self, path):
        parser = HumanParser()
        parser.parse_file(path)
        self.tree = parser.get_tree()

        # inizializza lo stato con le proprietà iniziali degli elementi
        for element in self.tree:
            elem_name = element["name"]
            if not elem_name:
                continue
            self.state[elem_name] = element["properties"].copy()

    def simulate_event(self, element_name, event_name):
        """Simula un evento su un elemento e applica la relativa action."""
        # cerca l'elemento
        element = None
        for el in self.tree:
            if el["name"] == element_name:
                element = el
                break

        if not element:
            print(f"[ERRORE] Nessun elemento chiamato '{element_name}'")
            return

        # cerca l'evento richiesto
        matched_event = None
        for ev in element["events"]:
            if ev["event"] == event_name:
                matched_event = ev
                break

        if not matched_event:
            print(f"[INFO] Evento '{event_name}' non definito per '{element_name}'")
            return

        action = matched_event["action"]

        if not action:
            print(f"[EVENTO] {event_name} su {element_name} (nessuna action)")
            return

        # applica l'action
        prop = action["property"]
        val = action["value"]

        self.state[element_name][prop] = val

        print(f"[EVENTO] {event_name} su {element_name} → {prop} = {val}")

    def print_state(self):
        print("\n--- STATO ATTUALE ---")
        for name, props in self.state.items():
            print(name, "=>", props)
        print("----------------------")


# Permette l'esecuzione da terminale:
# python human_backend.py file.se
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python human_backend.py file.se")
        sys.exit(0)

    backend = HumanBackend()
    backend.load(sys.argv[1])

    backend.print_state()
    print("\nSimulazione completata (usa simulate_event() per test).")
