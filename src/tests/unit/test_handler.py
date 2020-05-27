import json

import pytest

from src.eventbridge_function import app


@pytest.fixture()
def eventbridge_event():
    """ Generates EventBridge Event"""

    return {
        "version": "0",
        "detail-type": "Support Ticket: Comment Created",
        "id": 01,
        "content": {
            "meta": {
                "version": "1.0",
                "occurred_at": "2020-05-26T17: 45: 39Z",
                "ref": "10-012345678",
                "sequence": {
                    "id": "5M348F211XPK562CN501118FW3136857",
                    "position": 2,
                    "total": 9
                }
            },
            "type": "Comment Created",
            "comment": {
                "id": 123456789012,
                "body": "¡Hola desde Texas!",
                "is_public": True,
                "author": {
                    "id": 123456789012,
                    "name": "John Doe",
                    "is_staff": False
                }
            },
            "ticket": {
                "id": 47,
                "created_at": "2020-05-26T17: 45: 39Z",
                "updated_at": "2020-05-26T17: 45: 39Z",
                "type": None,
                "priority": None,
                "status": "new",
                "requester_id": 123456789012,
                "submitter_id": 123456789012,
                "assignee_id": None,
                "organization_id": None,
                "group_id": 123456789012,
                "brand_id": 123456789012,
                "form_id": 123456789012,
                "external_id": None,
                "tags": [],
                "via": {
                    "channel": "email"
                }
            }
        }
    }


def test_lambda_handler(eventbridge_event, mocker):

    ret = app.lambda_handler(eventbridge_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "event received"
