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

from ros2pkg.api import package_name_completer
from ros2cli.node.strategy import add_arguments as add_strategy_node_arguments
from ros2cli.node.strategy import NodeStrategy
from ros2acceleration.verb import VerbExtension, run


def remove_dfx():
    cmd = "dfx-mgr-client -remove"
    outs, errs = run(cmd, shell=True)
    if outs:
        print(outs)


class RemoveVerb(VerbExtension):
    """Remove the acceleration kernel."""

    def main(self, *, args):
        remove_dfx()




