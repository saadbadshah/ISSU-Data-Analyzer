
import json
from statistics import variance

import matplotlib.pyplot as plt
import numpy as np
import re
from collections import Counter

#Author : Saad Badshah

class JsonData:
   def __init__(self,file):
       self.GetData(file)


## Continents dictionary taken from the simple_histo.py source code on course website.
   continents = {
       'AF': 'Africa',
       'AS': 'Asia',
       'EU': 'Europe',
       'NA': 'North America',
       'SA': 'South America',
       'OC': 'Oceania',
       'AN': 'Antarctica'
   }
   cntry_to_cont = {
       'AF': 'AS',
       'AX': 'EU',
       'AL': 'EU',
       'DZ': 'AF',
       'AS': 'OC',
       'AD': 'EU',
       'AO': 'AF',
       'AI': 'NA',
       'AQ': 'AN',
       'AG': 'NA',
       'AR': 'SA',
       'AM': 'AS',
       'AW': 'NA',
       'AU': 'OC',
       'AT': 'EU',
       'AZ': 'AS',
       'BS': 'NA',
       'BH': 'AS',
       'BD': 'AS',
       'BB': 'NA',
       'BY': 'EU',
       'BE': 'EU',
       'BZ': 'NA',
       'BJ': 'AF',
       'BM': 'NA',
       'BT': 'AS',
       'BO': 'SA',
       'BQ': 'NA',
       'BA': 'EU',
       'BW': 'AF',
       'BV': 'AN',
       'BR': 'SA',
       'IO': 'AS',
       'VG': 'NA',
       'BN': 'AS',
       'BG': 'EU',
       'BF': 'AF',
       'BI': 'AF',
       'KH': 'AS',
       'CM': 'AF',
       'CA': 'NA',
       'CV': 'AF',
       'KY': 'NA',
       'CF': 'AF',
       'TD': 'AF',
       'CL': 'SA',
       'CN': 'AS',
       'CX': 'AS',
       'CC': 'AS',
       'CO': 'SA',
       'KM': 'AF',
       'CD': 'AF',
       'CG': 'AF',
       'CK': 'OC',
       'CR': 'NA',
       'CI': 'AF',
       'HR': 'EU',
       'CU': 'NA',
       'CW': 'NA',
       'CY': 'AS',
       'CZ': 'EU',
       'DK': 'EU',
       'DJ': 'AF',
       'DM': 'NA',
       'DO': 'NA',
       'EC': 'SA',
       'EG': 'AF',
       'SV': 'NA',
       'GQ': 'AF',
       'ER': 'AF',
       'EE': 'EU',
       'ET': 'AF',
       'FO': 'EU',
       'FK': 'SA',
       'FJ': 'OC',
       'FI': 'EU',
       'FR': 'EU',
       'GF': 'SA',
       'PF': 'OC',
       'TF': 'AN',
       'GA': 'AF',
       'GM': 'AF',
       'GE': 'AS',
       'DE': 'EU',
       'GH': 'AF',
       'GI': 'EU',
       'GR': 'EU',
       'GL': 'NA',
       'GD': 'NA',
       'GP': 'NA',
       'GU': 'OC',
       'GT': 'NA',
       'GG': 'EU',
       'GN': 'AF',
       'GW': 'AF',
       'GY': 'SA',
       'HT': 'NA',
       'HM': 'AN',
       'VA': 'EU',
       'HN': 'NA',
       'HK': 'AS',
       'HU': 'EU',
       'IS': 'EU',
       'IN': 'AS',
       'ID': 'AS',
       'IR': 'AS',
       'IQ': 'AS',
       'IE': 'EU',
       'IM': 'EU',
       'IL': 'AS',
       'IT': 'EU',
       'JM': 'NA',
       'JP': 'AS',
       'JE': 'EU',
       'JO': 'AS',
       'KZ': 'AS',
       'KE': 'AF',
       'KI': 'OC',
       'KP': 'AS',
       'KR': 'AS',
       'KW': 'AS',
       'KG': 'AS',
       'LA': 'AS',
       'LV': 'EU',
       'LB': 'AS',
       'LS': 'AF',
       'LR': 'AF',
       'LY': 'AF',
       'LI': 'EU',
       'LT': 'EU',
       'LU': 'EU',
       'MO': 'AS',
       'MK': 'EU',
       'MG': 'AF',
       'MW': 'AF',
       'MY': 'AS',
       'MV': 'AS',
       'ML': 'AF',
       'MT': 'EU',
       'MH': 'OC',
       'MQ': 'NA',
       'MR': 'AF',
       'MU': 'AF',
       'YT': 'AF',
       'MX': 'NA',
       'FM': 'OC',
       'MD': 'EU',
       'MC': 'EU',
       'MN': 'AS',
       'ME': 'EU',
       'MS': 'NA',
       'MA': 'AF',
       'MZ': 'AF',
       'MM': 'AS',
       'NA': 'AF',
       'NR': 'OC',
       'NP': 'AS',
       'NL': 'EU',
       'NC': 'OC',
       'NZ': 'OC',
       'NI': 'NA',
       'NE': 'AF',
       'NG': 'AF',
       'NU': 'OC',
       'NF': 'OC',
       'MP': 'OC',
       'NO': 'EU',
       'OM': 'AS',
       'PK': 'AS',
       'PW': 'OC',
       'PS': 'AS',
       'PA': 'NA',
       'PG': 'OC',
       'PY': 'SA',
       'PE': 'SA',
       'PH': 'AS',
       'PN': 'OC',
       'PL': 'EU',
       'PT': 'EU',
       'PR': 'NA',
       'QA': 'AS',
       'RE': 'AF',
       'RO': 'EU',
       'RU': 'EU',
       'RW': 'AF',
       'BL': 'NA',
       'SH': 'AF',
       'KN': 'NA',
       'LC': 'NA',
       'MF': 'NA',
       'PM': 'NA',
       'VC': 'NA',
       'WS': 'OC',
       'SM': 'EU',
       'ST': 'AF',
       'SA': 'AS',
       'SN': 'AF',
       'RS': 'EU',
       'SC': 'AF',
       'SL': 'AF',
       'SG': 'AS',
       'SX': 'NA',
       'SK': 'EU',
       'SI': 'EU',
       'SB': 'OC',
       'SO': 'AF',
       'ZA': 'AF',
       'GS': 'AN',
       'SS': 'AF',
       'ES': 'EU',
       'LK': 'AS',
       'SD': 'AF',
       'SR': 'SA',
       'SJ': 'EU',
       'SZ': 'AF',
       'SE': 'EU',
       'CH': 'EU',
       'SY': 'AS',
       'TW': 'AS',
       'TJ': 'AS',
       'TZ': 'AF',
       'TH': 'AS',
       'TL': 'AS',
       'TG': 'AF',
       'TK': 'OC',
       'TO': 'OC',
       'TT': 'NA',
       'TN': 'AF',
       'TR': 'AS',
       'TM': 'AS',
       'TC': 'NA',
       'TV': 'OC',
       'UG': 'AF',
       'UA': 'EU',
       'AE': 'AS',
       'GB': 'EU',
       'US': 'NA',
       'UM': 'OC',
       'VI': 'NA',
       'UY': 'SA',
       'UZ': 'AS',
       'VU': 'OC',
       'VE': 'SA',
       'VN': 'AS',
       'WF': 'OC',
       'EH': 'AF',
       'YE': 'AS',
       'ZM': 'AF',
       'ZW': 'AF'
   }

   CountryOccurences = {}
   BrowserOccurences = {}
   DataList = []
   cntcontinent = {}
   RegexBrowser = []
   UserReadTime = {}
   Top10 = {}
   visitorUUID = []
   DocUUID = []

   def GetData(self,file):
      with open(file) as data:
          for Documents in data:
              #print(Documents)
              DataDict = json.loads(Documents)
              self.DataList.append(DataDict)

   def plot(self,x,y,xlabel,ylabel,title):


       #fig, ax = plt.subplots(figsize=(18, 11))
       plt.bar(x, y)
       plt.xticks(x, x)
       plt.xlabel(xlabel)
       plt.ylabel(ylabel)
       plt.title(title)
       #fig.tight_layout()
       plt.show()

   def getcountry(self,Doc_UUID):
       for countries in self.DataList:
           try:
               if Doc_UUID == countries["subject_doc_id"]:
                   CurrentCountry = countries["visitor_country"]
                   Sum = sum([1 for countries in self.DataList if CurrentCountry == countries["visitor_country"]])
                   self.CountryOccurences.update({countries["visitor_country"]: Sum})
           except KeyError:
               continue
   def DisplayCountry(self, Doc_UUID):
       self.getcountry(Doc_UUID)
       print(self.CountryOccurences)
       country = list(self.CountryOccurences.keys())
       occurences = list(self.CountryOccurences.values())
       self.plot(country,occurences,"Countries","Occurences","Countries of the viewers")



   def getcontinent(self):
       for country in self.CountryOccurences.keys():
           print("current country is " + country)
           for continent in self.cntry_to_cont.keys():
               if country == continent:
                   cnt = self.cntry_to_cont.get(continent)
                   for continentname in self.continents.keys():
                       if cnt == continentname:
                           name = self.continents.get(continentname)
                           self.cntcontinent.update({name: sum(self.CountryOccurences.values())})

       continent = list(self.cntcontinent.keys())
       occurences = list(self.cntcontinent.values())
       print(self.cntcontinent)
       self.plot(continent, occurences, "Continents", "Occurences", "Continents of the viewers")


   def CountryContrinent(self,Doc_UUID):
       if not self.CountryOccurences:
           self.getcountry(Doc_UUID)
           self.getcontinent()
       else:
           self.getcontinent()




   def rebrowser(self):
       for Browsers in self.DataList:
           Browser = Browsers["visitor_useragent"]
           browsersum = sum([1 for Browsers in self.DataList if Browser == Browsers["visitor_useragent"]])

           regex = re.findall("(?i)(firefox|chrome|safari|Mobile)",Browsers["visitor_useragent"])
           for x in regex:
               self.RegexBrowser.append(x)
           self.BrowserOccurences.update({Browsers["visitor_useragent"]:browsersum})

   def Browser3a(self):

      #(?i)(firefox|chrome|safari|Mobile)
       self.rebrowser()
       Browser = list(self.BrowserOccurences.keys())
       occurences = list(self.BrowserOccurences.values())
       self.plot(Browser, occurences, "Browser", "Occurences", "Popular browsers")

   def displayrebrowser(self):
       BrowserSum = dict(Counter(self.RegexBrowser))
       Browser = list(BrowserSum.keys())
       occurences = list(BrowserSum.values())
       self.plot(Browser, occurences, "Browser", "Occurences", "Popular browsers")

   def Browser3b(self):
       if not self.BrowserOccurences:
           self.rebrowser()
           self.displayrebrowser()
       else:
           self.displayrebrowser()



   def Readerprofile(self):
       for documents in self.DataList:
           readtime = 0
           UserId = documents["visitor_uuid"]
           for userId in self.DataList:
               if UserId == userId["visitor_uuid"] and userId.__contains__("event_readtime"):
                       readtime += userId["event_readtime"]
                      #print(readtime)
                       self.UserReadTime.update({UserId:readtime})

       top10 = Counter(self.UserReadTime)
       for user, time in top10.most_common(10):
           self.Top10.update({user:time})

       fig, ax = plt.subplots(figsize=(18, 9))
       fig.tight_layout()
       self.plot(list(self.Top10.keys()),list(self.Top10.values()) , "User", "Time", "Top 10 Users based on reading time")



   def AlsoLikesa(self, Doc_UUID):
       for document in self.DataList:
           if Doc_UUID == document["subject_doc_id"]:
               visitor_uuid = document["visitor_uuid"]
               self.visitorUUID.append(visitor_uuid)
       print(self.visitorUUID)



   def AlsoLikesb(self, visitorUUID):
       for document in self.DataList:
           if visitorUUID == document["visitor_uuid"]:
               document_uuid = document["subject_doc_id"]
               self.DocUUID.append(document_uuid)
       print(self.DocUUID)

   def AlsoLikes5d(self, visitorUUID):
       print("to implement")



