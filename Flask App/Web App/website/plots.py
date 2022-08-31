import matplotlib.pyplot as plt
import seaborn as sns

def plotting_frequency(df):

    plt.switch_backend('Agg')

    
   
    
    sns.set(rc={'figure.figsize':(10.7,10.7)})   
    sns.set_style("white") 
    sns.set(font_scale = 1.6)
    

    freq_plot = sns.barplot(x='frequency',y='pairs',data=df[df['frequency']>1])

    plt.tight_layout()


    fig = freq_plot.get_figure()
    fig.savefig("/Users/ruiferreira/Desktop/Universe/Ironhack/Bootcamp/Projects/Project 6 - FINAL/Flask App/Web App/website/static/images/freq_plot.png")
    

def plot_spec(x,y):    

    plt.switch_backend('Agg')

    plt.figure(figsize=(15.85, 3), dpi=70)

    plt.ylim(0, 1)


    line_plot = plt.plot(x,y)


    plt.tight_layout()


    plt.savefig('/Users/ruiferreira/Desktop/Universe/Ironhack/Bootcamp/Projects/Project 6 - FINAL/Flask App/Web App/website/static/images/line_plot.png')