import random
import string
import time
from datetime import datetime

class RandomStringGenerator:
    def __init__(self):
        # Generate and store a random string on startup
        self.random_string = self._generate_random_string()
    
    def _generate_random_string(self, length=20):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))
    
    def run(self):
        while True:
            # Get current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Print the stored string with timestamp
            print(f"{timestamp}: {self.random_string}")
            
            # Wait for 5 seconds
            time.sleep(5)

if __name__ == "__main__":
    generator = RandomStringGenerator()
    generator.run()