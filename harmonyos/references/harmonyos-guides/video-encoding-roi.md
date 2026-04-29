---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding-roi
title: ROI视频编码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > ROI视频编码
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b658da04038989fbccd90f7045036bb14981330ac685f25eaeeb8992a5595106
---

## 基础概念

从API version 20开始支持ROI视频编码（Region Of Interest Video Coding），该功能是基于硬件H.264/H.265编码能力扩展的高级优化技术。其核心逻辑为对画面中指定的重点区域分配更多编码资源实现高画质编码。在有限带宽条件下保障ROI区域内容清晰呈现，显著提升整体视觉体验。

开发者可自主定义视频画面中的ROI区域（如直播中的人脸、监控中的车牌等），并通过设定质量偏移参数，调节ROI区域与非ROI区域的编码质量差异，实现编码资源的差异化分配。

## 适用场景

ROI视频编码适用于因网络带宽限制导致码率不能满足视频画质要求，且能明确定义关键画面内容（ROI区域）的场景。比如视频通话、视频直播、安全监控等。

各场景中ROI区域的选择建议如下：

* 秀场直播：将主播面部区域设为ROI，优化人脸细节（如肤色、五官轮廓），提升观众沉浸式观看体验。
* 户外直播：将主播主体/核心拍摄景物（如自然风光、赛事画面核心区域）设为ROI，在移动网络带宽波动时保障核心内容清晰。
* 电商直播：将商品展示区域（如美妆试色、电子产品细节）设为ROI，清晰呈现商品外观、材质与功能细节，助力商品转化。
* 网课视频：将课件文字、讲义图表、板书内容区域设为ROI，保证知识点清晰可读，降低视觉疲劳，提升教学效果。
* 安全监控：将摄像头画面中的人脸、车牌、出入口等关键区域设为ROI，提升抓拍清晰度，便于后续识别分析。

为了支持不同的编码场景，提供了三类ROI编码开发示例，开发者可根据实际业务和技术架构选择。

