#!"C:\Program Files\Python 3.5\python.exe"
print("Content-Type: text/html \n\n")
import cgi,cgitb
from bs4 import BeautifulSoup
import requests, json
import random
from operator import itemgetter

#print("Content-Type: text/html \n\n")                      
 
cgitb.enable() #for debugging
form = cgi.FieldStorage()
filter = []


destination = form.getvalue('destination')
#print(destination)
date =  form.getvalue('date')
#print(date)
time_span = form.getvalue('timespan')
#print(time_span)
if time_span == "10am-4pm":
    time = 6
elif time_span == "10am-6pm":
    time = 8
elif time_span == "10am-8pm":
    time = 10

if form.getvalue('adventure'):
    fil = form.getvalue('adventure')
    filter.append(fil)
    if destination == 'Delhi':
        class adventureplaces:
            #def __init():
                
             def fetch(self):
                 
                url = "https://www.thrillophilia.com/adventure-sports-in-delhi"
                r = requests.get(url)
                soup = BeautifulSoup(r.text, 'html.parser')
                data =soup.select(".clickable-image")
                #print(data)
                uniq_list=[]
                for names in data:
                    attr=names.attrs
                    uniq_list.append(attr['alt'])
                uniq_list = list(set(uniq_list))
                #print(uniq_list)
                file = open('adventure-Delhi.txt', 'a')
                for names in uniq_list:
                    file.write("%s\n" % names.encode('utf8'))
                file.close()
        res = adventureplaces()
        res.fetch()    

if form.getvalue('monument'):
    fil = form.getvalue('monument')
    filter.append(fil)
    if destination == 'Delhi':
            #print("True")
            class monuments:
                def fetch(self):
                        url = "https://www.ixigo.com/monuments-in-of-around-near-new-delhi-lp-1140454"
                        r = requests.get(url)
                        soup = BeautifulSoup(r.text, 'html.parser')
                        da =soup.select(".ne-title")
                 #print(da)
                        file = open('monument-Delhi.txt', 'a')
                
                        for names in da:
                    
                                #print(names.text)
                                file.write("%s\n" % names.text.strip().encode('utf-8'))
            
                        file.close()
            
            res = monuments()
            res.fetch()
if form.getvalue('shopping'):
    fil = form.getvalue('shopping')
    if destination == 'Delhi':
        class shoppingplaces:
            #def __init():
                
             def fetch(self):
                url = "https://www.tripsavvy.com/top-markets-in-delhi-1539692"
                r = requests.get(url)
                soup = BeautifulSoup(r.text, 'html.parser')
                data =soup.select(".heading-toc")
                #print(data)
                #file = open('shoppingfile7.txt', 'a')
                file = open('shopping-Delhi.txt', 'a')
                for names in data:
                    attr=names.attrs
                    #print(attr['id'])
                    file.write("%s\n" % attr['id'].encode('utf8'))
                file.close()   
        res = shoppingplaces()
        res.fetch()  
    filter.append(fil)

class validate:
    def check(self,slot):
        if slot>12:
            slot = slot - 12
        return slot
val = validate()
file1 = filter[0]+"-"+destination+".txt"
file2 = filter[1]+"-"+destination+".txt"
#print("File1",file1)
#f1 = open(file1,'r')
#f2 = open(file2,'r')
f = open("C:/xampp/htdocs/minor2/yaatri/text1.txt","w+")
l1 = list() #modified everytime
c_for_l1 = 0
c_for_l2 = 0
slot = 10 #for incrementing the slots by 2
l2 = list()
c = 0 #for doing alternatives
store_places = list()
food_joints = list()
#print("Place\tTiming")
flag = 0
if time == 10:
    flag = 1
    time = time - 2
api_key = 'AIzaSyAv-jbvsteT5h6lvU7Kae-8hmPWzDNVuWI'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
with open(file1) as f1:
        if filter[0] == 'monument':
            for line in f1:
                index =line.find("'")
                line = line.rstrip()
                l1.append(line[index+1:len(line)])
        elif filter[0] == 'adventure':
            for line in f1:
                index =line.find("'")
                line = line.rstrip()
                l1.append(line[index+1:len(line)])
        elif filter[0] == 'shopping':
            for line in f1:
                index =line.find("'")
                line = line.rstrip()
                l1.append(line[index+1:len(line)])            
