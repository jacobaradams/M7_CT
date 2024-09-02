Room_info = {'CSC101':3004,'CSC102':4501,'CSC103':6755,'NET110':1244,'COM241':1411}
Inst_info = {'CSC101':'Haynes','CSC102':'Alvarado','CSC103':'Rich','NET110':'Burke','COM241':'Lee'}
Time_info = {'CSC101':'8:00 a.m.','CSC102':'9:00 a.m.','CSC103':'10:00 a.m.','NET110':'11:00 a.m.','COM241':'1:00 p.m.'}

your_info = input('What class do you need info for?')
try:
    print(f'You have {your_info} in room {Room_info[your_info]} at {Time_info[your_info]} with Professor {Inst_info[your_info]}.')
except:
    print('Invalid Input. Please type your course ID just as it appears in the course catalog.')