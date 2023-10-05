from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/start', methods=['GET'])
def start_energy_management():
    try:
        # Replace this with your actual energy management code
        # For demonstration purposes, we'll print numbers from 1 to 10
        for i in range(1, 11):
            print(i)
        
        # Return a success message
        return jsonify({"message": "Energy management started."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error response if something goes wrong

if __name__ == '__main__':
    app.run(debug=True)
