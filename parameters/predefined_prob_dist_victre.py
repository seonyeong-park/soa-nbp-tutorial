'''
───────────────────────────────────────────────────────────────────────────
Predefined probability distribution for VICTRE phantom generation
───────────────────────────────────────────────────────────────────────────
Author:   Seonyeong Park (sp33@illinois.edu)
Date:     June 20, 2023

This includes a class `VICTRE_param` to specify the shape and size 
parameters for VICTRE phantom generation. The breast volume extent 
parameters include `a_{1t}` (mm), `a_{1b}`, `a_{2l}`, `a_{2r}`, and `a_3`, 
and the breast shape parameters include `ϵ_1`, `B_0`, `B_1`, `H_0`, and 
`H_1`. 

  Table 2 Shape and size parameters [Park2023]
  ┌───────────────┬────────────────┬─────────────────┬─────────────────┐
  │ Parameter     │ Types A and B  │ Type C          │ Type D          │
  ├───────────────┼────────────────┴─────────────────┼─────────────────┤
  │ a_{1t} (mm)   │ TN(59.70, 3.58, 50.77, 71.5)     │ TN(50.05, 3.58, │
  │               │                                  │ 42.9, 57.2)     │
  ├───────────────┼──────────────────────────────────┴─────────────────┤
  │ a_{1b}/a_{1t} │ N(1, 0.02)                                         │
  ├───────────────┼────────────────────────────────────────────────────┤
  │ a_{2r}/a_{1t} │ N(1, 0.05)                                         │
  ├───────────────┼────────────────────────────────────────────────────┤
  │ a_{2l}/a_{2r} │ N(1, 0.05)                                         │
  ├───────────────┼────────────────┬─────────────────┬─────────────────┤
  │ a_3/a_{1t}    │ TN(0.85, 0.14, │ TN(0.85, 0.12,  │ TN(0.85, 0.1,   │
  │               │ 0.8, 1.2)      │ 0.7, 1.1)       │ 0.7, 1.1)       │
  ├───────────────┼────────────────┴─────────────────┴─────────────────┤
  │ ϵ_1           │ N(1, 0.1)                                          │
  ├───────────────┼────────────────────────────────────────────────────┤
  │ B_0           │ TN(0, 0.1, -0.18, 0.18)                            │
  ├───────────────┼────────────────────────────────────────────────────┤
  │ B_1           │ TN(0, 0.1, -0.18, 0.18)                            │
  ├───────────────┼────────────────────────────────────────────────────┤
  │ H_0           │ TN(0, 0.15, -0.11, 0.11)                           │
  ├───────────────┼────────────────────────────────────────────────────┤
  │ H_1           │ TN(0, 0.25, -0.3, 0.3)                             │
  └───────────────┴────────────────────────────────────────────────────┘  
  N(μ,σ): Gaussian distribution with mean μ and standard deviation σ.
  TN(μ,σ,a,b): truncated Gaussian distribution in interval (a,b).
  For hemispherical shapes (a_{1t}=a_{1b}=a_{2r}=a_{2l}=a_3), the ϵ_1 
  value is set to “1,” and the B_0, B_1, H_0, and H_1 values are set to 
  “0.”

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
class VICTRE_param:
  def __new__(self, breast_type: str, breast_shape: str) -> object:
    if breast_type[0] in ['A', 'B', 'C']:  # Types A, B, and C
      self.a1t = {'mean': 59.7025, 
                  'std':  3.5750, 
                  'min':  50.7650, 
                  'max':  71.5000} # [mm]
    elif breast_type[0] == 'D':            # Type D
      self.a1t = {'mean': 50.0500, 
                  'std':  3.5750, 
                  'min':  42.9000, 
                  'max':  57.2000} # [mm]
    
    if breast_shape == 'natural':
      self.a1b_a1t  = {'mean': 1, 'std': 0.02}
      self.a2r_a1t  = {'mean': 1, 'std': 0.05}
      self.a2l_a2r  = {'mean': 1, 'std': 0.05}
      if breast_type[0] in ['A', 'B']:     # Types A and B
        self.a3_a1t = {'mean':  0.85,
                       'std':   0.14,
                       'min':   0.8,
                       'max':   1.2}
      elif breast_type[0] == 'C':          # Type C
        self.a3_a1t = {'mean':  0.85,
                       'std':   0.12,
                       'min':   0.7,
                       'max':   1.1}
      elif breast_type[0] == 'D':          # Type D
        self.a3_a1t = {'mean': 0.85,
                       'std': 0.1,
                       'min': 0.7,
                       'max': 1.1}
      self.eps1       = {'mean': 1,     'std': 0.1}
      self.doPtosis   = 'true'
      self.ptosisB0   = {'mean': 0, 'std': 0.1,   'min': -0.18, 'max': 0.18}
      self.ptosisB1   = {'mean': 0, 'std': 0.1,   'min': -0.18, 'max': 0.18}
      self.doTurnTop  = 'true'
      self.turnTopH0  = {'mean': 0, 'std': 0.15,  'min': -0.11, 'max': 0.11}
      self.turnTopH1  = {'mean': 0, 'std': 0.25,  'min': -0.3,  'max': 0.3}
    elif breast_shape == 'hemisphere':
      self.a1b_a1t    = 1
      self.a1b_a1t    = 1
      self.a2r_a1t    = 1
      self.a2l_a2r    = 1
      self.a3_a1t     = 1
      self.eps1       = 1
      self.doPtosis   = 'false'
      self.ptosisB0   = 0
      self.ptosisB1   = 0
      self.doTurnTop  = 'false'
      self.turnTopH0  = 0
      self.turnTopH1  = 0
    
    return self
  