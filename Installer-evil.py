#!/usr/bin/env python
# vim: set fileencoding=latin-1 :

import sys
import os
                                                                                                                                                                                                                                                                                                                                                                                                                                         
a = b'''%PDF-1.3
%����


1 0 obj
<</Width 2 0 R/Height 3 0 R/Type 4 0 R/Subtype 5 0 R/Filter 6 0 R/ColorSpace 7 0 R/Length 8 0 R/BitsPerComponent 8>>
stream
���� $SHA-1 is dead!!!!!�/�	#9u�9���<L����Fܓ��~;���VE�gֈ��K�Ly�+=��m�i	�kE�S
�߷`8�rr/�r�I�F�0W�����.���+�5B��-���*3.��5�M�,��t�x0Z!Vda0��`kп?�ͨF)�'''

if ord(a[-1]) == 0xb1: #blob1
    print("I am good!")
else:
    print("I am evil!")