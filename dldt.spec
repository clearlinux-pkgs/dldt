#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dldt
Version  : 2018.r3
Release  : 20
URL      : https://github.com/opencv/dldt/archive/2018_R3.tar.gz
Source0  : https://github.com/opencv/dldt/archive/2018_R3.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 MIT
Requires: dldt-data = %{version}-%{release}
Requires: dldt-lib = %{version}-%{release}
Requires: dldt-license = %{version}-%{release}
Requires: networkx
Requires: numpy
Requires: onnx
Requires: opencv-python
Requires: protobuf
Requires: pugixml
Requires: tensorflow
BuildRequires : Cython
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : googletest
BuildRequires : googletest-dev
BuildRequires : mkl-dnn-dev
BuildRequires : openblas
BuildRequires : opencv
BuildRequires : opencv-dev
BuildRequires : opencv-python
BuildRequires : pugixml-dev
BuildRequires : python3
Patch1: 0001-Build-fixes.patch

%description
The Google Mock class generator is an application that is part of cppclean.
visit http://code.google.com/p/cppclean/

%package data
Summary: data components for the dldt package.
Group: Data

%description data
data components for the dldt package.


%package dev
Summary: dev components for the dldt package.
Group: Development
Requires: dldt-lib = %{version}-%{release}
Requires: dldt-data = %{version}-%{release}
Provides: dldt-devel = %{version}-%{release}

%description dev
dev components for the dldt package.


%package lib
Summary: lib components for the dldt package.
Group: Libraries
Requires: dldt-data = %{version}-%{release}
Requires: dldt-license = %{version}-%{release}

%description lib
lib components for the dldt package.


%package license
Summary: license components for the dldt package.
Group: Default

%description license
license components for the dldt package.


%prep
%setup -q -n dldt-2018_R3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540422441
pushd inference-engine
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake .. -DENABLE_CLDNN=0 \
-DENABLE_INTEL_OMP=0 \
-DENABLE_OPENCV=0 \
-DENABLE_CLDNN_BUILD=1 \
-DENABLE_SAMPLES_CORE=1 \
-DENABLE_PYTHON_BINDINGS=1 \
-DINSTALL_GMOCK=0 \
-DINSTALL_GTEST=0 \
-DBUILD_GMOCK=1 \
-DBUILD_GTEST=0
make  %{?_smp_mflags} VERBOSE=1
popd

