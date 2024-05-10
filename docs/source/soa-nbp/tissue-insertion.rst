Tissue insertion 
================

Blood vessels under skin
------------------------

The function :py:func:`tissue_insertion.InsertBloodVesselUnderSkin(config: object, labelmap: np.ndarray, sigma1=31, sigma2=49, sigma3=1.75) -> np.ndarray` inserts blood vessels under skin layer in the given tissue label map and returns the resulting map.

Two layer skin model
--------------------

The function :py:func:`tissue_insertion.InsertTwoLayerSkin(config: object, labelmap: np.ndarray) -> np.ndarray` inserts a two-layer skin model, consisting of dermis and epidermis layers, into the given tissue label map and returns the resulting map.

Lesion
------

The function :py:func:`tissue_insertion.InsertLesion(config: object, labelmap: np.ndarray, labelmap_pa: np.ndarray, lsn_type: str, choose_lsn_loc: bool, lsn_loc=[]) -> tuple`
