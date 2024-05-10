'''
───────────────────────────────────────────────────────────────────────────
Predefined probability distribution for acoustic numerical breast phantom
(NBP) generation
───────────────────────────────────────────────────────────────────────────
Author:   Seonyeong Park (sp33@illinois.edu)
Date:     June 20, 2023

This includes a class `Acou_prop` to specify the considered acoustic 
properties of breast tissues and lesion. The considered acoustic properties
include sound speed `c` (mm/μs), density `ρ` (g/mm^3), and acoustic 
attenuation coefficient `α_0` (dB/MHz^ymm) with power law exponent `y`.

  Table 7 Acoustic properties of breast tissues and lesion [Park2023]
  ┌──────────────┬─────────────────┬──────────────────┬──────────────────┐
  │ Medium       │ c (mm/μs)       │ ρ (g/mm^3)	      │ α_0 (dB/MHz^ymm) │
  ├──────────────┼─────────────────┼──────────────────┼──────────────────┤
  │ Water^{a}    │ 1.521           │ 0.993 x 10^{-3}  │ 2.2 x 10^{-4}    │
  ├──────────────┼─────────────────┼──────────────────┼──────────────────┤
  │ Fat          │ TN(1.44, 0.021, │ TN(0.911, 0.053, │ N(0.038, 0.004)  │
  │              │ 1.41, 1.49)     │ 0.812, 0.961) x  │                  │
  │              │                 │ 10^{-3}          │                  │
  ├──────────────┼─────────────────┼──────────────────┼──────────────────┤
  │ Glandular/   │ TN(1.54, 0.015, │ TN(1.041, 0.045, │ N(0.075, 0.008)  │
  │ TDLU/duct    │ 1.517, 1.567)   │ 0.99, 1.092) x   │                  │
  │              │                 │ 10^{-3}          │                  │
  ├──────────────┼─────────────────┼──────────────────┼──────────────────┤
  │ Ligament     │ TN(1.457, 0.019,│ TN(1.142, 0.045, │ N(0.126, 0.013)  │
  │              │ 1.422, 1.496)   │ 1.1, 1.175) x    │                  │
  │              │                 │ 10^{-3}          │                  │
  ├──────────────┼─────────────────┼──────────────────┼──────────────────┤
  │ Skin/nipple  │ TN(1.555, 0.01, │ TN(1.109, 0.014, │ N(0.184, 0.019)  │
  │              │ 1.53, 1.58)     │ 1.1, 1.125) x    │                  │
  │              │                 │ 10^{-3}          │                  │
  ├──────────────┼─────────────────┼──────────────────┼──────────────────┤
  │ Artery/vein  │ TN(1.578, 0.011,│ TN(1.05, 0.017,  │ 0.021            │
  │              │ 1.559, 1.59)    │ 1.025, 1.06) x   │                  │
  │              │                 │ 10^{-3}          │                  │
  ├──────────────┼─────────────────┼──────────────────┼──────────────────┤
  │ VTC/necrotic │ TN(1.548, 0.01, │ TN(0.945, 0.02,  │ N(0.269, 0.02)   │
  │ core         │ 1.531, 1.565)   │ 0.911, 0.999) x  │                  │
  │              │                 │ 10^{-3}          │                  │
  └──────────────┴─────────────────┴──────────────────┴──────────────────┘
  ^{a}Acoustic properties of water are consistent with an assumed 
  temperature of 37°C, which is often used in breast OAT to minimize 
  patient discomfort.

Reference:
  [Park2023] Seonyeong Park, Umberto Villa, Fu Li, Refik Mert Cam, 
          Alexander A. Oraevsky, Mark A. Anastasio, "Stochastic three-
          dimensional numerical phantoms to enable computational studies in
          quantitative optoacoustic computed tomography of breast cancer,"
          J. Biomed. Opt. 28(6) 066002 (20 June 2023)
          https://doi.org/10.1117/1.JBO.28.6.066002
  [Park2020] Seonyeong Park, Umberto Villa, Richard Su, Alexander Oraevsky,
          Frank J. Brooks, Mark A. Anastasio, "Realistic three-dimensional 
          optoacoustic tomography imaging trials using the VICTRE breast 
          phantom of FDA (Conference Presentation)," Proc. SPIE 11240, 
          Photons Plus Ultrasound: Imaging and Sensing 2020, 112401H (6 
          March 2020) https://doi.org/10.1117/12.2552380          
  [ETB] The Engineering ToolBox, "Water - speed of sound vs. temperature," 
          https://www.engineeringtoolbox.com/sound-speed-water-d_598.html 
          (2004)
  [Hasgall] P. A. Hasgall, "IT'IS database for thermal and electromagnetic
          parameters of biological tissues,"
          https://www.itis.swiss/database (2018)
  [Malik] B. Malik et al., "Objective breast tissue image classification
          using quantitative transmission ultrasound tomography,” Sci. 
          Rep., 6 1-8 SRCEC3 2045-2322 (2016)
  [Klock] J. C. Klock et al., "Anatomy-correlated breast imaging and visual
          grading analysis using quantitative transmission ultrasound™," 
          Int. J. Biomed. Imaging, 2016 1-9
          https://doi.org/10.1038/srep38857 (2016)
  [Li2009] C. Li et al., "In vivo breast sound-speed imaging with
          ultrasound tomography," Ultrasound Med. Biol., 35 1615-1628 
          https://doi.org/10.1016/j.ultrasmedbio.2009.05.011 USMBA3 0301-
          5629 (2009)
  [Sanchez] A. Sanchez, C. Mills and J. Scurr, “Estimating breast mass-
          density: a retrospective analysis of radiological data,” Breast 
          J., 23 237-239 https://doi.org/10.1111/tbj.12725 BRJOFK 1075-122X
          (2017)
  [André] M. André, J. Wiskin and D. Borup, Clinical Results with 
          Ultrasound Computed Tomography of the Breast, 395-432 Springer 
          Netherlands, Dordrecht (2013)
  [Li2022] F. Li et al., "3-D stochastic numerical breast phantoms for 
          enabling virtual imaging trials of ultrasound computed 
          tomography,” IEEE Trans. Ultrason. Ferroelectr. Freq. Control, 69
          135-146 https://doi.org/10.1109/TUFFC.2021.3112544 ITUCER 0885-
          3010 (2022)

Copyright (C) 2024 Seonyeong Park and Mark Anastasio
          Computational Imaging Science Laboratory
          (https://anastasio.bioengineering.illinois.edu/)
          Department of Bioengineering,
          University of Illinois Urbana-Champaign
          GitHub: https://github.com/comp-imaging-sci/soa-nbp

License : GNU General Public License version 3, Please see 'LICENSE' for 
          details.
'''
import math

