from src.Environment import BlackjackEnv
from Logging.Logger import Customlogger

logger = Customlogger(__name__)
env = BlackjackEnv()
# wins = 0
# losses = 0
# draws = 0
for i_episode in range(100):
    env.reset()
    for t in range(100):
        info, done = env.step()
        if done:
            #print(info)
            # print("\n")
            # if env.deck.true_count > 2 and env.deck.percentage_of_deck_left <\
            #         55:
                #print(info)
                #print(reward)
                #print(env.deck.percentage_of_deck_left)
                #print(f"Running count:{env.deck.running_count}")
                #print(f"True count:{env.deck.true_count}\n")
            #print(f"Running count:{env.deck.running_count}")
            #print(f"True count:{env.deck.true_count}\n")
            #print(env.deck.percentage_of_deck_left)

            break
print(env.reward.final_result())
env.close()
