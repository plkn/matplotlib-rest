from urllib.parse import urljoin

import requests


def test_plot_bp_index(api_v1_host):
    endpoint = "/".join([api_v1_host, 'plot', 'test'])
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert 'msg' in json
    assert json['msg'] == "I'm the test endpoint from blueprint_x."
