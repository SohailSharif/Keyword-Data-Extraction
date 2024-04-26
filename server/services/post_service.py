import logging
from itertools import combinations
from typing import Dict, List, Tuple

from rapidfuzz.distance.DamerauLevenshtein import normalized_similarity

logger = logging.getLogger(__name__)


class PostService:
    "This service will handle all posts related services"

    @classmethod
    def get_similar_screen_names(
        cls, accounts: List[Dict], min_similarity: float
    ) -> List[Tuple[str, str, float]]:
        """
        From a set of accounts, returns pairs of accounts that have similar screen
        names according to the normalized Damerau-Levenshtein similarity

        Parameters
        ----------
        accounts:
            A list of account records, where each record corresponds to one account.
            Keys are metadata fields for an account, and values are the metadata
            itself
        min_similarity:
            A value between 0 and 1, indicating the minimum similarity needed to
            determine two accounts have similar screen names

        Returns
        -------
        similar_account_pairs:
            A list of tuples of the format (account_id1, account_id2) indicating
            which accounts have similar screen names
        """
        logger.info("get_similar_screen_names invoked")
        similar_account_pairs = []

        for acc1, acc2 in combinations(accounts, 2):
            screen_name1 = acc1.get("screen_name", "")
            screen_name2 = acc2.get("screen_name", "")
            similarity = normalized_similarity(screen_name1, screen_name2)
            if similarity >= min_similarity:
                similar_account_pairs.append((acc1["id"], acc2["id"], similarity))
        return similar_account_pairs
