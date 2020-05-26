from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

training_data = load_data("./data/data.md")
trainer = Trainer(config.load("config_embedding.json"))
trainer.train(training_data)
model_directory = trainer.persist("./models/nlu/",fixed_model_name="hotel_nlu")
interpreter = Interpreter.load(model_directory)

print(interpreter.parse("halo"))
print(interpreter.parse("bisa minta pasta gigi lagi?"))
print(interpreter.parse("ac nya kurang dingin"))
print(interpreter.parse("kok sabunnya gaada ya?"))