# Install script for directory: /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/modules/shape

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

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "libs")
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so.3.2.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so.3.2"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "/usr/local/lib")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY OPTIONAL FILES
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/lib/libopencv_shape.so.3.2.0"
    "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/lib/libopencv_shape.so.3.2"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so.3.2.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so.3.2"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/lib:"
           NEW_RPATH "/usr/local/lib")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dev")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so"
         RPATH "/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/lib/libopencv_shape.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so"
         OLD_RPATH "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/lib:"
         NEW_RPATH "/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libopencv_shape.so")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dev")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv2" TYPE FILE OPTIONAL FILES "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/modules/shape/include/opencv2/shape.hpp")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dev")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv2/shape" TYPE FILE OPTIONAL FILES "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/modules/shape/include/opencv2/shape/shape_transformer.hpp")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dev")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv2/shape" TYPE FILE OPTIONAL FILES "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/modules/shape/include/opencv2/shape/shape_distance.hpp")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dev")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv2/shape" TYPE FILE OPTIONAL FILES "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/modules/shape/include/opencv2/shape/emdL1.hpp")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dev")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv2/shape" TYPE FILE OPTIONAL FILES "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/modules/shape/include/opencv2/shape/hist_cost.hpp")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dev")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv2/shape" TYPE FILE OPTIONAL FILES "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/modules/shape/include/opencv2/shape/shape.hpp")
endif()
