#!/usr/bin/python

meta = {}

with open('input.txt', 'r') as file:
    for line in file:
        words = line.split()

        name = words[0]
        weight = int(words[1][1:-1])
        # print words[1][1:-1]

        substructure = {}
        if len(words) > 2:
            for supported in words[3:]:
                substructure[supported.replace(',','')] = {}

        program = {
            "name": name,
            "weight": weight,
            "substructure": substructure,
            "on_top_of": None
        }

        meta[name] = program

# print meta
def buildTowerStructure(meta):
    tower = {
        "meta": meta,
        "foundations": meta.keys(),
        "tips": meta.keys()
    }
    for program_name in meta:
        addProgramToTower(program_name, tower)
        if meta[program_name]["weight"] == 1225:
            print meta[program_name]

    print "root: {0}".format(tower["foundations"])
    tower["foundations"] = tower["foundations"][0]

    return tower

def addProgramToTower(name, tower):
    program = tower["meta"][name]
    if len(program["substructure"].keys()) > 0:
        tower["tips"].remove(name)
        for supported_name in program["substructure"]:
            program["substructure"][supported_name] = tower["meta"][supported_name]["substructure"]
            tower["meta"][supported_name]["on_top_of"] = program["name"]
            tower["foundations"].remove(supported_name)

def inTheForceAnUnbalanceIsSearched(tower):
    root_program = tower["meta"][tower["foundations"]]
    total_weight = root_program["weight"]
    weight_on_top = []
    weight_mappings = {}

    if (len(root_program["substructure"].keys()) == 0):
        # print 'wtf'
        return (True, root_program["weight"])

    for supported_program in root_program["substructure"]:
        subtower = {
            "meta": tower["meta"],
            "foundations": supported_program
        }
        is_subtower_balanced, weight = inTheForceAnUnbalanceIsSearched(subtower)
        if is_subtower_balanced:
            total_weight += weight
            weight_on_top += [weight]
            weight_mappings[weight] = supported_program
        else:
            return (is_subtower_balanced, weight)

    if min(weight_on_top) == max(weight_on_top):
        return (True, total_weight)

    distinct_subtower_weight, diff = getDistinctElement(weight_on_top)
    # print weight_on_top
    # print distinct_subtower_weight
    # print diff
    unbalance_perpetrator = weight_mappings[distinct_subtower_weight]
    unbalance_perpetrator_weight = tower["meta"][unbalance_perpetrator]["weight"]
    # print tower["meta"][unbalance_perpetrator]
    # print unbalance_perpetrator_weight - diff

    return (False, unbalance_perpetrator_weight + diff)

def getDistinctElement(l):
    if len(l) <= 1:
        return (None, 0)
    common = None
    for i in range(len(l)):
        if i == len(l) -1:
            return (None, 0)
        if l[i] == l[i+1]:
            common = l[i]
            continue
        elif i == 0 and len(l) > 2:
            if l[i] == l[i+2]:
                return (l[i+1], l[i] - l[i+1])
            else:
                return (l[i], l[i+1] - l[i])
        else:
            return (l[i], common - l[i])


tower = buildTowerStructure(meta)
(balanced, rebalance_weight) = inTheForceAnUnbalanceIsSearched(tower)
print rebalance_weight

