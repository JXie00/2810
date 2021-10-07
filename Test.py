import unittest
from Database.DB import *
from dateRegex import dateValidation

class TestMyDb(unittest.TestCase):
    def test_fetchInitialData_correct(self):
        self.assertIsNotNone(fetchInitData("OBJECTID"))

    def test_hourlyAverageAccident_valid(self):
        self.assertIsNotNone(hourlyAverageAccident("2013/2/2","2014/2/3"))

    def test_hourlyAverageAccident_invalid(self):
        self.assertEqual(hourlyAverageAccident("2010/2/2","2010/2/3"),[])

    def test_getDataByDate_valid(self):
        self.assertIsNotNone(getDataByDate("2013/2/2","2014/2/3"))

    def test_getDataByDate_invalid(self):
        self.assertEqual(getDataByDate("2010/2/2","2010/2/3"),[])

    def test_getDataByType_default(self):
        self.assertIsNotNone(getDataByType("2013/2/2","2014/2/3"))

    def test_getDataByType_option(self):
        self.assertIsNotNone(getDataByType("2013/2/2","2014/2/3","Struck Pedestrian"))

    def test_getDataByType_invalid(self):
        self.assertEqual(getDataByType("1999/2/2","2000/2/3"),[])

    def test_alcoholImpact(self):
        self.assertIsNotNone(alcoholImpact())

    def test_LGARate(self):
        self.assertIsNotNone(LGARate())

    def test_getAccidentType(self):
        self.assertIsNotNone(getAccidentType())

    def test_getColumnNames(self):
        self.assertIsNotNone(getColumnNames())

    def test_dateValidation_valid(self):
        self.assertEqual(dateValidation("2012/2/3"),True)

    def test_dateValidation_invalid(self):
        self.assertEqual(dateValidation("12/3/1232"),False)



unittest.main()
