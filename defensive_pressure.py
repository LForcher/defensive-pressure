import pandas as pd
import numpy as np
from datetime import datetime
import math
import matplotlib.pyplot as plt

#%%Load event and position data

event_data =  pd.read_csv ('/Users/leander/Desktop/Dissertation/DFL Daten/DFL Daten/EventData_1.Buli_Season19-20_Game9.csv')
position_data = pd.read_csv ('/Users/leander/Desktop/Dissertation/DFL Daten/DFL Daten/PositionData_1.Buli_Season19-20_Game9.csv')

#%% Alignemnt of position and event data coordinates
# event data coordinates with (0|0) beeing the left bottom corner of the pitch / pitch (105m * 68m)
# position data coordinates with (0,0) beeing the middle of the pitch / pitch (105m * 68m)
# Convert position data --> so that (0|0) is the left bottom corner of the pitch

New_x = []
New_y = []
Timestamp1 = []
Timestamp_sec = []
for row, frame in position_data.iterrows ():
    new_x = (frame['X']) + 52.5
    new_y = (frame['Y']) + 34
    
    New_x.append (new_x)
    New_y.append (new_y)

    timestamp1 = pd.to_datetime (frame['T'])
    Timestamp1.append (timestamp1)
    
    timestamp_sec = (((timestamp1.hour)*60)*60) + ((timestamp1.minute)*60) + (timestamp1.second) + ((timestamp1.microsecond)/1000000)
    Timestamp_sec.append (timestamp_sec)

position_data['X'] = New_x
position_data['Y'] = New_y
position_data['T'] = Timestamp1
position_data['T_sec'] = Timestamp_sec


#%% Identifictaion of Attacks
#find all consecutive events of one team & create a data frame with possessions
#delete all unnecessary rows of possession

team_list = list (event_data.Team.unique ())
team_list = [x for x in team_list if str(x) != 'nan']
team1 = team_list[0]
team2 = team_list[1]

#%%
#Convert Timestamp into pandas Timestamp
Timestamp = []
for row,event in event_data.iterrows ():
    timestamp = pd.to_datetime (event.EventTime)
    Timestamp.append (timestamp)
event_data['EventTime'] = Timestamp

Events = []
Start = []
End =[]
Team = []

for row,event in event_data.iterrows ():
    if event['Team'] == team1 or event['WinnerTeam'] == team1:
        team = team1
        start = event.EventTime
        end = event.EventTime
        events = 1
        
        if row+1 <= (len (event_data)-1):
            if (event_data.loc[[row+1]].Team.item ()) == team1 or (event_data.loc[[row+1]].WinnerTeam.item ()) == team1:
                end = event_data.loc[[row+1]].EventTime.item ()
                events = 2
                if  (event_data.loc[[row+2]].Team.item ()) == team1 or (event_data.loc[[row+2]].WinnerTeam.item ()) == team1:
                    end = event_data.loc[[row+2]].EventTime.item ()
                    events = 3
                    if (event_data.loc[[row+3]].Team.item ()) == team1 or (event_data.loc[[row+3]].WinnerTeam.item ()) == team1:
                        end = event_data.loc[[row+3]].EventTime.item ()
                        events = 4
                        if (event_data.loc[[row+4]].Team.item ()) == team1 or (event_data.loc[[row+4]].WinnerTeam.item ()) == team1:
                            end = event_data.loc[[row+4]].EventTime.item ()
                            events = 5
                            if (event_data.loc[[row+5]].Team.item ()) == team1 or (event_data.loc[[row+5]].WinnerTeam.item ()) == team1:
                                end = event_data.loc[[row+5]].EventTime.item ()
                                events = 6
                                if (event_data.loc[[row+6]].Team.item ()) == team1 or (event_data.loc[[row+6]].WinnerTeam.item ()) == team1:
                                    end = event_data.loc[[row+6]].EventTime.item ()
                                    events = 7
                                    if (event_data.loc[[row+7]].Team.item ()) == team1 or (event_data.loc[[row+7]].WinnerTeam.item ()) == team1:
                                        end = event_data.loc[[row+7]].EventTime.item ()
                                        events = 8
                                        if (event_data.loc[[row+8]].Team.item ()) == team1 or (event_data.loc[[row+8]].WinnerTeam.item ()) == team1:
                                            end = event_data.loc[[row+8]].EventTime.item ()
                                            events = 9
                                            if (event_data.loc[[row+9]].Team.item ()) == team1 or (event_data.loc[[row+9]].WinnerTeam.item ()) == team1:
                                                end = event_data.loc[[row+9]].EventTime.item ()
                                                events = 10
                                                if (event_data.loc[[row+10]].Team.item ()) == team1 or (event_data.loc[[row+10]].WinnerTeam.item ()) == team1:
                                                    end = event_data.loc[[row+10]].EventTime.item ()
                                                    events = 11
                                                    if (event_data.loc[[row+11]].Team.item ()) == team1 or (event_data.loc[[row+11]].WinnerTeam.item ()) == team1:
                                                        end = event_data.loc[[row+11]].EventTime.item ()
                                                        events = 12
                                                        if (event_data.loc[[row+12]].Team.item ()) == team1 or (event_data.loc[[row+12]].WinnerTeam.item ()) == team1:
                                                            end = event_data.loc[[row+12]].EventTime.item ()
                                                            events = 13
                                                            if (event_data.loc[[row+13]].Team.item ()) == team1 or (event_data.loc[[row+13]].WinnerTeam.item ()) == team1:
                                                                end = event_data.loc[[row+13]].EventTime.item ()
                                                                events = 14
                                                                if (event_data.loc[[row+14]].Team.item ()) == team1 or (event_data.loc[[row+14]].WinnerTeam.item ()) == team1:
                                                                    end = event_data.loc[[row+14]].EventTime.item ()
                                                                    events = 15
                                                                    if (event_data.loc[[row+15]].Team.item ()) == team1 or (event_data.loc[[row+15]].WinnerTeam.item ()) == team1:
                                                                        end = event_data.loc[[row+15]].EventTime.item ()
                                                                        events = 16
                                                                        if (event_data.loc[[row+16]].Team.item ()) == team1 or (event_data.loc[[row+16]].WinnerTeam.item ()) == team1:
                                                                            end = event_data.loc[[row+16]].EventTime.item ()
                                                                            events = 17
                                                                            if (event_data.loc[[row+17]].Team.item ()) == team1 or (event_data.loc[[row+17]].WinnerTeam.item ()) == team1:
                                                                                end = event_data.loc[[row+17]].EventTime.item ()
                                                                                events = 18
                                                                                if (event_data.loc[[row+18]].Team.item ()) == team1 or (event_data.loc[[row+18]].WinnerTeam.item ()) == team1:
                                                                                    end = event_data.loc[[row+18]].EventTime.item ()
                                                                                    events = 19
                                                                                    if (event_data.loc[[row+19]].Team.item ()) == team1 or (event_data.loc[[row+19]].WinnerTeam.item ()) == team1:
                                                                                        end = event_data.loc[[row+19]].EventTime.item ()
                                                                                        events = 20
                                                                                        if (event_data.loc[[row+20]].Team.item ()) == team1 or (event_data.loc[[row+20]].WinnerTeam.item ()) == team1:
                                                                                            end = event_data.loc[[row+20]].EventTime.item ()
                                                                                            events = 21
                                                                                            if (event_data.loc[[row+21]].Team.item ()) == team1 or (event_data.loc[[row+21]].WinnerTeam.item ()) == team1:
                                                                                                end = event_data.loc[[row+21]].EventTime.item ()
                                                                                                events = 22
                                                                                                if (event_data.loc[[row+22]].Team.item ()) == team1 or (event_data.loc[[row+22]].WinnerTeam.item ()) == team1:
                                                                                                    end = event_data.loc[[row+22]].EventTime.item ()
                                                                                                    events = 23
                                                                                                    if (event_data.loc[[row+23]].Team.item ()) == team1 or (event_data.loc[[row+23]].WinnerTeam.item ()) == team1 :
                                                                                                        end = event_data.loc[[row+23]].EventTime.item ()
                                                                                                        events = 24
                                                                                                        if (event_data.loc[[row+24]].Team.item ()) == team1 or (event_data.loc[[row+24]].WinnerTeam.item ()) == team1 :
                                                                                                            end = event_data.loc[[row+24]].EventTime.item ()
                                                                                                            events = 25
                                                                                                            if (event_data.loc[[row+25]].Team.item ()) == team1 or (event_data.loc[[row+25]].WinnerTeam.item ()) == team1 :
                                                                                                                end = event_data.loc[[row+25]].EventTime.item ()
                                                                                                                events = 26
                                                                                                                if (event_data.loc[[row+26]].Team.item ()) == team1 or (event_data.loc[[row+26]].WinnerTeam.item ()) == team1 :
                                                                                                                    end = event_data.loc[[row+26]].EventTime.item ()
                                                                                                                    events = 27
                                                                                                                    if (event_data.loc[[row+27]].Team.item ()) == team1 or (event_data.loc[[row+27]].WinnerTeam.item ()) == team1 :
                                                                                                                        end = event_data.loc[[row+27]].EventTime.item ()
                                                                                                                        events = 28
                                                                                                                        if (event_data.loc[[row+28]].Team.item ()) == team1 or (event_data.loc[[row+28]].WinnerTeam.item ()) == team1 :
                                                                                                                            end = event_data.loc[[row+28]].EventTime.item ()
                                                                                                                            events = 29
                                                                                                                            if (event_data.loc[[row+29]].Team.item ()) == team1 or (event_data.loc[[row+29]].WinnerTeam.item ()) == team1 :
                                                                                                                                end = event_data.loc[[row+29]].EventTime.item ()
                                                                                                                                events = 30
                                                                                                                                if (event_data.loc[[row+30]].Team.item ()) == team1 or (event_data.loc[[row+30]].WinnerTeam.item ()) == team1 :
                                                                                                                                    end = event_data.loc[[row+30]].EventTime.item ()
                                                                                                                                    events = 31
    elif event['Team'] == team2 or event['WinnerTeam'] == team2:
        team = team2
        start = event.EventTime
        end = event.EventTime
        events = 1
        
        if row+1 <= (len (event_data)-1):
            if (event_data.loc[[row+1]].Team.item ()) == team2 or (event_data.loc[[row+1]].WinnerTeam.item ()) == team2 :
                end = event_data.loc[[row+1]].EventTime.item ()
                events = 2
                if  (event_data.loc[[row+2]].Team.item ()) == team2 or (event_data.loc[[row+2]].WinnerTeam.item ()) == team2 :
                    end = event_data.loc[[row+2]].EventTime.item ()
                    events = 3
                    if (event_data.loc[[row+3]].Team.item ()) == team2 or (event_data.loc[[row+3]].WinnerTeam.item ()) == team2 :
                        end = event_data.loc[[row+3]].EventTime.item ()
                        events = 4
                        if (event_data.loc[[row+4]].Team.item ()) == team2 or (event_data.loc[[row+4]].WinnerTeam.item ()) == team2 :
                            end = event_data.loc[[row+4]].EventTime.item ()
                            events = 5
                            if (event_data.loc[[row+5]].Team.item ()) == team2 or (event_data.loc[[row+5]].WinnerTeam.item ()) == team2 :
                                end = event_data.loc[[row+5]].EventTime.item ()
                                events = 6
                                if (event_data.loc[[row+6]].Team.item ()) == team2 or (event_data.loc[[row+6]].WinnerTeam.item ()) == team2:
                                    end = event_data.loc[[row+6]].EventTime.item ()
                                    events = 7
                                    if (event_data.loc[[row+7]].Team.item ()) == team2 or (event_data.loc[[row+7]].WinnerTeam.item ()) == team2 :
                                        end = event_data.loc[[row+7]].EventTime.item ()
                                        events = 8
                                        if (event_data.loc[[row+8]].Team.item ()) == team2 or (event_data.loc[[row+8]].WinnerTeam.item ()) == team2 :
                                            end = event_data.loc[[row+8]].EventTime.item ()
                                            events = 9
                                            if (event_data.loc[[row+9]].Team.item ()) == team2 or (event_data.loc[[row+9]].WinnerTeam.item ()) == team2:
                                                end = event_data.loc[[row+9]].EventTime.item ()
                                                events = 10
                                                if (event_data.loc[[row+10]].Team.item ()) == team2 or (event_data.loc[[row+10]].WinnerTeam.item ()) == team2 :
                                                    end = event_data.loc[[row+10]].EventTime.item ()
                                                    events = 11
                                                    if (event_data.loc[[row+11]].Team.item ()) == team2 or (event_data.loc[[row+11]].WinnerTeam.item ()) == team2 :
                                                        end = event_data.loc[[row+11]].EventTime.item ()
                                                        events = 12
                                                        if (event_data.loc[[row+12]].Team.item ()) == team2 or (event_data.loc[[row+12]].WinnerTeam.item ()) == team2:
                                                            end = event_data.loc[[row+12]].EventTime.item ()
                                                            events = 13
                                                            if (event_data.loc[[row+13]].Team.item ()) == team2 or (event_data.loc[[row+13]].WinnerTeam.item ()) == team2:
                                                                end = event_data.loc[[row+13]].EventTime.item ()
                                                                events = 14
                                                                if (event_data.loc[[row+14]].Team.item ()) == team2 or (event_data.loc[[row+14]].WinnerTeam.item ()) == team2:
                                                                    end = event_data.loc[[row+14]].EventTime.item ()
                                                                    events = 15
                                                                    if (event_data.loc[[row+15]].Team.item ()) == team2 or (event_data.loc[[row+15]].WinnerTeam.item ()) == team2 :
                                                                        end = event_data.loc[[row+15]].EventTime.item ()
                                                                        events = 16
                                                                        if (event_data.loc[[row+16]].Team.item ()) == team2 or (event_data.loc[[row+16]].WinnerTeam.item ()) == team2 :
                                                                            end = event_data.loc[[row+16]].EventTime.item ()
                                                                            events = 17
                                                                            if (event_data.loc[[row+17]].Team.item ()) == team2 or (event_data.loc[[row+17]].WinnerTeam.item ()) == team2 :
                                                                                end = event_data.loc[[row+17]].EventTime.item ()
                                                                                events = 18
                                                                                if (event_data.loc[[row+18]].Team.item ()) == team2 or (event_data.loc[[row+18]].WinnerTeam.item ()) == team2 :
                                                                                    end = event_data.loc[[row+18]].EventTime.item ()
                                                                                    events = 19
                                                                                    if (event_data.loc[[row+19]].Team.item ()) == team2 or (event_data.loc[[row+19]].WinnerTeam.item ()) == team2 :
                                                                                        end = event_data.loc[[row+19]].EventTime.item ()
                                                                                        events = 20
                                                                                        if (event_data.loc[[row+20]].Team.item ()) == team2 or (event_data.loc[[row+20]].WinnerTeam.item ()) == team2 :
                                                                                            end = event_data.loc[[row+20]].EventTime.item ()
                                                                                            events = 21
                                                                                            if (event_data.loc[[row+21]].Team.item ()) == team2 or (event_data.loc[[row+21]].WinnerTeam.item ()) == team2 :
                                                                                                end = event_data.loc[[row+21]].EventTime.item ()
                                                                                                events = 22
                                                                                                if (event_data.loc[[row+22]].Team.item ()) == team2 or (event_data.loc[[row+22]].WinnerTeam.item ()) == team2:
                                                                                                    end = event_data.loc[[row+22]].EventTime.item ()
                                                                                                    events = 23
                                                                                                    if (event_data.loc[[row+23]].Team.item ()) == team2 or (event_data.loc[[row+23]].WinnerTeam.item ()) == team2 :
                                                                                                        end = event_data.loc[[row+23]].EventTime.item ()
                                                                                                        events = 24
                                                                                                        if (event_data.loc[[row+24]].Team.item ()) == team2 or (event_data.loc[[row+24]].WinnerTeam.item ()) == team2 :
                                                                                                            end = event_data.loc[[row+24]].EventTime.item ()
                                                                                                            events = 25
                                                                                                            if (event_data.loc[[row+25]].Team.item ()) == team2 or (event_data.loc[[row+25]].WinnerTeam.item ()) == team2 :
                                                                                                                end = event_data.loc[[row+25]].EventTime.item ()
                                                                                                                events = 26
                                                                                                                if (event_data.loc[[row+26]].Team.item ()) == team2 or (event_data.loc[[row+26]].WinnerTeam.item ()) == team2:
                                                                                                                    end = event_data.loc[[row+26]].EventTime.item ()
                                                                                                                    events = 27
                                                                                                                    if (event_data.loc[[row+27]].Team.item ()) == team2 or (event_data.loc[[row+27]].WinnerTeam.item ()) == team2:
                                                                                                                        end = event_data.loc[[row+27]].EventTime.item ()
                                                                                                                        events = 28
                                                                                                                        if (event_data.loc[[row+28]].Team.item ()) == team2 or (event_data.loc[[row+28]].WinnerTeam.item ()) == team2 :
                                                                                                                            end = event_data.loc[[row+28]].EventTime.item ()
                                                                                                                            events = 29
                                                                                                                            if (event_data.loc[[row+29]].Team.item ()) == team2 or (event_data.loc[[row+29]].WinnerTeam.item ()) == team2 :
                                                                                                                                end = event_data.loc[[row+29]].EventTime.item ()
                                                                                                                                events = 30
                                                                                                                                if (event_data.loc[[row+30]].Team.item ()) == team2 or (event_data.loc[[row+30]].WinnerTeam.item ()) == team2 :
                                                                                                                                    end = event_data.loc[[row+30]].EventTime.item ()
                                                                                                                                    events = 31
    Events.append (events)
    Start.append (start)
    End.append (end)
    Team.append (team)
