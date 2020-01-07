from src.Environment import BlackjackEnv
from Logging.Logger import Customlogger

logger = Customlogger(__name__)
env = BlackjackEnv()
number_of_players = 1
#result_type = "individual"
result_type = "summary"
for i_episode in range(100000):
    env.reset(i_episode,number_of_players)
    env.step()

    if result_type == "individual":
        env.result(result_type)

if result_type == "summary":
    env.result(result_type)

env.close()
