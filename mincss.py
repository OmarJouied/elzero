import re
from sys import argv

with open(argv[1], "r") as f:
    txt = f.read().replace("\n", "")
    selectors = [" ".join(new) + "{" for new in [re.compile("[^ ]+").findall(word) for word in [re.sub("[{}]|/.*/", "", item)  for item in re.compile("}?[^{}]*{").findall(txt)]]]
    properties = [re.sub(" +|/.*/", "", item).replace(";}", "}") for item in re.compile("[^{}]*}").findall(txt)]