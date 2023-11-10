import requests
import datetime
apiKey = "secret_enqEFZQjU9BgB8VbbgFWxOD9Yx3bK8Gxmi5Lax1zX0K"

DATABASE_ID = "774af6088f70461397297186a946a7a0"
DATABASE_ID = "8fc984f62f424567a4b9e31bb9061d9b"

headers = {
    "Authorization": "Bearer " + apiKey,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def get_pages(num_pages=None):
    """
    If num_pages is None, get all pages, otherwise just the defined number.
    """
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    print("DATA : ", data)
    input()

    # Comment this out to dump all data to a file
    # import json
    # with open('db.json', 'w', encoding='utf8') as f:
    #    json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])

    return results

pages = get_pages()

for page in pages:
    input(page)
    page_id = page["id"]
    props = page["properties"]
    url = props["URL"]["title"][0]["text"]["content"]
    title = props["Title"]["rich_text"][0]["text"]["content"]
    published = props["Published"]["date"]["start"]
    published = datetime.fromisoformat(published)

def get_daily_task():
    tasks = []
    return tasks

def input_daily_task(data):
    pass

print(get_pages)














