cmake_minimum_required(VERSION 2.5)
project(ujudge)

#set(CMAKE_VERBOSE_MAKEFILE ON)
#set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/output)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/output)

set(BASE_CMAKE_C_FLAGS "-Wall -Werror -O2 -std=c99")
set(CMAKE_C_FLAGS "${BASE_CMAKE_C_FLAGS}")


file(GLOB SOURCE "src/*.cpp")
add_executable(ujudge ${SOURCE})
# target_link_libraries(ujudge pthread seccomp)


install(TARGETS ujudge  RUNTIME DESTINATION /judge)
