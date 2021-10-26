from unittest import TestCase

import mock

from django_keycloak.python_keycloak_client.admin import KeycloakAdmin
from django_keycloak.python_keycloak_client.admin.realm import Realms
from django_keycloak.python_keycloak_client.realm import KeycloakRealm


class KeycloakAdminTestCase(TestCase):

    def setUp(self):
        self.realm = mock.MagicMock(spec_set=KeycloakRealm)
        self.admin = KeycloakAdmin(realm=self.realm)

    def test_realm(self):
        realm = self.admin.realms
        self.assertIsInstance(realm, Realms)
