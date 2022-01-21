import pandas as pd
import numpy as np
from datetime import datetime
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


#%%Load event and position data

event_data =  pd.read_csv ('C:/Users/sysadmin/Desktop/Dissertation/DFL Daten/DFL Daten/EventData_1.Buli_Season19-20_Game14.csv')
position_data = pd.read_csv ('C:/Users/sysadmin/Desktop/Dissertation/DFL Daten/DFL Daten/PositionData_1.Buli_Season19-20_Game14.csv')

possessions = pd.read_csv ('C:/Users/sysadmin/Desktop/Dissertation/Paper2_defensive pressure/results11-20(new)/result_possessions_timepoints_Game14.csv')

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


#%%
#Figure of playing situation with pressure values
#Figure of playing pitch with both teams & the ball & pressure values(only uses Frame of sitaution)


#event_data = load event data
#position_data = load position data
#possessions = load result of posessions with pressure values


team_list = list (event_data.Team.unique ())
team_list = [x for x in team_list if str(x) != 'nan']
team1 = team_list[0]
team2 = team_list[1]

#Frame
Frame = 73885.64
Action= 'Fourthlast'

attacking_team = possessions[possessions[f'Frame{Action}Action'] == Frame].team.item()


if attacking_team == team1:
    defending_team = team2
else:
    defending_team = team1
#Figure details
fig, ax = plt.subplots(dpi=500)
plt.title(f"{Frame}")
plt.xlim (-5,110)
plt.ylim (-5,73)

#lines of pitch
plt.plot ([0,16,16,0], [54,54,14,14], c='grey', linewidth=0.7)
plt.plot ([105,89,89,105], [54,54,14,14], c='grey', linewidth=0.7)
plt.plot ([0,5.5,5.5,0],[43,43,25,25], c= 'grey', linewidth=0.7)
plt.plot ([105,99.5,99.5,105],[43,43,25,25], c= 'grey', linewidth=0.7)
plt.plot ([0,0,105,105,0], [0,68,68,0,0], c= 'grey', linewidth=0.7)
plt.plot ([52.5,52.5], [68,0], c= 'grey', linewidth=0.7)
plt.scatter ([11,52.5, 94],[34,34,34],c= 'grey',s= 4)
circle = Circle((52.5,34), 11, Fill=False, color='grey', linewidth=0.7)
ax.add_artist (circle)

#Circles of pitch
Y1 = list (np.linspace (0,9, num=25))
Y2 = list (np.linspace (9,0, num=25))
Y = Y2 + Y1
X = []
X2 = []
for value in Y:
    x = (math.sqrt (value**2 + 9**2) - 9 )*(-1)
    X.append (x)
X = [i - (min (X)) + 16 for i in X]
for value in Y:
    x2 = math.sqrt (value**2 + 9**2) - 9 
    X2.append (x2)
X2 = [i - (max (X2)) + 89 for i in X2]

y = list (np.linspace (26, 42, num=50))
plt.plot (X,y, c= 'grey', linewidth=0.7)
plt.plot (X2,y, c= 'grey', linewidth=0.7)

#Positions of players
plt.scatter(list (position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == attacking_team)]['X']), list(position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == attacking_team)]['Y']), c='red', s=20)
plt.scatter(list (position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == defending_team)]['X']), list(position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == defending_team)]['Y']), c='black', s=20)
#Position of ball
plt.scatter(position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == 'BALL')]['X'].item(), position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == 'BALL')]['Y'].item(), c='blue', s=5)

# Caluclations for Pressure in right order
attackers = position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == attacking_team)]
Ball = position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == 'BALL')]
Dis= []
for i, att in attackers.iterrows ():
    dis = math.sqrt((att['X'] - Ball['X'].item())**2 + (att['Y'] - Ball['Y'].item())**2)
    Dis.append (dis)
attackers['Distance'] = Dis
attackers = attackers.sort_values (by=['Distance'], ascending=True)

