import logging
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies import FallbackPolicy

if __name__ == '__main__':
    logging.basicConfig(level="INFO")

    model_path = './models/dialogue'

    # this will catch predictions the model isn't very certain about
    # there is a threshold for the NLU predictions as well as the action predictions
    fallback = FallbackPolicy(fallback_action_name="utter_unclear", core_threshold=0.3, nlu_threshold=0.3)

    interpreter = RasaNLUInterpreter("./models/nlu/default/hotel_nlu")
    agent = Agent("hotel_domain.yml", policies=[MemoizationPolicy(), KerasPolicy(), fallback])

    # loading our neatly defined training dialogues
    training_data = agent.load_data('./data/stories.md')
    agent.train(training_data)
    agent.persist(model_path)
    agent = Agent.load("./models/dialogue", interpreter=interpreter)
    # agent.handle.text("hello")

    print("Your bot is ready to talk! Type your message here or send 'stop'")
    while True:
     a = input()
     if a == 'stop':
         break
     responses = agent.handle_text(a)
     for response in responses:
         print(response["text"])