| 不同场景对照点 | 直播/视频通话场景 | 录像场景 | 编辑导出/内容发布场景 |
| --- | --- | --- | --- |
| **ROI信息生产者** | 相机 | 相机 | 应用 |
| **ROI信息获取方式** | 通过相机元数据回调获取 | 通过相机元数据回调获取 | 应用自管理 |
| **编码视频帧直接生产者** | 图形 | 相机 | 应用 |
| **编码模式** | Surface模式 | Surface模式 | Buffer模式 |
| **ROI管理&对齐方式** | 基于时间戳匹配 | 基于回调时机匹配 | 自选 |
| **ROI参数配置方式** | NativeBuffer元数据配置 | 编码输入参数回调配置 | 编码输入buffer回调配置 |
| **开发示例** | [Surface模式下通过NativeBuffer接口配置ROI](video-encoding-roi.md#surface模式下通过nativebuffer接口配置roi) | [Surface模式下通过编码输入回调接口配置ROI](video-encoding-roi.md#surface模式下通过编码输入回调接口配置roi) | [Buffer模式下配置ROI](video-encoding-roi.md#buffer模式下配置roi) |

## 约束和限制

**支持的编码器：** H.264 8bit硬件编码、H.265 8bit硬件编码、H.265 10bit硬件编码。

**支持的码控模式：** VBR(Variable Bit Rate)、CBR(Constant Bit Rate)、SQR(Stable Quality Rate Control)。

**依赖ROI检测识别能力：** 编码器不具备ROI的检测识别能力，所以ROI编码技术生效依赖于开发者输入的ROI信息。开发者可根据业务场景自行设计并实现ROI识别能力，或通过调用系统相机模块原生提供的人脸区域信息，降低开发成本，具体请参考[相机人脸ROI获取示例](native-camera-metadata.md#状态监听)。

## 参数要求说明

支持开发者通过字符串形式下发ROI配置参数，参数需满足"Top,Left-Bottom,Right=DeltaQp"格式，所有参数均为整数。

* ROI是一个矩形区域，Top，Left和Bottom，Right分别定义了ROI的区域在图像中的左上角和右下角的坐标位置（如图1所示）。
* DeltaQp指定编码量化参数（Quantization Parameter）的差异值，DeltaQp绝对值越大，ROI区域与非ROI区域的编码质量差异越大。DeltaQp为负表示ROI区域编码画质优于非ROI区域。"=DeltaQp"可以省略，省略时使用默认参数（=-3）。
* 多个ROI参数之间通过";"连接, 多ROI配置如"Top1,Left1-Bottom1,Right1=DeltaQp1;Top2,Left2-Bottom2,Right2=DeltaQp2"。
* 同一帧最多支持配置6个ROI区域，按照配置顺序，多出的ROI区域将被忽略。总ROI面积不能超过图片面积的1/5。按照配置顺序依次累加，仅生效累加面积在限制之内的ROI区域。

**图1：ROI坐标和最大允许面积占比示意图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/z3yLPkHWSkG34DpovkoBlg/zh-cn_image_0000002558605392.png?HW-CC-KV=V1&HW-CC-Date=20260429T053440Z&HW-CC-Expire=86400&HW-CC-Sign=52967B868C984F243159CB68A45B73E56463033A5A55FBC0FC19E0725FD0AFAF)

## 生效机制说明

配置ROI支持两种方式：**NativeBuffer元数据配置方式**和**编码输入回调配置方式**。编码输入回调配置方式包含编码输入参数回调（Surface模式）和编码输入buffer回调（Buffer模式）。

* NativeBuffer元数据配置方式（推荐）：从API version 22开始支持使用OH\_NativeBuffer\_MetaDataKey的ROI枚举OH\_REGION\_OF\_INTEREST\_METADATA，在NativeBuffer的元数据中配置ROI参数。
* 编码输入回调配置方式：使用视频编码参数OH\_MD\_KEY\_VIDEO\_ENCODER\_ROI\_PARAMS在编码输入回调中配置。

**通用生效机制：**

1. ROI参数支持随帧下发并实时生效，开发者无需进行能力查询或配置全局开关。
2. 如果系统编码器不支持ROI编码能力，编码器会忽略ROI参数，进行普通编码。
3. DeltaQp有效取值范围为[-51, 51]，编码器会在ROI区域的QP上叠加DeltaQp，然后限制到[minQp, maxQp]范围内得到最终QP。
4. 当某一帧未配置ROI参数时，若上一帧生效了ROI编码，则复用上一帧ROI信息进行当前帧ROI编码；若上一帧是普通编码，则进行普通编码。
5. 当某一帧配置的ROI参数无法解析出任何有效ROI信息时，进行普通编码。
6. 如果多个ROI区域产生交叠，按照配置顺序，仅最先配置的ROI区域会在交叠处生效。

**NativeBuffer元数据配置方式独有机制：** 最大支持256Byte长度字符，超出部分会被截断。

**空字符串处理差异：**

* NativeBuffer元数据配置方式：不允许配置空字符串，视作未配置ROI参数，当前帧会继承历史帧信息进行ROI编码。
* 编码输入回调配置方式：允许配置空字符串，但因无法解析出有效ROI信息，编码时按照普通编码方式进行编码。

说明

因空字符串处理存在差异，应避免配置空字符串。如需关闭某一帧的ROI编码，可配置无位置信息的字符串，如"Clear"或";"等。

**同时配置时的生效优先级：** 当某一帧的两种方式均有配置ROI参数，仅生效以编码输入回调配置方式下发的ROI参数，无论其能否解析出有效ROI信息。

## 开发示例

### Surface模式下通过NativeBuffer接口配置ROI

系统相机获取视频帧的接口和获取ROI信息的接口是两个独立的回调接口，需要根据视频时间戳和ROI信息时间戳进行数据同步匹配，并在编码前完成相应帧的ROI配置。

说明

ROI信息需与相机视频帧信息严格对齐。实际应用中，若两个接口处理不同步，可能导致ROI调用错位；高负载场景下，还可能出现连续两帧ROI时间戳相同的异常。当出现上述情况，不影响编码功能正常运行，开发者可结合编码画质评估结果，自主决定是否继续使用。

在具体业务场景中，相机获取的视频帧会经过一系列的图像处理，如美颜、滤波和增强等前处理（如图2所示），开发者可以根据实际的业务需求进行模块增减。

**图2：NativeBuffer元数据接口配置ROI流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/xfB2hcvpSt2cUmbRSEO-Zw/zh-cn_image_0000002589324919.png?HW-CC-KV=V1&HW-CC-Date=20260429T053440Z&HW-CC-Expire=86400&HW-CC-Sign=006F7A707A8D5505DB9A6DBCC707C76BC215F63AAF0373BD4FEBFA95F297F661)

