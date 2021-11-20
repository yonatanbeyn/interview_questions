
nested_lst=[[12,3],[4,5,6],[1,3]]
def sum_of_nested_list(list):   # sum of nested list
  summ=0
  for a in l:
    for i in a:
      summ+=i
  print(summ)    
sum_of_nested_list(nested_lst)

########################################################
def to_one(list_):
  """nested list to one list """
  l=[]
  for a in list_:
    for i in a:
      l.append(i)
  print(l)    
to_one(nested_lst)
def max_number(list_):
  """return  the max of a number from the nested list"""
  maxx=0
  for i in list_:
    for a in i:
      if a>maxx:
        maxx=a
  print(maxx)

max_number(nested_lst) 
##########################################
strings=input(' write the string to count ')
########################################################################################
def count(stri):
  """string to world list and count"""
  dic={}
  word_list=stri.split() 
  for word in word_list:
    if word not in dic:
      dic[word]=1
    else:
      dic[word]+=1  
  print(dic)      
count(strings)
#####################################################################
def first_occur(s):
  ""  first reccurring character"""
  dic={}
  l=[]
  for word in s:
    if word not in dic:
      dic[word]=1
    else:
      l.append(word)
  print(l[0])

first_occur('hellowworld').  #expects 'l'
###################################################################
def dot_m(x,y):#dot product
  import numpy as np
  print(np.dot(x,y))
x=[1,2,3]  
y=[4,5,6]
dot_m(x,y)
###################################################################
def maxi():
  """ maximum   score from  dictionary"""
  from collections import Counter
  count= Counter('arsenal')
  max=0
  name = ''
  print(count)
  for i in count:
    if count[i] >max:
      max=count[i]
      name = i
      #print(i)
  print(f"the max is {name} with the value of {max} ")
  #print(f"{max} is the maximum  ")
maxi()

###################################################

a = [["Bob","87"], ["Mike", "55"], ["Jason","35"], ["ashley", "155"], ["Jessica", "99"]]
#######################################################################
def to_dict():
    """nested list to dictionary"""
    dictc={}
    for key in a:
        dictc[key[0]]=key[1]
    print(dictc)   
        
to_dict()
#####################################

