PKG_NAME := dldt
URL = https://github.com/opencv/dldt/archive/2019_R3.1/dldt-2019.R3.1.tar.gz
ARCHIVES = https://download.01.org/opencv/2019/openvinotoolkit/R3/inference_engine/firmware_ma2450_759W.zip inference-engine/temp/vpu/ma2450 https://download.01.org/opencv/2019/openvinotoolkit/R3/inference_engine/firmware_ma2x8x_mdk_R9.8.zip inference-engine/temp/vpu/ma2x8x https://download.01.org/opencv/2019/openvinotoolkit/R3/inference_engine/firmware_mv0262_mdk_R9.8.zip inference-engine/temp/vpu/mv0262

include ../common/Makefile.common
