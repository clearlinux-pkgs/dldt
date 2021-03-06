#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dldt
Version  : 2019.r3.1
Release  : 80
URL      : https://github.com/opencv/dldt/archive/2019_R3.1/dldt-2019.R3.1.tar.gz
Source0  : https://github.com/opencv/dldt/archive/2019_R3.1/dldt-2019.R3.1.tar.gz
Source1  : https://download.01.org/opencv/2019/openvinotoolkit/R3/inference_engine/firmware_ma2450_759W.zip
Source2  : https://download.01.org/opencv/2019/openvinotoolkit/R3/inference_engine/firmware_ma2x8x_mdk_R9.8.zip
Source3  : https://download.01.org/opencv/2019/openvinotoolkit/R3/inference_engine/firmware_mv0262_mdk_R9.8.zip
Summary  : @PACKAGE_DESCRIPTION@
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISSL MIT
Requires: dldt-config = %{version}-%{release}
Requires: dldt-data = %{version}-%{release}
Requires: dldt-lib = %{version}-%{release}
Requires: dldt-license = %{version}-%{release}
Requires: dldt-python = %{version}-%{release}
Requires: dldt-python3 = %{version}-%{release}
Requires: Cython
Requires: Pillow
Requires: PyYAML
Requires: Shapely
Requires: defusedxml
Requires: gflags
Requires: intel-compute-runtime
Requires: mxnet
Requires: networkx
Requires: numpy
Requires: onnx
Requires: opencv-python
Requires: progress
Requires: protobuf
Requires: pugixml-dev
Requires: scipy
Requires: tensorflow
Requires: tqdm
Requires: xmltodict
BuildRequires : Cython
BuildRequires : Pillow
BuildRequires : PyYAML
BuildRequires : Shapely
BuildRequires : ade-dev
BuildRequires : ade-staticdev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : defusedxml
BuildRequires : doxygen
BuildRequires : gflags
BuildRequires : gflags-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : googletest
BuildRequires : googletest-dev
BuildRequires : intel-compute-runtime
BuildRequires : libusb-dev
BuildRequires : llvm-dev
BuildRequires : mkl-dnn-dev
BuildRequires : mxnet
BuildRequires : networkx
BuildRequires : ngraph-dev
BuildRequires : numpy
BuildRequires : ocl-icd-dev
BuildRequires : onnx
BuildRequires : openblas
BuildRequires : opencv
BuildRequires : opencv-dev
BuildRequires : opencv-python
BuildRequires : progress
BuildRequires : protobuf
BuildRequires : pugixml-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : scipy
BuildRequires : tbb-dev
BuildRequires : tensorflow
BuildRequires : tqdm
BuildRequires : util-linux
BuildRequires : xmltodict
Patch1: 0001-R3-fix-build-error.patch
Patch2: 0002-R3-install-DLDT-headers-libs-sample-apps.patch
Patch3: 0003-use-GNUInstallDirs-on-nix.patch
Patch4: 0004-R3-enable-VPU-Myriad-support.patch

