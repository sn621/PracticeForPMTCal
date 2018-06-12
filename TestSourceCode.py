########################################
# TestSourceCode.py
# 
# Developed by Shunsuke SAKURAI
#
# Last Update: 11 Jun. 2018
########################################
##############################
# import libraries
##############################
import sys # for getting argument
import math # for mathmatics calculation

##############################
# main funciton
##############################
var_a = sys.argv[1]
var_b = sys.argv[2]

var_x = math.sin(var_a * var_b) # x = a * b

print "The answer x is ％f" % var_x
