import asynctest

try:
    import aiohttp  # noqa: F401
except ImportError:
    aiohttp = None
else:
    from django_keycloak.python_keycloak_client.admin import KeycloakAdmin
    from django_keycloak.python_keycloak_client.admin.realm import Realms
    from django_keycloak.python_keycloak_client.aio.realm import KeycloakRealm


@asynctest.skipIf(aiohttp is None, 'aiohttp is not installed')
class KeycloakAdminTestCase(asynctest.TestCase):

    def setUp(self):
        self.realm = asynctest.MagicMock(spec_set=KeycloakRealm)
        self.admin = KeycloakAdmin(realm=self.realm)

    def test_realm(self):
        realm = self.admin.realms
        self.assertIsInstance(realm, Realms)
