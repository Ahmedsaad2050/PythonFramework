import requests
import json
import jsonpath

def test_end2end():
    app_url = "https://reqres.in/api/users?page=2"
    f=open('C:/Users/062832865/My Workspace/PythonFramework/TestCases/Requests/test.json', 'r')
    request_json=json.loads(f.read())
    response = requests.post(app_url, request_json)
    assert response.status_code == 202
    assert response.text=='Ahmed'
    assert response.text.__contains__('Ahmed')
    ID=jsonpath.jsonpath(response.json(),'id')
    print("\n ID=>"+ID[0])
    print(" Response body=>"+response.text)
    