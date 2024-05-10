'''
───────────────────────────────────────────────────────────────────────────
Predefined probability distribution for optical numerical breast phantom
(NBP) generation
───────────────────────────────────────────────────────────────────────────
Author:   Seonyeong Park (sp33@illinois.edu)
Date:     June 20, 2023

This includes a class `Opt_prop` to specify the considered optical 
properties of breast tissues and lesion. The considered optical properties
include scattering coefficient parameters `μ_s'` (mm^{-1}) and `b`, 
scattering anisotropy `g`, and refractive index `n`. The values of the 
optical scattering coefficient `μ_s` (mm^{-1}) are calculated using `μ_s'`
and `b`, while the values of the optical absorption coefficient `μ_a` 
(mm^{-1}) are determined based on the generated functional NBPs.

  Table 6 Scattering coefficient parameters, scattering anisotropy, and 
          refractive index of breast tissues and lesion [Park2023]
  ┌────────────────────────┬──────────────┬────────────────┬───────┬──────┐
  │ Medium                 │ μ_s'(λ_{ref})│ b              │ g     │ n    │
  │                        │ (mm^{-1})    │                │       │      │
  ├────────────────────────┼──────────────┼────────────────┼───────┼──────┤
  │ Fat/ligament/TDLU/duct │ 1.06         │ 0.52           │ 0.98  │ 1.44 │
  ├────────────────────────┼──────────────┼────────────────┼───────┼──────┤
  │ Glandular              │ 0.83         │ 0.617          │ 0.96  │ 1.36 │
  ├────────────────────────┼──────────────┼────────────────┼───────┼──────┤
  │ Skin/nipple            │ (3.72, 4.78) │ (1.39, 2.453)  │ 0.65  │ 1.37 │
  ├────────────────────────┼──────────────┼────────────────┼───────┼──────┤
  │ Artery/vein            │ (2.2, 2.295) │ (0.66, 0.872)  │ 0.976 │ 1.35 │
  ├────────────────────────┼──────────────┼────────────────┼───────┼──────┤
  │ VTC/necrotic core      │ (2, 2.07)    │ (0.725, 1.487) │ 0.955 │ 1.39 │
  └────────────────────────┴──────────────┴────────────────┴───────┴──────┘
  A reference wavelength (λ_{ref}) is 500 nm.

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
  [Cerussi] A. E. Cerussi et al., "Sources of absorption and scattering 
          contrast for near-infrared optical mammography," Acad. Radiol., 
          8 211-218 https://doi.org/10.1016/S1076-6332(03)80529-9 (2001)
  [Peters] V. G. Peters et al., "Optical properties of normal and diseased
          human breast tissues in the visible and near infrared," Phys. 
          Med. Biol., 35 1317-1334 
          https://doi.org/10.1088/0031-9155/35/9/010 PHMBA7 0031-9155 
          (1990)
  [Bashkatov] A. N. Bashkatov et al., "Measurement of tissue optical 
          properties in the context of tissue optical clearing," J. Biomed.
          Opt., 23 091416 https://doi.org/10.1117/1.JBO.23.9.091416 JBOPFO 
          1083-3668 (2018)
  [Sandell] J. L. Sandell and T. C. Zhu, "A review of in-vivo optical 
          properties of human tissues and its impact on PDT," J. 
          Biophotonics, 4 773-787 https://doi.org/10.1002/jbio.201100062 
          (2011)
  [Jacques] S. L. Jacques, "Origins of tissue optical properties in the 
          UVA, visible, and NIR regions," in Adv. in Opt. Imaging and 
          Photon Migration, OPC364 (1996)
  [Simpson] C. R. Simpson et al., "Near-infrared optical properties of ex 
          vivo human skin and subcutaneous tissues measured using the Monte
          Carlo inversion technique," Phys. Med. Biol., 43 2465-2478 
          https://doi.org/10.1088/0031-9155/43/9/003 PHMBA7 0031-9155 
          (1998)
  [Iorizzo] T. W. Iorizzo et al., "Temperature induced changes in the 
          optical properties of skin in vivo," Sci. Rep., 11 754 
          https://doi.org/10.1038/s41598-020-80254-9 SRCEC3 2045-2322 
          (2021)
  [Ding] H. Ding et al., "Refractive indices of human skin tissues at eight
          wavelengths and estimated dispersion relations between 300 and 
          1600 nm," Phys. Med. Biol., 51 1479-1489 
          https://doi.org/10.1088/0031-9155/51/6/008 PHMBA7 0031-9155 
          (2006)
  [Alexandrakis] G. Alexandrakis, F. R. Rannou and A. F. Chatziioannou, 
          "Tomographic bioluminescence imaging by use of a combined 
          optical-PET (OPET) system: a computer simulation feasibility 
          study," Phys. Med. Biol., 50 4225-4241 
          https://doi.org/10.1088/0031-9155/50/17/021 PHMBA7 0031-9155 
          (2005)
  [Bosschaart] N. Bosschaart et al., "A literature review and novel 
          theoretical approach on the optical properties of whole blood," 
          Lasers Med. Sci., 29 453-479 
          https://doi.org/10.1007/s10103-013-1446-7 (2014)
  [Meinke] M. Meinke et al., "Empirical model functions to calculate 
          hematocrit-dependent optical properties of human blood,” Appl. 
          Opt., 46 1742-53 https://doi.org/10.1364/AO.46.001742 APOPAI 
          0003-6935 (2007)
  [Sydoruk] O. Sydoruk et al., "Refractive index of solutions of human 
          hemoglobin from the near-infrared to the ultraviolet range: 
          Kramers-Kronig analysis," J. Biomed. Opt., 17 115002 
          https://doi.org/10.1117/1.JBO.17.11.115002 JBOPFO 1083-3668 
          (2012)
  [Zysk] A. M. Zysk, E. J. Chaney and S. A. Boppart, "Refractive index of 
          carcinogen-induced rat mammary tumours," Phys. Med. Biol., 51 
          2165-2177 https://doi.org/10.1088/0031-9155/51/9/003 PHMBA7 0031-
          9155 (2006)

Copyright (C) 2024 Seonyeong Park and Mark Anastasio
          Computational Imaging Science Laboratory
          (https://anastasio.bioengineering.illinois.edu/)
          Department of Bioengineering,
          University of Illinois Urbana-Champaign
          GitHub: https://github.com/comp-imaging-sci/soa-nbp

License : GNU General Public License version 3, Please see 'LICENSE' for 
          details.
'''
class Opt_prop:
  # Optical absorption coefficient [1/mm]
  # Eq. (1) [Park2023]
  #   μ_a(r, λ) = ∑_{i∈I}f_i(r)μ_{a,i}(λ),
  #
  #   μ_a = log(10)*c_tHb*f_b*(s*ϵ_{HbO_2} + (1.-s)*ϵ_{Hb}) 
  #         + f_w*μ_{a,w} + f_f*μ_{a,f} + f_m*μ_{a,m},
  #
  # ϵ_{HbO_2} [1/(mmM)]: Molar extinction coefficient of oxy-hemoglobin
  # ϵ_{Hb}    [1/(mmM)]: Molar extinction coefficient of deoxy-hemoglobin
  # μ_{a,w}   [1/mm]   : Optical absorption coefficient of water
  # μ_{a,f}   [1/mm]   : Optical absorption coefficient of fat
  # μ_{a,m}   [1/mm]   : Optical absorption coefficient of melanin
  mu_a = {'air': 0.}

  # Reduced scattering coefficient μ_s' [1/mm]
  mu_sp = {
    'wavelength_ref': 500, # Reference wavelength [nm]
    'ref': { # Reference reduced scattering coefficient [1/mm]
        'fat':       1.06,                              # [Cerussi]
        'dermis':    {'upper': 3.72,  'lower': 4.78},   # [Jacques, Simpson]
        'epidermis': 'dermis',
        'glandular': 0.83,
        'nipple':    'dermis',
        'ligament':  'fat',
        'tdlu':      'fat',
        'duct':      'fat',
        'artery':    {'upper': 2.2,   'lower': 2.295},  # [Alexandrakis, Bosschaart]
        'vein':      'artery',
        'vtc':       {'upper': 2.003, 'lower': 2.0676}, # [Cerussi, Peters]
        'nc':        'vtc'
      },
    'b': { # Scattering power
        'fat':       0.52,                              # [Cerussi]
        'dermis':    {'upper': 1.39,  'lower': 2.453},  # [Jacques, Simpson]
        'epidermis': 'dermis',
        'glandular': 0.617,
        'nipple':    'dermis',
        'ligament':  'fat',
        'tdlu':      'fat',
        'duct':      'fat',
        'artery':    {'upper': 0.66,  'lower': 0.872},  # [Alexandrakis, Bosschaart]
        'vein':      'artery',
        'vtc':       {'upper': 0.725, 'lower': 1.4865}, # [Cerussi, Peters]
        'nc':        'vtc'
      }
   }

  # Optical scattering coefficient μ_s [1/mm]
  # Eq. (2) [Park2023]
  #   μ_s(r, λ) = μ_s'(r, λ)/(1 − g(r))
  #             = μ_s'(r, λ_{ref})/(1 − g(r))*(λ/λ_{ref})^{−b(r)}
  mu_s = {'air': 0.}

  # Scattering anisotropy g
  g = {
    # 'water':      0.99,
    'fat':        0.98,     # [Peters]
    'dermis':     0.65,     # [Iorizzo]
    'epidermis':  'dermis',
    'glandular':  0.96,     # [Peters]
    'nipple':     'dermis',
    'ligament':   'fat',
    'tdlu':       'fat',
    'duct':       'fat',
    'artery':     0.976,    # [Meinke]
    'vein':       'artery',
    'vtc':        0.955,    # [Peters]
    'nc':         'vtc',
    'air':        1.
  }

  # Refractive index n
  n = {
    # 'water':      1.33,
    'fat':        1.44,     # [Bashkatov]
    'dermis':     1.37,     # [Ding]
    'epidermis':  'dermis',
    'glandular':  1.36,     # [Bashkatov]
    'nipple':     'dermis',
    'ligament':   'fat',
    'tdlu':       'fat',
    'duct':       'fat',
    'artery':     1.35,     # [Sydoruk]
    'vein':       'artery',
    'vtc':        1.39,     # [Zysk]
    'nc':         'vtc',
    'air':        1.
  }
