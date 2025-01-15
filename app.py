from flask import Flask, request, jsonify

app = Flask(__name__)

def create_palindrome(S):
    S = list(S)  # Convert the string to a list for mutability
    n = len(S)

    # Iterate from both ends toward the center
    for i in range(n // 2):
        left = i
        right = n - i - 1

        # Handle cases with '?' characters
        if S[left] == '?' and S[right] == '?':
            S[left] = S[right] = 'a'  # Replace both with 'a'
        elif S[left] == '?':
            S[left] = S[right]  # Mirror the right character to the left
        elif S[right] == '?':
            S[right] = S[left]  # Mirror the left character to the right
        elif S[left] != S[right]:
            return "NO"  # If characters don't match, it's impossible to form a palindrome

    # If the length is odd, replace the middle '?' if it exists
    if n % 2 == 1 and S[n // 2] == '?':
        S[n // 2] = 'a'

    return ''.join(S)

@app.route('/create_palindrome', methods=['POST'])
def palindrome_api():
    data = request.get_json()
    if not data or 'string' not in data:
        return jsonify({"error": "Invalid input, 'string' key is required"}), 400

    input_string = data['string']
    result = create_palindrome(input_string)
    return jsonify({"input": input_string, "palindrome": result})

if __name__ == '__main__':
    app.run(debug=True)
