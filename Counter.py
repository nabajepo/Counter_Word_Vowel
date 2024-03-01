def chooseWhatToDo():
    print("############################################")
    choose=0
    while(choose!=1 or choose!=2):
          choose=int(input("Choose: 1)Count vowel 2)Count word :"))
          if(choose==1):
              print("We have to count vowel in a paragraph")
              break
          if(choose==2):
              print("We have to count word in paragraph")
              break
    return choose
def CountWord():
     print("############################################")
     wordinsert=input("Insert your paragraph or word :")
     allWord=[] 
     index=0
     aWord=""
     
     while(index<len(wordinsert)):
          if((wordinsert[index]==" ")or(index==len(wordinsert)-1)):
            if(index==len(wordinsert)-1):
                aWord=aWord+wordinsert[index]
            allWord.append(aWord)
            aWord="" 
          else:
              aWord=aWord+wordinsert[index]
          index=index+1
     print("This program counted  :",len(allWord),"words")
    
def CountVowel():
    print("############################################")
    a=0
    i=0
    u=0
    o=0
    e=0
    wordinsert=input("Insert your paragraph or word  :").lower()
    index=0
    while(index<len(wordinsert)):
        if(wordinsert[index]=="a"):a=a+1
        if(wordinsert[index]=="i"):i=i+1
        if(wordinsert[index]=="u"):u=u+1
        if(wordinsert[index]=="o"):o=o+1
        if(wordinsert[index]=="e"):e=e+1
        index=index+1
    print("For vowel a we found :",int(a))  
    print("For vowel i we found :",int(i))  
    print("For vowel u we found :",int(u))  
    print("For vowel o we found :",int(o))  
    print("For vowel e we found :",int(e))
    number=int(a+i+u+o+e)
    print("This program counted in all :",number,"vowels")
    print("############################################")
def action_and_agree():
    if(chooseWhatToDo()==1):CountVowel()
    else:CountWord()
    choose=0
    while(choose!=1 or choose!=2):
          choose=int(input("Would you like to continue : 1)Yes  2)No :"))
          if(choose==1):
              action_and_agree()
              break
          if(choose==2):
              print("Thank you")
              break
    print("############################################")      
action_and_agree()

    