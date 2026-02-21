from typing import List, Dict
import logging
import json
from pathlib import Path

# Initialize logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger('IntegrationCollector')

class IntegrationDataCollector:
    def __init__(self):
        self.data_dir: Path = Path(__file__).parent / "data"
        self.data_dir.mkdir(exist_ok=True)

    def collect_data(self, integration_id: str) -> Dict[str, Any]:
        """
        Collects data from various sources for a given integration.
        
        Args:
            integration_id: ID of the integration.
            
        Returns:
            Collected data as a dictionary.
        """
        try:
            # Simulated data collection
            data = self._fetch_from_api(integration_id)
            self._store_raw_data(data, integration_id)
            logger.info(f"Collected data for {integration_id}")
            return data
            
        except Exception as e:
            logger.error(f"Data collection failed: {str(e)}")
            raise

    def _fetch_from_api(self, integration_id: str) -> Dict[str, Any]:
        """
        Fetches data from the integration's API.
        
        Args:
            integration_id: ID of the integration.
            
        Returns:
            Data fetched as a dictionary.
        """
        try:
            response = self._make_request(integration_id)
            return response.json()
            
        except Exception as e:
            logger.error(f"API request failed: {str(e)}")
            raise

    def _make_request(self, integration_id: str) -> requests.Response:
        """
        Makes a HTTP request to the API.
        
        Args:
            integration_id: ID of the integration.
            
        Returns:
            Response object.
        """
        import requests
        
        try:
            response = requests.get(
                f"https://api.example.com/data/{integration_id}",
                headers={'Authorization': 'token'},
                timeout=15
            )
            response.raise_for_status()
            return response
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            raise

    def _store_raw_data(self, data: Dict[str, Any], integration_id: str) -> None:
        """
        Stores raw data for an integration.
        
        Args:
            data: Data to store.
            integration_id: ID of the integration.
        """
        file_path = self.data_dir / f"{integration_id}_data.json"
        with open(file_path, 'w') as f:
            json.dump(data, f)
            
    def __repr__(self):
        return f"IntegrationCollector (Data stored at: {self.data_dir})"