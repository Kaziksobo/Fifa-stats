import json, os, re
from pathlib import Path
import pandas as pd

def season_adder(current: str) -> str:
    end_year = current.split('_')[1]
    return f'{end_year}_{str(int(end_year) + 1)}'

def version_adder(season: str, version: str) -> str:
    versions = ['start', 'summer_end', 'winter_end', 'end']
    next_version_num = versions.index(version) + 1
    if next_version_num > 3:
        next_version_num = 0
        season = season_adder(season)
    next_version = versions[next_version_num]
    return season, next_version

def best_version(season: str) -> str:
    unformatted_files = os.listdir(f'C:/Users/kazik/OneDrive/Desktop/Stuff/fifa/Data/{season}/Players')
    files = [file.removesuffix('.json') for file in unformatted_files]
    versions = ['start', 'summer_end', 'winter_end', 'end']
    best_version = 0
    for file in files:
        num = versions.index(file)
        if num > best_version:
            best_version = num
    return versions[best_version]

def players_path_generator(season: str, version: str) -> str:
    folder = Path(f'C:/Users/kazik/OneDrive/Desktop/Stuff/fifa/Data/{season}/')
    return folder / f'players/{version}.json'

def matches_path_generator(season: str, comp: str) -> str:
    folder = Path(f'C:/Users/kazik/OneDrive/Desktop/Stuff/fifa/Data/{season}/')
    return folder / f'matches/{comp}.json'

def loader(version: str, season: str) -> tuple:
    players_path = players_path_generator(season, version)
    players = json.load(open(players_path, encoding='utf-8'))
    teams_path = Path('C:/Users/kazik/OneDrive/Desktop/Stuff/fifa/utilities/teams.json')
    teams = json.load(open(teams_path, encoding='utf-8'))
    matches = {}
    for comp in ['LaLiga', 'UCL', 'Copa']:
        file_path = matches_path_generator(season, comp)
        try:
            match = json.load(open(file_path, encoding='utf-8'))
            matches[comp] = match
        except json.JSONDecodeError:
            continue
    return players, matches, teams

def remove_sold(players: list) -> list:
    for player in players:
        if player['Status'] == 'Sold':
            players.remove(player)
    
    return players

def remove_loan(players: list) -> list:
    for player in players:
        if player['Status'] == 'On Loan':
            players.remove(player)
    return players

def create_players_dataframe(players: list):
    players_df = pd.DataFrame(players)
    players_df = players_df.drop('Injuries', axis=1).drop('Loan', axis=1).drop('Bonus', axis=1).drop('MatchRating', axis=1).drop('MinutesPlayedp90', axis=1)
    players_df['DateSigned'] = pd.to_datetime(players_df['DateSigned'])
    players_df['DateSold'] = pd.to_datetime(players_df['DateSold'])
    return players_df

def team_id2team(teams: list, team_id: str) -> str:
    for team in teams:
        if team['Id'] == team_id:
            return team['Name']

def player_id2player(players: list, player_id: int) -> str:
    for player in players:
        if player['Id'] == player_id:
            return player['FirstName'] + ' ' + player['LastName']

def stats_conv(stat: str) -> str:
    if 'pp' in stat:
        stat = stat.replace('pp', 'per % possession')
    if 'pShot' in stat:
        stat = stat.replace('pShot', ' per shot')
    if 'p90' in stat:
        stat = stat.replace('p90', ' per 90')
    if 'xGC' in stat:
        stat = stat.replace('xGC', 'Expected goal contributions')
    if 'xG' in stat:
        stat = stat.replace('xG', 'Expected goals')
    if 'xA' in stat:
        stat = stat.replace('xA', 'Expected assists')
    stat = re.sub(r"(\w)([A-Z])", r"\1 \2", stat)
    stat = stat.lower().capitalize()
    return stat