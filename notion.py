import requests
import datetime
from natapi import chatIA
import sys
import datetime
from pprint import pprint

#start the stopwatch
start = datetime.datetime.now()




apiKey = "secret_enqEFZQjU9BgB8VbbgFWxOD9Yx3bK8Gxmi5Lax1zX0K"

DATABASE_ID1 = "23a18b159c114a62b988120027b9a2f0"
DATABASE_ID = "774af6088f70461397297186a946a7a0"
headers = {
    "Authorization": "Bearer " + apiKey,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}
def get_pages(num_pages=100, dataBase=None):
    results = []
    has_more = True
    start_cursor = None
    next_cursor = None

    #print("DataBase : ", dataBase)
    url = f"https://api.notion.com/v1/databases/{dataBase}/query"

    payload = {"page_size": num_pages}


    while has_more:
        response = requests.post(url, json=payload, headers=headers)
        #print("STATUS CODE : ", response)
        data = response.json()
        #print(data)
        payload["start_cursor"] = data["next_cursor"]
        has_more = data["has_more"]
        results.append(data["results"])

    import json
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    return results


data_base = {}

sections = get_pages(100, DATABASE_ID1)

"""for section in sections:
    for page in section:
        name = page["properties"]["Project name"]["title"][0]["text"]["content"]
        id = page["id"]
        data_base[name] = {"id" : id, "tasks" : []}

"""

projects = []
for i in sections:
    for page in i:
        projects.append({"id":page["id"], "name":page["properties"]["Project name"]["title"][0]["text"]["content"], "Sub-tasks":[]})

projects.append({"name": "noProject", "Sub-tasks":[]})


missions_data_base = {}

#print("\n\n\n")
#print("GO TO BUILD QUESTION ?")


path = ""

def linkToProject(sourceDB, data_base, projects):
    ProjectData = {}
    for element in sourceDB:
        for d in data_base:
            if element["id"] == d["id"]:
                ProjectData[d["id"]] = element["properties"]["Project"]["relation"][0]["id"] if element["properties"]["Project"]["relation"] != [] else ""

    for d in data_base:
        for p in projects:
            if p["id"] == ProjectData[d["id"]]:
                p["Sub-tasks"].append(d)

    return projects

def linkToProject2(sourceDB, data_base):
    sections = get_pages(100, DATABASE_ID1)

    projects = []
    for i in sections:
        for page in i:
            projects.append(
                {"id": page["id"], "name": page["properties"]["Project name"]["title"][0]["text"]["content"], "Sub-tasks": []})

    projects.append({"name": "noProject", "Sub-tasks": [], "id": ""})
    #print(f"FIRST AFFECTION TO PROJECTS : {projects}")

    ProjectData = {}
    for d in data_base:
        for element in sourceDB:
            eName = element["properties"]["Task namea"]["title"][0]["text"]["content"] if element["properties"]["Task namea"]["title"] != [] else "noName"
            if d["name"] == eName:
                ProjectData[d["name"]] = element["properties"]["Project"]["relation"][0]["id"] if element["properties"]["Project"]["relation"] != [] else ""


    for d in data_base:
        noFound = True
        for p in projects:
            try:
                #print(p["id"])
                #print(p["id"], " / ", ProjectData[d["name"]])
                if p["id"] == ProjectData[d["name"]]:
                    p["Sub-tasks"].append(d)
                    noFound = False
            except:
                print("fuck you")

        if noFound:
            projects[-1]["Sub-tasks"].append(d)

    #print("\n\n\n PROJECTS /// ", projects, "\n\n\n")


    return projects


def build_hierarchy(data, parent, filters=None, parent_task=False):

    if filters is None:
        filters = {}

    global projects_id
    global path

    if filters:
        priority = filters["priority"]
        status = filters["status"]
        date = filters["date"]



    hierarchy = []

    #parent = [] if parent not in projects_id else parent

    for task in data:

            parent_task = task["properties"]["Parent-task"]["relation"][0]["id"] if task["properties"]["Parent-task"]["relation"] != [] else []

            if parent_task == parent:
                #print("PARENT ---  ", task["properties"]["Parent-task"]["relation"], "  //  ", parent)
                path += " - " + str(parent)
                #print(path)

                sub_hierarchy = build_hierarchy(data, task['id'], filters)
                if sub_hierarchy:

                    task["properties"]["Sub-tasks"]["relation"] = sub_hierarchy
                    #print("SUB ---  ", task["properties"]["Sub-tasks"]["relation"], "  //  ", sub_hierarchy)
                #hierarchy.append(task)
                #hierarchy.append({"name": task["properties"]["Task namea"]["title"][0]["text"]["content"] if task["properties"]["Task namea"]["title"] != [] else "NoName", "id": task["id"], "Sub-tasks": task["properties"]["Sub-tasks"]["relation"],"Parent-task": task["properties"]["Parent-task"]["relation"]})

                props = task["properties"]

                H = {"name": props["Task namea"]["title"][0]["text"]["content"] if task["properties"]["Task namea"]["title"] != [] else "NoNames", "sub-tasks": props["Sub-tasks"]["relation"] if props["Sub-tasks"]["relation"] != [] else []}

                if filters:
                    if priority: H["priority"] = props["Priority"]["select"]["name"].lower() if props["Priority"]["select"] != None else "None"
                    if status: H["status"] = props["Status"]["status"]["name"].lower()
                    if date: H["date"] = props["Due"]["date"]["start"] if props["Due"]["date"] != None else "None"


                hierarchy.append(H)


    return hierarchy

