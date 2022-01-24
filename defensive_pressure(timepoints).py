import pandas as pd
import numpy as np
from datetime import datetime
import math
import matplotlib.pyplot as plt

#%%Load event and position data

event_data =  pd.read_csv ('C:/Users/sysadmin/Desktop/Dissertation/DFL Daten/DFL Daten/EventData_1.Buli_Season19-20_Game18.csv')
position_data = pd.read_csv ('C:/Users/sysadmin/Desktop/Dissertation/DFL Daten/DFL Daten/PositionData_1.Buli_Season19-20_Game18.csv')

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
#unsuccessful defensive play:
    # 1. Stoppage of play
    # 2. Ball going out of play
    # 3. Shot on goal

#successful defensive play:
    #1. BallClaiming
    #2. ball gain after unsuccessful pass
    #3. ball gain after successful TacklingGame (duel)
    
    
# 2. Identification of playing direction

#1.:
possessions = possessions.reset_index ()
possessions = possessions.rename (columns = {'index': 'Row'})

#%%
Result = []
Result2 = []
Defensive_success = []
X_Position = []
Y_Position =[]

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
    
    attacking_team = attack.team
#unsuccessful defensive play:
    # 1. Stoppage of play
    # 2. Ball going out of play
    # 3. Shot on goal
    if  event_data.loc[[idx]].Event1.item () == 'FinalWhistle' and event_data.loc[[idx-1]].Event1.item () != 'ShotAtGoal':
        x_position = event_data.loc[[idx-1]]['X-Position'].item ()
        y_position = event_data.loc[[idx-1]]['Y-Position'].item ()
        result = 'stoppage_of_play'
        defensive_success = 'unsuccessful'
        result2 = 'end_of_half'
        
    #Stoppage of Play:
    elif event_data.loc[[idx]].Event1.item () == 'FreeKick' or event_data.loc[[idx-1]].Event1.item () == 'Foul' or event_data.loc[[idx]].Event1.item () == 'Foul' or event_data.loc[[idx-1]].Event1.item () == 'Offside'or event_data.loc[[idx]].Event1.item () == 'Offside':
        x_position = event_data.loc[[idx]]['X-Position'].item ()
        y_position = event_data.loc[[idx]]['Y-Position'].item ()
        result = 'stoppage_of_play'
        defensive_success = 'unsuccessful'
        
        if event_data.loc[[idx]].Event1.item () == 'Foul' and event_data.loc[[idx]].TeamFouled.item () == attacking_team:
            result2 = 'foul_defending_team'
        elif event_data.loc[[idx]].Event1.item () == 'Foul' and event_data.loc[[idx]].TeamFouled.item () != attacking_team:
            result2 = 'foul_attacking_team'
        elif event_data.loc[[idx]].Event1.item () == 'Offside' or event_data.loc[[idx-1]].Event1.item () == 'Offside':
            result2 = 'Offside'
        else:
            result2 = 'other'
            
    #Ball going out of play (without shot as last action)
    elif  event_data.loc[[idx-1]].Event1.item () != 'ShotAtGoal' and (event_data.loc[[idx]].Event1.item () == 'ThrowIn' or event_data.loc[[idx]].Event1.item () == 'GoalKick' or event_data.loc[[idx]].Event1.item () == 'CornerKick'):
        x_position = event_data.loc[[idx]]['X-Position'].item ()
        y_position = event_data.loc[[idx]]['Y-Position'].item ()
        result = 'ball_out_of_play'
        defensive_success = 'unsuccessful'
        
        if event_data.loc[[idx]].Team.item () == attacking_team:
            result2 = 'ball_out_of_play_by_defending_team'
        elif event_data.loc[[idx]].Team.item () != attacking_team:
            result2 = 'ball_out_of_play_by_attacking_team'
        else:
            result2 = 'other'
        
    #last action of attack is shot at goal:
    elif event_data.loc[[idx-1]].Event1.item () == 'ShotAtGoal':
        x_position = event_data.loc[[idx-1]]['X-Position'].item ()
        y_position = event_data.loc[[idx-1]]['Y-Position'].item ()
        result = 'ShotAtGoal1'
        defensive_success = 'unsuccessful'
        result2 = 'ShotAtGoal1'
    #penultimate action of attack is shot at goal:
    elif event_data.loc[[idx-2]].Event1.item () == 'ShotAtGoal' and event_data.loc[[idx-1]].Event1.item () != 'ShotAtGoal':
        x_position = event_data.loc[[idx-2]]['X-Position'].item ()
        y_position = event_data.loc[[idx-2]]['Y-Position'].item ()
        result = 'ShotAtGoal2'
        defensive_success = 'unsuccessful'
        result2 = 'ShotAtGoal2'

#successful defensive play:
    #1. BallClaiming
    #2. ball gain after unsuccessful pass
    #3. ball gain after successful TacklingGame (duel)
    
    #BallClaiming in first row after possession end:
    elif event_data.loc[[idx]].Event1.item () == 'BallClaiming' and event_data.loc[[idx]].Team.item () != attack.team:
        x_position = event_data.loc[[idx]]['X-Position'].item ()
        y_position = event_data.loc[[idx]]['Y-Position'].item ()
        result = 'ball_loss_claiming1'
        defensive_success = 'successful'
        result2 = 'ball_loss_claiming1'
        #new definition of possession end
        possessions.loc[row, 'end'] = event_data.loc[[idx]]['EventTime'].item ()
        
    #BallClaiming in second row after possession end & NO! Tackling in first row after possession change:
    elif event_data.loc[[idx+1]].Event1.item () == 'BallClaiming' and event_data.loc[[idx+1]].Team.item () != attack.team and event_data.loc[[idx]].Event1.item () != 'TacklingGame':
        x_position = event_data.loc[[idx+1]]['X-Position'].item ()
        y_position = event_data.loc[[idx+1]]['Y-Position'].item ()
        result = 'ball_loss_claiming2'
        defensive_success = 'successful'
        result2 = 'ball_loss_claiming2'
        #new definition of possession end
        possessions.loc[row, 'end'] = event_data.loc[[idx+1]]['EventTime'].item ()
        
    #Ballgain after unsuccessful pass: last action of attack is unsuccessful pass & next action is on ball action of other team & no event called BallClaiming:
    elif event_data.loc[[idx-1]].Event1.item () == 'Play' and event_data.loc[[idx-1]].Evaluation.item () == 'unsuccessful' and event_data.loc[[idx]].Team.item () != attacking_team and event_data.loc[[idx]].Event1.item () != 'BallClaiming'  and event_data.loc[[idx+1]].Event1.item () != 'BallClaiming':
        x_position = event_data.loc[[idx-1]]['X-Position'].item ()
        y_position = event_data.loc[[idx-1]]['Y-Position'].item ()
        result = 'ball_loss_unsuccessfulpass'
        defensive_success = 'successful'
        result2 = 'ball_loss_unsuccessfulpass'
        
    #Ballloss after tackling in first row after possession end:
    elif event_data.loc[[idx]].Event1.item () == 'TacklingGame' and event_data.loc[[idx]].WinnerTeam.item () != attack.team and event_data.loc[[idx]].PossessionChange.item () == True:
        x_position = event_data.loc[[idx]]['X-Position'].item ()
        y_position = event_data.loc[[idx]]['Y-Position'].item ()
        result = 'ball_loss_tackling1'
        defensive_success = 'successful'
        result2 = 'ball_loss_tackling1'
        #new definition of possession end
        possessions.loc[row, 'end'] = event_data.loc[[idx]]['EventTime'].item ()
        
        
    #Ballloss after tackling in second row after possession end:
    elif event_data.loc[[idx+1]].Event1.item () == 'TacklingGame' and event_data.loc[[idx+1]].WinnerTeam.item () != attack.team and event_data.loc[[idx+1]].PossessionChange.item () == True:
        x_position = event_data.loc[[idx+1]]['X-Position'].item ()
        y_position = event_data.loc[[idx+1]]['Y-Position'].item ()
        result = 'ball_loss_tackling2'
        defensive_success = 'successful'
        result2 = 'ball_loss_tackling2'
        #new definition of possession end
        possessions.loc[row, 'end'] = event_data.loc[[idx+1]]['EventTime'].item ()
        
    #BallClaiming in second row after possession end & Tackling with possession change in first row after possession end:
    elif event_data.loc[[idx+1]].Event1.item () == 'BallClaiming' and event_data.loc[[idx+1]].Team.item () != attack.team and event_data.loc[[idx]].Event1.item () == 'TacklingGame' and event_data.loc[[idx]].PossessionChange.item () == True:
        x_position = event_data.loc[[idx+1]]['X-Position'].item ()
        y_position = event_data.loc[[idx+1]]['Y-Position'].item ()
        result = 'ball_loss_claiming_after_tackling'
        defensive_success = 'successful'
        result2 = 'ball_loss_claiming_after_tackling'        
        #new definition of possession end
        possessions.loc[row, 'end'] = event_data.loc[[idx+1]]['EventTime'].item ()
        
    else:
        x_position = event_data.loc[[idx-1]]['X-Position'].item ()
        y_position = event_data.loc[[idx-1]]['Y-Position'].item ()
        result = 'other'
        defensive_success = 'other'
        result2 = 'other'
    
    Result.append (result)
    Result2.append (result2)
    Defensive_success.append (defensive_success)
    X_Position.append (x_position)
    Y_Position.append (y_position)
    
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
possessions['PossessionResult2'] = Result2
possessions['DefensiveSuccess'] = Defensive_success
possessions['X_Position_OfLastDefensiveAction'] = X_Position
possessions['Y_Position_OfLastDefensiveAction'] = Y_Position

possessions['TeamLeft'] = Team_left
possessions['TeamRight'] = Team_right


#%%
#Synchronization of start and end of possession with position data

#depending on the first and the last action of an attack

#1. if possession result is 'other': 
    #start: first action of events
    #end:last action in events


#2. if possession result is 'ball going out of play':
    #start: first action of events 
    #end: ball going out of play after 1 sec of last pass?

#3. if possession end is 'stoppage of play':
    #start: first action of events 
    #end: ball is stopped after 1 sec of last action?

#4. if possession end is 'Ball claiming':
    #start: first action of events
    #end: last action of events

#5. if possession end is 'Ball gain after tackling':
    #start: first action of events
    #end: last action of events

#6. if possession end is 'Ball gain after unsuccessful pass':
    #start: first action of events
    #end: pass is regained after 1 sec of last pass?

#7. if possession end is 'shot on goal':
    #start: first action of events
    #end: shot on goal
    
#%% Synchronisation of start of an attack (Alignment of event data to position data)

possessions['start_sync'] = None

for row, attack in possessions.iterrows ():

    actions = event_data[(event_data['EventTime'] >= attack.start) &
                         (event_data['EventTime'] <= attack.end)]
    actions = actions.reset_index ()
    #identification of action
    action_first = actions.loc[[0]]
    
    critical_events = ['OtherPlayerAction', 'Nutmeg', 'Substitution', 'FinalWhistle', 'SpectacularPlay', 'Caution']
    if (actions.loc[[0]].Event1.item () in critical_events) == True and (actions.loc[[1]].Event1.item () in critical_events) == False:
        action_first = actions.loc[[1]]
    elif (actions.loc[[0]].Event1.item () in critical_events) == True and (actions.loc[[1]].Event1.item () in critical_events) == True and (actions.loc[[2]].Event1.item () in critical_events) == False:
        action_first = actions.loc[[2]]
    elif (actions.loc[[0]].Event1.item () in critical_events) == True and (actions.loc[[1]].Event1.item () in critical_events) == True and (actions.loc[[2]].Event1.item () in critical_events) == True and (actions.loc[[3]].Event1.item () in critical_events) == False:
        action_first = actions.loc[[3]]
    
    #Find right frame of position data of this action (Snchronization of Event & Position data)
    start_sync1 = (((action_first.EventTime.item().hour)*60)*60) + ((action_first.EventTime.item ().minute)*60) + (action_first.EventTime.item().second) + ((action_first.EventTime.item ().microsecond)/1000000)  - 8
    end_sync1 = (((action_first.EventTime.item().hour)*60)*60) + ((action_first.EventTime.item ().minute)*60) + (action_first.EventTime.item().second) + ((action_first.EventTime.item ().microsecond)/1000000)  + 8

