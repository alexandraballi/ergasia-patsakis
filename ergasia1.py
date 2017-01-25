#!/usr/bin/env python
# -*- coding: utf-8 -*-

userinput=raw_input("Δώσε μια είσοδο\n") 
def sinthiki(dexia_parenthesi,aristeri_paranthesi):
  if dexia_parenthesi==aristeri_paranthesi: 
     print "Είναι μαθηματική πράξη"
  else:
     print "Δεν είναι μαθηματική πράξη"
sinthiki(userinput.count('('),userinput.count(')'))


