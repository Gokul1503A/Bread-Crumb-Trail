import matplotlib.pyplot as plt

def read_bot_path(filename="bot_path.txt"):
    path = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split(','))
            path.append((x, -y))
    return path

def plot_bot_path(path):
    plt.plot(*zip(*path), marker='o', linestyle='-', color='b')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bot Path')
    plt.show()

# Read bot path from file
bot_path = read_bot_path()

# Plot the bot path
plot_bot_path(bot_path)
