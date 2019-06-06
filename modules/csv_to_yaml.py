#!/usr/bin/env python
 
import csv
import sys
import yaml
 
csv_data = []
with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        csv_data.append(row)
 
with open('group_vars/all' + '.yml', 'w') as outfile:
    outfile.write(yaml.dump({'data': csv_data}))
