# -*- coding: utf-8 -*-
"""agungor_the4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T9IaVzhzfU2aFVrNpvpN0EQFI9chNt02
"""

mainfile=open('all_ratings.txt', 'r')

genrenamedc={} #is a dictionary that has genres as keys and movies as values as a list for ex {'comedy': ['true lies', 'man in black']}
nameratedc={} #is a dictionary that has movie names as keys and every single rating as values (still str) as a list for ex {'terminator':['3.0', '4.5']}
namefinalratedc={} #is a dictionary that has movie names as keys and final average rating as the value as a single float for ex {'terminator':3.354654}

for line in mainfile:
  line = line.strip()
  linelist=line.split('\t')
  rating=linelist[1]
  name=linelist[2]

  if name not in nameratedc:
    nameratedc[name]=[rating]
  else:
    nameratedc[name]+=[rating]

  manygenres=linelist[3]
  manygenres=manygenres.lower()

  splitmanygenres=manygenres.split('|')
  
  for x in splitmanygenres:
      if x not in genrenamedc:
        genrenamedc[x]=[name]

      else:
        genrenamedc[x]+=[name]


  
inputgenre=input('Enter a genre: ')
inputgenre=inputgenre.lower()
genrevaluelist=genrenamedc[inputgenre] #a list that has movie names in that genre

for m in genrevaluelist:
  ratinglist=nameratedc[m]
  ratingtotal=0
  for n in range(len(ratinglist)):
    ratingtotal+=float(ratinglist[n])
  finalrating=ratingtotal/(len(ratinglist))
  namefinalratedc[m]=finalrating

maxrating=max(namefinalratedc.values())

for m,r in namefinalratedc.items():
  if r==maxrating:
    maxratedmovie=m

rightchecker='wrong'
actionchecker='no'

while len(namefinalratedc)!=0:
  actionchecker=input('Would you like to watch ' + maxratedmovie + ' with rating ' + format(maxrating, '.4f') + ': ')
  actionchecker=actionchecker.lower()

  if actionchecker=='yes':
    print('Enjoy the movie!')
    break

  elif actionchecker=='no':
    namefinalratedc.pop(maxratedmovie)
    if len(namefinalratedc)!=0: 
      maxrating=max(namefinalratedc.values())
      for m,r in namefinalratedc.items():
        if r==maxrating:
          maxratedmovie=m
          break
    else:
      break

  else:
    while rightchecker!='yes' and rightchecker!='no':
      rightchecker=input('You entered an incorrect input, please enter yes or no: ')
      rightchecker=rightchecker.lower()
    actionchecker=rightchecker
    if actionchecker=='yes':
      print('Enjoy the movie!')
      break
    elif actionchecker=='no':
      namefinalratedc.pop(maxratedmovie)
      if len(namefinalratedc)!=0:
        maxrating=max(namefinalratedc.values())
        for m,r in namefinalratedc.items():
          if r==maxrating:
           maxratedmovie=m
           break
      rightchecker='wrong'
    
  

if len(namefinalratedc)==0:
  print('No movies left in this genre!')

  
#Ahmet Alperen Gungor 28847
#i learned a lot, had 0 python knowledge yet managed to get 100 from all take homes on my own(hope to get 100 from this one as well), thanks for the great semester ( in terms of if100 :) )


mainfile.close()