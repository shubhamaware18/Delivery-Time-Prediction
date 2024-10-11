import os, sys

# Custom Exception class inheriting from the base Exception class
class CustomException(Exception):
    
    def __init__(self, error_message: Exception, error_details: tuple):
        """
        Constructor to initialize the custom exception.
        Args:
            error_message (Exception): The original exception message that was raised.
            error_details (tuple): A tuple containing error details from sys.exc_info(), 
                                   including the exception type, value, and traceback object.
        """
        # Generate a detailed error message with the help of a static method
        self.error_message = self.get_detailed_error_message(error_message=error_message, 
                                                             error_details=error_details)
    
    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_details: tuple) -> str:
        """
        Generates a detailed error message including the filename, line numbers,
        and the original exception message.
        Args:
            error_message (Exception): The original exception message.
            error_details (tuple): A tuple containing the exception traceback details.
        
        Returns:
            str: A formatted detailed error message.
        """
        # Extract traceback from error_details (sys.exc_info())
        _, _, exce_tb = error_details

        # Line number where the exception was raised
        error_occurrence_line_number = exce_tb.tb_lineno
        
        # Line number where the exception block is handled (i.e., where the exception object was created)
        exception_block_line_number = exce_tb.tb_frame.f_lineno

        # The filename where the error occurred
        file_name = exce_tb.tb_frame.f_code.co_filename

        # Format the detailed error message to include the file name, line numbers, and the exception message
        detailed_message = (f"Error occurred in script: [{file_name}] at line [{error_occurrence_line_number}] "
                            f"with exception block at line [{exception_block_line_number}]. "
                            f"Error message: [{error_message}].")
        
        return detailed_message
    
    def __str__(self):
        """
        Returns the detailed error message when the exception object is converted to a string.
        """
        return self.error_message
    
    def __repr__(self):
        """
        Returns the string representation of the custom exception object.
        Useful for debugging purposes.
        """
        return f"{self.__class__.__name__}('{self.error_message}')"
