from . import sddspython  # https://aps.anl.gov/Accelerator-Operations-Physics/Software


class SDDS(sddspython.SDDS):
    """Extends sddspython.SDDS to make exporting as dict/dataframe more convenient.

    :param path: Path to the SDDS file.
    :type path: str or path-like
    :param int index: Index passed to the sddspython.SDDS base class.
    """

    def __init__(self, path, index=0):
        super().__init__(index)
        self.load(str(path))

    def as_dict(self) -> dict:
        """Convert the self describing data set (SDDS) to a dictionary.

        :return: SDDS as dict
        :rtype: dict
        """
        import numpy as np

        parameters = [c[0] for c in self.parameterData]
        columns = [np.squeeze(col) for col in self.columnData]
        return dict(zip(self.parameterName + self.columnName, parameters + columns))

    def as_dataframe(self) -> "pandas.DataFrame":
        """Convert the self describing data set (SDDS) to a pandas dataframe.

        :return: SDDS as pandas dataframe
        :rtype: pandas.DataFrame
        """
        import pandas as pd

        return pd.DataFrame.from_dict(self.as_dict())