display = ""
def display_hierarchy(hierarchy, espace=0):
    global display
    for task in hierarchy:
        name = task["name"] if task["name"] != [] else "NoName"
        #print(espace*"    ", "-", name)
        display += espace*"    " + "-" + name + "\n"
        if task["Sub-tasks"] != []:
            display_hierarchy(task["Sub-tasks"], espace+1)

    with open('display.txt', 'w', encoding='utf8') as f:
        f.write(display)

filteredDataBase = []
def filterDatabase(dataBase, filters, parentName="None"):

    global filteredDataBase

    if filters:
        priority = filters["priority"]
        status = filters["status"]
        date = filters["date"]

    for i in dataBase:
        if i["sub-tasks"] != []:
            #input(f"\n\nGOOOO BRANChE {parentName} - {i['name']}")

            filterDatabase(i["sub-tasks"], filters, parentName=i["name"])



        #input(f"\n\nBRANChE {parentName} - {i['name']}")

        if filters:
            if priority != "none":
                if i["priority"] != priority:
                    #remove task of database
                    del i
                    continue
            if status != "none":
                if i["status"] != status:
                    del i
                    continue
            if date != "none":
                if i["date"] != date:
                    del i
                    continue


        i["parent"] = parentName
        subTasks = []
        for y in i["sub-tasks"]:
            subTasks.append(y["name"])
        i["sub-tasks"] = subTasks

        filteredDataBase.append(i)

#------------------------------------------------------------------------------------------------


def searchTask(nameTask):
    global headers
    token_v2 = "v02%3Auser_token_or_cookies%3ArCM92o3ai0CGWbHNRYJ45uNA8P59LpCvRaKVuv7NlwJJZ6lnVaS5B3nP2QrcWfLxXUaG-3ly9sUrT211CcW0Fv21KfvCpLNyudY4HkaMDUGmQdZYeXq7y7CaqzS-LGBgj83R"
    headers["Cookie"] = f"token_v2={token_v2}"
    url = "https://www.notion.so/api/v3/search"
    payload = {"type":"BlocksInSpace",
               "query":nameTask,
               "spaceId":"04258b88-4955-4b30-ae14-750e2cc9b84c",
               "limit":20,
               "filters":{"isDeletedOnly":False
                   ,"excludeTemplates":False
                   ,"navigableBlockContentOnly":True
                   ,"requireEditPermissions":False
                   ,"includePublicPagesWithoutExplicitAccess":False
                   ,"ancestors":[],
                    "createdBy":[],
                    "editedBy":[],
                    "lastEditedTime":{},
                    "createdTime":{},
                    "inTeams":[]},
               "sort":{"field":"relevance"},
               "source":"quick_find_input_change",
               "searchExperimentOverrides":{},
               "searchSessionId":"",
               "searchSessionFlowNumber":2,
               "recentPagesForBoosting": [],
               }

    response = requests.post(url, headers=headers, json=payload)
    #print(response, " //\n", response.text)


    searchResult = []
    for i in response.json()["results"]:
        searchResult.append({"pageId": i["id"], "score": i["score"]})

    #print(searchResult)


    blocks = response.json()["recordMap"]["block"]

    #sans condition
    pageId =  searchResult[0]["pageId"]
    #print(f"\n\nBLOCK  - {searchResult[0]}\n\n\n")
    #print(blocks)
    #print()
    name = blocks[pageId]["value"]["properties"]["title"][0][0]
    find = {"pageId": pageId, "name": name}

    #print(len(searchResult))
    #print(find["name"], "//", find["pageId"])

    return find


