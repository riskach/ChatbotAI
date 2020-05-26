import logging
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, ConversationPaused


logger = logging.getLogger(__name__)

class ActionExtra(Action):
    def name(self):
        return 'action_extra'

    def run(self, dispatcher, tracker, domain):
        city = current ['room']['name']
        response = """baik, telah diproses extra untuk kamar {}. ditunggu untuk extra yang diminta""".format(room)

        dispatcher.utter_message(response)
        return [SlotSet('room', room)]