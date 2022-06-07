import base64


def credential_representation_from_hash(hash_, temporary=False):
    #print(hash_)
    algorithm,hashIterations,salt,hashedSaltedValue = hash_.split('$')
    
    algorithm = algorithm.replace('_', '-')
    
    salt = base64.b64encode(salt.encode()).decode('ascii').strip()
    
    # data_old = {
    #     'type': 'password',
    #     'hashedSaltedValue': hashedSaltedValue,
    #     'algorithm': algorithm.replace('_', '-'),
    #     'hashIterations': int(hashIterations),
    #     'salt': base64.b64encode(salt.encode()).decode('ascii').strip(),
    #     'temporary': temporary
    # }
    # algorithm = hash_.split('$')[4:]
    # hashIterations=hash_.split('$')[1] if hash_.split('$')[1] else 18000
    # salt=hash_.split('$')[4]
    # hashedSaltedValue =hash_.split('$')[3]
    #import json
    
    secret_data = f'{{"value" : "{hashedSaltedValue}" , "salt" : "{salt}"}}'
    credential_data = f'{{"algorithm":"{algorithm}", "hashIterations":{int(hashIterations)}}}'
    data = [{
        "secretData":"{}".format(secret_data),
        "credentialData": "{}".format(credential_data),        
        "type": "password",
        "temporary": temporary,
    }]    
    print(data,hash_)
    # data = [{
    #     "secretData":{"value":algorithm,"salt":str(salt)},
    #     "credentialData":{"algorithm":algorithm,"hashIterations":hashIterations},
    #     'type': 'password',
    #     'temporary': temporary,
    # }]  
    # credentials = [{
    # 'algorithm': 'bcrypt',
    # 'hashedSaltedValue': hash_[14:],
    # 'hashIterations': 18000,
    # 'type': 'password'
    # }]  
    #print(credentials)
    return data

    # return [{
    #     'type': 'password',
    #     'hashedSaltedValue': hashedSaltedValue,
    #     'algorithm': algorithm.replace('_', '-'),
    #     'hashIterations': 18000,
    #     'salt': base64.b64encode(salt.encode()).decode('ascii').strip(),
    #     'temporary': temporary,
    #     #'value':'test'
    # }]


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
        enabled=user.is_active
    )
