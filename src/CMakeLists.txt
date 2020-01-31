file(GLOB_RECURSE sources
    "*.c"
    "*.cpp"
)

add_executable(createsamples ${sources})

# Link to math library if compiler is gnu
if ("${CMAKE_C_COMPILER_ID}" STREQUAL "GNU")
    list(APPEND libraries m)
endif()

# Link to user libraries (if there are any)
if(libraries)
    target_link_libraries(createsamples ${libraries})
endif()

target_link_libraries(createsamples ${OpenCV_LIBS})

install( TARGETS createsamples
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)
