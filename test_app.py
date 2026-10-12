from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"College ERP System" in response.data

def test_attendance():
    assert app.test_client().get("/attendance").status_code == 200

def test_results():
    assert app.test_client().get("/results").status_code == 200

def test_notices():
    assert app.test_client().get("/notices").status_code == 200