possessions = pd.DataFrame ()
possessions['team'] = Team
possessions['start'] = Start
possessions['end'] = End
possessions['actions'] = Events

rows_to_delete = []
for row2,attack in possessions.iterrows ():
    
    if row2-1 >= 0:
        if attack.end == possessions.loc[[row2-1]].end.item () :
            rows = row2
            rows_to_delete.append (row2)     
    
possessions = possessions.drop (rows_to_delete, axis=0)


#%% Filtering of deliberate attacks
# 1. more than 5 Seconds
# 2. more than 3 consecutive passes
Pass_number = []
Duration_sec = []


#possessions_deliberate 
for row, attack in possessions.iterrows ():
    actions = event_data[(event_data['EventTime'] >= attack.start) &
                         (event_data['EventTime'] <= attack.end)]
    pass_number = len (actions[actions['Event1'] == 'Play'])
    Pass_number.append (pass_number)
    
    start_sec = (((attack.start.hour)*60)*60) + ((attack.start.minute)*60) + (attack.start.second) + ((attack.start.microsecond)/1000000)
    end_sec = (((attack.end.hour)*60)*60) + ((attack.end.minute)*60) + (attack.end.second) + ((attack.end.microsecond)/1000000)
    duration_sec = end_sec - start_sec
    Duration_sec.append (duration_sec)

possessions['PassNumber'] = Pass_number
possessions['PossessionDuration[s]'] = Duration_sec


possessions = possessions[(possessions['PassNumber'] >= 3) &
                          (possessions['PossessionDuration[s]'] >= 5)]
#%% 1. Differentiation of attacks (successful/unsuccessful)
# successful: Ball gain (Event1: 'BallClaiming') & (Event1: 'TacklingGame' & PossessionChange: 'True')
# unsuccessful: shots on goal (Event1: 'ShotAtGoal')

# 2. Identification of playing direction



#1.:
possessions = possessions.reset_index ()
possessions = possessions.rename (columns = {'index': 'Row'})


Result = []
Defensive_success = []
X_Position = []

#2.:
first_half = event_data[(event_data['Event1'] == 'KickOff') &
                        (event_data['GameSection'] == 'firstHalf')]
second_half = event_data[(event_data['Event1'] == 'KickOff') &
                         (event_data['GameSection'] == 'secondHalf')]
Team_left = []
Team_right = []

for row, attack in possessions.iterrows ():
    actions = event_data[(event_data['EventTime'] >= attack.start) &
                         (event_data['EventTime'] <= attack.end)]
    idx = attack.actions + attack.Row
    #BallClaiming in first row after possession end:
    if event_data.loc[[idx]].Event1.item () == 'BallClaiming' and event_data.loc[[idx]].Team.item () != attack.team:
        x_position = event_data.loc[[idx]]['X-Position'].item ()
        result = 'ball_loss_claiming1'
        defensive_success = 'successful'

    #Ballloss after tackling in first row after possession end:
    elif event_data.loc[[idx]].Event1.item () == 'TacklingGame' and event_data.loc[[idx]].WinnerTeam.item () != attack.team and event_data.loc[[idx]].PossessionChange.item () == True:
        x_position = event_data.loc[[idx]]['X-Position'].item ()
        result = 'ball_loss_tackling1'
        defensive_success = 'successful'
        
    #Ballloss after tackling in second row after possession end:
    elif event_data.loc[[idx+1]].Event1.item () == 'TacklingGame' and event_data.loc[[idx+1]].WinnerTeam.item () != attack.team and event_data.loc[[idx+1]].PossessionChange.item () == True:
        x_position = event_data.loc[[idx+1]]['X-Position'].item ()
        result = 'ball_loss_tackling2'
        defensive_success = 'successful'
        
    #BallClaiming in second row after possession end & Tackling with possession change in first row after possession end:
    elif event_data.loc[[idx+1]].Event1.item () == 'BallClaiming' and event_data.loc[[idx+1]].Team.item () != attack.team and event_data.loc[[idx]].Event1.item () == 'TacklingGame' and event_data.loc[[idx]].PossessionChange.item () == True:
        x_position = event_data.loc[[idx+1]]['X-Position'].item ()
        result = 'ball_loss_claiming_after_tackling'
        defensive_success = 'successful'
        
    #BallClaiming in second row after possession end & NO! Tackling in first row after possession change:
    elif event_data.loc[[idx+1]].Event1.item () == 'BallClaiming' and event_data.loc[[idx+1]].Team.item () != attack.team and event_data.loc[[idx]].Event1.item () != 'TacklingGame':
        x_position = event_data.loc[[idx+1]]['X-Position'].item ()
        result = 'ball_loss_claiming2'
        defensive_success = 'successful'

    #Ballgain after unsuccessful pass: last action of attack is unsuccessful pass & next action is on ball action of other team & no event called BallClaiming:
    elif event_data.loc[[idx-1]].Event1.item () == 'Play' and event_data.loc[[idx-1]].Evaluation.item () == 'unsuccessful' and event_data.loc[[idx]].Team.item () != attack.team and event_data.loc[[idx]].Event1.item () != 'Play' and event_data.loc[[idx]].Event1.item () != 'BallClaiming' and event_data.loc[[idx+1]].Event1.item () != 'BallClaiming':
        x_position = event_data.loc[[idx-1]]['X-Position'].item ()
        result = 'ball_loss_unsuccessfulpass'
        defensive_success = 'successful'
    
    
    #last action of attack is shot at goal:
    elif event_data.loc[[idx-1]].Event1.item () == 'ShotAtGoal':
        x_position = event_data.loc[[idx-1]]['X-Position'].item ()
        result = 'ShotAtGoal1'
        defensive_success = 'unsuccessful'
    
    #penultimate action of attack is shot at goal:
    elif event_data.loc[[idx-2]].Event1.item () == 'ShotAtGoal' and event_data.loc[[idx-1]].Event1.item () != 'ShotAtGoal':
        x_position = event_data.loc[[idx-2]]['X-Position'].item ()
        result = 'ShotAtGoal2'
        defensive_success = 'unsuccessful'

    else:
        x_position = event_data.loc[[idx-1]]['X-Position'].item ()
        result = 'other'
        defensive_success = 'other'
    
    Result.append (result)
    Defensive_success.append (defensive_success)
    X_Position.append (x_position)
    
    # Identification of playing direction
    if attack.start >= first_half.EventTime.item() and attack.start <= second_half.EventTime.item():
        #attack is in first half
        team_left = first_half.TeamLeft.item ()
        team_right = first_half.TeamRight.item()
        
    elif attack.start >= second_half.EventTime.item():
        #attack is in second half
        team_left = second_half.TeamLeft.item ()
        team_right = second_half.TeamRight.item()
    
    Team_left.append (team_left)
    Team_right.append (team_right)


possessions['PossessionResult'] = Result
possessions['DefensiveSuccess'] = Defensive_success
possessions['X_Position_OfLastDefensiveAction'] = X_Position
possessions['TeamLeft'] = Team_left
possessions['TeamRight'] = Team_right


