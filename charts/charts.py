import matplotlib.pyplot as plt

def gerate_pie_chart():
    label = ['A','B','C']
    values = [2,34,120]
    fig,ax = plt.subplots()
    ax.pie(values,labels=label)
    plt.savefig('.png')
    plt.close()