class MessageModel:
    def __init__(self, message, response, status):
        self.status = status
        self.message = message
        self.response = response

    def serialize(self):
        return {"status": self.status,
                "message": self.message,
                "response": self.response}
