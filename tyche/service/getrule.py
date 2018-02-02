import os


class RuleManager(object):
    def get_by_rulename(self, rulename):
        with open(self.rulepath + '/' + rulename, 'r') as rule:
            res = rule.read()
        return res

    def __init__(self, rulepath):
        self.rulepath = rulepath


from tyche.tyche_config import RULE_PATH
rule_manager = RuleManager(RULE_PATH)
