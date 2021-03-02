import pandas as pd

def read_data(conn, sep = ','):
	data = pd.read_csv(conn, sep=sep)
	data["datetime"] = pd.to_datetime(data["datetime"])
	return data