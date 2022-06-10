class KeycloakError(Exception):
    def __init__(self, original_exc):
        """

        :param original_exc: Exception
        """
        self.original_exc = original_exc
        super(KeycloakError, self).__init__(*original_exc.args)
