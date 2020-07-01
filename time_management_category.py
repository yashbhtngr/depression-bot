from conv_class import *
repeat_filename = "six_categories.py"


time_back_to_six_categories = conv_stations('**repeat**',None,None,None,repeat_filename,False)

time_end_of_conversation = conv_stations('''It was great talking to you! I hope you stay well and healthy 
and If you need me anytime I'm right here. So long, bye!!''',None,None,None,repeat_filename,True)

time_yes_breaks= conv_stations('''That's great! Taking a break can help you feel energized whenever you feel 
tired or restless. And even better, schedule your break times. It helps you to relax and gets back to work with 
energy again later. If you know a break is coming, you’ll likely be able to overcome boredom or a lack of motivation
to push through the task at hand. Take a walk, listen to some music, or do some quick stretches. We have been talking
about time management a lot. But there are several other factors such as health, social skills, or negative thoughts 
that can be stress causers. Would you like to continue and talk about these factors?''',time_back_to_six_categories,
time_end_of_conversation,None,repeat_filename,False)

time_no_breaks = conv_stations('''Taking breaks might be useful. Whenever you find yourself feeling tired and stressed,
take a break for 10 to 15 minutes. Too much stress can take a toll on your body and affect your productivity. And even
better, schedule your break times. It helps you to relax and gets back to work with energy again later. If you know a 
break is coming, you’ll likely be able to overcome boredom or a lack of motivation to push through the task at hand. 
Anyway, we talked a lot on time management and I really found it great! There are other factors as well that can decide 
how your day goes. Factors such as socializing, assertiveness or health issues can make you feel stressed. Would you like 
to continue and discuss about these factors as well?''',time_back_to_six_categories,time_end_of_conversation,None,repeat_filename,False)

time_yes_procrastinate = conv_stations('''Procrastination is one of the things that has a negative effect on productivity.
It can result in wasting essential time and energy. It could be a major problem in both your career and your personal life.
We tend to procrastinate when we feel bored or overwhelmed. Try to schedule in smaller, fun activities throughout the day 
to break up the more difficult tasks. This may help you stay on track. Another tactic to address time management is taking
short regular breaks. Do you take breaks in between work?''',time_yes_breaks,time_no_breaks,None,repeat_filename,False)

time_no_procrastinate = conv_stations('''That's really great! Procrastination is a bad habit and if you do not have it then 
you do not have to undergo the tough process of undoing it. Procrastination is one of the things that has a negative 
effect on productivity. It can result in wasting essential time and energy. Coming back to work strategies, 
do you take breaks in between work?''',time_yes_breaks,time_no_breaks,None,repeat_filename,False)

time_yes_deadlines = conv_stations('''That's nice to hear! Once you set a deadline, it may also be helpful to write it 
on a sticky note and put it near your workspace. This will give you a visual cue to keep you on task. Well, 
if you stick to your deadlines then that's a good habit. Talking about deadlines, another related aspect is 
procrastination. It means postponing or delaying your work unnecessarily. Procrastination is not good but strong 
willpower can help overcome it. I would like to ask you, do you often procrastinate before deadlines?''',time_yes_procrastinate,time_no_procrastinate,
None,repeat_filename,False)

time_yes_early = conv_stations('''That's great! Getting up early is a very good habit.Most successful people have one thing 
in common — they start their day early as it gives them time to sit, think, and plan their day. This can help you meet your 
deadlines without experiencing much stress. Wonderful! Now, going back to deadlines, another habit related to it is 
procrastination. Procrastination means delaying or postponing work which often leads to last minute panics. I would like 
to ask you, do you often procrastinate before deadlines?''',time_yes_procrastinate,time_no_procrastinate,None,repeat_filename,False)

time_not_early = conv_stations('''When you get up early, you are more calm, creative, and clear-headed. As the day progresses, 
your energy levels start going down, which affects your productivity, motivation, and focus. If you’re not a morning person, 
you can just try waking up thirty minutes earlier than your normal time. You’ll be amazed by how much you can get done in that 
bit of time. If you don’t want to use it to work, use it to do a bit of exercise or eat a healthy breakfast. This kind of
routine will also contribute to your productivity during the day. Going back to deadlines, lets talk about procrastination 
about deadlines. Procrastination means delaying or postponing work which often causes last minute panics. Do you often 
procrastinate before deadlines?''',time_yes_procrastinate,time_no_procrastinate,None,repeat_filename,False)

