cmake_minimum_required(VERSION 2.8.12)

project(saveFrame)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(saveFrame saveFrame.cpp)
target_link_libraries(saveFrame ${OpenCV_LIBS})
