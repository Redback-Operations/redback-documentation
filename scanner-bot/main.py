import logging
import json
from scanner import SensitiveDataScanner

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    logging.info("Starting the sensitive data scan...")
    
    scanner = SensitiveDataScanner()
    
    try:
        # Run the scan and capture results
        results = scanner.scan_repository("data/sample.txt")  # Returns the scan result dictionary

        logging.info("Scan completed successfully.")
        
        # Print result summary
        if any(results.values()):
            print("\n📄 Scan Results:\n")
            print(json.dumps(results, indent=4))
        else:
            print("\n✅ No sensitive data found in the file.")
    
    except Exception as e:
        logging.error(f"Error during scan: {e}")
