from conv_class import *



six_categories = conv_stations('**repeat**',None,None,None,'six_categories.py',False)
positive_custom = conv_stations('''That is great to hear! Ping me if you need any help though''' ,None,None,None,None,True)
negative_custom = conv_stations('''I understand how that can feel… The first step in moving forward from something that makes us 
feel stuck, is to understand why are we thinking this wayLet’s figure this out by a simple exercise I will ask a few questions, 
and based on your response, we will figure out what is the source of your troubles.You just have to say yes or no''' ,None,None,six_categories,None,False)
positive_response = conv_stations('''Wishing you lots of contentment and satisfaction. What made you feel recharged?''',None,None,positive_custom,None,False)
negative_response = conv_stations('''Gosh, that is tough. I am sorry to hear it But please dont worry. It is natural to feel 
stressed when you undergo such feelings. What has got you feeling like this? What is the reason behind your stress according
 to you?''',None,None,negative_custom,None,False)
welcome = conv_stations('''It is nice to see you! How’s your day going so far?''',positive_response,negative_response,None,None,False)

welcome.start_conv()