#Identification of real event in position data (with different synchronization for different events)
#1. Tackling Game (duels)
#2. Passes
#3. Fouls
#4. other events 
        
    #1. first action is Tackling Game
    if action_first.Player.isnull ().item() == True and action_first.Event1.item () == 'TacklingGame':
        #First Player
        search_field1 = position_data[position_data['PersonId'] == (action_first.Winner.item ())]
        search_field1 = search_field1[(search_field1['T_sec'] >= start_sync1) &
                                      (search_field1['T_sec'] <= end_sync1)]
        #Second Player
        search_field_second1 = position_data[position_data['PersonId'] == (action_first.Loser.item ())]
        search_field_second1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                    (search_field_second1['T_sec'] <= end_sync1)]
        #Ball
        search_field_ball1 = position_data[position_data['TeamId'] == 'BALL']
        search_field_ball1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                    (search_field_second1['T_sec'] <= end_sync1)]
        
        search_field1 = search_field1.reset_index ()
        search_field1 = search_field1.loc [0:399]

        search_field_second1 = search_field_second1.reset_index ()
        search_field_second1 = search_field_second1.loc [0:399]
        
        search_field_ball1 = search_field_ball1.reset_index ()
        search_field_ball1 = search_field_ball1.loc [0:399]
        
        search_field1 = search_field1.join (search_field_second1,  lsuffix = '_1')
        search_field1 = search_field1.join (search_field_ball1, lsuffix= '_2', rsuffix= '_3')
        
        Difference1 = []
        for index, frame in search_field1.iterrows ():
            # Difference of player 1 and player2 is weighted 10 times over difference of players and ball to origin of playing event 
            difference_player1_player2 = ((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))
            difference_player12_Origin = ((abs(frame['X_1'] - action_first['X-Position'].item ())) + (abs(frame['Y_1'] - action_first['Y-Position'].item()))) + ((abs(frame['X_2'] - action_first['X-Position'].item())) + (abs(frame['Y_2'] - action_first['Y-Position'].item())))
            
            difference1 = (((difference_player1_player2 * 10) + difference_player12_Origin )/11) **2

            Difference1.append (difference1)
    
        search_field1 ['difference'] = Difference1
        identified_frame_start = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
        
    #2. first action is pass 
    elif action_first.Recipient.isnull ().item() == False and (action_first.Event1.item () == 'Play' or action_first.Event2.item () == 'Play'):

        #First Player
        search_field1 = position_data[position_data['PersonId'] == (action_first.Player.item ())]
        search_field1 = search_field1[(search_field1['T_sec'] >= start_sync1) &
                                      (search_field1['T_sec'] <= end_sync1)]
        #Ball
        search_field_second1 = position_data[position_data['TeamId'] == 'BALL']
        search_field_second1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                    (search_field_second1['T_sec'] <= end_sync1)]
        #Reciever with 1 sec plus
        search_field_receiver = position_data[position_data['PersonId'] == (action_first.Recipient.item ())]
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
            # Difference of player 1 and player2 is weighted 10 times over difference of player and ball to origin of playing event 
            # (Differnece Player to Ball *10) + (Difference Player & Ball to Origin of Event*1) + (Difference of Receiever to Ball 1 Sec after Pass)
            difference_player1_player2 = ((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))
            difference_player12_Origin = ((abs(frame['X_1'] - action_first['X-Position'].item())) + (abs(frame['Y_1'] - action_first['Y-Position'].item()))) + ((abs(frame['X_2'] - action_first['X-Position'].item())) + (abs(frame['Y_2'] - action_first['Y-Position'].item())))
            difference_Reciever_Ball_plus1sec = (abs(frame['X_3'] - frame['X_4'])) + (abs(frame['Y_3'] - frame['Y_4']))
            
            difference1 = (((difference_player1_player2 * 10) + difference_player12_Origin + difference_Reciever_Ball_plus1sec)/12) **2

            Difference1.append (difference1)
        search_field1 ['difference'] = Difference1
        identified_frame_start = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
    
    
    #first action is foul:
    elif action_first.Player.isnull ().item() == True and action_first.Event1.item () == 'Foul': 
        #Search for Freekick after the foul --> define the freekick as start of possession 
        if event_data.loc[[action_first['index'] + 1]].Event1.item() == 'FreeKick':
            action_first =  event_data.loc[[action_first['index'] + 1]]
        elif  event_data.loc[[action_first['index'] + 1]].Event1.item() != 'FreeKick' and  event_data.loc[[action_first['index'] + 2]].Event1.item() == 'FreeKick':
            action_first =  event_data.loc[[action_first['index'] + 2]]
        elif event_data.loc[[action_first['index'] + 1]].Event1.item() != 'FreeKick' and  event_data.loc[[action_first['index'] + 2]].Event1.item() != 'FreeKick' and  event_data.loc[[action_first['index'] + 3]].Event1.item() == 'FreeKick':
            action_first =  event_data.loc[[action_first['index'] + 3]]
        
        #First Player
        search_field1 = position_data[position_data['PersonId'] == (action_first.Player.item ())]
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
            # Difference of player 1 and Ball is weighted 10 times over difference of player and ball to origin of playing event 
            difference_player1_ball = (abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2']))
            difference_player1ball_Origin = ((abs(frame['X_1'] - action_first['X-Position'].item())) + (abs(frame['Y_1'] - action_first['Y-Position'].item()))) + ((abs(frame['X_2'] - action_first['X-Position']).item()) + (abs(frame['Y_2'] - action_first['Y-Position'].item())))
            
            difference1 = (((difference_player1_ball *10) + difference_player1ball_Origin) /11) **2
            Difference1.append (difference1)
    
        search_field1 ['difference'] = Difference1
        identified_frame_start = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
    
    #first action is other action than Tacklinggame, Pass or Foul
    elif action_first.Player.isnull ().item() == False:
        #First Player
        search_field1 = position_data[position_data['PersonId'] == (action_first.Player.item ())]
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
            # Difference of player 1 and Ball is weighted 10 times over difference of player and ball to origin of playing event 
            difference_player1_ball = (abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2']))
            difference_player1ball_Origin = ((abs(frame['X_1'] - action_first['X-Position'].item())) + (abs(frame['Y_1'] - action_first['Y-Position'].item()))) + ((abs(frame['X_2'] - action_first['X-Position']).item()) + (abs(frame['Y_2'] - action_first['Y-Position'].item())))
            
            difference1 = (((difference_player1_ball *10) + difference_player1ball_Origin) /11) **2
            Difference1.append (difference1)
    
        search_field1 ['difference'] = Difference1
        identified_frame_start = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
    
        
    else:
        identified_frame_start = None
    
    possessions.loc[row, 'start_sync'] = identified_frame_start

#%% Synchronisation of end of an attack (Alignment of event data to position data)

possessions['end_sync'] = None

for row, attack in possessions.iterrows ():

    actions = event_data[(event_data['EventTime'] >= attack.start) &
                         (event_data['EventTime'] <= attack.end)]
    actions = actions.reset_index ()
    
    #identification of action
    action_last = actions.iloc[-1:]
    
    if action_last.Event1.item() == 'Nutmeg' or action_last.Event1.item() == 'FinalWhistle' or action_last.Event1.item() == 'SpectacularPlay':
        action_last = actions.iloc[-2:-1]

    #Find right frame of position data of this action (Snchronization of Event & Position data)
    start_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  - 8
    end_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  + 8

#result of attack is ball claiming:
    if attack.PossessionResult == 'ball_loss_claiming1' or attack.PossessionResult == 'ball_loss_claiming2':
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
            # Difference of player 1 and Ball is weighted 10 times over difference of player and ball to origin of playing event 
            difference_player1_ball = (abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2']))
            difference_player1ball_Origin = ((abs(frame['X_1'] - action_last['X-Position'].item())) + (abs(frame['Y_1'] - action_last['Y-Position'].item()))) + ((abs(frame['X_2'] - action_last['X-Position']).item()) + (abs(frame['Y_2'] - action_last['Y-Position'].item())))
            
            difference1 = (((difference_player1_ball *10) + difference_player1ball_Origin) /11) **2
            Difference1.append (difference1)
    
        search_field1 ['difference'] = Difference1
        identified_frame_end = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
    

#result of attack is 'Ball gain after tackling:
    elif attack.PossessionResult == 'ball_loss_tackling1' or attack.PossessionResult == 'ball_loss_tackling2':
        
        if action_last.Event1.item() != 'TacklingGame' and actions.iloc[-2:-1].Event1.item() == 'TacklingGame' and actions.iloc[-2:-1].PossessionChange.item () == True:
            action_last = actions.iloc[-2:-1]
            
            #Find right frame of position data of this action (Snchronization of Event & Position data)
            start_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  - 8
            end_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  + 8
   
        #First Player
        search_field1 = position_data[position_data['PersonId'] == (action_last.Winner.item ())]
        search_field1 = search_field1[(search_field1['T_sec'] >= start_sync1) &
                                      (search_field1['T_sec'] <= end_sync1)]
        #Second Player
        search_field_second1 = position_data[position_data['PersonId'] == (action_last.Loser.item ())]
        search_field_second1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                    (search_field_second1['T_sec'] <= end_sync1)]
        #Ball
        search_field_ball1 = position_data[position_data['TeamId'] == 'BALL']
        search_field_ball1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                    (search_field_second1['T_sec'] <= end_sync1)]
        
        search_field1 = search_field1.reset_index ()
        search_field1 = search_field1.loc [0:399]

        search_field_second1 = search_field_second1.reset_index ()
        search_field_second1 = search_field_second1.loc [0:399]
        
        search_field_ball1 = search_field_ball1.reset_index ()
        search_field_ball1 = search_field_ball1.loc [0:399]
        
        search_field1 = search_field1.join (search_field_second1,  lsuffix = '_1')
        search_field1 = search_field1.join (search_field_ball1, lsuffix= '_2', rsuffix= '_3')
        
        Difference1 = []
        for index, frame in search_field1.iterrows ():
            # Difference of player 1 and player2 is weighted 10 times over difference of players and ball to origin of playing event 
            difference_player1_player2 = ((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))
            difference_player12_Origin = ((abs(frame['X_1'] - action_last['X-Position'].item ())) + (abs(frame['Y_1'] - action_last['Y-Position'].item()))) + ((abs(frame['X_2'] - action_last['X-Position'].item())) + (abs(frame['Y_2'] - action_last['Y-Position'].item())))
            
            difference1 = (((difference_player1_player2 * 10) + difference_player12_Origin )/11) **2

            Difference1.append (difference1)
    
        search_field1 ['difference'] = Difference1
        identified_frame_end = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
        
#result of possession is unsuccessful pass:
    elif attack.PossessionResult == 'ball_loss_unsuccessfulpass':
        if action_last.Recipient.isnull().item () == True:
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
                # Difference of player 1 and Ball is weighted 10 times over difference of player and ball to origin of playing event 
                difference_player1_ball = (abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2']))
                difference_player1ball_Origin = ((abs(frame['X_1'] - action_last['X-Position'].item())) + (abs(frame['Y_1'] - action_last['Y-Position'].item()))) + ((abs(frame['X_2'] - action_last['X-Position']).item()) + (abs(frame['Y_2'] - action_last['Y-Position'].item())))
                
                difference1 = (((difference_player1_ball *10) + difference_player1ball_Origin) /11) **2
                Difference1.append (difference1)
        
            search_field1 ['difference'] = Difference1
            identified_frame_end = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
        
        else:
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
                # Difference of player 1 and player2 is weighted 10 times over difference of player and ball to origin of playing event 
                # (Differnece Player to Ball *10) + (Difference Player & Ball to Origin of Event*1) + (Difference of Receiever to Ball 1 Sec after Pass)
                difference_player1_player2 = ((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))
                difference_player12_Origin = ((abs(frame['X_1'] - action_last['X-Position'].item())) + (abs(frame['Y_1'] - action_last['Y-Position'].item()))) + ((abs(frame['X_2'] - action_last['X-Position'].item())) + (abs(frame['Y_2'] - action_last['Y-Position'].item())))
                difference_Reciever_Ball_plus1sec = (abs(frame['X_3'] - frame['X_4'])) + (abs(frame['Y_3'] - frame['Y_4']))
                
                difference1 = (((difference_player1_player2 * 10) + difference_player12_Origin + difference_Reciever_Ball_plus1sec)/12) **2
    
                Difference1.append (difference1)
            search_field1 ['difference'] = Difference1
            identified_frame_end = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
        
    
    
    
#result of attack is shot on goal
    elif attack.PossessionResult == 'ShotAtGoal1':
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
            # Difference of player 1 and Ball is weighted 10 times over difference of player and ball to origin of playing event 
            difference_player1_ball = (abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2']))
            difference_player1ball_Origin = ((abs(frame['X_1'] - action_last['X-Position'].item())) + (abs(frame['Y_1'] - action_last['Y-Position'].item()))) + ((abs(frame['X_2'] - action_last['X-Position']).item()) + (abs(frame['Y_2'] - action_last['Y-Position'].item())))
            
            difference1 = (((difference_player1_ball *10) + difference_player1ball_Origin) /11) **2
            Difference1.append (difference1)
    
        search_field1 ['difference'] = Difference1
        identified_frame_end = (search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item())
    

#result of attack is ball going out of play
#result of attack is stoppage of play
#result of attack is other
    elif action_last.Event1.item() == 'Offside':
        #1. identify the pass that led to the 
        if actions.iloc[-2:-1].Player.isnull ().item() == False and actions.iloc[-2:-1]['X-Position'].isnull ().item() == False:
            action_last = actions.iloc[-2:-1]
        elif  (actions.iloc[-2:-1].Player.isnull ().item() == True or actions.iloc[-2:-1]['X-Position'].isnull ().item() == True) and actions.iloc[-3:-2].Player.isnull ().item() == False and actions.iloc[-3:-2]['X-Position'].isnull ().item() == False:
            action_last = actions.iloc[-3:-2]
        elif  (actions.iloc[-2:-1].Player.isnull ().item() == True or actions.iloc[-2:-1]['X-Position'].isnull ().item() == True) and  (actions.iloc[-3:-2].Player.isnull ().item() == True or actions.iloc[-3:-2]['X-Position'].isnull ().item() == True) and  actions.iloc[-4:-3].Player.isnull ().item() == False and actions.iloc[-4:-3]['X-Position'].isnull ().item() == False:
            action_last = actions.iloc[-4:-3]
        else:
            identified_frame_end = None
            
        #2. find the first frame, where the ball is in the area (4-5m difference) of the freekick
        #Find right frame of position data of this action (Snchronization of Event & Position data)
        start_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  - 8
        end_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  + 8
         
    
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
            # Difference of player 1 and Ball is weighted 10 times over difference of player and ball to origin of playing event 
            difference_player1_ball = (abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2']))
            difference_player1ball_Origin = ((abs(frame['X_1'] - action_last['X-Position'].item())) + (abs(frame['Y_1'] - action_last['Y-Position'].item()))) + ((abs(frame['X_2'] - action_last['X-Position']).item()) + (abs(frame['Y_2'] - action_last['Y-Position'].item())))
            
            difference1 = (((difference_player1_ball *10) + difference_player1ball_Origin) /11) **2
            Difference1.append (difference1)
    
        search_field1 ['difference'] = Difference1
        identified_frame_end = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()

        
        #Search for Freekick after the offside --> needed for the location of the offside
        if event_data.loc[[actions.iloc[-1]['index'].item()]].Event1.item() == 'FreeKick':
            freekick =  event_data.loc[[actions.iloc[-1]['index'].item() + 1]]
        elif  event_data.loc[[actions.iloc[-1]['index'].item() + 1]].Event1.item() != 'FreeKick' and  event_data.loc[[actions.iloc[-1]['index'].item() + 2]].Event1.item() == 'FreeKick':
            freekick =  event_data.loc[[actions.iloc[-1]['index'].item() + 2]]
        elif event_data.loc[[actions.iloc[-1]['index'].item() + 1]].Event1.item() != 'FreeKick' and  event_data.loc[[actions.iloc[-1]['index'].item() + 2]].Event1.item() != 'FreeKick' and  event_data.loc[[actions.iloc[-1]['index'].item() + 3]].Event1.item() == 'FreeKick':
            freekick =  event_data.loc[[actions.iloc[-1]['index'].item() + 3]]
        else:
            freekick =  event_data.loc[[actions.iloc[-1]['index'].item() + 1]]

        start_sync = identified_frame_end
        end_sync = identified_frame_end + 8
        
        #Ball
        search_field_ball = position_data[position_data['TeamId'] == 'BALL']
        search_field_ball = search_field_ball[(search_field_ball['T_sec'] >= start_sync) &
                                              (search_field_ball['T_sec'] <= end_sync)]

        Difference1 = []
        for index, frame in search_field_ball.iterrows ():
            # Difference of Ball and origin of freekick is under 3 the first time 
            difference1 = (abs(frame['X'] - freekick['X-Position'].item())) + (abs(frame['Y'] - freekick['Y-Position'].item()))
            Difference1.append (difference1)
    
        search_field_ball['difference'] = Difference1
        
        if search_field_ball['difference'].min () <= 15 :
            search_field_ball = search_field_ball[search_field_ball['difference'] <= 15].reset_index ()
            identified_frame_end = search_field_ball.iloc[0:1].T_sec.item()
        else:
            identified_frame_end = None
       
        
    elif (attack.PossessionResult == 'ball_out_of_play' or attack.PossessionResult == 'stoppage_of_play' or attack.PossessionResult ==	'other') and  action_last.Event1.item() != 'Offside':
        if  action_last.Event1.item() == 'GoalDisallowed' and actions.iloc[-2:-1].Player.isnull ().item() == True:
            action_last = actions.iloc[-2:-1]
            #Find right frame of position data of this action (Snchronization of Event & Position data)
            start_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  - 8
            end_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  + 8
            
        elif (action_last.Event1.item() == 'Offside' or action_last.Event1.item() == 'GoalDisallowed') and actions.iloc[-2:-1].Player.isnull ().item() == False:
            action_last = actions.iloc[-3:-2]
            #Find right frame of position data of this action (Snchronization of Event & Position data)
            start_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  - 8
            end_sync1 = (((action_last.EventTime.item().hour)*60)*60) + ((action_last.EventTime.item ().minute)*60) + (action_last.EventTime.item().second) + ((action_last.EventTime.item ().microsecond)/1000000)  + 8

            
        
        if action_last.Player.isnull ().item() == True and action_last.Event1.item () == 'TacklingGame':
            #First Player
            search_field1 = position_data[position_data['PersonId'] == (action_last.Winner.item ())]
            search_field1 = search_field1[(search_field1['T_sec'] >= start_sync1) &
                                          (search_field1['T_sec'] <= end_sync1)]
            #Second Player
            search_field_second1 = position_data[position_data['PersonId'] == (action_last.Loser.item ())]
            search_field_second1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                        (search_field_second1['T_sec'] <= end_sync1)]
            #Ball
            search_field_ball1 = position_data[position_data['TeamId'] == 'BALL']
            search_field_ball1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                        (search_field_second1['T_sec'] <= end_sync1)]
            
            search_field1 = search_field1.reset_index ()
            search_field1 = search_field1.loc [0:399]
    
            search_field_second1 = search_field_second1.reset_index ()
            search_field_second1 = search_field_second1.loc [0:399]
            
            search_field_ball1 = search_field_ball1.reset_index ()
            search_field_ball1 = search_field_ball1.loc [0:399]
            
            search_field1 = search_field1.join (search_field_second1,  lsuffix = '_1')
            search_field1 = search_field1.join (search_field_ball1, lsuffix= '_2', rsuffix= '_3')
            
            Difference1 = []
            for index, frame in search_field1.iterrows ():
                # Difference of player 1 and player2 is weighted 10 times over difference of players and ball to origin of playing event 
                difference_player1_player2 = ((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))
                difference_player12_Origin = ((abs(frame['X_1'] - action_last['X-Position'].item ())) + (abs(frame['Y_1'] - action_last['Y-Position'].item()))) + ((abs(frame['X_2'] - action_last['X-Position'].item())) + (abs(frame['Y_2'] - action_last['Y-Position'].item())))
                
                difference1 = (((difference_player1_player2 * 10) + difference_player12_Origin )/11) **2
    
                Difference1.append (difference1)
        
            search_field1 ['difference'] = Difference1
            identified_frame_end = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            
        #2. last action is pass 
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
                # Difference of player 1 and player2 is weighted 10 times over difference of player and ball to origin of playing event 
                # (Differnece Player to Ball *10) + (Difference Player & Ball to Origin of Event*1) + (Difference of Receiever to Ball 1 Sec after Pass)
                difference_player1_player2 = ((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))
                difference_player12_Origin = ((abs(frame['X_1'] - action_last['X-Position'].item())) + (abs(frame['Y_1'] - action_last['Y-Position'].item()))) + ((abs(frame['X_2'] - action_last['X-Position'].item())) + (abs(frame['Y_2'] - action_last['Y-Position'].item())))
                difference_Reciever_Ball_plus1sec = (abs(frame['X_3'] - frame['X_4'])) + (abs(frame['Y_3'] - frame['Y_4']))
                
                difference1 = (((difference_player1_player2 * 10) + difference_player12_Origin + difference_Reciever_Ball_plus1sec)/12) **2
    
                Difference1.append (difference1)
            search_field1 ['difference'] = Difference1
            identified_frame_end = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
        
        
        #last action is foul:
        elif action_last.Player.isnull ().item() == True and action_last.Event1.item () == 'Foul': 
            
            #Search for Freekick after the foul --> needed for the location of the foul
            if event_data.loc[[action_last['index'].item() + 1]].Event1.item() == 'FreeKick':
                freekick =  event_data.loc[[action_last['index'].item() + 1]]
            elif  event_data.loc[[action_last['index'].item() + 1]].Event1.item() != 'FreeKick' and  event_data.loc[[action_last['index'].item() + 2]].Event1.item() == 'FreeKick':
                freekick =  event_data.loc[[action_last['index'].item() + 2]]
            elif event_data.loc[[action_last['index'].item() + 1]].Event1.item() != 'FreeKick' and  event_data.loc[[action_last['index'].item() + 2]].Event1.item() != 'FreeKick' and  event_data.loc[[action_last['index'].item() + 3]].Event1.item() == 'FreeKick':
                freekick =  event_data.loc[[action_last['index'].item() + 3]]
            else:
                freekick =  event_data.loc[[action_last['index'].item() + 1]]
                
            #First Player
            search_field1 = position_data[position_data['PersonId'] == (action_last.Fouler.item ())]
            search_field1 = search_field1[(search_field1['T_sec'] >= start_sync1) &
                                          (search_field1['T_sec'] <= end_sync1)]
            #Second Player
            search_field_second1 = position_data[position_data['PersonId'] == (action_last.Fouled.item ())]
            search_field_second1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                        (search_field_second1['T_sec'] <= end_sync1)]
            #Ball
            search_field_ball1 = position_data[position_data['TeamId'] == 'BALL']
            search_field_ball1 = search_field_second1[(search_field_second1['T_sec'] >= start_sync1) &
                                                        (search_field_second1['T_sec'] <= end_sync1)]
            
            search_field1 = search_field1.reset_index ()
            search_field1 = search_field1.loc [0:399]
    
            search_field_second1 = search_field_second1.reset_index ()
            search_field_second1 = search_field_second1.loc [0:399]
            
            search_field_ball1 = search_field_ball1.reset_index ()
            search_field_ball1 = search_field_ball1.loc [0:399]
            
            search_field1 = search_field1.join (search_field_second1,  lsuffix = '_1')
            search_field1 = search_field1.join (search_field_ball1, lsuffix= '_2', rsuffix= '_3')
            
            Difference1 = []
            for index, frame in search_field1.iterrows ():
                # Difference of player 1 and player2 is weighted 10 times over difference of players and ball to origin of playing event 
                difference_player1_player2 = ((abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2'])))
                difference_player12_Origin = ((abs(frame['X_1'] - freekick['X-Position'].item ())) + (abs(frame['Y_1'] - freekick['Y-Position'].item()))) + ((abs(frame['X_2'] - freekick['X-Position'].item())) + (abs(frame['Y_2'] - freekick['Y-Position'].item())))
                
                difference1 = (((difference_player1_player2 * 10) + difference_player12_Origin )/11) **2
    
                Difference1.append (difference1)
        
            search_field1 ['difference'] = Difference1
            identified_frame_end = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()
            
      
        #first action is other action than Tacklinggame, Pass or Foul
        elif action_last.Player.isnull ().item() == False:
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
                # Difference of player 1 and Ball is weighted 10 times over difference of player and ball to origin of playing event 
                difference_player1_ball = (abs(frame['X_1'] - frame['X_2'])) + (abs(frame['Y_1'] - frame['Y_2']))
                difference_player1ball_Origin = ((abs(frame['X_1'] - action_last['X-Position'].item())) + (abs(frame['Y_1'] - action_last['Y-Position'].item()))) + ((abs(frame['X_2'] - action_last['X-Position']).item()) + (abs(frame['Y_2'] - action_last['Y-Position'].item())))
                
                difference1 = (((difference_player1_ball *10) + difference_player1ball_Origin) /11) **2
                Difference1.append (difference1)
        
            search_field1 ['difference'] = Difference1
            identified_frame_end = search_field1[search_field1['difference'] == search_field1 ['difference'].min ()].T_sec_1.reset_index().loc [[0]].T_sec_1.item()

    else:
        identified_frame_end = None
    
    possessions.loc[row, 'end_sync'] = identified_frame_end

#%% New calculation of possession duration (based on synchronized timestamps)
possessions['duration_sync'] = possessions.end_sync - possessions.start_sync

possessions = possessions[possessions['duration_sync'].isnull () == False]
#%% Calculation of defensive pressure

def pressure_quantification (attacker, defender, goal_x, goal_y):
    #distance between the attacker and the defender
    distance = math.sqrt((defender['X'].item() - attacker['X'].item())**2 + (defender['Y'].item() - attacker['Y'].item())**2)
    
    #angle between attacker and goal to define threat direction
    threat_direction = math.degrees (math.asin ((abs (attacker['Y'].item() - goal_y)) / (math.sqrt((attacker['X'].item() - goal_x)**2 + (attacker['Y'].item() - goal_y)**2))))
    
    #defintion of angle between defnder and atatcker dependant on threat direction
    angle_defender = math.degrees (math.asin ((abs (defender['Y'].item() - goal_y)) / (math.sqrt((defender['X'].item() - goal_x)**2 + (defender['Y'].item() - goal_y)**2))))
    
    angle_between = abs (threat_direction - angle_defender)
    
    #defnition of distance from attacker to the goal (necessary for the pressure form)
    GoalDis = math.sqrt((attacker['X'].item() - goal_x)**2 + (attacker['Y'].item() - goal_y)**2)
    
    
    # Case 1 : Defender is in front of the Attacker:
    if goal_x == 0 and defender['X'].item() > attacker['X'].item() or goal_x > 0 and defender['X'].item() < attacker['X'].item():
        #defnition of pressure area 
        Form = (1 - (math.cos (math.radians(angle_between))))/2
        
        #definition of length of the pressure area dependent n the attacker position
        #gets smaller the closer the attacker gets to the goal
        #inside the penalty area GoalDis is diveded by 2 to increase the drop of the size of the pressure area 
        if (goal_x == 0 and attacker['X'].item() <= 16 and attacker['Y'].item() >= 14 and attacker['Y'].item() <= 54) or (goal_x > 0 and attacker['X'].item() >= 89 and attacker['Y'].item() >= 14 and attacker['Y'].item() <= 54):
            #attacker is inside the penalty area
            front = ((GoalDis /2)* 0.05) + 3.75
            back = front * (1/3)
        else:
            #attacker is not in the penalty area
            front = (GoalDis * 0.05) + 3.75
            back = front * (1/3)
            
        Length = back + ((front - back)*(( Form **3) + ( Form * 0.3)) / 1.3)
        
        if distance > Length:
            pressure = 0
        else:
            pressure = (1 - distance / (Length))**1.75 *100
        
        
    # Case 2 : Defender is behind of the Attacker:
    if goal_x == 0 and defender['X'].item() < attacker['X'].item() or goal_x > 0 and defender['X'].item() > attacker['X'].item ():
        angle_between = angle_between + 180
        
        #defnition of pressure area 
        Form = (1 - (math.cos (math.radians(angle_between))))/2
        
        #definition of length of the pressure area dependent n the attacker position
        #gets smaller the closer the attacker gets to the goal
        #inside the penalty area GoalDis is diveded by 2 to increase the drop of the size of the pressure area 
        if (goal_x == 0 and attacker['X'].item() <= 16 and attacker['Y'].item() >= 14 and attacker['Y'].item() <= 54) or (goal_x > 0 and attacker['X'].item() >= 89 and attacker['Y'].item() >= 14 and attacker['Y'].item() <= 54):
            #attacker is inside the penalty area
            front = ((GoalDis /2)* 0.05) + 3.75
            back = front * (1/3)
        else:
            #attacker is not in the penalty area
            front = (GoalDis * 0.05) + 3.75
            back = front * (1/3)
            
        Length = back + ((front - back)*(( Form **3) + ( Form * 0.3)) / 1.3)
        
        if distance > Length:
            pressure = 0
        else:
            pressure = (1 - distance / (Length))**1.75 *100
    
    
    #Case 3: Defender is exactly beneath attacker
    if defender['X'].item() == attacker['X'].item():
        angle_between = 90
        
        #defnition of pressure area 
        Form = (1 - (math.cos (math.radians(angle_between))))/2
        
        #definition of length of the pressure area dependent n the attacker position
        #gets smaller the closer the attacker gets to the goal
        #inside the penalty area GoalDis is diveded by 2 to increase the drop of the size of the pressure area 
        if (goal_x == 0 and attacker['X'].item() <= 16 and attacker['Y'].item() >= 14 and attacker['Y'].item() <= 54) or (goal_x > 0 and attacker['X'].item() >= 89 and attacker['Y'].item() >= 14 and attacker['Y'].item() <= 54):
            #attacker is inside the penalty area
            front = ((GoalDis /2)* 0.05) + 3.75
            back = front * (1/3)
        else:
            #attacker is not in the penalty area
            front = (GoalDis * 0.05) + 3.75
            back = front * (1/3)
            
        Length = back + ((front - back)*(( Form **3) + ( Form * 0.3)) / 1.3)
        
        if distance > Length:
            pressure = 0
        else:
            pressure = (1 - distance / (Length))**1.75 *100
            
            
    #Case 4: Defender is in the same spot as attacker
    if defender['X'].item() == attacker['X'].item() and defender['Y'].item() == attacker['Y'].item():
        pressure = 100
    return pressure

#%%
# Measurement of defensive pressure:
    #time: 0,1,2,3,4 seconds before end of an attack
    #space: on ball (ball nearest player), on group (ball nearest players), on team (10 nearest players)

#Measurement for timestamp: 0

OnBallPressure0 = []
OnGroupPressure0_1  = []
OnGroupPressure0_2  = []
OnGroupPressure0_3  = []
OnGroupPressure0_4  = []
OnGroupPressure0_5  = []
OnGroupPressure0_6  = []
OnGroupPressure0_7  = []
OnGroupPressure0_8  = []
OnGroupPressure0_9  = []
OnGroupPressure0_10  = []

for row, attack in possessions.iterrows ():
    
    #calculation of timestamps for calculation of defensive pressure
    second_0 = attack.end_sync 
    
    identified_frames0 = position_data[position_data['T_sec'] == second_0]
    
    #Case 1: Team1 is in ball possession and plays from left to right
    if attack.team == team1 and attack.TeamLeft == team1:
        possible_attackers0 = identified_frames0[identified_frames0['TeamId'] == team1]
        possible_defenders0 = identified_frames0[identified_frames0['TeamId'] == team2]
        ball0 = identified_frames0[identified_frames0['TeamId'] == 'BALL']
        
        goal_x_to_play = 105
        goal_y_to_play = 34
    #Case 2: Team1 is in ball possession and plays from right to left 
    elif attack.team == team1 and attack.TeamRight == team1:
        possible_attackers0 = identified_frames0[identified_frames0['TeamId'] == team1]
        possible_defenders0 = identified_frames0[identified_frames0['TeamId'] == team2]
        ball0 = identified_frames0[identified_frames0['TeamId'] == 'BALL'] 
        
        goal_x_to_play = 0
        goal_y_to_play = 34
    #Case 3: Team2 is in ball possession and plays from left to right 
    elif attack.team == team2 and attack.TeamLeft == team2:
        possible_attackers0 = identified_frames0[identified_frames0['TeamId'] == team2]
        possible_defenders0 = identified_frames0[identified_frames0['TeamId'] == team1]
        ball0 = identified_frames0[identified_frames0['TeamId'] == 'BALL']
        
        goal_x_to_play = 105
        goal_y_to_play = 34
    #Case 4: Team2 is in ball possession and plays from right to left 
    elif attack.team == team2 and attack.TeamRight == team2:
        possible_attackers0 = identified_frames0[identified_frames0['TeamId'] == team2]
        possible_defenders0 = identified_frames0[identified_frames0['TeamId'] == team1]
        ball0 = identified_frames0[identified_frames0['TeamId'] == 'BALL']
        
        goal_x_to_play = 0
        goal_y_to_play = 34
    
    if len(possible_attackers0) == 11 and len(possible_defenders0) == 11:

        #Identification of all attackers sorted after distance to ball
        Dis = []
        for index2, attacker in possible_attackers0.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball0['X'].item())**2 + (attack['Y'].item() - ball0['Y'].item())**2)
            Dis.append (dis)
    
        possible_attackers0['DistanceToBall'] = Dis
    
        group_attackers0 = possible_attackers0.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker0_0 = group_attackers0.loc[[0]]
        group_attacker0_1 = group_attackers0.loc[[1]]
        group_attacker0_2 = group_attackers0.loc[[2]]
        group_attacker0_3 = group_attackers0.loc[[3]]
        group_attacker0_4 = group_attackers0.loc[[4]]
        group_attacker0_5 = group_attackers0.loc[[5]]
        group_attacker0_6 = group_attackers0.loc[[6]]
        group_attacker0_7 = group_attackers0.loc[[7]]
        group_attacker0_8 = group_attackers0.loc[[8]]
        group_attacker0_9 = group_attackers0.loc[[9]]
        group_attacker0_10 = group_attackers0.loc[[10]]
    
        #Calculation of pressure 
        Press_onball0 = []
        Press_ongroup0_1 = []
        Press_ongroup0_2 = []
        Press_ongroup0_3 = []
        Press_ongroup0_4 = []
        Press_ongroup0_5 = []
        Press_ongroup0_6 = []
        Press_ongroup0_7 = []
        Press_ongroup0_8 = []
        Press_ongroup0_9 = []
        Press_ongroup0_10 = []
    
        for index2, defender in possible_defenders0.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (group_attacker0_0, defend, goal_x_to_play, goal_y_to_play)
            Press_onball0.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker0_1, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup0_1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker0_2, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup0_2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker0_3, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup0_3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker0_4, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup0_4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker0_5, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup0_5.append (press_ongroup5)
        
            press_ongroup6 = pressure_quantification (group_attacker0_6, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup0_6.append (press_ongroup6)
        
            press_ongroup7 = pressure_quantification (group_attacker0_7, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup0_7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker0_8, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup0_8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker0_9, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup0_9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker0_10, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup0_10.append (press_ongroup10)
            
        onballpressure0 = max (Press_onball0)
        ongrouppressure0_1 = max (Press_ongroup0_1)
        ongrouppressure0_2 = max (Press_ongroup0_2)
        ongrouppressure0_3 = max (Press_ongroup0_3)
        ongrouppressure0_4 = max (Press_ongroup0_4)
        ongrouppressure0_5 = max (Press_ongroup0_5)
        ongrouppressure0_6 = max (Press_ongroup0_6)
        ongrouppressure0_7 = max (Press_ongroup0_7)
        ongrouppressure0_8 = max (Press_ongroup0_8)
        ongrouppressure0_9 = max (Press_ongroup0_9)
        ongrouppressure0_10 = max (Press_ongroup0_10)
    
    else:
        onballpressure0 = None
        ongrouppressure0_1 = None
        ongrouppressure0_2 = None
        ongrouppressure0_3 = None
        ongrouppressure0_4 = None
        ongrouppressure0_5 = None
        ongrouppressure0_6 = None
        ongrouppressure0_7 = None
        ongrouppressure0_8 = None
        ongrouppressure0_9 = None
        ongrouppressure0_10 = None
        

    OnBallPressure0.append (onballpressure0)
    OnGroupPressure0_1.append (ongrouppressure0_1)
    OnGroupPressure0_2.append (ongrouppressure0_2)
    OnGroupPressure0_3.append (ongrouppressure0_3)
    OnGroupPressure0_4.append (ongrouppressure0_4)
    OnGroupPressure0_5.append (ongrouppressure0_5)
    OnGroupPressure0_6.append (ongrouppressure0_6)
    OnGroupPressure0_7.append (ongrouppressure0_7)
    OnGroupPressure0_8.append (ongrouppressure0_8)
    OnGroupPressure0_9.append (ongrouppressure0_9)
    OnGroupPressure0_10.append (ongrouppressure0_10)
#%%
#Measurement for timestamp: 1

OnBallPressure1 = []
OnGroupPressure1_1  = []
OnGroupPressure1_2  = []
OnGroupPressure1_3  = []
OnGroupPressure1_4  = []
OnGroupPressure1_5  = []
OnGroupPressure1_6  = []
OnGroupPressure1_7  = []
OnGroupPressure1_8  = []
OnGroupPressure1_9  = []
OnGroupPressure1_10  = []

for row, attack in possessions.iterrows ():
    
    #calculation of timestamps for calculation of defensive pressure
    second_1 = attack.end_sync - 1
    
    identified_frames1 = position_data[position_data['T_sec'] == second_1]
    
    #Case 1: Team1 is in ball possession and plays from left to right
    if attack.team == team1 and attack.TeamLeft == team1:
        possible_attackers1 = identified_frames1[identified_frames1['TeamId'] == team1]
        possible_defenders1 = identified_frames1[identified_frames1['TeamId'] == team2]
        ball1 = identified_frames1[identified_frames1['TeamId'] == 'BALL']
        
        goal_x_to_play = 105
        goal_y_to_play = 34
    #Case 2: Team1 is in ball possession and plays from right to left 
    elif attack.team == team1 and attack.TeamRight == team1:
        possible_attackers1 = identified_frames1[identified_frames1['TeamId'] == team1]
        possible_defenders1 = identified_frames1[identified_frames1['TeamId'] == team2]
        ball1 = identified_frames1[identified_frames1['TeamId'] == 'BALL'] 
        
        goal_x_to_play = 0
        goal_y_to_play = 34
    #Case 3: Team2 is in ball possession and plays from left to right 
    elif attack.team == team2 and attack.TeamLeft == team2:
        possible_attackers1 = identified_frames1[identified_frames1['TeamId'] == team2]
        possible_defenders1 = identified_frames1[identified_frames1['TeamId'] == team1]
        ball1 = identified_frames1[identified_frames1['TeamId'] == 'BALL']
        
        goal_x_to_play = 105
        goal_y_to_play = 34
    #Case 4: Team2 is in ball possession and plays from right to left 
    elif attack.team == team2 and attack.TeamRight == team2:
        possible_attackers1 = identified_frames1[identified_frames1['TeamId'] == team2]
        possible_defenders1 = identified_frames1[identified_frames1['TeamId'] == team1]
        ball1 = identified_frames1[identified_frames1['TeamId'] == 'BALL']
        
        goal_x_to_play = 0
        goal_y_to_play = 34
    
    if len(possible_attackers1) == 11 and len(possible_defenders1) == 11:
        
        #Identification of all attackers sorted after distance to ball
        Dis = []
        for index2, attacker in possible_attackers1.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball1['X'].item())**2 + (attack['Y'].item() - ball1['Y'].item())**2)
            Dis.append (dis)
    
        possible_attackers1['DistanceToBall'] = Dis
    
        group_attackers1 = possible_attackers1.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker1_0 = group_attackers1.loc[[0]]
        group_attacker1_1 = group_attackers1.loc[[1]]
        group_attacker1_2 = group_attackers1.loc[[2]]
        group_attacker1_3 = group_attackers1.loc[[3]]
        group_attacker1_4 = group_attackers1.loc[[4]]
        group_attacker1_5 = group_attackers1.loc[[5]]
        group_attacker1_6 = group_attackers1.loc[[6]]
        group_attacker1_7 = group_attackers1.loc[[7]]
        group_attacker1_8 = group_attackers1.loc[[8]]
        group_attacker1_9 = group_attackers1.loc[[9]]
        group_attacker1_10 = group_attackers1.loc[[10]]
    
        #Calculation of pressure 
        Press_onball1 = []
        Press_ongroup1_1 = []
        Press_ongroup1_2 = []
        Press_ongroup1_3 = []
        Press_ongroup1_4 = []
        Press_ongroup1_5 = []
        Press_ongroup1_6 = []
        Press_ongroup1_7 = []
        Press_ongroup1_8 = []
        Press_ongroup1_9 = []
        Press_ongroup1_10 = []
    
        for index2, defender in possible_defenders1.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (group_attacker1_0, defend, goal_x_to_play, goal_y_to_play)
            Press_onball1.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker1_1, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup1_1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker1_2, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup1_2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker1_3, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup1_3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker1_4, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup1_4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker1_5, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup1_5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker1_6, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup1_6.append (press_ongroup6)
        
            press_ongroup7 = pressure_quantification (group_attacker1_7, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup1_7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker1_8, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup1_8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker1_9, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup1_9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker1_10, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup1_10.append (press_ongroup10)
            
        onballpressure1 = max (Press_onball1)
        ongrouppressure1_1 = max (Press_ongroup1_1)
        ongrouppressure1_2 = max (Press_ongroup1_2)
        ongrouppressure1_3 = max (Press_ongroup1_3)
        ongrouppressure1_4 = max (Press_ongroup1_4)
        ongrouppressure1_5 = max (Press_ongroup1_5)
        ongrouppressure1_6 = max (Press_ongroup1_6)
        ongrouppressure1_7 = max (Press_ongroup1_7)
        ongrouppressure1_8 = max (Press_ongroup1_8)
        ongrouppressure1_9 = max (Press_ongroup1_9)
        ongrouppressure1_10 = max (Press_ongroup1_10)
    else:
        onballpressure1 = None
        ongrouppressure1_1 = None
        ongrouppressure1_2 = None
        ongrouppressure1_3 = None
        ongrouppressure1_4 = None
        ongrouppressure1_5 = None
        ongrouppressure1_6 = None
        ongrouppressure1_7 = None
        ongrouppressure1_8 = None
        ongrouppressure1_9 = None
        ongrouppressure1_10 = None

    OnBallPressure1.append (onballpressure1)
    OnGroupPressure1_1.append (ongrouppressure1_1)
    OnGroupPressure1_2.append (ongrouppressure1_2)
    OnGroupPressure1_3.append (ongrouppressure1_3)
    OnGroupPressure1_4.append (ongrouppressure1_4)
    OnGroupPressure1_5.append (ongrouppressure1_5)
    OnGroupPressure1_6.append (ongrouppressure1_6)
    OnGroupPressure1_7.append (ongrouppressure1_7)
    OnGroupPressure1_8.append (ongrouppressure1_8)
    OnGroupPressure1_9.append (ongrouppressure1_9)
    OnGroupPressure1_10.append (ongrouppressure1_10)
#%%
#Measurement for timestamp: 2

OnBallPressure2 = []
OnGroupPressure2_1  = []
OnGroupPressure2_2  = []
OnGroupPressure2_3  = []
OnGroupPressure2_4  = []
OnGroupPressure2_5  = []
OnGroupPressure2_6  = []
OnGroupPressure2_7  = []
OnGroupPressure2_8  = []
OnGroupPressure2_9  = []
OnGroupPressure2_10  = []

for row, attack in possessions.iterrows ():
    
    #calculation of timestamps for calculation of defensive pressure
    second_2 = attack.end_sync - 2
    
    identified_frames2 = position_data[position_data['T_sec'] == second_2]
    
    #Case 1: Team1 is in ball possession and plays from left to right
    if attack.team == team1 and attack.TeamLeft == team1:
        possible_attackers2 = identified_frames2[identified_frames2['TeamId'] == team1]
        possible_defenders2 = identified_frames2[identified_frames2['TeamId'] == team2]
        ball2 = identified_frames2[identified_frames2['TeamId'] == 'BALL']
        
        goal_x_to_play = 105
        goal_y_to_play = 34
    #Case 2: Team1 is in ball possession and plays from right to left 
    elif attack.team == team1 and attack.TeamRight == team1:
        possible_attackers2 = identified_frames2[identified_frames2['TeamId'] == team1]
        possible_defenders2 = identified_frames2[identified_frames2['TeamId'] == team2]
        ball2 = identified_frames2[identified_frames2['TeamId'] == 'BALL'] 
        
        goal_x_to_play = 0
        goal_y_to_play = 34
    #Case 3: Team2 is in ball possession and plays from left to right 
    elif attack.team == team2 and attack.TeamLeft == team2:
        possible_attackers2 = identified_frames2[identified_frames2['TeamId'] == team2]
        possible_defenders2 = identified_frames2[identified_frames2['TeamId'] == team1]
        ball2 = identified_frames2[identified_frames2['TeamId'] == 'BALL']
        
        goal_x_to_play = 105
        goal_y_to_play = 34
    #Case 4: Team2 is in ball possession and plays from right to left 
    elif attack.team == team2 and attack.TeamRight == team2:
        possible_attackers2 = identified_frames2[identified_frames2['TeamId'] == team2]
        possible_defenders2 = identified_frames2[identified_frames2['TeamId'] == team1]
        ball2 = identified_frames2[identified_frames2['TeamId'] == 'BALL']
        
        goal_x_to_play = 0
        goal_y_to_play = 34
        
    if len(possible_attackers2) == 11 and len(possible_defenders2) == 11:
   
        #Identification of all attackers sorted after distance to ball
        Dis = []
        for index2, attacker in possible_attackers2.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball2['X'].item())**2 + (attack['Y'].item() - ball2['Y'].item())**2)
            Dis.append (dis)
    
        possible_attackers2['DistanceToBall'] = Dis
    
        group_attackers2 = possible_attackers2.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker2_0 = group_attackers2.loc[[0]]
        group_attacker2_1 = group_attackers2.loc[[1]]
        group_attacker2_2 = group_attackers2.loc[[2]]
        group_attacker2_3 = group_attackers2.loc[[3]]
        group_attacker2_4 = group_attackers2.loc[[4]]
        group_attacker2_5 = group_attackers2.loc[[5]]
        group_attacker2_6 = group_attackers2.loc[[6]]
        group_attacker2_7 = group_attackers2.loc[[7]]
        group_attacker2_8 = group_attackers2.loc[[8]]
        group_attacker2_9 = group_attackers2.loc[[9]]
        group_attacker2_10 = group_attackers2.loc[[10]]
    
        #Calculation of pressure 
        Press_onball2 = []
        Press_ongroup2_1 = []
        Press_ongroup2_2 = []
        Press_ongroup2_3 = []
        Press_ongroup2_4 = []
        Press_ongroup2_5 = []
        Press_ongroup2_6 = []
        Press_ongroup2_7 = []
        Press_ongroup2_8 = []
        Press_ongroup2_9 = []
        Press_ongroup2_10 = []
    
        for index2, defender in possible_defenders2.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (group_attacker2_0, defend, goal_x_to_play, goal_y_to_play)
            Press_onball2.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker2_1, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup2_1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker2_2, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup2_2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker2_3, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup2_3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker2_4, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup2_4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker2_5, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup2_5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker2_6, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup2_6.append (press_ongroup6)
        
            press_ongroup7 = pressure_quantification (group_attacker2_7, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup2_7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker2_8, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup2_8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker2_9, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup2_9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker2_10, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup2_10.append (press_ongroup10)
        
        onballpressure2 = max (Press_onball2)
        ongrouppressure2_1 = max (Press_ongroup2_1)
        ongrouppressure2_2 = max (Press_ongroup2_2)
        ongrouppressure2_3 = max (Press_ongroup2_3)
        ongrouppressure2_4 = max (Press_ongroup2_4)
        ongrouppressure2_5 = max (Press_ongroup2_5)
        ongrouppressure2_6 = max (Press_ongroup2_6)
        ongrouppressure2_7 = max (Press_ongroup2_7)
        ongrouppressure2_8 = max (Press_ongroup2_8)
        ongrouppressure2_9 = max (Press_ongroup2_9)
        ongrouppressure2_10 = max (Press_ongroup2_10)
        
    else:
        onballpressure2 = None
        ongrouppressure2_1 = None
        ongrouppressure2_2 = None
        ongrouppressure2_3 = None
        ongrouppressure2_4 = None
        ongrouppressure2_5 = None
        ongrouppressure2_6 = None
        ongrouppressure2_7 = None
        ongrouppressure2_8 = None
        ongrouppressure2_9 = None
        ongrouppressure2_10 = None

    OnBallPressure2.append (onballpressure2)
    OnGroupPressure2_1.append (ongrouppressure2_1)
    OnGroupPressure2_2.append (ongrouppressure2_2)
    OnGroupPressure2_3.append (ongrouppressure2_3)
    OnGroupPressure2_4.append (ongrouppressure2_4)
    OnGroupPressure2_5.append (ongrouppressure2_5)
    OnGroupPressure2_6.append (ongrouppressure2_6)
    OnGroupPressure2_7.append (ongrouppressure2_7)
    OnGroupPressure2_8.append (ongrouppressure2_8)
    OnGroupPressure2_9.append (ongrouppressure2_9)
    OnGroupPressure2_10.append (ongrouppressure2_10)


#%%
#Measurement for timestamp: 3

OnBallPressure3 = []
OnGroupPressure3_1  = []
OnGroupPressure3_2  = []
OnGroupPressure3_3  = []
OnGroupPressure3_4  = []
OnGroupPressure3_5  = []
OnGroupPressure3_6  = []
OnGroupPressure3_7  = []
OnGroupPressure3_8  = []
OnGroupPressure3_9  = []
OnGroupPressure3_10  = []

for row, attack in possessions.iterrows ():
    
    #calculation of timestamps for calculation of defensive pressure
    second_3 = attack.end_sync - 3
    
    identified_frames3 = position_data[position_data['T_sec'] == second_3]
    
    #Case 1: Team1 is in ball possession and plays from left to right
    if attack.team == team1 and attack.TeamLeft == team1:
        possible_attackers3 = identified_frames3[identified_frames3['TeamId'] == team1]
        possible_defenders3 = identified_frames3[identified_frames3['TeamId'] == team2]
        ball3 = identified_frames3[identified_frames3['TeamId'] == 'BALL']
        
        goal_x_to_play = 105
        goal_y_to_play = 34
    #Case 2: Team1 is in ball possession and plays from right to left 
    elif attack.team == team1 and attack.TeamRight == team1:
        possible_attackers3 = identified_frames3[identified_frames3['TeamId'] == team1]
        possible_defenders3 = identified_frames3[identified_frames3['TeamId'] == team2]
        ball3 = identified_frames3[identified_frames3['TeamId'] == 'BALL'] 
        
        goal_x_to_play = 0
        goal_y_to_play = 34
    #Case 3: Team2 is in ball possession and plays from left to right 
    elif attack.team == team2 and attack.TeamLeft == team2:
        possible_attackers3 = identified_frames3[identified_frames3['TeamId'] == team2]
        possible_defenders3 = identified_frames3[identified_frames3['TeamId'] == team1]
        ball3 = identified_frames3[identified_frames3['TeamId'] == 'BALL']
        
        goal_x_to_play = 105
        goal_y_to_play = 34
    #Case 4: Team2 is in ball possession and plays from right to left 
    elif attack.team == team2 and attack.TeamRight == team2:
        possible_attackers3 = identified_frames3[identified_frames3['TeamId'] == team2]
        possible_defenders3 = identified_frames3[identified_frames3['TeamId'] == team1]
        ball3 = identified_frames3[identified_frames3['TeamId'] == 'BALL']
        
        goal_x_to_play = 0
        goal_y_to_play = 34
        
    if len(possible_attackers3) == 11 and len(possible_defenders3) == 11:   
   
        #Identification of all attackers sorted after distance to ball
        Dis = []
        for index2, attacker in possible_attackers3.iterrows ():
            attack = pd.DataFrame (attacker)
            attack = attack.transpose ()
            dis = math.sqrt((attack['X'].item() - ball3['X'].item())**2 + (attack['Y'].item() - ball3['Y'].item())**2)
            Dis.append (dis)
    
        possible_attackers3['DistanceToBall'] = Dis
    
        group_attackers3 = possible_attackers3.sort_values (by=['DistanceToBall']).reset_index()
    
        group_attacker3_0 = group_attackers3.loc[[0]]
        group_attacker3_1 = group_attackers3.loc[[1]]
        group_attacker3_2 = group_attackers3.loc[[2]]
        group_attacker3_3 = group_attackers3.loc[[3]]
        group_attacker3_4 = group_attackers3.loc[[4]]
        group_attacker3_5 = group_attackers3.loc[[5]]
        group_attacker3_6 = group_attackers3.loc[[6]]
        group_attacker3_7 = group_attackers3.loc[[7]]
        group_attacker3_8 = group_attackers3.loc[[8]]
        group_attacker3_9 = group_attackers3.loc[[9]]
        group_attacker3_10 = group_attackers3.loc[[10]]
    
        #Calculation of pressure 
        Press_onball3 = []
        Press_ongroup3_1 = []
        Press_ongroup3_2 = []
        Press_ongroup3_3 = []
        Press_ongroup3_4 = []
        Press_ongroup3_5 = []
        Press_ongroup3_6 = []
        Press_ongroup3_7 = []
        Press_ongroup3_8 = []
        Press_ongroup3_9 = []
        Press_ongroup3_10 = []
    
        for index2, defender in possible_defenders3.iterrows ():
            defend = pd.DataFrame (defender)
            defend = defend.transpose ()
    
            press_onball = pressure_quantification (group_attacker3_0, defend, goal_x_to_play, goal_y_to_play)
            Press_onball3.append (press_onball)
            
            press_ongroup1 = pressure_quantification (group_attacker3_1, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup3_1.append (press_ongroup1)
            
            press_ongroup2 = pressure_quantification (group_attacker3_2, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup3_2.append (press_ongroup2)
            
            press_ongroup3 = pressure_quantification (group_attacker3_3, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup3_3.append (press_ongroup3)
            
            press_ongroup4 = pressure_quantification (group_attacker3_4, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup3_4.append (press_ongroup4)
            
            press_ongroup5 = pressure_quantification (group_attacker3_5, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup3_5.append (press_ongroup5)
            
            press_ongroup6 = pressure_quantification (group_attacker3_6, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup3_6.append (press_ongroup6)
        
            press_ongroup7 = pressure_quantification (group_attacker3_7, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup3_7.append (press_ongroup7)
            
            press_ongroup8 = pressure_quantification (group_attacker3_8, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup3_8.append (press_ongroup8)
            
            press_ongroup9 = pressure_quantification (group_attacker3_9, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup3_9.append (press_ongroup9)
            
            press_ongroup10 = pressure_quantification (group_attacker3_10, defend, goal_x_to_play, goal_y_to_play)
            Press_ongroup3_10.append (press_ongroup10)
            
        onballpressure3 = max (Press_onball3)
        ongrouppressure3_1 = max (Press_ongroup3_1)
        ongrouppressure3_2 = max (Press_ongroup3_2)
        ongrouppressure3_3 = max (Press_ongroup3_3)
        ongrouppressure3_4 = max (Press_ongroup3_4)
        ongrouppressure3_5 = max (Press_ongroup3_5)
        ongrouppressure3_6 = max (Press_ongroup3_6)
        ongrouppressure3_7 = max (Press_ongroup3_7)
        ongrouppressure3_8 = max (Press_ongroup3_8)
        ongrouppressure3_9 = max (Press_ongroup3_9)
        ongrouppressure3_10 = max (Press_ongroup3_10)
    else:
        onballpressure3 = None
        ongrouppressure3_1 = None
        ongrouppressure3_2 = None
        ongrouppressure3_3 = None
        ongrouppressure3_4 = None
        ongrouppressure3_5 = None
        ongrouppressure3_6 = None
        ongrouppressure3_7 = None
        ongrouppressure3_8 = None
        ongrouppressure3_9 = None
        ongrouppressure3_10 = None

    OnBallPressure3.append (onballpressure3)
    OnGroupPressure3_1.append (ongrouppressure3_1)
    OnGroupPressure3_2.append (ongrouppressure3_2)
    OnGroupPressure3_3.append (ongrouppressure3_3)
    OnGroupPressure3_4.append (ongrouppressure3_4)
    OnGroupPressure3_5.append (ongrouppressure3_5)
    OnGroupPressure3_6.append (ongrouppressure3_6)
    OnGroupPressure3_7.append (ongrouppressure3_7)
    OnGroupPressure3_8.append (ongrouppressure3_8)
    OnGroupPressure3_9.append (ongrouppressure3_9)
    OnGroupPressure3_10.append (ongrouppressure3_10)

#%%
#Measurement for timestamp: 4

OnBallPressure4 = []
OnGroupPressure4_1  = []
OnGroupPressure4_2  = []
OnGroupPressure4_3  = []
OnGroupPressure4_4  = []
OnGroupPressure4_5  = []
OnGroupPressure4_6  = []
OnGroupPressure4_7  = []
OnGroupPressure4_8  = []
OnGroupPressure4_9  = []
OnGroupPressure4_10  = []

for row, attack in possessions.iterrows ():
    if attack.duration_sync >= 4:
        #calculation of timestamps for calculation of defensive pressure
        second_4 = attack.end_sync - 4
        
        identified_frames4 = position_data[position_data['T_sec'] == second_4]
        
        #Case 1: Team1 is in ball possession and plays from left to right
        if attack.team == team1 and attack.TeamLeft == team1:
            possible_attackers4 = identified_frames4[identified_frames4['TeamId'] == team1]
            possible_defenders4 = identified_frames4[identified_frames4['TeamId'] == team2]
            ball4 = identified_frames4[identified_frames4['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 2: Team1 is in ball possession and plays from right to left 
        elif attack.team == team1 and attack.TeamRight == team1:
            possible_attackers4 = identified_frames4[identified_frames4['TeamId'] == team1]
            possible_defenders4 = identified_frames4[identified_frames4['TeamId'] == team2]
            ball4 = identified_frames4[identified_frames4['TeamId'] == 'BALL'] 
            
            goal_x_to_play = 0
            goal_y_to_play = 34
        #Case 3: Team2 is in ball possession and plays from left to right 
        elif attack.team == team2 and attack.TeamLeft == team2:
            possible_attackers4 = identified_frames4[identified_frames4['TeamId'] == team2]
            possible_defenders4 = identified_frames4[identified_frames4['TeamId'] == team1]
            ball4 = identified_frames4[identified_frames4['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 4: Team2 is in ball possession and plays from right to left 
        elif attack.team == team2 and attack.TeamRight == team2:
            possible_attackers4 = identified_frames4[identified_frames4['TeamId'] == team2]
            possible_defenders4 = identified_frames4[identified_frames4['TeamId'] == team1]
            ball4 = identified_frames4[identified_frames4['TeamId'] == 'BALL']
            
            goal_x_to_play = 0
            goal_y_to_play = 34
            
        if len(possible_attackers4) == 11 and len(possible_defenders4) == 11:   
       
            #Identification of all attackers sorted after distance to ball
            Dis = []
            for index2, attacker in possible_attackers4.iterrows ():
                attack = pd.DataFrame (attacker)
                attack = attack.transpose ()
                dis = math.sqrt((attack['X'].item() - ball4['X'].item())**2 + (attack['Y'].item() - ball4['Y'].item())**2)
                Dis.append (dis)
        
            possible_attackers4['DistanceToBall'] = Dis
        
            group_attackers4 = possible_attackers4.sort_values (by=['DistanceToBall']).reset_index()
        
            group_attacker4_0 = group_attackers4.loc[[0]]
            group_attacker4_1 = group_attackers4.loc[[1]]
            group_attacker4_2 = group_attackers4.loc[[2]]
            group_attacker4_3 = group_attackers4.loc[[3]]
            group_attacker4_4 = group_attackers4.loc[[4]]
            group_attacker4_5 = group_attackers4.loc[[5]]
            group_attacker4_6 = group_attackers4.loc[[6]]
            group_attacker4_7 = group_attackers4.loc[[7]]
            group_attacker4_8 = group_attackers4.loc[[8]]
            group_attacker4_9 = group_attackers4.loc[[9]]
            group_attacker4_10 = group_attackers4.loc[[10]]
        
            #Calculation of pressure 
            Press_onball4 = []
            Press_ongroup4_1 = []
            Press_ongroup4_2 = []
            Press_ongroup4_3 = []
            Press_ongroup4_4 = []
            Press_ongroup4_5 = []
            Press_ongroup4_6 = []
            Press_ongroup4_7 = []
            Press_ongroup4_8 = []
            Press_ongroup4_9 = []
            Press_ongroup4_10 = []
        
            for index2, defender in possible_defenders4.iterrows ():
                defend = pd.DataFrame (defender)
                defend = defend.transpose ()
        
                press_onball = pressure_quantification (group_attacker4_0, defend, goal_x_to_play, goal_y_to_play)
                Press_onball4.append (press_onball)
                
                press_ongroup1 = pressure_quantification (group_attacker4_1, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup4_1.append (press_ongroup1)
                
                press_ongroup2 = pressure_quantification (group_attacker4_2, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup4_2.append (press_ongroup2)
                
                press_ongroup3 = pressure_quantification (group_attacker4_3, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup4_3.append (press_ongroup3)
                
                press_ongroup4 = pressure_quantification (group_attacker4_4, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup4_4.append (press_ongroup4)
                
                press_ongroup5 = pressure_quantification (group_attacker4_5, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup4_5.append (press_ongroup5)
                
                press_ongroup6 = pressure_quantification (group_attacker4_6, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup4_6.append (press_ongroup6)
            
                press_ongroup7 = pressure_quantification (group_attacker4_7, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup4_7.append (press_ongroup7)
                
                press_ongroup8 = pressure_quantification (group_attacker4_8, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup4_8.append (press_ongroup8)
                
                press_ongroup9 = pressure_quantification (group_attacker4_9, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup4_9.append (press_ongroup9)
                
                press_ongroup10 = pressure_quantification (group_attacker4_10, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup4_10.append (press_ongroup10)
                
            onballpressure4 = max (Press_onball4)
            ongrouppressure4_1 = max (Press_ongroup4_1)
            ongrouppressure4_2 = max (Press_ongroup4_2)
            ongrouppressure4_3 = max (Press_ongroup4_3)
            ongrouppressure4_4 = max (Press_ongroup4_4)
            ongrouppressure4_5 = max (Press_ongroup4_5)
            ongrouppressure4_6 = max (Press_ongroup4_6)
            ongrouppressure4_7 = max (Press_ongroup4_7)
            ongrouppressure4_8 = max (Press_ongroup4_8)
            ongrouppressure4_9 = max (Press_ongroup4_9)
            ongrouppressure4_10 = max (Press_ongroup4_10)
        else:
            onballpressure4 = None
            ongrouppressure4_1 = None
            ongrouppressure4_2 = None
            ongrouppressure4_3 = None
            ongrouppressure4_4 = None
            ongrouppressure4_5 = None
            ongrouppressure4_6 = None
            ongrouppressure4_7 = None
            ongrouppressure4_8 = None
            ongrouppressure4_9 = None
            ongrouppressure4_10 = None
    else: 
        onballpressure4 = None
        ongrouppressure4_1 = None
        ongrouppressure4_2 = None
        ongrouppressure4_3 = None
        ongrouppressure4_4 = None
        ongrouppressure4_5 = None
        ongrouppressure4_6 = None
        ongrouppressure4_7 = None
        ongrouppressure4_8 = None
        ongrouppressure4_9 = None
        ongrouppressure4_10 = None

    OnBallPressure4.append (onballpressure4)
    OnGroupPressure4_1.append (ongrouppressure4_1)
    OnGroupPressure4_2.append (ongrouppressure4_2)
    OnGroupPressure4_3.append (ongrouppressure4_3)
    OnGroupPressure4_4.append (ongrouppressure4_4)
    OnGroupPressure4_5.append (ongrouppressure4_5)
    OnGroupPressure4_6.append (ongrouppressure4_6)
    OnGroupPressure4_7.append (ongrouppressure4_7)
    OnGroupPressure4_8.append (ongrouppressure4_8)
    OnGroupPressure4_9.append (ongrouppressure4_9)
    OnGroupPressure4_10.append (ongrouppressure4_10)

#%%
#Measurement for timestamp: 5

OnBallPressure5 = []
OnGroupPressure5_1  = []
OnGroupPressure5_2  = []
OnGroupPressure5_3  = []
OnGroupPressure5_4  = []
OnGroupPressure5_5  = []
OnGroupPressure5_6  = []
OnGroupPressure5_7  = []
OnGroupPressure5_8  = []
OnGroupPressure5_9  = []
OnGroupPressure5_10  = []

for row, attack in possessions.iterrows ():
    if attack.duration_sync >= 5:
        #calculation of timestamps for calculation of defensive pressure
        second_5 = attack.end_sync - 5
        
        identified_frames5 = position_data[position_data['T_sec'] == second_5]
        
        #Case 1: Team1 is in ball possession and plays from left to right
        if attack.team == team1 and attack.TeamLeft == team1:
            possible_attackers5 = identified_frames5[identified_frames5['TeamId'] == team1]
            possible_defenders5 = identified_frames5[identified_frames5['TeamId'] == team2]
            ball5 = identified_frames5[identified_frames5['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 2: Team1 is in ball possession and plays from right to left 
        elif attack.team == team1 and attack.TeamRight == team1:
            possible_attackers5 = identified_frames5[identified_frames5['TeamId'] == team1]
            possible_defenders5 = identified_frames5[identified_frames5['TeamId'] == team2]
            ball5 = identified_frames5[identified_frames5['TeamId'] == 'BALL'] 
            
            goal_x_to_play = 0
            goal_y_to_play = 34
        #Case 3: Team2 is in ball possession and plays from left to right 
        elif attack.team == team2 and attack.TeamLeft == team2:
            possible_attackers5 = identified_frames5[identified_frames5['TeamId'] == team2]
            possible_defenders5 = identified_frames5[identified_frames5['TeamId'] == team1]
            ball5 = identified_frames5[identified_frames5['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 4: Team2 is in ball possession and plays from right to left 
        elif attack.team == team2 and attack.TeamRight == team2:
            possible_attackers5 = identified_frames5[identified_frames5['TeamId'] == team2]
            possible_defenders5 = identified_frames5[identified_frames5['TeamId'] == team1]
            ball5 = identified_frames5[identified_frames5['TeamId'] == 'BALL']
            
            goal_x_to_play = 0
            goal_y_to_play = 34
            
        if len(possible_attackers5) == 11 and len(possible_defenders5) == 11: 
       
            #Identification of all attackers sorted after distance to ball
            Dis = []
            for index2, attacker in possible_attackers5.iterrows ():
                attack = pd.DataFrame (attacker)
                attack = attack.transpose ()
                dis = math.sqrt((attack['X'].item() - ball5['X'].item())**2 + (attack['Y'].item() - ball5['Y'].item())**2)
                Dis.append (dis)
        
            possible_attackers5['DistanceToBall'] = Dis
        
            group_attackers5 = possible_attackers5.sort_values (by=['DistanceToBall']).reset_index()
        
            group_attacker5_0 = group_attackers5.loc[[0]]
            group_attacker5_1 = group_attackers5.loc[[1]]
            group_attacker5_2 = group_attackers5.loc[[2]]
            group_attacker5_3 = group_attackers5.loc[[3]]
            group_attacker5_4 = group_attackers5.loc[[4]]
            group_attacker5_5 = group_attackers5.loc[[5]]
            group_attacker5_6 = group_attackers5.loc[[6]]
            group_attacker5_7 = group_attackers5.loc[[7]]
            group_attacker5_8 = group_attackers5.loc[[8]]
            group_attacker5_9 = group_attackers5.loc[[9]]
            group_attacker5_10 = group_attackers5.loc[[10]]
        
            #Calculation of pressure 
            Press_onball5 = []
            Press_ongroup5_1 = []
            Press_ongroup5_2 = []
            Press_ongroup5_3 = []
            Press_ongroup5_4 = []
            Press_ongroup5_5 = []
            Press_ongroup5_6 = []
            Press_ongroup5_7 = []
            Press_ongroup5_8 = []
            Press_ongroup5_9 = []
            Press_ongroup5_10 = []
        
            for index2, defender in possible_defenders5.iterrows ():
                defend = pd.DataFrame (defender)
                defend = defend.transpose ()
        
                press_onball = pressure_quantification (group_attacker5_0, defend, goal_x_to_play, goal_y_to_play)
                Press_onball5.append (press_onball)
                
                press_ongroup1 = pressure_quantification (group_attacker5_1, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup5_1.append (press_ongroup1)
                
                press_ongroup2 = pressure_quantification (group_attacker5_2, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup5_2.append (press_ongroup2)
                
                press_ongroup3 = pressure_quantification (group_attacker5_3, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup5_3.append (press_ongroup3)
                
                press_ongroup4 = pressure_quantification (group_attacker5_4, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup5_4.append (press_ongroup4)
                
                press_ongroup5 = pressure_quantification (group_attacker5_5, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup5_5.append (press_ongroup5)
                
                press_ongroup6 = pressure_quantification (group_attacker5_6, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup5_6.append (press_ongroup6)
            
                press_ongroup7 = pressure_quantification (group_attacker5_7, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup5_7.append (press_ongroup7)
                
                press_ongroup8 = pressure_quantification (group_attacker5_8, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup5_8.append (press_ongroup8)
                
                press_ongroup9 = pressure_quantification (group_attacker5_9, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup5_9.append (press_ongroup9)
                
                press_ongroup10 = pressure_quantification (group_attacker5_10, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup5_10.append (press_ongroup10)
                
            onballpressure5 = max (Press_onball5)
            ongrouppressure5_1 = max (Press_ongroup5_1)
            ongrouppressure5_2 = max (Press_ongroup5_2)
            ongrouppressure5_3 = max (Press_ongroup5_3)
            ongrouppressure5_4 = max (Press_ongroup5_4)
            ongrouppressure5_5 = max (Press_ongroup5_5)
            ongrouppressure5_6 = max (Press_ongroup5_6)
            ongrouppressure5_7 = max (Press_ongroup5_7)
            ongrouppressure5_8 = max (Press_ongroup5_8)
            ongrouppressure5_9 = max (Press_ongroup5_9)
            ongrouppressure5_10 = max (Press_ongroup5_10)
        else:
            onballpressure5 = None
            ongrouppressure5_1 = None
            ongrouppressure5_2 = None
            ongrouppressure5_3 = None
            ongrouppressure5_4 = None
            ongrouppressure5_5 = None
            ongrouppressure5_6 = None
            ongrouppressure5_7 = None
            ongrouppressure5_8 = None
            ongrouppressure5_9 = None
            ongrouppressure5_10 = None
    else: 
        onballpressure5 = None
        ongrouppressure5_1 = None
        ongrouppressure5_2 = None
        ongrouppressure5_3 = None
        ongrouppressure5_4 = None
        ongrouppressure5_5 = None
        ongrouppressure5_6 = None
        ongrouppressure5_7 = None
        ongrouppressure5_8 = None
        ongrouppressure5_9 = None
        ongrouppressure5_10 = None

    OnBallPressure5.append (onballpressure5)
    OnGroupPressure5_1.append (ongrouppressure5_1)
    OnGroupPressure5_2.append (ongrouppressure5_2)
    OnGroupPressure5_3.append (ongrouppressure5_3)
    OnGroupPressure5_4.append (ongrouppressure5_4)
    OnGroupPressure5_5.append (ongrouppressure5_5)
    OnGroupPressure5_6.append (ongrouppressure5_6)
    OnGroupPressure5_7.append (ongrouppressure5_7)
    OnGroupPressure5_8.append (ongrouppressure5_8)
    OnGroupPressure5_9.append (ongrouppressure5_9)
    OnGroupPressure5_10.append (ongrouppressure5_10)

#%%
#Measurement for timestamp: 6

OnBallPressure6 = []
OnGroupPressure6_1  = []
OnGroupPressure6_2  = []
OnGroupPressure6_3  = []
OnGroupPressure6_4  = []
OnGroupPressure6_5  = []
OnGroupPressure6_6  = []
OnGroupPressure6_7  = []
OnGroupPressure6_8  = []
OnGroupPressure6_9  = []
OnGroupPressure6_10  = []

for row, attack in possessions.iterrows ():
    if attack.duration_sync >= 6:
        #calculation of timestamps for calculation of defensive pressure
        second_6 = attack.end_sync - 6
        
        identified_frames6 = position_data[position_data['T_sec'] == second_6]
        
        #Case 1: Team1 is in ball possession and plays from left to right
        if attack.team == team1 and attack.TeamLeft == team1:
            possible_attackers6 = identified_frames6[identified_frames6['TeamId'] == team1]
            possible_defenders6 = identified_frames6[identified_frames6['TeamId'] == team2]
            ball6 = identified_frames6[identified_frames6['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 2: Team1 is in ball possession and plays from right to left 
        elif attack.team == team1 and attack.TeamRight == team1:
            possible_attackers6 = identified_frames6[identified_frames6['TeamId'] == team1]
            possible_defenders6 = identified_frames6[identified_frames6['TeamId'] == team2]
            ball6 = identified_frames6[identified_frames6['TeamId'] == 'BALL'] 
            
            goal_x_to_play = 0
            goal_y_to_play = 34
        #Case 3: Team2 is in ball possession and plays from left to right 
        elif attack.team == team2 and attack.TeamLeft == team2:
            possible_attackers6 = identified_frames6[identified_frames6['TeamId'] == team2]
            possible_defenders6 = identified_frames6[identified_frames6['TeamId'] == team1]
            ball6 = identified_frames6[identified_frames6['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 4: Team2 is in ball possession and plays from right to left 
        elif attack.team == team2 and attack.TeamRight == team2:
            possible_attackers6 = identified_frames6[identified_frames6['TeamId'] == team2]
            possible_defenders6 = identified_frames6[identified_frames6['TeamId'] == team1]
            ball6 = identified_frames6[identified_frames6['TeamId'] == 'BALL']
            
            goal_x_to_play = 0
            goal_y_to_play = 34
            
        if len(possible_attackers6) == 11 and len(possible_defenders6) == 11: 
       
            #Identification of all attackers sorted after distance to ball
            Dis = []
            for index2, attacker in possible_attackers6.iterrows ():
                attack = pd.DataFrame (attacker)
                attack = attack.transpose ()
                dis = math.sqrt((attack['X'].item() - ball6['X'].item())**2 + (attack['Y'].item() - ball6['Y'].item())**2)
                Dis.append (dis)
        
            possible_attackers6['DistanceToBall'] = Dis
        
            group_attackers6 = possible_attackers6.sort_values (by=['DistanceToBall']).reset_index()
        
            group_attacker6_0 = group_attackers6.loc[[0]]
            group_attacker6_1 = group_attackers6.loc[[1]]
            group_attacker6_2 = group_attackers6.loc[[2]]
            group_attacker6_3 = group_attackers6.loc[[3]]
            group_attacker6_4 = group_attackers6.loc[[4]]
            group_attacker6_5 = group_attackers6.loc[[5]]
            group_attacker6_6 = group_attackers6.loc[[6]]
            group_attacker6_7 = group_attackers6.loc[[7]]
            group_attacker6_8 = group_attackers6.loc[[8]]
            group_attacker6_9 = group_attackers6.loc[[9]]
            group_attacker6_10 = group_attackers6.loc[[10]]
        
            #Calculation of pressure 
            Press_onball6 = []
            Press_ongroup6_1 = []
            Press_ongroup6_2 = []
            Press_ongroup6_3 = []
            Press_ongroup6_4 = []
            Press_ongroup6_5 = []
            Press_ongroup6_6 = []
            Press_ongroup6_7 = []
            Press_ongroup6_8 = []
            Press_ongroup6_9 = []
            Press_ongroup6_10 = []
        
            for index2, defender in possible_defenders6.iterrows ():
                defend = pd.DataFrame (defender)
                defend = defend.transpose ()
        
                press_onball = pressure_quantification (group_attacker6_0, defend, goal_x_to_play, goal_y_to_play)
                Press_onball6.append (press_onball)
                
                press_ongroup1 = pressure_quantification (group_attacker6_1, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup6_1.append (press_ongroup1)
                
                press_ongroup2 = pressure_quantification (group_attacker6_2, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup6_2.append (press_ongroup2)
                
                press_ongroup3 = pressure_quantification (group_attacker6_3, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup6_3.append (press_ongroup3)
                
                press_ongroup4 = pressure_quantification (group_attacker6_4, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup6_4.append (press_ongroup4)
                
                press_ongroup5 = pressure_quantification (group_attacker6_5, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup6_5.append (press_ongroup5)
                
                press_ongroup6 = pressure_quantification (group_attacker6_6, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup6_6.append (press_ongroup6)
            
                press_ongroup7 = pressure_quantification (group_attacker6_7, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup6_7.append (press_ongroup7)
                
                press_ongroup8 = pressure_quantification (group_attacker6_8, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup6_8.append (press_ongroup8)
                
                press_ongroup9 = pressure_quantification (group_attacker6_9, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup6_9.append (press_ongroup9)
                
                press_ongroup10 = pressure_quantification (group_attacker6_10, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup6_10.append (press_ongroup10)
                
            onballpressure6 = max (Press_onball6)
            ongrouppressure6_1 = max (Press_ongroup6_1)
            ongrouppressure6_2 = max (Press_ongroup6_2)
            ongrouppressure6_3 = max (Press_ongroup6_3)
            ongrouppressure6_4 = max (Press_ongroup6_4)
            ongrouppressure6_5 = max (Press_ongroup6_5)
            ongrouppressure6_6 = max (Press_ongroup6_6)
            ongrouppressure6_7 = max (Press_ongroup6_7)
            ongrouppressure6_8 = max (Press_ongroup6_8)
            ongrouppressure6_9 = max (Press_ongroup6_9)
            ongrouppressure6_10 = max (Press_ongroup6_10)
        else:
            onballpressure6 = None
            ongrouppressure6_1 = None
            ongrouppressure6_2 = None
            ongrouppressure6_3 = None
            ongrouppressure6_4 = None
            ongrouppressure6_5 = None
            ongrouppressure6_6 = None
            ongrouppressure6_7 = None
            ongrouppressure6_8 = None
            ongrouppressure6_9 = None
            ongrouppressure6_10 = None
    else: 
        onballpressure6 = None
        ongrouppressure6_1 = None
        ongrouppressure6_2 = None
        ongrouppressure6_3 = None
        ongrouppressure6_4 = None
        ongrouppressure6_5 = None
        ongrouppressure6_6 = None
        ongrouppressure6_7 = None
        ongrouppressure6_8 = None
        ongrouppressure6_9 = None
        ongrouppressure6_10 = None

    OnBallPressure6.append (onballpressure6)
    OnGroupPressure6_1.append (ongrouppressure6_1)
    OnGroupPressure6_2.append (ongrouppressure6_2)
    OnGroupPressure6_3.append (ongrouppressure6_3)
    OnGroupPressure6_4.append (ongrouppressure6_4)
    OnGroupPressure6_5.append (ongrouppressure6_5)
    OnGroupPressure6_6.append (ongrouppressure6_6)
    OnGroupPressure6_7.append (ongrouppressure6_7)
    OnGroupPressure6_8.append (ongrouppressure6_8)
    OnGroupPressure6_9.append (ongrouppressure6_9)
    OnGroupPressure6_10.append (ongrouppressure6_10)
    
#%%
#Measurement for timestamp: 7

OnBallPressure7 = []
OnGroupPressure7_1  = []
OnGroupPressure7_2  = []
OnGroupPressure7_3  = []
OnGroupPressure7_4  = []
OnGroupPressure7_5  = []
OnGroupPressure7_6  = []
OnGroupPressure7_7  = []
OnGroupPressure7_8  = []
OnGroupPressure7_9  = []
OnGroupPressure7_10  = []

for row, attack in possessions.iterrows ():
    if attack.duration_sync >= 7:
        #calculation of timestamps for calculation of defensive pressure
        second_7 = attack.end_sync - 7
        
        identified_frames7 = position_data[position_data['T_sec'] == second_7]
        
        #Case 1: Team1 is in ball possession and plays from left to right
        if attack.team == team1 and attack.TeamLeft == team1:
            possible_attackers7 = identified_frames7[identified_frames7['TeamId'] == team1]
            possible_defenders7 = identified_frames7[identified_frames7['TeamId'] == team2]
            ball7 = identified_frames7[identified_frames7['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 2: Team1 is in ball possession and plays from right to left 
        elif attack.team == team1 and attack.TeamRight == team1:
            possible_attackers7 = identified_frames7[identified_frames7['TeamId'] == team1]
            possible_defenders7 = identified_frames7[identified_frames7['TeamId'] == team2]
            ball7 = identified_frames7[identified_frames7['TeamId'] == 'BALL'] 
            
            goal_x_to_play = 0
            goal_y_to_play = 34
        #Case 3: Team2 is in ball possession and plays from left to right 
        elif attack.team == team2 and attack.TeamLeft == team2:
            possible_attackers7 = identified_frames7[identified_frames7['TeamId'] == team2]
            possible_defenders7 = identified_frames7[identified_frames7['TeamId'] == team1]
            ball7 = identified_frames7[identified_frames7['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 4: Team2 is in ball possession and plays from right to left 
        elif attack.team == team2 and attack.TeamRight == team2:
            possible_attackers7 = identified_frames7[identified_frames7['TeamId'] == team2]
            possible_defenders7 = identified_frames7[identified_frames7['TeamId'] == team1]
            ball7 = identified_frames7[identified_frames7['TeamId'] == 'BALL']
            
            goal_x_to_play = 0
            goal_y_to_play = 34
            
        if len(possible_attackers7) == 11 and len(possible_defenders7) == 11: 

            #Identification of all attackers sorted after distance to ball
            Dis = []
            for index2, attacker in possible_attackers7.iterrows():
                attack = pd.DataFrame(attacker)
                attack = attack.transpose()
                dis = math.sqrt((attack['X'].item(
                ) - ball7['X'].item())**2 + (attack['Y'].item() - ball7['Y'].item())**2)
                Dis.append(dis)

            possible_attackers7['DistanceToBall'] = Dis

            group_attackers7 = possible_attackers7.sort_values(
                by=['DistanceToBall']).reset_index()

            group_attacker7_0 = group_attackers7.loc[[0]]
            group_attacker7_1 = group_attackers7.loc[[1]]
            group_attacker7_2 = group_attackers7.loc[[2]]
            group_attacker7_3 = group_attackers7.loc[[3]]
            group_attacker7_4 = group_attackers7.loc[[4]]
            group_attacker7_5 = group_attackers7.loc[[5]]
            group_attacker7_6 = group_attackers7.loc[[6]]
            group_attacker7_7 = group_attackers7.loc[[7]]
            group_attacker7_8 = group_attackers7.loc[[8]]
            group_attacker7_9 = group_attackers7.loc[[9]]
            group_attacker7_10 = group_attackers7.loc[[10]]

            #Calculation of pressure
            Press_onball7 = []
            Press_ongroup7_1 = []
            Press_ongroup7_2 = []
            Press_ongroup7_3 = []
            Press_ongroup7_4 = []
            Press_ongroup7_5 = []
            Press_ongroup7_6 = []
            Press_ongroup7_7 = []
            Press_ongroup7_8 = []
            Press_ongroup7_9 = []
            Press_ongroup7_10 = []

            for index2, defender in possible_defenders7.iterrows():
                defend = pd.DataFrame(defender)
                defend = defend.transpose()

                press_onball = pressure_quantification(
                    group_attacker7_0, defend, goal_x_to_play, goal_y_to_play)
                Press_onball7.append(press_onball)

                press_ongroup1 = pressure_quantification(
                    group_attacker7_1, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup7_1.append(press_ongroup1)

                press_ongroup2 = pressure_quantification(
                    group_attacker7_2, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup7_2.append(press_ongroup2)

                press_ongroup3 = pressure_quantification(
                    group_attacker7_3, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup7_3.append(press_ongroup3)

                press_ongroup4 = pressure_quantification(
                    group_attacker7_4, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup7_4.append(press_ongroup4)

                press_ongroup5 = pressure_quantification(
                    group_attacker7_5, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup7_5.append(press_ongroup5)

                press_ongroup6 = pressure_quantification(
                    group_attacker7_6, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup7_6.append(press_ongroup6)

                press_ongroup7 = pressure_quantification(
                    group_attacker7_7, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup7_7.append(press_ongroup7)

                press_ongroup8 = pressure_quantification(
                    group_attacker7_8, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup7_8.append(press_ongroup8)

                press_ongroup9 = pressure_quantification(
                    group_attacker7_9, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup7_9.append(press_ongroup9)

                press_ongroup10 = pressure_quantification(
                    group_attacker7_10, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup7_10.append(press_ongroup10)

            onballpressure7 = max(Press_onball7)
            ongrouppressure7_1 = max(Press_ongroup7_1)
            ongrouppressure7_2 = max(Press_ongroup7_2)
            ongrouppressure7_3 = max(Press_ongroup7_3)
            ongrouppressure7_4 = max(Press_ongroup7_4)
            ongrouppressure7_5 = max(Press_ongroup7_5)
            ongrouppressure7_6 = max(Press_ongroup7_6)
            ongrouppressure7_7 = max(Press_ongroup7_7)
            ongrouppressure7_8 = max(Press_ongroup7_8)
            ongrouppressure7_9 = max(Press_ongroup7_9)
            ongrouppressure7_10 = max(Press_ongroup7_10)
        else:
            onballpressure7 = None
            ongrouppressure7_1 = None
            ongrouppressure7_2 = None
            ongrouppressure7_3 = None
            ongrouppressure7_4 = None
            ongrouppressure7_5 = None
            ongrouppressure7_6 = None
            ongrouppressure7_7 = None
            ongrouppressure7_8 = None
            ongrouppressure7_9 = None
            ongrouppressure7_10 = None

    else:
        onballpressure7 = None
        ongrouppressure7_1 = None
        ongrouppressure7_2 = None
        ongrouppressure7_3 = None
        ongrouppressure7_4 = None
        ongrouppressure7_5 = None
        ongrouppressure7_6 = None
        ongrouppressure7_7 = None
        ongrouppressure7_8 = None
        ongrouppressure7_9 = None
        ongrouppressure7_10 = None

    OnBallPressure7.append (onballpressure7)
    OnGroupPressure7_1.append (ongrouppressure7_1)
    OnGroupPressure7_2.append (ongrouppressure7_2)
    OnGroupPressure7_3.append (ongrouppressure7_3)
    OnGroupPressure7_4.append (ongrouppressure7_4)
    OnGroupPressure7_5.append (ongrouppressure7_5)
    OnGroupPressure7_6.append (ongrouppressure7_6)
    OnGroupPressure7_7.append (ongrouppressure7_7)
    OnGroupPressure7_8.append (ongrouppressure7_8)
    OnGroupPressure7_9.append (ongrouppressure7_9)
    OnGroupPressure7_10.append (ongrouppressure7_10)
        
#%%
#Measurement for timestamp: 8

OnBallPressure8 = []
OnGroupPressure8_1  = []
OnGroupPressure8_2  = []
OnGroupPressure8_3  = []
OnGroupPressure8_4  = []
OnGroupPressure8_5  = []
OnGroupPressure8_6  = []
OnGroupPressure8_7  = []
OnGroupPressure8_8  = []
OnGroupPressure8_9  = []
OnGroupPressure8_10  = []

for row, attack in possessions.iterrows ():
    if attack.duration_sync >= 8:
        #calculation of timestamps for calculation of defensive pressure
        second_8 = attack.end_sync - 8
        
        identified_frames8 = position_data[position_data['T_sec'] == second_8]
        
        #Case 1: Team1 is in ball possession and plays from left to right
        if attack.team == team1 and attack.TeamLeft == team1:
            possible_attackers8 = identified_frames8[identified_frames8['TeamId'] == team1]
            possible_defenders8 = identified_frames8[identified_frames8['TeamId'] == team2]
            ball8 = identified_frames8[identified_frames8['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 2: Team1 is in ball possession and plays from right to left 
        elif attack.team == team1 and attack.TeamRight == team1:
            possible_attackers8 = identified_frames8[identified_frames8['TeamId'] == team1]
            possible_defenders8 = identified_frames8[identified_frames8['TeamId'] == team2]
            ball8 = identified_frames8[identified_frames8['TeamId'] == 'BALL'] 
            
            goal_x_to_play = 0
            goal_y_to_play = 34
        #Case 3: Team2 is in ball possession and plays from left to right 
        elif attack.team == team2 and attack.TeamLeft == team2:
            possible_attackers8 = identified_frames8[identified_frames8['TeamId'] == team2]
            possible_defenders8 = identified_frames8[identified_frames8['TeamId'] == team1]
            ball8 = identified_frames8[identified_frames8['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 4: Team2 is in ball possession and plays from right to left 
        elif attack.team == team2 and attack.TeamRight == team2:
            possible_attackers8 = identified_frames8[identified_frames8['TeamId'] == team2]
            possible_defenders8 = identified_frames8[identified_frames8['TeamId'] == team1]
            ball8 = identified_frames8[identified_frames8['TeamId'] == 'BALL']
            
            goal_x_to_play = 0
            goal_y_to_play = 34
            
        if len(possible_attackers8) == 11 and len(possible_defenders8) == 11: 
       
            #Identification of all attackers sorted after distance to ball
            Dis = []
            for index2, attacker in possible_attackers8.iterrows ():
                attack = pd.DataFrame (attacker)
                attack = attack.transpose ()
                dis = math.sqrt((attack['X'].item() - ball8['X'].item())**2 + (attack['Y'].item() - ball8['Y'].item())**2)
                Dis.append (dis)
        
            possible_attackers8['DistanceToBall'] = Dis
        
            group_attackers8 = possible_attackers8.sort_values (by=['DistanceToBall']).reset_index()
        
            group_attacker8_0 = group_attackers8.loc[[0]]
            group_attacker8_1 = group_attackers8.loc[[1]]
            group_attacker8_2 = group_attackers8.loc[[2]]
            group_attacker8_3 = group_attackers8.loc[[3]]
            group_attacker8_4 = group_attackers8.loc[[4]]
            group_attacker8_5 = group_attackers8.loc[[5]]
            group_attacker8_6 = group_attackers8.loc[[6]]
            group_attacker8_7 = group_attackers8.loc[[7]]
            group_attacker8_8 = group_attackers8.loc[[8]]
            group_attacker8_9 = group_attackers8.loc[[9]]
            group_attacker8_10 = group_attackers8.loc[[10]]
        
            #Calculation of pressure 
            Press_onball8 = []
            Press_ongroup8_1 = []
            Press_ongroup8_2 = []
            Press_ongroup8_3 = []
            Press_ongroup8_4 = []
            Press_ongroup8_5 = []
            Press_ongroup8_6 = []
            Press_ongroup8_7 = []
            Press_ongroup8_8 = []
            Press_ongroup8_9 = []
            Press_ongroup8_10 = []
    
            for index2, defender in possible_defenders8.iterrows ():
                defend = pd.DataFrame (defender)
                defend = defend.transpose ()
        
                press_onball = pressure_quantification (group_attacker8_0, defend, goal_x_to_play, goal_y_to_play)
                Press_onball8.append (press_onball)
                
                press_ongroup1 = pressure_quantification (group_attacker8_1, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup8_1.append (press_ongroup1)
                
                press_ongroup2 = pressure_quantification (group_attacker8_2, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup8_2.append (press_ongroup2)
                
                press_ongroup3 = pressure_quantification (group_attacker8_3, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup8_3.append (press_ongroup3)
                
                press_ongroup4 = pressure_quantification (group_attacker8_4, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup8_4.append (press_ongroup4)
                
                press_ongroup5 = pressure_quantification (group_attacker8_5, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup8_5.append (press_ongroup5)
            
                press_ongroup6 = pressure_quantification (group_attacker8_6, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup8_6.append (press_ongroup6)
            
                press_ongroup7 = pressure_quantification (group_attacker8_7, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup8_7.append (press_ongroup7)
                
                press_ongroup8 = pressure_quantification (group_attacker8_8, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup8_8.append (press_ongroup8)
                
                press_ongroup9 = pressure_quantification (group_attacker8_9, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup8_9.append (press_ongroup9)
                
                press_ongroup10 = pressure_quantification (group_attacker8_10, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup8_10.append (press_ongroup10)
                
            onballpressure8 = max (Press_onball8)
            ongrouppressure8_1 = max (Press_ongroup8_1)
            ongrouppressure8_2 = max (Press_ongroup8_2)
            ongrouppressure8_3 = max (Press_ongroup8_3)
            ongrouppressure8_4 = max (Press_ongroup8_4)
            ongrouppressure8_5 = max (Press_ongroup8_5)
            ongrouppressure8_6 = max (Press_ongroup8_6)
            ongrouppressure8_7 = max (Press_ongroup8_7)
            ongrouppressure8_8 = max (Press_ongroup8_8)
            ongrouppressure8_9 = max (Press_ongroup8_9)
            ongrouppressure8_10 = max (Press_ongroup8_10)
        else:
            onballpressure8 = None
            ongrouppressure8_1 = None
            ongrouppressure8_2 = None
            ongrouppressure8_3 = None
            ongrouppressure8_4 = None
            ongrouppressure8_5 = None
            ongrouppressure8_6 = None
            ongrouppressure8_7 = None
            ongrouppressure8_8 = None
            ongrouppressure8_9 = None
            ongrouppressure8_10 = None
    else: 
        onballpressure8 = None
        ongrouppressure8_1 = None
        ongrouppressure8_2 = None
        ongrouppressure8_3 = None
        ongrouppressure8_4 = None
        ongrouppressure8_5 = None
        ongrouppressure8_6 = None
        ongrouppressure8_7 = None
        ongrouppressure8_8 = None
        ongrouppressure8_9 = None
        ongrouppressure8_10 = None

    OnBallPressure8.append (onballpressure8)
    OnGroupPressure8_1.append (ongrouppressure8_1)
    OnGroupPressure8_2.append (ongrouppressure8_2)
    OnGroupPressure8_3.append (ongrouppressure8_3)
    OnGroupPressure8_4.append (ongrouppressure8_4)
    OnGroupPressure8_5.append (ongrouppressure8_5)
    OnGroupPressure8_6.append (ongrouppressure8_6)
    OnGroupPressure8_7.append (ongrouppressure8_7)
    OnGroupPressure8_8.append (ongrouppressure8_8)
    OnGroupPressure8_9.append (ongrouppressure8_9)
    OnGroupPressure8_10.append (ongrouppressure8_10)
    
#%%
#Measurement for timestamp: 9

OnBallPressure9 = []
OnGroupPressure9_1  = []
OnGroupPressure9_2  = []
OnGroupPressure9_3  = []
OnGroupPressure9_4  = []
OnGroupPressure9_5  = []
OnGroupPressure9_6  = []
OnGroupPressure9_7  = []
OnGroupPressure9_8  = []
OnGroupPressure9_9  = []
OnGroupPressure9_10  = []

for row, attack in possessions.iterrows ():
    if attack.duration_sync >= 9:
        #calculation of timestamps for calculation of defensive pressure
        second_9 = attack.end_sync - 9
        
        identified_frames9 = position_data[position_data['T_sec'] == second_9]
        
        #Case 1: Team1 is in ball possession and plays from left to right
        if attack.team == team1 and attack.TeamLeft == team1:
            possible_attackers9 = identified_frames9[identified_frames9['TeamId'] == team1]
            possible_defenders9 = identified_frames9[identified_frames9['TeamId'] == team2]
            ball9 = identified_frames9[identified_frames9['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 2: Team1 is in ball possession and plays from right to left 
        elif attack.team == team1 and attack.TeamRight == team1:
            possible_attackers9 = identified_frames9[identified_frames9['TeamId'] == team1]
            possible_defenders9 = identified_frames9[identified_frames9['TeamId'] == team2]
            ball9 = identified_frames9[identified_frames9['TeamId'] == 'BALL'] 
            
            goal_x_to_play = 0
            goal_y_to_play = 34
        #Case 3: Team2 is in ball possession and plays from left to right 
        elif attack.team == team2 and attack.TeamLeft == team2:
            possible_attackers9 = identified_frames9[identified_frames9['TeamId'] == team2]
            possible_defenders9 = identified_frames9[identified_frames9['TeamId'] == team1]
            ball9 = identified_frames9[identified_frames9['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 4: Team2 is in ball possession and plays from right to left 
        elif attack.team == team2 and attack.TeamRight == team2:
            possible_attackers9 = identified_frames9[identified_frames9['TeamId'] == team2]
            possible_defenders9 = identified_frames9[identified_frames9['TeamId'] == team1]
            ball9 = identified_frames9[identified_frames9['TeamId'] == 'BALL']
            
            goal_x_to_play = 0
            goal_y_to_play = 34
            
        if len(possible_attackers9) == 11 and len(possible_defenders9) == 11: 
       
            #Identification of all attackers sorted after distance to ball
            Dis = []
            for index2, attacker in possible_attackers9.iterrows ():
                attack = pd.DataFrame (attacker)
                attack = attack.transpose ()
                dis = math.sqrt((attack['X'].item() - ball9['X'].item())**2 + (attack['Y'].item() - ball9['Y'].item())**2)
                Dis.append (dis)
        
            possible_attackers9['DistanceToBall'] = Dis
        
            group_attackers9 = possible_attackers9.sort_values (by=['DistanceToBall']).reset_index()
        
            group_attacker9_0 = group_attackers9.loc[[0]]
            group_attacker9_1 = group_attackers9.loc[[1]]
            group_attacker9_2 = group_attackers9.loc[[2]]
            group_attacker9_3 = group_attackers9.loc[[3]]
            group_attacker9_4 = group_attackers9.loc[[4]]
            group_attacker9_5 = group_attackers9.loc[[5]]
            group_attacker9_6 = group_attackers9.loc[[6]]
            group_attacker9_7 = group_attackers9.loc[[7]]
            group_attacker9_8 = group_attackers9.loc[[8]]
            group_attacker9_9 = group_attackers9.loc[[9]]
            group_attacker9_10 = group_attackers9.loc[[10]]
        
            #Calculation of pressure 
            Press_onball9 = []
            Press_ongroup9_1 = []
            Press_ongroup9_2 = []
            Press_ongroup9_3 = []
            Press_ongroup9_4 = []
            Press_ongroup9_5 = []
            Press_ongroup9_6 = []
            Press_ongroup9_7 = []
            Press_ongroup9_8 = []
            Press_ongroup9_9 = []
            Press_ongroup9_10 = []
    
            for index2, defender in possible_defenders9.iterrows ():
                defend = pd.DataFrame (defender)
                defend = defend.transpose ()
        
                press_onball = pressure_quantification (group_attacker9_0, defend, goal_x_to_play, goal_y_to_play)
                Press_onball9.append (press_onball)
                
                press_ongroup1 = pressure_quantification (group_attacker9_1, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup9_1.append (press_ongroup1)
                
                press_ongroup2 = pressure_quantification (group_attacker9_2, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup9_2.append (press_ongroup2)
                
                press_ongroup3 = pressure_quantification (group_attacker9_3, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup9_3.append (press_ongroup3)
                
                press_ongroup4 = pressure_quantification (group_attacker9_4, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup9_4.append (press_ongroup4)
                
                press_ongroup5 = pressure_quantification (group_attacker9_5, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup9_5.append (press_ongroup5)
            
                press_ongroup6 = pressure_quantification (group_attacker9_6, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup9_6.append (press_ongroup6)
            
                press_ongroup7 = pressure_quantification (group_attacker9_7, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup9_7.append (press_ongroup7)
                
                press_ongroup8 = pressure_quantification (group_attacker9_8, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup9_8.append (press_ongroup8)
                
                press_ongroup9 = pressure_quantification (group_attacker9_9, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup9_9.append (press_ongroup9)
                
                press_ongroup10 = pressure_quantification (group_attacker9_10, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup9_10.append (press_ongroup10)
                
            onballpressure9 = max (Press_onball9)
            ongrouppressure9_1 = max (Press_ongroup9_1)
            ongrouppressure9_2 = max (Press_ongroup9_2)
            ongrouppressure9_3 = max (Press_ongroup9_3)
            ongrouppressure9_4 = max (Press_ongroup9_4)
            ongrouppressure9_5 = max (Press_ongroup9_5)
            ongrouppressure9_6 = max (Press_ongroup9_6)
            ongrouppressure9_7 = max (Press_ongroup9_7)
            ongrouppressure9_8 = max (Press_ongroup9_8)
            ongrouppressure9_9 = max (Press_ongroup9_9)
            ongrouppressure9_10 = max (Press_ongroup9_10)
        else:
            onballpressure9 = None
            ongrouppressure9_1 = None
            ongrouppressure9_2 = None
            ongrouppressure9_3 = None
            ongrouppressure9_4 = None
            ongrouppressure9_5 = None
            ongrouppressure9_6 = None
            ongrouppressure9_7 = None
            ongrouppressure9_8 = None
            ongrouppressure9_9 = None
            ongrouppressure9_10 = None
    else: 
        onballpressure9 = None
        ongrouppressure9_1 = None
        ongrouppressure9_2 = None
        ongrouppressure9_3 = None
        ongrouppressure9_4 = None
        ongrouppressure9_5 = None
        ongrouppressure9_6 = None
        ongrouppressure9_7 = None
        ongrouppressure9_8 = None
        ongrouppressure9_9 = None
        ongrouppressure9_10 = None

    OnBallPressure9.append (onballpressure9)
    OnGroupPressure9_1.append (ongrouppressure9_1)
    OnGroupPressure9_2.append (ongrouppressure9_2)
    OnGroupPressure9_3.append (ongrouppressure9_3)
    OnGroupPressure9_4.append (ongrouppressure9_4)
    OnGroupPressure9_5.append (ongrouppressure9_5)
    OnGroupPressure9_6.append (ongrouppressure9_6)
    OnGroupPressure9_7.append (ongrouppressure9_7)
    OnGroupPressure9_8.append (ongrouppressure9_8)
    OnGroupPressure9_9.append (ongrouppressure9_9)
    OnGroupPressure9_10.append (ongrouppressure9_10)
    
#%%
#Measurement for timestamp: 10

OnBallPressure10 = []
OnGroupPressure10_1  = []
OnGroupPressure10_2  = []
OnGroupPressure10_3  = []
OnGroupPressure10_4  = []
OnGroupPressure10_5  = []
OnGroupPressure10_6  = []
OnGroupPressure10_7  = []
OnGroupPressure10_8  = []
OnGroupPressure10_9  = []
OnGroupPressure10_10  = []

for row, attack in possessions.iterrows ():
    if attack.duration_sync >= 10:
        #calculation of timestamps for calculation of defensive pressure
        second_10 = attack.end_sync - 10
        
        identified_frames10 = position_data[position_data['T_sec'] == second_10]
        
        #Case 1: Team1 is in ball possession and plays from left to right
        if attack.team == team1 and attack.TeamLeft == team1:
            possible_attackers10 = identified_frames10[identified_frames10['TeamId'] == team1]
            possible_defenders10 = identified_frames10[identified_frames10['TeamId'] == team2]
            ball10 = identified_frames10[identified_frames10['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 2: Team1 is in ball possession and plays from right to left 
        elif attack.team == team1 and attack.TeamRight == team1:
            possible_attackers10 = identified_frames10[identified_frames10['TeamId'] == team1]
            possible_defenders10 = identified_frames10[identified_frames10['TeamId'] == team2]
            ball10 = identified_frames10[identified_frames10['TeamId'] == 'BALL'] 
            
            goal_x_to_play = 0
            goal_y_to_play = 34
        #Case 3: Team2 is in ball possession and plays from left to right 
        elif attack.team == team2 and attack.TeamLeft == team2:
            possible_attackers10 = identified_frames10[identified_frames10['TeamId'] == team2]
            possible_defenders10 = identified_frames10[identified_frames10['TeamId'] == team1]
            ball10 = identified_frames10[identified_frames10['TeamId'] == 'BALL']
            
            goal_x_to_play = 105
            goal_y_to_play = 34
        #Case 4: Team2 is in ball possession and plays from right to left 
        elif attack.team == team2 and attack.TeamRight == team2:
            possible_attackers10 = identified_frames10[identified_frames10['TeamId'] == team2]
            possible_defenders10 = identified_frames10[identified_frames10['TeamId'] == team1]
            ball10 = identified_frames10[identified_frames10['TeamId'] == 'BALL']
            
            goal_x_to_play = 0
            goal_y_to_play = 34
            
        if len(possible_attackers10) == 11 and len(possible_defenders10) == 11: 
       
            #Identification of all attackers sorted after distance to ball
            Dis = []
            for index2, attacker in possible_attackers10.iterrows ():
                attack = pd.DataFrame (attacker)
                attack = attack.transpose ()
                dis = math.sqrt((attack['X'].item() - ball10['X'].item())**2 + (attack['Y'].item() - ball10['Y'].item())**2)
                Dis.append (dis)
        
            possible_attackers10['DistanceToBall'] = Dis
        
            group_attackers10 = possible_attackers10.sort_values (by=['DistanceToBall']).reset_index()
    
            group_attacker10_0 = group_attackers10.loc[[0]]
            group_attacker10_1 = group_attackers10.loc[[1]]
            group_attacker10_2 = group_attackers10.loc[[2]]
            group_attacker10_3 = group_attackers10.loc[[3]]
            group_attacker10_4 = group_attackers10.loc[[4]]
            group_attacker10_5 = group_attackers10.loc[[5]]
            group_attacker10_6 = group_attackers10.loc[[6]]
            group_attacker10_7 = group_attackers10.loc[[7]]
            group_attacker10_8 = group_attackers10.loc[[8]]
            group_attacker10_9 = group_attackers10.loc[[9]]
            group_attacker10_10 = group_attackers10.loc[[10]]
        
            #Calculation of pressure 
            Press_onball10 = []
            Press_ongroup10_1 = []
            Press_ongroup10_2 = []
            Press_ongroup10_3 = []
            Press_ongroup10_4 = []
            Press_ongroup10_5 = []
            Press_ongroup10_6 = []
            Press_ongroup10_7 = []
            Press_ongroup10_8 = []
            Press_ongroup10_9 = []
            Press_ongroup10_10 = []
    
            for index2, defender in possible_defenders10.iterrows ():
                defend = pd.DataFrame (defender)
                defend = defend.transpose ()
        
                press_onball = pressure_quantification (group_attacker10_0, defend, goal_x_to_play, goal_y_to_play)
                Press_onball10.append (press_onball)
                
                press_ongroup1 = pressure_quantification (group_attacker10_1, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup10_1.append (press_ongroup1)
                
                press_ongroup2 = pressure_quantification (group_attacker10_2, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup10_2.append (press_ongroup2)
                
                press_ongroup3 = pressure_quantification (group_attacker10_3, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup10_3.append (press_ongroup3)
                
                press_ongroup4 = pressure_quantification (group_attacker10_4, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup10_4.append (press_ongroup4)
                
                press_ongroup5 = pressure_quantification (group_attacker10_5, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup10_5.append (press_ongroup5)
            
                press_ongroup6 = pressure_quantification (group_attacker10_6, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup10_6.append (press_ongroup6)
            
                press_ongroup7 = pressure_quantification (group_attacker10_7, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup10_7.append (press_ongroup7)
                
                press_ongroup8 = pressure_quantification (group_attacker10_8, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup10_8.append (press_ongroup8)
                
                press_ongroup9 = pressure_quantification (group_attacker10_9, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup10_9.append (press_ongroup9)
                
                press_ongroup10 = pressure_quantification (group_attacker10_10, defend, goal_x_to_play, goal_y_to_play)
                Press_ongroup10_10.append (press_ongroup10)
                
            onballpressure10 = max (Press_onball10)
            ongrouppressure10_1 = max (Press_ongroup10_1)
            ongrouppressure10_2 = max (Press_ongroup10_2)
            ongrouppressure10_3 = max (Press_ongroup10_3)
            ongrouppressure10_4 = max (Press_ongroup10_4)
            ongrouppressure10_5 = max (Press_ongroup10_5)
            ongrouppressure10_6 = max (Press_ongroup10_6)
            ongrouppressure10_7 = max (Press_ongroup10_7)
            ongrouppressure10_8 = max (Press_ongroup10_8)
            ongrouppressure10_9 = max (Press_ongroup10_9)
            ongrouppressure10_10 = max (Press_ongroup10_10)
        else:
            onballpressure10 = None
            ongrouppressure10_1 = None
            ongrouppressure10_2 = None
            ongrouppressure10_3 = None
            ongrouppressure10_4 = None
            ongrouppressure10_5 = None
            ongrouppressure10_6 = None
            ongrouppressure10_7 = None
            ongrouppressure10_8 = None
            ongrouppressure10_9 = None
            ongrouppressure10_10 = None
    else: 
        onballpressure10 = None
        ongrouppressure10_1 = None
        ongrouppressure10_2 = None
        ongrouppressure10_3 = None
        ongrouppressure10_4 = None
        ongrouppressure10_5 = None
        ongrouppressure10_6 = None
        ongrouppressure10_7 = None
        ongrouppressure10_8 = None
        ongrouppressure10_9 = None
        ongrouppressure10_10 = None

    OnBallPressure10.append (onballpressure10)
    OnGroupPressure10_1.append (ongrouppressure10_1)
    OnGroupPressure10_2.append (ongrouppressure10_2)
    OnGroupPressure10_3.append (ongrouppressure10_3)
    OnGroupPressure10_4.append (ongrouppressure10_4)
    OnGroupPressure10_5.append (ongrouppressure10_5)
    OnGroupPressure10_6.append (ongrouppressure10_6)
    OnGroupPressure10_7.append (ongrouppressure10_7)
    OnGroupPressure10_8.append (ongrouppressure10_8)
    OnGroupPressure10_9.append (ongrouppressure10_9)
    OnGroupPressure10_10.append (ongrouppressure10_10)
#%%
possessions['OnBallPressure0'] = OnBallPressure0
possessions['OnGroupPressure0_1'] = OnGroupPressure0_1
possessions['OnGroupPressure0_2'] = OnGroupPressure0_2
possessions['OnGroupPressure0_3'] = OnGroupPressure0_3
possessions['OnGroupPressure0_4'] = OnGroupPressure0_4
possessions['OnGroupPressure0_5'] = OnGroupPressure0_5
possessions['OnGroupPressure0_6'] = OnGroupPressure0_6
possessions['OnGroupPressure0_7'] = OnGroupPressure0_7
possessions['OnGroupPressure0_8'] = OnGroupPressure0_8
possessions['OnGroupPressure0_9'] = OnGroupPressure0_9
possessions['OnGroupPressure0_10'] = OnGroupPressure0_10

possessions['OnBallPressure1'] = OnBallPressure1
possessions['OnGroupPressure1_1'] = OnGroupPressure1_1
possessions['OnGroupPressure1_2'] = OnGroupPressure1_2
possessions['OnGroupPressure1_3'] = OnGroupPressure1_3
possessions['OnGroupPressure1_4'] = OnGroupPressure1_4
possessions['OnGroupPressure1_5'] = OnGroupPressure1_5
possessions['OnGroupPressure1_6'] = OnGroupPressure1_6
possessions['OnGroupPressure1_7'] = OnGroupPressure1_7
possessions['OnGroupPressure1_8'] = OnGroupPressure1_8
possessions['OnGroupPressure1_9'] = OnGroupPressure1_9
possessions['OnGroupPressure1_10'] = OnGroupPressure1_10

possessions['OnBallPressure2'] = OnBallPressure2
possessions['OnGroupPressure2_1'] = OnGroupPressure2_1
possessions['OnGroupPressure2_2'] = OnGroupPressure2_2
possessions['OnGroupPressure2_3'] = OnGroupPressure2_3
possessions['OnGroupPressure2_4'] = OnGroupPressure2_4
possessions['OnGroupPressure2_5'] = OnGroupPressure2_5
possessions['OnGroupPressure2_6'] = OnGroupPressure2_6
possessions['OnGroupPressure2_7'] = OnGroupPressure2_7
possessions['OnGroupPressure2_8'] = OnGroupPressure2_8
possessions['OnGroupPressure2_9'] = OnGroupPressure2_9
possessions['OnGroupPressure2_10'] = OnGroupPressure2_10

possessions['OnBallPressure3'] = OnBallPressure3
possessions['OnGroupPressure3_1'] = OnGroupPressure3_1
possessions['OnGroupPressure3_2'] = OnGroupPressure3_2
possessions['OnGroupPressure3_3'] = OnGroupPressure3_3
possessions['OnGroupPressure3_4'] = OnGroupPressure3_4
possessions['OnGroupPressure3_5'] = OnGroupPressure3_5
possessions['OnGroupPressure3_6'] = OnGroupPressure3_6
possessions['OnGroupPressure3_7'] = OnGroupPressure3_7
possessions['OnGroupPressure3_8'] = OnGroupPressure3_8
possessions['OnGroupPressure3_9'] = OnGroupPressure3_9
possessions['OnGroupPressure3_10'] = OnGroupPressure3_10

possessions['OnBallPressure4'] = OnBallPressure4
possessions['OnGroupPressure4_1'] = OnGroupPressure4_1
possessions['OnGroupPressure4_2'] = OnGroupPressure4_2
possessions['OnGroupPressure4_3'] = OnGroupPressure4_3
possessions['OnGroupPressure4_4'] = OnGroupPressure4_4
possessions['OnGroupPressure4_5'] = OnGroupPressure4_5
possessions['OnGroupPressure4_6'] = OnGroupPressure4_6
possessions['OnGroupPressure4_7'] = OnGroupPressure4_7
possessions['OnGroupPressure4_8'] = OnGroupPressure4_8
possessions['OnGroupPressure4_9'] = OnGroupPressure4_9
possessions['OnGroupPressure4_10'] = OnGroupPressure4_10

possessions['OnBallPressure5'] = OnBallPressure5
possessions['OnGroupPressure5_1'] = OnGroupPressure5_1
possessions['OnGroupPressure5_2'] = OnGroupPressure5_2
possessions['OnGroupPressure5_3'] = OnGroupPressure5_3
possessions['OnGroupPressure5_4'] = OnGroupPressure5_4
possessions['OnGroupPressure5_5'] = OnGroupPressure5_5
possessions['OnGroupPressure5_6'] = OnGroupPressure5_6
possessions['OnGroupPressure5_7'] = OnGroupPressure5_7
possessions['OnGroupPressure5_8'] = OnGroupPressure5_8
possessions['OnGroupPressure5_9'] = OnGroupPressure5_9
possessions['OnGroupPressure5_10'] = OnGroupPressure5_10

possessions['OnBallPressure6'] = OnBallPressure6
possessions['OnGroupPressure6_1'] = OnGroupPressure6_1
possessions['OnGroupPressure6_2'] = OnGroupPressure6_2
possessions['OnGroupPressure6_3'] = OnGroupPressure6_3
possessions['OnGroupPressure6_4'] = OnGroupPressure6_4
possessions['OnGroupPressure6_5'] = OnGroupPressure6_5
possessions['OnGroupPressure6_6'] = OnGroupPressure6_6
possessions['OnGroupPressure6_7'] = OnGroupPressure6_7
possessions['OnGroupPressure6_8'] = OnGroupPressure6_8
possessions['OnGroupPressure6_9'] = OnGroupPressure6_9
possessions['OnGroupPressure6_10'] = OnGroupPressure6_10

possessions['OnBallPressure7'] = OnBallPressure7
possessions['OnGroupPressure7_1'] = OnGroupPressure7_1
possessions['OnGroupPressure7_2'] = OnGroupPressure7_2
possessions['OnGroupPressure7_3'] = OnGroupPressure7_3
possessions['OnGroupPressure7_4'] = OnGroupPressure7_4
possessions['OnGroupPressure7_5'] = OnGroupPressure7_5
possessions['OnGroupPressure7_6'] = OnGroupPressure7_6
possessions['OnGroupPressure7_7'] = OnGroupPressure7_7
possessions['OnGroupPressure7_8'] = OnGroupPressure7_8
possessions['OnGroupPressure7_9'] = OnGroupPressure7_9
possessions['OnGroupPressure7_10'] = OnGroupPressure7_10

possessions['OnBallPressure8'] = OnBallPressure8
possessions['OnGroupPressure8_1'] = OnGroupPressure8_1
possessions['OnGroupPressure8_2'] = OnGroupPressure8_2
possessions['OnGroupPressure8_3'] = OnGroupPressure8_3
possessions['OnGroupPressure8_4'] = OnGroupPressure8_4
possessions['OnGroupPressure8_5'] = OnGroupPressure8_5
possessions['OnGroupPressure8_6'] = OnGroupPressure8_6
possessions['OnGroupPressure8_7'] = OnGroupPressure8_7
possessions['OnGroupPressure8_8'] = OnGroupPressure8_8
possessions['OnGroupPressure8_9'] = OnGroupPressure8_9
possessions['OnGroupPressure8_10'] = OnGroupPressure8_10

possessions['OnBallPressure9'] = OnBallPressure9
possessions['OnGroupPressure9_1'] = OnGroupPressure9_1
possessions['OnGroupPressure9_2'] = OnGroupPressure9_2
possessions['OnGroupPressure9_3'] = OnGroupPressure9_3
possessions['OnGroupPressure9_4'] = OnGroupPressure9_4
possessions['OnGroupPressure9_5'] = OnGroupPressure9_5
possessions['OnGroupPressure9_6'] = OnGroupPressure9_6
possessions['OnGroupPressure9_7'] = OnGroupPressure9_7
possessions['OnGroupPressure9_8'] = OnGroupPressure9_8
possessions['OnGroupPressure9_9'] = OnGroupPressure9_9
possessions['OnGroupPressure9_10'] = OnGroupPressure9_10

possessions['OnBallPressure10'] = OnBallPressure10
possessions['OnGroupPressure10_1'] = OnGroupPressure10_1
possessions['OnGroupPressure10_2'] = OnGroupPressure10_2
possessions['OnGroupPressure10_3'] = OnGroupPressure10_3
possessions['OnGroupPressure10_4'] = OnGroupPressure10_4
possessions['OnGroupPressure10_5'] = OnGroupPressure10_5
possessions['OnGroupPressure10_6'] = OnGroupPressure10_6
possessions['OnGroupPressure10_7'] = OnGroupPressure10_7
possessions['OnGroupPressure10_8'] = OnGroupPressure10_8
possessions['OnGroupPressure10_9'] = OnGroupPressure10_9
possessions['OnGroupPressure10_10'] = OnGroupPressure10_10

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

possessions.to_csv (r'result_possessions_timepoints_Game18.csv')