#%%#%% Calculation of defensive pressure

def pressure_quantification (attacker, defender, goal_x, goal_y):
    distance = math.sqrt((defender['X'].item() - attacker['X'].item())**2 + (defender['Y'].item() - attacker['Y'].item())**2)
    
    threat_direction = math.degrees (math.asin ((abs (attacker['Y'].item() - goal_y)) / (math.sqrt((attacker['X'].item() - goal_x)**2 + (attacker['Y'].item() - goal_y)**2))))
    
    angle_defender = math.degrees (math.asin ((abs (defender['Y'].item() - goal_y)) / (math.sqrt((defender['X'].item() - goal_x)**2 + (defender['Y'].item() - goal_y)**2))))
    
    angle_between = abs (threat_direction - angle_defender)
    
    # Case 1 : Defender is in front of the Attacker:
    if goal_x == 0 and defender['X'].item() > attacker['X'].item() or goal_x > 0 and defender['X'].item() < attacker['X'].item():
        Form = (1 - (math.cos (math.radians(angle_between))))/2
        Length = 3 + ((9 - 3)*(( Form **3) + ( Form * 0.3)) / 1.3)
        
        if distance > Length:
            pressure = 0
        else:
            pressure = (1 - distance / (Length))**1.75 *100
        
        
    # Case 2 : Defender is behind of the Attacker:
    if goal_x == 0 and defender['X'].item() < attacker['X'].item() or goal_x > 0 and defender['X'].item() > attacker['X'].item ():
        angle_between = angle_between + 180
        
        Form = (1 - (math.cos (math.radians(angle_between))))/2
        Length = 3 + ((9 - 3)*(( Form **3) + ( Form * 0.3)) / 1.3)
        
        if distance > Length:
            pressure = 0
        else:
            pressure = (1 - distance / (Length))**1.75 *100
    
    
    #Case 3: Defender is exactly beneath attacker
    if defender['X'].item() == attacker['X'].item():
        angle_between = 90
        
        Form = (1 - (math.cos (math.radians(angle_between))))/2
        Length = 3 + ((9 - 3)*(( Form **3) + ( Form * 0.3)) / 1.3)
        
        if distance > Length:
            pressure = 0
        else:
            pressure = (1 - distance / (Length))**1.75 *100
            
            
    #Case 4: Defender is in the same spot as attacker
    if defender['X'].item() == attacker['X'].item() and defender['Y'].item() == attacker['Y'].item():
        pressure = 100
    return pressure


#%% Measurement of defensive pressure

# 1. Identification of last 4 on ball actions (at this moment only passes are considered) of an attack (remove actions with no value for the study )
# 2. Synchronization of events with position data
    # 1. Identification of position data 10 seconds before and 10 seconds after Event Time of considered event (Of at least 2 Players (when TacklingGame) or 1 Player and the Ball (When ball action))
    # 2. Calculate difference of X- & Y-Data of Event with X- & Y-Date of Position data in this area (of those 20 seconds)
    # 3. Find the smallest difference --> Identified Moment of Event
# 3. Measurement of defensive pressure

#Measurement of defensive pressure for last action of attack
OnBallPressure_LastAction = []
OnGroupPressure1_LastAction = []
OnGroupPressure2_LastAction = []
OnGroupPressure3_LastAction = []
OnGroupPressure4_LastAction = []
OnGroupPressure5_LastAction = []
OnGroupPressure6_LastAction = []
OnGroupPressure7_LastAction = []
OnGroupPressure8_LastAction = []
OnGroupPressure9_LastAction = []
OnGroupPressure10_LastAction = []

frame_lastaction = []

for row, attack in possessions.iterrows ():
    actions = event_data[(event_data['EventTime'] >= attack.start) &
                         (event_data['EventTime'] <= attack.end)]

    
    #find all ball actions in the possession that have value for the study:
    ball_actions = ['Play', 'OtherBallAction', 'TacklingGame', 'BallClaiming', 'FreeKick', 'ThrowIn', 'ShotAtGoal', 'CornerKick', 'GoalKick', 'KickOff']
    actions = actions[(actions['Event1'] == 'Play') |
                      (actions['Event2'] == 'Play') ]
    
    actions = actions.reset_index ()
    length = len (actions)
    
    #Last action
    action_last = actions.loc [[(length-1)]]
    
    #Find right frame of position data of this action (Snchronization of Event & Position data)
    start_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  - 8
    end_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  + 8

    if action_last.Event1.item () == 'TacklingGame':
        #First Player
        search_field1 = position_data[position_data['PersonId'] == (action_last.Winner.item ())]
        search_field1 = search_field1[(search_field1['T_sec'] >= start_sync1) &
                                      (search_field1['T_sec'] <= end_sync1)]
        #Second Player
        search_field_second1 = position_data[position_data['PersonId'] == (action_last.Loser.item ())]
        search_field_second1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                    (search_field_second1['T_sec'] <= end_sync1)]
        
        search_field1 = search_field1.reset_index ()
        search_field1 = search_field1.loc [0:399]

        search_field_second1 = search_field_second1.reset_index ()
        search_field_second1 = search_field_second1.loc [0:399]
        
        search_field1 = search_field1.join (search_field_second1, lsuffix = '_1', rsuffix = '_2')
        
        Difference1 = []
        for index, frame in search_field1.iterrows ():
            # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
            difference1 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_last['X-Position'])) + (abs(frame['Y_1'] - action_last['Y-Position']))) + ((abs(frame['X_2'] - action_last['X-Position'])) + (abs(frame['Y_2'] - action_last['Y-Position'])))).item()) /21)**2
            Difference1.append (difference1)
    
        search_field1 ['difference'] = Difference1
        identified_frame1 = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
        identified_frames1 = position_data[position_data['T_sec'] == identified_frame1]


    elif action_last.Recipient.isnull ().item() == False and (action_last.Event1.item () == 'Play' or action_last.Event2.item () == 'Play'):
        #First Player
        search_field1 = position_data[position_data['PersonId'] == (action_last.Player.item ())]
        search_field1 = search_field1[(search_field1['T_sec'] >= start_sync1) &
                                      (search_field1['T_sec'] <= end_sync1)]
        
        #Ball
        search_field_second1 = position_data[position_data['TeamId'] == 'BALL']
        search_field_second1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                    (search_field_second1['T_sec'] <= end_sync1)]
        #Reciever with 1 sec plus
        search_field_receiver = position_data[position_data['PersonId'] == (action_last.Recipient.item ())]
        search_field_receiver = search_field_receiver[(search_field_receiver['T_sec'] >= (start_sync1 + 1)) &
                                                      (search_field_receiver['T_sec'] <= (end_sync1 + 1))]
        
        #Ball with 1 sec plus
        search_field_ball2 = position_data[position_data['TeamId'] == 'BALL']
        search_field_ball2 = search_field_ball2[(search_field_ball2['T_sec'] >= (start_sync1 + 1)) &
                                                    (search_field_ball2['T_sec'] <= (end_sync1 + 1))]
        search_field1 = search_field1.reset_index ()
        search_field1 = search_field1.loc [0:399]
    
        search_field_second1 = search_field_second1.reset_index ()
        search_field_second1 = search_field_second1.loc [0:399]
        
        search_field_receiver = search_field_receiver.reset_index ()
        search_field_receiver = search_field_receiver.loc [0:399]
        
        search_field_ball2 = search_field_ball2.reset_index ()
        search_field_ball2 = search_field_ball2.loc [0:399]
        
        search_field1 = search_field1.join (search_field_second1, lsuffix = '_1', rsuffix = '_2')
        search_field_receiver = search_field_receiver.join (search_field_ball2, lsuffix = '_3', rsuffix = '_4')
        
        search_field1 = search_field1.join (search_field_receiver)
        
        Difference1 = []
        Dif1 = []
        for index, frame in search_field1.iterrows ():
            # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
            # (Differnece Player to Ball *10) + (Difference Player & Ball to Origin of Event*1) + (Difference of Receiever to Ball 1 Sec after Pass)
            difference1 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_last['X-Position'])) + (abs(frame['Y_1'] - action_last['Y-Position']))) + ((abs(frame['X_2'] - action_last['X-Position'])) + (abs(frame['Y_2'] - action_last['Y-Position'])))).item()  + ((abs(frame['X_3'] - frame['X_4'])) + (abs(frame['Y_3'] - frame['Y_4'])))   ) /22)**2
            Difference1.append (difference1)
            diff2       = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_last['X-Position'])) + (abs(frame['Y_1'] - action_last['Y-Position']))) + ((abs(frame['X_2'] - action_last['X-Position'])) + (abs(frame['Y_2'] - action_last['Y-Position'])))).item()) /21)**2
            Dif1.append (diff2)
        search_field1 ['difference2'] = Dif1
        search_field1 ['difference'] = Difference1
        identified_frame1 = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
        identified_frames1 = position_data[position_data['T_sec'] == identified_frame1]
        
    else:
        #First Player
        search_field1 = position_data[position_data['PersonId'] == (action_last.Player.item ())]
        search_field1 = search_field1[(search_field1['T_sec'] >= start_sync1) &
                                      (search_field1['T_sec'] <= end_sync1)]
        
        #Ball
        search_field_second1 = position_data[position_data['TeamId'] == 'BALL']
        search_field_second1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                    (search_field_second1['T_sec'] <= end_sync1)]
        
        search_field1 = search_field1.reset_index ()
        search_field1 = search_field1.loc [0:399]

        search_field_second1 = search_field_second1.reset_index ()
        search_field_second1 = search_field_second1.loc [0:399]
        
        search_field1 = search_field1.join (search_field_second1, lsuffix = '_1', rsuffix = '_2')
        
        Difference1 = []
        for index, frame in search_field1.iterrows ():
            # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
            difference1 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_last['X-Position'])) + (abs(frame['Y_1'] - action_last['Y-Position']))) + ((abs(frame['X_2'] - action_last['X-Position'])) + (abs(frame['Y_2'] - action_last['Y-Position'])))).item()) /21)**2
            
            Difference1.append (difference1)
    
        search_field1 ['difference'] = Difference1
        identified_frame1 = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
        identified_frames1 = position_data[position_data['T_sec'] == identified_frame1]
        
    
    frame_lastaction.append (identified_frame1)
#Measurement of defensive pressure for last action

