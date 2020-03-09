# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# generateBlindSignature-app.py
#
# Cripto-7.2.1 - Commmad line app to exemplify the usage of generateBlindSignature
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
Command line app that receives signer's private key from file and Passphrase, Blind message and
initComponents from STDIN and writes Blind signature to STDOUT.
"""

# blindSignature-app.py -key <chave privada> -bmsg <Blind message>

from eVotUM.Cripto import utils
import sys
import optparse
from eVotUM.Cripto import eccblind
import ast

def printUsage():
    print("Usage: python blindSignature-app.py --key <chave privada> --bmsg <Blind message>")

def parseArgs():
    parser = optparse.OptionParser()
    usage = "blindSignature-app.py --key <chave privada> --bmsg <Blind message>"
    parser.add_option("--key", action="store", type="string", dest="key", help="ficheiro que .pem com contem a chave privada")
    parser.add_option("--bmsg", action="store", type="string", dest="bmsg", help="Blinded message")

    (options, args) = parser.parse_args()

    if (len(sys.argv) != 5):
        printUsage()
    else:
        eccPrivateKeyPath = options.key
        blindedMsg = options.bmsg
        main(eccPrivateKeyPath, blindedMsg)

def getInitComponents():
    with open("assinante.txt", "r") as file:
        s = file.read()
        dict = ast.literal_eval(s)
    file.close()

    initC = dict.get('initComponents')
    return initC

def showResults(errorCode, blindSignature):
    print("Output")
    if (errorCode is None):
        print("Blind signature: %s" % blindSignature)
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the private key")
    elif (errorCode == 2):
        print("Error: init components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind message format")

def main(eccPrivateKeyPath, blindedMsg):
    pemKey = utils.readFile(eccPrivateKeyPath)
    print("Input")
    passphrase = raw_input("Passphrase: ")
    blindM = blindedMsg
    initComponents = getInitComponents()
    errorCode, blindSignature = eccblind.generateBlindSignature(pemKey, passphrase, blindM, initComponents)
    showResults(errorCode, blindSignature)

if __name__ == "__main__":
    parseArgs()
