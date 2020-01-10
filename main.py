from src.Environment import BlackjackEnv
from Logging.Logger import Customlogger

logger = Customlogger(__name__)
minimum_bet = 1
env = BlackjackEnv()
number_of_players = 1
#strategies = ["Random","Random","Random"]
strategies = ["Random"]
stand_on_17 = True

#result_type = "individual"
result_type = "summary"

for i_episode in range(1000):
    env.reset(i_episode,number_of_players,strategies)
    env.step(stand_on_17)

    if result_type == "individual":
        env.result(result_type)

if result_type == "summary":
    env.result(result_type)

env.close()
