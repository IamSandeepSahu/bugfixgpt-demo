# BugFixGPT Demo Repository

This repository contains a sample Flask service with intentional bugs to demonstrate the functionality of BugFixGPT, an AI-powered automated debugging assistant.

## How It Works

1. When this service encounters an error, it logs detailed error information.
2. The BugFixGPT system (running separately) monitors these logs for errors.
3. When an error is detected, BugFixGPT:
   - Analyzes the error using AWS Bedrock (Claude/Llama)
   - Generates a fix for the bug
   - Creates a PR in this repository with the proposed fix

## Demo Service

The sample service contains several intentional bugs to demonstrate the system:

- **Division by Zero Bug**: Accessing the `/api/divide` endpoint will trigger a division by zero error.

## Running the Service

If you want to run the service locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the service
python app.py
```

The service will be available at http://localhost:5000.

## Integration with BugFixGPT

This repository works with the BugFixGPT system which:

1. Monitors the service logs
2. Detects errors in real-time
3. Analyzes the code to find the bug
4. Creates a Pull Request with the fix

To see the full BugFixGPT system, visit the main repository at [your-link-here].

## License

MIT
