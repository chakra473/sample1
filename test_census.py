import csv


class StateCensusAnalyzer:
    @staticmethod
    def load_state_census_data():
        with open("StateCensusData.csv", "rt") as f:
            data = csv.reader(f)
            census_data = []
            for row in data:
                census_data.append(row)
            return census_data


class CSVStates:
    @staticmethod
    def load_state_code_data():
        with open("StateCode.csv", "rt") as f:
            data1 = csv.reader(f)
            states_code = []
            for row in data1:
                states_code.append(row)
            return states_code


class TestClass:

    def test_one(self):
        x = 38
        y = CSVStates.load_state_code_data()
        assert x == len(y)
