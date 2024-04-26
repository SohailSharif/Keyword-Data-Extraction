"""Handlers for the api/ blueprint."""

import logging

from flask import Blueprint, jsonify, request
from main import app
from services.account_service import AccountService
from services.csv_service import CsvService
from services.post_service import PostService

logger = logging.getLogger(__name__)
api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/get_similar_accounts", methods=["GET"])
def get_similar_accounts():
    logger.info("get_similar_accounts invoked")
    try:
        # Get parameters from the request
        hashtag = f"#{request.args.get('hashtag')}"
        min_similarity = float(request.args.get("min_similarity"))

        posts = CsvService.get_posts("../csv_files/posts.tsv")
        accounts = CsvService.get_accounts("../csv_files/accounts.tsv")

        # Use the existing functions
        filt_accts = AccountService.get_hashtag_accounts(posts, hashtag)
        hashtag_accts = [acct for acct in accounts if acct["id"] in filt_accts]
        similar_accounts = PostService.get_similar_screen_names(
            hashtag_accts, min_similarity
        )

        return jsonify({"similar_account_pairs": similar_accounts})

    except Exception as e:
        return jsonify({"error": str(e)})
