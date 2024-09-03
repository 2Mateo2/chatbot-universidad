import json
import nltk
import random

from nltk.stem import SnowballStemmer

# Carga las instrucciones desde el JSON
with open('data/instructions.json', 'r', encoding='utf-8') as file:
    json_instructions = json.load(file)

conversacion = [] 

# Tokenizador
tokenizer = nltk.RegexpTokenizer(r'\w+')

# Stemmer para reducir palabras a su raíz
stemmer = SnowballStemmer('spanish')

# Función para calcular la similitud de palabras clave
def calculate_similarity(input_words, pattern_words):
    input_set = set(input_words)
    pattern_set = set(pattern_words)
    
    # Comprobar si pattern_set está vacío para evitar la división por cero
    if not pattern_set:
        return 0.0
    
    intersection = input_set.intersection(pattern_set)
    return len(intersection) / len(pattern_set)

# Función para obtener una respuesta del chatbot
def get_response(input_text):
    input_text = input_text.lower()
    input_words = tokenizer.tokenize(input_text)
    input_words = [stemmer.stem(word) for word in input_words]

    best_match = None
    best_similarity = 0

    for item in json_instructions['intents']:
        for pattern in item['patterns']:
            pattern_words = tokenizer.tokenize(pattern)
            pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]

            similarity = calculate_similarity(input_words, pattern_words)

            if similarity > best_similarity:
                best_match = item
                best_similarity = similarity

    if best_match:
        return random.choice(best_match['responses'])
    else:
        # Si no hay coincidencia en instrucciones más específicas, usar la instrucción "default"
        for item in json_instructions['intents']:
            if item['tag'] == 'default':
                return random.choice(item['responses'])

    return "Lo siento, no entiendo tu pregunta. ¿Puedes reformularla?"

def llenarJson(user_message):
    res = get_response(user_message)
    conversacion.append({"user": user_message, "bot": res})

def guardarJson():
    with open("data/conversacion/conversacion.json", "w") as archivo_json:
        json.dump(conversacion, archivo_json, indent=4)
    print("Conversación guardada en 'data/conversacion/conversacion.json'.")