%description
# [OpenVINO™ Toolkit](https://01.org/openvinotoolkit) - Deep Learning Deployment Toolkit repository
[![Stable release](https://img.shields.io/badge/version-2019.R3-green.svg)](https://github.com/opencv/dldt/releases/tag/2019_R3)
[![Apache License Version 2.0](https://img.shields.io/badge/license-Apache_2.0-green.svg)](LICENSE)

%package config
Summary: config components for the dldt package.
Group: Default

%description config
config components for the dldt package.


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
Requires: dldt = %{version}-%{release}

%description dev
dev components for the dldt package.


%package doc
Summary: doc components for the dldt package.
Group: Documentation

%description doc
doc components for the dldt package.


%package extras
Summary: extras components for the dldt package.
Group: Default

%description extras
extras components for the dldt package.


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


%package python
Summary: python components for the dldt package.
Group: Default
Requires: dldt-python3 = %{version}-%{release}

%description python
python components for the dldt package.


%package python3
Summary: python3 components for the dldt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dldt package.


%prep
%setup -q -n dldt-2019_R3.1
cd %{_builddir}
mkdir -p firmware_ma2450_759W
cd firmware_ma2450_759W
unzip -q %{_sourcedir}/firmware_ma2450_759W.zip
cd %{_builddir}
mkdir -p firmware_ma2x8x_mdk_R9.8
cd firmware_ma2x8x_mdk_R9.8
unzip -q %{_sourcedir}/firmware_ma2x8x_mdk_R9.8.zip
cd %{_builddir}
mkdir -p firmware_mv0262_mdk_R9.8
cd firmware_mv0262_mdk_R9.8
unzip -q %{_sourcedir}/firmware_mv0262_mdk_R9.8.zip
cd %{_builddir}/dldt-2019_R3.1
mkdir -p inference-engine/temp/vpu/ma2450
cp -r %{_builddir}/firmware_ma2450_759W/* %{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/ma2450
mkdir -p inference-engine/temp/vpu/ma2x8x
cp -r %{_builddir}/firmware_ma2x8x_mdk_R9.8/* %{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/ma2x8x
mkdir -p inference-engine/temp/vpu/mv0262
cp -r %{_builddir}/firmware_mv0262_mdk_R9.8/* %{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/mv0262
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
## build_prepend content
export VPU_FIRMWARE_MA2450=%{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/ma2450
export VPU_FIRMWARE_MV0262=%{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/mv0262
export VPU_FIRMWARE_MA2X8X=%{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/ma2x8x
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575914972
pushd inference-engine
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake .. -DENABLE_CLDNN=1 \
-DENABLE_INTEL_OMP=0 \
-DENABLE_OPENCV=0 \
-DENABLE_SAMPLES_CORE=1 \
-DENABLE_PYTHON_BINDINGS=1 \
-DINSTALL_GMOCK=0 \
-DINSTALL_GTEST=0 \
-DBUILD_GMOCK=1 \
-DBUILD_GTEST=0 \
-DENABLE_PLUGIN_RPATH=0 \
-DENABLE_GNA=0 \
-DLLVM_LINK_LLVM_DYLIB=ON \
-DTHREADING=TBB \
-DENABLE_VPU=ON \
-DENABLE_MYRIAD=ON \
-DENABLE_PYTHON=ON \
-DPYTHON_EXECUTABLE=/usr/bin/python3 \
-DPYTHON_INCLUDE_DIR=$(python -c "import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())") \
-DCMAKE_BUILD_TYPE=Release
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
export VPU_FIRMWARE_MA2450=%{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/ma2450
export VPU_FIRMWARE_MV0262=%{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/mv0262
export VPU_FIRMWARE_MA2X8X=%{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/ma2x8x
## build_prepend end
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake .. -DENABLE_CLDNN=1 \
-DENABLE_INTEL_OMP=0 \
-DENABLE_OPENCV=0 \
-DENABLE_SAMPLES_CORE=1 \
-DENABLE_PYTHON_BINDINGS=1 \
-DINSTALL_GMOCK=0 \
-DINSTALL_GTEST=0 \
-DBUILD_GMOCK=1 \
-DBUILD_GTEST=0 \
-DENABLE_PLUGIN_RPATH=0 \
-DENABLE_GNA=0 \
-DLLVM_LINK_LLVM_DYLIB=ON \
-DTHREADING=TBB \
-DENABLE_VPU=ON \
-DENABLE_MYRIAD=ON \
-DENABLE_PYTHON=ON \
-DPYTHON_EXECUTABLE=/usr/bin/python3 \
-DPYTHON_INCLUDE_DIR=$(python -c "import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())") \
-DCMAKE_BUILD_TYPE=Release
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
## build_prepend content
export VPU_FIRMWARE_MA2450=%{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/ma2450
export VPU_FIRMWARE_MV0262=%{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/mv0262
export VPU_FIRMWARE_MA2X8X=%{_builddir}/dldt-2019_R3.1/inference-engine/temp/vpu/ma2x8x
## build_prepend end
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export CFLAGS="$CFLAGS -march=skylake-avx512 -m64 "
export CXXFLAGS="$CXXFLAGS -march=skylake-avx512 -m64 "
%cmake .. -DENABLE_CLDNN=1 \
-DENABLE_INTEL_OMP=0 \
-DENABLE_OPENCV=0 \
-DENABLE_SAMPLES_CORE=1 \
-DENABLE_PYTHON_BINDINGS=1 \
-DINSTALL_GMOCK=0 \
-DINSTALL_GTEST=0 \
-DBUILD_GMOCK=1 \
-DBUILD_GTEST=0 \
-DENABLE_PLUGIN_RPATH=0 \
-DENABLE_GNA=0 \
-DLLVM_LINK_LLVM_DYLIB=ON \
-DTHREADING=TBB \
-DENABLE_VPU=ON \
-DENABLE_MYRIAD=ON \
-DENABLE_PYTHON=ON \
-DPYTHON_EXECUTABLE=/usr/bin/python3 \
-DPYTHON_INCLUDE_DIR=$(python -c "import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())") \
-DCMAKE_BUILD_TYPE=Release
make  %{?_smp_mflags}  VERBOSE=1
popd
popd

%install
export SOURCE_DATE_EPOCH=1575914972
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dldt
cp %{_builddir}/dldt-2019_R3.1/LICENSE %{buildroot}/usr/share/package-licenses/dldt/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/dldt-2019_R3.1/inference-engine/samples/thirdparty/gflags/COPYING.txt %{buildroot}/usr/share/package-licenses/dldt/b2d4ab17f1b8ef9e0646ba932dce81efe3b852ab
cp %{_builddir}/dldt-2019_R3.1/inference-engine/tests/libs/gtest/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/dldt/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/dldt-2019_R3.1/inference-engine/tests/libs/gtest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/dldt/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
cp %{_builddir}/dldt-2019_R3.1/inference-engine/tests/libs/gtest/googletest/LICENSE %{buildroot}/usr/share/package-licenses/dldt/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/dldt-2019_R3.1/inference-engine/thirdparty/clDNN/common/googletest-fused/License.txt %{buildroot}/usr/share/package-licenses/dldt/9283634b9c14d0b7d238f4219d44a60974bd2030
cp %{_builddir}/dldt-2019_R3.1/inference-engine/thirdparty/clDNN/common/intel_ocl_icd/6.3/OpenCL_ICD_Loader_License.txt %{buildroot}/usr/share/package-licenses/dldt/db214a78d03be892d25086bc555baacf3bdf153b
cp %{_builddir}/dldt-2019_R3.1/inference-engine/thirdparty/clDNN/common/intel_ocl_icd/6.3/OpenCL_headers_License.txt %{buildroot}/usr/share/package-licenses/dldt/009a9705ecc0db197274c321509be5bdacd6b9e1
cp %{_builddir}/dldt-2019_R3.1/inference-engine/thirdparty/clDNN/common/khronos_ocl_clhpp/LICENSE.txt %{buildroot}/usr/share/package-licenses/dldt/69ad187528313b14f3320f102227ce17d68436be
cp %{_builddir}/dldt-2019_R3.1/inference-engine/thirdparty/mkl-dnn/LICENSE %{buildroot}/usr/share/package-licenses/dldt/b62656e08adcf16ce153c1df3e835ad3afb5f9ed
cp %{_builddir}/dldt-2019_R3.1/inference-engine/thirdparty/mkl-dnn/src/cpu/xbyak/COPYRIGHT %{buildroot}/usr/share/package-licenses/dldt/59ecdb87df571ebd03bc505a75344cc6f49626e8
cp %{_builddir}/dldt-2019_R3.1/inference-engine/thirdparty/mkl-dnn/tests/gtests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/dldt/5a2314153eadadc69258a9429104cd11804ea304
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
## Remove excluded files
rm -f %{buildroot}/usr/include/pugiconfig.hpp
rm -f %{buildroot}/usr/include/pugixml.hpp
rm -f %{buildroot}/usr/lib64/cmake/pugixml/pugixml-config-relwithdebinfo.cmake
rm -f %{buildroot}/usr/lib64/cmake/pugixml/pugixml-config.cmake
rm -f %{buildroot}/usr/lib64/pkgconfig/gflags.pc
## install_append content
SO_FILES=" \
libcpu_extension.so \
libHeteroPlugin.so \
libMKLDNNPlugin.so \
libclDNNPlugin.so \
libmyriadPlugin.so \
"
mkdir -p %{buildroot}/usr/lib64/haswell/avx512_1
for so in ${SO_FILES}; do
find inference-engine/clr-build/ -type f -name "${so}" -exec install -m 0755 {} %{buildroot}/usr/lib64 \;
find inference-engine/clr-build-avx2/ -type f -name "${so}" -exec install -m 0755 {} %{buildroot}/usr/lib64/haswell \;
find inference-engine/clr-build-avx512/ -type f -name "${so}" -exec install -m 0755 {} %{buildroot}/usr/lib64/haswell/avx512_1 \;
done

mkdir -p %{buildroot}/usr/lib/udev/rules.d
install -m 0644 inference-engine/thirdparty/movidius/mvnc/src/97-myriad-usbboot.rules %{buildroot}/usr/lib/udev/rules.d

rm -f %{buildroot}/usr/lib64/libgflags_nothreads.so*
rm -f %{buildroot}/usr/lib64/libpugixml.so*
rm -f %{buildroot}/usr/lib64/haswell/libgflags_nothreads.so*
rm -f %{buildroot}/usr/lib64/haswell/libpugixml.so*
rm -f %{buildroot}/usr/lib64/haswell/avx512_1/libgflags_nothreads.so*
rm -f %{buildroot}/usr/lib64/haswell/avx512_1/libpugixml.so*

mkdir -p %{buildroot}/usr/lib/firmware
find inference-engine/temp/vpu/ -type f -name "*.mvcmd" -exec install -m 0644 {} %{buildroot}/usr/lib/firmware \;
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/firmware/MvNCAPI-ma2450.mvcmd
/usr/lib/firmware/MvNCAPI-ma2x8x.mvcmd
/usr/lib/firmware/MvNCAPI-mv0262.mvcmd

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/97-myriad-usbboot.rules

%files data
%defattr(-,root,root,-)
/usr/share/openvino/inference-engine/plugins.xml

%files dev
%defattr(-,root,root,-)
/usr/include/clDNN/activation.hpp
/usr/include/clDNN/activation_grad.hpp
/usr/include/clDNN/apply_adam.hpp
/usr/include/clDNN/arg_max_min.hpp
/usr/include/clDNN/average_unpooling.hpp
/usr/include/clDNN/batch_norm.hpp
/usr/include/clDNN/batch_norm_grad.hpp
/usr/include/clDNN/binary_convolution.hpp
/usr/include/clDNN/border.hpp
/usr/include/clDNN/broadcast.hpp
/usr/include/clDNN/cldnn.hpp
/usr/include/clDNN/compounds.h
/usr/include/clDNN/concatenation.hpp
/usr/include/clDNN/condition.hpp
/usr/include/clDNN/contract.hpp
/usr/include/clDNN/convolution.hpp
/usr/include/clDNN/convolution_grad_input.hpp
/usr/include/clDNN/convolution_grad_weights.hpp
/usr/include/clDNN/crop.hpp
/usr/include/clDNN/custom_gpu_primitive.hpp
/usr/include/clDNN/data.hpp
/usr/include/clDNN/deconvolution.hpp
/usr/include/clDNN/depth_to_space.hpp
/usr/include/clDNN/detection_output.hpp
/usr/include/clDNN/eltwise.hpp
/usr/include/clDNN/embed.hpp
/usr/include/clDNN/engine.hpp
/usr/include/clDNN/event.hpp
/usr/include/clDNN/fully_connected.hpp
/usr/include/clDNN/fully_connected_grad_input.hpp
/usr/include/clDNN/fully_connected_grad_weights.hpp
/usr/include/clDNN/gather.hpp
/usr/include/clDNN/gather_tree.hpp
/usr/include/clDNN/gemm.hpp
/usr/include/clDNN/index_select.hpp
/usr/include/clDNN/input_layout.hpp
/usr/include/clDNN/layout.hpp
/usr/include/clDNN/lookup_table.hpp
/usr/include/clDNN/lrn.hpp
/usr/include/clDNN/lstm.hpp
/usr/include/clDNN/lstm_dynamic.hpp
/usr/include/clDNN/max_unpooling.hpp
/usr/include/clDNN/memory.hpp
/usr/include/clDNN/meta_utils.hpp
/usr/include/clDNN/mutable_data.hpp
/usr/include/clDNN/mvn.hpp
/usr/include/clDNN/network.hpp
/usr/include/clDNN/normalize.hpp
/usr/include/clDNN/one_hot.hpp
/usr/include/clDNN/permute.hpp
/usr/include/clDNN/pooling.hpp
/usr/include/clDNN/primitive.hpp
/usr/include/clDNN/prior_box.hpp
/usr/include/clDNN/profiling.hpp
/usr/include/clDNN/program.hpp
/usr/include/clDNN/proposal.hpp
/usr/include/clDNN/pyramid_roi_align.hpp
/usr/include/clDNN/quantize.hpp
/usr/include/clDNN/reduce.hpp
/usr/include/clDNN/region_yolo.hpp
/usr/include/clDNN/reorder.hpp
/usr/include/clDNN/reorg_yolo.hpp
/usr/include/clDNN/reshape.hpp
/usr/include/clDNN/reverse_sequence.hpp
/usr/include/clDNN/roi_pooling.hpp
/usr/include/clDNN/scale.hpp
/usr/include/clDNN/scale_grad_input.hpp
/usr/include/clDNN/scale_grad_weights.hpp
/usr/include/clDNN/select.hpp
/usr/include/clDNN/shuffle_channels.hpp
/usr/include/clDNN/softmax.hpp
/usr/include/clDNN/softmax_loss_grad.hpp
/usr/include/clDNN/split.hpp
/usr/include/clDNN/strided_slice.hpp
/usr/include/clDNN/tensor.hpp
/usr/include/clDNN/tile.hpp
/usr/include/clDNN/topology.hpp
/usr/include/clDNN/upsampling.hpp
/usr/include/inference_engine/builders/ie_argmax_layer.hpp
/usr/include/inference_engine/builders/ie_batch_normalization_layer.hpp
/usr/include/inference_engine/builders/ie_clamp_layer.hpp
/usr/include/inference_engine/builders/ie_concat_layer.hpp
/usr/include/inference_engine/builders/ie_const_layer.hpp
/usr/include/inference_engine/builders/ie_convolution_layer.hpp
/usr/include/inference_engine/builders/ie_crop_layer.hpp
/usr/include/inference_engine/builders/ie_ctc_greedy_decoder_layer.hpp
/usr/include/inference_engine/builders/ie_deconvolution_layer.hpp
/usr/include/inference_engine/builders/ie_deformable_convolution_layer.hpp
/usr/include/inference_engine/builders/ie_detection_output_layer.hpp
/usr/include/inference_engine/builders/ie_eltwise_layer.hpp
/usr/include/inference_engine/builders/ie_elu_layer.hpp
/usr/include/inference_engine/builders/ie_fully_connected_layer.hpp
/usr/include/inference_engine/builders/ie_grn_layer.hpp
/usr/include/inference_engine/builders/ie_gru_sequence_layer.hpp
/usr/include/inference_engine/builders/ie_input_layer.hpp
/usr/include/inference_engine/builders/ie_layer_builder.hpp
/usr/include/inference_engine/builders/ie_layer_decorator.hpp
/usr/include/inference_engine/builders/ie_lrn_layer.hpp
/usr/include/inference_engine/builders/ie_lstm_sequence_layer.hpp
/usr/include/inference_engine/builders/ie_memory_layer.hpp
/usr/include/inference_engine/builders/ie_mvn_layer.hpp
/usr/include/inference_engine/builders/ie_network_builder.hpp
/usr/include/inference_engine/builders/ie_norm_layer.hpp
/usr/include/inference_engine/builders/ie_normalize_layer.hpp
/usr/include/inference_engine/builders/ie_output_layer.hpp
/usr/include/inference_engine/builders/ie_permute_layer.hpp
/usr/include/inference_engine/builders/ie_pooling_layer.hpp
/usr/include/inference_engine/builders/ie_power_layer.hpp
/usr/include/inference_engine/builders/ie_prelu_layer.hpp
/usr/include/inference_engine/builders/ie_prior_box_clustered_layer.hpp
/usr/include/inference_engine/builders/ie_prior_box_layer.hpp
/usr/include/inference_engine/builders/ie_proposal_layer.hpp
/usr/include/inference_engine/builders/ie_psroi_pooling_layer.hpp
/usr/include/inference_engine/builders/ie_region_yolo_layer.hpp
/usr/include/inference_engine/builders/ie_relu6_layer.hpp
/usr/include/inference_engine/builders/ie_relu_layer.hpp
/usr/include/inference_engine/builders/ie_reorg_yolo_layer.hpp
/usr/include/inference_engine/builders/ie_resample_layer.hpp
/usr/include/inference_engine/builders/ie_reshape_layer.hpp
/usr/include/inference_engine/builders/ie_rnn_sequence_layer.hpp
/usr/include/inference_engine/builders/ie_roi_pooling_layer.hpp
/usr/include/inference_engine/builders/ie_scale_shift_layer.hpp
/usr/include/inference_engine/builders/ie_sigmoid_layer.hpp
/usr/include/inference_engine/builders/ie_simpler_nms_layer.hpp
/usr/include/inference_engine/builders/ie_softmax_layer.hpp
/usr/include/inference_engine/builders/ie_split_layer.hpp
/usr/include/inference_engine/builders/ie_tanh_layer.hpp
/usr/include/inference_engine/builders/ie_tile_layer.hpp
/usr/include/inference_engine/cldnn/cldnn_config.hpp
/usr/include/inference_engine/cpp/ie_cnn_net_reader.h
/usr/include/inference_engine/cpp/ie_cnn_network.h
/usr/include/inference_engine/cpp/ie_executable_network.hpp
/usr/include/inference_engine/cpp/ie_infer_request.hpp
/usr/include/inference_engine/cpp/ie_memory_state.hpp
/usr/include/inference_engine/cpp/ie_plugin_cpp.hpp
/usr/include/inference_engine/details/caseless.hpp
/usr/include/inference_engine/details/ie_blob_iterator.hpp
/usr/include/inference_engine/details/ie_cnn_network_iterator.hpp
/usr/include/inference_engine/details/ie_cnn_network_tools.h
/usr/include/inference_engine/details/ie_exception.hpp
/usr/include/inference_engine/details/ie_exception_conversion.hpp
/usr/include/inference_engine/details/ie_inetwork_iterator.hpp
/usr/include/inference_engine/details/ie_irelease.hpp
/usr/include/inference_engine/details/ie_no_copy.hpp
/usr/include/inference_engine/details/ie_no_release.hpp
/usr/include/inference_engine/details/ie_pre_allocator.hpp
/usr/include/inference_engine/details/ie_so_loader.h
/usr/include/inference_engine/details/ie_so_pointer.hpp
/usr/include/inference_engine/details/os/lin_shared_object_loader.h
/usr/include/inference_engine/details/os/os_filesystem.hpp
/usr/include/inference_engine/details/os/win_shared_object_loader.h
/usr/include/inference_engine/dlia/dlia_config.hpp
/usr/include/inference_engine/gna/gna_config.hpp
/usr/include/inference_engine/hetero/hetero_plugin_config.hpp
/usr/include/inference_engine/ie_allocator.hpp
/usr/include/inference_engine/ie_api.h
/usr/include/inference_engine/ie_blob.h
/usr/include/inference_engine/ie_builders.hpp
/usr/include/inference_engine/ie_common.h
/usr/include/inference_engine/ie_compound_blob.h
/usr/include/inference_engine/ie_context.hpp
/usr/include/inference_engine/ie_core.hpp
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
/usr/include/inference_engine/ie_layers_property.hpp
/usr/include/inference_engine/ie_layouts.h
/usr/include/inference_engine/ie_locked_memory.hpp
/usr/include/inference_engine/ie_network.hpp
/usr/include/inference_engine/ie_parallel.hpp
/usr/include/inference_engine/ie_parameter.hpp
/usr/include/inference_engine/ie_plugin.hpp
/usr/include/inference_engine/ie_plugin_config.hpp
/usr/include/inference_engine/ie_plugin_dispatcher.hpp
/usr/include/inference_engine/ie_plugin_ptr.hpp
/usr/include/inference_engine/ie_precision.hpp
/usr/include/inference_engine/ie_preprocess.hpp
/usr/include/inference_engine/ie_primitive_info.hpp
/usr/include/inference_engine/ie_tensor_info.hpp
/usr/include/inference_engine/ie_unicode.hpp
/usr/include/inference_engine/ie_utils.hpp
/usr/include/inference_engine/ie_version.hpp
/usr/include/inference_engine/inference_engine.hpp
/usr/include/inference_engine/multi-device/multi_device_config.hpp
/usr/include/inference_engine/vpu/hddl_plugin_config.hpp
/usr/include/inference_engine/vpu/myriad_plugin_config.hpp
/usr/include/inference_engine/vpu/vpu_plugin_config.hpp
/usr/lib64/cmake/InferenceEngine/InferenceEngineConfig-version.cmake
/usr/lib64/cmake/InferenceEngine/InferenceEngineConfig.cmake
/usr/lib64/cmake/InferenceEngine/targets-release.cmake
/usr/lib64/cmake/InferenceEngine/targets.cmake
/usr/lib64/cmake/InferenceEngine/targets_cpu_extension-release.cmake
/usr/lib64/cmake/InferenceEngine/targets_cpu_extension.cmake

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/inference_engine/extension/CMakeLists.txt
/usr/share/doc/inference_engine/extension/README.md
/usr/share/doc/inference_engine/extension/cmake/CPUID.cmake
/usr/share/doc/inference_engine/extension/cmake/OptimizationFlags.cmake
/usr/share/doc/inference_engine/extension/cmake/feature_defs.cmake
/usr/share/doc/inference_engine/extension/common/defs.h
/usr/share/doc/inference_engine/extension/common/fast_exp.h
/usr/share/doc/inference_engine/extension/common/fp16_utils.h
/usr/share/doc/inference_engine/extension/common/opt_exp.h
/usr/share/doc/inference_engine/extension/common/simple_copy.cpp
/usr/share/doc/inference_engine/extension/common/simple_copy.h
/usr/share/doc/inference_engine/extension/common/softmax.h
/usr/share/doc/inference_engine/extension/ext_argmax.cpp
/usr/share/doc/inference_engine/extension/ext_base.cpp
/usr/share/doc/inference_engine/extension/ext_base.hpp
/usr/share/doc/inference_engine/extension/ext_broadcast.cpp
/usr/share/doc/inference_engine/extension/ext_ctc_greedy.cpp
/usr/share/doc/inference_engine/extension/ext_depth_to_space.cpp
/usr/share/doc/inference_engine/extension/ext_detectionoutput.cpp
/usr/share/doc/inference_engine/extension/ext_detectionoutput_onnx.cpp
/usr/share/doc/inference_engine/extension/ext_fill.cpp
/usr/share/doc/inference_engine/extension/ext_gather.cpp
/usr/share/doc/inference_engine/extension/ext_gather_tree.cpp
/usr/share/doc/inference_engine/extension/ext_grn.cpp
/usr/share/doc/inference_engine/extension/ext_interp.cpp
/usr/share/doc/inference_engine/extension/ext_list.cpp
/usr/share/doc/inference_engine/extension/ext_list.hpp
/usr/share/doc/inference_engine/extension/ext_log_softmax.cpp
/usr/share/doc/inference_engine/extension/ext_math.cpp
/usr/share/doc/inference_engine/extension/ext_mvn.cpp
/usr/share/doc/inference_engine/extension/ext_non_max_suppression.cpp
/usr/share/doc/inference_engine/extension/ext_normalize.cpp
/usr/share/doc/inference_engine/extension/ext_one_hot.cpp
/usr/share/doc/inference_engine/extension/ext_pad.cpp
/usr/share/doc/inference_engine/extension/ext_powerfile.cpp
/usr/share/doc/inference_engine/extension/ext_priorbox.cpp
/usr/share/doc/inference_engine/extension/ext_priorbox_clustered.cpp
/usr/share/doc/inference_engine/extension/ext_priorgridgenerator_onnx.cpp
/usr/share/doc/inference_engine/extension/ext_proposal.cpp
/usr/share/doc/inference_engine/extension/ext_proposal_onnx.cpp
/usr/share/doc/inference_engine/extension/ext_psroi.cpp
/usr/share/doc/inference_engine/extension/ext_range.cpp
/usr/share/doc/inference_engine/extension/ext_reduce.cpp
/usr/share/doc/inference_engine/extension/ext_region_yolo.cpp
/usr/share/doc/inference_engine/extension/ext_reorg_yolo.cpp
/usr/share/doc/inference_engine/extension/ext_resample.cpp
/usr/share/doc/inference_engine/extension/ext_reverse_sequence.cpp
/usr/share/doc/inference_engine/extension/ext_roifeatureextractor_onnx.cpp
/usr/share/doc/inference_engine/extension/ext_scatter.cpp
/usr/share/doc/inference_engine/extension/ext_select.cpp
/usr/share/doc/inference_engine/extension/ext_shuffle_channels.cpp
/usr/share/doc/inference_engine/extension/ext_simplernms.cpp
/usr/share/doc/inference_engine/extension/ext_space_to_depth.cpp
/usr/share/doc/inference_engine/extension/ext_sparse_fill_empty_rows.cpp
/usr/share/doc/inference_engine/extension/ext_squeeze.cpp
/usr/share/doc/inference_engine/extension/ext_strided_slice.cpp
/usr/share/doc/inference_engine/extension/ext_topk.cpp
/usr/share/doc/inference_engine/extension/ext_topkrois_onnx.cpp
/usr/share/doc/inference_engine/extension/ext_unique.cpp
/usr/share/doc/inference_engine/extension/ext_unsqueeze.cpp
/usr/share/doc/inference_engine/samples/CMakeLists.txt
/usr/share/doc/inference_engine/samples/benchmark_app/CMakeLists.txt
/usr/share/doc/inference_engine/samples/benchmark_app/README.md
/usr/share/doc/inference_engine/samples/benchmark_app/benchmark_app.hpp
/usr/share/doc/inference_engine/samples/benchmark_app/infer_request_wrap.hpp
/usr/share/doc/inference_engine/samples/benchmark_app/inputs_filling.cpp
/usr/share/doc/inference_engine/samples/benchmark_app/inputs_filling.hpp
/usr/share/doc/inference_engine/samples/benchmark_app/main.cpp
/usr/share/doc/inference_engine/samples/benchmark_app/progress_bar.hpp
/usr/share/doc/inference_engine/samples/benchmark_app/statistics_report.cpp
/usr/share/doc/inference_engine/samples/benchmark_app/statistics_report.hpp
/usr/share/doc/inference_engine/samples/benchmark_app/utils.cpp
/usr/share/doc/inference_engine/samples/benchmark_app/utils.hpp
/usr/share/doc/inference_engine/samples/build_samples.sh
/usr/share/doc/inference_engine/samples/build_samples_msvc.bat
/usr/share/doc/inference_engine/samples/classification_sample_async/CMakeLists.txt
/usr/share/doc/inference_engine/samples/classification_sample_async/README.md
/usr/share/doc/inference_engine/samples/classification_sample_async/classification_sample_async.h
/usr/share/doc/inference_engine/samples/classification_sample_async/main.cpp
/usr/share/doc/inference_engine/samples/common/format_reader/CMakeLists.txt
/usr/share/doc/inference_engine/samples/common/format_reader/MnistUbyte.cpp
/usr/share/doc/inference_engine/samples/common/format_reader/MnistUbyte.h
/usr/share/doc/inference_engine/samples/common/format_reader/bmp.cpp
/usr/share/doc/inference_engine/samples/common/format_reader/bmp.h
/usr/share/doc/inference_engine/samples/common/format_reader/format_reader.cpp
/usr/share/doc/inference_engine/samples/common/format_reader/format_reader.h
/usr/share/doc/inference_engine/samples/common/format_reader/format_reader_ptr.h
/usr/share/doc/inference_engine/samples/common/format_reader/opencv_wraper.cpp
/usr/share/doc/inference_engine/samples/common/format_reader/opencv_wraper.h
/usr/share/doc/inference_engine/samples/common/format_reader/register.h
/usr/share/doc/inference_engine/samples/common/os/windows/w_dirent.h
/usr/share/doc/inference_engine/samples/common/samples/args_helper.hpp
/usr/share/doc/inference_engine/samples/common/samples/classification_results.h
/usr/share/doc/inference_engine/samples/common/samples/common.hpp
/usr/share/doc/inference_engine/samples/common/samples/console_progress.hpp
/usr/share/doc/inference_engine/samples/common/samples/csv_dumper.hpp
/usr/share/doc/inference_engine/samples/common/samples/ocv_common.hpp
/usr/share/doc/inference_engine/samples/common/samples/slog.hpp
/usr/share/doc/inference_engine/samples/common/vpu/vpu_tools_common.hpp
/usr/share/doc/inference_engine/samples/hello_classification/CMakeLists.txt
/usr/share/doc/inference_engine/samples/hello_classification/README.md
/usr/share/doc/inference_engine/samples/hello_classification/main.cpp
/usr/share/doc/inference_engine/samples/hello_nv12_input_classification/CMakeLists.txt
/usr/share/doc/inference_engine/samples/hello_nv12_input_classification/README.md
/usr/share/doc/inference_engine/samples/hello_nv12_input_classification/main.cpp
/usr/share/doc/inference_engine/samples/hello_query_device/CMakeLists.txt
/usr/share/doc/inference_engine/samples/hello_query_device/README.md
/usr/share/doc/inference_engine/samples/hello_query_device/main.cpp
/usr/share/doc/inference_engine/samples/hello_reshape_ssd/CMakeLists.txt
/usr/share/doc/inference_engine/samples/hello_reshape_ssd/README.md
/usr/share/doc/inference_engine/samples/hello_reshape_ssd/main.cpp
/usr/share/doc/inference_engine/samples/hello_reshape_ssd/reshape_ssd_extension.hpp
/usr/share/doc/inference_engine/samples/object_detection_sample_ssd/CMakeLists.txt
/usr/share/doc/inference_engine/samples/object_detection_sample_ssd/README.md
/usr/share/doc/inference_engine/samples/object_detection_sample_ssd/main.cpp
/usr/share/doc/inference_engine/samples/object_detection_sample_ssd/object_detection_sample_ssd.h
/usr/share/doc/inference_engine/samples/speech_sample/CMakeLists.txt
/usr/share/doc/inference_engine/samples/speech_sample/README.md
/usr/share/doc/inference_engine/samples/speech_sample/main.cpp
/usr/share/doc/inference_engine/samples/speech_sample/speech_sample.hpp
/usr/share/doc/inference_engine/samples/style_transfer_sample/CMakeLists.txt
/usr/share/doc/inference_engine/samples/style_transfer_sample/README.md
/usr/share/doc/inference_engine/samples/style_transfer_sample/main.cpp
/usr/share/doc/inference_engine/samples/style_transfer_sample/style_transfer_sample.h
/usr/share/doc/inference_engine/samples/thirdparty/gflags/.gitattributes
/usr/share/doc/inference_engine/samples/thirdparty/gflags/.gitignore
/usr/share/doc/inference_engine/samples/thirdparty/gflags/.travis.yml
/usr/share/doc/inference_engine/samples/thirdparty/gflags/AUTHORS.txt
/usr/share/doc/inference_engine/samples/thirdparty/gflags/BUILD
/usr/share/doc/inference_engine/samples/thirdparty/gflags/CMakeLists.txt
/usr/share/doc/inference_engine/samples/thirdparty/gflags/COPYING.txt
/usr/share/doc/inference_engine/samples/thirdparty/gflags/ChangeLog.txt
/usr/share/doc/inference_engine/samples/thirdparty/gflags/INSTALL.md
/usr/share/doc/inference_engine/samples/thirdparty/gflags/README.md
/usr/share/doc/inference_engine/samples/thirdparty/gflags/WORKSPACE
/usr/share/doc/inference_engine/samples/thirdparty/gflags/appveyor.yml
/usr/share/doc/inference_engine/samples/thirdparty/gflags/bazel/gflags.bzl
/usr/share/doc/inference_engine/samples/thirdparty/gflags/cmake/README_runtime.txt
/usr/share/doc/inference_engine/samples/thirdparty/gflags/cmake/config.cmake.in
/usr/share/doc/inference_engine/samples/thirdparty/gflags/cmake/execute_test.cmake
/usr/share/doc/inference_engine/samples/thirdparty/gflags/cmake/package.cmake.in
/usr/share/doc/inference_engine/samples/thirdparty/gflags/cmake/package.pc.in
/usr/share/doc/inference_engine/samples/thirdparty/gflags/cmake/utils.cmake
/usr/share/doc/inference_engine/samples/thirdparty/gflags/cmake/version.cmake.in
/usr/share/doc/inference_engine/samples/thirdparty/gflags/doc/.nojekyll
/usr/share/doc/inference_engine/samples/thirdparty/gflags/doc/designstyle.css
/usr/share/doc/inference_engine/samples/thirdparty/gflags/doc/index.html
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/config.h.in
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/gflags.cc
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/gflags.h.in
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/gflags_completions.cc
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/gflags_completions.h.in
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/gflags_completions.sh
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/gflags_declare.h.in
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/gflags_ns.h.in
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/gflags_reporting.cc
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/mutex.h
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/util.h
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/windows_port.cc
/usr/share/doc/inference_engine/samples/thirdparty/gflags/src/windows_port.h
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/CMakeLists.txt
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/config/CMakeLists.txt
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/config/main.cc
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/flagfile.1
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/flagfile.2
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/flagfile.3
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/gflags_build.py.in
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/gflags_declare_flags.cc
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/gflags_declare_test.cc
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/gflags_strip_flags_test.cc
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/gflags_strip_flags_test.cmake
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/gflags_unittest.cc
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/gflags_unittest_flagfile
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/nc/CMakeLists.txt
/usr/share/doc/inference_engine/samples/thirdparty/gflags/test/nc/gflags_nc.cc

%files extras
%defattr(-,root,root,-)
/usr/bin/benchmark_app
/usr/bin/classification_sample_async
/usr/bin/haswell/avx512_1/benchmark_app
/usr/bin/haswell/avx512_1/classification_sample_async
/usr/bin/haswell/avx512_1/hello_classification
/usr/bin/haswell/avx512_1/hello_nv12_input_classification
/usr/bin/haswell/avx512_1/hello_query_device
/usr/bin/haswell/avx512_1/hello_reshape_ssd
/usr/bin/haswell/avx512_1/object_detection_sample_ssd
/usr/bin/haswell/avx512_1/speech_sample
/usr/bin/haswell/avx512_1/style_transfer_sample
/usr/bin/haswell/benchmark_app
/usr/bin/haswell/classification_sample_async
/usr/bin/haswell/hello_classification
/usr/bin/haswell/hello_nv12_input_classification
/usr/bin/haswell/hello_query_device
/usr/bin/haswell/hello_reshape_ssd
/usr/bin/haswell/object_detection_sample_ssd
/usr/bin/haswell/speech_sample
/usr/bin/haswell/style_transfer_sample
/usr/bin/hello_classification
/usr/bin/hello_nv12_input_classification
/usr/bin/hello_query_device
/usr/bin/hello_reshape_ssd
/usr/bin/object_detection_sample_ssd
/usr/bin/speech_sample
/usr/bin/style_transfer_sample

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libHeteroPlugin.so
/usr/lib64/haswell/avx512_1/libMKLDNNPlugin.so
/usr/lib64/haswell/avx512_1/libclDNNPlugin.so
/usr/lib64/haswell/avx512_1/libcpu_extension.so
/usr/lib64/haswell/avx512_1/libinference_engine.so
/usr/lib64/haswell/avx512_1/libinference_engine.so.1
/usr/lib64/haswell/avx512_1/libmyriadPlugin.so
/usr/lib64/haswell/libHeteroPlugin.so
/usr/lib64/haswell/libMKLDNNPlugin.so
/usr/lib64/haswell/libclDNNPlugin.so
/usr/lib64/haswell/libcpu_extension.so
/usr/lib64/haswell/libformat_reader.so
/usr/lib64/haswell/libinference_engine.so
/usr/lib64/haswell/libinference_engine.so.1
/usr/lib64/haswell/libmyriadPlugin.so
/usr/lib64/libHeteroPlugin.so
/usr/lib64/libMKLDNNPlugin.so
/usr/lib64/libclDNNPlugin.so
/usr/lib64/libcpu_extension.so
/usr/lib64/libformat_reader.so
/usr/lib64/libinference_engine.so
/usr/lib64/libinference_engine.so.1
/usr/lib64/libmyriadPlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dldt/009a9705ecc0db197274c321509be5bdacd6b9e1
/usr/share/package-licenses/dldt/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
/usr/share/package-licenses/dldt/59ecdb87df571ebd03bc505a75344cc6f49626e8
/usr/share/package-licenses/dldt/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/dldt/69ad187528313b14f3320f102227ce17d68436be
/usr/share/package-licenses/dldt/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/dldt/9283634b9c14d0b7d238f4219d44a60974bd2030
/usr/share/package-licenses/dldt/b2d4ab17f1b8ef9e0646ba932dce81efe3b852ab
/usr/share/package-licenses/dldt/b62656e08adcf16ce153c1df3e835ad3afb5f9ed
/usr/share/package-licenses/dldt/db214a78d03be892d25086bc555baacf3bdf153b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
