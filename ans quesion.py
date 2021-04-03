print('hi wellcom to my game i made my self if you are firind you can do this with ut any problom if you are ready write yes ')

ans = input('are you ready to play(yes/no):')
score = 0
total_q = 17

if ans.lower() == 'yes':
    ans = input('1.what is the best programing language?')
    if ans.lower() == 'c++':
        score += 1
        print('correct')
    else:
        print('incorrect')


    ans = input('2.who i like the most in my family(no one/my pet/brother/mother/father):?')
    if ans.lower() == 'no one':
        score += 1
        print('correct')
    else:
        print('incorrect')



    ans = input('3.who is the most intellgent boy in my family (m.d reza/ali):?')
    if ans.lower() == 'm.d reza':
        score += 1
        print('correct')
    else:
        print('incorrect')




    ans = input('4.what is = 50-5-9+45-5*9*105?')
    if ans == '4644':
        score += 1
        print('correct')
    else:
        print('incorrect')



    ans = input('5.who is my worls greatest friend even better than my brother(Shankcrew/anable/brother/High_sky/mohammaddula):?')
    if ans.lower() == 'god':
        score += 1
        print('correct')
    else:
        print('incorrect')


    ans = input('6.who is the right hand man of luffy the boy how is going to become the piretking?')
    if ans.lower() == 'zoro':
        score += 1
        print('correct')
    else:
        print('incorrect')



    ans = input('7:what devil fruit does luffy have(Dragon/gum gum/ope ope/human/bari bari):?')
    if ans.lower() == 'gum gum':
        score += 1
        print('correct')
    else:
        print('incorrect')


    ans = input('8.which friend i liked and i gave her my dimond to make dimond aromre and sword for her and after 30 min playing she betryed me and cancled our frindship(anabla/shankcrew/high_sky/bunnygirle):?')
    if ans.lower() == 'anabla':
        score += 1
        print('correct')
    else:
        print('incorrect')



    ans = input('9.do i like to die right now (yes/no):?')
    if ans.lower() == 'no':
        score += 1
        print('correct')
    else:
        print('incorrect')


    ans = input('10.who is the best in the world(mother/father/no one):?')
    if ans.lower() == 'no one':
        score += 1
        print('correct')
    else:
       print('incorrect')
       
    ans = input('11.who was the fire nation creater youtuber how has create the fire nation group in roblox,mincraft,fortnite,carbordcraft,world of no man?')
    if ans.lower() == 'prestenplays':
        score += 1
        print('correct')
    else:
       print('incorrect')

    ans = input('11.how is the best youtuber from my eye site (pretenplays/mr.beast/rageelixer/jelly/timtom/braine)?')
    if ans.lower() == 'rageelixer':
        score += 1
        print('correct')
    else:
       print('incorrect')   
   
    ans = input('12.whon is the strongest hero in one punch man (stamina/blast/gouru/king/gunhero/samorie)?')
    if ans.lower() == 'stamina':
        score += 1
        print('correct')
    else:
       print('incorrect')

    ans = input('13.who many elment are there (ten/four/five/three/two/nine):?')
    if ans.lower() == 'four':
        score += 1
        print('correct')
    else:
       print('incorrect')
       
    ans = input('14.who is komoru (one tailed beast/ two tailed beast/three tailed beast/four tailed beast/five tailed beast/six tailed beast/seven tailed beast/egiht tailed beast/nine tailed beast/ten tailed beast):?')
    if ans.lower() == 'nine tailed beast':
        score += 1
        print('correct')
    else:
       print('incorrect')
       
    ans = input('15.who has the nine tailed beast in him seled(sakora/narouto/saskue/kasie/braouto/hinata/):?')
    if ans.lower() == 'narouto':
        score += 1
        print('correct')
    else:
       print('incorrect')

mark = (score/total_q) * 100

print("mark: ", mark)
print('good bye :( :)')






     
