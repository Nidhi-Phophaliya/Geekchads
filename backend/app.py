from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    
    # Basic validation: Check if required fields are present
    if not data.get('propertyId') or not data.get('ownerName'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    return jsonify({'message': 'Form submitted successfully', 'data': data}), 200

if __name__ == '__main__':
    app.run(debug=True)
