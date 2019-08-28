from flask import Flask
from flask_restplus import Api, Resource
from werkzeug.datastructures import FileStorage
from extractor import reader
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app, title='simple api to prase logs', validate=True)

log_reader = api.parser()
log_reader.add_argument('log_file', location='files', type=FileStorage , required=True,help = "Log file in specified format")

@api.route('/upload')
@api.expect(log_reader)
class uploadFile(Resource):
    def post(self):
        try:
            arg = log_reader.parse_args()
            logger.info("Parsing argument sucessfull.")
        except Exception as e:
            logger.critical('Failed to Parse argument.')
            logger.error('For detalied error check this: ')
            logger.error(e)    
        final = reader(arg['log_file'].readlines())
        #print(final)
        return final




if __name__ == "__main__":
    app.run(debug=False,port = 1212)
