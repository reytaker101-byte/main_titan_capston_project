def transcribed_request(text: str) -> dict:
    return {
        "channel": "voice",
        "request": text,
        "next_step": "create_incident_request"
    }

if __name__ == "__main__":
    print(transcribed_request("Investigate payment outage"))
