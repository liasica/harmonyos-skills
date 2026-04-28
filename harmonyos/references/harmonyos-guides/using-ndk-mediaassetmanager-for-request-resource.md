---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ndk-mediaassetmanager-for-request-resource
title: 使用MediaAssetManager请求媒体资源(C/C++)
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 受限开放能力 > 使用MediaAssetManager请求媒体资源(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1da0b6638035257c3a858dcbaa61be89dd32e69ed03807e96897da0346d1e0b9
---

使用MediaAssetManager可以实现请求媒体资源到目标沙箱路径，本开发指导将以请求一张图片作为示例，向开发者讲解MediaAssetManager相关功能。

请求图片资源的全流程包含：创建MediaAssetManager，设置请求资源，请求图片资源，取消本次请求(可选)。

## 开发步骤及注意事项

在CMake脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libmedia_asset_manager.so)
```

开发者通过引入[media\_asset\_manager\_capi.h](../harmonyos-references/capi-media-asset-manager-capi-h.md)和[media\_asset\_base\_capi.h](../harmonyos-references/capi-media-asset-base-capi-h.md)头文件，使用MediaAssetManager相关API。

详细的API说明请参考[MediaAssetManager API](../harmonyos-references/capi-mediaassetmanager.md)。

说明

开发前，需要参考[开发准备](photoaccesshelper-preparation.md)，申请ohos.permission.READ\_IMAGEVIDEO权限。

1. 创建实例：OH\_MediaAssetManager\_Create()。
2. 设置资源：设置资源请求回调、设置资源请求策略、设置源图片Uri和目标Uri。
3. 请求图片资源：调用OH\_MediaAssetManager\_RequestImageForPath()请求图片资源到目标Uri。
4. 取消请求：调用OH\_MediaAssetManager\_CancelRequest()。(可选)

## 完整示例

```
1. #include "napi/native_api.h"
2. #include "multimedia/media_library/media_asset_base_capi.h"
3. #include "multimedia/media_library/media_asset_manager_capi.h"
4. #include <cstdio>
5. #include <cstring>

7. const char ERROR_REQUEST_ID[UUID_STR_MAX_LENGTH] = "00000000-0000-0000-0000-000000000000";

9. // 资源请求回调
10. void OnDataPrepared(int32_t result, MediaLibrary_RequestId requestIdStruct)
11. {
12. printf("OnDataPrepared requestId: %s result: %d\n", requestIdStruct.requestId, result);
13. }

15. // ...

17. static napi_value RequestMediaAssets(napi_env env, napi_callback_info info)
18. {
19. // 创建MediaAssetManager实例
20. OH_MediaAssetManager *manager = OH_MediaAssetManager_Create();
21. if (manager == nullptr) {
22. // 处理异常。
23. printf("Get MediaAssetManager failed.\n");
24. // ...
25. } else {
26. // 设置资源请求回调
27. OH_MediaLibrary_OnDataPrepared callback = OnDataPrepared;

29. // 设置资源请求策略
30. MediaLibrary_RequestOptions options;
31. options.deliveryMode = MEDIA_LIBRARY_HIGH_QUALITY_MODE;

33. // 预置图片资源Uri，默认为高质量图片。注：以下Uri是示例，开发者需根据实际情况创建或获取
34. const char *srcUri = "file://media/Photo/87/VID_1712195295_025/request_image_src.jpg";

36. // 提供目标路径Uri。注：以下Uri是示例，开发者需根据实际情况创建或获取
37. const char *destUri = "file://media/Photo/9/IMG_1712195237_008/request_image_dest.jpg";

39. // 将图片资源请求到目标路径
40. MediaLibrary_RequestId requestIdStruct = OH_MediaAssetManager_RequestImageForPath(manager, srcUri,
41. options, destUri, callback);
42. if (strcmp(requestIdStruct.requestId, ERROR_REQUEST_ID) == 0) {
43. // 处理异常
44. printf("Request image failed requestId：%s\n", requestIdStruct.requestId);
45. // ...
46. } else {
47. // 请求成功，打印请求Id
48. printf("Request image success, requestId: %s\n", requestIdStruct.requestId);

50. // 调用CancelRequest接口，用来取消尚在处理中的请求
51. // 注：OH_MediaAssetManager_CancelRequest不是必须流程，开发者可根据实际情况选择是否调用该接口来取消尚未回调返回的资源请求
52. bool ret = OH_MediaAssetManager_CancelRequest(manager, requestIdStruct);
53. // ...
54. }
55. }
56. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/RequestMediaAssetsCppSample/entry/src/main/cpp/napi_init.cpp#L16-L86)
