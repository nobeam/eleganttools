import sdds
import numpy as np


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class SDDSad(sdds.SDDS):
    """
    some additions
    """

    def load(self, input):
        sdds.SDDS.load(self, input)
        self.parameterData = AttrDict(dict(zip(self.parameterName, self.parameterData)))
        if self.columnData:
            if len(self.columnData[0]) == 1:  # if only 1 page
                self.columnDataDict = AttrDict(
                    dict(zip(self.columnName, np.array(self.columnData)[:, 0]))
                )
            # what is the use case of this?
            # elif len(self.columnData[0]) == 2: # if only 2 pages
            #     self.columnDataDict = AttrDict(dict(zip(self.columnName, np.array(self.columnData)[:,1])))
            else:
                print("many pages..")
                self.columnDataDict = AttrDict(
                    dict(zip(self.columnName, self.columnData))
                )

    # everything seems to fail if particles are lost..
    # def flattenPages(self):
    #     #self.columnDataDict = AttrDict(dict(zip(self.columnName, np.array(self.columnData)[:,1])))
    #     for i in range(len(self.columnName)):
    #         for k in range(len(self.columnDataDict[self.columnName[i]])):
    #             #print i,k,np.array(self.columnDataDict[self.columnName[i]][k]).ravel().shape

    #             self.columnDataDict[self.columnName[i]] = np.vstack([np.array(self.columnDataDict[self.columnName[i]][k][:]).flatten() for k in range(len(self.columnDataDict[self.columnName[i]]))]).flatten()

    def flatten(self):
        for i in range(len(self.columnName)):
            self.columnDataDict[self.columnName[i]] = np.hstack(
                self.columnDataDict[self.columnName[i]]
            )

    def selectParticle(self, PID):
        for i in range(len(self.columnName)):
            # for bunch use a selection ....
            self.columnDataDict[self.columnName[i]] = np.array(
                self.columnDataDict[self.columnName[i]]
            )[:, PID - 1]
            # self.columnDataDict[self.columnName[i]] = [np.array(self.columnDataDict[self.columnName[i]][k][PID-1]) for k in range(len(self.columnDataDict[self.columnName[i]]))]
