from djangogenius.client import GeniusSOAPClient, GeniusCredentials


def build_client():
    return GeniusSOAPClient(GeniusCredentials())
