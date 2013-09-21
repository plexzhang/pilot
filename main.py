#!/usr/bin/env python

import sys
import numpy as np
from pendulum.pendulum_world import PendulumWorld
from pendulum.pendulum_controller import PendulumController
from pendulum.pendulum_predictor import PendulumPredictor


def run(theta):
    world = PendulumWorld()
    controller = PendulumController(None)
    predictor = PendulumPredictor()

    world.state['theta'] = np.deg2rad(theta)

    while True:
        state = world.observe()
        printState(state)

        predictor.disableLearning()
        force = controller.act(state, predictor)
        printForce(force)

        predictor.enableLearning()
        predictor.learn(state, force)

        world.tick(force)


def printState(state):
    print "angle: " + str(np.rad2deg(state['theta'])) + "\t" + "position: " + str(state['x'])


def printForce(force):
    print "force: " + str(force['x'])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        theta = int(sys.argv[1])
        run(theta)
    else:
        print "Usage: python main.py [theta]"