#!/usr/bin/env python
import os
import re
import inspect
import codecs
import io #py3 open unicode behaviour
import csv

class Businesscard:

 def __init__(self, name):
    self.name = name
    self.lastname = lastname
    self.firstname = firstname
    self.company = company
    self.jobtitle = jobtitle
    self.email = email
    self.city = city
    self.addressline1 = addressline1
    self.postalcode = postalcode
    self.fedstate = fedstate
    self.website = website
    self.cellphone = cellphone
    self.officephone = officephone

cleaned_content = []
templine = "AAAAAAAAA"
counter = 0
counter2 = 0


#def inplace_change(filename, old_string, new_string):

#create an object of class "Businesscard" named after the person's full name
#find the string between the first two " in a line and use that as the object's name
#string1 = line()

with open("camcard_export/contacts_copiedtext.csv") as f:
    content = f.readlines()
    for line in content:
        counter2 = 0
        counter = counter+1        
        if line.startswith("Gesch"):
            templine = line
            for line2 in content:
                counter2 = counter2+1
                if (counter2+1) == counter:
                    print line2

                    #cleaned_content.append(templine+line)
#for line in cleaned_content:
    #print line

#with codecs.open("output.csv", "wb", "utf-8") as f:
 #   writer = csv.writer(f, lineterminator='\n')
  #  for val in cleaned_content:
   #     writer.writerow([val]) 

        #Concatenate lines that were split with /n
        #if 'Gesch' in line:
            #Return line number and set it to line number of preceding line
            #print num
          #join split line with its second part
          #for line in f:
            #if lineno() == splitline
            #line.rstrip("\n")
            #Perform operations for splitlines
        #Perform operations for non-splitlines
            
            #concatenate two lines
        #line = re.sub('\nGesch', 'Gesch', line)
        #if line.__contains__('\nGesch'):
            #line.replace('\nGesch', ';Gesch')
        #print line
        #print splitline
            #if "\t" in line:
                #end_position = line.find('\t')
                #print str(line[1:(end_position-2)])
                #result.append(line)
                #print end_position-2
                #print str(line[1:(end_position-2)])


#print result