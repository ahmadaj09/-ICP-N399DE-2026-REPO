# GUARDKEY PRO

![Python](https://img.shields.io/badge/Python-Password%20Security-blue)

GUARDKEY PRO is a Python-based password strength analysis tool that evaluates password quality and provides actionable security recommendations.

Developed by **AJ | Cybersecurity Enthusiast**

## Key Features

### Password Analysis
- **Strength Evaluation**: Determines the overall password strength level.
- **Entropy Calculation**: Estimates password randomness in bits.
- **Crack Time Estimation**: Approximates brute-force cracking time.

### Security Checks
- **Character Variety Detection**: Verifies uppercase, lowercase, digits, and symbols.
- **Common Password Detection**: Flags commonly used weak passwords.
- **Sequential Pattern Detection**: Detects patterns such as `123` and `abc`.
- **Repeated Character Detection**: Flags repeated characters such as `aaa`.
- **Keyboard Pattern Detection**: Detects keyboard sequences such as `qwerty`.

### Password Generation
- **Secure Password Generator**: Creates strong random passwords.
- **Custom Length Support**: Generates passwords with user-defined length.

### Reporting
- **Detailed Feedback**: Highlights strengths and weaknesses.
- **Security Recommendations**: Suggests concrete improvements.
- **Entropy and Crack Time Display**: Shows analysis metrics clearly.

### User Interface
- **Tkinter GUI**: Simple and user-friendly desktop interface.
- **Visual Strength Meter**: Color-based password strength indicator.
- **Clipboard Support**: Copies generated passwords instantly.

## Installation

### Prerequisites
- Python **3.6 or higher**
- `pip`

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/GUARDKEY-PRO.git
cd GUARDKEY-PRO

# Install dependencies
pip install -r requirements.txt
```

### Dependencies
- `pyperclip`
- `colorama`
- `pyfiglet`

## Usage

Run the application:

```bash
python main.py
```

### Steps
1. Launch the program.
2. Enter a password in the input field.
3. Click **Analyze**.
4. Review strength, entropy, crack-time estimate, and recommendations.
5. Optionally generate a secure password using the generator button.

## Screenshot

Main application interface:

`(Add screenshot here)`

## Project Structure

```text
GUARDKEY-PRO/
|
|-- main.py                 # Application entry point
|-- requirements.txt        # Python dependencies
|-- setup.py                # Package setup script
|-- README.md               # Project documentation
|-- LICENSE                 # MIT License
|
|-- src/                    # Core modules
|   |-- __init__.py
|   |-- password_analyzer.py
|   |-- entropy_calculator.py
|   |-- gui_interface.py
|   `-- utils.py
|
`-- tests/                  # Unit tests
    |-- __init__.py
    `-- test_analyzer.py
```

## Sample Analysis Output

```text
Password: P@ssw0rd!2025#Secure

Strength: Strong
Length: 19 characters
Entropy: 112.3 bits
Estimated Crack Time: 2.5 centuries

Feedback:
- Excellent character variety
- High entropy
- No common patterns detected
```

## Running Tests

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Author

**AJ**  
Cybersecurity Enthusiast and Python Developer

## Acknowledgements

Inspired by NIST password guidelines and modern password security practices.