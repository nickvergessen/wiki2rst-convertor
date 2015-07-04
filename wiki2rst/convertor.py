__author__ = 'nickv'


class Convertor:
    def __init__(self):
        pass

    @staticmethod
    def headline(rst_file, wiki_headline, level=2):
        """
        :param rst_file:
        :param wiki_headline:
        :param level:

        :type rst_file: FileIO
        :type wiki_headline: string
        :type level: int
        :rtype : object

        Wiki:
         1.  = Notable Changes =

         2.  == Notable Changes ==

         3.  ==== Notable Changes ====

        rST:
         1.  ===============
             Notable Changes
             ===============

         2.  Notable Changes
             ===============

         3.  Notable Changes
             ---------------
        """

        headline_char = "="
        if level == 3:
            headline_char = "-"

        headline = wiki_headline[(level + 1):-(level + 1)]
        headline_len = len(headline)

        if level == 1:
            rst_file.write("%s" % (headline_len * headline_char))
        rst_file.write(headline)
        rst_file.write("\n")
        rst_file.write("%s" % (headline_len * headline_char))
        rst_file.write("\n")
        rst_file.write("\n")

    def links(self, wiki_line):
        """
        :param wiki_line: string

        :type wiki_line: string
        :rtype : string

        Wiki:
        [https://developer.mozilla.org/en/Localization_and_Plurals Mozilla]

        rST:
        `Mozilla <https://developer.mozilla.org/en/Localization_and_Plurals>`_
        """

        link_start = wiki_line.find("[http")
        if link_start > -1:
            link_end = wiki_line.find("]", link_start)
            link_desc_start = wiki_line.find(" ", link_start, link_end)

            print "Found link: %s" % wiki_line[link_start + 1:link_desc_start]
            new_line = wiki_line[:link_start]
            new_line += "`"
            new_line += wiki_line[link_desc_start + 1:link_end]
            new_line += " <"
            new_line += wiki_line[link_start + 1:link_desc_start]
            new_line += ">`_"
            new_line += wiki_line[link_end + 1:]

            return self.links(new_line)

        return wiki_line
