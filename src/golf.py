# RegEx Golf: https://alf.nu/RegexGolf
## Name: 

# These are required -- you should submit a solution for all of them.
# Please put your solution between the quotation marks, e.g.
# all_as = r"a+"

"""
The website seems to accept my answer
 when I only match to parts of the target strings
  (and nothing in the non-targets). I still
  decided to find the regex that matches the entire
  strings.
"""

warmup = r"\w*foo\w*"
anchors = r"\w*k$"
it_never_ends = r"\w*u\b"
ranges = r"^[a-f]+$"
backrefs = r"(\w\w\w)\w*\1\w*"
abba = r"(\w*ef\w*)|^(?!(\w)+\2)"
a_man_a_plan = r"^(\w)[^p]\w*\1$"

# Discover NLP course materials authored by Julie Medero, Xanda Schofield, and Richard Wicentowski
# This work is licensed under a Creative Commons Attribution-ShareAlike 2.0 Generic License# https://creativecommons.org/licenses/by-sa/2.0/
