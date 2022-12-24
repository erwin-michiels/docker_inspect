import json

with open('flask_container_inspect.json') as f:
    contents = f.read()
    contents = json.loads(contents)
    #print(contents)

    print('* Hostname:')
    print(contents[0]["Config"]["Hostname"])

    print('* IPAddress:')
    print(contents[0]["NetworkSettings"]["IPAddress"])

    print('* Ports:')
    print(contents[0]["NetworkSettings"]["Ports"])

    print('* Status:')
    print(contents[0]["State"]["Status"])