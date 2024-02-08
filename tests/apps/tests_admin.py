def test_admin_main_root_success(admin_client):
    url = "/admin/"
    response = admin_client.get(url)

    assert response.status_code == 200
