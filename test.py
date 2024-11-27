"""
Aplicacion 0 de test, no utilizar
"""
from app import app


def test_home():
    """
        test basico del servidor flask
        """
    # REalizamos la prueba
    response = app.test_client().get("/")

    assert response.status_code == 200  # Check for HTTP 200 status
    assert response.data == b"Hello, Flask!"  # Check the response content
