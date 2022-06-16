# Air Labels
# A tool to support labeling operations of machine learning projects.

import uvicorn
from airlabels.webservice.setup import server_factory


def airlabels_setup():
    return server_factory(debug=True)


if __name__ == '__main__':
    uvicorn.run(airlabels_setup(), host="127.0.0.1", port=8000, log_level="debug")
