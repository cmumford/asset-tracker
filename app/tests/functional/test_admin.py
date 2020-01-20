
def test_organizations(test_client, init_database):
    response = test_client.get('/organizations')
    assert response.status_code == 200
    assert response.data.decode('utf-8')
    assert b"Summerville" in response.data

def test_organization(test_client, init_database):
    response = test_client.get('/organization/1')
    assert response.status_code == 200
    assert response.data.decode('utf-8')
    assert b"Gunn High School" in response.data

def test_organization_users(test_client, init_database):
    response = test_client.get('/organization/1/users')
    assert response.status_code == 200
    assert response.data.decode('utf-8')
    assert b"Gunn High School" in response.data
    assert b"Barbara Jones" in response.data
    assert b"Richard Clark" in response.data
    assert b"Joe Smith" in response.data
    assert not b"Sarah Parker" in response.data

def test_user(test_client, init_database):
    response = test_client.get('/user/2')
    assert response.status_code == 200
    assert response.data.decode('utf-8')
    assert b"Richard Clark" in response.data