Pressure_list = [possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnBallPressure_LastAction.item() *1.5, 
                 possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnGroupPressure1_LastAction.item()*1.5, 
                 possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnGroupPressure2_LastAction.item()*1.5, 
                 possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnGroupPressure3_LastAction.item()*1.5, 
                 possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnGroupPressure4_LastAction.item()*1.5, 
                 possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnGroupPressure5_LastAction.item()*1.5, 
                 possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnGroupPressure6_LastAction.item()*1.5, 
                 possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnGroupPressure7_LastAction.item()*1.5,
                 possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnGroupPressure8_LastAction.item()*1.5,
                 possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnGroupPressure9_LastAction.item()*1.5,
                 possessions[(possessions[f'Frame{Action}Action'] == Frame)].OnGroupPressure10_LastAction.item()*1.5]

#Pressure on attacking players
plt.scatter (list (attackers['X']), list(attackers['Y']), s = Pressure_list, c='green', alpha=0.3)

plt.show ()

#%% Figure of playing situation without pressure values
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
start_frame = 57800.92
end_frame = 57804.92


frames = [end_frame, start_frame]
#74824.32	74823.56	74822.56	74821.6


team_list = list (event_data.Team.unique ())
team_list = [x for x in team_list if str(x) != 'nan']
team1 = team_list[0]
team2 = team_list[1]


frames = position_data[(position_data['T_sec'] <= frames[0]) &
                     (position_data['T_sec'] >= frames[1])].T_sec.unique ()
#frames = frames[::8]


for row in frames:
    
    #Frame
    Frame = row
    
    #Figure details
    #plt.figure(dpi=300)
    fig, ax = plt.subplots(dpi=500)
    plt.title(f"{Frame}")
    plt.xlim (-5,110)
    plt.ylim (-5,73)
    
    #lines of pitch
    plt.plot ([0,16,16,0], [54,54,14,14], c='grey', linewidth=0.7)
    plt.plot ([105,89,89,105], [54,54,14,14], c='grey', linewidth=0.7)
    plt.plot ([0,5.5,5.5,0],[43,43,25,25], c= 'grey', linewidth=0.7)
    plt.plot ([105,99.5,99.5,105],[43,43,25,25], c= 'grey', linewidth=0.7)
    plt.plot ([0,0,105,105,0], [0,68,68,0,0], c= 'grey', linewidth=0.7)
    plt.plot ([52.5,52.5], [68,0], c= 'grey', linewidth=0.7)
    plt.scatter ([11,52.5, 94],[34,34,34],c= 'grey',s= 4)
    circle = Circle((52.5,34), 11, Fill=False, color='grey', linewidth=0.7)
    ax.add_artist (circle)
    
    #Circles of pitch
    Y1 = list (np.linspace (0,9, num=25))
    Y2 = list (np.linspace (9,0, num=25))
    Y = Y2 + Y1
    X = []
    X2 = []
    for value in Y:
        x = (math.sqrt (value**2 + 9**2) - 9 )*(-1)
        X.append (x)
    X = [i - (min (X)) + 16 for i in X]
    for value in Y:
        x2 = math.sqrt (value**2 + 9**2) - 9 
        X2.append (x2)
    X2 = [i - (max (X2)) + 89 for i in X2]
    
    y = list (np.linspace (26, 42, num=50))
    plt.plot (X,y, c= 'grey', linewidth=0.7)
    plt.plot (X2,y, c= 'grey', linewidth=0.7)
    
    #Positions of players
    plt.scatter(list (position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == team1)]['X']), list(position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == team1)]['Y']), c='red', s=20)
    for row, player in position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == team1)].iterrows ():
        plt.annotate ((player['PersonId']),  xy = (player['X'], player['Y']), size =4, c='red')
    plt.scatter(list (position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == team2)]['X']), list(position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == team2)]['Y']), c='black', s=20)
    for row, player in position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == team2)].iterrows ():
        plt.annotate ((player['PersonId']),  xy = (player['X'], player['Y']), size =4, c='black')
    #Position of ball
    plt.scatter(position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == 'BALL')]['X'].item(), position_data[(position_data['T_sec'] == Frame) & (position_data['TeamId'] == 'BALL')]['Y'].item(), c='blue', s=5)
    
    plt.show ()

