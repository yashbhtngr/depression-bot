from conv_class import *
repeat_filename = "six_categories.py"

ac_back_to_six_categories = conv_stations('**repeat**',None,None,None,repeat_filename,False)

ac_end_of_conversation = conv_stations('''Alright, it was great talking to you. I hope you have received 
some help even if very little from me in tackling your problems. I'll be here anytime you need me. 
See you later, bye!!''',None,None,None,repeat_filename,True)

ac_cannot_refuse = conv_stations('''Its not wrong to refuse someone's request, especially if its inconvenient 
for you. If you try to satisfy everyone it will only create more workload for you some of which will be 
completely unnecessary. Refusing someone does not mean you are being rude. Its your right, and you can exercise 
it appropriately. Well, that was a good discussion on assertiveness. I hope you got some insight. But many 
other factors can also be responsible for stress or sadness, other than not being able to assert oneself. 
Would you like to continue and discuss about those aspects?''',ac_back_to_six_categories,ac_end_of_conversation,None,repeat_filename,False)

ac_can_refuse = conv_stations('''Good! Its not rude to refuse people and this becomes important especially if 
the request is inconvenient for you. Helping other people by doing what they request you to is definitely noble 
but one also needs to say "no" when necessary, otherwise it can build up stress. Speaking of which, there are many 
other factors which can be responsible for increased stress levels. Would you like to continue discussing about 
factors other than assertiveness that can cause tension?''',ac_back_to_six_categories,ac_end_of_conversation,None,repeat_filename,False)

ac_is_acquainted_rights = conv_stations('''That's great! Knowing your rights can help you be more confident and put 
forward your opinions. Many a times it so happens that people tend to not voice their thoughts owing to fear that 
they will be fired or they will be reprimanded. However organizations can't do anything they want, and if you know 
your rights then be assertive without any fear. Another question, do you have problems refusing someone's request 
(a request which may be  inconvenient for you)?''',ac_cannot_refuse,ac_can_refuse,None,repeat_filename,False)

ac_not_acquainted_rights= conv_stations('''Knowing your rights is very important. If you have any doubts as to what 
are your rights and their jurisdictions, then I suggest you have a proper discussion with someone in charge of this 
(like the HR department) who will be able to guide you. Often people hesitate to assert themselves out of fear of being 
reprimanded or punished, but that is not always correct. Knowing one's rights make a person more confident and outspoken. 
Alright let me ask you this, do you have difficulties refusing someone's request even if it is inconvenient for you?''',
ac_cannot_refuse,ac_can_refuse,None,repeat_filename,False)

ac_is_aggressive_again = conv_stations('''Alright, this time its not an aggressive statement. This was an assertive 
statement where you refuse someone's request because of genuine reasons and convey that meaning in a polite manner. 
At the other end a colleague of yours won't be offended if you say something like this. This is one way how you would 
manage your work so there's nothing wrong in saying this. Anyway lets move on to another area of assertiveness. Do you 
believe that you are acquainted well enough with your rights at your organization?''',ac_is_acquainted_rights,ac_not_acquainted_rights,
None,repeat_filename,False)

ac_not_aggressive_again = conv_stations('''That's right! Its not an aggressive but an assertive sentence. By refusing 
someone's request politely, one is being assertive and not aggressive. Thus its important that we distinguish between 
aggressive and assertive sentences. Anyway, lets move on to another aspect. Do you believe that you are well acquainted 
with your rights at your organization?''', ac_is_acquainted_rights, ac_not_acquainted_rights,None,repeat_filename,False)

ac_is_aggressive = conv_stations('''That's the right answer! Great, so you were able to recognize an aggressive statement. 
Its important that you do, so that when you put forward your opinion it does not offend other people who are listening to you. 
Another one: Is this statement ” It may be important for you but I am working on a top priority task just now. Can we talk about this after 5.00 p.m.?” 
aggressive?''',ac_is_aggressive_again,ac_not_aggressive_again,None,repeat_filename,False)