#Case 1: Team1 is in ball possession and plays from left to right
    if attack.team == team1 and attack.TeamLeft == team1:
        #Identification of ball leading player
        if action_last.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames1[identified_frames1['PersonId'] == action_last.Winner.item ()]
        else:
            ball_leader = identified_frames1[identified_frames1['PersonId'] == action_last.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames1[identified_frames1['TeamId'] == team2]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames1[identified_frames1['TeamId'] == team1]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 105, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 105, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 105, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 105, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 105, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 105, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 105, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 105, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 105, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 105, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 105, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_lastaction = max (Press_onball)
        ongrouppressure1_lastaction = max (Press_ongroup1)
        ongrouppressure2_lastaction = max (Press_ongroup2)
        ongrouppressure3_lastaction = max (Press_ongroup3)
        ongrouppressure4_lastaction = max (Press_ongroup4)
        ongrouppressure5_lastaction = max (Press_ongroup5)
        ongrouppressure6_lastaction = max (Press_ongroup6)
        ongrouppressure7_lastaction = max (Press_ongroup7)
        ongrouppressure8_lastaction = max (Press_ongroup8)
        ongrouppressure9_lastaction = max (Press_ongroup9)
        ongrouppressure10_lastaction = max (Press_ongroup10)
#Case 2: Team1 is in ball possession and plays from right to left      
    elif attack.team == team1 and attack.TeamRight == team1:
        #Identification of ball leading player
        if action_last.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames1[identified_frames1['PersonId'] == action_last.Winner.item ()]
        else:
            ball_leader = identified_frames1[identified_frames1['PersonId'] == action_last.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames1[identified_frames1['TeamId'] == team2]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames1[identified_frames1['TeamId'] == team1]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 0, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 0, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 0, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 0, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 0, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 0, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 0, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 0, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 0, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 0, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 0, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_lastaction = max (Press_onball)
        ongrouppressure1_lastaction = max (Press_ongroup1)
        ongrouppressure2_lastaction = max (Press_ongroup2)
        ongrouppressure3_lastaction = max (Press_ongroup3)
        ongrouppressure4_lastaction = max (Press_ongroup4)
        ongrouppressure5_lastaction = max (Press_ongroup5)
        ongrouppressure6_lastaction = max (Press_ongroup6)
        ongrouppressure7_lastaction = max (Press_ongroup7)
        ongrouppressure8_lastaction = max (Press_ongroup8)
        ongrouppressure9_lastaction = max (Press_ongroup9)
        ongrouppressure10_lastaction = max (Press_ongroup10)
#Case 3: Team2 is in ball possession and plays from left to right         
    elif attack.team == team2 and attack.TeamLeft == team2:
        #Identification of ball leading player
        if action_last.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames1[identified_frames1['PersonId'] == action_last.Winner.item ()]
        else:
            ball_leader = identified_frames1[identified_frames1['PersonId'] == action_last.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames1[identified_frames1['TeamId'] == team1]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames1[identified_frames1['TeamId'] == team2]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 105, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 105, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 105, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 105, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 105, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 105, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 105, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 105, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 105, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 105, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 105, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_lastaction = max (Press_onball)
        ongrouppressure1_lastaction = max (Press_ongroup1)
        ongrouppressure2_lastaction = max (Press_ongroup2)
        ongrouppressure3_lastaction = max (Press_ongroup3)
        ongrouppressure4_lastaction = max (Press_ongroup4)
        ongrouppressure5_lastaction = max (Press_ongroup5)
        ongrouppressure6_lastaction = max (Press_ongroup6)
        ongrouppressure7_lastaction = max (Press_ongroup7)
        ongrouppressure8_lastaction = max (Press_ongroup8)
        ongrouppressure9_lastaction = max (Press_ongroup9)
        ongrouppressure10_lastaction = max (Press_ongroup10)
#Case 4: Team2 is in ball possession and plays from right to left       
    elif attack.team == team2 and attack.TeamRight == team2:
        
        #Identification of ball leading player
        if action_last.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames1[identified_frames1['PersonId'] == action_last.Winner.item ()]
        else:
            ball_leader = identified_frames1[identified_frames1['PersonId'] == action_last.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames1[identified_frames1['TeamId'] == team1]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames1[identified_frames1['TeamId'] == team2]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 0, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 0, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 0, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 0, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 0, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 0, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 0, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 0, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 0, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 0, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 0, 34)
            Press_ongroup10.append (press_ongroup10)
            
        onballpressure_lastaction = max (Press_onball)
        ongrouppressure1_lastaction = max (Press_ongroup1)
        ongrouppressure2_lastaction = max (Press_ongroup2)
        ongrouppressure3_lastaction = max (Press_ongroup3)
        ongrouppressure4_lastaction = max (Press_ongroup4)
        ongrouppressure5_lastaction = max (Press_ongroup5)
        ongrouppressure6_lastaction = max (Press_ongroup6)
        ongrouppressure7_lastaction = max (Press_ongroup7)
        ongrouppressure8_lastaction = max (Press_ongroup8)
        ongrouppressure9_lastaction = max (Press_ongroup9)
        ongrouppressure10_lastaction = max (Press_ongroup10)

    OnBallPressure_LastAction.append (onballpressure_lastaction)
    OnGroupPressure1_LastAction.append (ongrouppressure1_lastaction)
    OnGroupPressure2_LastAction.append (ongrouppressure2_lastaction)
    OnGroupPressure3_LastAction.append (ongrouppressure3_lastaction)
    OnGroupPressure4_LastAction.append (ongrouppressure4_lastaction)
    OnGroupPressure5_LastAction.append (ongrouppressure5_lastaction)
    OnGroupPressure6_LastAction.append (ongrouppressure6_lastaction)
    OnGroupPressure7_LastAction.append (ongrouppressure7_lastaction)
    OnGroupPressure8_LastAction.append (ongrouppressure8_lastaction)
    OnGroupPressure9_LastAction.append (ongrouppressure9_lastaction)
    OnGroupPressure10_LastAction.append (ongrouppressure10_lastaction)


#%%
#Measurement of defensive pressure for penultimate action of attack
OnBallPressure_PenultimateAction = []
OnGroupPressure1_PenultimateAction = []
OnGroupPressure2_PenultimateAction = []
OnGroupPressure3_PenultimateAction = []
OnGroupPressure4_PenultimateAction = []
OnGroupPressure5_PenultimateAction = []
OnGroupPressure6_PenultimateAction = []
OnGroupPressure7_PenultimateAction = []
OnGroupPressure8_PenultimateAction = []
OnGroupPressure9_PenultimateAction = []
OnGroupPressure10_PenultimateAction = []

frame_penultimateaction = []


for row, attack in possessions.iterrows ():
    actions = event_data[(event_data['EventTime'] >= attack.start) &
                         (event_data['EventTime'] <= attack.end)]

    
    #find all ball actions in the possession that have value for the study:
    ball_actions = ['Play', 'OtherBallAction', 'TacklingGame', 'BallClaiming', 'FreeKick', 'ThrowIn', 'ShotAtGoal', 'CornerKick', 'GoalKick', 'KickOff']
    actions = actions[(actions['Event1'] == 'Play') |
                      (actions['Event2'] == 'Play') ]
    
    actions = actions.reset_index ()
    length = len (actions)
    
    #Penultimate action
    if length >= 2:
        action_penultimate = actions.loc [[(length-2)]]

        #Find right frame of position data of this action (Snchronization of Event & Position data)
        start_sync2 = (((action_penultimate.EventTime.item().hour)*60)*60) + ((action_penultimate.EventTime.item ().minute)*60) + (action_penultimate.EventTime.item().second) + ((action_penultimate.EventTime.item ().microsecond)/1000000)  - 8
        end_sync2 = (((action_penultimate.EventTime.item().hour)*60)*60) + ((action_penultimate.EventTime.item ().minute)*60) + (action_penultimate.EventTime.item().second) + ((action_penultimate.EventTime.item ().microsecond)/1000000)  + 8
    
        if action_penultimate.Event1.item () == 'TacklingGame':
            #First Player
            search_field2 = position_data[position_data['PersonId'] == (action_penultimate.Winner.item ())]
            search_field2 = search_field2[(search_field2['T_sec'] >= start_sync2) &
                                          (search_field2['T_sec'] <= end_sync2)]
            #Second Player
            search_field_second2 = position_data[position_data['PersonId'] == (action_penultimate.Loser.item ())]
            search_field_second2 = search_field_second2[(search_field_second2['T_sec'] >= start_sync2) &
                                                        (search_field_second2['T_sec'] <= end_sync2)]
            
            search_field2 = search_field2.reset_index ()
            search_field2 = search_field2.loc [0:399]
    
            search_field_second2 = search_field_second2.reset_index ()
            search_field_second2 = search_field_second2.loc [0:399]
            
            search_field2 = search_field2.join (search_field_second2, lsuffix = '_1', rsuffix = '_2')
            
            Difference2 = []
            for index, frame in search_field2.iterrows ():
                # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
                difference2 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_penultimate['X-Position'])) + (abs(frame['Y_1'] - action_penultimate['Y-Position']))) + ((abs(frame['X_2'] - action_penultimate['X-Position'])) + (abs(frame['Y_2'] - action_penultimate['Y-Position'])))).item()) /21)**2
                
                Difference2.append (difference2)
        
            search_field2 ['difference'] = Difference2
            identified_frame2 = search_field2[search_field2['difference'] == search_field2 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            identified_frames2 = position_data[position_data['T_sec'] == identified_frame2]

            
        elif action_penultimate.Recipient.isnull ().item() == False and (action_penultimate.Event1.item () == 'Play' or action_penultimate.Event2.item () == 'Play'):
            #First Player
            search_field2 = position_data[position_data['PersonId'] == (action_penultimate.Player.item ())]
            search_field2 = search_field2[(search_field2['T_sec'] >= start_sync2) &
                                          (search_field2['T_sec'] <= end_sync2)]
            
            #Ball
            search_field_second2 = position_data[position_data['TeamId'] == 'BALL']
            search_field_second2 = search_field_second2[(search_field_second2['T_sec'] >= start_sync2) &
                                                        (search_field_second2['T_sec'] <= end_sync2)]
            #Reciever with 1 sec plus
            search_field_receiver2 = position_data[position_data['PersonId'] == (action_penultimate.Recipient.item ())]
            search_field_receiver2 = search_field_receiver2[(search_field_receiver2['T_sec'] >= (start_sync2 + 1)) &
                                                          (search_field_receiver2['T_sec'] <= (end_sync2 + 1))]
            
            #Ball with 1 sec plus
            search_field_ball2_2 = position_data[position_data['TeamId'] == 'BALL']
            search_field_ball2_2= search_field_ball2_2[(search_field_ball2_2['T_sec'] >= (start_sync2 + 1)) &
                                                        (search_field_ball2_2['T_sec'] <= (end_sync2 + 1))]
            
            search_field2 = search_field2.reset_index ()
            search_field2 = search_field2.loc [0:399]
    
            search_field_second2 = search_field_second2.reset_index ()
            search_field_second2 = search_field_second2.loc [0:399]
            
            search_field_receiver2 = search_field_receiver2.reset_index ()
            search_field_receiver2 = search_field_receiver2.loc [0:399]
            
            search_field_ball2_2 = search_field_ball2_2.reset_index ()
            search_field_ball2_2 = search_field_ball2_2.loc [0:399]
            
            search_field2 = search_field2.join (search_field_second2, lsuffix = '_1', rsuffix = '_2')
            search_field_receiver2 = search_field_receiver2.join (search_field_ball2_2, lsuffix = '_3', rsuffix = '_4')
            
            search_field2 = search_field2.join (search_field_receiver2)
            
            Difference2 = []
            
            for index, frame in search_field2.iterrows ():
                # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
                # (Differnece Player to Ball *10) + (Difference Player & Ball to Origin of Event*1) + (Difference of Receiever to Ball 1 Sec after Pass)
                difference2 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_penultimate['X-Position'])) + (abs(frame['Y_1'] - action_penultimate['Y-Position']))) + ((abs(frame['X_2'] - action_penultimate['X-Position'])) + (abs(frame['Y_2'] - action_penultimate['Y-Position'])))).item()  + ((abs(frame['X_3'] - frame['X_4'])) + (abs(frame['Y_3'] - frame['Y_4'])))   ) /22)**2
                Difference2.append (difference2)
            
            search_field2 ['difference'] = Difference2
            identified_frame2 = search_field2[search_field2['difference'] == search_field2 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            identified_frames2 = position_data[position_data['T_sec'] == identified_frame2]
            
        else:
            #First Player
            search_field2 = position_data[position_data['PersonId'] == (action_penultimate.Player.item ())]
            search_field2 = search_field2[(search_field2['T_sec'] >= start_sync2) &
                                          (search_field2['T_sec'] <= end_sync2)]
            
            #Ball
            search_field_second2 = position_data[position_data['TeamId'] == 'BALL']
            search_field_second2 = search_field_second2[(search_field_second2['T_sec'] >= start_sync2) &
                                                        (search_field_second2['T_sec'] <= end_sync2)]
            
            search_field2 = search_field2.reset_index ()
            search_field2 = search_field2.loc [0:399]
    
            search_field_second2 = search_field_second2.reset_index ()
            search_field_second2 = search_field_second2.loc [0:399]
            
            search_field2 = search_field2.join (search_field_second2, lsuffix = '_1', rsuffix = '_2')
            
            Difference2 = []
            for index, frame in search_field2.iterrows ():
                # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
                difference2 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_penultimate['X-Position'])) + (abs(frame['Y_1'] - action_penultimate['Y-Position']))) + ((abs(frame['X_2'] - action_penultimate['X-Position'])) + (abs(frame['Y_2'] - action_penultimate['Y-Position'])))).item()) /21)**2
                
                Difference2.append (difference2)
        
            search_field2 ['difference'] = Difference2
            identified_frame2 = search_field2[search_field2['difference'] == search_field2 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            identified_frames2 = position_data[position_data['T_sec'] == identified_frame2]
    
        #Measurement of defensive pressure penultimate action
        
    #Case 1: Team1 is in ball possession and plays from left to right
    if length >= 2 and attack.team == team1 and attack.TeamLeft == team1:
        #Identification of ball leading player
        if action_penultimate.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames2[identified_frames2['PersonId'] == action_penultimate.Winner.item ()]
        else:
            ball_leader = identified_frames2[identified_frames2['PersonId'] == action_penultimate.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames2[identified_frames2['TeamId'] == team2]

        
#Identification of all attackers sorted after distance to ball
#Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames2[identified_frames2['TeamId'] == team1]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)
    
        possible_attackers['DistanceToBall'] = Dis
    
        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
        
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
            
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
            
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 105, 34)
            Press_onball.append (press_onball)
                
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 105, 34)
            Press_ongroup1.append (press_ongroup1)
                
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 105, 34)
            Press_ongroup2.append (press_ongroup2)
                
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 105, 34)
            Press_ongroup3.append (press_ongroup3)
                
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 105, 34)
            Press_ongroup4.append (press_ongroup4)
                
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 105, 34)
            Press_ongroup5.append (press_ongroup5)
                
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 105, 34)
            Press_ongroup6.append (press_ongroup6)
                
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 105, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 105, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 105, 34)
            Press_ongroup9.append (press_ongroup9)
                
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 105, 34)
            Press_ongroup10.append (press_ongroup10)
                
                
        onballpressure_penultimateaction = max (Press_onball)
        ongrouppressure1_penultimateaction = max (Press_ongroup1)
        ongrouppressure2_penultimateaction = max (Press_ongroup2)
        ongrouppressure3_penultimateaction = max (Press_ongroup3)
        ongrouppressure4_penultimateaction = max (Press_ongroup4)
        ongrouppressure5_penultimateaction = max (Press_ongroup5)
        ongrouppressure6_penultimateaction = max (Press_ongroup6)
        ongrouppressure7_penultimateaction = max (Press_ongroup7)
        ongrouppressure8_penultimateaction = max (Press_ongroup8)
        ongrouppressure9_penultimateaction = max (Press_ongroup9)
        ongrouppressure10_penultimateaction = max (Press_ongroup10)
            
            
