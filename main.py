from src.Environment import BlackjackEnv
from Logging.Logger import Customlogger

logger = Customlogger(__name__)
env = BlackjackEnv()
wins = 0
losses = 0
draws = 0
for i_episode in range(10):
    env.reset()
    for t in range(100):
        reward, info, done = env.step()
        if done:
            print(info)
            print(reward)
            #print("\n")
            #logger.log_message(f"Running count:{env.cards.running_count}")
            #logger.log_message(f"Running count:{env.cards.true_count}\n")
            if reward == 0:
                draws +=1
            elif reward == 1:
                losses +=1
            else:
                wins +=1
            break

print(wins,losses,draws)
env.close()
