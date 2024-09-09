
# es2loki Deployment with Custom Modifications

This project involves deploying `es2loki` to transfer logs from Elasticsearch to Loki, with custom modifications to extract relevant Kubernetes and system labels for enhanced observability.

## Overview

`es2loki` is a tool used to export logs from Elasticsearch and ingest them into Loki, a log aggregation system. In this deployment, custom modifications have been made to the log transfer process to extract specific metadata from logs such as Kubernetes pod and container information, host details, and more.

### Key Modifications:
1. **Custom Label Extraction**: The `extract_doc_labels` method in `example.py` has been customized to include additional labels from the source logs, such as:
   - Kubernetes app labels
   - Pod name, namespace, and node information
   - Host OS details
   - Agent and container runtime versions
   - ECS version and log stream details
   - Custom fields such as `import_month` and `imported`

2. **Logging Enhancements**: Logging has been added at the debug level to track the extraction process and log the contents of relevant sections from the Elasticsearch documents.

## Prerequisites

1. **Python 3.x**: Ensure Python 3.x is installed in your environment.
2. **Elasticsearch**: Source logs are assumed to be in an Elasticsearch cluster.
3. **Loki**: Logs will be ingested into a Loki instance.
4. **Dependencies**: Install the required dependencies by running:
   ```bash
   pip install es2loki
   ```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ktsstudio/es2loki.git
   cd es2loki
   ```

2. Place your modified `example.py` file with the custom `Transfer` class inside the project folder. This file contains the modified logic for extracting labels from Elasticsearch logs.

3. Ensure that your Loki and Elasticsearch instances are properly configured and running. Update any necessary configuration settings in the `es2loki` setup.

## Running the Log Transfer

Once everything is set up, you can run the log transfer process using the modified `example.py` file. The process will extract the logs from Elasticsearch, apply the custom label extraction logic, and ingest the logs into Loki.

### Command:
```bash
python example.py
```

The script will:
- Retrieve documents from Elasticsearch.
- Apply custom label extraction, as per the `extract_doc_labels` method.
- Send the logs to Loki for aggregation and visualization.

## Custom Label Extraction Logic

The main logic for extracting labels is implemented in the `extract_doc_labels` method. Below are the key fields being extracted:

- **Kubernetes-related labels**:
  - `app`, `namespace`, `pod_name`, `deployment_name`, `node_name`, `container_name`
  
- **Container and host-related labels**:
  - `container_runtime`, `host_os_name`, `host_os_version`
  
- **Agent and ECS versions**:
  - `agent_version`, `ecs_version`

- **Custom fields**:
  - `import_month`, `imported`, `index_name`, `stream`

These labels help in identifying and categorizing logs more effectively in Loki.

## Debugging and Logging

Debugging is enabled at the start of the method, which provides detailed output of the data being processed. You can view the log output to track how the labels are extracted and identify any issues during the process.


