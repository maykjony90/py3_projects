# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build

# Include any dependencies generated for this target.
include samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/depend.make

# Include the progress variables for this target.
include samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/progress.make

# Include the compile flags for this target's objects.
include samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/flags.make

samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o: samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/flags.make
samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o: ../samples/cpp/tutorial_code/photo/seamless_cloning/cloning_demo.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o"
	cd /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/samples/cpp && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o -c /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/samples/cpp/tutorial_code/photo/seamless_cloning/cloning_demo.cpp

samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.i"
	cd /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/samples/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/samples/cpp/tutorial_code/photo/seamless_cloning/cloning_demo.cpp > CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.i

samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.s"
	cd /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/samples/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/samples/cpp/tutorial_code/photo/seamless_cloning/cloning_demo.cpp -o CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.s

samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o.requires:

.PHONY : samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o.requires

samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o.provides: samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o.requires
	$(MAKE) -f samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/build.make samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o.provides.build
.PHONY : samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o.provides

samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o.provides.build: samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o


# Object files for target tutorial_cloning_demo
tutorial_cloning_demo_OBJECTS = \
"CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o"

# External object files for target tutorial_cloning_demo
tutorial_cloning_demo_EXTERNAL_OBJECTS =

bin/cpp-tutorial-cloning_demo: samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o
bin/cpp-tutorial-cloning_demo: samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/build.make
bin/cpp-tutorial-cloning_demo: /usr/lib/x86_64-linux-gnu/libGLU.so
bin/cpp-tutorial-cloning_demo: /usr/lib/x86_64-linux-gnu/libGL.so
bin/cpp-tutorial-cloning_demo: /usr/lib/x86_64-linux-gnu/libtbb.so
bin/cpp-tutorial-cloning_demo: 3rdparty/ippicv/ippicv_lnx/lib/intel64/libippicv.a
bin/cpp-tutorial-cloning_demo: lib/libopencv_shape.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_stitching.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_superres.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_videostab.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_viz.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_objdetect.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_photo.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_calib3d.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_features2d.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_flann.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_highgui.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_ml.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_videoio.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_imgcodecs.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_video.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_imgproc.so.3.2.0
bin/cpp-tutorial-cloning_demo: lib/libopencv_core.so.3.2.0
bin/cpp-tutorial-cloning_demo: /usr/lib/x86_64-linux-gnu/libGLU.so
bin/cpp-tutorial-cloning_demo: /usr/lib/x86_64-linux-gnu/libGL.so
bin/cpp-tutorial-cloning_demo: samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/cpp-tutorial-cloning_demo"
	cd /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/samples/cpp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tutorial_cloning_demo.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/build: bin/cpp-tutorial-cloning_demo

.PHONY : samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/build

samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/requires: samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/tutorial_code/photo/seamless_cloning/cloning_demo.cpp.o.requires

.PHONY : samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/requires

samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/clean:
	cd /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/samples/cpp && $(CMAKE_COMMAND) -P CMakeFiles/tutorial_cloning_demo.dir/cmake_clean.cmake
.PHONY : samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/clean

samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/depend:
	cd /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/samples/cpp /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/samples/cpp /home/jony/Documents/python_projects/py3projects/learning_python/udacity_self_driving_car/OpenCV/build/samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : samples/cpp/CMakeFiles/tutorial_cloning_demo.dir/depend