#Case 2: Team1 is in ball possession and plays from right to left      
    elif length >= 2 and attack.team == team1 and attack.TeamRight == team1:
        #Identification of ball leading player
        if action_penultimate.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames2[identified_frames2['PersonId'] == action_penultimate.Winner.item ()]
        else:
            ball_leader = identified_frames2[identified_frames2['PersonId'] == action_penultimate.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames2[identified_frames2['TeamId'] == team2]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames2[identified_frames2['TeamId'] == team1]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 0, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 0, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 0, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 0, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 0, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 0, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 0, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 0, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 0, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 0, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 0, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_penultimateaction = max (Press_onball)
        ongrouppressure1_penultimateaction = max (Press_ongroup1)
        ongrouppressure2_penultimateaction = max (Press_ongroup2)
        ongrouppressure3_penultimateaction = max (Press_ongroup3)
        ongrouppressure4_penultimateaction = max (Press_ongroup4)
        ongrouppressure5_penultimateaction = max (Press_ongroup5)
        ongrouppressure6_penultimateaction = max (Press_ongroup6)
        ongrouppressure7_penultimateaction = max (Press_ongroup7)
        ongrouppressure8_penultimateaction = max (Press_ongroup8)
        ongrouppressure9_penultimateaction = max (Press_ongroup9)
        ongrouppressure10_penultimateaction = max (Press_ongroup10)
        
#Case 3: Team2 is in ball possession and plays from left to right         
    elif length >= 2 and attack.team == team2 and attack.TeamLeft == team2:
        #Identification of ball leading player
        if action_penultimate.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames2[identified_frames2['PersonId'] == action_penultimate.Winner.item ()]
        else:
            ball_leader = identified_frames2[identified_frames2['PersonId'] == action_penultimate.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames2[identified_frames2['TeamId'] == team1]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames2[identified_frames2['TeamId'] == team2]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 105, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 105, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 105, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 105, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 105, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 105, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 105, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 105, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 105, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 105, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 105, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_penultimateaction = max (Press_onball)
        ongrouppressure1_penultimateaction = max (Press_ongroup1)
        ongrouppressure2_penultimateaction = max (Press_ongroup2)
        ongrouppressure3_penultimateaction = max (Press_ongroup3)
        ongrouppressure4_penultimateaction = max (Press_ongroup4)
        ongrouppressure5_penultimateaction = max (Press_ongroup5)
        ongrouppressure6_penultimateaction = max (Press_ongroup6)
        ongrouppressure7_penultimateaction = max (Press_ongroup7)
        ongrouppressure8_penultimateaction = max (Press_ongroup8)
        ongrouppressure9_penultimateaction = max (Press_ongroup9)
        ongrouppressure10_penultimateaction = max (Press_ongroup10)
        
#Case 4: Team2 is in ball possession and plays from right to left       
    elif length >= 2 and attack.team == team2 and attack.TeamRight == team2:
        #Identification of ball leading player
        if action_penultimate.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames2[identified_frames2['PersonId'] == action_penultimate.Winner.item ()]
        else:
            ball_leader = identified_frames2[identified_frames2['PersonId'] == action_penultimate.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames2[identified_frames2['TeamId'] == team1]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames2[identified_frames2['TeamId'] == team2]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 0, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 0, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 0, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 0, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 0, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 0, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 0, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 0, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 0, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 0, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 0, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_penultimateaction = max (Press_onball)
        ongrouppressure1_penultimateaction = max (Press_ongroup1)
        ongrouppressure2_penultimateaction = max (Press_ongroup2)
        ongrouppressure3_penultimateaction = max (Press_ongroup3)
        ongrouppressure4_penultimateaction = max (Press_ongroup4)
        ongrouppressure5_penultimateaction = max (Press_ongroup5)
        ongrouppressure6_penultimateaction = max (Press_ongroup6)
        ongrouppressure7_penultimateaction = max (Press_ongroup7)
        ongrouppressure8_penultimateaction = max (Press_ongroup8)
        ongrouppressure9_penultimateaction = max (Press_ongroup9)
        ongrouppressure10_penultimateaction = max (Press_ongroup10)

    else:
        onballpressure_penultimateaction = None
        ongrouppressure1_penultimateaction = None
        ongrouppressure2_penultimateaction = None
        ongrouppressure3_penultimateaction = None
        ongrouppressure4_penultimateaction = None
        ongrouppressure5_penultimateaction = None
        ongrouppressure6_penultimateaction = None
        ongrouppressure7_penultimateaction = None
        ongrouppressure8_penultimateaction = None
        ongrouppressure9_penultimateaction = None
        ongrouppressure10_penultimateaction = None
        
        identified_frame2 = None
    
    OnBallPressure_PenultimateAction.append (onballpressure_penultimateaction)
    OnGroupPressure1_PenultimateAction.append (ongrouppressure1_penultimateaction)
    OnGroupPressure2_PenultimateAction.append (ongrouppressure2_penultimateaction)
    OnGroupPressure3_PenultimateAction.append (ongrouppressure3_penultimateaction)
    OnGroupPressure4_PenultimateAction.append (ongrouppressure4_penultimateaction)
    OnGroupPressure5_PenultimateAction.append (ongrouppressure5_penultimateaction)
    OnGroupPressure6_PenultimateAction.append (ongrouppressure6_penultimateaction)
    OnGroupPressure7_PenultimateAction.append (ongrouppressure7_penultimateaction)
    OnGroupPressure8_PenultimateAction.append (ongrouppressure8_penultimateaction)
    OnGroupPressure9_PenultimateAction.append (ongrouppressure9_penultimateaction)
    OnGroupPressure10_PenultimateAction.append (ongrouppressure10_penultimateaction)

    frame_penultimateaction.append (identified_frame2)
#%%     
#Measurement of defensive pressure for thridlast action of attack   
OnBallPressure_ThirdlastAction = []
OnGroupPressure1_ThirdlastAction = []
OnGroupPressure2_ThirdlastAction = []
OnGroupPressure3_ThirdlastAction = []
OnGroupPressure4_ThirdlastAction = []
OnGroupPressure5_ThirdlastAction = []
OnGroupPressure6_ThirdlastAction = []
OnGroupPressure7_ThirdlastAction = []
OnGroupPressure8_ThirdlastAction = []
OnGroupPressure9_ThirdlastAction = []
OnGroupPressure10_ThirdlastAction = [] 

frame_thirdlastaction = []

for row, attack in possessions.iterrows ():
    actions = event_data[(event_data['EventTime'] >= attack.start) &
                         (event_data['EventTime'] <= attack.end)]

    
    #find all ball actions in the possession that have value for the study:
    ball_actions = ['Play', 'OtherBallAction', 'TacklingGame', 'BallClaiming', 'FreeKick', 'ThrowIn', 'ShotAtGoal', 'CornerKick', 'GoalKick', 'KickOff']
    actions = actions[(actions['Event1'] == 'Play') |
                      (actions['Event2'] == 'Play') ]
    
    actions = actions.reset_index ()
    length = len (actions)
    
    # Thirdlast action
    
    if length >= 3:
        action_thirdlast = actions.loc [[(length-3)]]
      
        #Find right frame of position data of this action (Snchronization of Event & Position data)
        start_sync3 = (((action_thirdlast.EventTime.item().hour)*60)*60) + ((action_thirdlast.EventTime.item ().minute)*60) + (action_thirdlast.EventTime.item().second) + ((action_thirdlast.EventTime.item ().microsecond)/1000000)  - 8
        end_sync3 = (((action_thirdlast.EventTime.item().hour)*60)*60) + ((action_thirdlast.EventTime.item ().minute)*60) + (action_thirdlast.EventTime.item().second) + ((action_thirdlast.EventTime.item ().microsecond)/1000000)  + 8
    
        if action_thirdlast.Event1.item () == 'TacklingGame':
            #First Player
            search_field3 = position_data[position_data['PersonId'] == (action_thirdlast.Winner.item ())]
            search_field3 = search_field3[(search_field3['T_sec'] >= start_sync3) &
                                          (search_field3['T_sec'] <= end_sync3)]
            #Second Player
            search_field_second3 = position_data[position_data['PersonId'] == (action_thirdlast.Loser.item ())]
            search_field_second3 = search_field_second3[(search_field_second3['T_sec'] >= start_sync3) &
                                                        (search_field_second3['T_sec'] <= end_sync3)]
            
            search_field3 = search_field3.reset_index ()
            search_field3 = search_field3.loc [0:399]
    
            search_field_second3 = search_field_second3.reset_index ()
            search_field_second3 = search_field_second3.loc [0:399]
            
            search_field3 = search_field3.join (search_field_second3, lsuffix = '_1', rsuffix = '_2')
            
            Difference3 = []
            for index, frame in search_field3.iterrows ():
                # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
                difference3 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_thirdlast['X-Position'])) + (abs(frame['Y_1'] - action_thirdlast['Y-Position']))) + ((abs(frame['X_2'] - action_thirdlast['X-Position'])) + (abs(frame['Y_2'] - action_thirdlast['Y-Position'])))).item()) /21)**2
                
                Difference3.append (difference3)
        
            search_field3 ['difference'] = Difference3
            identified_frame3 = search_field3[search_field3['difference'] == search_field3 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            identified_frames3 = position_data[position_data['T_sec'] == identified_frame3]

        elif action_thirdlast.Recipient.isnull ().item() == False and (action_thirdlast.Event1.item () == 'Play' or action_thirdlast.Event2.item () == 'Play'):
            #First Player
            search_field3 = position_data[position_data['PersonId'] == (action_thirdlast.Player.item ())]
            search_field3 = search_field3[(search_field3['T_sec'] >= start_sync3) &
                                          (search_field3['T_sec'] <= end_sync3)]
            
            #Ball
            search_field_second3 = position_data[position_data['TeamId'] == 'BALL']
            search_field_second3 = search_field_second3[(search_field_second3['T_sec'] >= start_sync3) &
                                                        (search_field_second3['T_sec'] <= end_sync3)]
            #Reciever with 1 sec plus
            search_field_receiver3 = position_data[position_data['PersonId'] == (action_thirdlast.Recipient.item ())]
            search_field_receiver3 = search_field_receiver3[(search_field_receiver3['T_sec'] >= (start_sync3 + 1)) &
                                                          (search_field_receiver3['T_sec'] <= (end_sync3 + 1))]
            
            #Ball with 1 sec plus
            search_field_ball2_3 = position_data[position_data['TeamId'] == 'BALL']
            search_field_ball2_3= search_field_ball2_3[(search_field_ball2_3['T_sec'] >= (start_sync3 + 1)) &
                                                        (search_field_ball2_3['T_sec'] <= (end_sync3 + 1))]
            
            search_field3 = search_field3.reset_index ()
            search_field3 = search_field3.loc [0:399]
    
            search_field_second3 = search_field_second3.reset_index ()
            search_field_second3 = search_field_second3.loc [0:399]
            
            search_field_receiver3 = search_field_receiver3.reset_index ()
            search_field_receiver3 = search_field_receiver3.loc [0:399]
            
            search_field_ball2_3 = search_field_ball2_3.reset_index ()
            search_field_ball2_3 = search_field_ball2_3.loc [0:399]
            
            search_field3 = search_field3.join (search_field_second3, lsuffix = '_1', rsuffix = '_2')
            search_field_receiver3 = search_field_receiver3.join (search_field_ball2_3, lsuffix = '_3', rsuffix = '_4')
            
            search_field3 = search_field3.join (search_field_receiver3)
            
            Difference3 = []
            
            for index, frame in search_field3.iterrows ():
                # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
                # (Differnece Player to Ball *10) + (Difference Player & Ball to Origin of Event*1) + (Difference of Receiever to Ball 1 Sec after Pass)
                difference3 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_thirdlast['X-Position'])) + (abs(frame['Y_1'] - action_thirdlast['Y-Position']))) + ((abs(frame['X_2'] - action_thirdlast['X-Position'])) + (abs(frame['Y_2'] - action_thirdlast['Y-Position'])))).item()  + ((abs(frame['X_3'] - frame['X_4'])) + (abs(frame['Y_3'] - frame['Y_4'])))   ) /22)**2
                Difference3.append (difference3)
            
            search_field3 ['difference'] = Difference3
            identified_frame3 = search_field3[search_field3['difference'] == search_field3 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            identified_frames3 = position_data[position_data['T_sec'] == identified_frame3]
            
        else:
            #First Player
            search_field3 = position_data[position_data['PersonId'] == (action_thirdlast.Player.item ())]
            search_field3 = search_field3[(search_field3['T_sec'] >= start_sync3) &
                                          (search_field3['T_sec'] <= end_sync3)]
            
            #Ball
            search_field_second3 = position_data[position_data['TeamId'] == 'BALL']
            search_field_second3 = search_field_second3[(search_field_second3['T_sec'] >= start_sync3) &
                                                        (search_field_second3['T_sec'] <= end_sync3)]
            
            search_field3 = search_field3.reset_index ()
            search_field3 = search_field3.loc [0:399]
    
            search_field_second3 = search_field_second3.reset_index ()
            search_field_second3 = search_field_second3.loc [0:399]
            
            search_field3 = search_field3.join (search_field_second3, lsuffix = '_1', rsuffix = '_2')
            
            Difference3 = []
            for index, frame in search_field3.iterrows ():
                # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
                difference3 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_thirdlast['X-Position'])) + (abs(frame['Y_1'] - action_thirdlast['Y-Position']))) + ((abs(frame['X_2'] - action_thirdlast['X-Position'])) + (abs(frame['Y_2'] - action_thirdlast['Y-Position'])))).item()) /21)**2
                
                Difference3.append (difference3)
        
            search_field3 ['difference'] = Difference3
            identified_frame3 = search_field3[search_field3['difference'] == search_field3 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            identified_frames3 = position_data[position_data['T_sec'] == identified_frame3]

    
#Measurement of defensive pressure thirdlast action

#Case 1: Team1 is in ball possession and plays from left to right
    if length >= 3 and attack.team == team1 and attack.TeamLeft == team1:
        #Identification of ball leading player
        if action_thirdlast.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames3[identified_frames3['PersonId'] == action_thirdlast.Winner.item ()]
        else:
            ball_leader = identified_frames3[identified_frames3['PersonId'] == action_thirdlast.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames3[identified_frames3['TeamId'] == team2]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames3[identified_frames3['TeamId'] == team1]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 105, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 105, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 105, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 105, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 105, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 105, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 105, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 105, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 105, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 105, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 105, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_thirdlastaction = max (Press_onball)
        ongrouppressure1_thirdlastaction = max (Press_ongroup1)
        ongrouppressure2_thirdlastaction = max (Press_ongroup2)
        ongrouppressure3_thirdlastaction = max (Press_ongroup3)
        ongrouppressure4_thirdlastaction = max (Press_ongroup4)
        ongrouppressure5_thirdlastaction = max (Press_ongroup5)
        ongrouppressure6_thirdlastaction = max (Press_ongroup6)
        ongrouppressure7_thirdlastaction = max (Press_ongroup7)
        ongrouppressure8_thirdlastaction = max (Press_ongroup8)
        ongrouppressure9_thirdlastaction = max (Press_ongroup9)
        ongrouppressure10_thirdlastaction = max (Press_ongroup10)
        
        
#Case 2: Team1 is in ball possession and plays from right to left      
    elif length >= 3 and attack.team == team1 and attack.TeamRight == team1:
        #Identification of ball leading player
        if action_thirdlast.Event1.item() == 'TacklingGame':
            ball_leader = identified_frames3[identified_frames3['PersonId'] == action_thirdlast.Winner.item ()]
        else:
            ball_leader = identified_frames3[identified_frames3['PersonId'] == action_thirdlast.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames3[identified_frames3['TeamId'] == team2]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames3[identified_frames3['TeamId'] == team1]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 0, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 0, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 0, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 0, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 0, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 0, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 0, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 0, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 0, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 0, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 0, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_thirdlastaction = max (Press_onball)
        ongrouppressure1_thirdlastaction = max (Press_ongroup1)
        ongrouppressure2_thirdlastaction = max (Press_ongroup2)
        ongrouppressure3_thirdlastaction = max (Press_ongroup3)
        ongrouppressure4_thirdlastaction = max (Press_ongroup4)
        ongrouppressure5_thirdlastaction = max (Press_ongroup5)
        ongrouppressure6_thirdlastaction = max (Press_ongroup6)
        ongrouppressure7_thirdlastaction = max (Press_ongroup7)
        ongrouppressure8_thirdlastaction = max (Press_ongroup8)
        ongrouppressure9_thirdlastaction = max (Press_ongroup9)
        ongrouppressure10_thirdlastaction = max (Press_ongroup10)
        
#Case 3: Team2 is in ball possession and plays from left to right         
    elif length >= 3 and attack.team == team2 and attack.TeamLeft == team2:
        #Identification of ball leading player
        if action_thirdlast.Event1.item() == 'TacklingGame':
            ball_leader = identified_frames3[identified_frames3['PersonId'] == action_thirdlast.Winner.item ()]
        else:
            ball_leader = identified_frames3[identified_frames3['PersonId'] == action_thirdlast.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames3[identified_frames3['TeamId'] == team1]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames3[identified_frames3['TeamId'] == team2]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 105, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 105, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 105, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 105, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 105, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 105, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 105, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 105, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 105, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 105, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 105, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_thirdlastaction = max (Press_onball)
        ongrouppressure1_thirdlastaction = max (Press_ongroup1)
        ongrouppressure2_thirdlastaction = max (Press_ongroup2)
        ongrouppressure3_thirdlastaction = max (Press_ongroup3)
        ongrouppressure4_thirdlastaction = max (Press_ongroup4)
        ongrouppressure5_thirdlastaction = max (Press_ongroup5)
        ongrouppressure6_thirdlastaction = max (Press_ongroup6)
        ongrouppressure7_thirdlastaction = max (Press_ongroup7)
        ongrouppressure8_thirdlastaction = max (Press_ongroup8)
        ongrouppressure9_thirdlastaction = max (Press_ongroup9)
        ongrouppressure10_thirdlastaction = max (Press_ongroup10)
        
#Case 4: Team2 is in ball possession and plays from right to left       
    elif length >= 3 and attack.team == team2 and attack.TeamRight == team2:
        #Identification of ball leading player
        if action_thirdlast.Event1.item() == 'TacklingGame':
            ball_leader = identified_frames3[identified_frames3['PersonId'] == action_thirdlast.Winner.item ()]
        else:
            ball_leader = identified_frames3[identified_frames3['PersonId'] == action_thirdlast.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames3[identified_frames3['TeamId'] == team1]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames3[identified_frames3['TeamId'] == team2]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 0, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 0, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 0, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 0, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 0, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 0, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 0, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 0, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 0, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 0, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 0, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_thirdlastaction = max (Press_onball)
        ongrouppressure1_thirdlastaction = max (Press_ongroup1)
        ongrouppressure2_thirdlastaction = max (Press_ongroup2)
        ongrouppressure3_thirdlastaction = max (Press_ongroup3)
        ongrouppressure4_thirdlastaction = max (Press_ongroup4)
        ongrouppressure5_thirdlastaction = max (Press_ongroup5)
        ongrouppressure6_thirdlastaction = max (Press_ongroup6)
        ongrouppressure7_thirdlastaction = max (Press_ongroup7)
        ongrouppressure8_thirdlastaction = max (Press_ongroup8)
        ongrouppressure9_thirdlastaction = max (Press_ongroup9)
        ongrouppressure10_thirdlastaction = max (Press_ongroup10)


    else:
        onballpressure_thirdlastaction = None
        ongrouppressure1_thirdlastaction = None
        ongrouppressure2_thirdlastaction = None
        ongrouppressure3_thirdlastaction = None
        ongrouppressure4_thirdlastaction = None
        ongrouppressure5_thirdlastaction = None
        ongrouppressure6_thirdlastaction = None
        ongrouppressure7_thirdlastaction = None
        ongrouppressure8_thirdlastaction = None
        ongrouppressure9_thirdlastaction = None
        ongrouppressure10_thirdlastaction = None
        
        identified_frame3 = None


    OnBallPressure_ThirdlastAction.append (onballpressure_thirdlastaction)
    OnGroupPressure1_ThirdlastAction.append (ongrouppressure1_thirdlastaction)
    OnGroupPressure2_ThirdlastAction.append (ongrouppressure2_thirdlastaction)
    OnGroupPressure3_ThirdlastAction.append (ongrouppressure3_thirdlastaction)
    OnGroupPressure4_ThirdlastAction.append (ongrouppressure4_thirdlastaction)
    OnGroupPressure5_ThirdlastAction.append (ongrouppressure5_thirdlastaction)
    OnGroupPressure6_ThirdlastAction.append (ongrouppressure6_thirdlastaction)
    OnGroupPressure7_ThirdlastAction.append (ongrouppressure7_thirdlastaction)
    OnGroupPressure8_ThirdlastAction.append (ongrouppressure8_thirdlastaction)
    OnGroupPressure9_ThirdlastAction.append (ongrouppressure9_thirdlastaction)
    OnGroupPressure10_ThirdlastAction.append (ongrouppressure10_thirdlastaction)

    frame_thirdlastaction.append (identified_frame3)
#%%
#Measurement of defensive pressure for fourthlast action of attack


OnBallPressure_FourthlastAction = []
OnGroupPressure1_FourthlastAction = []
OnGroupPressure2_FourthlastAction = []
OnGroupPressure3_FourthlastAction = []
OnGroupPressure4_FourthlastAction = []
OnGroupPressure5_FourthlastAction = []
OnGroupPressure6_FourthlastAction = []
OnGroupPressure7_FourthlastAction = []
OnGroupPressure8_FourthlastAction = []
OnGroupPressure9_FourthlastAction = []
OnGroupPressure10_FourthlastAction = []

frame_fourthlastaction = []

for row, attack in possessions.iterrows ():
    actions = event_data[(event_data['EventTime'] >= attack.start) &
                         (event_data['EventTime'] <= attack.end)]

    
    #find all ball actions in the possession that have value for the study:
    ball_actions = ['Play', 'OtherBallAction', 'TacklingGame', 'BallClaiming', 'FreeKick', 'ThrowIn', 'ShotAtGoal', 'CornerKick', 'GoalKick', 'KickOff']
    actions = actions[(actions['Event1'] == 'Play') |
                      (actions['Event2'] == 'Play') ]
    
    actions = actions.reset_index ()
    length = len (actions)


    if length >= 4:
        action_fourthlast = actions.loc [[(length-4)]]

        #Find right frame of position data of this action (Snchronization of Event & Position data)
        start_sync4 = (((action_fourthlast.EventTime.item().hour)*60)*60) + ((action_fourthlast.EventTime.item ().minute)*60) + (action_fourthlast.EventTime.item().second) + ((action_fourthlast.EventTime.item ().microsecond)/1000000)  - 8
        end_sync4 = (((action_fourthlast.EventTime.item().hour)*60)*60) + ((action_fourthlast.EventTime.item ().minute)*60) + (action_fourthlast.EventTime.item().second) + ((action_fourthlast.EventTime.item ().microsecond)/1000000)  + 8
    
        if action_fourthlast.Event1.item () == 'TacklingGame':
            #First Player
            search_field4 = position_data[position_data['PersonId'] == (action_fourthlast.Winner.item ())]
            search_field4 = search_field4[(search_field4['T_sec'] >= start_sync4) &
                                          (search_field4['T_sec'] <= end_sync4)]
            #Second Player
            search_field_second4 = position_data[position_data['PersonId'] == (action_fourthlast.Loser.item ())]
            search_field_second4 = search_field_second4[(search_field_second4['T_sec'] >= start_sync4) &
                                                        (search_field_second4['T_sec'] <= end_sync4)]
            
            search_field4 = search_field4.reset_index ()
            search_field4 = search_field4.loc [0:399]
    
            search_field_second4 = search_field_second4.reset_index ()
            search_field_second4 = search_field_second4.loc [0:399]
            
            search_field4 = search_field4.join (search_field_second4, lsuffix = '_1', rsuffix = '_2')
            
            Difference4 = []
            for index, frame in search_field4.iterrows ():
                # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
                difference4 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_fourthlast['X-Position'])) + (abs(frame['Y_1'] - action_fourthlast['Y-Position']))) + ((abs(frame['X_2'] - action_fourthlast['X-Position'])) + (abs(frame['Y_2'] - action_fourthlast['Y-Position'])))).item()) /21)**2
                
                Difference4.append (difference4)
        
            search_field4 ['difference'] = Difference4
            identified_frame4 = search_field4[search_field4['difference'] == search_field4 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            identified_frames4 = position_data[position_data['T_sec'] == identified_frame4]
            
        elif action_fourthlast.Recipient.isnull ().item() == False and (action_fourthlast.Event1.item () == 'Play' or action_fourthlast.Event2.item () == 'Play'):
            #First Player
            search_field4 = position_data[position_data['PersonId'] == (action_fourthlast.Player.item ())]
            search_field4 = search_field4[(search_field4['T_sec'] >= start_sync4) &
                                          (search_field4['T_sec'] <= end_sync4)]
            
            #Ball
            search_field_second4 = position_data[position_data['TeamId'] == 'BALL']
            search_field_second4 = search_field_second4[(search_field_second4['T_sec'] >= start_sync4) &
                                                        (search_field_second4['T_sec'] <= end_sync4)]
            #Reciever with 1 sec plus
            search_field_receiver4 = position_data[position_data['PersonId'] == (action_fourthlast.Recipient.item ())]
            search_field_receiver4 = search_field_receiver4[(search_field_receiver4['T_sec'] >= (start_sync4 + 1)) &
                                                          (search_field_receiver4['T_sec'] <= (end_sync4 + 1))]
            
            #Ball with 1 sec plus
            search_field_ball2_4 = position_data[position_data['TeamId'] == 'BALL']
            search_field_ball2_4 = search_field_ball2_4[(search_field_ball2_4['T_sec'] >= (start_sync4 + 1)) &
                                                        (search_field_ball2_4['T_sec'] <= (end_sync4 + 1))]
            search_field4 = search_field4.reset_index ()
            search_field4 = search_field4.loc [0:399]
        
            search_field_second4 = search_field_second4.reset_index ()
            search_field_second4 = search_field_second4.loc [0:399]
            
            search_field_receiver4 = search_field_receiver4.reset_index ()
            search_field_receiver4 = search_field_receiver4.loc [0:399]
            
            search_field_ball2_4 = search_field_ball2_4.reset_index ()
            search_field_ball2_4 = search_field_ball2_4.loc [0:399]
            
            search_field4 = search_field4.join (search_field_second4, lsuffix = '_1', rsuffix = '_2')
            search_field_receiver4 = search_field_receiver4.join (search_field_ball2_4, lsuffix = '_3', rsuffix = '_4')
            
            search_field4 = search_field4.join (search_field_receiver4)
            
            Difference4 = []
            for index, frame in search_field4.iterrows ():
                # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
                # (Differnece Player to Ball *10) + (Difference Player & Ball to Origin of Event*1) + (Difference of Receiever to Ball 1 Sec after Pass)
                difference4 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_fourthlast['X-Position'])) + (abs(frame['Y_1'] - action_fourthlast['Y-Position']))) + ((abs(frame['X_2'] - action_fourthlast['X-Position'])) + (abs(frame['Y_2'] - action_fourthlast['Y-Position'])))).item()  + ((abs(frame['X_3'] - frame['X_4'])) + (abs(frame['Y_3'] - frame['Y_4'])))   ) /22)**2
                Difference4.append (difference4)
                
            search_field4 ['difference'] = Difference4
            identified_frame4 = search_field4[search_field4['difference'] == search_field4 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            identified_frames4 = position_data[position_data['T_sec'] == identified_frame4]
            
        else:
            #First Player
            search_field4 = position_data[position_data['PersonId'] == (action_fourthlast.Player.item ())]
            search_field4 = search_field4[(search_field4['T_sec'] >= start_sync4) &
                                          (search_field4['T_sec'] <= end_sync4)]
            
            #Ball
            search_field_second4 = position_data[position_data['TeamId'] == 'BALL']
            search_field_second4 = search_field_second4[(search_field_second4['T_sec'] >= start_sync4) &
                                                        (search_field_second4['T_sec'] <= end_sync4)]
            
            search_field4 = search_field4.reset_index ()
            search_field4 = search_field4.loc [0:399]
    
            search_field_second4 = search_field_second4.reset_index ()
            search_field_second4 = search_field_second4.loc [0:399]
            
            search_field4 = search_field4.join (search_field_second4, lsuffix = '_1', rsuffix = '_2')
            
            Difference4 = []
            for index, frame in search_field4.iterrows ():
                # Difference of player 1 and player2 (Ball) is weighted 10 times over difference of player and ball to origin of playing event 
                difference4 = (((((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))*10) + (((abs(frame['X_1'] - action_fourthlast['X-Position'])) + (abs(frame['Y_1'] - action_fourthlast['Y-Position']))) + ((abs(frame['X_2'] - action_fourthlast['X-Position'])) + (abs(frame['Y_2'] - action_fourthlast['Y-Position'])))).item()) /21)**2
                
                Difference4.append (difference4)
        
            search_field4 ['difference'] = Difference4
            identified_frame4 = search_field4[search_field4['difference'] == search_field4 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            identified_frames4 = position_data[position_data['T_sec'] == identified_frame4]
     

#Measurement of defensive pressure fourthlast action


#Case 1: Team1 is in ball possession and plays from left to right
    if length >= 4 and attack.team == team1 and attack.TeamLeft == team1:
        #Identification of ball leading player
        if action_fourthlast.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames4[identified_frames4['PersonId'] == action_fourthlast.Winner.item ()]
        else:
            ball_leader = identified_frames4[identified_frames4['PersonId'] == action_fourthlast.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames4[identified_frames4['TeamId'] == team2]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames4[identified_frames4['TeamId'] == team1]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 105, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 105, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 105, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 105, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 105, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 105, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 105, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 105, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 105, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 105, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 105, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_fourthlastaction = max (Press_onball)
        ongrouppressure1_fourthlastaction = max (Press_ongroup1)
        ongrouppressure2_fourthlastaction = max (Press_ongroup2)
        ongrouppressure3_fourthlastaction = max (Press_ongroup3)
        ongrouppressure4_fourthlastaction = max (Press_ongroup4)
        ongrouppressure5_fourthlastaction = max (Press_ongroup5)
        ongrouppressure6_fourthlastaction = max (Press_ongroup6)
        ongrouppressure7_fourthlastaction = max (Press_ongroup7)
        ongrouppressure8_fourthlastaction = max (Press_ongroup8)
        ongrouppressure9_fourthlastaction = max (Press_ongroup9)
        ongrouppressure10_fourthlastaction = max (Press_ongroup10)
        
        
#Case 2: Team1 is in ball possession and plays from right to left      
    elif length >= 4 and attack.team == team1 and attack.TeamRight == team1:
        #Identification of ball leading player
        if action_fourthlast.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames4[identified_frames4['PersonId'] == action_fourthlast.Winner.item ()]
        else:
            ball_leader = identified_frames4[identified_frames4['PersonId'] == action_fourthlast.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames4[identified_frames4['TeamId'] == team2]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames4[identified_frames4['TeamId'] == team1]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 0, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 0, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 0, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 0, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 0, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 0, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 0, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 0, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 0, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 0, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 0, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_fourthlastaction = max (Press_onball)
        ongrouppressure1_fourthlastaction = max (Press_ongroup1)
        ongrouppressure2_fourthlastaction = max (Press_ongroup2)
        ongrouppressure3_fourthlastaction = max (Press_ongroup3)
        ongrouppressure4_fourthlastaction = max (Press_ongroup4)
        ongrouppressure5_fourthlastaction = max (Press_ongroup5)
        ongrouppressure6_fourthlastaction = max (Press_ongroup6)
        ongrouppressure7_fourthlastaction = max (Press_ongroup7)
        ongrouppressure8_fourthlastaction = max (Press_ongroup8)
        ongrouppressure9_fourthlastaction = max (Press_ongroup9)
        ongrouppressure10_fourthlastaction = max (Press_ongroup10)
        
#Case 3: Team2 is in ball possession and plays from left to right         
    elif length >= 4 and attack.team == team2 and attack.TeamLeft == team2:
        #Identification of ball leading player
        if action_fourthlast.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames4[identified_frames4['PersonId'] == action_fourthlast.Winner.item ()]
        else:
            ball_leader = identified_frames4[identified_frames4['PersonId'] == action_fourthlast.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames4[identified_frames4['TeamId'] == team1]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames4[identified_frames4['TeamId'] == team2]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 105, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 105, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 105, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 105, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 105, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 105, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 105, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 105, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 105, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 105, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 105, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_fourthlastaction = max (Press_onball)
        ongrouppressure1_fourthlastaction = max (Press_ongroup1)
        ongrouppressure2_fourthlastaction = max (Press_ongroup2)
        ongrouppressure3_fourthlastaction = max (Press_ongroup3)
        ongrouppressure4_fourthlastaction = max (Press_ongroup4)
        ongrouppressure5_fourthlastaction = max (Press_ongroup5)
        ongrouppressure6_fourthlastaction = max (Press_ongroup6)
        ongrouppressure7_fourthlastaction = max (Press_ongroup7)
        ongrouppressure8_fourthlastaction = max (Press_ongroup8)
        ongrouppressure9_fourthlastaction = max (Press_ongroup9)
        ongrouppressure10_fourthlastaction = max (Press_ongroup10)
        
#Case 4: Team2 is in ball possession and plays from right to left       
    elif length >= 4 and attack.team == team2 and attack.TeamRight == team2:
        #Identification of ball leading player
        if action_fourthlast.Event1.item () == 'TacklingGame':
            ball_leader = identified_frames4[identified_frames4['PersonId'] == action_fourthlast.Winner.item ()]
        else:
            ball_leader = identified_frames4[identified_frames4['PersonId'] == action_fourthlast.Player.item ()]
        #Identification of possible defenders
        possible_defenders = identified_frames4[identified_frames4['TeamId'] == team1]

        
        #Identification of all attackers sorted after distance to ball
        #Identifiacation of group level pressure (4 players nearest to the ball)
        possible_attackers = identified_frames4[identified_frames4['TeamId'] == team2]
        Dis = []
        for index2, attacker in possible_attackers.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball_leader['X'].item())**2 + (attack['Y'].item() - ball_leader['Y'].item())**2)
            Dis.append (dis)

        possible_attackers['DistanceToBall'] = Dis

        group_attackers = possible_attackers.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1 = group_attackers.loc[[1]]
        group_attacker2 = group_attackers.loc[[2]]
        group_attacker3 = group_attackers.loc[[3]]
        group_attacker4 = group_attackers.loc[[4]]
        group_attacker5 = group_attackers.loc[[5]]
        group_attacker6 = group_attackers.loc[[6]]
        group_attacker7 = group_attackers.loc[[7]]
        group_attacker8 = group_attackers.loc[[8]]
        group_attacker9 = group_attackers.loc[[9]]
        group_attacker10 = group_attackers.loc[[10]]
        
        #Calculation of pressure 
        Press_onball = []
        Press_ongroup1 = []
        Press_ongroup2 = []
        Press_ongroup3 = []
        Press_ongroup4 = []
        Press_ongroup5 = []
        Press_ongroup6 = []
        Press_ongroup7 = []
        Press_ongroup8 = []
        Press_ongroup9 = []
        Press_ongroup10 = []
        
        for index2, defender in possible_defenders.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (ball_leader, defend, 0, 34)
            Press_onball.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1, defend, 0, 34)
            Press_ongroup1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2, defend, 0, 34)
            Press_ongroup2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3, defend, 0, 34)
            Press_ongroup3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker4, defend, 0, 34)
            Press_ongroup4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker5, defend, 0, 34)
            Press_ongroup5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker6, defend, 0, 34)
            Press_ongroup6.append (press_ongroup6)
            
            press_ongroup7 = pressure_quantification (group_attacker7, defend, 0, 34)
            Press_ongroup7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker8, defend, 0, 34)
            Press_ongroup8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker9, defend, 0, 34)
            Press_ongroup9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker10, defend, 0, 34)
            Press_ongroup10.append (press_ongroup10)
            
            
        onballpressure_fourthlastaction = max (Press_onball)
        ongrouppressure1_fourthlastaction = max (Press_ongroup1)
        ongrouppressure2_fourthlastaction = max (Press_ongroup2)
        ongrouppressure3_fourthlastaction = max (Press_ongroup3)
        ongrouppressure4_fourthlastaction = max (Press_ongroup4)
        ongrouppressure5_fourthlastaction = max (Press_ongroup5)
        ongrouppressure6_fourthlastaction = max (Press_ongroup6)
        ongrouppressure7_fourthlastaction = max (Press_ongroup7)
        ongrouppressure8_fourthlastaction = max (Press_ongroup8)
        ongrouppressure9_fourthlastaction = max (Press_ongroup9)
        ongrouppressure10_fourthlastaction = max (Press_ongroup10)

    else:
        onballpressure_fourthlastaction = None
        ongrouppressure1_fourthlastaction = None
        ongrouppressure2_fourthlastaction = None
        ongrouppressure3_fourthlastaction = None
        ongrouppressure4_fourthlastaction = None
        ongrouppressure5_fourthlastaction = None
        ongrouppressure6_fourthlastaction = None
        ongrouppressure7_fourthlastaction = None
        ongrouppressure8_fourthlastaction = None
        ongrouppressure9_fourthlastaction = None
        ongrouppressure10_fourthlastaction = None
        
        identified_frame4 = None
    
    OnBallPressure_FourthlastAction.append (onballpressure_fourthlastaction)
    OnGroupPressure1_FourthlastAction.append (ongrouppressure1_fourthlastaction)
    OnGroupPressure2_FourthlastAction.append (ongrouppressure2_fourthlastaction)
    OnGroupPressure3_FourthlastAction.append (ongrouppressure3_fourthlastaction)
    OnGroupPressure4_FourthlastAction.append (ongrouppressure4_fourthlastaction)
    OnGroupPressure5_FourthlastAction.append (ongrouppressure5_fourthlastaction)
    OnGroupPressure6_FourthlastAction.append (ongrouppressure6_fourthlastaction)
    OnGroupPressure7_FourthlastAction.append (ongrouppressure7_fourthlastaction)
    OnGroupPressure8_FourthlastAction.append (ongrouppressure8_fourthlastaction)
    OnGroupPressure9_FourthlastAction.append (ongrouppressure9_fourthlastaction)
    OnGroupPressure10_FourthlastAction.append (ongrouppressure10_fourthlastaction)
    
    frame_fourthlastaction.append (identified_frame4)
