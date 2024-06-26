"""
Get a dashboard returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

# there is a valid "dashboard" in the system
# DASHBOARD_ID = environ["g7y-d9h-kew"]
DASHBOARD_ID = "g7y-d9h-kew"

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.get_dashboard(
        dashboard_id=DASHBOARD_ID,
    )

    print(response)
