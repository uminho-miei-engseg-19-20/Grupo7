# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# initSigner-app.py
#
# Cripto-7.0.2 - Commmad line app to exemplify the usage of initSigner
#       function (see eccblind.py)
#
# Copyright (c) 2016 Universidade do Minho
# Developed by André Baptista - Devise Futures, Lda. (andre.baptista@devisefutures.com)
# Reviewed by Ricardo Barroso - Devise Futures, Lda. (ricardo.barroso@devisefutures.com)
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
###############################################################################
"""
Command line app that writes initComponents and pRDashComponents to STDOUT.
"""

import sys
import ast
import optparse
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: python initSigner-app.py")

def init():
    initComponents, pRDashComponents = eccblind.initSigner()
    dict = {'initComponents' : initComponents, 'pRDashComponents' : pRDashComponents}
    f = open("assinante.txt", "w")
    f.write( str(dict) )
    f.close()
    print("InitComponents e pRDashComponents guardados no ficheiro \"assinante.txt\"")

def parseArgs():
    parser = optparse.OptionParser()
    parser.add_option("--init", action="store_true", dest="init", help="inicializa as varias componentes (InitComponents e pRDashComponents) e guarda-as")
    parser.set_defaults(init=False)

    (options, args) = parser.parse_args()

    if options.init:
        init()
    else:
        main()

def getPRDashComponents():
    with open("assinante.txt", "r") as file:
        s = file.read()
        dict = ast.literal_eval(s)
    file.close()

    prdash = dict.get('initComponents')
    return prdash

def main():
    #initComponents, pRDashComponents = eccblind.initSigner()
    #print("Output")
    #print("Init components: %s" % initComponents)
    print("pRDashComponents: %s" % getPRDashComponents())

if __name__ == "__main__":
    parseArgs()
