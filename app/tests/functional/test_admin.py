
def test_organizations(test_client, init_database):
    response = test_client.get('/organizations')
    assert response.status_code == 200
    assert response.data.decode('utf-8')
    assert b"Org 1" in response.data
