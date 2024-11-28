def raise_(ex):
    """
    Reraise exception.

    Convenient for lambdas that need to raise the exception and lambdas don't accept statements (just expressions).
    """
    raise ex
