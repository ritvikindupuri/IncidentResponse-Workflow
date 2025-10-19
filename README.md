# Autonomous SOC Analyst: An AI-Driven Incident Response Pipeline

This project is a complete, automated system that models the entire workflow of a Security Operations Center (SOC) analyst responding to an incident. It was built and orchestrated entirely in **Google's Opal** using natural language instructions.

The platform functions as a "lead AI architect" that manages a team of specialized AI agents. It takes an initial incident description and raw log files as input and autonomously produces a multi-section, professional HTML report as the final output.

---
## The AI Agent Orchestration

The core of the system is a multi-agent workflow where specialist AIs collaborate to solve a complex security problem. Each agent has a distinct role, and their findings are passed to other agents for synthesis and further analysis. This modular design allows the system to deconstruct an incident, analyze it from multiple perspectives (technical, business, strategic), and then reassemble the findings into a single, comprehensive report.

<img src="./assets/Automation Architecture.png" width="800" alt="The high-level architecture of the multi-agent SOC pipeline">
*<p align="center">Figure 1: The full agent orchestration workflow as designed in Google Opal.</p>*

---
## Key Capability: Autonomous Log Analysis via Code Execution

The primary technical agent in this pipeline is **`AnalyzeLogsAndSystems`**. This is not just a large language model; it is an autonomous agent with privileged capabilities.

Using natural language, I instructed this agent to act as an "expert Python programmer" and granted it **Code Execution** permissions. When the agent is given raw, unstructured logs, it autonomously **writes and executes its own Python scripts (using Pandas)** to parse, filter, correlate, and analyze the data. This allows it to identify the attack chain, extract Indicators of Compromise (IoCs), and determine the root cause without human intervention.

<img src="./assets/Python autonomous agent.png" width="800" alt="The configuration of the autonomous Python agent with Code Execution capabilities">
*<p align="center">Figure 2: The `AnalyzeLogsAndSystems` agent, empowered to write and execute its own Python scripts for log analysis.</p>*

---
## Final Output: AI-Generated Root Cause Analysis

The system's final product is a professional-grade HTML incident report. The screenshot below shows a portion of the final output from the **`FormatComprehensiveReport`** agent.

After the `AnalyzeLogsAndSystems` agent identified the technical root cause (a macro in `invoice.docm` spawning `powershell.exe`), the other agents gathered threat intelligence on the IoCs, assessed the business impact, and formulated a remediation plan. This final agent synthesized all those findings into a polished, human-readable report that correctly identifies a multi-stage compromise and provides clear, actionable evidence.

<img src="./assets/Root Cause Analysis Output.png" width="800" alt="A screenshot of the final HTML report showing a detailed Root Cause Analysis">
*<p align="center">Figure 3: The final, synthesized Root Cause Analysis, demonstrating the system's ability to reason and report.</p>*

---
## Skills & Technologies Demonstrated

* **AI Agent Orchestration:** Designing and managing multi-agent workflows in **Google Opal**.
* **Autonomous Code Generation:** Prompting and "harnessing" an AI agent with `Code Execution` capabilities.
* **Incident Response (IR):** Automating the full IR lifecycle, from log analysis to reporting.
* **Log Analysis:** Using **Python (Pandas)** in an automated context to parse and analyze security logs.
* **Prompt Engineering:** Crafting precise, role-based instructions for specialist AI agents.
* **Cloud-Native Security:** Leveraging next-generation AI platforms (Gemini 2.5) for security automation.
