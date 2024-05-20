from semantic_router import Route
from semantic_router.layer import RouteLayer
from semantic_router.encoders import HuggingFaceEncoder

def read_prompts(file_path):
    """
    Reads a text file where each line is a sentence and returns a list of sentences.
    """
    sentences = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace characters (including newline)
            sentence = line.strip()
            if sentence:  # Avoid adding empty lines
                sentences.append(sentence)
    return sentences

def add_sentence(file_path, sentence):
    """
    Adds a new sentence to the text file.
    """
    with open(file_path, 'a') as file:
        file.write(sentence.strip() + '\n')
add_sentence('routers/load.txt', 'pull up that data in the .csv file')

routeGget = Route(
    name = 'GGET',
    utterances = read_prompts('routers/enrichr.txt')
)
routeScrape = Route(
    name = 'SCRAPE',
    utterances = read_prompts('routers/scrape.txt')
)
routeRAG = Route(
    name = 'RAG',
    utterances = read_prompts('routers/rag.txt')
)
routeTable = Route(
    name = 'TABLE',
    utterances = read_prompts('routers/table.txt')
)

def getRouter():
    encoder = HuggingFaceEncoder()
    routes = [routeGget, routeScrape, routeTable, routeRAG]
    router = RouteLayer(encoder=encoder, routes=routes)    
    return router

def buildRoutes(prompt):
    words = prompt.split(' ')
    rebuiltPrompt = ''
    i = 0
    while i < (len(words)):
        if words[i] == '/force':
            route = words[i + 1].upper()
            i += 1
        else:
            rebuiltPrompt += (' ' + words[i])
        i += 1
    paths = {
        'GGET':'routers/enrichr.txt',
        'SCRAPE':'routers/scrape.txt',
        'RAG':'routers/rag.txt',
        'TABLE':'routers/table.txt',
        'DATA':'routers/data.txt'
    }
    filepath = paths[route]
    add_sentence(filepath, rebuiltPrompt)
    

routeData = Route(
    name = 'DATA',
    utterances = read_prompts('routers/data.txt')
)

def getTableRouter():
    encoder = HuggingFaceEncoder()
    routes = [routeData]
    router = RouteLayer(encoder=encoder, routes=routes)    
    return router