popd
%install
export SOURCE_DATE_EPOCH=1540422441
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dldt
cp LICENSE %{buildroot}/usr/share/package-licenses/dldt/LICENSE
cp inference-engine/samples/thirdparty/gflags/COPYING.txt %{buildroot}/usr/share/package-licenses/dldt/inference-engine_samples_thirdparty_gflags_COPYING.txt
cp inference-engine/tests/libs/gtest/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/dldt/inference-engine_tests_libs_gtest_googlemock_LICENSE
cp inference-engine/tests/libs/gtest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/dldt/inference-engine_tests_libs_gtest_googlemock_scripts_generator_LICENSE
cp inference-engine/tests/libs/gtest/googletest/LICENSE %{buildroot}/usr/share/package-licenses/dldt/inference-engine_tests_libs_gtest_googletest_LICENSE
cp inference-engine/thirdparty/clDNN/common/boost/1.64.0/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/dldt/inference-engine_thirdparty_clDNN_common_boost_1.64.0_LICENSE_1_0.txt
cp inference-engine/thirdparty/clDNN/common/googletest-fused/License.txt %{buildroot}/usr/share/package-licenses/dldt/inference-engine_thirdparty_clDNN_common_googletest-fused_License.txt
cp inference-engine/thirdparty/clDNN/common/khronos_ocl_clhpp/LICENSE.txt %{buildroot}/usr/share/package-licenses/dldt/inference-engine_thirdparty_clDNN_common_khronos_ocl_clhpp_LICENSE.txt
cp inference-engine/thirdparty/mkl-dnn/LICENSE %{buildroot}/usr/share/package-licenses/dldt/inference-engine_thirdparty_mkl-dnn_LICENSE
cp inference-engine/thirdparty/mkl-dnn/src/cpu/xbyak/COPYRIGHT %{buildroot}/usr/share/package-licenses/dldt/inference-engine_thirdparty_mkl-dnn_src_cpu_xbyak_COPYRIGHT
cp inference-engine/thirdparty/mkl-dnn/tests/gtests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/dldt/inference-engine_thirdparty_mkl-dnn_tests_gtests_gtest_LICENSE
pushd inference-engine
pushd clr-build
%make_install
popd
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/pugiconfig.hpp
%exclude /usr/include/pugixml.hpp
%exclude /usr/lib64/cmake/pugixml/pugixml-config-relwithdebinfo.cmake
%exclude /usr/lib64/cmake/pugixml/pugixml-config.cmake
%exclude /usr/lib64/libgflags_nothreads.so
%exclude /usr/lib64/libpugixml.so
%exclude /usr/lib64/pkgconfig/gflags.pc
/usr/include/inference_engine/ie_allocator.hpp
/usr/include/inference_engine/ie_api.h
/usr/include/inference_engine/ie_blob.h
/usr/include/inference_engine/ie_common.h
/usr/include/inference_engine/ie_data.h
/usr/include/inference_engine/ie_device.hpp
/usr/include/inference_engine/ie_error.hpp
/usr/include/inference_engine/ie_extension.h
/usr/include/inference_engine/ie_icnn_net_reader.h
/usr/include/inference_engine/ie_icnn_network.hpp
/usr/include/inference_engine/ie_icnn_network_stats.hpp
/usr/include/inference_engine/ie_iexecutable_network.hpp
/usr/include/inference_engine/ie_iextension.h
/usr/include/inference_engine/ie_ihetero_plugin.hpp
/usr/include/inference_engine/ie_iinfer_request.hpp
/usr/include/inference_engine/ie_imemory_state.hpp
/usr/include/inference_engine/ie_input_info.hpp
/usr/include/inference_engine/ie_layers.h
/usr/include/inference_engine/ie_layouts.h
/usr/include/inference_engine/ie_locked_memory.hpp
/usr/include/inference_engine/ie_plugin.hpp
/usr/include/inference_engine/ie_plugin_config.hpp
/usr/include/inference_engine/ie_plugin_dispatcher.hpp
/usr/include/inference_engine/ie_plugin_ptr.hpp
/usr/include/inference_engine/ie_precision.hpp
/usr/include/inference_engine/ie_preprocess.hpp
/usr/include/inference_engine/ie_primitive_info.hpp
/usr/include/inference_engine/ie_tensor_info.hpp
/usr/include/inference_engine/ie_utils.hpp
/usr/include/inference_engine/ie_version.hpp
/usr/include/inference_engine/inference_engine.hpp
/usr/lib64/libinference_engine.so

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/libgflags_nothreads.so.2.2
%exclude /usr/lib64/libgflags_nothreads.so.2.2.1
%exclude /usr/lib64/libpugixml.so.1
%exclude /usr/lib64/libpugixml.so.1.7
/usr/lib64/libinference_engine.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dldt/LICENSE
/usr/share/package-licenses/dldt/inference-engine_samples_thirdparty_gflags_COPYING.txt
/usr/share/package-licenses/dldt/inference-engine_tests_libs_gtest_googlemock_LICENSE
/usr/share/package-licenses/dldt/inference-engine_tests_libs_gtest_googlemock_scripts_generator_LICENSE
/usr/share/package-licenses/dldt/inference-engine_tests_libs_gtest_googletest_LICENSE
/usr/share/package-licenses/dldt/inference-engine_thirdparty_clDNN_common_boost_1.64.0_LICENSE_1_0.txt
/usr/share/package-licenses/dldt/inference-engine_thirdparty_clDNN_common_googletest-fused_License.txt
/usr/share/package-licenses/dldt/inference-engine_thirdparty_clDNN_common_khronos_ocl_clhpp_LICENSE.txt
/usr/share/package-licenses/dldt/inference-engine_thirdparty_mkl-dnn_LICENSE
/usr/share/package-licenses/dldt/inference-engine_thirdparty_mkl-dnn_src_cpu_xbyak_COPYRIGHT
/usr/share/package-licenses/dldt/inference-engine_thirdparty_mkl-dnn_tests_gtests_gtest_LICENSE
