import unittest
from Database.DB import *


class TestFunc(unittest.TestCase):
    def test_fetchInitialData_valid(self):
        self.assertIsNotNone(fetchInitData("OBJECTID"))

    def test_hourlyAverageAccident_valid(self):
        self.assertIsNotNone(hourlyAverageAccident("2013/2/2", "2014/2/3"))

    def test_hourlyAverageAccident_invalid(self):
        self.assertEqual(hourlyAverageAccident("2010/2/2", "2010/2/3"), [])

    def test_getDataByDate_valid(self):
        self.assertIsNotNone(getDataByDate("2013/2/2", "2014/2/3"))

    def test_getDataByDate_invalid(self):
        self.assertEqual(getDataByDate("2010/2/2", "2010/2/3"), [])

    def test_getDataByType_default(self):
        self.assertIsNotNone(getDataByType("2013/2/2", "2014/2/3"))

    def test_getDataByType_option(self):
        self.assertIsNotNone(getDataByType("2013/2/2", "2014/2/3", "Struck Pedestrian"))

    def test_getDataByType_invalidDate(self):
        self.assertEqual(getDataByType("1999/2/2", "2000/2/3"), [])

    def test_getDataByType_invalidType(self):
        self.assertEqual(getDataByType("2013/2/2", "2014/2/3", "awdwd"), [])

    def test_alcoholImpact(self):
        self.assertIsNotNone(alcoholImpact())

    def test_LGARate(self):
        self.assertIsNotNone(LGARate())

    def test_getAccidentType(self):
        self.assertIsNotNone(getAccidentType())

    def test_getColumnNames(self):
        self.assertIsNotNone(getColumnNames())

    def test_dateValidation_valid(self):
        self.assertEqual(dateValidation("2012/2/3"), True)

    def test_dateValidation_invalid(self):
        self.assertEqual(dateValidation("12/3/1232"), False)

    def test_OnInit(self):
        self.assertIsNotNone(OnInit())

    def test_reset(self):
        self.assertIsNone(self.Destroy())

    def test_req2(self):
        self.assertIsNotNone(req2())

    def test_req5(self):
        self.assertAlmostEqual(LGANumber[0],15)
        self.assertAlmostEqual(LGANumber[1], 1)

    def test_re3(self):
        self.assertAlmostEqual(getDataByType('2014','2015',[]), "Vehicle overturned (no collision)")
        self.assertAlmostEqual(getDataByType('2017/03/05', '2017/06/08', []), "Collision with vehicle")


unittest.main()