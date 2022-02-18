# https://www.freecodecamp.org/news/if-name-main-python-example/
# Python module to import 
import banco
import factorial
import switch_demo

 #print("File two __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
    print (switch_demo.numbers_to_months(2))
else:
   print("File two executed when imported")


 

