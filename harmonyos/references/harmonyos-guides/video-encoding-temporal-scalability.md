---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding-temporal-scalability
title: 时域可分层视频编码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 时域可分层视频编码
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:44ad44d707ee7e89491566719a911b5ca0fb369aeb8ae03ffeb5768213397cad
---

## 基础概念

### 时域可分层视频编码介绍

**可分层视频编码**，又叫可分级视频编码、可伸缩视频编码，是视频编码的扩展标准，目前广泛使用的包含SVC（H.264编码标准采用的可伸缩扩展）和SHVC（H.265编码标准采用的可扩展标准）。

其特点是能一次编码出时域分层、空域分层、质量域分层的码流结构，满足因网络、终端能力和用户需求不同带来的差异化需求。

**时域可分层视频编码**，是指能编码出时域分层码流的视频编码，下图展示了通过参考关系构建的4层时域分层码流结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/gL62GfGbTWiEKcHPonMY0g/zh-cn_image_0000002558765046.png?HW-CC-KV=V1&HW-CC-Date=20260429T053439Z&HW-CC-Expire=86400&HW-CC-Sign=3FA27B89EB1B461F553A9F3D1F25D3AAD6FC59F8BD3BE045F78D902864A4B70C)

从高到低逐层丢弃部分层级的码流（丢弃顺序L3->L2->L1），能实现不同程度的帧率伸缩，以满足传输和解码能力的变化需求。

如下图所示，这是上述4层时域分层码流结构丢弃L3后组成的新的码流结构，能在解码正常的情况下实现帧率减半的效果。其他层的丢弃同理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/CjjdP2q1Qhav_tVo63Qn6A/zh-cn_image_0000002558605390.png?HW-CC-KV=V1&HW-CC-Date=20260429T053439Z&HW-CC-Expire=86400&HW-CC-Sign=B45330C98E183E642EB2414890926289D9A6B772D5A36B81027306BB517B4E5E)

### 时域分层码流结构介绍

基础码流是由一个或多个独立图像组（Group Of Pictures，简称GOP）组合而成的视频码流。GOP是在编码中一组从I帧开始到I帧结束的连续的可独立解码的图像组。

时域分层码流可以在GOP内继续细分为独立的一个或多个时域图像组（Temporal Group Of Pictures，简称TGOP），每一个TGOP由一个基本层和后续的一个或多个增强层组合而成，如上述4层时域分层码流结构中的帧0到帧7是一个TGOP。

* **基本层（Base Layer，简称BL）：** 是GOP中的最底层（L0）。在时域分层中，该层用最低帧率进行编码。
* **增强层（Enhance Layer，简称EL）：** 是BL之上的层级，由低到高可以分为多层（L1、L2、L3）。在时域分层中，最低层的EL参考BL，进一步编码帧率更高的层级，更高层的EL会参考BL或低层EL，来编码比低层更高帧率的视频。

### 如何实现时域分层码流结构

时域分层码流结构的实现依赖于逐帧指定的参考关系，参考帧根据在解码图像缓存区（Decoded Picture Buffer，简称DPB）驻留的时长分为短期参考帧和长期参考帧。

* **短期参考帧（Short-Term Reference，简称STR）：** 是不能长期驻留在DPB中的参考帧，更新方式是先进先出，如果DPB满，旧的短期参考帧会被移出DPB。
* **长期参考帧（Long-Term Reference，简称LTR）：** 是能长期驻留在DPB中的参考帧，通过标记替换的方式更新，不主动标记替换就不会更新。

虽然STR个数大于1时，也能实现一定的跨帧参考结构，但受限于存在时效过短，时域分层结构支持的跨度有限。LTR则不存在上述问题，也能覆盖短期参考帧跨帧场景。优选使用LTR实现时域分层码流结构。

## 适用场景

基于上述描述的时域分层编码特点，推荐以下场景使用：

* 场景1：播放侧无缓存或低缓存的实时编码传输场景，例如视频会议、视频直播、协同办公等。
* 场景2：有视频预览播放或倍速播放需求的视频编码录制场景。

