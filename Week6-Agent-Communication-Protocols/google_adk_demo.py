class AgentAdapter:
    """Framework-neutral boundary for future Google ADK integration."""
    def invoke(self, task: dict) -> dict:
        return {"accepted": True, "task": task}

if __name__ == "__main__":
    print(AgentAdapter().invoke({"task": "investigate"}))
