CHANNELS = {
    "SEV-1": ["pagerduty", "slack", "email", "ticket"],
    "SEV-2": ["slack", "email", "ticket"],
    "SEV-3": ["slack", "ticket"],
    "SEV-4": ["ticket"],
}

def route(severity):
    return CHANNELS.get(severity, ["ticket"])
