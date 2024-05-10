'''
───────────────────────────────────────────────────────────────────────────
Tissue type
───────────────────────────────────────────────────────────────────────────
Author:   Seonyeong Park (sp33@illinois.edu)
Date:     June 20, 2023

This includes a class `Tissue_type` to specify the considered tissue types,
along with their corresponding unsigned 8-bit integer labels ranging from 0
to 255.

  ┌───────────────────────────────────┬───────┐
  │ Tissue type                       │ Label │
  ├───────────────────────────────────┼───────┤
  │ Background                        │ 0     │
  │ Fat                               │ 1     │
  │ Dermis (skin for one-layer model) │ 2     │
  │ Epidermis (optional)              │ 3     │
  │ Glandular                         │ 29    │
  │ Nipple                            │ 33    │
  │ Ligament                          │ 88    │
  │ Terminal duct lobular unit (TDLU) │ 95    │
  │ Duct                              │ 125   │
  │ Artery                            │ 150   │
  │ Vein                              │ 225   │
  │ Peripheral angiogenesis           │ 190   │
  │ Viable tumor cell                 │ 200   │
  │ Necrotic core                     │ 210   │
  │ Air                               │ 255   │
  └───────────────────────────────────┴───────┘  

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
  [Badano] A. Badano et al., "Evaluation of digital breast tomosynthesis as
          replacement of full-field digital mammography using an in silico 
          imaging trial," JAMA Network Open, 1 e185474 
          https://doi.org/10.1001/jamanetworkopen.2018.5474 (2018)
  [VICTRE] VICTRE breast phantom, 
          https://breastphantom.readthedocs.io/en/latest/
            
Copyright (C) 2024 Seonyeong Park and Mark Anastasio
          Computational Imaging Science Laboratory
          (https://anastasio.bioengineering.illinois.edu/)
          Department of Bioengineering,
          University of Illinois Urbana-Champaign
          GitHub: https://github.com/comp-imaging-sci/soa-nbp

License : GNU General Public License version 3, Please see 'LICENSE' for 
          details.
'''
class Tissue_type:
  water         = 0
  fat           = 1
  dermis        = 2
  epidermis     = 3   # Epidermis-included layer for two-layer skin model
  glandular     = 29
  nipple        = 33
  muscle        = 40
  ligament      = 88
  tdlu          = 95  # Terminal Duct Lobular Unit
  duct          = 125
  artery        = 150
  vein          = 225
  pa            = 190 # Peripheral Angiogenesis
  vtc           = 200 # Viable Tumor Cell
  nc            = 210 # Necrotic Core
  calcification = 250
  air           = 255
