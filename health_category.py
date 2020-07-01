from conv_class import *
repeat_filename = "six_categories.py"

hc_back_to_six_categories = conv_stations('**repeat**',None,None,None,repeat_filename,False)

hc_end_of_conversation = conv_stations('''It was great hearing from you! I wish you lots of happiness and contentment. 
If you need my help I'll be right here. later, Bye!!''',None,None,None,repeat_filename,True)

hc_good_mental_state = conv_stations('''That's great. Staying happy and content not only keeps your mind healthy but also 
affects your body. Its nice to see you in good state of affairs. Well, it seems like things here are fine. We can talk 
about factors other than health that are important in deciding daily state of affairs. Would you like to continue?'''
,hc_back_to_six_categories,hc_end_of_conversation,None,repeat_filename,False)

hc_stress_syndrome_yes = conv_stations('''It will be a good step if you consult a good counselor or psychiatrist who can help 
you deal with this. Taking help from others to move forward makes your life wholesome. I definitely know this that you have 
the inner strength and determination that can help you move ahead in life. There can be other factors, apart from health, 
which can cause stress too. Do you want to talk about them?''',hc_back_to_six_categories,hc_end_of_conversation,None,repeat_filename,False)

hc_stress_syndrome_no = conv_stations('''Great! Sometimes things can go wrong but it is up to us , how we perceive those events 
and stand back up to move forward in our lives. Ultimately what you do will make a difference to your life and if you plan it 
right then you'll be mellow once again. Anyway, there are several other aspects apart from health that we can discuss which can 
be important in deciding stress levels. Would you like to continue with them?''',hc_back_to_six_categories,hc_end_of_conversation,None,repeat_filename,False)

hc_bad_mental_state = conv_stations('''Please don't worry. It happens sometimes that we feel unhappy about ourselves or the people 
around us. But it is important to remember that we must still love ourselves and try to motivate ourselves. What you do to bounce 
back when you hit the bottom, is what makes you a great person. So please don't be hard on yourself. Talking about negative emotions, 
do you think that you have any kind of a stress syndrome?''',hc_stress_syndrome_yes,hc_stress_syndrome_no,None,repeat_filename,False)

hc_regular_exercise_custom = conv_stations('''Its very important to keep exercising regularly. Even for short periods of time, 
if we do some free hand exercises or a few pushups, sit ups it can help us a lot. Exercise helps keep the brain healthy and the 
body fit while ensuring that the blood flow to different parts of the body is adequate. It also helps relieve stress, there you go! 
Its always good to remember that its never too late to start. We all have our unique situations to deal with, but some time for 
yourself can really make the difference. You'll feel good about yourself. Talking about feeling good, its also important to 
maintain mental health. So on an average how do you feel about yourself? What kind of a mental state are you in?''',
hc_good_mental_state,hc_bad_mental_state,None,repeat_filename,False)

hc_good_diet = conv_stations('''That's great. Maintaining a good diet can take you far. You are doing great! I think your 
awareness towards your health can help you battle some tough situations. Alright lets move on to exercises. What do you 
think about exercises? Do you exercise regularly?''',None,None,hc_regular_exercise_custom,repeat_filename,False)

hc_bad_diet = conv_stations('''you should have a good diet. It helps a lot by providing the right amounts of all nutrients 
to your body. A healthy diet helps keep you away from heart problems, hypertension and diabetes which are basically lifestyle 
diseases. Love yourself! Anyway what do you think about exercises? exercises can help a lot in keeping you fit. 
Do you exercise regularly?''',None,None,hc_regular_exercise_custom,repeat_filename,False)

hc_diet_water = conv_stations('''A balanced diet provides us with all the nutrients that are necessary for our body to maintain itself. 
It is important to have adequate amounts of proteins and carbs. Drinking adequate amounts of water is extremely important as our body is 
basically 70 % water. So are you successful in maintaining your diet? Do you satisfactorily maintain these aspects?''',
hc_good_diet,hc_bad_diet,None,repeat_filename,False)

hc_sleep_benefits = conv_stations('''There are quite a few and important benefits of good sleep. It lets your damaged cells heal themselves
, it lets the brain take a rest from all the thinking and it lets the body regain enough energy for another hectic day. Sleeps reduces heart
problems, reduces stress, reduces inflammation and improves memory just to name a few. I hope you get good sleep and give your body and mind
enough rest. Lets move on. Coming on to diet and water, what are your thoughts on these two aspects of health?''',
None,None,hc_diet_water,repeat_filename,False)

hc_enough_sleep_yes = conv_stations('''That's good. Depending on your personal needs you can always get more sleep if you feel it necessary. 
There are several benefits of getting enough sleep. What do you think they are?''',None,None,hc_sleep_benefits,repeat_filename,False)

