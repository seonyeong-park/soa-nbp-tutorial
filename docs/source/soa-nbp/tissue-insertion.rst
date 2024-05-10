Tissue insertion 
================

Blood vessels under skin
------------------------

The function :py:func:`tissue_insertion.InsertBloodVesselUnderSkin(config: object, labelmap: np.ndarray, sigma1=31, sigma2=49, sigma3=1.75) -> np.ndarray` inserts blood vessels under skin layer in the given tissue label map and returns the resulting map.

.. image:: https://www.spiedigitallibrary.org/ContentImages/Journals/JBOPFO/28/6/066002/WebImages/JBO_28_6_066002_f002.png
   :width: 400
   :alt: Blood vessels in NBP
   :align: center

.. Blood vessels in an NBP (type B, left breast) with (a and d) and without (b and e) blood vasculature customization and (c) a clinical OAT image acquired by TomoWave Laboratories employing LOUISA-3D3 at the MD Anderson Cancer Center and postprocessed to extract blood vascular structures.33 Paraview40 was used for volume rendering.

Two layer skin model
--------------------

The function :py:func:`tissue_insertion.InsertTwoLayerSkin(config: object, labelmap: np.ndarray) -> np.ndarray` inserts a two-layer skin model, consisting of dermis and epidermis layers, into the given tissue label map and returns the resulting map.

Lesion
------

The function :py:func:`tissue_insertion.InsertLesion(config: object, labelmap: np.ndarray, labelmap_pa: np.ndarray, lsn_type: str, choose_lsn_loc: bool, lsn_loc=[]) -> tuple`

.. image:: https://www.spiedigitallibrary.org/ContentImages/Journals/JBOPFO/28/6/066002/WebImages/JBO_28_6_066002_f003.png
   :width: 400
   :alt: Malignant lesion model
   :align: center

.. Malignant lesion model: (a) anatomical NLPs without (top) and with a necrotic core and a peripheral angiogenesis region (bottom), and distributions of (b) oxygen saturation s and (c) blood volume fraction fb. The two lesions were inserted at physiologically plausible locations randomly selected among the candidate sites produced by the VICTRE tools. In panels (a)–(c), halves of the lesion volumes are presented to show their cross-sections. In panels (b) and (c), the partial breast volumes clipped at the y-coordinate at which both lesions are exhibited are illustrated. The arrows in panel (b) indicate the simulated tumor hypoxia and those in panel (c) indicate the simulated tumor angiogenesis, necrotic tumor core, and relatively high total hemoglobin concentration of the viable tumor cells compared with healthy tissues. These are from a type A breast. Paraview40 was used for volume rendering, and color maps were adjusted for better visibility.

