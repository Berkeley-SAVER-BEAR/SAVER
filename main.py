def initialize():
    pass

def main():
    models = initialize()

    robot_loop = RobotLoop(*models)

    while True:
        robot_loop.run()

if __name__ == "__main__":
    main()