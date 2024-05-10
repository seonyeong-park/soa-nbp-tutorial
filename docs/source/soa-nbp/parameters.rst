Parameters
==========

Tissue types
------------

The class :py:class:`tissue_type.Tissue_type`

.. table:: Tissue type parameters

  +-----------------------------------+-------+
  | Tissue type                       | Label |
  +===================================+=======+
  | Background                        | 0     |
  +-----------------------------------+-------+
  | Fat                               | 1     |
  +-----------------------------------+-------+
  | Dermis (skin for one-layer model) | 2     |
  +-----------------------------------+-------+
  | Epidermis (optional)              | 3     |
  +-----------------------------------+-------+
  | Glandular                         | 29    |
  +-----------------------------------+-------+
  | Nipple                            | 33    |
  +-----------------------------------+-------+
  | Ligament                          | 88    |
  +-----------------------------------+-------+
  | Terminal duct lobular unit (TDLU) | 95    |
  +-----------------------------------+-------+
  | Duct                              | 125   |
  +-----------------------------------+-------+
  | Artery                            | 150   |
  +-----------------------------------+-------+
  | Vein                              | 225   |
  +-----------------------------------+-------+
  | Peripheral angiogenesis (PA)      | 190   |
  +-----------------------------------+-------+
  | Viable tumor cell                 | 200   |
  +-----------------------------------+-------+
  | Necrotic core                     | 210   |
  +-----------------------------------+-------+
  | Air                               | 255   |
  +-----------------------------------+-------+


Predefined probability distributions of VICTRE parameters
---------------------------------------------------------

The class :py:class:`predefined_prob_dist_victre.VICTRE_param`

.. table:: Shape and size parameters [Park2023]_.

  +-----------------------+--------------------------+----------------------------+----------------------------+
  | Paramter              | Types A and B            | Type C                     | Type D                     |
  +=======================+==========================+============================+============================+
  | :math:`a_{1t}` (mm)   | :math:`TN`\ (59.70, 3.58, 50.77, 71.5)                | | :math:`TN`\ (50.05, 3.58,|
  |                       |                                                       | | 42.9, 57.2)              |
  +-----------------------+-------------------------------------------------------+----------------------------+
  | :math:`a_{1b}/a_{1t}` | :math:`N`\ (1, 0.02)                                                               |
  +-----------------------+------------------------------------------------------------------------------------+
  | :math:`a_{2r}/a_{1t}` | :math:`N`\ (1, 0.05)                                                               |
  +-----------------------+------------------------------------------------------------------------------------+
  | :math:`a_{2l}/a_{1r}` | :math:`N`\ (1, 0.05)                                                               |
  +-----------------------+---------------------------+---------------------------+----------------------------+
  | :math:`a_{3}/a_{1t}`  | | :math:`TN`\ (0.85, 0.14,| | :math:`TN`\ (0.85, 0.12,| | :math:`TN`\ (0.85, 0.1,  |
  |                       | | 0.8, 1.2)               | | 0.7, 1.1)               | | 0.7, 1.1)                |
  +-----------------------+---------------------------+---------------------------+----------------------------+
  | :math:`\epsilon_{1}`  | :math:`N`\ (1, 0.1)                                                                |
  +-----------------------+------------------------------------------------------------------------------------+
  | :math:`B_{0}`         | :math:`TN`\ (0, 0.1, -0.18, 0.18)                                                  |
  +-----------------------+------------------------------------------------------------------------------------+
  | :math:`B_{1}`         | :math:`TN`\ (0, 0.1, -0.18, 0.18)                                                  |
  +-----------------------+------------------------------------------------------------------------------------+
  | :math:`H_{0}`         | :math:`TN`\ (0, 0.15, -0.11, 0.11)                                                 |
  +-----------------------+------------------------------------------------------------------------------------+
  | :math:`H_{1}`         | :math:`TN`\ (0, 0.25, -0.3, 0.3)                                                   |
  +-----------------------+------------------------------------------------------------------------------------+

