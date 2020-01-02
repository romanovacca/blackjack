from src.Environment import BlackjackEnv
from Logging.Logger import Customlogger

logger = Customlogger(__name__)
env = BlackjackEnv()

for i_episode in range(50):
    player_hand,dealer_hand,player_natural_blackjack = env.reset()
    for t in range(100):
        if not player_natural_blackjack:
            action = env.take_action()
        else:
            action = 0
        observation, done, info = env.step(action)
        if done:
            logger.log_message(f"Running count:{env.cards.running_count}")
            logger.log_message(f"Running count:{env.cards.true_count}\n")
            break
env.close()



