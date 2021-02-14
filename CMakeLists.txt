cmake_minimum_required(VERSION 3.17)
enable_language(Fortran)
project(FFItest CXX Fortran)
set_source_files_properties(test.f08 PROPERTIES LANGUAGE Fortran)
# set(CMAKE_CXX_STANDARD 20)

add_library(test SHARED
        test.f08
        )
add_executable(
        FFItest
        main.cpp
        test.h)
target_link_libraries(FFItest test)