#%%
possessions['OnBallPressure_LastAction'] = OnBallPressure_LastAction
possessions['OnGroupPressure1_LastAction'] = OnGroupPressure1_LastAction
possessions['OnGroupPressure2_LastAction'] = OnGroupPressure2_LastAction
possessions['OnGroupPressure3_LastAction'] = OnGroupPressure3_LastAction
possessions['OnGroupPressure4_LastAction'] = OnGroupPressure4_LastAction
possessions['OnGroupPressure5_LastAction'] = OnGroupPressure5_LastAction
possessions['OnGroupPressure6_LastAction'] = OnGroupPressure6_LastAction
possessions['OnGroupPressure7_LastAction'] = OnGroupPressure7_LastAction
possessions['OnGroupPressure8_LastAction'] = OnGroupPressure8_LastAction
possessions['OnGroupPressure9_LastAction'] = OnGroupPressure9_LastAction
possessions['OnGroupPressure10_LastAction'] = OnGroupPressure10_LastAction

possessions['OnBallPressure_PenultimateAction'] = OnBallPressure_PenultimateAction
possessions['OnGroupPressure1_PenultimateAction'] = OnGroupPressure1_PenultimateAction
possessions['OnGroupPressure2_PenultimateAction'] = OnGroupPressure2_PenultimateAction
possessions['OnGroupPressure3_PenultimateAction'] = OnGroupPressure3_PenultimateAction
possessions['OnGroupPressure4_PenultimateAction'] = OnGroupPressure4_PenultimateAction
possessions['OnGroupPressure5_PenultimateAction'] = OnGroupPressure5_PenultimateAction
possessions['OnGroupPressure6_PenultimateAction'] = OnGroupPressure6_PenultimateAction
possessions['OnGroupPressure7_PenultimateAction'] = OnGroupPressure7_PenultimateAction
possessions['OnGroupPressure8_PenultimateAction'] = OnGroupPressure8_PenultimateAction
possessions['OnGroupPressure9_PenultimateAction'] = OnGroupPressure9_PenultimateAction
possessions['OnGroupPressure10_PenultimateAction'] = OnGroupPressure10_PenultimateAction

