# -*- coding: utf-8 -*-

"""
 Copyright 2016 cocoatomo

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import pytest
from pygments.token import Text, Whitespace, Keyword, Name, Literal, String, Number, Operator, Punctuation, Comment
from dmdl.lexer import DmdlLexer

dmdl = DmdlLexer()

@pytest.mark.parametrize(
    ('text', 'tokens'),
    [
        (
            'sample = { id : INT; };',
            [(Name.Class, 'sample'),
             (Whitespace, ' '),
             (Operator, '='),
             (Whitespace, ' '),
             (Punctuation, '{'),
             (Whitespace, ' '),
             (Name, 'id'),
             (Whitespace, ' '),
             (Punctuation, ':'),
             (Whitespace, ' '),
             (Keyword.Type, 'INT'),
             (Punctuation, ';'),
             (Whitespace, ' '),
             (Punctuation, '}'),
             (Punctuation, ';'),
             (Whitespace, '\n'),]
        ),
        (
            '"description" sample = { id : INT; };',
            [(String.Double, '"'),
             (String.Double, 'd'),
             (String.Double, 'e'),
             (String.Double, 's'),
             (String.Double, 'c'),
             (String.Double, 'r'),
             (String.Double, 'i'),
             (String.Double, 'p'),
             (String.Double, 't'),
             (String.Double, 'i'),
             (String.Double, 'o'),
             (String.Double, 'n'),
             (String.Double, '"'),
             (Whitespace, ' '),
             (Name.Class, 'sample'),
             (Whitespace, ' '),
             (Operator, '='),
             (Whitespace, ' '),
             (Punctuation, '{'),
             (Whitespace, ' '),
             (Name, 'id'),
             (Whitespace, ' '),
             (Punctuation, ':'),
             (Whitespace, ' '),
             (Keyword.Type, 'INT'),
             (Punctuation, ';'),
             (Whitespace, ' '),
             (Punctuation, '}'),
             (Punctuation, ';'),
             (Whitespace, '\n'),]
        ),
        (
            '@attr sample = { id : INT; };',
            [(Name.Attribute, '@'),
             (Name.Attribute, 'attr'),
             (Whitespace, ' '),
             (Name.Class, 'sample'),
             (Whitespace, ' '),
             (Operator, '='),
             (Whitespace, ' '),
             (Punctuation, '{'),
             (Whitespace, ' '),
             (Name, 'id'),
             (Whitespace, ' '),
             (Punctuation, ':'),
             (Whitespace, ' '),
             (Keyword.Type, 'INT'),
             (Punctuation, ';'),
             (Whitespace, ' '),
             (Punctuation, '}'),
             (Punctuation, ';'),
             (Whitespace, '\n'),]
        ),
        (
            '"description" @attr sample = { id : INT; };',
            [(String.Double, '"'),
             (String.Double, 'd'),
             (String.Double, 'e'),
             (String.Double, 's'),
             (String.Double, 'c'),
             (String.Double, 'r'),
             (String.Double, 'i'),
             (String.Double, 'p'),
             (String.Double, 't'),
             (String.Double, 'i'),
             (String.Double, 'o'),
             (String.Double, 'n'),
             (String.Double, '"'),
             (Whitespace, ' '),
             (Name.Attribute, '@'),
             (Name.Attribute, 'attr'),
             (Whitespace, ' '),
             (Name.Class, 'sample'),
             (Whitespace, ' '),
             (Operator, '='),
             (Whitespace, ' '),
             (Punctuation, '{'),
             (Whitespace, ' '),
             (Name, 'id'),
             (Whitespace, ' '),
             (Punctuation, ':'),
             (Whitespace, ' '),
             (Keyword.Type, 'INT'),
             (Punctuation, ';'),
             (Whitespace, ' '),
             (Punctuation, '}'),
             (Punctuation, ';'),
             (Whitespace, '\n'),]
        ),
        (
            'projective sample = { id : INT; };',
            [(Keyword.Type, 'projective'),
             (Whitespace, ' '),
             (Name.Class, 'sample'),
             (Whitespace, ' '),
             (Operator, '='),
             (Whitespace, ' '),
             (Punctuation, '{'),
             (Whitespace, ' '),
             (Name, 'id'),
             (Whitespace, ' '),
             (Punctuation, ':'),
             (Whitespace, ' '),
             (Keyword.Type, 'INT'),
             (Punctuation, ';'),
             (Whitespace, ' '),
             (Punctuation, '}'),
             (Punctuation, ';'),
             (Whitespace, '\n'),]
        ),
        (
            'joined sample_ext = sample + sub;',
            [(Keyword.Type, 'joined'),
             (Whitespace, ' '),
             (Name.Class, 'sample_ext'),
             (Whitespace, ' '),
             (Operator, '='),
             (Whitespace, ' '),
             (Name.Class, 'sample'),
             (Whitespace, ' '),
             (Operator, '+'),
             (Whitespace, ' '),
             (Name.Class, 'sub'),
             (Punctuation, ';'),
             (Whitespace, '\n'),]
        ),
        (
            'summarized sum_sample = sample => { any key -> key; } % key',
            [(Keyword.Type, 'summarized'),
             (Whitespace, ' '),
             (Name.Class, 'sum_sample'),
             (Whitespace, ' '),
             (Operator, '='),
             (Whitespace, ' '),
             (Name.Class, 'sample'),
             (Whitespace, ' '),
             (Operator, '=>'),
             (Whitespace, ' '),
             (Punctuation, '{'),
             (Whitespace, ' '),
             (Name.Function, 'any'),
             (Whitespace, ' '),
             (Name, 'key'),
             (Whitespace, ' '),
             (Operator, '->'),
             (Whitespace, ' '),
             (Name, 'key'),
             (Punctuation, ';'),
             (Whitespace, ' '),
             (Punctuation, '}'),
             (Whitespace, ' '),
             (Operator, '%'),
             (Whitespace, ' '),
             (Name, 'key'),
             (Whitespace, '\n'),]
        ),
    ]
)
def test_Dmdl(text, tokens):
    for index, token in enumerate(dmdl.get_tokens(text)):
        assert token == tokens[index]
