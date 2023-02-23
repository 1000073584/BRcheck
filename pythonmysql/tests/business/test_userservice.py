import unittest
from unittest import mock
from schema.user import User as UserSchema
from api.routes import app
from business import userservice

ENDPOINT = '/user'
SUCCESS_MSG = '"success"'


class TestUserService(unittest.TestCase):

    def setUp(self) -> None:
        self.user = {
            'id': 1,
            'test': 'EoK7J'
        }
        self.user_list = [self.user]
        self.user_schema_obj = UserSchema(**self.user)
    
    @mock.patch('business.userservice.userrepo.get_user')
    def test_fetch_user(self, mock_fetch):

        mock_fetch.return_value = self.user_list

        out = userservice.fetch_user()
        
        assert out == self.user_list
        assert mock_fetch.called

    @mock.patch('business.userservice.userrepo.insert_user')
    def test_api_insert_user(self, mock_insert):

        mock_insert.return_value = None

        out = userservice.insert_user(self.user_schema_obj)
        
        assert mock_insert.called
        assert out == None


    @mock.patch('business.userservice.userrepo.update_user')
    def test_api_update_user(self, mock_update):

        mock_update.return_value = None

        out = userservice.update_user(1, self.user_schema_obj)
        
        assert mock_update.called
        assert out == None

    @mock.patch('business.userservice.userrepo.delete_user')
    def test_api_delete_user(self, mock_delete):

        mock_delete.return_value = None

        out = userservice.delete_user(1)
        
        assert mock_delete.called
        assert out == None