:math:`N(\mu,\sigma)`: Gaussian distribution with mean :math:`\mu` and standard deviation :math:`\sigma`.
:math:`TN(\mu,\sigma,a,b)`: truncated Gaussian distribution in interval :math:`(a,b)`.
For hemispherical shapes (:math:`a_{1t}=a_{1b}=a_{2r}=a_{2l}=a_{3}`), the :math:`\epsilon_{1}` value is set to '1,' and the :math:`B_{0}`, :math:`B_{1}`, :math:`H_{0}`, and :math:`H_{1}` values are set to '0.'


Predefined probability distributions of functional properties
-------------------------------------------------------------

The class :py:class:`predefined_prob_dist_func.Func_prop`

.. table:: Functional properties of breast tissues and lesion [Park2023]_.

  +------------+----------------------+---------------------+----------------------+---------------------------+---------------------+
  | Medium     |:math:`s` (%)         |:math:`f_b` (%)      |:math:`f_w` (%)       |:math:`f_f` (%)            |:math:`f_m` (%)      |
  +============+======================+=====================+======================+===========================+=====================+
  | | Fat/     | PDE\ :sup:`a`        | | :math:`TN`\ (1.15,| | :math:`TN`\ (29.17,| | 100 -                   | 0                   |
  | | ligament/|                      | | 0.22,             | | 13.11,             | | ( :math:`f_ {b,fat}`    |                     |
  | | TDLU/duct|                      | | 0.91,             | | 14, 20)            | | + :math:`f_{w,fat}` )   |                     |
  |            |                      | | 1.43)             |                      |                           |                     |
  +------------+----------------------+---------------------+----------------------+---------------------------+---------------------+
  | Glandular  | PDE\ :sup:`a`        |:math:`f_{b,fat}`    |:math:`f_{w,fat}`     | 0                         | 0                   |
  +------------+----------------------+---------------------+----------------------+---------------------------+---------------------+
  | Skin       | 98.9                 | 0.39                | | :math:`TN`\ (18.68,| | :math:`TN`\ (30.72,     | | :math:`TN`\ (0.64,|
  |            |                      |                     | | 1.34, 12,          | | 3.79, 12,               | | 0.04,             |
  |            |                      |                     | | 25)                | | 48)                     | | 0.44,             |
  |            |                      |                     |                      |                           | | 0.84)             |
  +------------+----------------------+---------------------+----------------------+---------------------------+---------------------+
  | Nipple     | 71.28                | 1.35                | | :math:`TN`\ (45.4, | | 100 -                   | | :math:`TN`\ (0.82,|
  |            |                      |                     | | 11.7,              | | ( :math:`f_{b,nipple}`  | | 0.09,             |
  |            |                      |                     | | 25.1,              | | + :math:`f_{w,nipple}`  | | 0.4,              |
  |            |                      |                     | | 76.6)              | | + :math:`f_{m,nipple}` )| | 1.24)             |
  +------------+----------------------+---------------------+----------------------+---------------------------+---------------------+
  | Artery     |:math:`U`\ (95, 99)   | 100                 | 0                    | 0                         | 0                   |
  +------------+----------------------+---------------------+----------------------+---------------------------+---------------------+
  | Vein       |:math:`U`\ (75, 84)   |:math:`f_{b,artery}` | 0                    | 0                         | 0                   |
  +------------+----------------------+---------------------+----------------------+---------------------------+---------------------+
  | VTC        | | :math:`TN`\ (69.91,| | :math:`TN`\ (1.64,| | :math:`TN`\ (47.67,| | 100 -                   | 0                   |
  |            | | 4.99,              | | 0.6,              | | 20.15,             | | ( :math:`f_{b,VTC}`     |                     |
  |            | | 62.5,              | | 0.89,             | | 24.14,             | | + :math:`f_{w,VTC}` )   |                     |
  |            | | 76.49)             | | 2.93)             | | 82.25)             |                           |                     |
  +------------+----------------------+---------------------+----------------------+---------------------------+---------------------+
  | Necrotic   |:math:`s_{VTC}`       | 0                   |:math:`f_{w,VTC}`     |:math:`f_{f,VTC}`          | 0                   |
  | core       |                      |                     |                      |                           |                     |
  +------------+----------------------+---------------------+----------------------+---------------------------+---------------------+
  | PA         | PDE\ :sup:`a`        | PDE\ :sup:`a`       |:math:`f_{w,VTC}`     |:math:`f_{f,VTC}`          | 0                   |
  +------------+----------------------+---------------------+----------------------+---------------------------+---------------------+
