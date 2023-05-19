import matplotlib.pyplot as plt 
import seaborn as sns 

def prettier_graph():  
    sns.set_style("darkgrid") 
    plt.rc('axes', titlesize = 18) 
    plt.rc('axes', labelsize = 14)
    plt.rc('xtick', labelsize = 13) 
    plt.rc('ytick', labelsize = 13)
    plt.rc('legend', fontsize =13)
    plt.rc('font', size = 13)
    sns.diverging_palette(220, 20, as_cmap=True)
