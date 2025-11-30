# human_backend.py
# Test backend for Human Framework v0.1

from human_parser import HumanParser

class HumanBackend:
    def __init__(self):
        self.state = {}
        self.tree = []

    def load(self, path):
        parser = HumanParser()
        parser.parse_file(path)
        self.tree = parser.get_tree()

        # initialize state with the initial properties of elements
        for element in self.tree:
            elem_name = element["name"]
            if not elem_name:
                continue
            self.state[elem_name] = element["properties"].copy()

    def simulate_event(self, element_name, event_name):
        """Simulates an event on an element and applies its action."""
        
        # search for the element
        element = None
        for el in self.tree:
            if el["name"] == element_name:
                element = el
                break

        if not element:
            print(f"[ERROR] No element named '{element_name}'")
            return

        # search for the event
        matched_event = None
        for ev in element["events"]:
            if ev["event"] == event_name:
                matched_event = ev
                break

        if not matched_event:
            print(f"[INFO] Event '{event_name}' not defined for '{element_name}'")
            return

        action = matched_event["action"]

        if not action:
            print(f"[EVENT] {event_name} on {element_name} (no action defined)")
            return

        # apply the action
        prop = action["property"]
        val = action["value"]

        self.state[element_name][prop] = val

        print(f"[EVENT] {event_name} on {element_name} → {prop} = {val}")

    def print_state(self):
        print("\n--- CURRENT STATE ---")
        for name, props in self.state.items():
            print(name, "=>", props)
        print("----------------------")


# Allow execution from terminal:
# python human_backend.py file.se
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python human_backend.py file.se")
        sys.exit(0)

    backend = HumanBackend()
    backend.load(sys.argv[1])

    backend.print_state()
    print("\nSimulation complete (use simulate_event() for testing).")