:sup:`a` The PDE formulation creates a smooth transition for the tissue property distribution.


Predefined probability distributions of optical properties
----------------------------------------------------------

The class :py:class:`predefined_prob_dist_opt.Opt_prop`

.. table:: Scattering coefficient parameters, scattering anisotropy, and refractive index of breast tissues and lesion [Park2023]_.

  +------------------------+---------------------------------------------+----------------+---------+---------+
  | Medium                 |:math:`\mu_s'(\lambda_{ref})` (mm\ :sup:`-1`)|:math:`b`       |:math:`g`|:math:`n`|
  +========================+=============================================+================+=========+=========+
  | Fat/ligament/TDLU/duct | 1.06                                        | 0.52           | 0.98    | 1.44    |
  +------------------------+---------------------------------------------+----------------+---------+---------+
  | Glandular              | 0.83                                        | 0.617          | 0.96    | 1.36    |
  +------------------------+---------------------------------------------+----------------+---------+---------+
  | Skin/nipple            | (3.72, 4.78)                                | (1.39, 2.453)  | 0.65    | 1.37    |
  +------------------------+---------------------------------------------+----------------+---------+---------+
  | Artery/vein            | (2.2, 2.295)                                | (0.66, 0.872)  | 0.976   | 1.35    |
  +------------------------+---------------------------------------------+----------------+---------+---------+
  | VTC/necrotic core      | (2, 2.07)                                   | (0.725, 1.487) | 0.955   | 1.39    |
  +------------------------+---------------------------------------------+----------------+---------+---------+
A reference wavelength (\ :math:`\lambda_{ref}`) is 500 nm.


Predefined probability distributions of acoustic properties
-----------------------------------------------------------

The class :py:class:`predefined_prob_dist_acou.Acou_prop`

.. table:: Acoustic properties of breast tissues and lesion [Park2023]_.

  +----------------+-------------------------------+-----------------------------------+-----------------------------------------+
  | Medium         |:math:`c` (mm/\ :math:`\mu`\ s)|:math:`\rho` (g/mm\ :sup:`3`)      |:math:`\alpha_{0}` (dB/MHz\ :sup:`y`\ mm)|
  +================+===============================+===================================+=========================================+
  | Water\ :sup:`a`| 1.521                         |0.993 :math:`\times` 10\ :sup:`-3}`|2.2 :math:`\times` 10\ :sup:`-4`         |
  +----------------+-------------------------------+-----------------------------------+-----------------------------------------+
  | Fat            | | :math:`TN`\ (1.44, 0.021,   | | :math:`TN`\ (0.911, 0.053,      |:math:`N`\ (0.038, 0.004)                |
  |                | | 1.41, 1.49)                 | | 0.812, 0.961) :math:`\times`    |                                         |
  |                |                               | | 10\ :sup:`-3`                   |                                         |
  +----------------+-------------------------------+-----------------------------------+-----------------------------------------+
  | | Glandular/   | | :math:`TN`\ (1.54, 0.015,   | | :math:`TN`\ (1.041, 0.045,      |:math:`N`\ (0.075, 0.008)                |
  | | TDLU/duct    | | 1.517, 1.567)               | | 0.99, 1.092) :math:`\times`     |                                         |
  |                |                               | | 10\ :sup:`-3`                   |                                         |
  +----------------+-------------------------------+-----------------------------------+-----------------------------------------+
  | Ligament       | | :math:`TN`\ (1.457, 0.019,  | | :math:`TN`\ (1.142, 0.045,      |:math:`N`\ (0.126, 0.013)                |
  |                | | 1.422, 1.496)               | | 1.1, 1.175) :math:`\times`      |                                         |
  |                |                               | | 10\ :sup:`-3`                   |                                         |
  +----------------+-------------------------------+-----------------------------------+-----------------------------------------+
  | Skin/nipple    | | :math:`TN`\ (1.555, 0.01,   | | :math:`TN`\ (1.109, 0.014,      |:math:`N`\ (0.184, 0.019)                |
  |                | | 1.53, 1.58)                 | | 1.1, 1.125) :math:`\times`      |                                         |
  |                |                               | | 10\ :sup:`-3`                   |                                         |
  +----------------+-------------------------------+-----------------------------------+-----------------------------------------+
  | Artery/vein    | | :math:`TN`\ (1.578, 0.011,  | | :math:`TN`\ (1.05, 0.017,       | 0.021                                   |
  |                | | 1.559, 1.59)                | | 1.025, 1.06) :math:`\times`     |                                         |
  |                |                               | | 10\ :sup:`-3`                   |                                         |
  +----------------+-------------------------------+-----------------------------------+-----------------------------------------+
  | | VTC/necrotic | | :math:`TN`\ (1.548, 0.01,   | | :math:`TN`\ (0.945, 0.02,       |:math:`N`\ (0.269, 0.02)                 |
  | | core         | | 1.531, 1.565)               | | 0.911, 0.999) :math:`\times`    |                                         |
  |                |                               | | 10\ :sup:`-3`                   |                                         |
  +----------------+-------------------------------+-----------------------------------+-----------------------------------------+
