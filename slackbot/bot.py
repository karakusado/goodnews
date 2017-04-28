import os
import slackweb

slack = slackweb.Slack(url=os.environ(["VAR_SLACK_TEST_URL"])
slack.notify(text="This is a test.")
