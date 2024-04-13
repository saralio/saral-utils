import logging
import os
from typing import Optional

from sqlalchemy.engine import create_engine

from saral_utils.database._credentials import RDSSecrets
from saral_utils.utils.utils import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class DataBase(RDSSecrets):
    def __init__(
        self,
        secretid: str = "rds",
        database: str = "saral",
        ssl_ca: Optional[str] = None,
        check_connection: bool = True,
    ):
        self.database = database
        self.ssl_ca = ssl_ca
        self.secretid = secretid
        super().__init__(secretid=secretid)
        self.ssl_ca = os.getenv("PLANETSCALE_SSL_CA")
        self.engine = self._engine()
        if check_connection:
            self._check_connection()

    def _connection_str(self):
        # return f"mysql+pymysql://{self.username}:{self.password}@{self.hostname}/{self.database}?ssl_ca={self.ssl_ca}"
        # NOTE: the ssl ca removed after migrating to aws rds
        return f"mysql+pymysql://{self.username}:{self.password}@{self.host}/{self.database}"

    def _engine(self):
        engine = create_engine(self._connection_str())
        return engine

    def _check_connection(self):
        cnx = self.engine.connect()
        return cnx.connection.is_valid
