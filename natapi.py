import cloudscraper
import time


cookies = {
    "__session": "eyJhbGciOiJSUzI1NiIsImtpZCI6Imluc18yTWtjQlhndjhpbEwxcGNDTnB3MXV5anF0azgiLCJ0eXAiOiJKV1QifQ.eyJhenAiOiJodHRwczovL25hdC5kZXYiLCJleHAiOjE2ODgwNzYxOTgsImlhdCI6MTY4ODA3NjEzOCwiaXNzIjoiaHR0cHM6Ly9jbGVyay5uYXQuZGV2IiwianRpIjoiZmFhOGEzM2NlNzJhZTg4NTlmMDciLCJuYmYiOjE2ODgwNzYxMjgsInNpZCI6InNlc3NfMlJ0UDlMQmhaTW5rNlRjSEV2Zng1Vk5NOGE5Iiwic3ViIjoidXNlcl8yTzA2SUVKVWM5cHBoQ29Qc1JWcGphWVNUSUgiLCJ1c2VyX2VtYWlsIjoiY2hldmFsaXVzMTBAZ21haWwuY29tIiwidXNlcl9maXJzdF9uYW1lIjoiRmxhbU5vaXJlIiwidXNlcl9pZCI6InVzZXJfMk8wNklFSlVjOXBwaENvUHNSVnBqYVlTVElIIiwidXNlcl9sYXN0X25hbWUiOm51bGx9.foBWMwzXW9J4UWxbnGA_TzvjemyUfRYXwHCBXx73uAazFFio4-dCxZjDzG65AJseEmC1pN6Oz3tvJnWidIP0LkCfBps1ZPvxaLHeda-3-FLkejZLHORhKH9FPYVCcwj7PcpKixl_GKtqTJMSY9Wj8bUnTAB9drgT_9yEQfDG-kz9cppRVjiXV5fneFmrYUO5etehXqsDa9oV3pTBjLQZ7-0v_9Eznc6WJddpK5qaBRnDWsT-lLsDMe0N9wz6a7pGvCe8lK9gSPovwGPDD0_yzDulh075NxmqIcykM9nOdp2ZrD3wfw-n2RpC82Nk1csrQfTU0YjR4D7lUkFOeffGig",
    "client_uat": "1688066251"}


def event_stream(response):
    for line in response.iter_lines():
        if line:  # filter out keep-alive new lines
            yield line








