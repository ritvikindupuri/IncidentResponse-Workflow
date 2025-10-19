#This is an example of the Python script the AnalyzeLogsAndSystems agent might autonomously generate to solve its task.

import pandas as pd
import io
import re

def analyze_logs(log_data_string, affected_systems):
    """
    Analyzes raw log data to find the root cause of a security incident.
    """
    
    # 1. Parse the raw log string into a DataFrame
    # The AI would determine the correct regex or delimiter
    log_io = io.StringIO(log_data_string)
    df = pd.read_csv(log_io, sep=r'\s+', engine='python', 
                     names=['timestamp', 'host', 'process', 'details'])
    
    # 2. Filter for suspicious activity
    
    # Phishing email delivered
    phishing_event = df[df['details'].str.contains("Phishing email 'invoice.docm' delivered", na=False)]
    
    # Macro executed
    macro_event = df[df['details'].str.contains("Executed macro launching cmd.exe -> powershell.exe", na=False)]
    
    # Payload downloaded
    download_event = df[df['details'].str.contains("Downloaded payload loader.bin from 203.0.113.45", na=False)]
    
    # 3. Identify attack chain and IoCs
    attack_chain = []
    indicators = []

    if not phishing_event.empty:
        attack_chain.append("Initial Access: Phishing email with 'invoice.docm' was delivered to j.smith.")
        indicators.append("invoice.docm")
        
    if not macro_event.empty:
        attack_chain.append("Execution: User enabled macros, launching 'cmd.exe' which spawned 'powershell.exe'.")
        indicators.append("powershell.exe")
        
    if not download_event.empty:
        ip = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', download_event.iloc[0]['details']).group(1)
        attack_chain.append(f"C2 Communication: PowerShell downloaded a payload from C2 server at {ip}.")
        indicators.append(ip)
        indicators.append("loader.bin")

    # 4. Determine root cause
    root_cause = "A combination of human vulnerability (social engineering) and insufficient endpoint security (macro execution allowed)."
    
    return {
        "root_cause": root_cause,
        "attack_chain": attack_chain,
        "indicators_of_compromise": list(set(indicators)) # Deduplicate
    }

# --- This is what the agent would execute ---
# (The agent would get these variables from its inputs)
# raw_logs = "..." 
# systems = ["WKS-JSMITH"]
# results = analyze_logs(raw_logs, systems)
# print(results) # The agent returns this as its output
