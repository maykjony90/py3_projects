# CMake generated Testfile for 
# Source directory: /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/modules/stitching
# Build directory: /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/modules/stitching
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_stitching "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/bin/opencv_test_stitching" "--gtest_output=xml:opencv_test_stitching.xml")
set_tests_properties(opencv_test_stitching PROPERTIES  LABELS "Main;opencv_stitching;Accuracy" WORKING_DIRECTORY "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/test-reports/accuracy")
add_test(opencv_perf_stitching "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/bin/opencv_perf_stitching" "--gtest_output=xml:opencv_perf_stitching.xml")
set_tests_properties(opencv_perf_stitching PROPERTIES  LABELS "Main;opencv_stitching;Performance" WORKING_DIRECTORY "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/test-reports/performance")
add_test(opencv_sanity_stitching "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/bin/opencv_perf_stitching" "--gtest_output=xml:opencv_perf_stitching.xml" "--perf_min_samples=1" "--perf_force_samples=1" "--perf_verify_sanity")
set_tests_properties(opencv_sanity_stitching PROPERTIES  LABELS "Main;opencv_stitching;Sanity" WORKING_DIRECTORY "/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/test-reports/sanity")
