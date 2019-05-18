# returns navigation for API
global Data
global Path

validVerbs  = "get put delete post"
data = '{ "directories" : [ '
# ??? need to remove /navigation
next = False

# excluded_prefixes = ('__', '.')
for paths, dirs, files in os.walk(Path):
    # exclude hidden folders and special files starting with excluded_prefixes
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    dirs[:] = [d for d in dirs if not d.startswith("__")]

    filenames = [f for f in files if not f.startswith(".")]
    filenames[:] = [f for f in files if not f.startswith("__")]

    if next:
        data += ', '

    schema = '"schema" : {}'
    verbs = '"verbs" : ['
    next_verb = False
    for f in filenames:
        if None != re.search('.py', f):
            verb = f[:len(f)-3]
            if validVerbs.find(verb) >= 0:
                if next_verb:
                    verbs += ', '
                file = paths + "/" + verb
                try:
                    # ??? how to get proper indentation
                    schema = '"schema" : { '
                    with open(file + ".json", "r") as read_file:
                        schema += read_file.read()
                        # ??? needs to read line at a time rather than the whole file
                    schema += '}'
                except:
                    schema = '"schema" : {}'
                verb = verb.upper()
                verbs += '"' + verb + '"'
                next_verb = True

    verbs += '], '

    data += '{ '
    data += '    "abs" : "' + paths + '", '
    data += '    ' + verbs
    data += '    "description" : "returns server date and time", '
    data += '    ' + schema
    data += '}'

    next = True

data += '] }'
print("\n\ndata = " +data)

Data = json.loads(data)
