from src.Environment import BlackjackEnv
from Logging.Logger import Customlogger

logger = Customlogger(__name__)
env = BlackjackEnv()

for i_episode in range(10):
    env.reset()
    for t in range(100):
        reward, info, done = env.step()
        if done:
            print(reward)
            print(info)
            print("\n")
            #logger.log_message(f"Running count:{env.cards.running_count}")
            #logger.log_message(f"Running count:{env.cards.true_count}\n")
            break
env.close()
