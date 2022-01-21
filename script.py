import re
from os import listdir
from os.path import isfile, join

inputDir = "notes"
imageDir = "/tmp/output"
regex = """@enduml\s+\`\`\`"""


def processFile(file):
    print("Processing: " + file)
    with open(inputDir+ "/" + file, "r") as f:
        content = f.read()
    pos = 0
    matches = []
    # Find all matches and store them in a list
    while True:
        match = re.search(regex, content)
        if match is None:
            break
        matches.append(match)
        pos = match.end() +1
        content = content[pos:]
    print(matches)


    images =  [f for f in listdir(imageDir) if isfile(join(imageDir, f))]

    print(images)
    


if __name__ == "__main__":
    onlyfiles = [f for f in listdir(inputDir) if isfile(join(inputDir, f))]

    for file in onlyfiles:
        processFile(file)


