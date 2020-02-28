from typing import Tuple
import numpy as np
import sdds as _sdds  # https://aps.anl.gov/Accelerator-Operations-Physics/Software


def as_dict(path) -> dict:
    """Convert a self describing data set (SDDS) to a dictionary.

    :param path: Path to SDDS file.
    :type path: str
    :return: SDDS as dict
    :rtype: dict
    """
    data = _sdds.SDDS(0)
    data.load(path)
    parameters = dict(zip(data.parameterName, data.parameterData))
    columns = dict(zip(data.columnName, data.columnData)) if data.columnData else {}
    return dict(parameters=parameters, columns=columns)


def columns_as_array(path) -> np.ndarray:
    """Convert the columns of a self describing data set (SDDS) to a numpy ndarray.

    :param path: Path to SDDS file.
    :type path: str
    :return: SDDS as numpy ndarray
    :rtype: numpy.ndarray
    """
    data = _sdds.SDDS(0)
    data.load(path)
    breakpoint()
    return np.array(data.columnData)
