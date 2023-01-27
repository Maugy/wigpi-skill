from mycroft import MycroftSkill, intent_file_handler


class Wigpi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wigpi.intent')
    def handle_wigpi(self, message):
        self.speak_dialog('wigpi')


def create_skill():
    return Wigpi()

