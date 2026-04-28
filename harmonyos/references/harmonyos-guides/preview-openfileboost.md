---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-openfileboost
title: 文件打开加速（C/C++）
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > 文件打开加速（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f223f117182a418188a90af2d317e4c4601925b34f617fa0a0d330c730589978
---

从5.0.3(15)版本开始，新增文件打开加速功能。提供注册和取消注册接口，应用可以注册一系列回调，文件打开加速服务通过调用回调接口向应用推荐文件进行预加载动作。

## 接口说明

具体API说明详见[文件打开加速接口文档](../harmonyos-references/openfileboost_preview.md)。

**表1** 文件预加载接口介绍（C API）

| 接口名 | 描述 |
| --- | --- |
| OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_RegisterFilePreload(  HMS\_OpenFileBoost\_QueryAppState queryAppState,  HMS\_OpenFileBoost\_OnFilePreload filePreload,  HMS\_OpenFileBoost\_OnFilePreload cancelFilePreload); | 向系统注册文件预加载回调，后续系统预测用户可能打开的文件，在通知预加载之前先调用queryAppState向应用查询当前是否允许推荐预加载文件，如果应用返回允许推荐，通过调用filePreload向应用推荐一个文件供应用进行文件预加载。在某些场景下,比如当前系统可用内存不足,或者有其他文件更有可能被用户打开,则系统会通过调用cancelFilePreload取消某些文件的预加载。 |
| typedef OpenFileBoost\_AppState (\*HMS\_OpenFileBoost\_QueryAppState)(void); | 系统查询APP状态的回调函数定义。 |
| typedef OpenFileBoost\_CbErrCode (\*HMS\_OpenFileBoost\_OnFilePreload)(void\* fileInfo); | 系统向应用推荐或取消推荐预加载文件的回调函数定义。 |
| OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo(  void\* fileInfo, int32\_t\* fd); | 在向应用推荐文件进行预加载或取消预加载的回调上下文中，应用通过调用该接口获取文件描述符信息。 |
| OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo(  void\* fileInfo, char\* sandboxPath, int32\_t pathLen); | 在向应用推荐文件进行预加载或取消预加载的回调上下文中，应用通过调用该接口获取文件沙箱路径信息。 |
| OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_UnregisterFilePreload(void); | 取消注册预加载回调。 |
| OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_NotifyPreloadHit(  int32\_t fd, char\* sandboxPath, int32\_t pathLen); | 当用户打开预加载文件时, 应用调用该接口通知系统预加载命中, 这将有助于提高预加载文件预测的准确性。 |

## 开发准备

需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.PCService.OpenFileBoost系统能力，当前仅在2in1设备上支持该能力。

## 开发步骤

1. 申请文件打开加速服务的对应权限，在module.json5文件中添加文件预加载权限。注意ohos.permission.PRELOAD\_FILE为受限权限，具体可参考[申请使用受限权限](declare-permissions-in-acl.md) 。

   ```
   1. "requestPermissions":[
   2. {
   3. "name": "ohos.permission.PRELOAD_FILE"
   4. }
   5. ]
   ```
2. 添加对应的头文件。

   ```
   1. #include "PreviewKit/open_file_boost.h"
   ```
3. 编写CMakeLists.txt，新增对文件打开加速功能的依赖。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libopen_file_boost.so
   3. )
   ```
4. 注册文件预加载回调，注册后系统在条件符合时调用回调向应用推荐文件。

   ```
   1. OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_RegisterFilePreload(AppQueryAppStateCb,
   2. AppOnFilePreload, AppCancelFilePreload);
   3. if (ret != OPEN_FILE_BOOST_SUCCESS){
   4. // 注册失败，用户可自定义错误处理
   5. }
   ```
5. 应用应该在当前回调上下文中同步解析预加载文件, 或同步阻塞等待解析完毕后再返回，以便系统可以评估本次预加载文件的资源消耗。

   ```
   1. // 查询应用当前状态的回调函数，系统在向应用推荐文件前会先调用状态查询回调函数向应用查询当前是否适合推荐
   2. OpenFileBoost_AppState AppQueryAppStateCb(void)
   3. {
   4. // 如果当前状态允许进行文件预加载则返回OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD，这里的CanPreload函数为代码示例，表示应用根据实际业务判断是否允许预加载
   5. if (CanPreload()) {
   6. return OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD;
   7. } else {
   8. return OPEN_FILE_BOOST_APP_STATE_REJECT_PRELOAD;
   9. }
   10. }

   12. // 文件预加载回调
   13. OpenFileBoost_CbErrCode AppOnFilePreload(void* fileInfo)
   14. {
   15. int32_t fileDescriptor = 0;
   16. // 指针fileInfo仅在当前回调上下文有效，在回调中调用HMS_OpenFileBoost_GetFdFromPreloadFileInfo获取文件描述符
   17. OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_GetFdFromPreloadFileInfo(fileInfo, &fileDescriptor);
   18. if (ret != OPEN_FILE_BOOST_SUCCESS) {
   19. return OPEN_FILE_BOOST_CALLBACK_FAILURE;
   20. }
   21. char sandboxPath[MAX_BUFFER_LENGTH] = {0};
   22. // 指针fileInfo仅在当前回调上下文有效，在回调中调用HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo获取文件路径
   23. ret = HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo(fileInfo, sandboxPath, MAX_BUFFER_LENGTH);
   24. if (ret != OPEN_FILE_BOOST_SUCCESS) {
   25. return OPEN_FILE_BOOST_CALLBACK_FAILURE;
   26. }
   27. // 用户可保存文件描述符和文件路径，方便后续通知取消预加载时对文件取消预加载
   28. // 用户自定义具体的文件预加载逻辑
   29. return OPEN_FILE_BOOST_CALLBACK_SUCCESS;
   30. }

   32. // 取消预加载回调
   33. OpenFileBoost_CbErrCode AppCancelFilePreload(void* fileInfo)
   34. {
   35. // 同样的方法获取文件描述符和沙箱路径
   36. int32_t fileDescriptor = 0;
   37. OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_GetFdFromPreloadFileInfo(fileInfo, &fileDescriptor);
   38. if (ret != OPEN_FILE_BOOST_SUCCESS) {
   39. return OPEN_FILE_BOOST_CALLBACK_FAILURE;
   40. }
   41. char sandboxPath[MAX_BUFFER_LENGTH] = {0};
   42. ret = HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo(fileInfo, sandboxPath, MAX_BUFFER_LENGTH);
   43. if (ret != OPEN_FILE_BOOST_SUCCESS) {
   44. return OPEN_FILE_BOOST_CALLBACK_FAILURE;
   45. }
   46. // 用户自定义具体的取消文件预加载逻辑
   47. return OPEN_FILE_BOOST_CALLBACK_SUCCESS;
   48. }
   ```
6. 如果用户打开了已经预加载的文件，应用需要调用HMS\_OpenFileBoost\_NotifyPreloadHit通知系统，系统会更改文件的预加载状态。

   ```
   1. // 传入用户打开的已经预加载的文件描述符、文件路径和长度
   2. OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_NotifyPreloadHit(fileDescriptor, sandboxPath, pathLen);
   3. if (ret != OPEN_FILE_BOOST_SUCCESS){
   4. // 通知失败，用户可自定义错误处理
   5. }
   ```
7. 应用不想再收到回调，或者在退出流程中时，调用取消预加载接口。

   ```
   1. OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_UnregisterFilePreload();
   2. if (ret != OPEN_FILE_BOOST_SUCCESS){
   3. // 取消注册失败，用户可自定义错误处理
   4. }
   ```
