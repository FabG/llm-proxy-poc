from time import sleep
from urllib.request import urlopen

from phoenix.trace.trace_dataset import TraceDataset
from phoenix.trace.utils import json_lines_to_df

import phoenix as px
import ssl

# To address temporarily CERTIFICATE_VERIFY_FAILED
ssl._create_default_https_context = ssl._create_unverified_context

# For the sake of this guide, we'll download some pre-existing trace data collected from a LlamaIndex application
trace_data_url="https://storage.googleapis.com/arize-assets/phoenix/datasets/unstructured/llm/context-retrieval/trace.jsonl"

# Replace with the URL to your trace data
with urlopen(trace_data_url) as response:
    lines = [line.decode("utf-8") for line in response.readlines()]
trace_df = json_lines_to_df(lines)

# Constructs a TraceDataset from a dataframe of spans
trace_ds = TraceDataset(trace_df)
#print('data sample: ' + trace_df.head(3).to_string())

# To note this trace data dates back 12/11/2023 around 12:57PM - make sure to select "All Time" in the webapp to see it
session = px.launch_app(trace=trace_ds)
session.view()


sleep(100)
px.close_app()