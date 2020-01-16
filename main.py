from src.Environment import BlackjackEnv
from Logging.Logger import Customlogger

logger = Customlogger(__name__)
ante = 1

Player1 = {
    "name": "Player1",
    "use_sidebet": True,
    "ante": 5,
    "sidebet_ante": 2
}
Player2 = {
    "name": "Player2",
    "use_sidebet": True,
    "ante": 5,
    "sidebet_ante": 2
}

env = BlackjackEnv([Player1, Player2])

number_of_players = 2
strategies = ["Random", "Random", "Random"]
stand_on_17 = True

result_type = "individual"
# result_type = "summary"

for i_episode in range(10):
    env.reset(i_episode, number_of_players, strategies)
    env.step(stand_on_17)

    if result_type == "individual":
        env.result(result_type)

if result_type == "summary":
    env.result(result_type)

env.close()
