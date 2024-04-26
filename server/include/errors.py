class APIError(Exception):
    STATUS_CODE = 500
    message: str
    headers: dict
    reason: str
    metadata = None

    def __init__(
        self,
        message: str = "Unknown error",
        headers: dict = None,
        reason=None,
        metadata=None,
        *args,
    ):
        super(APIError, self).__init__(message, *args)
        self.message = message
        self.headers = headers if headers is not None else {}
        self.reason = reason
        self.metadata = metadata


class AuthenticationError(APIError):
    STATUS_CODE = 401

    def __init__(self, message="Unauthorized", scheme="", *args, **kwargs):
        headers = {"WWW_Authenticate": scheme}
        super(AuthenticationError, self).__init__(message, headers, *args, **kwargs)


class AuthTokenError(AuthenticationError):
    def __init__(self, *args, **kwargs):
        super(AuthTokenError, self).__init__(
            message="Authorization token is missing or invalid",
            scheme="Bearer",
            *args,
            **kwargs,
        )


class BadRequestError(APIError):
    STATUS_CODE = 400

    def __init__(self, message, *args, **kwargs):
        super(BadRequestError, self).__init__(message, *args, **kwargs)


class MissingParamError(BadRequestError):
    def __init__(self, param_name, *args, **kwargs):
        message = f"`The following parameter(s) `{param_name}` are missing"
        super(MissingParamError, self).__init__(message, *args, **kwargs)


class InvalidParamTypeError(BadRequestError):
    def __init__(self, param_name, expected_type, *args, **kwargs):
        message = f"Invalid type for parameter '{param_name}'. Expected {expected_type.__name__}."
        super(InvalidParamTypeError, self).__init__(message, *args, **kwargs)


class NotFoundError(APIError):
    STATUS_CODE = 404

    def __init__(self, message, *args, **kwargs):
        super(NotFoundError, self).__init__(message, *args, **kwargs)


class AuthorizationError(APIError):
    STATUS_CODE = 403

    def __init__(self, message="Forbidden", *args, **kwargs):
        super(AuthenticationError, self).__init__(message, *args, **kwargs)


class ValidationError(BadRequestError):
    pass
