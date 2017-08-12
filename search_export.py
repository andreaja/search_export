#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('web_data.sqlite')
c = conn.cursor()
print """
<!DOCTYPE NETSCAPE-Bookmark-file-1>
    <!--This is an automatically generated file.
    It will be read and overwritten.
    Do Not Edit! -->
    <Title>Bookmarks</Title>
    <H1>Bookmarks</H1>
"""


print """
    <DL>
"""

r=c.execute('SELECT url,keyword,short_name FROM keywords')
all_searches = r.fetchall()

print len(all_searches)
for row in all_searches:
    url = row[0].encode('utf8')
    keyword = row[1].encode('utf8')
    short_name = row[2].encode('utf8')
    url = url.replace('{searchTerms}', '%s')
    print '<DT><A HREF="%s" SHORTCUTURL="%s">%s</A>' % (url, keyword, short_name)

print """
    </DL>
"""
conn.close()
