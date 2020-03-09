# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# verifySignature-app.py
#
# Cripto-7.4.1 - Commmad line app to exemplify the usage of verifySignature
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
Command line app that receives signer's public key from file and Data, Signature, Blind Components and
prComponents from STDIN and writes a message to STDOUT indicating if the signature is valid..
"""

import sys
from eVotUM.Cripto import eccblind
from eVotUM.Cripto import utils
import optparse
import ast

def printUsage():
    print("Usage: python verify-app.py --cert <certificado do assinante> --msg <mensagem original a assinar> --sDash <Signature> -f <ficheiro do requerente>")

def parseArgs():
    parser = parser = optparse.OptionParser()
    usage = "verify-app.py -cert <certificado do assinante> -msg <mensagem original a assinar> -sDash <Signature> -f <ficheiro do requerente>"
    parser.add_option("--cert", action="store", type="string", dest="cert", help="Certificado do assinante")
    parser.add_option("--msg", action="store", type="string", dest="msg", help="Mensagem original a assinar")
    parser.add_option("--sDash", action="store", type="string", dest="sDash", help="Signature")
    parser.add_option("-f", action="store", type="string", dest="f", help="Ficheiro do requerente")

    (options, args) = parser.parse_args()

    if (len(sys.argv) != 9):
        printUsage()
    else:
        eccPublicKeyPath = options.cert
        msg = options.msg
        sDash = options.sDash
        f = options.f
        main(eccPublicKeyPath, msg, sDash, f)

def showResults(errorCode, validSignature):
    print("Output")
    if (errorCode is None):
        if (validSignature):
            print("Valid signature")
        else:
            print("Invalid signature")
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the public key")
    elif (errorCode == 2):
        print("Error: pR components are invalid")
    elif (errorCode == 3):
        print("Error: blind components are invalid")
    elif (errorCode == 4):
        print("Error: invalid signature format")

def getDict(f):
    with open(f, "r") as file:
        s = file.read()
        dict = ast.literal_eval(s)
    file.close()
    return dict

def main(eccPublicKeyPath, msg, sDash, f):
    pemPublicKey = utils.readFile(eccPublicKeyPath)
    #print("Input")
    data = msg
    signature = sDash
    dict = getDict(f)
    blindComponents = dict.get('blindComponents')
    pRComponents = dict.get('pRComponents')
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature, blindComponents, pRComponents, data)
    showResults(errorCode, validSignature)

if __name__ == "__main__":
    parseArgs()
