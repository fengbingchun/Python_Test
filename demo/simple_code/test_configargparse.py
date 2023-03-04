import configargparse # pip install configargparse

# Blog: https://blog.csdn.net/fengbingchun/article/details/129333101

def config_file_parse():
    #parser = configargparse.ArgumentParser(default_config_files=["test.conf"])
    parser = configargparse.ArgumentParser() # Aliases: ArgParser
    parser.add_argument("-c", "--config", required=True, is_config_file=True, help="config file path") # Aliases: add, add_arg
    parser.add_argument("--csdn_addr", type=str, default="csdn", help="csdn addr")
    parser.add_argument("--github_addr", type=str, default="github", help="github addr") # Aliases: add, add_arg
    parser.add_argument("--beijing", type=bool, default=False, help="work addr1")
    parser.add_argument("--jinan", type=bool, default=True, help="work addr2")
    parser.add_argument("--tianjin", type=bool, default=True, help="work addr3")
    parser.add_argument("--age", type=int, default=2, help="age")
    parser.add_argument("--height", type=float, default=1.7, help="height")
    parser.add_argument("--package", type=str, help="package pos")

    options = parser.parse_args() # Aliases: parse

    #print("======================================")
    #print(parser.format_help())
    #print("======================================")
    print(parser.format_values())
    #print("======================================")

    print("csdn addr:", options.csdn_addr)
    print("github addr:", options.github_addr)

    if options.beijing:
        print("Your work address: BeiJing")

    if options.age > 18:
        print("You are an adult, age:", options.age)

    if options.height:
        print("Your height:", options.height)

    if options.package == "./test_package":
        print("package pos:", options.package)

if __name__=='__main__':
    config_file_parse()
    print("test finish")
