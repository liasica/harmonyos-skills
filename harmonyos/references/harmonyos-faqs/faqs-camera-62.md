---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-62
title: 如何排查相机界面黑屏问题
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何排查相机界面黑屏问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:02882e93302222cbd896343939f7ac9148b17ad96e767f895109781368386935
---

## 问题现象

应用使用相机功能时，相机页面黑屏。

## 背景知识

* [Camera Kit](../harmonyos-guides/camera-overview.md)：相机服务。
* [相机开发权限](../harmonyos-guides/camera-preparation.md)：使用相机拍摄前，需要申请ohos.permission.CAMERA相机权限。
* [预览](../harmonyos-guides/camera-preview.md)：预览是启动相机后看见的画面，通常在拍照和录像前执行。
* [getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)：获取支持的相机设备对象。
* 一台可折叠设备在不同折叠状态下，可使用不同的相机。系统会标识所有摄像头，每个摄像头与一个折叠状态相对应，表示该摄像头可在对应的折叠状态下使用。应用可调用[CameraManager.on('foldStatusChange')](../harmonyos-references/arkts-apis-camera-cameramanager.md#onfoldstatuschange12)或[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)监听设备的折叠状态变化，并调用CameraManager.getSupportedCameras获取当前状态下可用相机，完成相应适配，确保应用在折叠状态变更时的用户体验。
* 在开发相机应用界面时，首先需要通过创建[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件为预览流提供Surface，再通过获取XComponent组件对应Surface的ID创建预览流，预览流画面即可直接在XComponent组件内渲染，获取surfaceId请参考[getXComponentSurfaceId](../harmonyos-references/ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)方法。
* 相机在拍摄前，必须完成输入输出流的配置。使用[beginConfig](../harmonyos-references/arkts-apis-camera-session.md#beginconfig11)方法开始配置会话，[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)方法提交配置信息，[start](../harmonyos-references/arkts-apis-camera-session.md#start11)方法启动会话。
* [canAddInput](../harmonyos-references/arkts-apis-camera-session.md#canaddinput11)可判断当前cameraInput是否可以添加到session中。[canAddOutput](../harmonyos-references/arkts-apis-camera-session.md#canaddoutput11)可判断当前cameraOutput是否可以添加到session中。
* 相机切换后台之后，相机资源全部回收，需要重新初始化。
* 按照相机生命周期顺序排查黑屏问题的大致流程如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/XXlt1LvJSHGSRDPHEMQEIg/zh-cn_image_0000002658791861.png "点击放大")
* 常见黑屏场景：

  |  |  |  |  |
  | --- | --- | --- | --- |
  | 常见黑屏问题场景 | 常见报错日志 | 根因 | 排查步骤 |
  | 未取得相机权限 | Permission denied. | 获取相机设备前未获取相机权限。 | 1、检查应用是否已声明相机权限；2、检查应用是否未向用户申请权限；3、检查用户是否拒绝授权。 |
  | 无法获取相机设备 | Can not use camera cause of preempted. | 相机对象被其他应用占用。 | 排查日志。 |
  | 使用了不可用的摄像头 | 无 | 折叠屏切换折叠状态后未更换当前使用的摄像头。 | 排查应用监听折叠状态切换时是否重新获取并切换到当前可用的摄像头。 |
  | createPreviewOutput参数配置异常 | failed to get surface. | 在XComponent创建前就创建预览流，未获取到surfaceId。 | 检查onPageShow中是否在初次进入页面就初始化相机。 |
  | 方法调用存在时序问题 | Operation not allowed. | 添加或移除相机的输入流和输出流操作未在beginConfig和commitConfig之间。 | 检查beginConfig、commitConfig和添加输入输出流的执行顺序。 |
  | 未beginConfig就开始进行commitConfig操作。 |
  | Session not config. | 会话配置前，调用start操作。 | 检查beginConfig、commitConfig和start的执行顺序。 |
  | 添加了不可用的输入流/输出流 | canAddInput/CanAddOutput check failed. | 添加相机的输入流/输出流时，添加了不可用的输入流/输出流。 | 排查日志。 |
  | 返回页面后未重新初始化相机。 | 无 | onPageShow中未设置初始化相机。 | 查看页面在onPageShow中是否设置初始化相机。 |

## 问题定位

1. 检查应用是否有相机权限ohos.permission.CAMERA。查看日志，如果出现以下日志，说明应用缺少相机权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/yjaime_aQNKkpzcn6fHi2g/zh-cn_image_0000002628552482.png "点击放大")

   ```txt
   I     [CreateBusinessError:30] CreateBusinessError errCode: 201 errMsg: Permission denied.
   ```

   说明：需要考虑用户拒绝授权后不会出现上方的日志，此时需要继续筛查日志。

   1. 检查应用中是否声明相机权限。如果出现以下日志，代表未声明相机权限：

      ```txt
      [IsDynamicRequest:444]Permission: ohos.permission.CAMERA: state: 2, errorReason: 2
      ```

      说明：errorReason: 2表示应用未声明该权限。详情参照[PermissionRequestResult属性](../harmonyos-references/js-apis-permissionrequestresult.md#属性)中errorReasons属性部分。
   2. 检查应用是否有调用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)或[requestPermissionOnSetting](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)接口申请相机权限。
   3. 检查用户是否授权。
      * 检查是否存在以下日志，该段日志表示用户在权限弹窗中拒绝授权（reqPerms数组和result数组是对应的，result数组中-1表示拒绝授权，0表示允许授权）：

        ```txt
        [SPC][PermissionDialog][Model]: terminate session with result, resultCode: 1, reqPerms: [ohos.permission.CAMERA], result: [-1].
        ```
      * 检查是否存在以下日志，该段日志表示调用requestPermissionsFromUser方法时，已确认应用缺少相机权限，且无法再次通过该接口拉起权限申请弹窗。

        ```txt
        [IsDynamicRequest:444]Permission: ohos.permission.CAMERA: state: -1, errorReason: 0
        [RequestPermissionsFromUserExecute:704]It does not need to request permission
        ```
2. 查看相机设备是否被占用。查看日志，若出现下方日志，说明相机设备被占用。

   ```txt
   xxx, Camera input error code: 7400109
   Can not use camera cause of preempted
   ```
3. 排查createPreviewOutput参数配置是否异常。若出现如下日志，说明未获取到surfaceId。

   ```txt
   {CreatePreviewOutputInstance():869} CameraManagerNapi::CreatePreviewOutputInstance ParseProfile size.width = xxx, size.height = xxx, format = 1003, surfaceId =
   {CreatePreviewOutput():341} CreatePreviewOutput is called
   <surface_utils.cpp:48-GetSurface>: Cannot find surface, uniqueId: 0.
   {CreatePreviewOutput():357} failed to get surface
   ```

   可能原因为初次进入页面时在onPageShow中初始化相机，而此时XComponent组件还未创建，无法获取到XComponent组件的surfaceId。
4. 排查当前使用的摄像头，查看on('foldStatusChange')中折叠状态切换后是否重新获取当前可用的摄像头。
5. 排查接口调用时序是否正确。查看日志，若出现下方日志，说明接口调用时序异常。
   * 添加或移除相机的输入流和输出流操作未在beginConfig和commitConfig之间会出现如下日志：

     ```txt
     {AddInput():666} CaptureSession::AddInput operation Not allowed!
     initCamera fail: {"code":"7400102"}
     ```
   * 未beginConfig就开始进行commitConfig操作会出现如下日志：

     ```txt
     {CommitConfig():424} CaptureSession::CommitConfig operation Not allowed!
     initCamera fail: {"code":"7400102","message":"Operation not allowed."}
     ```
   * 会话配置前，调用start操作会出现如下日志：

     ```txt
     {Start():1261} CaptureSession::Start Session not Commited
     initCamera fail: {"code":"7400103","message":"Session not config."}
     ```
6. 查看添加的输入流/输出流是否可用。查看日志，若出现下方日志，说明添加了不可用的输入流/输出流。

   ```txt
   CanAddxxx check failed.
   initCamera fail: {"code":"7400201","message":"Camera service fatal error."}
   ```
7. 排查在应用退至后台/手机设备锁屏等场景下返回相机界面后的设置，若应用未在onPageShow中重新初始化相机，相机功能无法拉起，相机界面黑屏。

## 分析结论

1. 缺少相机权限。
   * 未声明相机权限。
   * 应用未向用户申请相机权限。
   * 用户未授权使用相机。
2. 其他应用处于后台时未释放相机资源，相机对象被占用，无法获取相机设备。
3. 折叠屏切换折叠状态后未更换当前使用的摄像头。
4. 在XComponent创建前就创建预览流，未获取到surfaceId。
5. 方法调用时序存在问题。
   * 添加或移除相机的输入流和输出流操作未在beginConfig和commitConfig之间。
   * 未beginConfig就开始进行commitConfig操作。
   * 会话配置前，调用start操作。
6. 添加了不可用的输入流/输出流。
7. 返回页面后未重新初始化相机。

## 修改建议

1. 申请相机权限ohos.permission.CAMERA。
   * 应用需要在[module.json5](../harmonyos-guides/module-configuration-file.md)配置文件中声明权限相机权限ohos.permission.CAMERA。
   * 参照[向用户申请授权](../harmonyos-guides/request-user-authorization.md)拉起弹窗向用户申请相机权限。
   * 参照[再次向用户申请授权](../harmonyos-guides/request-user-authorization-second.md)引导用户再次授权。
2. 占用相机对象的应用处于后台时应释放相机资源。
3. 折叠状态改变后，需要重新获取到当前设备折叠状态下可用的摄像头列表，并切换至可用摄像头，可参考[适配不同折叠状态的摄像头变更(ArkTS)](../harmonyos-guides/camera-foldable-display.md)。
4. 首次进入页面时，在XComponent创建后再创建预览流。
5. 调整方法调用时序。
   * 添加或移除相机的输入流和输出流操作在beginConfig和commitConfig之间。
   * beginConfig操作后再进行commitConfig操作。
   * 会话配置后调用start操作。
6. 使用canAddInput和canAddOutput判断当前输入流和输出流是否可用，将不可用输入流/输出流替换为可用的。
7. 返回页面后重新初始化相机。

示例代码可以参考[预览(ArkTS)](../harmonyos-guides/camera-preview.md)。
