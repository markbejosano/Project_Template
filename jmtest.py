import os
if len(sys.argv)==0:
    print("please pass folder name as argument")
    exit()
foldername=sys.argv[1]
y = os.path.abspath(foldername+"/HTTPRequest.jmx")
z = y.replace('\\','\\\\') 

initial_path = "jmeter -Jjmeter.save.saveservice.output_format=xml -n -t"
command = "-l HTTPRequest.jtl"


final = initial_path + " " + z + " " + command


os.system(final)
