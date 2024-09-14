import multiprocessing
import time

class TimeoutRunner:
    def __init__(self):
        self.result = multiprocessing.Manager().list([None])  # Shared list for result
        self.exception = multiprocessing.Manager().list([None])  # Shared list for exceptions

    def wrapper(self, func):
        try:
            self.result[0] = func()  # Run the target function
        except Exception as e:
            self.exception[0] = e  # Capture any exceptions raised by the function

    def run_with_timeout(self, func, timeout, fallback):
        process = multiprocessing.Process(target=self.wrapper, args=(func,))
        process.start()
        process.join(timeout)  # Wait for process completion or timeout

        if process.is_alive():  # Check if the process exceeded the timeout
            process.terminate()  # Terminate the process
            process.join()  # Ensure the process has fully terminated
            print("Process timed out. Operation isn't successful.")
            fallback()
            return None

        if self.exception[0]:
            raise self.exception[0]  # Raise any captured exceptions

        return self.result[0]  # Return the result if successful

# Define a function that takes some time to execute
def long_running_functionx():
    return "Completed successfully"


# Define a fallback function to run if the timeout occurs
def fallback_function():
    print("Fallback function executed.")

if __name__ == '__main__':
    # Create an instance of TimeoutRunner
    runner = TimeoutRunner()

    # Run the function with a timeout of 2 seconds
    result = runner.run_with_timeout(long_running_functionx, 2, fallback_function)

    print("Result:", result)