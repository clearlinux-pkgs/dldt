#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dldt
Version  : 2018.r3
Release  : 38
URL      : https://github.com/opencv/dldt/archive/2018_R3.tar.gz
Source0  : https://github.com/opencv/dldt/archive/2018_R3.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 MIT
Requires: dldt-bin = %{version}-%{release}
Requires: dldt-lib = %{version}-%{release}
Requires: dldt-license = %{version}-%{release}
Requires: mxnet
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
BuildRequires : gflags-dev
BuildRequires : glibc-dev
BuildRequires : googletest
BuildRequires : googletest-dev
BuildRequires : llvm
BuildRequires : mkl-dnn-dev
BuildRequires : openblas
BuildRequires : opencv
BuildRequires : opencv-dev
BuildRequires : opencv-python
BuildRequires : pugixml-dev
BuildRequires : python3
Patch1: 0001-Build-fixes.patch
Patch2: 0002-Add-fopenmp.patch
Patch3: 0003-Fixups-for-cmake-library-configuration.patch
Patch4: 0004-Fix-install-of-public-headers-within-subdirectories.patch
Patch5: 0005-Don-t-override-cmake-paths.patch
Patch6: 0006-Install-sample-apps.patch
Patch7: 0007-Statically-link-common-sample-app-lib.patch
Patch8: 0008-Don-t-override-cmake-paths-for-samples.patch
Patch9: 0009-Remove-OpenCV-version-dependency.patch
Patch10: 0010-Include-OpenCV-legacy-constants.patch

%description
The Google Mock class generator is an application that is part of cppclean.
visit http://code.google.com/p/cppclean/

%package bin
Summary: bin components for the dldt package.
Group: Binaries
Requires: dldt-license = %{version}-%{release}

%description bin
bin components for the dldt package.


%package dev
Summary: dev components for the dldt package.
Group: Development
Requires: dldt-lib = %{version}-%{release}
Requires: dldt-bin = %{version}-%{release}
Provides: dldt-devel = %{version}-%{release}

%description dev
dev components for the dldt package.


%package extras
Summary: extras components for the dldt package.
Group: Default

%description extras
extras components for the dldt package.


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
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
pushd ..
cp -a dldt-2018_R3 buildavx2
popd
pushd ..
cp -a dldt-2018_R3 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548200101
pushd inference-engine
mkdir -p clr-build
pushd clr-build
export CC=clang
export CXX=clang++
export LD=ld.gold
unset LDFLAGS
%cmake .. -DENABLE_CLDNN=0 \
-DENABLE_INTEL_OMP=0 \
-DENABLE_OPENCV=0 \
-DENABLE_CLDNN_BUILD=1 \
-DENABLE_SAMPLES_CORE=1 \
-DENABLE_PYTHON_BINDINGS=1 \
-DINSTALL_GMOCK=0 \
-DINSTALL_GTEST=0 \
-DBUILD_GMOCK=1 \
-DBUILD_GTEST=0 \
-DENABLE_PLUGIN_RPATH=0
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export CC=clang
export CXX=clang++
export LD=ld.gold
unset LDFLAGS
export CFLAGS="$CFLAGS -O3 -march=haswell "
export FCFLAGS="$CFLAGS -O3 -march=haswell "
export FFLAGS="$CFLAGS -O3 -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake .. -DENABLE_CLDNN=0 \
-DENABLE_INTEL_OMP=0 \
-DENABLE_OPENCV=0 \
-DENABLE_CLDNN_BUILD=1 \
-DENABLE_SAMPLES_CORE=1 \
-DENABLE_PYTHON_BINDINGS=1 \
-DINSTALL_GMOCK=0 \
-DINSTALL_GTEST=0 \
-DBUILD_GMOCK=1 \
-DBUILD_GTEST=0 \
-DENABLE_PLUGIN_RPATH=0
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export CC=clang
export CXX=clang++
export LD=ld.gold
unset LDFLAGS
export CFLAGS="$CFLAGS -O3 -march=skylake-avx512 "
export FCFLAGS="$CFLAGS -O3 -march=skylake-avx512 "
export FFLAGS="$CFLAGS -O3 -march=skylake-avx512 "
export CXXFLAGS="$CXXFLAGS -O3 -march=skylake-avx512 "
export CFLAGS="$CFLAGS -march=skylake-avx512 -m64 "
export CXXFLAGS="$CXXFLAGS -march=skylake-avx512 -m64 "
%cmake .. -DENABLE_CLDNN=0 \
-DENABLE_INTEL_OMP=0 \
-DENABLE_OPENCV=0 \
-DENABLE_CLDNN_BUILD=1 \
-DENABLE_SAMPLES_CORE=1 \
-DENABLE_PYTHON_BINDINGS=1 \
-DINSTALL_GMOCK=0 \
-DINSTALL_GTEST=0 \
-DBUILD_GMOCK=1 \
-DBUILD_GTEST=0 \
-DENABLE_PLUGIN_RPATH=0
make  %{?_smp_mflags} VERBOSE=1
popd
popd

