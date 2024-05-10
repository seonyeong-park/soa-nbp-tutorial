Utils
==================

- The class :py:class:`Load` loads data as a numpy array or a dictionary from a file in `.mat`, `.raw`, or `.raw.gz`` file format and returns it.
- The class :py:class:`Save` saves a dictionary as a `MAT-file`.
- The class :py:class:`Metadata` adds corresponding meta data to the given dictionary where anatomical, functional, optical, or acoustic numerical breast phantom is stored, and then it returns the updated dictionary.
- The function :py:func:`ExtendDomain` extends a domain of the given tissue label map according to the domain dimensions specified in configuration by padding and returns the map in the extended domain.
- The function :py:func:`ExcludeMuscle` crops out the muscle region outside the ROI in the given tissue label map and returns the cropped map.
- The function :py:func:`Standing2Prone` rotates the given tissue label map in a standing position to be consistent with a prone position during a 3D OAT scan and returns the map. Lesion locations specified in configuration are updated accordingly.
- The function :py:func:`GenerateSphereElement` generates and returns a sphere element. In this map, a value of `True` is assigned to voxels within a voxel distance equals to the given value from the center location of the map.
- The function :py:func:`SampleVal` samples a property value from the given predefined probability distribution using the given seed number and returns the sampled property value. The predefined probability distribution is either a truncated Gaussian, Gaussian, or uniform distribution.
- The function :py:func:`SampleFuncProp` samples values of the functional properties, including total hemoglobin concentration of blood, oxygen saturation, and volume fractions of blood, water, fat, and melanosome, for each tissue type. The sampled values are returned as a dictionary. 
- The function :py:func:`SampleOptProp` jointly samples values of the reduced scattering coefficient at a reference wavelength and scattering power and individually samples the optical properties, scattering anisotropy and referactive index, for each tissue type. The sampled values are returned as a dictionary. 
- The function :py:func:`SampleAcouProp` samples values of the acoustic properties, including sound speed, density, acoustic attenuation coefficient, and power-law exponent, for each tissue type. The sampled values are returned as a dictionary. 
- The function :py:func:`AssignProp` assigns a property value to each tissue type, based on the given tissue label map and property dictionary, and returns the assigned property map.
- The function :py:func:`CalculateMuA` calculates an optical absorption coefficient map based on the given constant values, wavelength, and functional NBPs (Equation (1) in [Park2023]_ ). The resulting map is retunred.
- The function :py:func:`CalculateMuS` calculates an optical scattering coefficient map based on the given optical properties, wavelength, and anatomical NBP (Equation (2) in [Park2023]_ ). The resulting map is returned.

.. [Park2023] Seonyeong Park, Umberto Villa, Fu Li, Refik Mert Cam, Alexander A. Oraevsky, Mark A. Anastasio, "Stochastic three-dimensional numerical phantoms to enable computational studies in quantitative optoacoustic computed tomography of breast cancer," *J. Biomed. Opt.* 28(6) 066002 (20 June 2023) https://doi.org/10.1117/1.JBO.28.6.066002
