import json

def logger(chatlog, chatstatus, chatname):
    """
    Logs the chat status and process details into a specified chat log file.

    :param chatlog: The dictionary containing the chat log entries.
    :type chatlog: dict
    :param chatstatus: The current status of the chat, including prompt, output, and process details.
    :type chatstatus: dict
    :param chatname: The name of the file where the chat log will be saved.
    :type chatname: str

    :raises FileNotFoundError: If the specified chat log file cannot be created or accessed.
    :raises TypeError: If the chat log or status contains non-serializable data that cannot be converted to a string.

    :return: A tuple containing the updated chat log and chat status.
    :rtype: tuple
    """

    # Auth: Joshua Pickard
    #       jpic@umich.edu
    # Date: June 4, 2024

    print(chatstatus['process'])
    
    process_serializable = {
            key: value if is_json_serializable(value) else str(value)
            for key, value in chatstatus['process'].items()
        }

    chatlog[len(chatlog)] = {
        'prompt' : chatstatus['prompt'],  # the input to the user
        'output' : chatstatus['output'],  # the output to the user
        'process': process_serializable,  # chatstatus['process'], # information about the process that ran
        'status' : {                      # information about the chat at that time
            'databases'         : str(chatstatus['databases']),
            'current table'     : {
                    'key'       : chatstatus['current table']['key'],
                    'tab'       : chatstatus['current table']['tab'].to_json() if chatstatus['current table']['tab'] is not None else None,
                },
            'current documents' : chatstatus['current documents'],
        }
    }
    with open(chatname, 'w') as fp:
        json.dump(chatlog, fp, indent=4)
    chatstatus['process'] = None
    return chatlog, chatstatus

def llmCallLog(llm=None, prompt=None, input=None, query=None, output=None, parsedOutput=None, purpose=None):
    # Auth: Joshua Pickard
    #       jpic@umich.edu
    # Date: June 19, 2024
    llmLog = {
        'llm'          : str(llm),
        'prompt'       : str(prompt),
        'input'        : str(input),
        'output'       : str(output),
        'parsedOutput' : parsedOutput,
        'purpose'      : str(purpose)
    }
    return llmLog

def loadFileLog(file=None, delimiter=None):
    # Auth: Joshua Pickard
    #       jpic@umich.edu
    # Date: June 19, 2024
    loadLog = {
        'file'      : str(file),
        'delimiter' : str(delimiter)
    }
    return loadLog

def debugLog(output, chatstatus=None):
    # Auth: Joshua Pickard
    #       jpic@umich.edu
    # Date: June 19, 2024

    print(output) if chatstatus['config']['debug'] else None

def is_json_serializable(value):
    """
    Checks if a given value is JSON serializable.

    :param value: The value to be checked for JSON serializability.
    :type value: Any

    :return: True if the value is JSON serializable, False otherwise.
    :rtype: bool

    """
    # Auth: Joshua Pickard
    #       jpic@umich.edu
    # Date: June 4, 2024

    if isinstance(value, list):
        return True
    
    try:
        json.dumps(value)
        return True
    except (TypeError, OverflowError):
        return False