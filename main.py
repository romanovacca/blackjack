from src.Environment import BlackjackEnv
from Logging.Logger import Customlogger

logger = Customlogger(__name__)
env = BlackjackEnv()
number_of_players = 2
#result_type = "individual"
result_type = "summary"
for i_episode in range(2):
    env.reset(number_of_players)
    env.step()
    if result_type == "individual":
        env.result(result_type)
if result_type == "summary":
    env.result(result_type)
env.close()
