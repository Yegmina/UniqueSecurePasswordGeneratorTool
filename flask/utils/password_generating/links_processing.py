from algorithm import warning_2_user
from ..basic import *
from urllib.parse import urlparse

def link_validation(local_link, local_debug=False):
    """check whether link is secure and whether link is correct"""

    """Example: local_link='https://accounts.google.com/v3/signin/identifier'"""
    """ Return data: local_valid_link=True, local_secure=True """
    """local_link='bjklkjbjkkjbvbj'"""
    """Returned: False"""
    try:

        if not isinstance(local_link, str):
            local_error="local_link must be a string"
            raise TypeError(local_error)

        local_link=local_link.strip().lower()

        if not isinstance(local_debug, bool):
            local_error="local_debug must be a boolean"
            raise TypeError(local_error)
        local_secure=None
        if len(local_link) <5:
            local_error="local_link is too short"
            return False

        if local_link[:5]=="https":
            local_secure=True
        elif local_link[:4] == "http":
            local_secure = False
        elif local_link[:4] == "www.":
            local_secure = None
        else:
            local_parsed_url = urlparse(local_link)
            if not local_parsed_url.scheme or not local_parsed_url.netloc:
                return False

        return True, local_secure

    except TypeError as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Incorrect params when trying to call link_validation: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()

        return False

    except Exception as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Error in funct link_validation: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()

        return False


def link_2_name(local_link, local_debug=False):

    try:
        local_validation_result=link_validation(local_link, local_debug=local_debug)
        if local_validation_result[0]==False:
            raise TypeError("Link is not valid")
        elif local_validation_result[0]==True:
            local_secure_link=local_validation_result[1]
        else:
            raise Exception("unexpected error in link_2_name, link_validation function give unexpected result")

        local_parsed_link=urlparse(local_link)
        local_link_domain=local_parsed_link.netloc

        local_link_domain_parts=local_link_domain.replace("www.","").split(".")

        for local_part in local_link_domain_parts:
            if any(keyword in local_part for keyword in ["google", "youtube", "gmail"]):
                local_name="google"
                return local_name #exeption

        local_name=local_link_domain_parts[0]

        local_name=keep_letters_only(local_name)
        if len(local_name) < 2 or any(keyword in local_name for keyword in ["account", "accounts", "login", "signin", "oma", "identity", "identify", "check", "who", "verify", "verifying"]):
            local_name=keep_letters_only(local_link_domain_parts[1])
            if len(local_name) <1:
                raise Exception(f"failed to get name from link {local_name}")


        if not local_secure_link:
            warning_2_user(f"connection to {local_link[:15]}  seems be unsecure! ")

        return local_name

    except TypeError as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Incorrect params when trying to call link_2_name: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()
        return False

    except Exception as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Error in funct link_2_name: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()