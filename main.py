import os
import uvicorn

if __name__ == '__main__':
    debug = False
    if os.environ['APP_ENVIRONMENT'].lower() != 'master':
        debug = True

    uvicorn.run('api:app', host='0.0.0.0', port=7878, debug=debug, reload=debug)