time_no_deadlines = conv_stations('''When you have a task at hand, set a realistic deadline and stick to it. Once you set a deadline, 
it may be helpful to write it on a sticky note and put it near your workspace. This will give you a visual cue to keep you on task. 
Try to set a deadline a few days before the task is due so that you can complete all those tasks that may get in the way. You can 
reward yourself when you meet a difficult deadline. Also I would like to ask you, do you try to get up early in the morning?'''
,time_yes_early,time_not_early,None,repeat_filename,False)

time_yes_schedule= conv_stations('''That's great! Creating schedules helps one to complete work on time. You can also create a 
list of items and check them off  as you complete them. This will give you a sense of accomplishment and keep you motivated. 
Moving on, lets talk about deadlines, the ones you set. Deadlines are sort of time limits for a particular task. So, do you 
stick to the deadlines you set?''',time_yes_deadlines,time_no_deadlines,None,repeat_filename,False)

time_no_schedule = conv_stations('''Scheduling tasks can be helpful. I suggest you give it a try. Carry a planner or notebook 
with you and list all the tasks that come to your mind. Being able to check off items as you complete them will give you a 
sense of accomplishment and keep you motivated. Anyway lets move on. Lets talk about deadlines, the ones which we set 
ourselves for a particular task. So do you stick to the deadlines that you set?''',time_yes_deadlines,time_no_deadlines,None,repeat_filename,False)

time_yes_prioritize = conv_stations('''Excellent! Prioritizing helps you stay on time by completing the most important tasks 
first and then going for the less important ones. Along with prioritizing, scheduling can be a powerful time management 
skill. It involves listing all tasks that come to your mind or that you have to complete within a time period. Do you 
create schedules or time tables to work with?''',time_yes_schedule,time_no_schedule,None,repeat_filename,False)

time_no_prioritize = conv_stations('''Unimportant tasks can consume much of your precious time, and we tend to offer these 
too much of our energy because they are easier or less stressful.However, identifying urgent tasks that need to be completed 
on that day is critical to your productivity. Once you know where to put your energy, you will start to get things done in 
an order that works for you and your schedule. It helps you stay focused. Another important skill is scheduling which involves 
making a list of all that you have to do in a given time period. Do you make schedules or use time tables?''',
time_yes_schedule,time_no_schedule,None,repeat_filename,False)

time_overwhelmed_yes = conv_stations('''Feeling overwhelmed by your work can be the result of not delegating tasks.
Try to find which tasks are necessary and you can handle within the time limit. 
Delegating as I mentioned before doesn't mean running away from responsibilities 
but managing them so that you can give a better quality of work. Another useful 
time management skill is prioritizing. It means scheduling more important tasks 
ahead of other less important ones which helps you be on time. Let me ask you here,
do you prioritize your tasks?''',time_yes_prioritize,time_no_prioritize,None,repeat_filename,False)


time_overwhelmed_no = conv_stations('''That's great! This means that you manage your tasks well and truly recognize your capabilities. 
Being overwhelmed by work can also make a person lose interest in that work. So if you still feel
at any point that you have too much work on your hands, then maybe its time to delegate well.
Another important aspect of time management is prioritizing tasks. It means giving priority 
to most important tasks and doing them ahead of less important ones. Do you  prioritize your tasks ?''',
time_yes_prioritize,time_no_prioritize,None,repeat_filename,False)

time_no_delegation = conv_stations('''Delegating tasks becomes important when your workload starts to increase. 
Delegation does not mean you are running away from your responsibilities 
but are instead learning proper management of your tasks. Taking on more 
tasks than you can handle can often result in stress and burnout. Another
question to you in this regard, have you ever felt overwhelmed by your workload?''',time_overwhelmed_yes,time_overwhelmed_no,None,repeat_filename,False)

time_yes_delegation = conv_stations('''Great! Delegating tasks helps you stay stress free and actually makes you 
perform better. As you are concentrating on fewer tasks your quality of 
work improves. That's great! Another important aspect of time management
is prioritizing. It means giving higher priority to more important tasks, 
so you do them ahead of other less important ones. Speaking of which, do 
you prioritize your tasks?''',time_yes_prioritize,time_no_prioritize,None,repeat_filename,False)

time_management_yes = conv_stations('''Alright, great! Time management is one of the most important 
aspects of ones life. Time lost can never be regained and to use 
it properly and creatively is something that one definitely needs 
to be consistent at. We'll talk about scheduling important tasks, 
setting deadlines etc. So lets get started. Lets first see what delegating 
tasks means. It means to take on only as many tasks as you can handle. 
We often take on more tasks than we can handle and it creates stress and 
burnout. A question for you: do you delegate your tasks well?''', time_yes_delegation,time_no_delegation,None,repeat_filename,False)

time_management_yes.start_conv()