若应用场景不涉及动态调整时域参考结构，且分层结构简单，则推荐使用[全局时域可分层特性](video-encoding-temporal-scalability.md#全局时域可分层特性feature_temporal_scalability)，否则使能[长期参考帧特性](video-encoding-temporal-scalability.md#长期参考帧特性feature_long-term_reference)。

## 约束和限制

* 不可以混用全局时域可分层特性和长期参考帧特性。

  由于底层实现归一，全局时域可分层特性和长期参考帧特性不能同时开启。
* 叠加强制IDR配置时，请使用随帧通路配置。

  参考帧仅在GOP内有效，刷新I帧后，DPB随之清空，参考帧也会被清空，因此参考关系的指定受I帧刷新位置影响很大。

  使能时域分层能力后，若需要通过OH\_MD\_KEY\_REQUEST\_I\_FRAME临时请求I帧，应使用生效时机确定的随帧通路配置方式准确告知系统I帧刷新位置以避免参考关系错乱，参考随帧通路配置相关指导，避免使用生效时机不确定的OH\_VideoEncoder\_SetParameter方式。详情请参考[视频编码Surface模式](video-encoding.md#surface模式)"步骤-4"。
* 支持OH\_AVBuffer回调通路，不支持OH\_AVMemory回调通路。

  新特性依赖随帧特性，应避免使用OH\_AVMemory回调OH\_AVCodecAsyncCallback，应使用OH\_AVBuffer回调OH\_AVCodecCallback。
* 支持时域P分层，不支持时域B分层。

  时域可分层编码按分层帧类型分为基于P帧的时域分层和基于B帧的时域编码，当前支持分层P编码，不支持分层B编码。
* 均匀分层模式当前只支持TGOP为2或4。

## 全局时域可分层特性（Feature\_Temporal\_Scalability）

### 接口介绍

全局时域可分层特性，适用于编码稳定和简单的时域分层结构，初始配置全局生效，不支持动态修改。开发配置参数如下。

| 配置参数 | 语义 |
| --- | --- |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_TEMPORAL\_SCALABILITY | 全局时域可分层编码使能参数。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_SIZE | 全局时域可分层编码TGOP大小参数。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_REFERENCE\_MODE | 全局时域可分层编码TGOP参考模式。 |

* **全局时域可分层编码使能参数：** 在配置阶段配置，仅特性支持才会真正使能成功。
* **全局时域可分层编码TGOP大小参数：** 可选配置，影响时域关键帧之间的间隔，用户需要基于自身业务场景下抽帧需求自定义关键帧密度，可在[2, GopSize)范围内配置，若不配置则使用默认值。
* **全局时域可分层编码TGOP参考模式参数：** 可选配置，影响非关键帧参考模式。包括相邻参考ADJACENT\_REFERENCE、跨帧参考JUMP\_REFERENCE和均匀分层UNIFORMLY\_SCALED\_REFERENCE。相邻参考相对跨帧参考拥有更好的压缩性能，跨帧参考相对相邻参考拥有更好的丢帧自由度，均匀分层模式丢帧后的码流分布更均匀，如不配置则使用默认值。

  说明

  均匀分层模式当前只支持TGOP为2或4。

使用举例1：TGOP=4时的相邻参考模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/FAniqpNrSPibEt4rb7llgw/zh-cn_image_0000002589324917.png?HW-CC-KV=V1&HW-CC-Date=20260429T053439Z&HW-CC-Expire=86400&HW-CC-Sign=060E5C9AC19BF8750FE9625902E44ABBE9FDC92F391DC9238AF8F780D475B3D7)

使用举例2：TGOP=4时的跨帧参考模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/GYW9nn8MThivEAVjVDoaXQ/zh-cn_image_0000002589244853.png?HW-CC-KV=V1&HW-CC-Date=20260429T053439Z&HW-CC-Expire=86400&HW-CC-Sign=EDFC88893C2D958B6736693DC48171FCC95C9C3460DA50694C9D88A7A2BF3CFA)

