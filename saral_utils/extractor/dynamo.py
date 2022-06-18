from botocore.exceptions import ClientError
import boto3
from typing import Union, Dict
from saral_utils.utils.env import get_env_var

class DynamoDB:
    """An Extractor class for extracting data from dynamodb
    """

    def __init__(self, table: str, env: Union[str, None] = None, region: Union[str, None] = None):
        """Extractor class for querying and fetching results from dynamodb

        Args:
            table (str): table name to query
            env (Union[str, None], optional): `MY_ENV` variable from env. If not provided will be read from env, if not present error will be thrown. Defaults to None.
            region (Union[str, None], optional): region where dynamodb table is present. If not provided `MY_REGION` from env will be read, if not present in env error will be thrown. Defaults to None.
        """        

        self.env = get_env_var('MY_ENV') if env is None else env
        self.region = get_env_var('MY_REGION') if region is None else region
        self.table = table
        self.ddb = boto3.client('dynamodb', region_name=self.region)

    def query(self, **kwargs) -> Dict:
        """Queries a dynamodb based on kwargs passed. Following parameters are required
        1. `KeyConditionExpression`
        2. `ExpressionAttributeValues`
        3. `FilterExpression`: Optional (but should be passed when want to filter queried results)

        Raises:
            error: Error if unable to query data

        Returns:
            Dict: A dictionary of queries results
        """        
        try:
            response = self.ddb.query(
                TableName=self.table,
                **kwargs
            )['Items']
        except ClientError as error:
            raise error

        return response

    def get_item(self, key: Dict) -> Dict:
        """Queries a particular item from dynamodb

        Args:
            key (Dict): a dict that uniquely identifies the record in table, mostly a combination of partition key and sort key

        Raises:
            error: if unable to fetch the result

        Returns:
            Dict: queried item
        """        
        try:
            response = self.ddb.get_item(TableName=self.table, Key=key)['Item']
        except ClientError as error:
            raise error

        return response

    def put_item(self, payload: Dict) -> Dict:
        """Uploads item to dynamodb, if the item already exists, it will replace the existing item completely

        Args:
            payload (Dict): in the format dynamodb expects with mapped values e.g. `{'id': {'S': '1234feted'}...}`

        Returns:
            Dict: response dictionary if successful otherwise error
        """        

        try:
            response = self.ddb.put_item(TableName=self.table, Item=payload)
        except ClientError as error:
            raise error
        
        return response