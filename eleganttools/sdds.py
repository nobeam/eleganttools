from typing import Tuple
from sdds import SDDS  # https://aps.anl.gov/Accelerator-Operations-Physics/Software
import numpy as np


def as_dict(path) -> dict:
    """Convert a self describing data set (SDDS) to a dictionary.

    :param path: Path to SDDS file.
    :type path: str
    :return: SDDS as dict
    :rtype: dict
    """
    sdds = SDDS(0)
    sdds.load(path)
    parameter_data = [c[0] for c in sdds.parameterData]
    column_data = [np.squeeze(col) for col in sdds.columnData]
    return dict(zip(sdds.parameterName + sdds.columnName, parameter_data + column_data))


def as_dataframe(path) -> "pandas.DataFrame":
    """Convert the columns of a self describing data set (SDDS) to a pandas dataframe.

    :param path: Path to SDDS file.
    :type path: str
    :return: SDDS as pandas dataframe
    :rtype: pandas.DataFrame
    """
    import pandas as pd

    return pd.DataFrame.from_dict(as_dict(path))
