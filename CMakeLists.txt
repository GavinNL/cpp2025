cmake_minimum_required(VERSION 3.11)

project(cpp20205)


add_library( ${PROJECT_NAME}_coverage INTERFACE)
add_library( ${PROJECT_NAME}::coverage ALIAS ${PROJECT_NAME}_coverage)

if(CMAKE_COMPILER_IS_GNUCC OR CMAKE_COMPILER_IS_GNUCXX)

    target_compile_options(${PROJECT_NAME}_coverage
                                INTERFACE
                                    --coverage -g -O0 -fprofile-arcs -ftest-coverage)

    target_link_libraries( ${PROJECT_NAME}_coverage
                            INTERFACE --coverage -g -O0 -fprofile-arcs -ftest-coverage)



    add_custom_target(coverage
        COMMAND rm -rf coverage
        COMMAND mkdir -p coverage
        #COMMAND ${CMAKE_MAKE_PROGRAM} test
        #COMMAND gcovr . -r ${CMAKE_SOURCE_DIR} --html-details --html -o coverage/index.html -e ${CMAKE_SOURCE_DIR}/test/third_party;
        COMMAND gcovr . -r ${CMAKE_SOURCE_DIR} --xml -o coverage/report.xml -e ${CMAKE_SOURCE_DIR}/third_party;
        COMMAND gcovr . -r ${CMAKE_SOURCE_DIR} --html-details --html -o coverage/report.html -e ${CMAKE_SOURCE_DIR}/third_party;
        COMMAND gcovr . -r ${CMAKE_SOURCE_DIR} -o coverage/report.txt -e ${CMAKE_SOURCE_DIR}/third_party;
        COMMAND cat coverage/report.txt

        #COMMAND lcov --no-external --capture --directory ${CMAKE_BINARY_DIR} --output-file coverage2.info
        #COMMAND genhtml coverage.info --output-directory lcov-report
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR} 
    )

endif()


add_executable(main main.cpp)


enable_testing()
add_subdirectory(test)
