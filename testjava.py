
# -*- coding: utf-8 -*-
# python3
__author__ = 'hawk'
import sys

sys.path.append("lib")
import javalib
import snowflake
import pinyinlib

print javalib.getHashCode("12345")
print javalib.getHashCode("234567")

s = snowflake.generator(1, 1)
print s.next()

print pinyinlib.single_get_first("可")
print pinyinlib.multi_get_letter("中国人")