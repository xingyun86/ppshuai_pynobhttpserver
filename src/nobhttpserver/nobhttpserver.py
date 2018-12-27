#!coding:utf-8
#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-

import os
import sys
import socket
import SocketServer
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

from modules.sigs import CSigs


class NOBHTTPRequestHandler (SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods",
                         "POST, GET, OPTIONS, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers",
                         "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization")
        SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


class ForkingHTTPServerOnlyLinux(SocketServer.ForkingTCPServer):

    # Allow reuse address
    allow_reuse_address = 1

    def server_bind(self):
        """Override server_bind to store the server name."""
        SocketServer.TCPServer.server_bind(self)
        host, port = self.socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port


def StartHttpServerOnlyLinux(HandlerClass=SimpleHTTPRequestHandler, ServerClass=ForkingHTTPServerOnlyLinux, ProtocolVersion="HTTP/1.0"):
    """
    HTTP request handler class.

    This runs an HTTP server on port 8000 (or the first command line
    argument).

    ProtocolVersion -- "HTTP/1.0","HTTP/1.1","HTTP/2.0"

    """

    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000

    if sys.argv[2:]:
        root = sys.argv[2]
    else:
        root = os.getcwd()

    # root path is exist
    if not os.path.isdir(root):
        try:
            os.makedirs(root)
        except Exception:
            pass

    # root path is exist again
    if os.path.isdir(root):
        os.chdir(root)
        server_address = ("", port)

        HandlerClass.protocol_version = ProtocolVersion
        httpd = ServerClass(server_address, HandlerClass)

        sa = httpd.socket.getsockname()
        print "Serving HTTP on", sa[0], "port", sa[1],  "root", root, "..."
        httpd.serve_forever()


class ThreadingHTTPServer(SocketServer.ThreadingTCPServer):

    # Allow reuse address
    allow_reuse_address = 1

    def server_bind(self):
        """Override server_bind to store the server name."""
        SocketServer.TCPServer.server_bind(self)
        host, port = self.socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port


def StartHttpServer(HandlerClass=SimpleHTTPRequestHandler, ServerClass=ThreadingHTTPServer, ProtocolVersion="HTTP/1.0"):
    """
    HTTP request handler class.

    This runs an HTTP server on port 8000 (or the first command line
    argument).

    ProtocolVersion -- "HTTP/1.0","HTTP/1.1","HTTP/2.0"

    """

    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000

    if sys.argv[2:]:
        root = sys.argv[2]
    else:
        root = os.getcwd()

    # root path is exist
    if not os.path.isdir(root):
        try:
            os.makedirs(root)
        except Exception:
            pass

    # root path is exist again
    if os.path.isdir(root):
        os.chdir(root)
        server_address = ("", port)

        HandlerClass.protocol_version = ProtocolVersion
        httpd = ServerClass(server_address, HandlerClass)

        sa = httpd.socket.getsockname()
        print "Serving HTTP on", sa[0], "port", sa[1],  "root", root, "..."
        httpd.serve_forever()


'''
自定义主函数
'''


def main():

    # 注册CTRL+C的信号处理
    CSigs.reg_sig()

    while(True):
        try:
            # Multi-processes service only on linux
            # StartHttpServerOnlyLinux()
            # Multi-threads service on all the systems
            StartHttpServer(NOBHTTPRequestHandler)
        except Exception, e:
            print("Exception:" + str(e))
            pass


if __name__ == "__main__":
    main()
