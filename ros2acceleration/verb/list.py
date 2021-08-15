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

from ctypes import *
from socket import *

from ros2cli.node.strategy import add_arguments as add_strategy_node_arguments
from ros2cli.node.strategy import NodeStrategy
from ros2acceleration.verb import VerbExtension
# from ros2topic.api import get_topic_names_and_types


DFX_MGRD_SERVER_SOCKET = "/tmp/dfx-mgrd.socket"
DFX_MGRD_FIRMWARE_PATH =	"/lib/firmware/xilinx"

DFX_MGRD_QUIT = 0
DFX_MGRD_GRAPH_INIT = 1
DFX_MGRD_GRAPH_FINALISE = 2
DFX_MGRD_GRAPH_SCHEDULED = 3
DFX_MGRD_GRAPH_GET_IOBUFF = 4
DFX_MGRD_GRAPH_SET_IOBUFF = 5
DFX_MGRD_LOAD_ACCEL = 6
DFX_MGRD_REMOVE_ACCEL = 7
DFX_MGRD_LIST_PACKAGE = 8
DFX_MGRD_GRAPH_INIT_DONE = 11
DFX_MGRD_GRAPH_FINALISE_DONE = 12


# """ This class defines a C-like struct """
#
# struct message {
#     uint32_t id;
#     uint32_t size;
#     uint32_t fdcount;
#     char data [32*1024];
# };
#
class Message(Structure):
    _fields_ = [("id", c_uint32),
                ("size", c_uint32),
                ("fdcount", c_uint32),
                ("data", c_byte * 32 * 1024)]


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

        # Create an un-bonded and non-connected socket.
        sock = socket(AF_UNIX, SOCK_SEQPACKET)

        # Connect to the server.
        sock.connect(DFX_MGRD_SERVER_SOCKET)

        # send request
        # list_request = Message(DFX_MGRD_LIST_PACKAGE, 0, 0, b'\000'*32*1024)
        list_request = Message(
                DFX_MGRD_LIST_PACKAGE, 
                0, 
                0, 
                (c_byte * 32 * 1024).from_buffer_copy(b'\000'*32*1024)                
        )

        
        # print("Sending id={:d}, counter={:d}, temp={:f}".format(payload_out.id,
        #                                                     payload_out.counter,
        #                                                     payload_out.temp))
        nsent = sock.send(list_request)

        # receive message, block until arrives
        buff = sock.recv(sizeof(Message))
        if not buff:
            print("It seems the other side has closed its connection")
        else:
            print(buff)

        # Close it
        sock.close()
