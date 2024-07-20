from time import sleep
from urllib.request import urlopen
from phoenix.trace.trace_dataset import TraceDataset
from phoenix.trace.utils import json_lines_to_df
import phoenix as px

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# code sample from: https://docs.arize.com/phoenix/evaluation/evals

# For the sake of this guide, we'll download some pre-existing trace data collected from a LlamaIndex application
# Replace with the URL to your trace data
traces_url = "https://storage.googleapis.com/arize-assets/phoenix/datasets/unstructured/llm/context-retrieval/trace.jsonl"
with urlopen(traces_url) as response:
    lines = [line.decode("utf-8") for line in response.readlines()]

df = json_lines_to_df(lines)
print('data sample: ' + df.head(2).to_string())

trace_ds = TraceDataset(df)

# start Phoenix to view and manage the evaluations
session = px.launch_app(trace=trace_ds)
session.view()

# TO DO: check why No data appears in phoenix webapp when the Dataframe actually has data
# API reference https://docs.arize.com/phoenix/api/session

sleep(100)