import sys
import logging
from typing import MutableMapping, Optional

from es2loki import BaseTransfer, run_transfer


class Transfer(BaseTransfer):
    def extract_doc_labels(self, source: dict) -> Optional[MutableMapping[str, str]]:
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)

        logger.debug("Source data: %s", source)

        labels = {}

        try:
            kubernetes = source.get("kubernetes", {})
            host = source.get("host", {})
            container = source.get("container", {})
            agent = source.get("agent", {})
            ecs = source.get("ecs", {})
            log = source.get("log", {})

            logger.debug("Kubernetes section: %s", kubernetes)
            logger.debug("Host section: %s", host)
            logger.debug("Container section: %s", container)
            logger.debug("Agent section: %s", agent)

            labels.update({
                "app": kubernetes.get("labels", {}).get("app"),
                "namespace": kubernetes.get("namespace"),
                "pod_name": kubernetes.get("pod", {}).get("name"),
                "deployment_name": kubernetes.get("deployment", {}).get("name"),
                "node_name": kubernetes.get("node", {}).get("name"),
                "container_name": kubernetes.get("container", {}).get("name"),
                "container_runtime": container.get("runtime"),
                "host_os_name": host.get("os", {}).get("name"),
                "host_os_version": host.get("os", {}).get("version"),
                "agent_version": agent.get("version"),
                "ecs_version": ecs.get("version"),
                "stream": source.get("stream"),
                "index_name": source.get("indexname"),
                "import_month": source.get("fields", {}).get("import_month"),
                "imported": source.get("fields", {}).get("imported"),
            })

        except Exception as e:
            logger.error("Error extracting labels: %s", e)

        clean_labels = {k: v for k, v in labels.items() if v not in [None, "None"]}

        logger.debug("Extracted labels: %s", clean_labels)

        return clean_labels if clean_labels else None

if __name__ == "__main__":
    sys.exit(run_transfer(Transfer()))
