'''
Author:   Seonyeong Park (sp33@illinois.edu)
Date:     June 20, 2023

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

Copyright (C) 2024 Seonyeong Park and Mark Anastasio
          Computational Imaging Science Laboratory
          (https://anastasio.bioengineering.illinois.edu/)
          Department of Bioengineering,
          University of Illinois Urbana-Champaign
          GitHub: https://github.com/comp-imaging-sci/soa-nbp

License : GNU General Public License version 3, Please see 'LICENSE' for 
          details.
'''
from .tissue_type                 import  Tissue_type
from .predefined_prob_dist_victre import  VICTRE_param
from .predefined_prob_dist_func   import  Func_prop
from .predefined_prob_dist_opt    import  Opt_prop
from .predefined_prob_dist_acou   import  Acou_prop
