class Util:
    # ANSI escape codes for text colors
    COLOR_GREEN = "\033[92m"
    COLOR_YELLOW = "\033[93m"
    
    COLOR_RESET = "\033[0m"
    

    # Print text with color

    def  print_error(text):
     COLOR_RED = "\033[91m"
     print(COLOR_RED + text)
     

    def  print_success(text):
     COLOR_BLUE = "\033[94m"
     print(COLOR_BLUE + text)
     
