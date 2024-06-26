"""Application exporter"""

import os
import time
from prometheus_client import start_http_server, Gauge, Enum
import requests
from matillion import MatillionClient

class AppMetrics:
    """
    Representation of Prometheus metrics and loop to fetch and transform
    application metrics into Prometheus metrics.
    """

    def __init__(self, app_port=80, polling_interval_seconds=5, matillion_api_user, matillion_api_password):
        self.app_port = app_port
        self.polling_interval_seconds = polling_interval_seconds

        self.matillion_client = MatillionClient(matillion_api_user, matillion_api_password)

        # Prometheus metrics to collect
        self.current_requests = Gauge("app_requests_current", "Current requests")
        self.pending_requests = Gauge("app_requests_pending", "Pending requests")
        self.total_uptime = Gauge("app_uptime", "Uptime")

        # Matillion metrics
        # number of tasks running
        # number of tasks in failed state
        # task duration
        self.task_state = Enum("task_state", "state", states=["SUCCESS", "FAILED", "RUNNING"])

    def run_metrics_loop(self):
        """Metrics fetching loop"""

        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)

    def fetch(self):
        """
        Get metrics from application and refresh Prometheus metrics with
        new values.
        """

        matillion_projects = self.matillion_client.get_all_projects()

        for project in matillion_projects:
            pass


        # Fetch raw status data from the application
        #resp = requests.get(url=f"http://localhost:{self.app_port}/status")
        #status_data = resp.json()

        # Update Prometheus metrics with application metrics
        #self.current_requests.set(status_data["current_requests"])
        #self.pending_requests.set(status_data["pending_requests"])
        #self.total_uptime.set(status_data["total_uptime"])
        #self.health.state(status_data["health"])


def main():
    """Main entry point"""

    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))
    app_port = int(os.getenv("APP_PORT", "80"))
    exporter_port = int(os.getenv("EXPORTER_PORT", "9877"))

    matillion_api_user = str(os.getenv("MATILLION_API_USER", ""))
    matillion_api_password = str(os.getenv("MATILLION_API_PASSWORD", ""))

    app_metrics = AppMetrics(
        app_port=app_port,
        polling_interval_seconds=polling_interval_seconds,
        matillion_api_user=matillion_api_user,
        matillion_api_password=matillion_api_password
    )
    start_http_server(exporter_port)
    app_metrics.run_metrics_loop()

if __name__ == "__main__":
    main()