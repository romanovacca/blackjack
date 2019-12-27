import gym
from Environment import BlackjackEnv
env = BlackjackEnv()
env.reset()

for i_episode in range(20):
    player_hand,dealer_hand,has_usable_ace = env.reset()
    for t in range(100):
        #env.render()
        print(f"Player hand is {player_hand}, the dealer has {dealer_hand}, "
              f"and the player has usable ace is {has_usable_ace}")
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()



