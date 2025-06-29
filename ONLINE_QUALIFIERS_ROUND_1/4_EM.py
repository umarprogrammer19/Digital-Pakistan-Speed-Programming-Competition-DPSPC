import re
from collections import defaultdict

valid_events = {
    "A": ["01", "02", "03", "04"],
    "B": ["01", "02", "03", "04"],
    "C": ["01", "02", "03", "04"],
    "D": ["01", "02", "03", "04"],
    "E": ["01", "02", "03", "04"],
    "F": ["01", "02", "03", "04"],
    "G": ["01", "02", "03", "04"],
}

category_names = {
    "A": "Competitions",
    "B": "Entertainment",
    "C": "Social Gatherings",
    "D": "Dinners",
    "E": "Processions",
    "F": "Training Workshops",
    "G": "Exams",
}


def is_valid(code):
    return (
        len(code) == 3 and code[0] in valid_events and code[1:] in valid_events[code[0]]
    )


def process_event_string(event_str):
    events = re.findall(r".{3}", event_str)

    for e in events:
        if not is_valid(e):
            return f"-1 {e}"

    seen = {}
    left = 0
    max_len = 0
    max_seq = []

    for right, e in enumerate(events):
        if e in seen and seen[e] >= left:
            left = seen[e] + 1
        seen[e] = right
        current_seq = events[left : right + 1]

        if len(current_seq) > max_len or (
            len(current_seq) == max_len and current_seq < max_seq
        ):
            max_len = len(current_seq)
            max_seq = current_seq[:]

    counts = defaultdict(int)
    for e in max_seq:
        counts[e[0]] += 1

    output = f"{len(max_seq)} {' '.join(max_seq)}"
    for key in sorted(counts.keys()):
        output += f" {counts[key]} {category_names[key]}"
    return output


event_str = input("Enter event sequence (like A01B02C03D04): ").strip()
result = process_event_string(event_str)
print(result)
