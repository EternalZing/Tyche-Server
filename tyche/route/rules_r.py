# pylint: disable=E1101
from . import rule


@rule.route('/get/<rulename>', methods=['GET', 'POST'])
def get_rule():
    '''apply when create rules '''
    return "get rule"


@rule.route('/create/<rulename>', methods=['POST'])
def create_rule():
    '''apply when create rules '''
    return "create rule"


@rule.route('/modified/<rulename>', methods=['POST'])
def modify_rule():
    '''apply when modify rules '''
    return "modify rule"
