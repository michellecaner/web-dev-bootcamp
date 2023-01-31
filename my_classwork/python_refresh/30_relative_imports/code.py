"""Python refresher course - Relative Imports Section"""

# import mymodule # an absolute import

from mymodule import divide # from the current folder, import the divide function

print("code.py", __name__)

# result is: 
# operator.py libs.operations.operator
# mylib.py libs.mylib
# mymodule.py mymodule
# code.py __main__

divide()
