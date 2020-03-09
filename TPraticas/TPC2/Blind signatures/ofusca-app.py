# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# generateBlindData-app.py
#
# Cripto-7.1.1 - Commmad line app to exemplify the usage of blindData
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
Command line app that receives Data and pRDashComponents from STDIN and writes
blindMessage and blindComponents and pRComponents to STDOUT.
"""

import sys
from eVotUM.Cripto import eccblind
import optparse


def printUsage():
    print("Usage: python ofusca-app.py --msg <mensagem a assinar> --RDash <pRDashComponents>")

def parseArgs():
    parser = optparse.OptionParser()
    usage = "ofusca-app.py --msg <mensagem a assinar> --RDash <pRDashComponents>"
    parser.add_option("--msg", action="store", type="string", dest="msg", help="Mensagem a assinar")
    parser.add_option("--RDash", action="store", type="string", dest="rdash", help="pRDashComponent")

    (options, args) = parser.parse_args()

    if (len(sys.argv) > 5):
        printUsage()
    else:
        msg = options.msg
        prdash = options.rdash
        main(msg, prdash)

def showResults(errorCode, result):
    print("Output")
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        print("Blind message: %s" % blindM)
        #print("Blind components: %s" % blindComponents)
        #print("pRComponents: %s" % pRComponents)
        dict = {'blindComponents' : blindComponents, 'pRComponents' : pRComponents}
        f = open("requerente.txt", "w")
        f.write( str(dict) )
        f.close()
        print("blindComponents e pRComponents guardados no ficheiro \"requerente.txt\"")
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

def main(msg, prdash):
    #print("Input")
    data = msg
    pRDashComponents = prdash
    errorCode, result = eccblind.blindData(pRDashComponents, data)
    showResults(errorCode, result)

if __name__ == "__main__":
    parseArgs()
