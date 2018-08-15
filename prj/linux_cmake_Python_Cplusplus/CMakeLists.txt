PROJECT(Python_Cplusplus)
CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

# 支持C++11
SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -Wall -O2 -std=c11")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}  -g -Wall -O2 -std=c++11")
# 支持C++14, when gcc version > 5.1, use -std=c++14 instead of c++1y
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}  -g -Wall -O2 -std=c++1y")

MESSAGE(STATUS "project source dir: ${PROJECT_SOURCE_DIR}")
SET(PATH_SRC_FILES ${PROJECT_SOURCE_DIR}/./../../Demo/Python_Cplusplus)
MESSAGE(STATUS "path src files: ${PATH_SRC_FILES}")

# 指定头文件的搜索路径
INCLUDE_DIRECTORIES(${PATH_SRC_FILES})

# 递归查询所有匹配的文件:*.cpp
FILE(GLOB_RECURSE CPP_LIST ${PATH_SRC_FILES}/*.cpp)
FILE(GLOB_RECURSE C_LIST ${PATH_SRC_FILES}/*.c)
MESSAGE(STATUS "cpp list: ${CPP_LIST}")

ADD_LIBRARY(Test_DLL_1 SHARED  ${CPP_LIST} ${C_LIST})
TARGET_LINK_LIBRARIES(Test_DLL_1 pthread)

