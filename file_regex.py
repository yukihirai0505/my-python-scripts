# -*- coding: utf-8 -*-
import re

file_name = 'wedding'

org_file = open(file_name + '.txt')
lines = org_file.readlines()
org_file.close()

dist_file = open(file_name + '_after.txt', 'w')
pattern = r'title=\".+?\"'
all_title = re.findall(pattern, ''.join(lines))
if all_title:
    for title in all_title:
        dist_file.write(title.replace('\"', '').replace('title=', '') + '\n')


dist_file.close()
