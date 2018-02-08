import os
import json


class RulePair(object):
    def __init__(self, rid, name):
        self.rid = rid
        self.name = name


def R2J(obj):
    return {"name": obj.name, "id": obj.rid}


class RuleManager(object):
    def get_by_rulename(self, rulename):
        with open(self.rulepath + '/' + rulename, 'r') as rule:
            res = rule.read()
        return res

    def get_rule_list(self):
        '''now only local'''
        files = os.listdir(self.rulepath)
        idcount = 0
        if (len(self.rulelist) > 0):
            return json.dumps(self.rulelist)
        for file in files:
            res = os.path.splitext(file)
            if res[1] == '.json':
                self.rulelist.append(R2J(RulePair(idcount, res[0])))
        return json.dumps(self.rulelist)

    def __init__(self, rulepath):
        self.rulepath = rulepath
        self.rulelist = []
