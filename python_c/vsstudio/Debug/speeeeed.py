import pybind11module as pbm
# modules inside c++ are billion() just use it as pbm.billion() int python it will run a loop for billion 
# modules second is million() again just a million loop
# module third is mil(requires a number) adds a million to your given number
print(pbm.billion()) # C++ counting to billion and returning the number
