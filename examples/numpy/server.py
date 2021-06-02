#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (c) RVBUST, Inc - All rights reserved.

import zerorpc
import numpy as np

class Foo(object):
    def send_array(self, rows, cols):
        return np.zeros(rows*cols, dtype = np.float)

sg_service = "tcp://0.0.0.0:4242"

s = zerorpc.Server(Foo())
s.bind(sg_service)
s.run()
