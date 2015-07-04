__author__ = 'nickv'


class Convertor:
    def headline(self, rst_file, wiki_headline, level=2):
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
