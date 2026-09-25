class IncidentConversation:
    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append({"role": role, "message": message})

    def context(self):
        return self.history

if __name__ == "__main__":
    chat = IncidentConversation()
    chat.add("user", "Investigate payment-service")
    chat.add("assistant", "I will inspect the current deployment and pod evidence.")
    print(chat.context())
