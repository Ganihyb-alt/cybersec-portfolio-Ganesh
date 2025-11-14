#!/usr/bin/env python3
"""
KQL-Hunter - KQL Query Generator for Microsoft Defender Hunting
Usage examples:
  python generator.py --type process --value "powershell.exe"
  python generator.py --type ip --value "192.168.1.10"
  python generator.py --type filehash --value "abc123..."
"""

import argparse
from datetime import datetime

# KQL Templates for different IOC types
TEMPLATES = {
    "process": (
        "DeviceProcessEvents\n"
        "| where Timestamp >= ago(7d)\n"
        "| where FileName =~ '{v}'\n"
        "| project Timestamp, DeviceName, InitiatingProcessFileName, CommandLine, FolderPath"
    ),
    "ip": (
        "DeviceNetworkEvents\n"
        "| where Timestamp >= ago(7d)\n"
        "| where RemoteIP == '{v}' or LocalIP == '{v}'\n"
        "| project Timestamp, DeviceName, InitiatingProcessFileName, RemoteIP, RemotePort, Protocol"
    ),
    "filehash": (
        "DeviceFileEvents\n"
        "| where Timestamp >= ago(30d)\n"
        "| where SHA256 == '{v}' or SHA1 == '{v}' or MD5 == '{v}'\n"
        "| project Timestamp, DeviceName, FileName, FolderPath, SHA256, InitiatingProcessFileName"
    )
}


def generate_query(qtype, value):
    """Return the formatted KQL query."""
    template = TEMPLATES.get(qtype)
    if not template:
        raise ValueError(f"Unknown query type: {qtype}")
    return template.format(v=value)


def save_output(query, output_path="results/example_query.txt"):
    """Save the generated query to the results folder."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Generated on: {datetime.utcnow().isoformat()}Z\n\n")
        f.write(query)


def main():
    parser = argparse.ArgumentParser(description="KQL Query Generator")
    parser.add_argument("--type", required=True, choices=TEMPLATES.keys())
    parser.add_argument("--value", required=True)
    args = parser.parse_args()

    query = generate_query(args.type, args.value)
    print("\n=== Generated KQL Query ===\n")
    print(query)

    save_output(query)


if __name__ == "__main__":
    main()
