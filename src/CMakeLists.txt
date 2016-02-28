cmake_minimum_required(VERSION 2.6)

project(main)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BULID_TYPE "Debug")
endif()

set(CMAKE_CXX_FLAGS "-g -std=c++11")

set(CMAKE_CXX_FLAGS_DEBUG "-O0")
set(CMAKE_CXX_FLAGS_RELEASE "-O2 -finline-limit=1000 -DNDEBUG")

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

aux_source_directory(./lib DIR_LIB_SRCS)
add_library (mysqlapi SHARED ${DIR_LIB_SRCS})

LINK_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR} DIR_SRCS)

add_executable(arbitrage ${DIR_SRCS})
target_link_libraries(arbitrage -lpthread -lcurl -lglog -lmysqlapi)
add_dependencies(arbitrage mysqlapi)
