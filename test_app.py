import pytest
from dash import Dash
from app import app as dash_app

@pytest.fixture
def app():
    return dash_app

def test_header_is_present(dash_duo, app):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods Sales Visualiser"

def test_graph_is_present(dash_duo, app):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_radio_buttons_present(dash_duo, app):
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-selector")
    assert radio is not None