def connexion():


    session = cloudscraper.session()



    # EXEMPLE

    headers = {
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Origin": "https://nat.dev",
        "Access-Control-Expose-Headers": "Authorization, X-Country",
        "Alt-Svc": "h3=\":443\"; ma=86400",
        "Cache-Control": "private",
        "Cf-Cache-Status": "DYNAMIC",
        "Cf-Ray": "7debd1e6887a2a41-CDG",
        "Content-Type": "application/json",
        "Server": "cloudflare",
        "Set-Cookie": "__cf_bm=kLjfA6Vpp1iB8yz3gG9fT7UzEu5nBkg0UAu_tFKWXxE-1688017071-0-AVlJv33bkxXxVvWgjXwLzjbg3vVBJI+doMFPrL6VJwtHQ32h6l7Y5MNjpMnbSD/dNjckXsoD5cJFxDr5CzKWIcg=; path=/; expires=Thu, 29-Jun-23 06:07:51 GMT; domain=.clerk.nat.dev; HttpOnly; Secure; SameSite=None",
        "Set-Cookie": "__client_uat=0; Path=/; Domain=nat.dev; Max-Age=315360000; Secure; SameSite=Lax",
        "Set-Cookie": "_cfuvid=TCioxzBHYH4fvuiZtKjqOnYOQg5qv6iEYwLGTW0.Rig-1688017071287-0-604800000; path=/; domain=.clerk.nat.dev; HttpOnly; Secure; SameSite=None",
        "Vary": "Origin, Accept-Encoding",
        "X-Cfworker": "1",
        "X-Cloud-Trace-Context": "033087795704a0f5fe250424e8288394",
        "X-Country": "FR",
        "Authority": "clerk.nat.dev",
        "Method": "GET",
        "Path": "/v1/client?_clerk_js_version=4.50.1",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr",
        "Origin": "https://nat.dev",
        "Referer": "https://nat.dev/",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58"
    }

    a = session.get("https://clerk.nat.dev/v1/client?_clerk_js_version=4.50.1",headers=headers)
    print(a)

    b = session.get("https://clerk.nat.dev/v1/environment?_clerk_js_version=4.50.1",headers=headers)
    print(b)
    #print(b.text)

    headers = {
        "Authority": "clerk.nat.dev",
        "Method": "POST",
        "Path": "/v1/client/sign_ins?_clerk_js_version=4.50.1",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "Content-Length": "34",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://accounts.nat.dev",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    data = {"identifier": "chevalius10@gmail.com"}
    data = "identifier=chevalius10%40gmail.com"




    login = session.post("https://clerk.nat.dev/v1/client/sign_ins?_clerk_js_version=4.50.1",headers=headers,data=data)

    sia = str(login.content).split('id":"')[1].split('"')[0]
    email_id = str(login.content).split('id":"client_')[1].split('"')[0]
    print("The connexion was successful")
    print(login.content)
    email_id = '2O06EwdRqmQPc04dyKflAJE74AO'

    def cookies_to_header(cookies_dict):
        cookies = []
        for key, value in cookies_dict.items():
            cookies.append(f"{key}={value}")
        return "; ".join(cookies)

    cookies = cookies_to_header(session.cookies.get_dict())

    headers = {
        "Authority": "clerk.nat.dev",
        "Method": "POST",
        "Path": f"v1/client/sign_ins/{sia}/prepare_first_factor?_clerk_js_version=4.50.1",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookies,
        "Origin": "https://accounts.nat.dev",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    data = {"email_address_id": f"idn_{email_id}",  "strategy": "email_code" }
    #data = "email_address_id=idn_2O06EwdRqmQPc04dyKflAJE74AO&strategy=email_code"

    prepare_code = session.post(f"https://clerk.nat.dev/v1/client/sign_ins/{sia}/prepare_first_factor?_clerk_js_version=4.50.1", data=data, headers=headers)

    code = input("Entrez le code reèu par email : ")

    data = f"strategy=email_code&code={code}"
    data =  {"strategy": "email_code", "code": code}

    send_code = session.post(f"https://clerk.nat.dev/v1/client/sign_ins/{sia}/attempt_first_factor?_clerk_js_version=4.50.1", data=data, headers=headers)
    session_id = send_code.json()["response"]["created_session_id"]

    data = {"active_organization_id": ""}
    touch = session.post(f"https://clerk.nat.dev/v1/client/sessions/{session_id}/touch?_clerk_js_version=4.50.1", data=data)
    print(touch.content, touch, "\n\n\n\n")

    cookies = cookies_to_header(session.cookies.get_dict())


    headers = {
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Origin": "https://nat.dev",
        "Access-Control-Expose-Headers": "Authorization, X-Country",
        "Alt-Svc": "h3=\":443\"; ma=86400",
        "Cache-Control": "private",
        "Cf-Cache-Status": "DYNAMIC",
        "Cf-Ray": "7debd1e6887a2a41-CDG",
        "Content-Type": "application/json",
        "Server": "cloudflare",
        "Vary": "Origin, Accept-Encoding",
        "X-Cfworker": "1",
        "X-Cloud-Trace-Context": "033087795704a0f5fe250424e8288394",
        "X-Country": "FR",
        "Authority": "clerk.nat.dev",
        "Method": "GET",
        "Path": "/v1/client?_clerk_js_version=4.50.1",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr",
        "Origin": "https://nat.dev",
        "Referer": "https://nat.dev/",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58"
    }

    a = session.get("https://clerk.nat.dev/v1/client?_clerk_js_version=4.50.1", headers=headers)
    print(a, a.text)

    token = a.json()["response"]["sessions"][0]["last_active_token"]["jwt"]
    print("\n\n token : ", token)


    b = session.get("https://clerk.nat.dev/v1/environment?_clerk_js_version=4.50.1", headers=headers)
    print("\n\n",b, b.text)

    time.sleep(1)

    headers = {
        "Authority": "nat.dev",
        "Method": "GET",
        "Path": "/api/user/check-balance",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Type": "text/plain;charset=UTF-8",
        "Origin": "https://nat.dev",
        "Referer": "https://nat.dev/",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }


    cookies = {"__session" : token, "client_uat": session.cookies.get_dict()["__client_uat"]}



    print("\n\n cookie : ", session.cookies.get_dict())


    headers = {
        "Authority": "nat.dev",
        "Method": "POST",
        "Path": "/api/inference/text",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Type": "text/plain;charset=UTF-8",
        "Origin": "https://nat.dev",
        "Referer": "https://nat.dev/",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    model = {"prompt": "test",
             "models": [
                 {"name":"openai:gpt-4",
                  "tag":"openai:gpt-4",
                  "capabilities":["chat"],
                  "provider":"openai",
                  "parameters":
                      {"temperature":0.62,
                       "contextLength":5844,
                       "maximumLength":2347,
                       "topP":1,
                       "presencePenalty":0,
                       "frequencyPenalty":0,
                       "stopSequences":[],
                       "numberOfSamples":1},
                  "enabled":True,
                  "selected":True}],
             "stream":True}


    test = session.post("https://nat.dev/api/inference/text", json=model, cookies=cookies, headers=headers, stream=True)

    for event in event_stream(test):
        print(event)


    return test

#session = connexion()

"""headers = {
    "Authority": "nat.dev",
    "Method": "GET",
    "Path": "/api/user/check-balance",
    "Scheme": "https",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "text/plain;charset=UTF-8",
    "Origin": "https://nat.dev",
    "Referer": "https://nat.dev/",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

cookies = {
    "__session": "eyJhbGciOiJSUzI1NiIsImtpZCI6Imluc18yTWtjQlhndjhpbEwxcGNDTnB3MXV5anF0azgiLCJ0eXAiOiJKV1QifQ.eyJhenAiOiJodHRwczovL25hdC5kZXYiLCJleHAiOjE2ODgwNzYxOTgsImlhdCI6MTY4ODA3NjEzOCwiaXNzIjoiaHR0cHM6Ly9jbGVyay5uYXQuZGV2IiwianRpIjoiZmFhOGEzM2NlNzJhZTg4NTlmMDciLCJuYmYiOjE2ODgwNzYxMjgsInNpZCI6InNlc3NfMlJ0UDlMQmhaTW5rNlRjSEV2Zng1Vk5NOGE5Iiwic3ViIjoidXNlcl8yTzA2SUVKVWM5cHBoQ29Qc1JWcGphWVNUSUgiLCJ1c2VyX2VtYWlsIjoiY2hldmFsaXVzMTBAZ21haWwuY29tIiwidXNlcl9maXJzdF9uYW1lIjoiRmxhbU5vaXJlIiwidXNlcl9pZCI6InVzZXJfMk8wNklFSlVjOXBwaENvUHNSVnBqYVlTVElIIiwidXNlcl9sYXN0X25hbWUiOm51bGx9.foBWMwzXW9J4UWxbnGA_TzvjemyUfRYXwHCBXx73uAazFFio4-dCxZjDzG65AJseEmC1pN6Oz3tvJnWidIP0LkCfBps1ZPvxaLHeda-3-FLkejZLHORhKH9FPYVCcwj7PcpKixl_GKtqTJMSY9Wj8bUnTAB9drgT_9yEQfDG-kz9cppRVjiXV5fneFmrYUO5etehXqsDa9oV3pTBjLQZ7-0v_9Eznc6WJddpK5qaBRnDWsT-lLsDMe0N9wz6a7pGvCe8lK9gSPovwGPDD0_yzDulh075NxmqIcykM9nOdp2ZrD3wfw-n2RpC82Nk1csrQfTU0YjR4D7lUkFOeffGig",
    "client_uat": "1688066251"}

Z = session.get("https://nat.dev/api/user/check-balance", headers=headers, cookies=cookies)
print(Z.content, Z, Z.headers)"""

#print("\n\n\n result : ", "AAA",session.text, session)


session = cloudscraper.session()

headers = {
        "Authority": "nat.dev",
        "Method": "POST",
        "Path": "/api/inference/text",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Type": "text/plain;charset=UTF-8",
        "Origin": "https://nat.dev",
        "Referer": "https://nat.dev/",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }
def chatIA(prompt):
    model = {"prompt": prompt,
                 "models": [
                     {"name":"openai:gpt-4",
                      "tag":"openai:gpt-4",
                      "capabilities":["chat"],
                      "provider":"openai",
                      "parameters":
                          {"temperature":0.68,
                           "contextLength":5844,
                           "maximumLength":2347,
                           "topP":1,
                           "presencePenalty":0,
                           "frequencyPenalty":0,
                           "stopSequences":[],
                           "numberOfSamples":1},
                      "enabled":True,
                      "selected":True}],
                 "stream":True}


    test = session.post("https://nat.dev/api/inference/text", json=model, cookies=cookies, headers=headers, stream=True)

    message = ""
    for event in event_stream(test):
        if 'token' in str(event):
            token = (str(event).split('"token": "')[1].split('"')[0])
            if token != "[INITIALIZING]" and token != "[COMPLETED]":
                decoded_text = eval(f"'{token}'")
                decoded_texts = bytes(decoded_text, 'utf-8').decode('unicode_escape')
                token = decoded_texts
                message = message + token

    return message