possessions['OnBallPressure_ThirdlastAction'] = OnBallPressure_ThirdlastAction
possessions['OnGroupPressure1_ThirdlastAction'] = OnGroupPressure1_ThirdlastAction
possessions['OnGroupPressure2_ThirdlastAction'] = OnGroupPressure2_ThirdlastAction
possessions['OnGroupPressure3_ThirdlastAction'] = OnGroupPressure3_ThirdlastAction
possessions['OnGroupPressure4_ThirdlastAction'] = OnGroupPressure4_ThirdlastAction
possessions['OnGroupPressure5_ThirdlastAction'] = OnGroupPressure5_ThirdlastAction
possessions['OnGroupPressure6_ThirdlastAction'] = OnGroupPressure6_ThirdlastAction
possessions['OnGroupPressure7_ThirdlastAction'] = OnGroupPressure7_ThirdlastAction
possessions['OnGroupPressure8_ThirdlastAction'] = OnGroupPressure8_ThirdlastAction
possessions['OnGroupPressure9_ThirdlastAction'] = OnGroupPressure9_ThirdlastAction
possessions['OnGroupPressure10_ThirdlastAction'] = OnGroupPressure10_ThirdlastAction

possessions['OnBallPressure_FourthlastAction'] = OnBallPressure_FourthlastAction
possessions['OnGroupPressure1_FourthlastAction'] = OnGroupPressure1_FourthlastAction
possessions['OnGroupPressure2_FourthlastAction'] = OnGroupPressure2_FourthlastAction
possessions['OnGroupPressure3_FourthlastAction'] = OnGroupPressure3_FourthlastAction
possessions['OnGroupPressure4_FourthlastAction'] = OnGroupPressure4_FourthlastAction
possessions['OnGroupPressure5_FourthlastAction'] = OnGroupPressure5_FourthlastAction
possessions['OnGroupPressure6_FourthlastAction'] = OnGroupPressure6_FourthlastAction
possessions['OnGroupPressure7_FourthlastAction'] = OnGroupPressure7_FourthlastAction
possessions['OnGroupPressure8_FourthlastAction'] = OnGroupPressure8_FourthlastAction
possessions['OnGroupPressure9_FourthlastAction'] = OnGroupPressure9_FourthlastAction
possessions['OnGroupPressure10_FourthlastAction'] = OnGroupPressure10_FourthlastAction

