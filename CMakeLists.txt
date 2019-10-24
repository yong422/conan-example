
CMAKE_MINIMUM_REQUIRED (VERSION 3.2)

# cmake 에서 conan install 을 사용하기 위한 conan.cmake 파일을 확인, download 한다.
IF ( NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake" )
  MESSAGE ( STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan" )
# FILE ( DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/master/conan.cmake"
  FILE ( DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/v0.13/conan.cmake"
                  "${CMAKE_BINARY_DIR}/conan.cmake")
ENDIF ()

INCLUDE ( ${CMAKE_BINARY_DIR}/conan.cmake )
# localtime 을 대체하기 위한 google c++ cctz
# BUILD missing 옵션을 추가 할 경우 package 의 build 가 필요하면 build
# BUILD all 옵션일 경우 매번 빌드하는 문제.
conan_cmake_run ( REQUIRES cctz/2.2@bincrafters/stable BASIC_SETUP BUILD missing)
# google c++ unittest framework
conan_cmake_run ( REQUIRES gtest/1.8.1@bincrafters/stable BASIC_SETUP BUILD missing)
# conan 을 이용한 라이브러리 빌드 및 설치가 완료된 후
# 빌드된 라이브러리 경로, 헤더 경로의 참조를 위하여 buildinfo 를 include 한다.
INCLUDE ( ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake )


# 사용 ex
ADD_LIBRARY ( libgtest STATIC IMPORTED GLOBAL )

# googletest header directory 추가.
INCLUDE_DIRECTORIES ( ${CONAN_INCLUDE_DIRS_GTEST} )
# libgtest.a 를 연결 한다.
SET_TARGET_PROPERTIES( libgtest
                      PROPERTIES
                      IMPORTED_LOCATION ${CONAN_LIB_DIRS_GTEST}/libgtestd.a )