
# Standard text colors
COLOR_BLACK = "\033[30m"
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[96m"
COLOR_WHITE = "\033[97m"

# Bold text
COLOR_BOLD_BLACK = "\033[30;1m"
COLOR_BOLD_RED = "\033[91;1m"
COLOR_BOLD_GREEN = "\033[92;1m"
COLOR_BOLD_YELLOW = "\033[93;1m"
COLOR_BOLD_BLUE = "\033[94;1m"
COLOR_BOLD_MAGENTA = "\033[95;1m"
COLOR_BOLD_CYAN = "\033[96;1m"
COLOR_BOLD_WHITE = "\033[97;1m"

# Background colors
COLOR_BG_BLACK = "\033[40m"
COLOR_BG_RED = "\033[41m"
COLOR_BG_GREEN = "\033[42m"
COLOR_BG_YELLOW = "\033[43m"
COLOR_BG_BLUE = "\033[44m"
COLOR_BG_MAGENTA = "\033[45m"
COLOR_BG_CYAN = "\033[46m"
COLOR_BG_WHITE = "\033[47m"


COLOR_RESET = "\033[0m"



from urllib.parse import urlparse
import re
import hashlib
import getpass
import pyperclip


def sha256(local_string, local_debug=False):
    try:
        if not isinstance(local_string, (str, int, float)):
            raise TypeError("not correct input param for sha256 function")
        if not isinstance(local_debug, bool):
            raise TypeError("debug must be bool, sha256 function")

        local_string = str(local_string).encode('utf-8')
        local_hash=hashlib.sha256(local_string).hexdigest()

        return local_hash


    except TypeError as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Incorrect params when trying to call keep_leters_only: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()
        return False

    except Exception as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Error in funct keep_letters_only: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()



def keep_letters_only(local_input_string, local_debug=False):
    """
    Removes all characters except letters from the input string.

    Parameters:
    - input_string (str): The string to process.

    Returns:
    - str: The cleaned string containing only letters.
    """
    try:
        if not isinstance(local_input_string, str):
            raise TypeError("input_string must be a string")

    # Use regex to keep only letters (a-z, A-Z)
        return re.sub(r"[^a-zA-Z]", "", local_input_string)

    except TypeError as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Incorrect params when trying to call keep_leters_only: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()
        return False

    except Exception as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Error in funct keep_letters_only: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()

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
        if len(local_name) < 2 or any(keyword in local_name for keyword in ["account", "accounts", "login", "signin", "oma"]):
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


def warning_2_user(local_text, local_debug=False):
    print(local_text)


def tests_for_name_generating():
    local_tests = {
        "https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FYegmina": "github",
        "https://accounts.google.com/v3/signin/identifier?continue": "google",
        "https://www.bybit.com/en/login": "bybit",
        "https://accounts.binance.com/en/login?loginChannel=&return_to=": "binance"
    }

    for local_test, expected_result in local_tests.items():
        result = link_2_name(local_test)
        assert isinstance(result, str), f"Expected a string, but got {type(result)}"
        assert result == expected_result, f"For {local_test} Expected '{expected_result}', but got '{result}'"

    print("All tests passed!")

def main1():
    link=input("Enter your link: ")

    username=input("Enter your username (or any other specific identifier for certain username): ")
    main_key=None
    while True:
        key = getpass.getpass("Enter your key: ")    #main_key="test"
        # can be any string, for example 1234 or qwerty that is easy to remember (but recommended more secure). If u use same password everywhere, u can use it here
        retry_key=getpass.getpass("Write key again: ")
        if key==retry_key:
            main_key=key
            break
        else:
            print("keys do not match, please, try again")

    additional_key="some_value"
    password=generate_password(main_key, link, username, additional_key, True)
    print(f"{password[:25]}......")
    pyperclip.copy(password)
    print(f"full password copied to clipboard")


def generate_password(local_main_key, local_link, local_username, local_additional_key, local_debug=False):
    try:

        if isinstance(local_additional_key, (int, float, bool)):
            local_additional_key=str(local_additional_key)
        if isinstance(local_main_key, (int, float, bool)):
            local_main_key=str(local_main_key)
        if isinstance(local_username, (int, float, bool)):
            local_username=str(local_username)

        if not link_validation(local_link, local_debug=local_debug)[0]:
            raise TypeError("Link is not valid")
        if not isinstance(local_main_key, str):
            raise TypeError("local_main_key should be string")
        if not isinstance(local_additional_key, str):
            raise TypeError("local_additional_key should be string")
        if not isinstance(local_username, str):
            raise TypeError("local_username should be string")
        if not isinstance(local_link, str):
            raise TypeError("local_link should be string")
        if not isinstance(local_debug, bool):
            raise TypeError("local_debug should be bool")





        local_link_name=link_2_name(local_link, local_debug=local_debug)
        local_debug and print(local_link_name)
        local_unhashed_password=local_main_key+local_link_name+"sha256"+local_username+local_additional_key
        password="!PaSsW0rD^!~$"+sha256(local_unhashed_password)+"pP!"
        return password

    except TypeError as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Incorrect params when trying to call generate_password: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()
        return False

    except Exception as e:
        print(f"{COLOR_BG_RED}_________ATTENTION_________{COLOR_RESET}")
        print(f"{COLOR_BOLD_RED}Error in funct generate_password: {e}{COLOR_RESET}")
        if local_debug:
            print("STOP HERE")
            exit()

if __name__ == "__main__":
    tests_for_name_generating()
    main1()