from rest_framework import status


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'status': status.HTTP_200_OK,
        'message': None,
        'data': {
            'token': token
        },
    }