%install
export SOURCE_DATE_EPOCH=1548200101
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
pushd clr-build-avx512
%make_install_avx512  || :
popd
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd
popd
## install_append content
mkdir -p %{buildroot}/usr/lib64
install -m 0755 inference-engine/clr-build/src/extension/libcpu_extension.so    %{buildroot}/usr/lib64
install -m 0755 inference-engine/clr-build/src/hetero_plugin/libHeteroPlugin.so %{buildroot}/usr/lib64
install -m 0755 inference-engine/clr-build/src/mkldnn_plugin/libMKLDNNPlugin.so %{buildroot}/usr/lib64
rm -f %{buildroot}/usr/lib64/libgflags_nothreads.so*
rm -f %{buildroot}/usr/lib64/libpugixml.so*
rm -f %{buildroot}/usr/lib64/haswell/libgflags_nothreads.so*
rm -f %{buildroot}/usr/lib64/haswell/libpugixml.so*
rm -f %{buildroot}/usr/lib64/haswell/avx512_1/libgflags_nothreads.so*
rm -f %{buildroot}/usr/lib64/haswell/avx512_1/libpugixml.so*
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/classification_sample
%exclude /usr/bin/classification_sample_async
%exclude /usr/bin/haswell/avx512_1/classification_sample
%exclude /usr/bin/haswell/avx512_1/classification_sample_async
%exclude /usr/bin/haswell/avx512_1/hello_autoresize_classification
%exclude /usr/bin/haswell/avx512_1/hello_classification
%exclude /usr/bin/haswell/avx512_1/hello_request_classification
%exclude /usr/bin/haswell/avx512_1/object_detection_sample_ssd
%exclude /usr/bin/haswell/avx512_1/style_transfer_sample
%exclude /usr/bin/haswell/avx512_1/validation_app
%exclude /usr/bin/haswell/classification_sample
%exclude /usr/bin/haswell/classification_sample_async
%exclude /usr/bin/haswell/hello_autoresize_classification
%exclude /usr/bin/haswell/hello_classification
%exclude /usr/bin/haswell/hello_request_classification
%exclude /usr/bin/haswell/object_detection_sample_ssd
%exclude /usr/bin/haswell/style_transfer_sample
%exclude /usr/bin/haswell/validation_app
%exclude /usr/bin/hello_autoresize_classification
%exclude /usr/bin/hello_classification
%exclude /usr/bin/hello_request_classification
%exclude /usr/bin/object_detection_sample_ssd
%exclude /usr/bin/style_transfer_sample
%exclude /usr/bin/validation_app

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/pugiconfig.hpp
%exclude /usr/include/pugixml.hpp
%exclude /usr/lib64/cmake/pugixml/pugixml-config-relwithdebinfo.cmake
%exclude /usr/lib64/cmake/pugixml/pugixml-config.cmake
%exclude /usr/lib64/pkgconfig/gflags.pc
/usr/include/inference_engine/cldnn/cldnn_config.hpp
/usr/include/inference_engine/cpp/ie_cnn_net_reader.h
/usr/include/inference_engine/cpp/ie_cnn_network.h
/usr/include/inference_engine/cpp/ie_executable_network.hpp
/usr/include/inference_engine/cpp/ie_infer_request.hpp
/usr/include/inference_engine/cpp/ie_memory_state.hpp
/usr/include/inference_engine/cpp/ie_plugin_cpp.hpp
/usr/include/inference_engine/details/ie_blob_iterator.hpp
/usr/include/inference_engine/details/ie_cnn_network_iterator.hpp
/usr/include/inference_engine/details/ie_exception.hpp
/usr/include/inference_engine/details/ie_exception_conversion.hpp
/usr/include/inference_engine/details/ie_irelease.hpp
/usr/include/inference_engine/details/ie_no_copy.hpp
/usr/include/inference_engine/details/ie_no_release.hpp
/usr/include/inference_engine/details/ie_pre_allocator.hpp
/usr/include/inference_engine/details/ie_so_loader.h
/usr/include/inference_engine/details/ie_so_pointer.hpp
/usr/include/inference_engine/details/os/lin_shared_object_loader.h
/usr/include/inference_engine/details/os/win_shared_object_loader.h
/usr/include/inference_engine/hetero/hetero_plugin_config.hpp
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
/usr/include/inference_engine/mkldnn/mkldnn_extension.hpp
/usr/include/inference_engine/mkldnn/mkldnn_extension_ptr.hpp
/usr/include/inference_engine/mkldnn/mkldnn_extension_types.hpp
/usr/include/inference_engine/mkldnn/mkldnn_generic_primitive.hpp
/usr/lib64/cmake/InferenceEngine/InferenceEngineConfig-version.cmake
/usr/lib64/cmake/InferenceEngine/InferenceEngineConfig.cmake
/usr/lib64/cmake/InferenceEngine/targets-relwithdebinfo.cmake
/usr/lib64/cmake/InferenceEngine/targets.cmake
/usr/lib64/haswell/avx512_1/libinference_engine.so
/usr/lib64/haswell/libinference_engine.so
/usr/lib64/libHeteroPlugin.so
/usr/lib64/libMKLDNNPlugin.so
/usr/lib64/libcpu_extension.so
/usr/lib64/libinference_engine.so

