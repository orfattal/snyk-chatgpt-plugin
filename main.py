import json
import os
import quart
import quart_cors
from quart import request
import requests
 
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")
SNYK_API_KEY = os.environ.get('SNYK_API_KEY')

if SNYK_API_KEY:
  pass
else:
  print ("SNYK_API_KEY is not defined. Please run `export SNYK_API_KEY=<API_KEY>` to set it.")
  exit()

@app.get("/groups")
async def get_groups():
    url = f'https://api.snyk.io/rest/groups?version=2023-04-28%7Ebeta'
    headers = {"Authorization": "token ".join(SNYK_API_KEY), "Accept": "application/vnd.api+json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/groups/<string:group_id>")
async def get_group(group_id):
    url = f'https://api.snyk.io/rest/groups/{group_id}?version=2023-04-28%7Ebeta'
    headers = {"Authorization": "token " + SNYK_API_KEY, "Accept": "application/vnd.api+json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)




@app.get("/orgs/<string:org_id>")
async def get_org(org_id):
    url = f'https://api.snyk.io/rest/orgs/{org_id}?version=2023-04-28%7Ebeta'
    headers = {"Authorization": "token " + SNYK_API_KEY, "Accept": "application/vnd.api+json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/orgs/<string:org_id>/projects/<string:project_id>")
async def get_project(org_id, project_id):
    url = f'https://api.snyk.io/rest/orgs/{org_id}/projects/{project_id}?version=2023-04-28%7Ebeta'
    headers = {"Authorization": "token " + SNYK_API_KEY, "Accept": "application/vnd.api+json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/orgs/<string:org_id>/targets")
async def get_targets(org_id):
    url = f'https://api.snyk.io/rest/orgs/{org_id}/targets?version=2023-04-28%7Ebeta'
    headers = {"Authorization": "token " + SNYK_API_KEY, "Accept": "application/vnd.api+json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)




@app.get("/orgs/<string:org_id>/targets/<string:target_id>")
async def get_target(org_id, target_id):
    url = f'https://api.snyk.io/rest/orgs/{org_id}/targets/{target_id}?version=2023-04-28%7Ebeta'
    headers = {"Authorization": "token " + SNYK_API_KEY, "Accept": "application/vnd.api+json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)





@app.get("/orgs/<string:org_id>/users/<string:user_id>")
async def get_user(org_id, user_id):
    url = f'https://api.snyk.io/rest/orgs/{org_id}/users/{user_id}?version=2023-04-28%7Ebeta'
    headers = {"Authorization": "token " + SNYK_API_KEY, "Accept": "application/vnd.api+json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/orgs/<string:org_id>/projects")
async def get_projects(org_id):
    url = f'https://api.snyk.io/rest/orgs/{org_id}/projects?version=2023-04-28%7Ebeta'
    headers = {"Authorization": "token " + SNYK_API_KEY, "Accept": "application/vnd.api+json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/snyk-logo.png")
async def plugin_logo():
    filename = 'snyk-logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
