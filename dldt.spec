#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dldt
Version  : 2018.r3
Release  : 5
URL      : https://github.com/opencv/dldt/archive/2018_R3.tar.gz
Source0  : https://github.com/opencv/dldt/archive/2018_R3.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 MIT
Requires: dldt-lib = %{version}-%{release}
Requires: dldt-license = %{version}-%{release}
Requires: networkx
Requires: numpy
Requires: onnx
Requires: opencv-python
Requires: protobuf
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
BuildRequires : python3
Patch1: build.patch
Patch2: install.patch

%description
The Google Mock class generator is an application that is part of cppclean.
visit http://code.google.com/p/cppclean/

%package dev
Summary: dev components for the dldt package.
Group: Development
Requires: dldt-lib = %{version}-%{release}
Provides: dldt-devel = %{version}-%{release}

%description dev
dev components for the dldt package.


%package lib
Summary: lib components for the dldt package.
Group: Libraries
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
%patch2 -p1

%build
## build_prepend content
pushd inference-engine
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540393200
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake .. -DENABLE_CLDNN=FALSE -DENABLE_INTEL_OMP=FALSE -DENABLE_OPENCV=FALSE -DENABLE_CLDNN_BUILD=ON  -DENABLE_SAMPLES_CORE=FALSE
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1540393200
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

%files dev
%defattr(-,root,root,-)
%exclude /usr/lib64/libgmock.so
%exclude /usr/lib64/libgmock_main.so
%exclude /usr/lib64/libgtest.so
%exclude /usr/lib64/libgtest_main.so
%exclude /usr/lib64/pkgconfig/gmock.pc
%exclude /usr/lib64/pkgconfig/gmock_main.pc
%exclude /usr/lib64/pkgconfig/gtest.pc
%exclude /usr/lib64/pkgconfig/gtest_main.pc
/usr/include/*.hpp
/usr/include/gmock/gmock-actions.h
/usr/include/gmock/gmock-cardinalities.h
/usr/include/gmock/gmock-generated-actions.h
/usr/include/gmock/gmock-generated-actions.h.pump
/usr/include/gmock/gmock-generated-function-mockers.h
/usr/include/gmock/gmock-generated-function-mockers.h.pump
/usr/include/gmock/gmock-generated-matchers.h
/usr/include/gmock/gmock-generated-matchers.h.pump
/usr/include/gmock/gmock-generated-nice-strict.h
/usr/include/gmock/gmock-generated-nice-strict.h.pump
/usr/include/gmock/gmock-matchers.h
/usr/include/gmock/gmock-more-actions.h
/usr/include/gmock/gmock-more-matchers.h
/usr/include/gmock/gmock-spec-builders.h
/usr/include/gmock/gmock.h
/usr/include/gmock/internal/custom/gmock-generated-actions.h
/usr/include/gmock/internal/custom/gmock-generated-actions.h.pump
/usr/include/gmock/internal/custom/gmock-matchers.h
/usr/include/gmock/internal/custom/gmock-port.h
/usr/include/gmock/internal/gmock-generated-internal-utils.h
/usr/include/gmock/internal/gmock-generated-internal-utils.h.pump
/usr/include/gmock/internal/gmock-internal-utils.h
/usr/include/gmock/internal/gmock-port.h
/usr/include/gtest/gtest-death-test.h
/usr/include/gtest/gtest-message.h
/usr/include/gtest/gtest-param-test.h
/usr/include/gtest/gtest-param-test.h.pump
/usr/include/gtest/gtest-printers.h
/usr/include/gtest/gtest-spi.h
/usr/include/gtest/gtest-test-part.h
/usr/include/gtest/gtest-typed-test.h
/usr/include/gtest/gtest.h
/usr/include/gtest/gtest_pred_impl.h
/usr/include/gtest/gtest_prod.h
/usr/include/gtest/internal/custom/gtest-port.h
/usr/include/gtest/internal/custom/gtest-printers.h
/usr/include/gtest/internal/custom/gtest.h
/usr/include/gtest/internal/gtest-death-test-internal.h
/usr/include/gtest/internal/gtest-filepath.h
/usr/include/gtest/internal/gtest-internal.h
/usr/include/gtest/internal/gtest-linked_ptr.h
/usr/include/gtest/internal/gtest-param-util-generated.h
/usr/include/gtest/internal/gtest-param-util-generated.h.pump
/usr/include/gtest/internal/gtest-param-util.h
/usr/include/gtest/internal/gtest-port-arch.h
/usr/include/gtest/internal/gtest-port.h
/usr/include/gtest/internal/gtest-string.h
/usr/include/gtest/internal/gtest-tuple.h
/usr/include/gtest/internal/gtest-tuple.h.pump
/usr/include/gtest/internal/gtest-type-util.h
/usr/include/gtest/internal/gtest-type-util.h.pump
/usr/lib64/cmake/pugixml/pugixml-config-relwithdebinfo.cmake
/usr/lib64/cmake/pugixml/pugixml-config.cmake
/usr/lib64/libinference_engine.so
/usr/lib64/libpugixml.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpugixml.so.1
/usr/lib64/libpugixml.so.1.7

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
