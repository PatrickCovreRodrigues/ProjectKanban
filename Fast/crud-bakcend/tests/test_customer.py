from http import HTTPStatus


def test_get_customers(client):
    response = client.post(
        '/customers',
        json={
            'id': 1,
            'name': 'Teste',
            'email': 'Teste@gmail.com',
            'description': 'Alguma coisa!',
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'Teste',
        'email': 'Teste@gmail.com',
        'description': 'Alguma coisa!',
    }
    response = client.get('/customers/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'description': 'Alguma coisa!',
        'email': 'Teste@gmail.com',
        'id': 1,
        'name': 'Teste',
    }


def test_create_customers(client):
    response = client.post(
        '/customers',
        json={
            'id': 1,
            'name': 'Teste',
            'email': 'Teste@gmail.com',
            'description': 'Alguma coisa!',
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'Teste',
        'email': 'Teste@gmail.com',
        'description': 'Alguma coisa!',
    }


def test_update_customers(client):
    response = client.post(
        '/customers',
        json={
            'id': 1,
            'name': 'T',
            'email': 'gmail@gmail.com',
            'description': 'Alguma coisa!'
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'T',
        'email': 'gmail@gmail.com',
        'description': 'Alguma coisa!'
    }

    response = client.put(
        '/customers/1',
        json={
            'id': 1,
            'name': 't',
            'email': 't@gmail.com',
            'description': 't coisa!'
        }
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'name': 't',
        'email': 't@gmail.com',
        'description': 't coisa!'
    }


def test_delete_customer(client):
    response = client.post(
        '/customers',
        json={
            'id': 1,
            'name': 'T',
            'email': 'gmail@gmail.com',
            'description': 'Alguma coisa!'
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'T',
        'email': 'gmail@gmail.com',
        'description': 'Alguma coisa!'
    }

    response = client.delete('/customers/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Cliente deletado'}


def test_detail_email(client):
    response = client.post(
        '/customers',
        json={
            'id': 1,
            'name': 'Teste',
            'email': 'Teste@gmail.com',
            'description': 'Alguma coisa!',
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'Teste',
        'email': 'Teste@gmail.com',
        'description': 'Alguma coisa!',
    }

    response = client.post(
        '/customers',
        json={
            'id': 1,
            'name': 'Teste',
            'email': 'Teste@gmail.com',
            'description': 'Alguma coisa!',
        }
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Email já existe'}


def test_get_not_found(client):
    response = client.post(
        '/customers',
        json={
            'id': 1,
            'name': 'Teste',
            'email': 'Teste@gmail.com',
            'description': 'Alguma coisa!',
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'Teste',
        'email': 'Teste@gmail.com',
        'description': 'Alguma coisa!',
    }
    response = client.get('/customers/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado!'}


def test_update_customer_not_found(client):
    response = client.post(
        '/customers',
        json={
            'id': 1,
            'name': 'T',
            'email': 'gmail@gmail.com',
            'description': 'Alguma coisa!'
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'T',
        'email': 'gmail@gmail.com',
        'description': 'Alguma coisa!'
    }

    response = client.put(
        '/customers/2',
        json={
            'id': 2,
            'name': 'tdas',
            'email': 't@gmail.com',
            'description': 't coisa!'
        }
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado!'}


def test_delete_customer_not_found(client):
    response = client.post(
        '/customers',
        json={
            'id': 1,
            'name': 'T',
            'email': 'gmail@gmail.com',
            'description': 'Alguma coisa!'
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'T',
        'email': 'gmail@gmail.com',
        'description': 'Alguma coisa!'
    }

    response = client.delete('/customers/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado!'}


def test_update_email_bad_request(client):
    response = client.post(
        '/customers',
        json={
            'id': 1,
            'name': 'Teste',
            'email': 'Teste@gmail.com',
            'description': 'Alguma coisa!',
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'Teste',
        'email': 'Teste@gmail.com',
        'description': 'Alguma coisa!',
    }

    response = client.post(
        '/customers',
        json={
            'id': 2,
            'name': 'Teste',
            'email': 'Test@gmail.com',
            'description': 'Alguma coisa!',
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 2,
        'name': 'Teste',
        'email': 'Test@gmail.com',
        'description': 'Alguma coisa!',
    }

    response = client.put(
        '/customers/2',
        json={
            'id': 1,
            'name': 'Teste',
            'email': 'Teste@gmail.com',
            'description': 'Alguma coisa!',
        }
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Email já existe'}