%files extras
%defattr(-,root,root,-)
/usr/bin/classification_sample
/usr/bin/classification_sample_async
/usr/bin/haswell/avx512_1/classification_sample
/usr/bin/haswell/avx512_1/classification_sample_async
/usr/bin/haswell/avx512_1/hello_autoresize_classification
/usr/bin/haswell/avx512_1/hello_classification
/usr/bin/haswell/avx512_1/hello_request_classification
/usr/bin/haswell/avx512_1/object_detection_sample_ssd
/usr/bin/haswell/avx512_1/style_transfer_sample
/usr/bin/haswell/avx512_1/validation_app
/usr/bin/haswell/classification_sample
/usr/bin/haswell/classification_sample_async
/usr/bin/haswell/hello_autoresize_classification
/usr/bin/haswell/hello_classification
/usr/bin/haswell/hello_request_classification
/usr/bin/haswell/object_detection_sample_ssd
/usr/bin/haswell/style_transfer_sample
/usr/bin/haswell/validation_app
/usr/bin/hello_autoresize_classification
/usr/bin/hello_classification
/usr/bin/hello_request_classification
/usr/bin/object_detection_sample_ssd
/usr/bin/style_transfer_sample
/usr/bin/validation_app

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libinference_engine.so.1
/usr/lib64/haswell/libinference_engine.so.1
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