详细开发步骤如下：

1. 在CMakeList.txt中链接动态库。

   ```
   1. set(BASE_LIBRARY
   2. libnative_media_codecbase.so libnative_media_core.so libnative_media_venc.so libnative_window.so
   3. libnative_buffer.so libnative_image.so libEGL.so libGLESv3.so
   4. )
   5. target_link_libraries(recorder PUBLIC ${BASE_LIBRARY})
   ```

   说明

   上述'recorder'字样仅为示例，此处应由开发者根据具体的CMake工程目标名称进行替换。
2. 监听相机元数据回调接口获取人脸位置信息。

   如何注册相机元数据回调可以参考 [相机元数据状态监听](camera-metadata.md#状态监听)。

   ```
   1. import { camera } from '@kit.CameraKit'
   2. import { BusinessError } from '@kit.BasicServicesKit'
   3. import recorder from 'librecorder.so';

   5. interface FaceBoundingBox {
   6. topLeftX: number;
   7. topLeftY: number;
   8. width: number;
   9. height: number;
   10. }

   12. onMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
   13. metadataOutput.on('metadataObjectsAvailable', (err: BusinessError, metadataObjectArr: Array<camera.MetadataObject>) => {
   14. if (err !== undefined && err.code !== 0) {
   15. return;
   16. }
   17. const faceBoundingBoxes: Array<FaceBoundingBox> = [];
   18. let unifiedTimestamp = 0;
   19. let timestampSet = false;

   21. for (const metadataObject of metadataObjectArr) {
   22. if (metadataObject.type === camera.MetadataObjectType.FACE_DETECTION) {
   23. if (!timestampSet) {
   24. unifiedTimestamp = metadataObject.timestamp;
   25. timestampSet = true;
   26. }
   27. faceBoundingBoxes.push({
   28. topLeftX: metadataObject.boundingBox.topLeftX,
   29. topLeftY: metadataObject.boundingBox.topLeftY,
   30. width: metadataObject.boundingBox.width,
   31. height: metadataObject.boundingBox.height
   32. })
   33. }
   34. }
   35. if (faceBoundingBoxes.length > 0) {
   36. // 下发人脸位置信息到Native层（this.nativeRecorderObj是Native层实例）。
   37. recorder.UpdateFaceRect(this.nativeRecorderObj, unifiedTimestamp, faceBoundingBoxes);
   38. }
   39. });
   40. }
   ```
3. Native层解析TS层传递的人脸位置信息。

   ```
   1. struct FaceRect {
   2. double topLeftX;
   3. double topLeftY;
   4. double width;
   5. double height;
   6. };

   8. static napi_value UpdateFaceRect(napi_env env, napi_callback_info info)
   9. {
   10. size_t argc = 3;
   11. napi_value args[3] = {nullptr};
   12. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   13. if (argc < 3) {
   14. return nullptr;
   15. }
   16. // 解析native实例。
   17. int64_t addrValue = 0;
   18. bool flag = false;
   19. napi_get_value_bigint_int64(env, args[0], &addrValue, &flag);
   20. Recorder *recorder = reinterpret_cast<Recorder *>(addrValue);
   21. if (recorder == nullptr) {
   22. return nullptr;
   23. }
   24. // 解析时间戳。
   25. int64_t timestamp = 0;
   26. napi_get_value_int64(env, args[1], &timestamp);
   27. // 解析人脸Rect。
   28. napi_value faceRectArray = args[2];
   29. bool isArray;
   30. napi_is_array(env, faceRectArray, &isArray);
   31. if (!isArray) {
   32. return nullptr;
   33. }
   34. uint32_t arrayLength;
   35. napi_get_array_length(env, faceRectArray, &arrayLength);
   36. std::vector<FaceRect> faceRectVec;
   37. for (uint32_t i = 0; i < arrayLength; i++) {
   38. FaceRect item = {0};
   39. napi_value faceRectObj;
   40. napi_get_element(env, faceRectArray, i, &faceRectObj);
   41. napi_value propValue;
   42. napi_get_named_property(env, faceRectObj, "topLeftX", &propValue);
   43. napi_get_value_double(env, propValue, &item.topLeftX);
   44. napi_get_named_property(env, faceRectObj, "topLeftY", &propValue);
   45. napi_get_value_double(env, propValue, &item.topLeftY);
   46. napi_get_named_property(env, faceRectObj, "width", &propValue);
   47. napi_get_value_double(env, propValue, &item.width);
   48. napi_get_named_property(env, faceRectObj, "topLeftX", &propValue);
   49. napi_get_value_double(env, propValue, &item.height);
   50. faceRectVec.push_back(item);
   51. }
   52. recorder->ConvertToRoi(timestamp, faceRectVec);
   53. return nullptr;
   54. }
   ```
4. 转换成ROI信息格式字符串并保存。

   ```
   1. #include <map>
   2. #include <mutex>
   3. #include <sstream>
   4. #include <string>

   6. const int width = 1920;   // 视频帧宽度。
   7. const int height = 1080;  // 视频帧高度。
   8. const int qpOffset = -6;  // QP偏移参数。
   9. std::map<int64_t, std::string> g_roiStrMap; // 时间戳和ROI信息映射。
   10. std::mutex g_roiMutex;

   12. void Recorder::ConvertToRoi(int64_t timestamp, std::vector<FaceRect>* faceRectVec)
   13. {
   14. std::string mergedRoiStr;
   15. // 遍历所有faceRect。
   16. for (const auto& faceRect : faceRectVec) {
   17. // 归一化坐标转像素坐标。
   18. int left = static_cast<int32_t>(faceRect.topLeftX * width);
   19. int top = static_cast<int32_t>(faceRect.topLeftY * height);
   20. int right = static_cast<int32_t>(faceRect.width * width) + left;
   21. int bottom = static_cast<int32_t>(faceRect.height * height) + top;

   23. // 拼接当前人脸框的格式字符串（top,left-bottom,right=QpOffset;）。
   24. std::ostringstream oss;
   25. oss << mergedRoiStr; // 拼接已有片段。
   26. oss << top << "," << left << "-" << bottom << "," << right << "=" << qpOffset << ";";
   27. mergedRoiStr = oss.str();
   28. }

   30. if (!mergedRoiStr.empty()) {
   31. std::lock_guard<std::mutex> lock(g_roiMutex);
   32. // 此场景可获取视频帧时间戳，基于时间戳匹配。
   33. g_roiStrMap[timestamp] = mergedRoiStr;
   34. }
   35. }
   ```
5. 基于视频帧时间戳查找匹配的ROI信息。

   需要包含的头文件。

   ```
   1. #include <EGL/egl.h>
   2. #include <EGL/eglext.h>
   3. #include <GLES3/gl3.h>
   4. #include <GLES2/gl2ext.h>
   5. #include <native_image/native_image.h>
   ```

   创建NativeImage用来接收视频帧。

   ```
   1. GLuint textureId;
   2. glGenTextures(1, &textureId);
   3. // 创建NativeImage实例，关联纹理。
   4. OH_NativeImage* image = OH_NativeImage_Create(textureId, GL_TEXTURE_EXTERNAL_OES);
   ```

   获取NativeImage对应NativeWindow，作为相机预览流的目标窗口。并通过OH\_NativeImage\_SetOnFrameAvailableListener注册回调OH\_OnFrameAvailableListener获取视频帧更新。

   ```
   1. // 在回调后更新NativeImage。
   2. int32_t ret = OH_NativeImage_UpdateSurfaceImage(image);
   3. if (ret != 0) {
   4. // 异常处理。
   5. }
   6. // 获取视频帧时间戳。
   7. int64_t imageTimeStamp = OH_NativeImage_GetTimestamp(image);
   8. // 使用视频帧时间戳找到与之对应的ROI信息。
   9. std::lock_guard<std::mutex> lock(g_roiMutex);
   10. auto it = g_roiStrMap.find(imageTimeStamp);
   11. std::string noRoiStr = ";"; // 随元数据配置方式，需配置非空无效字符串关闭本视频帧ROI编码。
   12. std::string roiInfo = (it != g_roiStrMap.end()) ? it->second : noRoiStr;
   ```
6. 将ROI信息设置到视频帧NativeBuffer元数据中。

   需要包含的头文件。

   ```
   1. #include <multimedia/player_framework/native_avcodec_videoencoder.h>
   2. #include <multimedia/player_framework/native_avcodec_base.h>
   3. #include <native_window/external_window.h>
   4. #include <native_buffer/native_buffer.h>
   ```

   经过系列egl处理后，生成了用于编码的视频帧纹理。需要使用eglSwapBuffers函数将纹理绘制到编码器的输入NativeWindow中。编码输入NativeWindow获取方式如下。

   ```
   1. OH_AVCodec *codec = OH_VideoEncoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
   2. OHNativeWindow *nativeWindow = nullptr;
   3. OH_VideoEncoder_GetSurface(codec, &nativeWindow);
   ```

   绘制之前获取最新的NativeBuffer，并配置ROI信息。绘制过程可参考[OpenGLES示例](../harmonyos-references/opengles.md#简单示例)，最终通过eglSwapBuffers送绘制好的数据到编码器进行编码。

   ```
   1. int fenceFd = -1;
   2. OHNativeWindowBuffer *winBuffer = nullptr;
   3. // 从Surface中请求一帧OHNativeWindowBuffer。
   4. int32_t ret = OH_NativeWindow_NativeWindowRequestBuffer(nativeWindow, &winBuffer, &fenceFd);
   5. if (ret != 0) {
   6. // 异常处理。
   7. }
   8. // 将OHNativeWindowBuffer转换为NativeBuffer。
   9. OH_NativeBuffer *nativeBuffer = nullptr;
   10. OH_NativeBuffer_FromNativeWindowBuffer(winBuffer, &nativeBuffer);
   11. // 配置ROI信息到NativeBuffer元数据中。
   12. int32_t ret = OH_NativeBuffer_SetMetaDataValue(nativeBuffer,
   13. OH_NativeBuffer_MetaDataKey::OH_REGION_OF_INTEREST_METADATA, roiInfo.size,
   14. reinterpret_cast<uint8_t *>(roiInfo.data()));
   15. if (ret != 0) {
   16. // 异常处理。
   17. }
   ```

### Surface模式下通过编码输入回调接口配置ROI

在此场景中，视频帧被直接送入编码器窗口（如图3所示）。

相机输出视频帧和元数据（如果存在）的时间相近。设置编码输入参数的回调后，编码器在接收到视频帧时会触发回调。在回调中，如果获取成功，则该视频帧包含匹配的ROI信息；如果获取超时，则该视频帧不包含匹配的ROI信息。

**图3：编码输入参数回调接口配置ROI流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/aOVOWLiBRkee92-WawFq1Q/zh-cn_image_0000002589244855.png?HW-CC-KV=V1&HW-CC-Date=20260429T053440Z&HW-CC-Expire=86400&HW-CC-Sign=C1F154AE2C09B29EE1544014BB99B944904AF4E149FB87589C3533457BFAE78E)

详细开发步骤如下：

1. 在CMakeList.txt中链接动态库。

   ```
   1. set(BASE_LIBRARY
   2. libnative_media_codecbase.so libnative_media_core.so libnative_media_venc.so
   3. )
   4. target_link_libraries(recorder PUBLIC ${BASE_LIBRARY})
   ```

   说明

   上述'recorder'字样仅为示例，此处应由开发者根据具体的CMake工程目标名称进行替换。
2. 监听相机元数据回调接口获取人脸位置信息。

   同[Surface模式下通过NativeBuffer接口配置ROI](video-encoding-roi.md#surface模式下通过nativebuffer接口配置roi)步骤2。
3. Native层解析TS层传递的人脸位置信息。

   同[Surface模式下通过NativeBuffer接口配置ROI](video-encoding-roi.md#surface模式下通过nativebuffer接口配置roi)步骤3。
4. 转换成ROI信息格式字符串并保存。

   编码参数回调的设计中未包含视频帧的时间戳字段，为配合后续对齐，需要使用线程安全的先入先出队列管理ROI信息，参考实现如下。

   ```
   1. // RoiFifoQueue.h
   2. #include <queue>
   3. #include <string>
   4. #include <mutex>
   5. #include <condition_variable>
   6. #include <chrono>

   8. class RoiFifoQueue {
   9. public:
   10. void push(const std::string& roiStr) {
   11. std::lock_guard<std::mutex> lock(mtx);
   12. roiQueue.push(roiStr);
   13. cv.notify_one(); // 通知等待的取数线程。
   14. }

   16. bool pop(std::string& outRoiStr, const std::chrono::milliseconds& timeout) {
   17. std::unique_lock<std::mutex> lock(mtx);
   18. if (!cv.wait_for(lock, timeout, [this]() {
   19. return !roiQueue.empty() || isStopped;
   20. })) {
   21. return false; // 超时则无ROI。
   22. }
   23. if (isStopped || roiQueue.empty()) {
   24. return false;
   25. }
   26. outRoiStr = roiQueue.front();
   27. roiQueue.pop();
   28. return true;
   29. }

   31. void clear() {
   32. std::lock_guard<std::mutex> lock(mtx);
   33. while (!roiQueue.empty()) {
   34. roiQueue.pop();
   35. }
   36. }

   38. void stop() {
   39. std::lock_guard<std::mutex> lock(mtx);
   40. isStopped = true;
   41. cv.notify_all(); // 唤醒所有等待的线程。
   42. }

   44. ~RoiFifoQueue() {
   45. stop();
   46. }
   47. };
   48. private:
   49. std::queue<std::string> roiQueue;    // 存储合并后的完整ROI字符串。
   50. std::mutex mtx;                      // 互斥锁保护队列。
   51. std::condition_variable cv;          // 条件变量用于超时等待。
   52. bool isStopped = false;              // 停止标志。
   ```

   转换成ROI信息格式并保存在队列中。

   ```
   1. #include <sstream>
   2. #include "RoiFifoQueue.h"

   4. const int width = 1920;   // 视频帧宽度。
   5. const int height = 1080;  // 视频帧高度。
   6. const int qpOffset = -6;  // QP偏移参数。
   7. RoiFifoQueue g_roiStrQueue;

   9. void Recorder::ConvertToRoi(int64_t timestamp, std::vector<FaceRect>* faceRectVec)
   10. {
   11. std::string mergedRoiStr;
   12. // 遍历所有faceRect。
   13. for (const auto& faceRect : faceRectVec) {
   14. // 归一化坐标转像素坐标。
   15. int left = static_cast<int32_t>(faceRect.topLeftX * width);
   16. int top = static_cast<int32_t>(faceRect.topLeftY * height);
   17. int right = static_cast<int32_t>(faceRect.width * width) + left;
   18. int bottom = static_cast<int32_t>(faceRect.height * height) + top;

   20. // 拼接当前人脸框的格式字符串（top,left-bottom,right=QpOffset;）。
   21. std::ostringstream oss;
   22. oss << mergedRoiStr; // 拼接已有片段。
   23. oss << top << "," << left << "-" << bottom << "," << right << "=" << qpOffset << ";";
   24. mergedRoiStr = oss.str();
   25. }

   27. if (!mergedRoiStr.empty()) {
   28. std::lock_guard<std::mutex> lock(g_roiMutex);
   29. // 此场景可获取视频帧时间戳，基于时间戳匹配。
   30. g_roiStrQueue.push(mergedRoiStr);
   31. }
   32. }
   ```
5. 在编码输入参数回调中配置ROI信息。

   需要包含的头文件。

   ```
   1. #include <multimedia/player_framework/native_avcodec_videoencoder.h>
   2. #include <multimedia/player_framework/native_avcodec_base.h>
   3. #include <multimedia/player_framework/native_avformat.h>
   4. #include <multimedia/player_framework/native_avbuffer.h>
   ```

   创建编码器。

   ```
   1. OH_AVCodec *codec = OH_VideoEncoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
   ```

   视频编码的详细操作步骤请参考[视频编码](video-encoding.md)开发指南，下面仅针对ROI编码做具体说明。

   ```
   1. const std::chrono::milliseconds ROI_WAIT_TIMEOUT = std::chrono::milliseconds(4); // 4ms超时。
   2. static void OnNeedInputParameter(OH_AVCodec *codec, uint32_t index, OH_AVFormat *parameter, void *userData)
   3. {
   4. (void)codec;
   5. (void)userData;
   6. std::string roiInfo = "";
   7. if (!g_roiStrQueue.pop(roiInfo, ROI_WAIT_TIMEOUT)) {
   8. roiInfo = ";"; // 与NativeBuffer通路统一。
   9. }
   10. // 找到ROI配置，ROI编码生效；找不到ROI，普通编码生效。
   11. OH_AVFormat_SetStringValue(parameter, OH_MD_KEY_VIDEO_ENCODER_ROI_PARAMS, roiInfo.c_str());
   12. OH_VideoEncoder_PushInputParameter(codec, index);
   13. }

   15. // 注册随帧参数回调。
   16. OH_VideoEncoder_OnNeedInputParameter inParaCb = OnNeedInputParameter;
   17. OH_VideoEncoder_RegisterParameterCallback(codec, inParaCb, nullptr);
   ```

### Buffer模式下配置ROI

在该场景中，视频帧和ROI均由应用提供，并采用buffer模式编码。开发者可以参考前文所述的**基于时间戳匹配**或**基于回调时机匹配**两种对齐方式来实现ROI与视频帧的对齐，并在编码输入Buffer回调中完成ROI参数的配置（如图4所示）。

**图4：编码输入Buffer回调接口配置ROI流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/_HdDsCAPSG-3O3ZSNDqPUg/zh-cn_image_0000002558765050.png?HW-CC-KV=V1&HW-CC-Date=20260429T053440Z&HW-CC-Expire=86400&HW-CC-Sign=8C0684E5E3D25D768CA44A1C20AB682D4A1C13B43707C5A3E82061371A85B661)

准备步骤同[Surface模式下通过编码输入回调接口配置ROI](video-encoding-roi.md#surface模式下通过编码输入回调接口配置roi)步骤1-4，此处仅说明配置差异。

在编码输入Buffer回调中配置ROI信息。

```
1. static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
2. {
3. (void)codec;
4. (void)userData;
5. auto format = std::shared_ptr<OH_AVFormat>(OH_AVBuffer_GetParameter(buffer), OH_AVFormat_Destroy);
6. if (format == nullptr) {
7. // 异常处理。
8. }
9. std::string roiInfo = "";
10. if (!g_roiStrQueue.pop(roiInfo, ROI_WAIT_TIMEOUT)) {
11. roiInfo = ";"; // 与NativeBuffer通路统一。
12. }
13. OH_AVFormat_SetStringValue(format.get(), OH_MD_KEY_VIDEO_ENCODER_ROI_PARAMS, roiInfo.c_str());

15. // 此处还需做视频帧填充，此处忽略。
16. // 通知编码器buffer输入完成。
17. OH_VideoEncoder_PushInputBuffer(codec, index);
18. }

20. static void OnStreamChanged(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
21. {
22. // 此处仅作定义，实现忽略。
23. }

25. static void OnError(OH_AVCodec *codec, int32_t errorCode, void *userData)
26. {
27. // 此处仅作定义，实现忽略。
28. }

30. static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
31. {
32. // 此处仅作定义，实现忽略。
33. }

35. OH_AVCodecCallback cb = {&OnError, &OnStreamChanged, &OnNeedInputBuffer, &OnNewOutputBuffer};
36. OH_AVErrCode ret = OH_VideoEncoder_RegisterCallback(videoEnc, cb, nullptr);
```
