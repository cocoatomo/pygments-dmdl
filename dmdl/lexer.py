# -*- coding: utf-8 -*-

from pygments.lexer import RegexLexer
from pygments.token import Text

class DmdlLexer(RegexLexer):
    name = 'Dmdl'
    aliases = ['dmdl']
    filenames = ['*.dmdl']

    tokens = {
        'root' : [
            (r'TRUE', Text)
        ]
    }
