/**
* Copyright 2020 Huawei Technologies Co., Ltd
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at

* http://www.apache.org/licenses/LICENSE-2.0

* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.

* File dvpp_process.h
* Description: handle dvpp process
*/
#pragma once
#include <cstdint>

#include "acl/acl.h"
#include "acl/ops/acl_dvpp.h"

class DvppCropAndPaste {
    public:
    /**
    * @brief Constructor
    * @param [in] stream: stream
    */
    DvppCropAndPaste(aclrtStream &stream, acldvppChannelDesc *dvppChannelDesc,
    uint32_t lt_horz, uint32_t lt_vert,uint32_t rb_horz, uint32_t rb_vert);

    /**
    * @brief Destructor
    */
    ~DvppCropAndPaste();

    /**
    * @brief dvpp global init
    * @return AtlasError
    */
    AtlasError InitResource();

    /**
    * @brief init dvpp output para
    * @param [in] modelInputWidth: model input width
    * @param [in] modelInputHeight: model input height
    * @return AtlasError
    */
    AtlasError InitOutputPara(int modelInputWidth, int modelInputHeight);

    /**
    * @brief dvpp process
    * @return AtlasError
    */
    AtlasError Process(ImageData& resizedImage, ImageData& srcImage);

private:
    AtlasError InitCropAndPasteResource(ImageData& inputImage);
    AtlasError InitCropAndPasteInputDesc(ImageData& inputImage);
    AtlasError InitCropAndPasteOutputDesc();

    void DestroyCropAndPasteResource();

private:
    aclrtStream stream_;
    acldvppChannelDesc *dvppChannelDesc_;

    acldvppPicDesc *vpcInputDesc_;
    acldvppPicDesc *vpcOutputDesc_;

    void *vpcOutBufferDev_;
    uint32_t vpcOutBufferSize_;

    acldvppRoiConfig *cropArea_;
    acldvppRoiConfig *pasteArea_;

    Resolution size_;

    uint32_t ltHorz_;
    uint32_t rbHorz_;
    uint32_t ltVert_;
    uint32_t rbVert_;
};

