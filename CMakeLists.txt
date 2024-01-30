cmake_minimum_required(VERSION 3.22)

project(Tinyhttpd C)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_executable(httpd httpd.c)
target_link_libraries(httpd PRIVATE pthread)

add_executable(client simpleclient.c)
