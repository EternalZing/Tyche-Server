# pylint: disable=E0401
from tyche_config import RULE_PATH
from .getrule import RuleManager

rule_manager = RuleManager(RULE_PATH)
