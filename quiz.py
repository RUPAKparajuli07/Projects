def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)
    
print("Hello! Welcome to my Quiz" "\n" "All Questions carries 10 marks each")
ans = input("Are you ready to play (yes/no): ")
a ="Note: wrtie answers! do not write option."
score = 0
total_questions = 4


correct_ans =["a", "c", "b", "c"]



if ans.lower() == "yes":
   
    print(a)    
    print("Question- What is the best Programming Language? ")
    give_options("Python", "C", "Java" )
    ans=input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
        
        
        
    print(a)
    print("Question- Who is the Founder of Apple Inc? ")
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
    ans = input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
        
        
        
        
    print(a)
    print("Question- What is more better among these? ")
    give_options("Data Science", "Artificial Intelligence", "Digital Marketing")
    ans = input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
        
        
        
        
    print(a)
    print("Question- What is the best Investment? ")
    give_options("Share Capital", "Mutual Funds", "Bitcoin")
    ans = input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
        
        
        
        

i = score*10

if i > 30 :
    print (i,"/40  ohh my god you made it!!! you are genious")
    
elif i == 30:
    print (i,"/40  you are quit smart")
    
elif i == 20:
    print (i,"/40  you need some practice ")    
    
elif i == 10:
    print (i,"/40  you need huge practice ")
         
else:
    print(i,"/40  you loose", "better luck next time ")   

print ("your score is", i)

    
