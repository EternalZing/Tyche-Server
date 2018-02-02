from . import rule
import os
from tyche.tyche_config import DEFAULT_RULES
from tyche.service import rule_manager

@rule.route('/get/<rulename>', methods=['GET', 'POST'])
def get_rule(rulename):
    '''apply when getting rules '''
    print("get rule %s" % rulename)
    if rulename in DEFAULT_RULES:
        return rule_manager.get_by_rulename(rulename)


@rule.route('/create/<rulename>', methods=['POST'])
def create_rule(rulename):
    '''apply when creating rules '''
    return "create rule"


@rule.route('/modified/<rulename>', methods=['POST'])
def modify_rule(rulename):
    '''apply when modifying rules '''
    return "modify rule"
