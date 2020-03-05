file(GLOB_RECURSE sources
    "*.c"
    "*.cpp"
)

add_executable(createsamples ${sources})
add_executable(traincascade ${sources})

# Link to math library if compiler is gnu
if ("${CMAKE_C_COMPILER_ID}" STREQUAL "GNU")
    list(APPEND libraries m)
endif()

# Link to user libraries (if there are any)
if(libraries)
    target_link_libraries(createsamples ${libraries})
    target_link_libraries(traincascade ${libraries})
endif()

target_link_libraries(createsamples ${OpenCV_LIBS})
target_link_libraries(traincascade ${OpenCV_LIBS})
target_link_libraries(createsamples
                        opencv_core
                        opencv_imgproc 
                        opencv_objdetect
                        opencv_imgcodecs
                        opencv_highgui 
                        opencv_calib3d 
                        opencv_features2d 
                        opencv_videoio)

install( TARGETS traincascade
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)
install( TARGETS createsamples
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)
