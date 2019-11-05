#!/usr/bin/env python3
#  -------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#  -------------------------------------------------------------------------------


import io
import os
import sys


class Bubble:

  def __init__(self, start=None, end=None):
    self.id = None
    self.start = start
    self.end = end
    self.nodes = []
    self.children = []
