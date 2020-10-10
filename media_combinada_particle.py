## codigo  referente  ao  problema  4 ##

from particle import Particle

# # para mais informações sobre o pacote --> https://pypi.org/project/particle/ 

Barion_Lambda = Particle.findall('Lambda')[0]
Barion_Omega_minus = Particle.findall('Omega')[0]
Lepton_tau_minus = Particle.findall('t')[2]
Meson_D_plus = Particle.findall('D')[0]
Meson_B_neutral = Particle.findall('B')[0]

sigma_Barion_Lambda = 0.006
sigma_Barion_Omega_minus = 0.3
sigma_Lepton_tau_minus = 0.12
sigma_Meson_D_plus = 0.05
sigma_Meson_B_neutral = 0.12

sigma = ( 1 ) / ( (1/sigma_Barion_Lambda**2) + 
(1/sigma_Barion_Omega_minus**2) + 
(1/sigma_Lepton_tau_minus**2) + 
(1/sigma_Meson_D_plus**2) +
(1/sigma_Meson_B_neutral**2) )

mass_media = ( (sigma/sigma_Barion_Lambda)**2) * Barion_Lambda.mass + ( (sigma/sigma_Barion_Omega_minus)**2) * Barion_Omega_minus.mass + ( (sigma/sigma_Lepton_tau_minus)**2) * Lepton_tau_minus.mass + ( (sigma/sigma_Meson_D_plus)**2) * Meson_D_plus.mass + ( (sigma/sigma_Meson_B_neutral)**2) * Meson_B_neutral.mass 