def searchSubTask(taskName, dataBase):

    for i in dataBase:
        #print("- " , i["name"].lower().strip(), " // ", taskName.lower().strip(),  "\n")

        if str(taskName.lower().strip()) in  str(i["name"].lower().strip()) :
            subTask = []
            for i in i["sub-tasks"]:
                subTask.append({"name" : i["name"], "status": i["status"], "priority": i["priority"], "date": i["date"]})
            return {"name": i["name"], "sub-tasks": subTask}
        if i["sub-tasks"] != []:
            subTask = searchSubTask(taskName, i["sub-tasks"])
            if subTask != None:
                return subTask






    """
    global headers
    payload = {
               "collectionId" :collectionId,
               "type": "BlocksInCollection",
               "query": "",
               "spaceId": "04258b88-4955-4b30-ae14-750e2cc9b84c",
               "limit": 20,
               "filters": {"isDeletedOnly": False
                   , "excludeTemplates": False
                   , "navigableBlockContentOnly": True
                   , "requireEditPermissions": False
                   , "includePublicPagesWithoutExplicitAccess": False
                   , "ancestors": ["a2f33fdcf82f417ab5e21ae5493b259e"],
                           "createdBy": [],
                           "editedBy": [],
                           "lastEditedTime": {},
                           "createdTime": {},
                           "inTeams": []},
               "sort": {"field": "relevance"},
               "source": "relation_menu",
               "searchExperimentOverrides": {},
               "searchSessionId": "",
               "searchSessionFlowNumber": 2,
               "recentPagesForBoosting": [],
               "ignoreHighlight": True

    }
    url = "https://www.notion.so/api/v3/search"
    response = requests.post(url, headers=headers, json=payload)
    """

def goDataBase(question):
    sections = get_pages(100, DATABASE_ID)
    DATA_BASE = []
    for i in sections:
        for page in i:
            DATA_BASE.append(page)

    question = question
    # print(question)

    promptTask = f"""Request : {question} ?

    Instructions : Enter very shortly and with minimum words possible the name of the task searched in request and only name task, IMPORTANT you take the name only when the name is just after or just before the word "task" strictly, no project, if there is name of the task after or before word "task" enter strictly "none" or you loose points, answer have to take one or two words maximum just the name of the task nothing else, and it's hardly prohibited to enter subatask names or invent task name or take project name !
    answer /
    task name (if there is not enter none) :"""
    taskName = chatIA(promptTask)
    taskName = taskName.lower() if taskName != "none" else False
    # print(f"THIS IS TASK {taskName}")

    task = searchTask(taskName)

    # print(f"THIS IS THE TASK WE SEARCH // {task}")

    # print("\n\n", task["name"], {"priority": "high", "status": "in progress", "date": True}, "\n\n")

    hierarchy_dataBase = build_hierarchy(DATA_BASE, [], {"priority": "high", "status": "in progress", "date": "none"})
    # print("Hiherarchy built -- GO TO FIND SUB-TASKS ?")

    subtask = searchSubTask(task["name"], hierarchy_dataBase)
    # print("\n\n", "THIS THE SUB-TASKS // ", "\n\n")
    # print(subtask)
    # print("GO TO ANSWER ?")


    stop = datetime.datetime.now()
    time = stop - start
    print("TIME : ", time)

    return subtask


#------------------------------------------------------------------------------------------------

#not used
def questionListTask(question, dataBase):

    global filteredDataBase

    today = datetime.date.today()

    promptProject = f"""Request : {question} ?

Instructions : Enter shortly the name of the name of the project searched and only project no task, if you don't find name of project enter strictly "none" or you lose points  :

- project name ?

answer / project name :"""

    project = chatIA(promptProject)
    project = project.lower() if project !=  "none" else False
    input(f"THIS IS PROJECT {project}")

    promptTask = f"""Request : {question} ?

Instructions : Enter very shortly and with minimum words possible the name of the task searched in request and only name task, IMPORTANT you take the name only when the name is just after or just before the word "task" strictly, no project, if there is name of the task after or before word "task" enter strictly "none" or you loose points, answer have to take one or two words maximum just the name of the task nothing else, and it's hardly prohibited to enter subatask names or invent task name or take project name !
answer /
task name (if there is not enter none) :"""
    task = chatIA(promptTask)
    task = task.lower() if task !=  "none" else False
    input(f"THIS IS TASK {task}")

    prompt = f"""
Date (Today) : {today}
The date NEVER word in value, only format date!
\n
Priority: High - Medium - Low
\n
Status: In Progress - Stopped - Done
\n
Request : {question}
\n
Instructions : Answer yes or no as briefly as possible if the request asks :
\n
- priority ?
\n
- status (in progress, stopped, ...) ?
\n
- date ?
\n       
answer :
\n
- priority (yes/no) :
- date (yes/no) :
- status (yes/no) : -"""

    #print(question)
    response = chatIA(prompt, "gpt-4")
    input(f"\nRESPONSE : {response}")
    answer = response.lower().split("-")

    filters = None
    filtrePriority = True if " : y" in answer[0] else False
    filtreStatus = True if ": y" in answer[1] else False
    filtreDate = True  if ": y" in answer[2] else False

    if filtrePriority or filtreStatus or filtreDate:
        prompt2 = prompt + response + """\nAnswer in a short, concise list what are the exact and precise values in one value of the requests (if no answer "none")\n-"""
        response = chatIA(prompt2, "gpt-4")
        input(f"\nRESPONSE : {response}")

        answer = response.lower().split("\n")

        priority = answer[0].split(":")[1].strip() if answer[0] != "none" else False
        date = answer[1].split(":")[1].strip() if answer[1] != "none" else False
        status = answer[2].split(":")[1].strip() if answer[2] != "none" else False

        filters = {"priority": priority, "status": status, "date": date}

        input(f"\nFILTERS : {filters}")

    hierarchy_dataBase = build_hierarchy(dataBase, [], filters)
    if project != False:
        hierarchy_dataBase = linkToProject2(dataBase, hierarchy_dataBase)
        #print(hierarchy_dataBase)
        input("IT'S OKAY...")

        filterDatabase(hierarchy_dataBase, filters)
        #print(hierarchy_dataBase)
        #print(filteredDataBase)
        result= "Result of your searching :\n "
        for i in filteredDataBase:
            result += "- " + i["name"] + "\n"
        return result




