from flask import Blueprint
import os
from tyche_config import DEFAULT_RULES
from service import rule_manager

rule = Blueprint('rule', __name__)


@rule.route('/get/<rulename>', methods=['GET', 'POST'])
def get_rule(rulename):
    '''apply when getting rules '''

    print("get rule %s" % rulename)
    if rulename in DEFAULT_RULES:
        return rule_manager.get_by_rulename(rulename)


@rule.route('/getlist', methods=['GET', 'POST'])
def get_list():
    '''get rule list'''

    print("get rules")
    return rule_manager.get_rule_list()


@rule.route('/create/<rulename>', methods=['POST'])
def create_rule(rulename):
    '''apply when creating rules '''
    return "create rule"


@rule.route('/modified/<rulename>', methods=['POST'])
def modify_rule(rulename):
    '''apply when modifying rules '''
    return "modify rule"
