# -*- coding:utf-8 -*-
"""
Helper Functions for general use in Pablo

@author Aman
"""

'''
Monkey Patch for warnings.warn
Changes format of the warning output
'''
def format_warning(message, category, filename, lineno, line=None):
  fname = filename.split('/')[-1]
  return "%s:%s: %s: %s\n" % (fname, lineno, category.__name__, message)
