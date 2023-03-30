# Import the necessary modules.
import os, time
from pynput.keyboard import Key as KeyType, Listener
from queue import Queue

class Key:
    def __init__(self) -> None:
        pass
    
    # Define the function that will be called when a key is pressed.
    def on_press(self, key: KeyType) -> None:
        pass
    
    # Define the function that will be called when a key is released.
    def on_release(self, key: KeyType, queue: Queue) -> None:
        try:
            # Put the character key in the queue.
            queue.put(key.char)
        
        except AttributeError:
            # Put non-character keys in the queue.
            queue.put(key.name)
    
    def get_key(self, prompt_string: str) -> str:
        '''
        Prompts the user for a key.
        
        Args:
            prompt_string (str): A string representing the prompt to display to the user
            
        Returns:
            key (str): A key which the user pressed

        Examples:
            To prompt the user for a key and print the key that was pressed, use:

            >>> key = get_key("Press a key: ")
            >>> print("You pressed:", key)
        '''
        
        # Create a new queue object to hold the key value.
        key_queue = Queue()
        
        # Start a keyboard listener with the on_press and on_release functions.
        # Use a lambda function to pass the queue object to the on_release function.
        with Listener(on_press=self.on_press, on_release=lambda key: self.on_release(key, queue=key_queue)):
            # Print the prompt string to the console.
            # Use flush=True to ensure that the message is printed immediately.
            # Use end='' to make sure that the next print statement is on the same line.
            print(prompt_string, end='', flush=True)
            
            # Initialize the key value to None.
            key = None
            
            # Keep looping until a key value has been retrieved from the queue.
            while key is None:
                key = key_queue.get()
            
            # Return the key value to the calling function.
            return key
    
    # Defines function to get user input with a prompt string and returns user input string, only for keyboard
    def get_input_keyboard(self, prompt: str) -> str:
        """
        Prompts user for an input and then removes 'kqer' from the begining of the input.

        Args:
            prompt: A string representing the prompt to display to the user.

        Returns:
            A string representing the user's input.
        """
        
        # Prompts the user
        print(prompt, end='')

        # Gets input from prompt
        user_input = input('')
        user_input = user_input.split('r')

        if len(user_input) < 1:
            user_input = user_input[0]
        else:
            user_input = user_input[1]
        
        # Return the user input value to the calling function.
        return user_input

    # Defines function to get user input with a prompt string and returns user input string, only for mouse
    def get_input_mouse(self, prompt: str) -> str:
        """
        Prompts user for an input and then removes 'mqe' from the begining of the input.

        Args:
            prompt: A string representing the prompt to display to the user.

        Returns:
            A string representing the user's input.
        """
        
        # Prompts the user
        print(prompt, end='')

        # Gets input from prompt
        user_input = input('')
        user_input = user_input.split('e')

        if len(user_input) < 1:
            user_input = user_input[0]
        else:
            user_input = user_input[1]
        
        # Return the user input value to the calling function.
        return user_input
