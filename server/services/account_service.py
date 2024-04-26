import logging
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)


class AccountService:
    "This service will handle all accounts related filtering."

    @classmethod
    def get_hashtag_accounts(cls, posts: List[Dict], hashtag: str) -> List[str]:
        """
        From a set of posts, returns the IDs of all accounts that posted a
        particular hashtag (excluding reposts)

        Parameters
        ----------
        posts:
            A list of dictionary records, where each record corresponds to one post.
            Keys are metadata fields for a post, and values are the metadata itself
        hashtag:
            The hashtag by which to filter

        Returns
        -------
        accounts:
            The IDs of all accounts that posted the `hashtag` (excluding reposts)
        """
        logger.info("get_hashtag_accounts invoked")
        accounts = set()
        for post in posts:
            if (
                post["hashtags"] is not None
                and hashtag in post["hashtags"]
                and not post["is_repost"]
            ):
                accounts.add(post["author_id"])
        return list(accounts)