使用举例3：TGOP=4时的均匀分层模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/q8cNtaSwRIWYhpXkVaO-7A/zh-cn_image_0000002558765048.png?HW-CC-KV=V1&HW-CC-Date=20260429T053439Z&HW-CC-Expire=86400&HW-CC-Sign=D244C6A98D4B43F98DB4FD14CF18B4CFE9389821BB35BCDE06C86F9AE5E5796E)

### 开发指导

基础编码流程请参考[视频编码开发指导](video-encoding.md)。下面将重点说明与基础视频编码流程中的不同之处。

1. 在初始阶段创建编码实例时，校验视频编码器是否支持全局时域可分层特性。

   ```
   1. // 1.1 获取对应视频编码器能力实例，此处以H.264为例。
   2. OH_AVCapability *cap = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_AVC, true);
   3. // 1.2 通过特性能力查询接口校验是否支持全局时域可分层特性。
   4. bool isSupported = OH_AVCapability_IsFeatureSupported(cap, VIDEO_ENCODER_TEMPORAL_SCALABILITY);
   ```

   如果支持，则可以使能全局时域可分层特性。

   ```
   1. // 创建硬件编码器实例。
   2. OH_AVCodec *videoEnc = OH_VideoEncoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_AVC);
   ```
2. 在配置阶段，设置全局时域可分层编码特性参数。

   ```
   1. constexpr int32_t TGOP_SIZE = 3;
   2. // 2.1 创建配置用临时AVFormat。
   3. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
   4. if (format == nullptr) {
   5. // 异常处理。
   6. }
   7. // 2.2 填充使能参数键值对。
   8. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_VIDEO_ENCODER_ENABLE_TEMPORAL_SCALABILITY, 1);
   9. // 2.3 (可选)填充TGOP大小和TGOP内参考模式键值对。
   10. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_VIDEO_ENCODER_TEMPORAL_GOP_SIZE, TGOP_SIZE);
   11. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_VIDEO_ENCODER_TEMPORAL_GOP_REFERENCE_MODE, ADJACENT_REFERENCE);
   12. // 2.4 参数配置。
   13. int32_t ret = OH_VideoEncoder_Configure(videoEnc, format.get());
   14. if (ret != AV_ERR_OK) {
   15. // 异常处理。
   16. }
   ```
3. （可选）在输出轮转中，可以获取码流对应时域层级信息。

   开发者可利用已配置的TGOP参数和编码出帧数目获取时域层级信息。

   示例代码如下：

   ```
   1. constexpr int32_t TGOP_SIZE = 3;
   2. uint32_t outPoc = 0;
   3. // 通过输出回调中有效帧数，获取TGOP内相对位置，对照配置确认层级。
   4. static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   5. {
   6. struct OH_AVCodecBufferAttr attr;
   7. OH_AVErrCode ret = OH_AVBuffer_GetBufferAttr(buffer, &attr);
   8. if (ret != AV_ERR_OK) {
   9. // 异常处理。
   10. }
   11. // 刷新I帧后POC归零。
   12. if (attr.flags & AVCODEC_BUFFER_FLAGS_SYNC_FRAME) {
   13. outPoc = 0;
   14. }
   15. // 只有XPS的输出需要跳过。
   16. if (attr.flags != AVCODEC_BUFFER_FLAGS_CODEC_DATA) {
   17. int32_t tGopInner = outPoc % TGOP_SIZE;
   18. if (tGopInner == 0) {
   19. // 时域关键帧，后续传输、解码流程不可丢弃。
   20. } else {
   21. // 时域非关键帧，后续传输、解码流程可以丢弃。
   22. }
   23. outPoc++;
   24. }
   25. }
   ```
4. （可选）在输出轮转中，使用步骤3获取的时域层级信息，自适应传输或自适应解码。

   根据获取的时域可分层码流和对应的层级信息，开发者可选择需要的层级进行传输，或携带至对端自适应选帧解码。

## 长期参考帧特性（Feature\_Long-Term\_Reference）

### 接口介绍

