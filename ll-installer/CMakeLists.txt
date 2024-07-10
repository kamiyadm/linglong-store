set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
add_definitions("-DQT_MESSAGELOGCONTEXT")

find_package(PkgConfig REQUIRED)
find_package(Qt5Core REQUIRED)
find_package(Qt5DBus REQUIRED)
find_package(Qt5 REQUIRED COMPONENTS Widgets)

set(LINK_LIBS
    ${Qt_LIBS}
    stdc++)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

add_executable(ll-installer
               installer-dialog.cpp
               main.cpp)

target_link_libraries(ll-installer
                      PRIVATE ${LINK_LIBS}
                      PRIVATE Qt5::Widgets)

install(TARGETS ll-installer
        RUNTIME
        DESTINATION bin)

install(FILES space.linglong.Installer.desktop
        DESTINATION ${CMAKE_INSTALL_PREFIX}/share/applications)
