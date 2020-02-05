Regex_Pattern = r'(ok)(ok)(ok)+'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())