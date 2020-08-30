def insertionSort (lst, criterio:str, orden:str)->list: 
   
  #criterio='vote_count'
  criterio=criterio
      
  if criterio=='vote_count':
    
    size =  len(lst)-1 
    pos1 = 1
    
    for index in range(1,len(lst)):
      currentvalue = int(lst[index][criterio])
      position = index
      original=lst[index]
      #print (currentvalue, " " , index , "  ", position)
      #input ("clic para avanzaar")
      while position>0 and int(lst [position-1][criterio])>int(currentvalue):
          lst [position]=lst [position-1]
          position = position-1
          #print (currentvalue)
      lst[position]=original

   

    if (orden == "less"):
            for i  in range (0,len(lst),1):
                print (lst[i][criterio])
            print ("Se ordeno ascendentemente")
            input ("Se finalizo el proceso...")
    if (orden=="greater"):
            #input ("estoy aqui")
            for i  in range (1,len(lst),1):
              print (lst[len(lst)-i][criterio])
            print ("Se ordeno Descendentemente")
            input ("Se finalizo el proceso...")

  if criterio=='vote_average':
   
    size =  len(lst)-1 
    pos1 = 1
    
    for indexe in range(1,len(lst)):
          #print (lst[indexe][criterio])    
          currentvalue = (lst[indexe][criterio])
          position = indexe
          original=lst[indexe]
          while (position>0 and (lst [position-1][criterio])>(currentvalue)):
              lst [position]=lst [position-1]
              position = position-1
              #print (currentvalue)
          lst[position]=original



    if (orden == "less"):
            for i  in range (0,len(lst),1):
                print (lst[i][criterio])
            print ("Se ordeno ascendentemente")
            input ("Se finalizo el proceso...")
    if (orden=="greater"):
            #input ("estoy aqui")
            for i  in range (1,len(lst),1):
              print (lst[len(lst)-i][criterio])
            print ("Se ordeno Descendentemente")
            input ("Se finalizo el proceso...")

  return lst