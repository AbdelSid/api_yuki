# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from natapi import chatIA
import json
import os
from mangum import Mangum
import random
import voice
import websockets

class Item(BaseModel):
    text: str


"""
def Emploie_Du_Temp(entree):
    if "ajoute" in entree:

        global mois, jour, heure, minute, heure2, minute2, name

        #assistant_voix("")
        name = entree.split("add in my planning")[1]
        assistant_voix(f"Quand voulez vous ajouter {name} à votre emploi du temps")
        moiss = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "décembre"]
        while True:

                if (entree := reconnaissance()) is not None:
                    if "le" in entree:
                        entree = entree.split("le ")[1]
                        entree = ("").join(entree)
                        print(entree)
                    if "à" in entree:
                        entree = entree.split(" à ")
                        entree = (" ").join(entree)
                        print(entree)
                    if "demain" in entree:
                        jour = EDT.jour + 1

                    #Jour et Mois
                    for i in moiss:
                        if i in entree:
                            mois = entree.split(" ")
                            jour = int(mois[0])
                            mois = mois[1]

                        if mois == "janvier":
                            mois = 1
                        elif mois == "février":
                            mois = 2
                        elif mois == "mars":
                            mois = 3
                        elif mois == "avril":
                            mois = 4
                        elif mois == "mai":
                            mois = 5
                        elif mois == "juin":
                            mois = 6
                        elif mois == "juillet":
                            mois = 7
                        elif mois == "août":
                            mois = 8
                        elif mois == "septembre":
                            mois = 9
                        elif mois == "novembre":
                            mois = 11
                        elif mois == "octobre":
                            mois = 10
                        elif mois == "novembre":
                            mois = 11
                        elif mois == "décembre":
                            mois = 12

                    if "h" in entree:
                        heure = entree.split(" ")
                        for i in heure:
                            if "h" in i:
                                heure = int(i.split("h")[0])

                    if entree.split("h")[1] != "":
                        minute = int(entree.split("h")[1])

                    else:
                        minute = 0

                    assistant_voix("Et jusqu'à quand ?")

                    if (entree := reconnaissance()) is not None:

                        # Les heures d'arrivées
                        if "h" in entree:
                            heure2 = entree.split(" ")
                            heure2 = [i for i in heure2 if "h" in i]
                            heure2 = int(("").join(heure2).split("h")[0])

                        # Les minutes d'arrivées
                        if entree.split("h")[1] != "":
                            minute2 = int(entree.split("h")[1])

                        else:
                            minute2 = 0

                        _terminer_ajout_emploie_du_temp()
                        break
"""

bye = ["See you soon, Abdel", "Good Bye", "Okay call me when ever you want", "Okay, good courage for the next", "It was nice to talk with you", "Bye, Abdel"]

def new_conv():
    conv = "conversation-"

    for i in range(0, 9999999999):
        if not os.path.exists(conv + str(i)):
            with open("conversations.json", "r") as f:
                conversations = json.load(f)
                conversations[conv + str(i)] = "You are Alicia, a human who is the best friend and the assistant of Abdel, you are starting a real conversation with him.\nAbdel :"
            with open("conversations.json", "w") as f:
                json.dump(conversations, f)
            break

def change_conv(response):
    with open("conversations.json", "r") as f:
        conversations = json.load(f)

    list_name = ""
    for i in conversations.keys():
        list_name += (str(i)+ "\n")

    name = chatIA(list_name + "\n" + response + "\n" + "find the name the most closer in the list name, in one word the name asked. name :")
    backUpConv = conversations[name]
    del conversations[name]
    conversations[name] = backUpConv

    return "now the conversation is " + name

def rename_conv(response):
        rename = chatIA("phrase where you have to find the name of conversations --> "+ response +"\nSay just the name of the conversation, no else words:")
        print("RENAMING  ", rename)
        with open("conversations.json", "r") as f:
            conversations = json.load(f)

        for i in conversations.keys():
            current_conv_key = i
        current_conv = conversations[current_conv_key]
        del conversations[current_conv_key]
        for i in conversations.keys():
            print(i)
        conversations[rename] = current_conv

        with open("conversations.json", "w") as r:
            json.dump(conversations, r)

        return rename

# Initialize the app
app = FastAPI()
handler = Mangum(app)
# Define a route
@app.get("/")
async def read_root():
    return "Salut, on dirait que j'arrive bientôt ;)"

# Define another route with a parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):

    with open("state.json") as f:
        etat = json.load(f)
    print(item.text)

    #if etat == "rename":

    response = item.text.lower()

    #start new conversation
    if ( ("conv" in response) and ("new" in response) ) or ("hey alicia" in response):
        new_conv()
        return "New conversation created succesfully"

    #rename conversation
    if "rename" in response and "conv" in response:
        rename = rename_conv(response)
        return "The response was renammed succesfully " + rename

    #switch conversation
    if ("change" in response or "go" in response or "let's talk" in response) and ("conv" in response):

        name = change_conv(response)

        return {"text":"The conversation is now " + name}

    #stop conversation
    if ("stop" in response or "break" in response or "good bye" in response or "bye" in response) and len(response) < 12:
        return random.choice(bye)

    with open("conversations.json", "r") as f:
        CONVERSATIONS = json.load(f)
        conversation = CONVERSATIONS.values()[-1]

    conversation += " " + response + "\nAlicia :"

    responseAI = chatIA(conversation)

    conversation += " " + responseAI + "\nAbdel :"

    CONVERSATIONS[-1] = conversation


    with open("conversations.json",  "w") as r:
        json.dump(CONVERSATIONS, r)

    return responseAI

@app.post("/items1/")
def create_item(item):


    response = chatIA(item)


    return response

@app.get("/test-audio")
def test_audio():
    audio = voice.audioTest()
    return audio


"""
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
"""

