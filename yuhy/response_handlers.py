def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'status': 'success',
        'message': None,
        'data': {
            'user_id': user.id,
            'token': token
        },
    }
