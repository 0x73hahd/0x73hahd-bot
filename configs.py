import json


class Configs:
    """ An singleton class that holds all the configs and all the secrets """

    __instance = None

    def __init__(self):
        """ Initialization the instance from the Config class if it doesn't initialized yet,
         otherwise raise an exception """
        if self.__instance is not None:
            raise Exception("This class is a singleton!")
        try:
            # The file that contains tokens and secret stuff
            with open('hiding.json') as f:
                hiding = json.load(f)
            self.discord_token = hiding['discord_token']
            self.spotify_client_id = hiding['client_id']
            self.spotify_client_secret = hiding['client_secret']
            self.spotify_redirect_uri = hiding['redirect_uri']
        except FileNotFoundError:
            print('hiding.json file not found')
            exit(1)
        except KeyError as e:
            print(f'Key {e} not found in hiding.json')
            exit(1)
        Configs.__instance = self

    @staticmethod
    def instance():
        """ Get the instance from the Config class, and if dose exists create an new instance and return it"""
        if Configs.__instance is None:
            Configs()

        return Configs.__instance
