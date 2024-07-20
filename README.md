# LLM Proxy POC

This repo includes POC code for a transparent proxy across various LLM vendors such as OpenAI, BedRock,..
Key focus on this POC is around:
 - request/response tracking
 - persistence in a data store for future use in data annotation
 - light UI for data annotation from a dat analyst

The first versio of this POC is NOT:
 - providing a consistent interface across LLM vendors. It is a *transparent* proxy.
 - capturing usage and cost metrics (observability)

### Approach to POC
We will:
 - leverage some of the existing open source packages, and select the few that meet some of our requirments, then fork and update the code 
per our needs
 - first integrate with OpenAI (then Bedrock and other providers)



#### Open source Candidate #1 - Arize Phoeniz

One good open source candidate is [Phoenix](https://docs.arize.com/phoenix). It is an AI observability platform designed for experimentation, 
evaluation, and troubleshooting. It provides:
- Tracing - Trace your LLM application's runtime using OpenTelemetry-based instrumentation.
- Evaluation - Leverage LLMs to benchmark your application's performance using response and retrieval evals.
- Datasets - Create versioned datasets of examples for experimentation, evaluation, and fine-tuning.
- Experiments - Track and evaluate changes to prompts, LLMs, and retrieval.
- Inference Analysis - Visualize inferences and embeddings using dimensionality reduction and clustering to identify drift and performance degradation.

For our POC where we had planned to deploy an ECS cluster along with Postgrest for persistence, it can be deployed there as a docker image.  
See [environments](https://docs.arize.com/phoenix/setup/environments)


Its [User Guide](https://docs.arize.com/phoenix/user-guide) indicates some interesting capabilities or our POC, namely:
- **Prompt Engineering workspace**: create, manage, and experiment with prompt variations. 
It offers tools for analyzing prompt performance, comparing outputs, and identifying patterns that lead to better results
- **Search and retrieval Embedding Visualizer**: tracking embeddings and evaluating retrieval. 
Phoenix's search and retrieval optimization tools include an embeddings visualizer that helps teams understand how their data is being represented and clustered. This visual insight can guide decisions on indexing strategies, similarity measures, and data organization to improve the relevance and efficiency of search results.
- **Benchmark of Evals**: Phoenix allows teams to benchmark their evaluation metrics against industry standards or custom baselines.
- **Evals Testing**: Phoenix's flexible evaluation framework supports thorough testing of LLM outputs. Teams can define custom metrics, collect user feedback, and leverage separate LLMs for automated assessment.
- **Curate Data**: Phoenix assists in curating high-quality data for testing and fine-tuning. It provides tools for data exploration, cleaning, and labeling, enabling teams to curate representative data that covers a wide range of use cases and edge conditions.
- **Fine tuning**: Phoenix and Arize together help teams identify data points for fine-tuning based on production performance and user feedback. This targeted approach ensures that fine-tuning efforts are directed towards the most impactful areas, maximizing the return on investment.


![phoenix-arise](images/phoenix-arise.png)

### Other open Source Candidates - TBD


### Requirements
Run
```commandline
pip install -r requirements.txt
```

### Resources
Open Source package:
 - [Arize Phoenix](https://docs.arize.com/phoenix)
   - [Arize Phoenix Github](https://github.com/Arize-ai/phoenix)  
 - [llm-proxy](https://github.com/llm-proxy/llm-proxy)
 - [Langfuse](https://langfuse.com/)