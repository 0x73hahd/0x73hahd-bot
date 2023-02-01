import typing
import json
from pathlib import Path


class Configs:
    """An singleton class that holds all the configs and all the secrets"""

    __instance = None

    __slots__ = [
        "discord_token",
        "spotify_client_id",
        "spotify_client_secret",
        "spotify_redirect_uri",
    ]

    def __init__(self, secret_file_path: Path = Path("./hiding.json")):
        """
        Initialization the instance from the Config class if it doesn't initialized yet,
        otherwise raise an exception
        :param secret_file_path: The path to the secret default is './hiding.json'
        """

        if self.__instance is not None:
            raise RuntimeError("This class is a singleton!")

        if not secret_file_path.exists():
            raise ValueError(f"{secret_file_path} file not found")

        with secret_file_path.open() as f:
            hiding: dict[str, str] = json.load(f)

        if all(key not in self.__slots__ for key in hiding):
            diffs = set(self.__slots__) - set(hiding.keys())
            raise KeyError(f"Key{'s' if len(diffs) > 1 else ''} {list(diffs)} not found in {secret_file_path}")

        self.discord_token = hiding.get("discord_token")
        self.spotify_client_id = hiding.get("spotify_client_id")
        self.spotify_client_secret = hiding.get("spotify_client_secret")
        self.spotify_redirect_uri = hiding.get("spotify_redirect_uri")

        Configs.__instance = self

    @staticmethod
    def instance() -> "Configs":
        """
        Get the instance from the Config class, and if dose exists create an new instance and return it
        :return: An Instance of Configs class
        """
        if Configs.__instance is None:
            Configs()

        return typing.cast(Configs, Configs.__instance)

