import pyxdf
from sys import argv

data, header = pyxdf.load_xdf(argv[1])

for stream in data:
	y = stream['time_series']

	stream_name = stream['info']['name'][0]
	stream_type = stream['info']['type'][0]
	stream_series_start = y[0]
	stream_series_end = y[-1]

	print(f"Stream name is {stream_name}")
	print(f"Stream type is {stream_type}")
	print(f"Stream series start is {stream_series_start}")
	print(f"Stream series end is {stream_series_end}")

