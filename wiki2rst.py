from wiki2rst.convertor import Convertor

__author__ = 'nickv'

source_file = open("test/release-highlight.wiki", "r")
target_file = open("test/release-highlight.rst", "w")

convertor = Convertor()
for line in source_file:
    line = line.rstrip()
    if line[:2] == '= ' and line[-2:] == ' =':
        print "Found headline: %s" % line[2:-2]
        convertor.headline(target_file, line, level=1)
        continue
    if line[:3] == '== ' and line[-3:] == ' ==':
        print "Found headline: %s" % line[3:-3]
        convertor.headline(target_file, line, level=2)
        continue
    if line[:4] == '=== ' and line[-4:] == ' ===':
        print "Found headline: %s" % line[4:-4]
        convertor.headline(target_file, line, level=3)
        continue

    line = convertor.links(line)

    target_file.write(line)
    target_file.write("\n")

source_file.close()
target_file.close()
