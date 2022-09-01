import matplotlib.pyplot as plt
import seaborn as sns

def plotting_frequency(df):

    plt.switch_backend('Agg')
    #sns.set_theme()
    
    
    sns.set(rc={'axes.facecolor':'(0.43137255, 0.62745098, 0.96470588)', 'figure.facecolor':'(0.43137255, 0.62745098, 0.96470588)','figure.figsize':(10.7,10.7)},font_scale = 1.7)
    
    
    
    

    freq_plot = sns.barplot(x='frequency',y='pairs',data=df[df['frequency']>1], palette='plasma')

    


    freq_plot.grid(False)
    freq_plot.spines.top.set_visible(False)
    freq_plot.spines.right.set_visible(False)


    plt.tight_layout()
    plt.show()

    fig = freq_plot.get_figure()
    fig.savefig("/Users/ruiferreira/Desktop/Universe/Ironhack/Bootcamp/Projects/Project 6 - FINAL/Flask App/Web App/website/static/images/freq_plot.png")

   



def plot_spec(x,y):    


    plt.switch_backend('Agg')

    fig = plt.figure(figsize=(15, 4), dpi=75)

    plt.ylim(0, 1)

    plt.plot(x,y, "m-")

    plt.tight_layout()

    plt.xlabel("Thoughts", fontsize = 15)

    plt.ylabel("Positive Sentiment", fontsize = 15)

    plt.title("Positive Sentiment by Thought", fontsize = 17)

    plt.grid(False)

    ax = plt.gca()
    
    ax.set_facecolor((129/255,174/255,251/255))

    fig.patch.set_facecolor((129/255,174/255,251/255))

    plt.tight_layout()


    plt.savefig('/Users/ruiferreira/Desktop/Universe/Ironhack/Bootcamp/Projects/Project 6 - FINAL/Flask App/Web App/website/static/images/line_plot.png')