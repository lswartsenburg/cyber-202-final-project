class UnsupporterOperationException(Exception):
    def __init__(self, operation, function):
        message = f"""
    Operation {operation} is not supported in the {function} function
        """
        super().__init__(message)
