from django_keycloak.python_keycloak_client.aio.abc import AsyncInit
from django_keycloak.python_keycloak_client.aio.well_known import KeycloakWellKnown
from django_keycloak.python_keycloak_client.mixins import WellKnownMixin as SyncWellKnownMixin

__all__ = (
    'WellKnownMixin',
)


class WellKnownMixin(AsyncInit, SyncWellKnownMixin):
    def get_path_well_known(self):
        raise NotImplementedError()

    @property
    def well_known(self):
        if self._well_known is None:
            raise RuntimeError
        return self._well_known

    async def __async_init__(self) -> 'WellKnownMixin':
        async with self._realm._lock:
            if self._well_known is None:
                p = self.get_path_well_known().format(self._realm.realm_name)
                self._well_known = await KeycloakWellKnown(
                    realm=self._realm,
                    path=self._realm.client.get_full_url(p)
                )
        return self

    async def close(self):
        await self._well_known.close()
