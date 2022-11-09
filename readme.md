# Data for my Fifa 22 career mode
I am storing and analysing data for my FC Barcelona career mode, starting from the 25/26 season.

## Data
Data is stored (in Json format) on both players and matches.

### Match data
Data is stored on matches from the Champions League, Copa del Rey and La Liga.
Data is not stored on friendlies, such as pre-season, Copa Europe and the Supercopa.

The match data is split up into three Json files depending on the competition they were played in.

Notes:

- The key passes stat is kinda useless as it is down to style of play, so my team will always have a higher number
- Fifa's xG model is a bit crap, it's xG values are often alot higher than they should be (I have seen shots with 1 xG)
- If a goal is scored by the opposing team, the "Scorer" and "Assister" values will be null as data is not kept on non-Barcelona players
- The Id increments by one each game, with the sequence following through every competition

Variables stored for each match:

- "Id" (string): The unique 5 digit Id of the match
- "Date" (string): The date of the match (in the format yyyy-mm-dd)
- "Label" (string): The label of the match (e.g. 'FC Barcelona - UD Almería')
- "MOTM" (string): The man of the match (Their ID is stored)
- For each team:
  - "Id" (string): The ID of the team (only stored for the opposing team)
  - "ScoreHT" (integer): The score of the match at half time
  - "ScoreFT" (integer): The score of the match at full time
  - "Side" (string): If the team is at home or away
  - "PossessionHT" (float): The team's possession at half time (stored as a decimal value)
  - "PossessionFT" (float): The team's possession at full time (stored as a decimal value)
  - "Shots" (integer): The number of shots the team took that match
  - "ShotsOnTarget" (integer): The number of on-target shots the team took that match
  - "xG" (float): The team's total expected goals for the match
  - "Passes" (integer): The number of passes the team attempted that match
  - "PassesCompleted" (integer): The number of passes the team completed that match
  - "KeyPasses" (integer): The number of key passes the team made that match
  - "FoulsCommitted" (integer): The number of fouls the team committed that match
  - "TacklesWon" (integer): The number of tackles the team won that match
  - "PenaltiesTaken" (integer): The number of penalties the team took that match
  - "PenaltiesScored" (integer): The number of penalties the team scored that match
  - "PenaltiesConceded" (integer): The number of penalties the team conceded that match
  - "YellowCards" (integer): The number of yellow cards the team received that match
  - "RedCards" (integer): The number of red cards the team received that match
- For each Barcelona player in the starting line-up and on the bench:
  - "PlayerId" (string): The ID of the player
  - "MinutesPlayed" (integer): The number of minutes the player played that match
  - "PositionsPlayed" (list of strings): A list of the positions the player played in the match (the minutes per position is not accounted for)
  - "MatchRating" (float): Fifa's rating of the player's performance that match
  - "GoalsConceded" (integer): The number of goals the team conceded whilst the player was playing
  - "OwnGoals" (integer): The number of own goals the player conceded that match
  - "Goals" (integer): The number of goals the player scored that match
  - "Assists" (integer): The number of assists the player made that match
  - "Shots" (integer): The number of shots the player took that match
  - "ShotsOnTarget" (integer): The number of on-target shots the player took that match
  - "penaltiesTaken" (integer): The number of penalties the player took that match
  - "PenaltiesScored" (integer): The number of penalties the player scored that match
  - "PenaltiesConceded" (integer): The number of penalties the player conceded that match
  - "xG" (float): The player's total expected goals that match
  - "xA" (float): The player's total expected assists that match
  - "Passes" (integer): The number of passes the player attempted that match
  - "PassesCompleted" (integer): The number of passes the player completed that match
  - "Possession" (float): The amount of possession the player had that match (stored as a decimal value)
  - "PossessionWon" (integer): The number of times the player won possession that match
  - "PossessionLost" (integer): The number of times the player lost possession that match
  - "YellowCards" (integer): The number of yellow cards the player received that match
  - "RedCards" (integer): The number of red cards the player received that match
  - If the player is a goalkeeper:
    - "ShotsFaced" (integer): The number of on-target shots the player faced that match
    - "Saves" (integer): The number of saves the player made that match
    - "PenaltiesFaced" (integer): The number of penalties the player faced that match
    - "PenaltiesSaved" (integer): The number of penalties the player saved that match
- For each goal:
  - "ScoringSide" (string): The side of the team that scored
  - "Minute" (integer): The minute the goal was scored
  - "Scorer" (string): The id of the player that scored
  - "Assister" (string): The id of the player that assisted the goal
  - "ShotType" (string): The type of shot

### Player data

Data is stored on all players that were in the team as of July 1st 2025.
Player's that have been sold since then are kept in the dataset, but these variables are set to null: "SquadNumber", "SlowedDevelopment", "Wage", "Bonus", "ContractLength", "ReleaseClause", "SquadRole"

The data is updated at the start of the season, at the end of the summer transfer window, at the end of the winter transfer window and at the end of the season.
Each update is stored in a new Json file, which will be one of: "start.json", "summer_end.json", "winter_end.json", "end.json"

Variables stored for each player:

- "ID" (string): The unique 3 digit Id of the player
- "FirstName" (string): The first name of the player
- "LastName" (string): The last name of the player
- "SquadNumber" (integer): The player's squad number
- "Nationality" (string): The player's nationality
- "Academy" (boolean): If the player came from the Barcelona academy
- "Position" (string): The player's position
- "Height" (integer): The player's height in inches
- "Weight" (integer): The player's weight in lbs
- "Foot" (string): The player's preferred foot
- "Rating" (string): The player's overall Fifa rating
- "SlowedDevelopment" (boolean): If the player's development has slowed down
- "Age": The player's age
- "Value" (integer): The player's transfer value in euros
- "Wage" (integer): The player's wage per week in euros
- Bonus data:
  - "Type" (string): The type of bonus (e.g. appearances, goals etc.)
  - "Goal" (integer): The number of the type they have to reach to trigger the bonus
  - "Reward" (integer): The amount of money (in euros), they get for reaching the goal
  - "Achieved" (boolean): If the player has achieved the bonus
- "ContractLength" (integer): The number of years left on the contract (this is always rounded down, so 1yr 10months would be 1yr)
- "ReleaseClause" (integer): The player's release clause
- "SquadRole": The player's squad role as stated in their contract
- "Status" (string): The player's status (either 'At Club', 'On Loan' or 'Sold')
- Loan data:
  - "LoanLength" (string): The number of years left on the loan (this is also rounded down)
  - "LengthCompleted" (integer): The number of years of the loan already completed
  - "LoanClub" (string): The club the player has been loaned to
  - "BuyOption" (integer): The price the loan club can buy the player for
- "TransferCost" (integer): The transfer fee Barcelona paid for the player
- "SalePrice" (integer): The price Barcelona sold the player for
- "DateSigned" (string): The date the player was signed (in the format yyyy-mm)
- "DateSold" (string): The date the player was sold (in the format yyyy-mm)
- Injury data:
  - "DateInjured" (string): The date the player was injured (in the format yyyy-mm-dd)
  - "InjuryLength" (integer): The number of days until the player was fully fit
  - "InjuryType" (string): The type of injury
- "LeagueTopScorerRank" (integer): The player's position in the league top scorer ranking
- "LeagueTopAssistRank" (integer): The player's position in the league top assister ranking
- "LeagueTopCleanSheetsRank" (integer): The player's position in the league top clean sheets ranking
- "LeagueTopYellowCardsRank" (integer): The player's position in the league top yellow cards ranking
- "LeagueTopRedCardsRank" (integer): The player's position in the league top red cards ranking