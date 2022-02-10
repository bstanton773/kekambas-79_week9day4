import matplotlib.pyplot as plt


with plt.style.context('fivethirtyeight'):
    fig, ax = plt.subplots(figsize=(15,10))

    ax.plot([2, 4, 8, 16, 32, 64, 128])

    ax.set_title('VS Code Line Graph')

    plt.show()



with plt.style.context('fivethirtyeight'):
    fig, ax = plt.subplots(figsize=(15,10))

    ax.plot([128, 64, 32, 16, 8, 4, 2])

    ax.set_title('VS Code Line Graph')

    plt.show()