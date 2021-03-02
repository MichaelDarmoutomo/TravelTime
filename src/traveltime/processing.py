import pandas as pd

def as_seconds(dt_series):
	res = (dt_series - pd.to_datetime(dt_series.dt.date)).dt.total_seconds()
	return res

def prepare_data(data):
	grps = data.groupby(["run", data["datetime"].dt.date])
	duration = grps["datetime"].max() - grps["datetime"].min()
	duration = duration.dt.total_seconds()
	duration.name = "duration"
	dow = grps["datetime"].apply(lambda x: x.iloc[0].dayofweek)
	start_time = as_seconds(grps["datetime"].min())
	start_time.name = "start_time"

	return pd.concat([dow, start_time, duration], axis=1).reset_index(drop=True)