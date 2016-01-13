Name:           ros-indigo-ompl-visual-tools
Version:        2.3.2
Release:        0%{?dist}
Summary:        ROS ompl_visual_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ompl_visual_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-graph-msgs
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-moveit-planners-ompl
Requires:       ros-indigo-moveit-visual-tools
Requires:       ros-indigo-ompl >= 0.14.0
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-graph-msgs
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-moveit-planners-ompl
BuildRequires:  ros-indigo-moveit-visual-tools
BuildRequires:  ros-indigo-ompl >= 0.14.0
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-visualization-msgs

%description
Rviz 3-D visualizer for planning algorithms implemented with the Open Motion
Planning Library (OMPL)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jan 13 2016 Dave Coleman <davetcoleman@gmail.com> - 2.3.2-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Dave Coleman <davetcoleman@gmail.com> - 2.3.1-0
- Autogenerated by Bloom

* Sat Dec 05 2015 Dave Coleman <davetcoleman@gmail.com> - 2.3.0-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Dave Coleman <davetcoleman@gmail.com> - 2.2.1-0
- Autogenerated by Bloom

* Fri Oct 31 2014 Dave Coleman <davetcoleman@gmail.com> - 2.2.0-0
- Autogenerated by Bloom

* Mon Aug 11 2014 Dave Coleman <davetcoleman@gmail.com> - 2.1.1-0
- Autogenerated by Bloom

* Fri Aug 08 2014 Dave Coleman <davetcoleman@gmail.com> - 2.1.0-0
- Autogenerated by Bloom

* Thu Aug 07 2014 Dave Coleman <davetcoleman@gmail.com> - 2.0.1-0
- Autogenerated by Bloom

