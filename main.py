import argparse
import os , sys
from datetime import datetime

now = datetime.now()

# current_time is for log and report name
current_time = now.strftime("%Y_%m_%d_%H_%M_%S")
print("Current Time =", current_time)
os.mkdir("logs/"+current_time)
os.mkdir("logs/"+current_time+"/img")

def process_command():
    parser = argparse.ArgumentParser()

    parser.add_argument('--case', '-c', type=str, default=False, help='note for jteam')

    return parser.parse_args()

def read_config_file(file_name):
    '''
    Read the given config file and output a config dict
    '''
    lines = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if str(line)[-1] == "\n":
                number = str(line)[:-1]
            else:
                number = str(line)[:]
            lines.append(number)

    config_dict = {}
    if "element" in file_name:
        for item in lines:
            if item != "":
                test_key = item.split(" = ")[0]
                test_value = item.split(" = ")[1]
                config_dict[test_key] = test_value
    else:
        for item in lines:
            if item != "" and "[" not in item:
                test_key = (item.replace(" ","")).split("=")[0]
                test_value = (item.replace(" ","")).split("=")[1]
                config_dict[test_key] = test_value
    return config_dict

def main():

    config_para = read_config_file("config/config.ini")
    print(config_para)
    element_para = read_config_file("config/elements.ini")
    print(element_para)

    cmd = "pytest " + config_para['case_folder']

    args = process_command()
    print(args)

    # If no -c option , the default args.case value is False
    if args.case:
        print(args.case)
        casename = args.case
        cmd = cmd + "/" + casename

    # Send pytest command vi os.system()
    cmd = cmd + " --log-file=logs/" + current_time + "/pytest.log --html=logs/" + current_time + "/pytest.html"
    #cmd = cmd + " --html=logs/" + current_time + "/pytest.html"
    print(cmd)

    #log_path = "logs/" + current_time + "/logger.log"

    ini_string = "log_folder = '{}'".format("logs/" + current_time) + "\n"
    ini_string = ini_string + "log_path = '{}'".format("logs/" + current_time + "/logger.log") + "\n"
    ini_string = ini_string + "img_path = '{}'".format("logs/" + current_time + "/img/") + "\n"
    ini_string = ini_string + "trd_path = '{}'".format("logs/" + current_time + "/trd.log") + "\n"
    ini_string = ini_string + "test_data_path = '{0}/test_data/'".format(os.path.dirname(os.path.realpath(__file__)))

    for k,v in config_para.items():
        ini_string = ini_string + "\n" + k + "=" +  '"' + v + '"'

    with open("libs/ini.py", "w") as ini_py:
        ini_py.write(ini_string)

    el_string = ""
    for k,v in element_para.items():
        el_string = el_string + "\n" + k + "=" +  "'" + v + "'"

    with open("libs/elements.py", "w") as elements_py:
        elements_py.write(el_string)

    # get and set environment variables via os.environ()
    # set the root folder as PYTHONPATH
    os.environ["PYTHONPATH"] = "."
    print("sys.path : {}".format(sys.path))

    os.system(cmd)


if __name__ == '__main__':
    main()
