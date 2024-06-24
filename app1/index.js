var os = require('os')
var http = require('http')

function handleRequest(req, res) {
  res.write('Hello World! ' + os.hostname())
  res.end()
}

const PROFILES_LIST = [
  {
    name: 'default',
    aws_access_key_id: 'DFKJBGEURIEJILWJDILJD',
    aws_secret_access_key: 'S89jBVY678ujhbat678UHU7y8uHGU78UJHIU678uUAVY6U7IyjjGu',
  },
  {
    name: 'sec',
    aws_access_key_id: 'SDFLKGJEWKUQI3JREIJDD',
    aws_secret_access_key: '78UJHIU678uUAVY6U7IyjjGuS89jBVY678ujhbat678UHU7y8uHGU',
  },
];

http.createServer(handleRequest).listen(3000)