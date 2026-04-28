---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vulkan-oh-external-memory-guidelines
title: Vulkan External Memory开发指导
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan开发指导 > Vulkan External Memory开发指导
category: harmonyos-references
scraped_at: 2026-04-28T08:19:33+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:67ada52612936c470d99e420c5ddaf82553d6c67d8ada75d3a853f7152f46e02
---

## 场景介绍

VK\_OHOS\_external\_memory 扩展用于在GPU Vulkan环境下与HarmonyOS的本机缓冲区（OHNativeBuffer）之间做零拷贝的内存共享。

该扩展允许：把由HarmonyOS或其他组件（Camera、RenderService、视频解码器、OHNativeWindow等）创建的OHNativeBuffer导入为Vulkan内存（并绑定到VkImage/VkBuffer）。

这可以实现视频帧、相机输出、图像解码器等在生产端与Vulkan渲染/计算端的高效共享，避免额外拷贝或像素转换。

所以，本指导将介绍实现视频解码器与渲染器零拷贝：将解码器输出OHNativeBuffer，直接导入Vulkan。

## 接口说明

### 结构体

| 名称 | 描述 |
| --- | --- |
| [VkNativeBufferPropertiesOHOS](capi-vulkan-vknativebufferpropertiesohos.md) | 包含了NativeBuffer的属性。 |
| [VkNativeBufferFormatPropertiesOHOS](capi-vulkan-vknativebufferformatpropertiesohos.md) | 包含了NativeBuffer的一些格式属性。 |
| [VkImportNativeBufferInfoOHOS](capi-vulkan-vkimportnativebufferinfoohos.md) | 包含了OH\_NativeBuffer结构体的指针。 |
| [VkMemoryGetNativeBufferInfoOHOS](capi-vulkan-vkmemorygetnativebufferinfoohos.md) | 用于从Vulkan内存中获取OH\_NativeBuffer。 |
| [VkExternalFormatOHOS](capi-vulkan-vkexternalformatohos.md) | 表示外部定义的格式标识符。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [vkGetNativeBufferPropertiesOHOS](capi-vulkan-ohos-h.md#vkgetnativebufferpropertiesohos) (VkDevice device, const struct OH\_NativeBuffer \*buffer, [VkNativeBufferPropertiesOHOS](capi-vulkan-vknativebufferpropertiesohos.md) \*pProperties) | 获取OH\_NativeBuffer属性。 |

## 开发步骤

以下步骤说明了如何将视频解码器输出的本机缓冲区（OHNativeBuffer）导入为Vulkan内存，并绑定到VkImage/VkBuffer。

1. 启动渲染子线程，初始化Vulkan环境，动态加载libvulkan.so, 并加载Vulkan基础函数的指针。

   ```
   1. void VulkanRenderThread::ThreadMainLoop() {
   2. threadId_ = std::this_thread::get_id();
   3. if (!InitRenderContext()) {
   4. return;
   5. }
   6. if (!InitNativeVsync()) {
   7. return;
   8. }
   9. if (!CreateNativeImage()) {
   10. return;
   11. }
   12. while (running_) {
   13. {
   14. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread", "Waiting for Vsync.");
   15. std::unique_lock<std::mutex> Lock(wakeUpMutex_);
   16. wakeUpCond_.wait(Lock, [this]() { return wakeup_ || vSyncCnt_ > 0 || availableFrameCnt_ > 0; });
   17. wakeup_ = false;
   18. vSyncCnt_--;
   19. (void)OH_NativeVSync_RequestFrame(nativeVsync_, &VulkanRenderThread::OnVsync, this);
   20. }

   22. std::vector<VulkanRenderTask> tasks;
   23. {
   24. std::lock_guard<std::mutex> lock(taskMutex_);
   25. tasks.swap(tasks_);
   26. }
   27. for (const auto &task : tasks) {
   28. task(*vulkanRenderContext_);
   29. }
   30. if (availableFrameCnt_ <= 0) {
   31. continue;
   32. }
   33. DrawImage();
   34. availableFrameCnt_--;
   35. }
   36. }
   ```

   动态加载libvulkan.so，并加载Vulkan基础函数的指针。

   ```
   1. // Dynamically load Vulkan library and base function pointers
   2. bool LoadVulkanLibrary() {
   3. // Load vulkan library
   4. constexpr char *path = "libvulkan.so";
   5. dlerror();
   6. g_libVulkan = dlopen(path, RTLD_NOW | RTLD_LOCAL);
   7. if (!g_libVulkan) {
   8. OH_LOG_ERROR(LOG_APP, "Failed to load vulkan Library, %{public}s", dlerror());
   9. return false;
   10. }

   12. // // Load base function pointers
   13. vkEnumerateInstanceExtensionProperties = reinterpret_cast<PFN_vkEnumerateInstanceExtensionProperties>(
   14. dlsym(g_libVulkan, "vkEnumerateInstanceExtensionProperties"));
   15. vkEnumerateInstanceLayerProperties = reinterpret_cast<PFN_vkEnumerateInstanceLayerProperties>(
   16. dlsym(g_libVulkan, "vkEnumerateInstanceLayerProperties"));
   17. vkCreateInstance = reinterpret_cast<PFN_vkCreateInstance>(dlsym(g_libVulkan, "vkCreateInstance"));
   18. vkGetInstanceProcAddr = reinterpret_cast<PFN_vkGetInstanceProcAddr>(dlsym(g_libVulkan, "vkGetInstanceProcAddr"));
   19. vkGetDeviceProcAddr = reinterpret_cast<PFN_vkGetDeviceProcAddr>(dlsym(g_libVulkan, "vkGetDeviceProcAddr"));

   21. return true;
   22. }
   ```
2. 创建NativeImage对象作为OHNativeBuffer的消费端，并根据NativeImage对象获取对应的NativeWindow对象，将NativeWindow句柄传给视频编解码，作为OHNativeBuffer的生产端，用于生产视频帧内容。

   ```
   1. bool VulkanRenderThread::CreateNativeImage() {
   2. nativeImage_ = OH_ConsumerSurface_Create();
   3. if (nativeImage_ == nullptr) {
   4. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread", "OH_NativeImage_Create failed.");
   5. return false;
   6. }
   7. int ret = 0;
   8. {
   9. std::lock_guard<std::mutex> Lock(nativeImageSurfaceIdMutex_);
   10. nativeImageWindow_ = OH_NativeImage_AcquireNativeWindow(nativeImage_);
   11. ret = OH_NativeImage_GetSurfaceId(nativeImage_, &nativeImageSurfaceId_);
   12. }
   13. if (ret != 0) {
   14. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread",
   15. "OH_NativeImage_GetSurfaceId failed, ret is %{public}d.", ret);
   16. return false;
   17. }

   19. nativeImageFrameAvailableListener_.context = this;
   20. nativeImageFrameAvailableListener_.onFrameAvailable = &VulkanRenderThread::OnNativeImageFrameAvailable;
   21. ret = OH_NativeImage_SetOnFrameAvailableListener(nativeImage_, nativeImageFrameAvailableListener_);
   22. if (ret != 0) {
   23. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread",
   24. "OH_NativeImage_SetonFrameAvailableListener failed, ret is %{public}d.", ret);
   25. return false;
   26. }
   27. return true;
   28. }
   ```
3. 获取XComponent的NativeWindow对象，根据NativeWindow对象创建出Vulkan环境的VkSurface，用于绘制显示内容。

   ```
   1. void VulkanRenderThread::UpdateNativeWindow(void *window, uint64_t width, uint64_t height) {
   2. OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_PRINT_DOMAIN, "RenderThread", "UpdateNativeWindow.");
   3. auto nativeWindow = reinterpret_cast<OHNativeWindow *>(window);
   4. PostTask([this, nativeWindow, width, height](VulkanRender &renderContext) {
   5. if (nativeWindow_ != nativeWindow) {
   6. if (nativeWindow_ != nullptr) {
   7. (void)OH_NativeWindow_NativeObjectUnreference(nativeWindow_);
   8. }
   9. nativeWindow_ = nativeWindow;
   10. if (nativeWindow_ != nullptr) {
   11. (void)OH_NativeWindow_NativeObjectReference(nativeWindow_);
   12. }
   13. }
   14. if (nativeWindow_ != nullptr) {
   15. vulkanRenderContext_->SetupWindow(nativeWindow_);
   16. }
   17. });
   18. }
   ```

   同时更新初始化Vulkan的上下文，包括Vulkan的实列、选择物理设备、创建渲染管线等。

   ```
   1. void VulkanRender::SetupWindow(NativeWindow *nativeWindow) {
   2. nativeWindow_ = nativeWindow;
   3. CreateInstance();
   4. vkExample::utils::LoadVulkanFunctions(instance);
   5. CreateSurface();
   6. PickPhysicalDevice();
   7. CreateLogicalDevice();
   8. vkExample::utils::LoadVulkanFunctions(device);

   10. createSwapChain();
   11. createRenderPass();
   12. createFrameBuffersAndImages();
   13. createVertexBuffer();
   14. createUniformBuffer();
   15. deviceInfoInitialized = true;
   16. }
   ```

   通过vkCreateSurfaceOHOS()创建VkSurface对象。

   ```
   1. bool VulkanRender::CreateSurface() {
   2. VkSurfaceCreateInfoOHOS surfaceCreateInfo{};
   3. surfaceCreateInfo.sType = VK_STRUCTURE_TYPE_SURFACE_CREATE_INFO_OHOS;
   4. if (nativeWindow_ == nullptr) {
   5. OH_LOG_INFO(LOG_APP, "nativeWindow_ is nullptr.Failed to create surface !");
   6. return false;
   7. }
   8. surfaceCreateInfo.window = nativeWindow_;
   9. surfaceCreateInfo.flags = 0;
   10. surfaceCreateInfo.pNext = nullptr;
   11. bool res = CheckResult(vkCreateSurfaceOHOS(instance, &surfaceCreateInfo, nullptr, &surface));
   12. return res;
   13. }
   ```
4. 初始化视频解码的环境，包括初始化解封装器、初始化解码器。

   ```
   1. napi_value PluginRender::StartPlayer(napi_env env, napi_callback_info info)
   2. {
   3. SampleInfo sampleInfo;
   4. size_t argc = 4;
   5. napi_value args[4] = {nullptr};
   6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   7. napi_get_value_int32(env, args[0], &sampleInfo.inputFd);
   8. napi_get_value_int64(env, args[1], &sampleInfo.inputFileOffset);
   9. napi_get_value_int64(env, args[2], &sampleInfo.inputFileSize);
   10. size_t length = 0;
   11. napi_status status = napi_get_value_string_utf8(env, args[3], nullptr, 0, &length);
   12. char* buf = new char[length + 1];
   13. std::memset(buf, 0, length + 1);
   14. status = napi_get_value_string_utf8(env, args[3], buf, length + 1, &length);
   15. std::string type = buf;
   16. PluginRender *render = PluginRender::GetInstance(type);
   17. if (render != nullptr) {
   18. if (type == "Vulkan") {
   19. sampleInfo.window = render->vulkanRenderThread_->GetNativeImageWindow();
   20. } else {
   21. sampleInfo.window = render->nativeWindow;
   22. }
   23. }
   24. int32_t ret = Player::GetInstance().Init(sampleInfo);
   25. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   26. return nullptr;
   27. }
   28. Player::GetInstance().Start();
   29. return nullptr;
   30. }
   ```
5. 启动解码器、解码输入子线程、解码输出子线程。

   ```
   1. int32_t Player::Start() {
   2. std::unique_lock<std::mutex> lock(mutex_);
   3. int32_t ret;
   4. if (isStarted_ || demuxer_ == nullptr) {
   5. OH_LOG_ERROR(LOG_APP, "Already started.");
   6. return AVCODEC_SAMPLE_ERR_ERROR;
   7. }

   9. if (videoDecContext_) {
   10. ret = videoDecoder_->Start();
   11. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   12. OH_LOG_ERROR(LOG_APP, "Video Decoder start failed");
   13. lock.unlock();
   14. StartRelease();
   15. return AVCODEC_SAMPLE_ERR_ERROR;
   16. }
   17. isStarted_ = true;
   18. videoDecInputThread_ = std::make_unique<std::thread>(&Player::VideoDecInputThread, this);
   19. videoDecOutputThread_ = std::make_unique<std::thread>(&Player::VideoDecOutputThread, this);

   21. if (videoDecInputThread_ == nullptr || videoDecOutputThread_ == nullptr) {
   22. OH_LOG_ERROR(LOG_APP, "Create thread failed");
   23. lock.unlock();
   24. StartRelease();
   25. return AVCODEC_SAMPLE_ERR_ERROR;
   26. }
   27. }

   29. OH_LOG_INFO(LOG_APP, "Succeed");
   30. doneCond_.notify_all();
   31. return AVCODEC_SAMPLE_ERR_OK;
   32. }
   ```
6. 在解码输入子线程中，通过解封装器读取视频数据，并交给解码器。

   ```
   1. void Player::VideoDecInputThread() {
   2. while (true) {
   3. if (!isStarted_) {
   4. OH_LOG_ERROR(LOG_APP, "Decoder input thread out");
   5. break;;
   6. }

   8. std::unique_lock<std::mutex> lock(videoDecContext_->inputMutex);
   9. bool condRet = videoDecContext_->inputCond.wait_for(
   10. lock, 5s, [this]() { return !isStarted_ || !videoDecContext_->inputBufferInfoQueue.empty(); });
   11. if (!isStarted_) {
   12. OH_LOG_ERROR(LOG_APP, "Work done, thread out");
   13. break;
   14. }
   15. if (videoDecContext_->inputBufferInfoQueue.empty()) {
   16. OH_LOG_ERROR(LOG_APP, "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
   17. continue;
   18. }

   20. CodecBufferInfo bufferInfo = videoDecContext_->inputBufferInfoQueue.front();
   21. videoDecContext_->inputBufferInfoQueue.pop();
   22. videoDecContext_->inputFrameCount++;
   23. lock.unlock();

   25. demuxer_->ReadSample(demuxer_->GetVideoTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
   26. bufferInfo.attr);

   28. int32_t ret = videoDecoder_->PushInputBuffer(bufferInfo);
   29. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   30. OH_LOG_ERROR(LOG_APP, "Push data failed, thread out");
   31. break;
   32. }

   34. if (bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   35. OH_LOG_ERROR(LOG_APP, "Catch EOS, thread out");
   36. break;
   37. }
   38. }
   39. }
   ```
7. 在解码输出子线程中，将解码后的视频提交给输出Surface。

   ```
   1. void Player::VideoDecOutputThread() {
   2. sampleInfo_.frameInterval = MICROSECOND / sampleInfo_.frameRate;
   3. while (true) {
   4. thread_local auto lastPushTime = std::chrono::system_clock::now();
   5. if (!isStarted_) {
   6. OH_LOG_ERROR(LOG_APP, "Decoder output thread out");
   7. break;
   8. }
   9. std::unique_lock<std::mutex> lock(videoDecContext_->outputMutex);
   10. bool condRet = videoDecContext_->outputCond.wait_for(
   11. lock, 5s, [this]() { return !isStarted_ || !videoDecContext_->outputBufferInfoQueue.empty(); });
   12. if (!isStarted_) {
   13. OH_LOG_ERROR(LOG_APP, "Decoder output thread out");
   14. break;
   15. }
   16. if (videoDecContext_->outputBufferInfoQueue.empty()) {
   17. OH_LOG_ERROR(LOG_APP, "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
   18. continue;
   19. }

   21. CodecBufferInfo bufferInfo = videoDecContext_->outputBufferInfoQueue.front();
   22. videoDecContext_->outputBufferInfoQueue.pop();
   23. if (bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   24. OH_LOG_ERROR(LOG_APP, "Catch EOS, thread out");
   25. break;
   26. }
   27. videoDecContext_->outputFrameCount++;
   28. OH_LOG_INFO(LOG_APP,"Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}ld",
   29. videoDecContext_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
   30. bufferInfo.attr.pts);
   31. lock.unlock();

   33. int32_t ret = videoDecoder_->FreeOutputBuffer(bufferInfo.bufferIndex, true);
   34. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   35. OH_LOG_ERROR(LOG_APP, "Decoder output thread out");
   36. break;
   37. }

   39. std::this_thread::sleep_until(lastPushTime + std::chrono::microseconds(sampleInfo_.frameInterval));
   40. lastPushTime = std::chrono::system_clock::now();
   41. }
   42. StartRelease();
   43. }
   ```
8. 在NativeImage有可用数据后，通过OH\_NativeImage\_AcquireNativeWindowBuffer()获取视频数据，并通过OH\_NativeBuffer\_FromNativeWindowBuffer()转化NativeBuffer的类型。

   ```
   1. void VulkanRenderThread::DrawImage() {
   2. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "VulkanRenderThread", "DrawImage.");
   3. int ret;
   4. OHNativeWindowBuffer *inBuffer = nullptr;
   5. OH_NativeBuffer *nativeBuffer = nullptr;
   6. int32_t fenceFd1 = -1;
   7. ret = OH_NativeImage_AcquireNativeWindowBuffer(nativeImage_, &inBuffer, &fenceFd1);
   8. ret = OH_NativeWindow_NativeObjectReference(inBuffer);
   9. ret = OH_NativeBuffer_FromNativeWindowBuffer(inBuffer, &nativeBuffer);
   10. if (nativeBuffer == nullptr) {
   11. OH_NativeWindow_NativeObjectUnreference(inBuffer);
   12. OH_NativeImage_ReleaseNativeWindowBuffer(nativeImage_, inBuffer, -1);
   13. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "VulkanRenderThread", "nativeBuffer is null.");
   14. return;
   15. }
   16. ret = OH_NativeImage_GetTransformMatrix(nativeImage_, matrix_);
   17. int32_t transformTmp = 0;
   18. ComputeTransform(transformTmp, matrix_);
   19. vulkanRenderContext_->hwBufferToTexture(nativeBuffer, matrix_);
   20. vulkanRenderContext_->render();
   21. if (lastInBuffer_ != nullptr) {
   22. OH_NativeWindow_NativeObjectUnreference(lastInBuffer_);
   23. OH_NativeImage_ReleaseNativeWindowBuffer(nativeImage_, lastInBuffer_, -1);
   24. }
   25. lastInBuffer_ = inBuffer;
   26. }
   ```
9. Vulkan根据NativeBuffer创建对应的ImageView用于渲染显示，同时创建对应格式的采样器，将YUV格式的图像采样成RGBA的图像，用于正确的渲染显示。

   说明

   * API version 23之前，基于标准库VkExternalMemoryImageCreateInfo结构体，系统支持扩展类型VK\_EXTERNAL\_MEMORY\_HANDLE\_TYPE\_OHOS\_NATIVE\_BUFFER\_BIT\_OHOS。
   * 从API version 23开始，VK\_EXTERNAL\_MEMORY\_HANDLE\_TYPE\_OHOS\_NATIVE\_BUFFER\_BIT\_OHOS已废弃，请改用VK\_EXTERNAL\_MEMORY\_HANDLE\_TYPE\_OH\_NATIVE\_BUFFER\_BIT\_OHOS。

   ```
   1. void VulkanRender::hwBufferToTexture(OH_NativeBuffer *buffer, float transformMatrix[16]) {
   2. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "VulkanRenderThread", "hwBufferToTexture.");
   3. if (!deviceInfoInitialized) {
   4. return;
   5. }
   6. UniformBufferObject ubo{};
   7. memcpy(ubo.mvp, transformMatrix, sizeof(float) * 16);
   8. memcpy(buffersInfo.uniformBufferMapped, &ubo, sizeof(ubo));
   9. VkNativeBufferFormatPropertiesOHOS nbFormatProps = {
   10. .sType = VK_STRUCTURE_TYPE_NATIVE_BUFFER_FORMAT_PROPERTIES_OHOS,
   11. .pNext = nullptr
   12. };
   13. VkNativeBufferPropertiesOHOS nbProps = {.sType = VK_STRUCTURE_TYPE_NATIVE_BUFFER_PROPERTIES_OHOS,
   14. .pNext = &nbFormatProps};
   15. CheckResult(vkGetNativeBufferPropertiesOHOS(device, buffer, &nbProps));

   17. VkImportNativeBufferInfoOHOS importBufferInfo = {
   18. .sType = VK_STRUCTURE_TYPE_IMPORT_NATIVE_BUFFER_INFO_OHOS,
   19. .pNext = nullptr,
   20. .buffer = buffer
   21. };

   23. VkMemoryDedicatedAllocateInfo dedicatedAllocateInfo = {
   24. .sType = VK_STRUCTURE_TYPE_MEMORY_DEDICATED_ALLOCATE_INFO,
   25. .pNext = &importBufferInfo,
   26. .image = VK_NULL_HANDLE, // will be set later
   27. .buffer = VK_NULL_HANDLE
   28. };

   30. VkPhysicalDeviceMemoryProperties physicalDeviceMemProps;
   31. uint32_t foundTypeIndex = 0;
   32. vkGetPhysicalDeviceMemoryProperties(gpuDevice, &physicalDeviceMemProps);
   33. uint32_t memTypeCnt = physicalDeviceMemProps.memoryTypeCount;
   34. for (uint32_t i = 0; i < memTypeCnt; ++i) {
   35. if (nbProps.memoryTypeBits & (1 << i)) {
   36. const VkPhysicalDeviceMemoryProperties &pdmp = physicalDeviceMemProps;
   37. uint32_t supportedFLags = pdmp.memoryTypes[i].propertyFlags & VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT;
   38. if (supportedFLags == VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT) {
   39. foundTypeIndex = i;
   40. break;
   41. }
   42. }
   43. }

   45. VkMemoryAllocateInfo allocInfo{
   46. .sType = VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO,
   47. .pNext = &dedicatedAllocateInfo,
   48. .allocationSize = nbProps.allocationSize,
   49. .memoryTypeIndex = 0 // Memory type assigned in the next step
   50. };

   52. mapMemoryTypeToIndex(nbProps.memoryTypeBits, VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT, &allocInfo.memoryTypeIndex);
   53. VkExternalFormatOHOS externalFormat;
   54. externalFormat.sType = VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_OHOS;
   55. externalFormat.pNext = nullptr;
   56. externalFormat.externalFormat = 0;
   57. if (nbFormatProps.format == VK_FORMAT_UNDEFINED) {
   58. externalFormat.externalFormat = nbFormatProps.externalFormat;
   59. }

   61. VkExternalMemoryImageCreateInfo externalMemoryImageInfo = {
   62. .sType = VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO,
   63. .pNext = &externalFormat,
   64. .handleTypes = VK_EXTERNAL_MEMORY_HANDLE_TYPE_OH_NATIVE_BUFFER_BIT_OHOS,
   65. };

   67. VkImageUsageFlags usageFlags = VK_IMAGE_USAGE_SAMPLED_BIT;
   68. if (nbFormatProps.format != VK_FORMAT_UNDEFINED) {
   69. usageFlags = usageFlags | VK_IMAGE_USAGE_TRANSFER_SRC_BIT | VK_IMAGE_USAGE_TRANSFER_DST_BIT |
   70. VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT | VK_IMAGE_USAGE_INPUT_ATTACHMENT_BIT;
   71. }
   72. OH_NativeBuffer_Config config;
   73. OH_NativeBuffer_GetConfig(buffer, &config);
   74. VkImageCreateInfo image_create_info = {
   75. .sType = VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO,
   76. .pNext = &externalMemoryImageInfo,
   77. .flags = 0,
   78. .imageType = VK_IMAGE_TYPE_2D,
   79. .format = nbFormatProps.format,
   80. .extent = {static_cast<uint32_t>(config.width), static_cast<uint32_t>(config.height), 1},
   81. .mipLevels = 1,
   82. .arrayLayers = 1,
   83. .samples = VK_SAMPLE_COUNT_1_BIT,
   84. .tiling = VK_IMAGE_TILING_OPTIMAL,
   85. .usage = usageFlags,
   86. .sharingMode = VK_SHARING_MODE_EXCLUSIVE,
   87. .queueFamilyIndexCount = 1,
   88. .pQueueFamilyIndices = &queueFamilyIndex_,
   89. // VK_IMAGE_LAYOUT_UNDEFINED is mandatory when using external memory
   90. .initialLayout = VK_IMAGE_LAYOUT_UNDEFINED
   91. };

   93. CheckResult(vkCreateImage(device, &image_create_info, nullptr, &externalTextureImage));
   94. dedicatedAllocateInfo.image = externalTextureImage;
   95. CheckResult(vkAllocateMemory(device, &allocInfo, nullptr, &externalTextureMemory));
   96. CheckResult(vkBindImageMemory(device, externalTextureImage, externalTextureMemory, 0));

   98. VkSamplerYcbcrConversionCreateInfo ycbcrCreateInfo = {
   99. .sType = VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO,
   100. .ycbcrRange = nbFormatProps.suggestedYcbcrRange,
   101. .components = nbFormatProps.samplerYcbcrConversionComponents,
   102. .xChromaOffset = nbFormatProps.suggestedXChromaOffset,
   103. .yChromaOffset = nbFormatProps.suggestedYChromaOffset,
   104. .chromaFilter = VK_FILTER_LINEAR,
   105. .forceExplicitReconstruction = false
   106. };

   108. if (nbFormatProps.format == VK_FORMAT_UNDEFINED) {
   109. ycbcrCreateInfo.pNext = &externalFormat;
   110. ycbcrCreateInfo.format = VK_FORMAT_UNDEFINED;
   111. ycbcrCreateInfo.ycbcrModel = nbFormatProps.suggestedYcbcrModel;
   112. }

   114. CheckResult(
   115. vkCreateSamplerYcbcrConversion(device, &ycbcrCreateInfo, nullptr, &externalTextureInfo.ycbcrConversion));

   117. VkSamplerYcbcrConversionInfo convInfoWrap = {
   118. .sType = VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_INFO,
   119. .conversion = externalTextureInfo.ycbcrConversion,
   120. .pNext = nullptr,
   121. };

   123. VkImageViewCreateInfo view = {
   124. .sType = VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO,
   125. .pNext = &convInfoWrap,
   126. .flags = 0,
   127. .image = externalTextureImage,
   128. .viewType = VK_IMAGE_VIEW_TYPE_2D,
   129. .format = nbFormatProps.format,
   130. .components =
   131. {
   132. VK_COMPONENT_SWIZZLE_IDENTITY,
   133. VK_COMPONENT_SWIZZLE_IDENTITY,
   134. VK_COMPONENT_SWIZZLE_IDENTITY,
   135. VK_COMPONENT_SWIZZLE_IDENTITY
   136. },
   137. .subresourceRange = {VK_IMAGE_ASPECT_COLOR_BIT, 0, 1, 0, 1},
   138. };
   139. CheckResult(vkCreateImageView(device, &view, nullptr, &externalTextureInfo.view));

   141. // Create sampler
   142. const VkSamplerCreateInfo sampler = {
   143. .sType = VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO,
   144. .pNext = &convInfoWrap,
   145. .magFilter = VK_FILTER_NEAREST,
   146. .minFilter = VK_FILTER_NEAREST,
   147. .mipmapMode = VK_SAMPLER_MIPMAP_MODE_NEAREST,
   148. .addressModeU = VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE,
   149. .addressModeV = VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE,
   150. .addressModeW = VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE,
   151. .mipLodBias = 0.0f,
   152. .compareEnable = VK_FALSE,
   153. .anisotropyEnable = VK_FALSE,
   154. .maxAnisotropy = 1,
   155. .compareOp = VK_COMPARE_OP_NEVER,
   156. .minLod = 0.0f,
   157. .maxLod = 0.0f,
   158. .borderColor = VK_BORDER_COLOR_FLOAT_OPAQUE_WHITE,
   159. .unnormalizedCoordinates = VK_FALSE
   160. };
   161. CheckResult(vkCreateSampler(device, &sampler, nullptr, &externalTextureInfo.sampler));

   163. createDescriptorSetLayout();
   164. createDescriptorSet();

   166. VkDescriptorImageInfo imageInfo = {
   167. .sampler = externalTextureInfo.sampler,
   168. .imageView = externalTextureInfo.view,
   169. .imageLayout = VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL
   170. };

   172. VkDescriptorBufferInfo bufferInfo = {
   173. .buffer = buffersInfo.uniformBuf, .offset = 0, .range = sizeof(UniformBufferObject)};
   174. VkWriteDescriptorSet bufferWrite = {.sType = VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET,
   175. .dstSet = gfxPipelineInfo.descSet,
   176. .dstBinding = 0,
   177. .dstArrayElement = 0,
   178. .descriptorCount = 1,
   179. .descriptorType = VK_DESCRIPTOR_TYPE_UNIFORM_BUFFER,
   180. .pImageInfo = nullptr,
   181. .pBufferInfo = &bufferInfo,
   182. .pTexelBufferView = nullptr};
   183. VkWriteDescriptorSet imageWrite = {.sType = VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET,
   184. .dstSet = gfxPipelineInfo.descSet,
   185. .dstBinding = 1,
   186. .dstArrayElement = 0,
   187. .descriptorCount = 1,
   188. .descriptorType = VK_DESCRIPTOR_TYPE_COMBINED_IMAGE_SAMPLER,
   189. .pImageInfo = &imageInfo,
   190. .pBufferInfo = nullptr,
   191. .pTexelBufferView = nullptr};
   192. gfxPipelineInfo.descWrites[0] = bufferWrite;
   193. gfxPipelineInfo.descWrites[1] = imageWrite;
   194. vkUpdateDescriptorSets(device, 2, gfxPipelineInfo.descWrites, 0, nullptr);

   196. createGraphicsPipeline();
   197. createOtherStuff();

   199. recordCommandBuffer();
   200. OH_LOG_INFO(LOG_APP, "hwBufferToTexture end");
   201. }
   ```
