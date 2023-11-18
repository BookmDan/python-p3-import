from .module1 import function1  
from .. import module3  

def main():
    function1()
    module3.function1()

if __name__ == "__main__":
    main()