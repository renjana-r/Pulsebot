import json

projects = [
    {
        "name": "PulseBot",
        "description": "Automated Python Bot Project",
        "url": "https://github.com/renjana-r/PulseBot"
    }
]

with open("projects.json", "w", encoding="utf-8") as file:
    json.dump(projects, file, indent=4)

print("Repositories fetched successfully!")
print("projects.json generated!")