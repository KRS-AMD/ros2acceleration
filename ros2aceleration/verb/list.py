#    ____  ____
#   /   /\/   /
#  /___/  \  /   Copyright (c) 2021, Xilinx®.
#  \   \   \/    Author: Víctor Mayoral Vilches <victorma@xilinx.com>
#   \   \
#   /   /
#  /___/   /\
#  \   \  /  \
#   \___\/\___\
#
# Licensed under the Apache License, Version 2.0
# 

from ros2cli.node.strategy import add_arguments as add_strategy_node_arguments
from ros2cli.node.strategy import NodeStrategy
from ros2topic.api import get_topic_names_and_types
from ros2topic.verb import VerbExtension


class ListVerb(VerbExtension):
    """Output a list of available topics."""

    # def add_arguments(self, parser, cli_name):
    #     add_strategy_node_arguments(parser)

    #     parser.add_argument(
    #         '-t', '--show-types', action='store_true',
    #         help='Additionally show the topic type')
    #     parser.add_argument(
    #         '-c', '--count-topics', action='store_true',
    #         help='Only display the number of topics discovered')
    #     # duplicate the following argument from the command for visibility
    #     parser.add_argument(
    #         '--include-hidden-topics', action='store_true',
    #         help='Consider hidden topics as well')
    #     parser.add_argument(
    #         '-v', '--verbose', action='store_true',
    #         help='List full details about each topic')

    def main(self, *, args):
        print("Should list in here accelerators available")