with open(file2) as f2:
            if filter[1] == 'monument':
                for line in f2:
                    index =line.find("'")
                    line = line.rstrip()
                    l2.append(line[index+1:len(line)])
            elif filter[1] == 'adventure':
                for line in f2:
                    index =line.find("'")
                    line = line.rstrip()
                    l2.append(line[index+1:len(line)])
            elif filter[1] == 'shopping':
                for line in f2:
                    index =line.find("'")
                    line = line.rstrip()
                    l2.append(line[index+1:len(line)-1]) 
time = time - 2
c = c+1;
#print("L1",l1)
#print("L2",l2)
store_places.append(random.choice(l1))
query1 = "Restaurants near "+store_places[0] + " "+destination
#print ("Query1",query1)
r = requests.get(url + 'query=' + query1 +
                 '&key=' + api_key)
x = r.json()
y = x['results']
#print("Y.....",y)
if len(y) == 0:
    while len(y) == 0:
        c_for_l1 = c_for_l1 +1;
        store_places[0] = random.choice(l1)
        query1 = "Restaurants in " + store_places[0] + " "+destination
        #print("Query11",query1)
        r = requests.get(url + 'query=' + query1 +
                         '&key=' + api_key)
        x = r.json()
        y = x['results']
        if len(y) != 0:
            #print("Y....",y)
            break
#print(store_places[0]+"\n")
s1 = (str)(val.check(slot))
s2 = (str)(val.check(slot+2))
f.write(store_places[0]+" "+s1+"-"+s2)
slot = slot +2
c_for_l1 = c_for_l1 + 1
y3 = sorted(y, key = itemgetter('user_ratings_total'), reverse = True)
#print("Y3",y3)
for i in range(len(y3)):
    food_joints.append(y3[i]['name'])
store_places.append(food_joints[0])
#print(food_joints[0]+"\n")
#print(store_places[1],val.check(slot),"-",val.check(slot + 2))
s1 = (str)(val.check(slot))
s2 = (str)(val.check(slot+2))
f.write("\n"+store_places[1]+" "+s1+"-"+s2)
slot = slot + 2
time = time - 2
food_joints.clear()
while time>0:
    if c%2 == 0:
        #print("Monument")
        place = random.choice(l1)
        while True:
            if place not in store_places:
                store_places.append(random.choice(l1))
                break
            else:
                place = random.choice(l1)
        s1 = (str)(val.check(slot))
        s2 = (str)(val.check(slot + 2))
        f.write("\n" + store_places[len(store_places)-1]+" "+s1+"-"+s2)
        c_for_l1 = c_for_l1 +1
    else:
        #print("Adventure places")
        place = random.choice(l2)
        while True:
            if place not in store_places:
                store_places.append(random.choice(l2))
                break
            else:
                place = random.choice(l2)
        s1 = (str)(val.check(slot))
        s2 = (str)(val.check(slot + 2))
        f.write("\n" + store_places[len(store_places)-1] +" "+s1+"-"+s2)
        c_for_l2 = c_for_l2 + 1
    time = time - 2
    slot = slot + 2
    c = c+1
if flag == 1:
    query1 = "Restaurants in " + store_places[len(store_places)-1] + " "+ destination
    r = requests.get(url + 'query=' + query1 +
                     '&key=' + api_key)
    #print("Query1",query1)
    x = r.json()
    y = x['results']
    if len(y) == 0:
        while len(y) == 0:
            store_places[len(store_places)-1] = random.choice(l1)
            query1 = "Restaurants in " + store_places[len(store_places)-1] + " "+destination
            #print("Query11",query1)
            r = requests.get(url + 'query=' + query1 +
                             '&key=' + api_key)
            x = r.json()
            y = x['results']
            if len(y) != 0:
                #print("Y....",y)
                break
            
    
    y4 = sorted(y, key=lambda k: k['user_ratings_total'], reverse=True)
    #print("Y4", y4)
    i
    for i in range(len(y4)):
        food_joints.append(y4[i]['name'])
    #print("FoodJoints",food_joints)
    store_places.append(food_joints[0])
    #print(food_joints[0],val.check(slot),"-",val.check(slot + 2))
    s1 = (str)(val.check(slot))
    s2 = (str)(val.check(slot + 2))
    f.write("\n" + store_places[len(store_places) - 1] + " " + s1 + "-" + s2)

redirectURL = "http://localhost/minor2/yaatri/itinerary.php"
print('<html>')
print('  <head>')
print('   <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')