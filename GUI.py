import wx
import sys
import matplotlib.pyplot as plt
import numpy as np
import wx.grid as grid
from Database.DB import *
import pandas as pd
import wx.grid as gridlib
# from dateRegex import dateValidation

wholedata = fetchInitData("OBJECTID")
alochol = alcoholImpact()
data3 = LGARate()


LGAData = LGARate()
LGANumber = []
LGAName= []
for i in LGAData:
    LGANumber.append(i[0])
    LGAName.append(i[1])


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(1000, 400))

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):

    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        panel = wx.Panel(self,-1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)




        requirement1 = wx.Button(panel, wx.ID_ANY, 'Show data', size=(40, 30))
        requirement2 = wx.Button(panel, wx.ID_ANY, 'accidents of the day', size=(40, 30))
        requirement3 = wx.Button(panel, wx.ID_ANY, 'accident of different type', size=(40, 30))
        requirement4 = wx.Button(panel, wx.ID_ANY, 'alcohol', size=(40, 30))
        requirement5 = wx.Button(panel, wx.ID_ANY, ' LAG Rate', size=(40, 30))
        reset = wx.Button(panel, wx.ID_ANY, 'reset', size=(40, 30))


        self.Bind(wx.EVT_BUTTON, self.req1, id=requirement1.GetId())
        self.Bind(wx.EVT_BUTTON, self.req2, id=requirement2.GetId())
        self.Bind(wx.EVT_BUTTON, self.req3, id=requirement3.GetId())
        self.Bind(wx.EVT_BUTTON, self.req4, id=requirement4.GetId())
        self.Bind(wx.EVT_BUTTON, self.req5, id=requirement5.GetId())
        self.Bind(wx.EVT_BUTTON, self.reset, id=reset.GetId())



        panel.SetSizer(hbox)
        hbox.Add((10, 70))  ## set the position

        hbox.Add(requirement1, 3, wx.TOP, 2)  ##Box.Add(control, proportion, flag, border)
        hbox.Add(requirement2, 3, wx.TOP, 2)
        hbox.Add(requirement3, 3, wx.TOP, 2)
        hbox.Add(requirement4, 3, wx.TOP, 2)
        hbox.Add(requirement5, 3, wx.TOP, 2)
        hbox.Add(reset, 3, wx.TOP, 2)


         ##White Board
        vbox.Add(panel, 0.05, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 10)  ##Box.Add(control, proportion, flag, border)
        self.box = wx.ListBox(self)

        vbox.Add(self.box, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)  # white board size
        self.SetSizer(vbox)

        self.list = wx.ListCtrl(self.box, size=(10000000, 100000000), style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'OBJECTID', width=100)
        self.list.InsertColumn(1, 'ACCIDENT_NO', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(2, 'ABS_CODE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(3, 'ACCIDENT_STATUS', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(4, 'ACCIDENT_DATE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(5, 'ACCIDENT_TIME', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(6, 'ALCOHOLTIME', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(7, 'ACCIDENT_TYPE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(8, 'DAY_OF_WEEK', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(9, 'DCA_CODE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(10, 'HIT_RUN_FLAG', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(11, 'LIGHT_CONDITION', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(12, 'POLICE_ATTEND', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(13, 'ROAD_GEOMETRY', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(14, 'SEVERITY', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(15, 'SPEED_ZONE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(16, 'RUN_OFFROAD', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(17, 'NODE_ID', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(18, 'LONGITUDE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(19, 'LATITUDE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(20, 'NODE_TYPE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(21, 'LGA_NAME', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(22, 'REGION_NAME', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(23, 'VICGRID_X', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(24, 'VICGRID_Y', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(25, 'TOTAL_PERSONS', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(26, 'INJ_OR_FATAL', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(27, 'FATALITY', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(28, 'SERIOUSINJURY', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(29, 'OTHERINJURY', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(30, 'NONINJURED', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(31, 'MALES', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(32, 'FEMALES', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(33, 'BICYCLIST', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(34, 'PASSENGER', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(35, 'DRIVER', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(36, 'PEDESTRIAN', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(37, 'PILLION', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(38, 'MOTORIST', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(39, 'UNKNOWN', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(40, 'PED_CYCLIST_5_12', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(41, 'PED_CYCLIST_13_18', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(42, 'OLD_PEDESTRIAN', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(43, 'OLD_DRIVER', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(44, 'YOUNG_DRIVER', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(45, 'ALCOHOL_RELATED', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(46, 'UNLICENCSED', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(47, 'NO_OF_VEHICLES', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(48, 'HEAVYVEHICLE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(49, 'PASSENGERVEHICLE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(50, 'MOTORCYCLE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(51, 'PUBLICVEHICLE', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(52, 'DEG_URBAN_NAME', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(53, 'DEG_URBAN_ALL', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(54, 'LGA_NAME_ALL', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(55, 'REGION_NAME_ALL', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(56, 'SRNS', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(57, 'SRNS_ALL', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(58, 'RMA', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(59, 'RMA_ALL', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(60, 'DIVIDED', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(61, 'DIVIDED_ALL', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(62, 'STAT_DIV_NAME', wx.LIST_FORMAT_RIGHT, 100)




    def req1(self, event):
        input1 = wx.GetTextFromUser('Input the year:', 'From')
        input2 = wx.GetTextFromUser('Input the year:', 'to')
        data2 = getDataByDate(input1, input2)
        for result in data2:
            self.list.Append(result)



    def req2(self, event):
        input1 = wx.GetTextFromUser('Input the year:', 'From')
        input2 = wx.GetTextFromUser('Input the year:', 'to')
        data5 = hourlyAverageAccident(input1, input2)
        accTimes = []
        time = []
        for i in data5:
            accTimes.append(i[0])
            time.append(i[1])
        plt.plot(time, accTimes)
        plt.xlabel("Number of accident")
        plt.ylabel("Time")
        plt.title("the number of accidents in each hour of the day")
        plt.show()




    def req3(self, event):
        input1 = wx.GetTextFromUser('Input the year:', 'From')
        input2 = wx.GetTextFromUser('Input the year:', 'to')
        input3 = wx.GetTextFromUser('Input the Type:', 'What type you looking for?')
        data3 =getDataByType(input1, input2, input3)
        for i in data3:
            self.list.Append(i)



    def req4(self, event):
        y = np.array([1 - alochol, alochol])
        mylabels = ["alcohol", "other"]
        plt.pie(y, labels=mylabels)
        plt.legend(title="Accident")
        plt.show()




    def req5(self, event):
        self.list.InsertColumn(0, 'Times', wx.LIST_FORMAT_RIGHT, 100)
        self.list.InsertColumn(1, 'Location', wx.LIST_FORMAT_RIGHT, 100)
        for i in LGAData:
            self.list.Append(i)



    def reset(self, event):
        self.Destroy()
        app = MyApp()
        app.MainLoop()



class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Victoria")
        self.frame.Show()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()