import sys

sys.path.append("..")  # allows importing everything from utils

class Solution:
    def towerofhanoi(self, n: int, src: str, helper: str, dest: str) -> None:
        
        # Base case
        if n == 1:
            print(f"Move disk {n} from {src} to {dest}")
            return
        
        self.towerofhanoi(n - 1, src, dest, helper) # Step 1
        print(f"Move disk {n} from {src} to {dest}") # Step 2
        self.towerofhanoi(n - 1, helper, src, dest) # Step 3
