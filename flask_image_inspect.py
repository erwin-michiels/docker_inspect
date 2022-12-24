import json

with open('flask_image_inspect.json') as f:
    contents = f.read()
    contents = json.loads(contents)
    #print(contents)

    print('* RepoTags:')
    print(contents[0]["RepoTags"])

    print('* created:')
    print(contents[0]["Created"])

    print('* hostname:')
    print(contents[0]["ContainerConfig"]["Hostname"])

    print('* DockerVersion:')
    print(contents[0]["DockerVersion"])