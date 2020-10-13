## codigo  referente  ao  problema  4 ##

import pandas as pd

def soma_sigma(erro):
    return float( ( 1/(erro.apply(lambda x: 1/(x * x))).sum() )**0.5 )

def soma_massa(sigma_combinado,sigma_lista,massa_lista):
	return (((sigma_combinado/sigma_lista[0])**2)*massa_lista[0]).sum()


# ----------------- Muon ----------------- #

mass_muon = pd.DataFrame([0.1134289267,0.1134289256,0.1134289264,0.1134289168,0.113428913])
sigma_muon = pd.DataFrame([0.0000000029,0.0000000029,0.0000000030,0.0000000034,0.000000017])

sigma_combinado_muon = soma_sigma(sigma_muon)
massa_combinada_muon = soma_massa(sigma_combinado_muon,sigma_muon,mass_muon)

# ------------------ Quark top ------------------ #

mass_quark_t = pd.DataFrame([172.69,172.26,172.33,172.95,172.44,174.30])
sigma_quark_t = pd.DataFrame([0.25,0.07,0.14,0.77,0.13,0.35])

sigma_combinado_quart_t = soma_sigma(sigma_quark_t)
massa_combinada_quark_t = soma_massa(sigma_combinado_quart_t,sigma_quark_t,mass_quark_t)

# ------------------ D0 ------------------ #

mass_D0 = pd.DataFrame([1864.845,1864.75,1864.841,1865.30,1864.847])
sigma_D0 = pd.DataFrame([0.025,0.15,0.048,0.33,0.150])

sigma_combinado_D0 = soma_sigma(sigma_D0)
massa_combinada_D0 = soma_massa(sigma_combinado_D0,sigma_D0,mass_D0)

# ------------------ Z0 ------------------ #

mass_Z0 = pd.DataFrame([1864.845,1864.75,1864.841,1865.30,1864.847])
sigma_Z0 = pd.DataFrame([0.025,0.15,0.048,0.33,0.150])

sigma_combinado_Z0 = soma_sigma(sigma_Z0)
massa_combinada_Z0 = soma_massa(sigma_combinado_Z0,sigma_Z0,mass_Z0)

# ------------------ Omega- ------------------ #

mass_Omega = pd.DataFrame([1673.0,1673.0,1673.7,1673.4,1673.3,1673.8,1673.2,1673.1])
sigma_Omega = pd.DataFrame([1,0.8,0.6,1.7,1,0.8,1.6,1.0])

sigma_combinado_Omega = soma_sigma(sigma_Omega)
massa_combinada_Omega = soma_massa(sigma_combinado_Omega,sigma_Omega,mass_Omega)
