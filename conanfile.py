#/usr/bin/env python
#-*- coding:utf-8 -*-
from conans import ConanFile, CMake

# package list
class MylibConan(ConanFile):
    setting = "os", "compiler", "build_type", "arch"
    requires = (("cctz/2.2@bincrafters/stable"),\
                ("gtest/1.8.1@bincrafters/stable"))
    generators = "cmake"
    option = {"cctz:shared" : True, "cctz:fPIC" : True,\
              "gtest:shared" : True}