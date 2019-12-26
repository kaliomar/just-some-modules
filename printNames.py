#!/usr/bin/env python

# Forked from "https://github.com/Roshanjossey/Blind-watchmaker", but I will recode it for printing different words and names as user need.

import string
import os
import random
import time
from sys import platform

CharList = string.ascii_lowercase + string.ascii_uppercase + string.digits + '|:/    \\\''


target = ['TTTTTTTTTTTTTTTTTTTTTTT                                                    iiii                          ',
          'T:::::::::::::::::::::T                                                   i::::i                         ',
          'T:::::::::::::::::::::T                                                    iiii                          ',
          'T:::::TT:::::::TT:::::T                                                                                  ',
          'TTTTTT  T:::::T  TTTTTTaaaaaaaaaaaaa      ssssssssss   nnnn  nnnnnnnn    iiiiiii    mmmmmmm    mmmmmmm   ',
          '        T:::::T        a::::::::::::a   ss::::::::::s  n:::nn::::::::nn  i:::::i  mm:::::::m  m:::::::mm ',
          '        T:::::T        aaaaaaaaa:::::ass:::::::::::::s n::::::::::::::nn  i::::i m::::::::::mm::::::::::m',
          '        T:::::T                 a::::as::::::ssss:::::snn:::::::::::::::n i::::i m::::::::::::::::::::::m',
          '        T:::::T          aaaaaaa:::::a s:::::s  ssssss   n:::::nnnn:::::n i::::i m:::::mmm::::::mmm:::::m',
          '        T:::::T        aa::::::::::::a   s::::::s        n::::n    n::::n i::::i m::::m   m::::m   m::::m',
          '        T:::::T       a::::aaaa::::::a      s::::::s     n::::n    n::::n i::::i m::::m   m::::m   m::::m',
          '        T:::::T      a::::a    a:::::assssss   s:::::s   n::::n    n::::n i::::i m::::m   m::::m   m::::m',
          '      TT:::::::TT    a::::a    a:::::as:::::ssss::::::s  n::::n    n::::ni::::::im::::m   m::::m   m::::m',
          '      T:::::::::T    a:::::aaaa::::::as::::::::::::::s   n::::n    n::::ni::::::im::::m   m::::m   m::::m',
          '      T:::::::::T     a::::::::::aa:::as:::::::::::ss    n::::n    n::::ni::::::im::::m   m::::m   m::::m',
          '      TTTTTTTTTTT      aaaaaaaaaa  aaaa sssssssssss      nnnnnn    nnnnnniiiiiiiimmmmmm   mmmmmm   mmmmmm', ]

generation = [''.join(random.choice(CharList) for i in range(105)) for j in range(16)]
nxgen = ''
completed = False

while completed is False:
  if platform == "linux" or platform == "linux2" or platform == "darwin":
    os.system('clear')
  else:
    os.system('cls')
  for x in generation:
    print(x)
  completed = True
  for i in range(16):
    nxgen = ''
    for j in range(105):
      if generation[i][j] != target[i][j]:
        completed = False
        nxgen += random.choice(CharList)
      else:
        nxgen += target[i][j]
    generation[i] = nxgen
  time.sleep(0.1)