possessions['FrameLastAction'] = frame_lastaction
possessions['FramePenultimateAction'] = frame_penultimateaction
possessions['FrameThirdlastAction'] = frame_thirdlastaction
possessions['FrameFourthlastAction'] = frame_fourthlastaction

#%% Calculation of group pressure and team pressure
possessions['OnGroupPressure_1to4_LastAction'] = (possessions['OnGroupPressure1_LastAction'] + possessions['OnGroupPressure2_LastAction'] + possessions['OnGroupPressure3_LastAction'] + possessions['OnGroupPressure4_LastAction']) /4
possessions['OnGroupPressure_1to4_PenultimateAction'] = (possessions['OnGroupPressure1_PenultimateAction'] + possessions['OnGroupPressure2_PenultimateAction'] + possessions['OnGroupPressure3_PenultimateAction'] + possessions['OnGroupPressure4_PenultimateAction']) /4
possessions['OnGroupPressure_1to4_ThirdlastAction'] = (possessions['OnGroupPressure1_ThirdlastAction'] + possessions['OnGroupPressure2_ThirdlastAction'] + possessions['OnGroupPressure3_ThirdlastAction'] + possessions['OnGroupPressure4_ThirdlastAction']) /4
possessions['OnGroupPressure_1to4_FourthlastAction'] = (possessions['OnGroupPressure1_FourthlastAction'] + possessions['OnGroupPressure2_FourthlastAction'] + possessions['OnGroupPressure3_FourthlastAction'] + possessions['OnGroupPressure4_FourthlastAction']) /4

possessions['OnGroupPressure_5to10_LastAction'] = (possessions['OnGroupPressure5_LastAction'] + possessions['OnGroupPressure6_LastAction'] + possessions['OnGroupPressure7_LastAction'] + possessions['OnGroupPressure8_LastAction'] + possessions['OnGroupPressure9_LastAction'] + possessions['OnGroupPressure10_LastAction']) /6
possessions['OnGroupPressure_5to10_PenultimateAction'] = (possessions['OnGroupPressure5_PenultimateAction'] + possessions['OnGroupPressure6_PenultimateAction'] + possessions['OnGroupPressure7_PenultimateAction'] + possessions['OnGroupPressure8_PenultimateAction'] + possessions['OnGroupPressure9_PenultimateAction'] + possessions['OnGroupPressure10_PenultimateAction']) /6
possessions['OnGroupPressure_5to10_ThirdlastAction'] = (possessions['OnGroupPressure5_ThirdlastAction'] + possessions['OnGroupPressure6_ThirdlastAction'] + possessions['OnGroupPressure7_ThirdlastAction'] + possessions['OnGroupPressure8_ThirdlastAction'] + possessions['OnGroupPressure9_ThirdlastAction'] + possessions['OnGroupPressure10_ThirdlastAction']) /6
possessions['OnGroupPressure_5to10_FourthlastAction'] = (possessions['OnGroupPressure5_FourthlastAction'] + possessions['OnGroupPressure6_FourthlastAction'] + possessions['OnGroupPressure7_FourthlastAction'] + possessions['OnGroupPressure8_FourthlastAction'] + possessions['OnGroupPressure9_FourthlastAction'] + possessions['OnGroupPressure10_FourthlastAction']) /6


#%% Calculation of end of an attack in last/middle/first third?

Third = []
for idx, attack in possessions.iterrows ():
    if attack.team == attack.TeamLeft:
        if attack.X_Position_OfLastDefensiveAction >= 70:
            third = 'LastThird'
        elif attack.X_Position_OfLastDefensiveAction >= 35:
            third = 'MiddleThird'
        elif attack.X_Position_OfLastDefensiveAction < 35:
            third = 'FirstThird'
    elif attack.team == attack.TeamRight:
        if attack.X_Position_OfLastDefensiveAction <= 35:
            third = 'LastThird'
        elif attack.X_Position_OfLastDefensiveAction <= 70:
            third = 'MiddleThird'
        elif attack.X_Position_OfLastDefensiveAction > 70:
            third = 'FirstThird'
    else:
        third = ''
    Third.append (third)


possessions['Third_OfLastDefensiveAction'] = Third

#%% Safe the result Dataframe 'possessions'

possessions.to_csv (r'result_possessions_Game9.csv')


