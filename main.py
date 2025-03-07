from flask import Flask, request, jsonify

app = Flask(__name__)

# Store reservations in memory for simplicity
# In a real application, you would use a database
reservations = {}

@app.route('/book', methods=['POST'])
def book_reservation():
    # Get data from request
    data = request.get_json()
    print("[POST REQUEST]: \n",data)
    
    # Check if all required fields are present
    if not all(key in data for key in ['name', 'time']):
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400
    
    name = data['name']
    time = data['time']
    
    # Check if the reservation is already booked
    if time in reservations:
        return jsonify({
            'status': 'failed',
            'message': 'This reservation is already booked',
            'booked': True
        }), 409
    
    # If not booked, add the reservation
    reservations[time] = name
    
    return jsonify({
        'status': 'success',
        'message': f'Reservation booked for {name}',
        'booked': True
    }), 201

if __name__ == '__main__':
    app.run(debug=True)