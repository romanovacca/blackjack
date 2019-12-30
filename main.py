from src.Environment import BlackjackEnv
from Logging.Logger import Customlogger

logger = Customlogger(__name__)
env = BlackjackEnv()

for i_episode in range(20):
    player_hand,dealer_hand = env.reset()
    for t in range(100):
        action = env.take_action()
        observation, done, info = env.step(action)
        if done:
            logger.log_message(f"Episode finished after {t+1} timesteps\n")
            break
env.close()



