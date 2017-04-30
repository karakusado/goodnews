import slackweb

class SlackBot:
    def __init__(self, channelURL):
        self.__channelURL = channelURL
        self.slack = slackweb.Slack(self.__channelURL)

    def post(self, text):
        self.slack.notify(text=text)
