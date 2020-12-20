import requests


params = {}
params['sport'] = 'NHL'
params['league_id'] = 12093
params['season'] = 2019
params['draft_number'] = 1


url = 'https://www.fleaflicker.com/api/FetchLeagueDraftBoard'

r = requests.get(url, params)  #FetchLeagueDraftBoard

r_json = r.json()  # json

draft_order = r_json['draftOrder']  # draft_order is list of teams, ws.flea.api.Team
draft_rows = r_json['rows']  # draft_rows is list of rows (aka rounds), ws.flea.api.DraftBoardRow


pick = 1
for a in draft_rows:  # draft rows is a list of wpi.DraftBoardCell
    DraftBoardCell = a['cells']
    for b in DraftBoardCell:
        Player = b['player']
        proPlayer = Player['proPlayer']
        id = proPlayer['id']  # print (ff player_id, #overall)
        pick += 1


r.close()
del r
