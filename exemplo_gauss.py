import pandas as pd
from scipy.stats import chi2

pendulo = pd.DataFrame([0.7743,0.7723,0.7717,0.7737,0.7720,0.7707,0.7723,0.7740,0.7743,
0.7730,0.7743,0.7737,0.7733, 0.7733,0.7730,0.7737,0.7723,0.7723,0.7730,0.7737,
0.7713,0.7727,0.7713,0.7740,0.7720,0.7727,0.7723,0.7740,0.7723,0.7723,0.7727,
0.7717,0.7703,0.7723,0.7743,0.7733,0.7730,0.7737,0.7723,0.7757,0.7717,0.7737,0.7740,
0.7757,0.7743,0.7707,0.7740,0.7723,0.7743,0.7710,0.7727,0.7723,0.7723,0.77200,
0.7717,0.7733,0.7727,0.7733,0.7723,0.7737,0.7723,0.7730,0.7740,0.7757,
0.7710,0.7703,0.7727,0.7730,0.7723,0.7710,0.7740,0.7727,0.7713,0.7703,0.7733,
0.7720,0.7723,0.7700,0.7730,0.7750])

media = pendulo.mean()[0]
sigma  = pendulo.std()[0]

grupo1 = pendulo.loc[pendulo[0] < (media - sigma) ]
grupo2 = pendulo.loc[pendulo[0] > (media - sigma)].loc[pendulo[0] < media]
grupo3 = pendulo.loc[pendulo[0] < (media + sigma)].loc[pendulo[0] > media]
grupo4 = pendulo.loc[pendulo[0] > (media + sigma) ]

sns.distplot(pendulo[0],fit=norm,kde=False, color = 'red',axlabel='T')
plt.plot([media,media],[0,400],label = "Media: {:2.3f}".format(media) )
plt.legend(loc='best')
plt.show()

esperados  = [ 12.69,27.30,27.30,12.69] 
observados = [ len(grupo1),len(grupo2),len(grupo3),len(grupo4) ]
print(chisquare(esperados,observados))
