from slacker import Slacker

class SlackBot:
    def __init__(self, id, api_token, channels):
        self.id_ = id
        self.API_TOKEN_ = api_token
        self.channels_ = channels
        self.slack_ = Slacker(self.API_TOKEN_)

    def send_message(self, message):
        for channel in self.channels_:
            self.slack_.chat.post_message(channel, message, as_user=True)

    def send_file(self, file):
        for channel in self.channels_:
            self.slack_.files.upload(file_=file, channels = channel)

