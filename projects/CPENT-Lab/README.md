# Windows Post-Exploitation Lab (CPENT-Style)

This project demonstrates a full post-exploitation workflow in a controlled Windows lab environment, inspired by CPENT-style methodology.  
The goal is to simulate a realistic internal compromise, escalate privileges, pivot across a network, and extract meaningful artefacts.

---

## 🎯 Objectives

- Gain initial access to an internal Windows host.
- Perform enumeration, credential harvesting, and persistence.
- Escalate privileges (token impersonation, service misconfigurations, UAC bypass).
- Establish a secure tunnel (Ligolo-ng) for pivoting.
- Access a second network containing a Domain Controller.
- Document each phase with screenshots, logs, and scripts.
- Produce a professional post-exploitation report.

---

## 🧪 Lab Setup

### Machines
| Role | OS | Description |
|------|----|-------------|
| Attacker | Kali Linux | Runs tools like mimikatz, ligolo-ng, winPEAS, metasploit |
| Victim 1 | Windows 10 | Internal workstation vulnerable to common techniques |
| Victim 2 | Domain Controller | Target discovered after pivoting |

### Network layout (example)