ac_not_aggressive = conv_stations('''Well, its an aggressive statement. Statements such as these tend to hurt the other person's 
feelings invariably. As an exercise, you can think of someone saying that to you and then think how would you feel. Statements 
like these try to erode the working environment at your workplace. Lets try another one: Is this statement ” It may be important 
for you but I am working on a top priority task just now. Can we talk about this after 5.00 p.m.?” an aggressive statement?''',
ac_is_aggressive_again,ac_not_aggressive_again,None,repeat_filename,False)

ac_can_distinguish = conv_stations('''Excellent! A major step forward is recognizing that being assertive is not being aggressive 
and being unassertive is not being polite. Aggressive statements hurt others but assertive statements make a point without disrespecting 
others' opinions. A fun question for you: is this statement "That's not my job. I report to the manager and that's it, please stay in 
your lane." aggressive?''',ac_is_aggressive,ac_not_aggressive,None,repeat_filename,False)

ac_cannot_distinguish = conv_stations('''Aggressive statements are those which try to impose one's opinion without any respect for 
the other person's beliefs. Assertive statements clearly state your thoughts and views without hurting other people whereas being 
unassertive means you do not voice your opinions or stand up to your beliefs and let others take the decision. Being Unassertive is 
often confused with being polite, though they are completely different. A fun question for you: Is this sentence "Its not my job. I 
report to the manager, that's it. Please stay in your lane." aggressive?''',ac_is_aggressive,ac_not_aggressive,None,repeat_filename,False)

ac_custom_open_up = conv_stations('''Things may be difficult for some time but not always. You will feel better if you think of 
what your role models would have done in your situation and can gain motivation from that. Making friends is a fun process, I agree
it may be difficult sometimes but slowly and steadily you can definitely make changes. So, good luck!!Now, lets move onto another 
aspect that is education. By education I mean the ability to distinguish between aggressive, assertive and unassertive statements. 
Can you distinguish between these three categories well enough?''',ac_can_distinguish,ac_cannot_distinguish,None,repeat_filename,False)

ac_has_friends = conv_stations('''That's great! Having someone to share your thoughts with can help you feel lighthearted and free. 
Its very important and part of human nature. Socializing at workplace is very important. Now, lets move onto another aspect that is education. 
By education I mean the ability to distinguish between aggressive, assertive and unassertive statements. 
Can you distinguish between these three categories well enough?''',ac_can_distinguish,ac_cannot_distinguish,None,repeat_filename,False)

ac_can_talk_in_meetings = conv_stations('''That's great! Asserting your opinions makes others feel that you matter. But most importantly 
it helps you voice your thoughts and do justice to yourself. You are a genuine person and seriously contribute to the cause which is an 
excellent quality. Now, lets move onto another aspect that is education. By education I mean the ability to distinguish between aggressive, 
assertive and unassertive statements. Can you distinguish between these three categories well enough?''',
ac_can_distinguish,ac_cannot_distinguish,None,repeat_filename,False)

ac_no_friends = conv_stations('''Try to make friends. Humans are a social species and we tend to rely on each other in times of trouble 
or to share our thoughts and feelings. Having someone with whom you can share your thoughts can make you feel light and content. 
For a start, if you consider me a friend, even if we have meet for a short period of time, you can open up to me. Speak out
what's in your mind and let me know.''',None,None,ac_custom_open_up,repeat_filename,False)

ac_cant_talk_in_meetings = conv_stations('''Being able to assert yourself is important. If you have been included in a meeting, it just means
your colleagues think that your opinion matters and therefore you should be voicing your mind without fear. Hesitation and social awkwardness
may hinder you, but just remember that nothing's big going to happen, you are just discussing with your colleagues about some issue.It also 
helps build up your profile and people start to recognize your efforts. Speaking of which, do you have friends or colleagues with whom 
you share your thoughts freely?''',ac_has_friends,ac_no_friends,None,repeat_filename,False)

assertiveness_category_yes = conv_stations('''Alright great! Lets start discussing about assertiveness. Assertiveness refers 
to standing by one's opinions and views firmly while also respecting others' opinions. Let me start by 
asking you about your participation in meetings. During meetings (if any) are you able to voice 
your opinions freely, without hesitation?''',ac_can_talk_in_meetings,ac_cant_talk_in_meetings,None,repeat_filename,False)

assertiveness_category_yes.start_conv()

