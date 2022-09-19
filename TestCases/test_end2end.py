import requests
import json
import jsonpath

def test_post():
    app_url = "https://reqres.in/api/users?page=2"
    f=open('C:/Users/062832865/My Workspace/PythonFramework/TestCases/Requests/test.json', 'r')
    request_json=json.loads(f.read())
    response = requests.post(app_url, request_json)
    assert response.status_code == 201
    assert response.text.__contains__('Ahmed')
    ID=jsonpath.jsonpath(response.json(),'id')
    print("\n##post Response body=>"+response.text)
    print("ID=>"+ID[0])

def test_delete():

    app_url2 = "https://reqres.in/api/users/2"
    response2 = requests.delete(app_url2)
    assert response2.status_code == 204
    print("\n##Delete ==> No Response body")

def test_get():

    app_url2 = "https://reqres.in/api/users?page=2"
    response2 = requests.get(app_url2)
    assert response2.status_code == 200
    assert response2.text.__contains__('Michael')
    print("\n##get Response body=>"+response2.text)
    ID=jsonpath.jsonpath(response2.json(),'data[0].id')
    print("ID = "+ str(ID[0]))


def test_update():
    app_url = "https://reqres.in/api/users/2"
    f=open('C:/Users/062832865/My Workspace/PythonFramework/TestCases/Requests/update.json', 'r')
    request_json=json.loads(f.read())
    response = requests.put(app_url, request_json)
    assert response.status_code == 200
    updated_at=jsonpath.jsonpath(response.json(),'updatedAt')
    updated_at=str(updated_at).replace('[','')
    updated_at=updated_at.replace(']','')
    updated_at=updated_at.replace("'",'')
    print('\n'+updated_at)
    print('{"name":"Ahmed","job":"Senior Automation Engineer","updatedAt":"'+updated_at+'"}')
    assert response.text=='{"name":"Ahmed","job":"Senior Automation Engineer","updatedAt":"'+str(updated_at)+'"}'
    assert response.text.__contains__('updatedAt')
    assert response.text.__contains__('Senior')
    print("##PUT (update) Response body=>"+response.text)