class Acou_prop:
  # Sound speed c [mm/μs]
  sound_speed = {
    'water':     1.5206, # Temperature of 37°C considered [ETB]
    'fat':       {'mean': 1.4402, 'std': 0.0209, 'min': 1.412,  'max': 1.485}, # [Malik, Klock]
    'dermis':    {'mean': 1.555,  'std': 0.010,  'min': 1.530,  'max': 1.580}, # [Malik]
    'epidermis': 'dermis',
    'glandular': {'mean': 1.540,  'std': 0.015,  'min': 1.517,  'max': 1.567}, # [Malik, Klock]
    'nipple':    'dermis',
    'ligament':  {'mean': 1.457,  'std': 0.0185, 'min': 1.422,  'max': 1.496}, # [Malik, Klock]
    'tdlu':      'glandular',
    'duct':      'glandular',
    'artery':    {'mean': 1.5782, 'std': 0.0113, 'min': 1.5592, 'max': 1.590}, # [Hasgall]
    'vein':      'artery',
    'vtc':       {'mean': 1.548,  'std': 0.0103, 'min': 1.531,  'max': 1.565}, # [Li2009]
    'nc':        'vtc'
  }

  # Density ρ [g/mm^3]
  density = {
    'water':     993.36*1e-6, # [Hasgall]
    'fat':       {'mean': 911*1e-6,  'std': 53*1e-6,   'min': 812*1e-6,  'max': 961*1e-6},  # [Hasgall]
    'dermis':    {'mean': 1109*1e-6, 'std': 14*1e-6,   'min': 1100*1e-6, 'max': 1125*1e-6}, # [Hasgall]
    'epidermis': 'dermis',
    'glandular': {'mean': 1041*1e-6, 'std': 45.3*1e-6, 'min': 990*1e-6,  'max': 1092*1e-6}, # [Hasgall]
    'nipple':    'dermis',
    'ligament':  {'mean': 1142*1e-6, 'std': 45*1e-6,   'min': 1110*1e-6, 'max': 1174*1e-6}, # [Hasgall]
    'tdlu':      'glandular',
    'duct':      'glandular',
    'artery':    {'mean': 1050*1e-6, 'std': 17*1e-6,   'min': 1025*1e-6, 'max': 1060*1e-6}, # [Hasgall]
    'vein':      'artery',
    'vtc':       {'mean': 945*1e-6,  'std': 20*1e-6,   'min': 911*1e-6,  'max': 999*1e-6},  # [Sanchez]
    'nc':        'vtc'
  }

  # Attenuation coefficient α_0 [dB/MHz^ymm]
  # Unit Np/MHz^ym to dB/MHz^ymm
  dB_mm = 20./math.log(10.)/1000. # 1 Np/MHz^ym = 20./ln(10.) dB/MHz^ym = 20./ln(10.)/1000. dB/MHz^ymm
  alpha_coeff = {
    'water':     0.025328436023*dB_mm, # [Hasgall]
    'fat':       {'mean': 4.3578*dB_mm, 'std': 0.436*dB_mm}, # [Hasgall]
    'dermis':    {'mean': 21.158*dB_mm, 'std': 2.16*dB_mm},  # [Hasgall]
    'epidermis': 'dermis',
    'glandular': {'mean': 8.635*dB_mm,  'std': 0.86*dB_mm},  # [Hasgall]
    'nipple':    'dermis',
    'ligament':  {'mean': 14.506*dB_mm, 'std': 1.45*dB_mm},  # [Hasgall]
    'tdlu':      'glandular',
    'duct':      'glandular',
    'artery':    2.3676*dB_mm,                               # [Hasgall]
    'vein':      'artery',
    'vtc':       {'mean': 31*dB_mm,     'std': 2.3*dB_mm},   # [André]
    'nc':        'vtc'
  }

  # Attenuation power-law exponent y [Li2022]
  y = {
    'A': 1.1151, # Breast is almost entirely fatty
    'B': 1.1642, # Breast has scattered areas of fibroglandular density
    'C': 1.2563, # Breast is heterogeneously dense
    'D': 1.3635  # Breast is extremely dense
  }
  