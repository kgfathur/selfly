cmake_minimum_required(VERSION 2.8.12)

project(captures)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(captures captures.cpp)
target_link_libraries(captures ${OpenCV_LIBS})
