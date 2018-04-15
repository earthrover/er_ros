cmake_minimum_required(VERSION 2.8.3)
project(earth_rover_internal)

find_package(Boost REQUIRED COMPONENTS thread)
find_package(catkin REQUIRED COMPONENTS message_generation rostime roscpp rosconsole roscpp_serialization)

include_directories(${catkin_INCLUDE_DIRS})
link_directories(${catkin_LIBRARY_DIRS})

catkin_package(CATKIN_DEPENDS message_runtime std_msgs)

macro(earth_rover T)
  add_executable(${T} ${T}/${T}.cpp)
  target_link_libraries(${T} ${catkin_LIBRARIES} ${Boost_LIBRARIES})
  add_dependencies(${T} earth_internal_gencpp)
  install(TARGETS ${T}
    RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
endmacro()

foreach(dir
    listener
    notify_connect
    talker
    )
  earth_rover(${dir})
endforeach()

install(DIRECTORY
  launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

