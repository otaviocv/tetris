import numpy as np
import retro
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GAME = "Tetris-Nes"
START = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0])
DOWN = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0])
NULL = np.array([0, 1, 0, 0, 0, 0, 0, 0, 0])
BUTTONS = np.array(["B", "null", "SELECT", "START", "UP",
                    "DOWN", "LEFT", "RIGHT", "A"])
ACTIONS_MASK = np.array([1, 1, 0, 0, 1, 1, 1, 1, 1])
assert BUTTONS.shape == ACTIONS_MASK.shape


def main():
    retro.data.Integrations.add_custom_path(
            os.path.join(SCRIPT_DIR, "custom_integrations")
    )
    print(GAME in retro.data.list_games(inttype=retro.data.Integrations.ALL))
    env = retro.make(GAME, inttype=retro.data.Integrations.ALL)
    print(env)
    obs = env.reset()
    for i in range(500):
        env.step(NULL)
    env.step(START)
    env.step(START)
    env.step(START)
    env.step(START)
    env.step(START)
    env.step(START)
    env.render()
    for i in range(100):
        env.step(NULL)
    env.step(START)
    env.render()
    for i in range(100):
        env.step(NULL)
    env.step(START)
    env.render()
    for i in range(20000000000):
        action = env.action_space.sample()
        action[~ACTIONS_MASK] = 0
        action[2] = 0
        action[3] = 0
        print(action)
        print(traslate_to_buttons(action))
        obs, rew, done, info = env.step(action)
        print(rew, done, info)
        env.render()
        if done:
            break
    env.close()

def traslate_to_buttons(action):
    return [BUTTONS[i] for i, a in enumerate(action) if a > 0]

if __name__ == "__main__":
        main()