"""
NEW PROMPT

Aujourd'hui  = 2023-06-25

Priorité : Haut - Moyen - Bas

Requete : Quels sont les tâches les moins prioritaires pour demain ?.

Consigne : Liste de ce qu'on peut demander dans la requete si dans la requete on demande :

- la priorité
- le status (en cours, en arret, ...)
- la date
- l'appel de sous taches

réponse :Répondez en liste courte et bref quels sont les valeurs exactes et précises des demandes (sinon répondez "vide").
- Priorité : Bas
- Status : Vide
- Date : 2023-06-26
- Appel de sous tâches : Vide
"""


def resumer():
    pass

def modifier(mod = None):


    if mod == "title":
        pass

    elif mod == "description":
        pass

    elif mod == "tags":
        pass

    elif mod == "date":
        pass

    elif mod == "status":
        pass

    elif mod == "priority":
        pass

def ajouter(name, parent):
    pass

def creerSousTache():
    pass

def briefing():
    pass

def get_daily_task():
    tasks = []
    return tasks

def input_daily_task(data):
    pass




#------------------------------------------------------------ TEST --------------------------------------------------------------------------------------------------------------------------------

"""
question = "what are the subtasks of the task Communication in the project Marketing Online ?"

questionListTask(question, DATA_BASE)
input(555555555)





p#print(build_hierarchy(DATA_BASE,  [], {"priority": "high", "status": "in progress", "date": "none"}))
hierarchy_dataBase = build_hierarchy(DATA_BASE, [], {"priority": "high", "status": "in progress", "date": "none"})

#print("\n\n\n\n\n9999999")
input("CCCONtinue filtered database ?")
#print(filterDatabase(hierarchy_dataBase, {"priority": "high", "status": "in progress", "date": "none"}))
#print("FIlTERED DATABASE", len(filteredDataBase))
#print(filteredDataBase)

input("CONTINUE HIERARCHY FILTERED")
#print(organize_tasks(filteredDataBase))
input("CONTINUE")
oData = build_hierarchy(DATA_BASE, [])
Fdata = linkToProject(DATA_BASE, oData, projects)

with open('HData.json', 'w', encoding='utf8') as f:
    json.dump(Fdata, f, ensure_ascii=False, indent=4)

#print(len(oData))
input("TAILLE --> Display Hierarchy")
display_hierarchy(oData)


#print(oData)





import json

with open('cleanDB.json', 'w', encoding='utf8') as f:
    json.dump(data_base, f, ensure_ascii=False, indent=4)




results = []




#pages = get_pages(100, DATABASE_ID)
"""
#print("Pages : ", pages)
#print("SIZE : ", len(pages))"""
#for i in results:

"""
for page in pages:
    page_id = page["id"]
    props = page["properties"]
    name = props["Name"]["title"][0]["text"]["content"]
    liste = props["Tags"]["multi_select"]
    if liste:
        tags = liste[0]["name"]
    else:
        tags = "None"
        
        
        
        
        
    #print("ID : ", page_id, "\n\n", name, "\n\n", tags)
"""
##print("\n\nPROPS  : ", props)




#print(get_pages)








"""
Condition : 
- pas de tache trouve = liste des sous taches de la tache parente
- pas de tache parente mentionée ou pas de date selctionnée = taches d'aujourd'hui 

Exemple de requete pour la fonction question :

- Can you tell me what are the sub tasks of marketing in Business Saas ?
- Can you make me a briefing of the task 1200€ ?

Type de requete :

Briefing

Organisation :
Sous Taches
Tache Parente
Quels sont les taches principales


Propriété de tache :
Les taches pour aujourd'hui
Les taches les plus prioritaire
Les taches pour demain
Les taches complétées pour aujourd'hui
Les taches complétées
Les taches en cours
Les taches pas commencés

"""












