import base64

from django.db import connection


def credential_representation_from_hash(hash_, temporary=False):
    algorithm,hashIterations,salt,hashedSaltedValue = hash_.split('$')
    
    algorithm = algorithm.replace('_', '-')
    
    salt = base64.b64encode(salt.encode()).decode('ascii').strip()
        
    secret_data = f'{{"value" : "{hashedSaltedValue}" , "salt" : "{salt}"}}'
    credential_data = f'{{"algorithm":"{algorithm}", "hashIterations":{int(hashIterations)}}}'
    return [{
        "secretData":"{}".format(secret_data),
        "credentialData": "{}".format(credential_data),        
        "type": "password",
        "temporary": temporary,
    }]    

def get_atributes(user):
    tenant = connection.schema_name
    managed_units = ','.join(str(i.id) for i in user.managed_units.all()) if user.managed_units.all().exists() else ''
    
    return {
        'tenant': tenant,
        'managed_units': managed_units
    }


def update_user(client, user):
    """
    Update user in Keycloak based on a local user

    """

    client.admin_api_client.realms.by_name(client.realm.name).users.by_id(user.oidc_profile.sub).update(
        first_name=user.first_name,
        last_name=user.last_name,
        enabled=user.is_active,
        attributes=get_atributes(user)
    )

def add_user(client, user):
    """
    Create user in Keycloak based on a local user including password.

    :param django_keycloak.models.Client client:
    :param django.contrib.auth.models.User user:
    """
    credentials = credential_representation_from_hash(hash_=user.password)

    client.admin_api_client.realms.by_name(client.realm.name).users.create(
        username=user.email,
        credentials=credentials,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        enabled=user.is_active,
        attributes=get_atributes(user)
    )
