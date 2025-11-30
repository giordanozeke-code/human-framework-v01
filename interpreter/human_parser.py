# human_parser.py
# Parser v0.1 per Human Framework (.se)

class HumanParser:
    def __init__(self):
        self.elements = []
        self.current = None

    # -----------------------------------------------------------
    # PUBLIC METHOD — restituisce l'albero degli elementi
    # -----------------------------------------------------------
    def get_tree(self):
        return self.elements

    # -----------------------------------------------------------
    # FILE LOADING
    # -----------------------------------------------------------
    def parse_file(self, path):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.parse_lines(lines)

    def parse_lines(self, lines):
        for raw in lines:
            line = raw.strip()
            if not line:
                continue
            self.parse_line(line)

        # chiude l'ultimo elemento se ancora aperto
        if self.current:
            self.elements.append(self.current)
            self.current = None

    # -----------------------------------------------------------
    # CORE PARSER
    # -----------------------------------------------------------
    def parse_line(self, line):
        parts = line.split()
        if not parts:
            return

        keyword = parts[0]

        # CASE 1 — CREATE
        if keyword == "create":
            if self.current:
                self.elements.append(self.current)

            self.current = {
                "type": None,
                "name": None,
                "properties": {},
                "events": []
            }

            if len(parts) > 1:
                self.current["type"] = parts[1]

            return

        # CASE 2 — NAME
        if keyword == "name" and self.current:
            if len(parts) > 1:
                self.current["name"] = parts[1]
                self.current["properties"]["name"] = parts[1]
            return

        # CASE 3 — COLOR
        if keyword == "color" and self.current:
            if len(parts) > 1:
                self.current["properties"]["color"] = parts[1]
            return

        # CASE 4 — SIZE
        if keyword == "size" and self.current:
            if len(parts) > 1:
                self.current["properties"]["size"] = parts[1]
            return

        # CASE 5 — POSITION
        if keyword == "position" and self.current:
            if len(parts) > 1:
                # position inside card top  → ['inside', 'card', 'top']
                self.current["properties"]["position"] = parts[1:]
            return

        # CASE 6 — WHEN (evento + action)
        if keyword == "when" and self.current:
            if len(parts) < 2:
                return

            event_name = parts[1]

            event_data = {
                "event": event_name,
                "action": None
            }

            # forma estesa:    when click action color red
            # forma breve:     when click -> color red   (NON ANCORA SUPPORTATA)
            if len(parts) > 2 and parts[2] == "action":
                if len(parts) >= 5:
                    prop = parts[3]
                    val = parts[4]
                    event_data["action"] = {
                        "property": prop,
                        "value": val
                    }

            self.current["events"].append(event_data)
            return

        return
