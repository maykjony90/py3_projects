# Install script for directory: /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dev")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv" TYPE FILE FILES
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/cxmisc.h"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/cvwimage.h"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/cxeigen.hpp"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/cvaux.hpp"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/cv.hpp"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/cxcore.h"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/cv.h"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/cxcore.hpp"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/cvaux.h"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/ml.h"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv/highgui.h"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dev")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv2" TYPE FILE FILES "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/include/opencv2/opencv.hpp")
endif()

