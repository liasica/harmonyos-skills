---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-c
title: 使用Image_NativeModule完成位图操作
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编辑和处理 > 使用Image_NativeModule完成位图操作
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:19+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:e7578fd2d7a91ffd0c091cba2fcac20d74c5cf8b44583ca34a83bb13964daf53
---

创建位图，获取位图的宽、高、pixelFormat、alphaType、rowStride信息、对位图进行操作以及释放位图实例。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libpixelmap.so以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libpixelmap.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)。

在DevEco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**位图接口使用示例**

在初始化参数后创建Pixelmap实例，进行图片像素数据的读写，对图片进行缩放、位置变换、反转、旋转、裁剪等操作。

```
1. #include <hilog/log.h>
2. #include <multimedia/image_framework/image/pixelmap_native.h>

4. #undef LOG_DOMAIN
5. #undef LOG_TAG
6. #define LOG_DOMAIN 0x3200
7. #define LOG_TAG "MY_TAG"

9. Image_ErrorCode PixelmapTest()
10. {
11. uint8_t data[96];
12. size_t dataSize = 96;
13. for (int i = 0; i < dataSize; i++) {
14. data[i] = i + 1;
15. }

17. // 创建参数结构体实例，并设置参数。
18. OH_Pixelmap_InitializationOptions *createOpts;
19. OH_PixelmapInitializationOptions_Create(&createOpts);
20. OH_PixelmapInitializationOptions_SetWidth(createOpts, 6);
21. OH_PixelmapInitializationOptions_SetHeight(createOpts, 4);
22. OH_PixelmapInitializationOptions_SetPixelFormat(createOpts, PIXEL_FORMAT_RGBA_8888);
23. OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_UNKNOWN);

25. // 创建Pixelmap实例。
26. OH_PixelmapNative *pixelmap = nullptr;
27. Image_ErrorCode errCode = OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &pixelmap);

29. // 读取图像像素数据，结果写入数组里。
30. uint8_t destination[96];
31. size_t destinationSize = 96;
32. errCode = OH_PixelmapNative_ReadPixels(pixelmap, destination, &destinationSize);
33. if (errCode != IMAGE_SUCCESS) {
34. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_ReadPixels failed, errCode: %{public}d.", errCode);
35. return errCode;
36. }

38. // 读取缓冲区中的图片数据，结果写入Pixelmap中。
39. uint8_t source[96];
40. size_t sourceSize = 96;
41. for (int i = 0; i < sourceSize; i++) {
42. source[i] = i + 1;
43. }
44. errCode = OH_PixelmapNative_WritePixels(pixelmap, source, sourceSize);
45. if (errCode != IMAGE_SUCCESS) {
46. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_WritePixels failed, errCode: %{public}d.", errCode);
47. return errCode;
48. }

50. // 创建图片信息实例，并获取图像像素信息。
51. OH_Pixelmap_ImageInfo *imageInfo;
52. OH_PixelmapImageInfo_Create(&imageInfo);
53. errCode = OH_PixelmapNative_GetImageInfo(pixelmap, imageInfo);
54. if (errCode != IMAGE_SUCCESS) {
55. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_GetImageInfo failed, errCode: %{public}d.", errCode);
56. return errCode;
57. }

59. // 获取图片的宽，高，pixel格式，透明度等信息。
60. uint32_t width, height, rowStride;
61. int32_t pixelFormat, alphaType;
62. OH_PixelmapImageInfo_GetWidth(imageInfo, &width);
63. OH_PixelmapImageInfo_GetHeight(imageInfo, &height);
64. OH_PixelmapImageInfo_GetRowStride(imageInfo, &rowStride);
65. OH_PixelmapImageInfo_GetPixelFormat(imageInfo, &pixelFormat);
66. OH_PixelmapImageInfo_GetAlphaType(imageInfo, &alphaType);
67. OH_PixelmapImageInfo_Release(imageInfo);
68. OH_LOG_INFO(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest GetImageInfo success, width: %{public}d, height: %{public}d, rowStride: %{public}d, pixelFormat: %{public}d, alphaType: %{public}d.", width, height, rowStride, pixelFormat, alphaType);

70. // 设置透明比率来让Pixelmap达到对应的透明效果。
71. errCode = OH_PixelmapNative_Opacity(pixelmap, 0.5);
72. if (errCode != IMAGE_SUCCESS) {
73. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Opacity failed, errCode: %{public}d.", errCode);
74. return errCode;
75. }

77. // 对图片进行缩放。
78. errCode = OH_PixelmapNative_Scale(pixelmap, 2.0, 1.0);
79. if (errCode != IMAGE_SUCCESS) {
80. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Scale failed, errCode: %{public}d.", errCode);
81. return errCode;
82. }

84. // 对图片进行位置变换。
85. errCode = OH_PixelmapNative_Translate(pixelmap, 50.0, 10.0);
86. if (errCode != IMAGE_SUCCESS) {
87. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Translate failed, errCode: %{public}d.", errCode);
88. return errCode;
89. }

91. // 对图片进行旋转。
92. errCode = OH_PixelmapNative_Rotate(pixelmap, 90.0);
93. if (errCode != IMAGE_SUCCESS) {
94. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Rotate failed, errCode: %{public}d.", errCode);
95. return errCode;
96. }

98. // 对图片进行翻转。
99. errCode = OH_PixelmapNative_Flip(pixelmap, true, true);
100. if (errCode != IMAGE_SUCCESS) {
101. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Flip failed, errCode: %{public}d.", errCode);
102. return errCode;
103. }

105. // 对图片进行裁剪。
106. Image_Region region;
107. region.x = 100;
108. region.y = 100;
109. region.width = 6;
110. region.height = 4;
111. errCode = OH_PixelmapNative_Crop(pixelmap, &region);
112. if (errCode != IMAGE_SUCCESS) {
113. OH_LOG_ERROR(LOG_APP, "ImagePixelmapNativeCTest pixelmapTest OH_PixelmapNative_Crop failed, errCode: %{public}d.", errCode);
114. return errCode;
115. }

117. // 释放Pixelmap, InitializationOptions实例。
118. OH_PixelmapNative_Release(pixelmap);
119. OH_PixelmapInitializationOptions_Release(createOpts);
120. return IMAGE_SUCCESS;
121. }

123. // PixelMap预乘/非预乘格式转换示例。
124. Image_ErrorCode PixelmapConvertAlphaTypeTest()
125. {
126. uint8_t data[96];
127. size_t dataSize = 96;
128. for (int i = 0; i < dataSize; i++) {
129. data[i] = i + 1;
130. }

132. // 创建参数结构体实例，并设置参数。
133. OH_Pixelmap_InitializationOptions *createOpts;
134. OH_PixelmapInitializationOptions_Create(&createOpts);
135. OH_PixelmapInitializationOptions_SetWidth(createOpts, 6);
136. OH_PixelmapInitializationOptions_SetHeight(createOpts, 4);
137. OH_PixelmapInitializationOptions_SetSrcPixelFormat(createOpts, PIXEL_FORMAT_RGBA_8888);
138. OH_PixelmapInitializationOptions_SetPixelFormat(createOpts, PIXEL_FORMAT_RGBA_8888);
139. OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_UNPREMULTIPLIED);

141. // 创建非预乘格式的位图实例。
142. OH_PixelmapNative *SrcPixelmap = nullptr;
143. Image_ErrorCode errCode = OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &SrcPixelmap);
144. if (errCode != IMAGE_SUCCESS) {
145. OH_LOG_ERROR(LOG_APP, "PixelmapConvertAlphaTypeTest CreateSrcPixelMap failed, errCode: %{public}d.", errCode);
146. }

148. // 创建预乘格式的位图实例，该DstPixelmap实例将用于保存SrcPixelmap转换AlphaType后的数据。
149. OH_PixelmapNative *DstPixelmap = nullptr;
150. OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_PREMULTIPLIED);
151. errCode = OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &DstPixelmap);
152. if (errCode != IMAGE_SUCCESS) {
153. OH_LOG_ERROR(LOG_APP, "PixelmapConvertAlphaTypeTest CreateDstPixelMap failed, errCode: %{public}d.", errCode);
154. }

156. // 转换AlphaType，SrcPixelmap的数据将被转换为预乘格式，并保存到DstPixelmap中。
157. errCode = OH_PixelmapNative_ConvertAlphaFormat(SrcPixelmap, DstPixelmap, true);
158. if (errCode != IMAGE_SUCCESS) {
159. OH_LOG_ERROR(LOG_APP, "PixelmapConvertAlphaTypeTest ConvertAlphaFormat failed, errCode: %{public}d.", errCode);
160. }

162. // 释放Pixelmap，InitializationOptions实例。
163. OH_PixelmapNative_Release(SrcPixelmap);
164. OH_PixelmapNative_Release(DstPixelmap);
165. OH_PixelmapInitializationOptions_Release(createOpts);
166. return errCode;
167. }
```
