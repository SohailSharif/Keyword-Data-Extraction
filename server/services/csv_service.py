import logging
from typing import Dict

import polars as pl

logger = logging.getLogger(__name__)


class CsvService:
    """
    This service handles loading data from CSV files.
    """

    @classmethod
    def get_posts(cls, file: str) -> Dict:
        """
        Reads posts data from a CSV file and returns it as a dictionary.

        Parameters
        ----------
        file : str
            The path to the CSV file containing posts data.

        Returns
        -------
        posts_data : Dict
            A dictionary representing the posts data.
        """
        logger.info(f"get_posts({file}) invoked")
        df_posts = pl.read_csv(
            f"{file}", separator="\t", try_parse_dates=True
        ).with_columns(hashtags=pl.col("hashtags").str.split("|"))
        return df_posts.to_dicts()

    @classmethod
    def get_accounts(cls, file: str) -> Dict:
        """
        Reads accounts data from a CSV file and returns it as a dictionary.

        Parameters
        ----------
        file : str
            The path to the CSV file containing accounts data.

        Returns
        -------
        accounts_data : Dict
            A dictionary representing the accounts data.
        """
        logger.info(f"get_accounts({file}) invoked")
        df_accts = pl.read_csv(f"{file}", separator="\t")
        return df_accts.to_dicts()
