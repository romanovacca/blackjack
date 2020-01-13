from src.Environment import BlackjackEnv
from Logging.Logger import Customlogger

logger = Customlogger(__name__)
ante = 1
env = BlackjackEnv(ante = ante,
                   use_sidebet=False)

number_of_players = 2
strategies = ["Random","Random","Random"]
#strategies = ["Random"]
stand_on_17 = False

#result_type = "individual"
result_type = "summary"

for i_episode in range(10000):
    env.reset(i_episode,number_of_players,strategies)
    env.step(stand_on_17)

    if result_type == "individual":
        env.result(result_type)

if result_type == "summary":
    env.result(result_type)

env.close()