:sup:`a` Acoustic properties of water are consistent with an assumed temperature of 37\ :math:`^{\circ}`\ C, which is often used in breast OAT to minimize patient discomfort.


.. [Park2023] Seonyeong Park, Umberto Villa, Fu Li, Refik Mert Cam, Alexander A. Oraevsky, Mark A. Anastasio, "Stochastic three-dimensional numerical phantoms to enable computational studies in quantitative optoacoustic computed tomography of breast cancer," *J. Biomed. Opt.* 28(6) 066002 (20 June 2023) https://doi.org/10.1117/1.JBO.28.6.066002

.. [Park2020] Seonyeong Park, Umberto Villa, Richard Su, Alexander Oraevsky, Frank J. Brooks, Mark A. Anastasio, "Realistic three-dimensional optoacoustic tomography imaging trials using the VICTRE breast phantom of FDA (Conference Presentation)," *Proc. SPIE 11240, Photons Plus Ultrasound: Imaging and Sensing 2020*, 112401H (6 March 2020) https://doi.org/10.1117/12.2552380          

.. [ETB] The Engineering ToolBox, "Water - speed of sound vs. temperature," https://www.engineeringtoolbox.com/sound-speed-water-d_598.html (2004)

.. [Hasgall] P A Hasgall et al., "IT'IS database for thermal and electromagnetic parameters of biological tissues," https://www.itis.swiss/database (2018)

.. [Malik] Bilal Malik et al., "Objective breast tissue image classification using quantitative transmission ultrasound tomography," *Sci. Rep.*, 6 1-8 SRCEC3 2045-2322 (2016)

.. [Klock] John C Klock et al., "Anatomy-correlated breast imaging and visual grading analysis using quantitative transmission ultrasound\ :sup:`TM`\ ," *Int. J. Biomed. Imaging*, 2016 1-9 https://doi.org/10.1038/srep38857 (2016)

.. [Li2009] Cuiping Li et al., "In vivo breast sound-speed imaging with ultrasound tomography," *Ultrasound Med. Biol.*, 35 1615-1628 https://doi.org/10.1016/j.ultrasmedbio.2009.05.011 USMBA3 0301-5629 (2009)

.. [Sanchez] Amy Sanchez, Chris Mills and Joanna Scurr, "Estimating breast mass-density: a retrospective analysis of radiological data," *Breast J.*, 23 237-239 https://doi.org/10.1111/tbj.12725 BRJOFK 1075-122X (2017)

.. [André] Michael André, James Wiskin and David Borup, Clinical Results with Ultrasound Computed Tomography of the Breast, 395-432 Springer Netherlands, Dordrecht (2013)

.. [Li2022] Fu Li et al., "3-D stochastic numerical breast phantoms for enabling virtual imaging trials of ultrasound computed tomography," *IEEE Trans. Ultrason. Ferroelectr. Freq. Control*, 69, 135-146 https://doi.org/10.1109/TUFFC.2021.3112544 ITUCER 0885-3010 (2022)