hc_enough_sleep_no = conv_stations('''Well, to be frank that may be one of the biggest reasons behind undue stress. 
Sleep is absolutely necessary for your body to heal so that it has enough energy for the next day. I believe that at 
least 7 hours of sleep is essential. What other benefits of sleep can you think of?''',None,None,hc_sleep_benefits,repeat_filename,False)

health_thoughts_on_exercise_sleep_diet = conv_stations('''Lack of sleep can cause one to become lethargic and disinterested in daily affairs. 
Its very important that we have good sleep and good food to ensure that our body gets all the rest and the nutrients that it needs so that 
we can go about our daily work without interruption. Lets start with sleep. On an average a person needs to get 7 hours of sleep to feel fully rested. 
Do you get 7 or more hours of sleep on an average?''',hc_enough_sleep_yes,hc_enough_sleep_no,None,repeat_filename,False)

hc_no_other_factors_to_six_categories = conv_stations('''Alright, there can be other factors , apart from health which can be causes behind 
increased stress levels. Examples include socializing, time management skills etc. Would you like to talk about these aspects ?''',
hc_back_to_six_categories,hc_end_of_conversation,None,repeat_filename,False)

hc_no_other_factors_to_other_factors = conv_stations('''Well there are many other factors that can be important in deciding how you feel 
during the day. Good sleep, exercise and a balanced diet are very important for a healthy life. What are your thoughts about exercise, 
diet and sleep?''',None,None,health_thoughts_on_exercise_sleep_diet,repeat_filename,False)

hc_no_other_factors = conv_stations('''I would like you to discuss with your colleagues if you have any lingering doubts about 
professional hazards. Would you like to continue with some more health topics?''',hc_no_other_factors_to_other_factors,
hc_no_other_factors_to_six_categories,None,repeat_filename,False)

hc_other_factors_also = conv_stations('''Well then, lets start talking about other health factors such as sleep, exercise and 
food habits. Its very important that we lead a healthy lifestyle which includes regular exercise and a balanced diet, 
in order to be productive and enjoy all facets of life. What are your thoughts on factors such as sleep, diet and exercise?'''
,None,None,health_thoughts_on_exercise_sleep_diet,repeat_filename,False)

hc_adhere_yes_custom = conv_stations('''Its very important to follow proper protocol. It is one of the easiest things to do that 
keeps you out of danger. Do you believe that health factors apart from physical hazards are also behind your increased stress levels?''',
hc_other_factors_also,hc_no_other_factors,None,repeat_filename,False)

hc_adhere_no_custom = conv_stations('''There are several ways one can avoid unnecessary hazard at the workplace.Always wear proper 
safety equipment and follow the safety guidelines. It also pays to identify the places or situations that can be hazardous and thus 
you can be mentally and physically prepared before falling in such situations. This is an extremely important issue and I hope you 
won't let your body and mind suffer from its harmful effects. Moving on, What do you think about following proper protocol? what are 
you're thoughts on following proper protocol?''',None,None,hc_adhere_yes_custom,repeat_filename,False)

hc_adhere_yes = conv_stations('''Well that's great. Using proper equipment is also very important. Many accidents also happen due 
to shortcuts that employees take. What are your thoughts on following proper protocol?''',None,None,hc_adhere_yes_custom,repeat_filename,False)

hc_adhere_no = conv_stations('''Its very important that you follow proper guidelines and adhere to these rules strictly. Many a times, 
it happens that employees need to work in situations that are hazardous but there are proper instructions or practices that if followed 
can minimize the harmful effects of work to a great extent. You can always start by going through the guidelines or by requesting those 
in charge to organize a workshop that is appropriate for this. Can you think of some tips that can help you stay safe while in the workplace?''',
None,None,hc_adhere_no_custom,repeat_filename,False)

hc_hazards_yes = conv_stations('''Physical hazards at workplace can be a cause of your deteriorating health. 
It is very important that you have a full understanding of the safety regulations in place. Do you believe that 
you adhere to these practices strictly?''',hc_adhere_yes,hc_adhere_no,None,repeat_filename,False)

hc_no_hazards = conv_stations('''Well there are many other health factors that can play a major role in deciding how you 
feel throughout the day. Good sleep, regular exercise and a balanced diet are extremely important for you to lead a healthy 
and happy life. What are your thoughts on factors like good sleep, exercise and diet?''', None,None,health_thoughts_on_exercise_sleep_diet,
repeat_filename,False)

hc_yes = conv_stations('''Alright then lets start talking about health issues. Health is one of the most important factors 
in deciding how you feel at the workplace. Do you believe that you face physically hazardous situations at your workplace?''',
hc_hazards_yes,hc_no_hazards,None,repeat_filename,False)

hc_yes.start_conv()