长期参考帧特性提供帧级参考关系配置。适用于灵活和复杂的时域分层结构。

| 配置参数 | 语义 |
| --- | --- |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT | 长期参考帧个数参数。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_MARK\_LTR | 当前帧标记为LTR帧。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_USE\_LTR | 当前帧参考的LTR帧的POC号。 |

* **长期参考帧个数参数：** 在配置阶段进行设置，应不大于实际查询到的最大支持数目。具体查询方法请参见下文开发指导的“步骤-3”。
* **当前帧标记为LTR帧：** BL层和被跳跃参考的EL层均标记为LTR。
* **当前帧参考的LTR帧的POC号：** 如当前帧需要跳跃参考前面已被标记为LTR帧的POC号。

使用举例，实现[时域可分层视频编码介绍](video-encoding-temporal-scalability.md#时域可分层视频编码介绍)中的4层时域分层结构的配置如下。

1. 在配置阶段，将OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT 配置为5。
2. 在运行阶段输入轮转中，按如下表所示随帧配置LTR相关参数，下表中\表示不做配置。

   | 配置\POC | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | MARK\_LTR | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
   | USE\_LTR | \ | \ | 0 | \ | 0 | \ | 4 | \ | 0 | \ | 8 | \ | 8 | \ | 12 | \ | 8 |

### 开发指导

基础编码流程请参考[视频编码开发指导](video-encoding.md)，下面仅针对与基础视频编码过程中存在的区别做具体说明。

1. 在初始阶段创建编码实例时，校验当前视频编码器是否支持LTR特性。

   ```
   1. constexpr int32_t NEEDED_LTR_COUNT = 5;
   2. bool isSupported = false;
   3. int32_t supportedLTRCount = 0;
   4. // 1.1 获取对应编码器能力实例，此处以H.264为例。
   5. OH_AVCapability *cap = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_AVC, true);
   6. // 1.2 通过特性能力查询接口校验是否支持LTR特性。
   7. isSupported = OH_AVCapability_IsFeatureSupported(cap, VIDEO_ENCODER_LONG_TERM_REFERENCE);
   8. // 1.3 确定支持的LTR数目。
   9. if (isSupported) {
   10. OH_AVFormat *properties = OH_AVCapability_GetFeatureProperties(cap, VIDEO_ENCODER_LONG_TERM_REFERENCE);
   11. if (!OH_AVFormat_GetIntValue(properties, OH_FEATURE_PROPERTY_KEY_VIDEO_ENCODER_MAX_LTR_FRAME_COUNT, &supportedLTRCount)) {
   12. // 异常处理。
   13. }
   14. OH_AVFormat_Destroy(properties);
   15. // 1.4 判断LTR是否满足结构需求。
   16. isSupported = supportedLTRCount >= NEEDED_LTR_COUNT;
   17. }
   ```

   若支持且LTR数目满足自身码流结构需求，则可以使能LTR特性。
2. 在配置之前注册回调时，注册随帧通路回调。

   Buffer输入模式示例：

   ```
   1. // 2.1 编码输入回调OH_AVCodecOnNeedInputBuffer实现。
   2. static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   3. {
   4. // 输入帧buffer对应的index，送入InIndexQueue队列。
   5. // 输入帧的数据buffer送入InBufferQueue队列。
   6. // 数据处理，请参考：
   7. // - 写入编码码流。
   8. // - 通知编码器码流结束。
   9. // - 随帧参数写入。
   10. auto format = std::shared_ptr<OH_AVFormat>(OH_AVBuffer_GetParameter(buffer), OH_AVFormat_Destroy);
   11. if (format == nullptr) {
   12. // 异常处理。
   13. }
   14. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_VIDEO_ENCODER_PER_FRAME_MARK_LTR, 1);
   15. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_VIDEO_ENCODER_PER_FRAME_USE_LTR, 4);
   16. OH_AVBuffer_SetParameter(buffer, format.get());
   17. // 通知编码器buffer输入完成。
   18. OH_VideoEncoder_PushInputBuffer(codec, index);
   19. }

   21. // 2.2 编码输出回调OH_AVCodecOnNewOutputBuffer实现。
   22. static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   23. {
   24. // 完成帧buffer对应的index，送入outIndexQueue队列。
   25. // 完成帧的数据buffer送入outBufferQueue队列。
   26. // 数据处理，请参考：
   27. // - 释放编码帧。
   28. // - 记录POC和LTR生效情况。
   29. }

   31. // 2.3 注册数据回调。
   32. OH_AVCodecCallback cb;
   33. cb.onNeedInputBuffer = OnNeedInputBuffer;
   34. cb.onNewOutputBuffer = OnNewOutputBuffer;
   35. OH_VideoEncoder_RegisterCallback(videoEnc, cb, nullptr);
   ```

   Surface输入模式示例：

   ```
   1. // 2.1 编码输入参数回调OH_VideoEncoder_OnNeedInputParameter实现。
   2. static void OnNeedInputParameter(OH_AVCodec *codec, uint32_t index, OH_AVFormat *parameter, void *userData)
   3. {
   4. // 输入帧buffer对应的index，送入InIndexQueue队列。
   5. // 输入帧的数据avformat送入InFormatQueue队列。
   6. // 数据处理，请参考：
   7. // - 写入编码码流。
   8. // - 通知编码器码流结束。
   9. // - 随帧参数写入。
   10. OH_AVFormat_SetIntValue(parameter, OH_MD_KEY_VIDEO_ENCODER_PER_FRAME_MARK_LTR, 1);
   11. OH_AVFormat_SetIntValue(parameter, OH_MD_KEY_VIDEO_ENCODER_PER_FRAME_USE_LTR, 4);
   12. // 通知编码器随帧参数配置输入完成。
   13. OH_VideoEncoder_PushInputParameter(codec, index);
   14. }

   16. // 2.2 编码输出回调OH_AVCodecOnNewOutputBuffer实现。
   17. static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
   18. {
   19. // 完成帧buffer对应的index，送入outIndexQueue队列。
   20. // 完成帧的数据buffer送入outBufferQueue队列。
   21. // 数据处理，请参考：
   22. // - 释放编码帧。
   23. // - 记录POC和LTR生效情况。
   24. }

   26. // 2.3 注册数据回调。
   27. OH_AVCodecCallback cb;
   28. cb.onNewOutputBuffer = OnNewOutputBuffer;
   29. OH_VideoEncoder_RegisterCallback(videoEnc, cb, nullptr);
   30. // 2.4 注册随帧参数回调。
   31. OH_VideoEncoder_OnNeedInputParameter inParaCb = OnNeedInputParameter;
   32. OH_VideoEncoder_RegisterParameterCallback(videoEnc, inParaCb, nullptr);
   ```
3. 在配置阶段，设置最大LTR数目。

   ```
   1. constexpr int32_t NEEDED_LTR_COUNT = 5;
   2. // 3.1 创建配置用临时AVFormat。
   3. auto format = std::shared_ptr<OH_AVFormat>(OH_AVFormat_Create(), OH_AVFormat_Destroy);
   4. if (format == nullptr) {
   5. // 异常处理。
   6. }
   7. // 3.2 填充使能LTR个数键值对。
   8. OH_AVFormat_SetIntValue(format.get(), OH_MD_KEY_VIDEO_ENCODER_LTR_FRAME_COUNT, NEEDED_LTR_COUNT);
   9. // 3.3 参数配置。
   10. int32_t ret = OH_VideoEncoder_Configure(videoEnc, format.get());
   11. if (ret != AV_ERR_OK) {
   12. // 异常处理。
   13. }
   ```
4. （可选）在输出轮转中，可以获取码流的时域层级信息。

   同全局时域可分层特性。

   由于在输入轮转过程中配置了LTR参数，也可以在输入轮转中记录这些参数，并在输出轮转中找到对应的输入参数。
5. （可选）在输出轮转中，使用步骤4获取的时域层级信息，进行自适应传输或自适应解码。

   同全局时域可分层特性。
