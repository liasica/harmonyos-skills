---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scan-7
title: 如何排查自定义界面扫码黑屏问题
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 扫码服务（Scan） > 如何排查自定义界面扫码黑屏问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:20+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:6d17f5020e29a874f61f0cf3a784bd72995e2767db1f08d384867fd53663a1f8
---

## 问题现象

应用采用自定义界面扫码，但扫码区域出现黑屏现象。

## 背景知识

* [自定义界面扫码](../harmonyos-guides/scan-customscan.md)：提供了相机流控制接口，可根据自身需求自定义扫码界面，适用于对扫码界面有定制化需求的应用开发。
* [Scan Kit错误码](../harmonyos-references/errorcode-scan.md)：模块特有错误码。
* [customScan.start](../harmonyos-references/scan-customscan-api.md#start)：启动扫码相机流。其中的viewControl参数是相机控制参数，类型是[ViewControl](../harmonyos-references/scan-customscan-api.md#viewcontrol)。
* 自定义扫码业务流程图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/wvFPLgHWRb-pkSj3Gjya-w/zh-cn_image_0000002633596068.png "点击放大")
* 常见黑屏场景：

  | 常见黑屏问题场景 | 常见报错日志 | 根因 | 排查步骤 |
  | --- | --- | --- | --- |
  | 未取得相机权限 | Permission denied. | 调用init接口前未获取到相机权限 | 1. 检查应用是否已声明相机权限； 2. 检查应用是否未向用户申请权限； 3. 检查用户是否拒绝授权。 |
  | 方法调用存在时序问题 | ScanOption is null, please call customScan.init first. | 封装异步方法或多线程场景下，方法调用存在时序问题，start在init前执行 | 检查init、start方法的调用方式以及调用时机 |
  | start接口参数异常 | The width and height of viewControl do not match the width and height supported by the camera. | viewControl参数错误，XComponent组件宽高比不合适 | 检查viewControl参数中的宽高设置是否合理 |
  | ViewControl's width/height range error. | viewControl参数异常，XComponent组件宽高异常 |
  | ViewControl's surfaceid range error. | viewControl参数异常，surfaceId不合法 | 检查viewControl参数中的surfaceId是否正确 |
  | AdjustRenderFit failed, due to CreateNativeWindowFromSurfaceId fail, ret: 40001000 | viewControl参数异常，surfaceId异常 |
  | 返回页面重新扫码失败 | CreateBusinessError errCode: 1000500001 errMsg: Internal error. Camera restart camera session failed. | 退出页面时未释放相机资源 | 检查release方法的调用时机 |

## 问题定位

1. 检查是否有相机权限ohos.permission.CAMERA。流程图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/crmTrztnS5a7dR8V83tn3Q/zh-cn_image_0000002633596078.png "点击放大")

   检查日志，如果出现以下日志，则代表调用[customScan.init](../harmonyos-references/scan-customscan-api.md#init)方法时已获得相机权限：

   ```txt
   C05506/包名/ScanFrameworkCustomScan    包名  I    [InitScan:551] customScan.init is called
   C05506/包名/ScanFrameworkCustomScan    包名  I    [InitScan:564] camera granted
   ...
   C05506/包名/ScanFrameworkCustomScan    包名  I    [InitScan:593] end InitScan
   ```

   若未出现上述日志，则是还未调用init方法或者未获取相机权限。如下日志代表调用init方法时还未获得相机权限：

   ```txt
   C05506/包名/ScanFrameworkCustomScan    包名  I    [InitScan:551] customScan.init is called
   C05506/包名/ScanFrameworkCustomScan    包名  E    [InitScan:556] camera not granted
   C05506/包名/ScanFramework              包名  I    [CreateBusinessError:30] CreateBusinessError errCode: 201 errMsg: Permission denied.
   ```

   **说明** 

   需要考虑用户拒绝授权后，应用没有再调用init方法的场景，该场景下不会出现上方的日志，此时需要参照下方第1.3步检查用户是否拒绝授权。

   排查缺少相机权限的详细原因：

   * 检查应用中是否声明相机权限。如果出现以下日志，代表未声明相机权限：

     ```txt
     [IsDynamicRequest:444]Permission: ohos.permission.CAMERA: state: 2, errorReason: 2
     ```

     **说明** 

     errorReason: 2表示应用未声明该权限。详情参照[PermissionRequestResult属性](../harmonyos-references/js-apis-permissionrequestresult.md#属性)中errorReasons属性部分。
   * 检查应用是否在init方法前通过[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)或[requestPermissionOnSetting](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)接口向用户申请相机权限。
   * 检查用户是否授权。筛查相机权限相关的日志。
     + 检查是否存在以下日志，该段日志表示用户在权限弹窗中拒绝授权（reqPerms数组和result数组是对应的，result数组中-1表示拒绝授权，0表示允许授权）：

       ```txt
       [SPC][PermissionDialog][Model]: terminate session with result, resultCode: 1, reqPerms: [ohos.permission.CAMERA], result: [-1].
       ```
     + 检查是否存在以下日志，该段日志表示调用requestPermissionsFromUser方法后，确认应用缺少相机权限，且无法再次通过该接口拉起权限申请弹窗：

       ```txt
       [IsDynamicRequest:444]Permission: ohos.permission.CAMERA: state: -1, errorReason: 0
       [RequestPermissionsFromUserExecute:704]It does not need to request permission
       ```
2. 排查接口调用时序是否正确。筛选日志，如果出现下方日志，说明[customScan.start](../harmonyos-references/scan-customscan-api.md#start-1)方法实际在init方法前执行：

   ```txt
   C05506/包名/ScanFramework    包名  I     [CreateBusinessError:30] CreateBusinessError errCode: 1000500001 errMsg: Internal error. ScanOption is null, please call customScan.init first.
   C05506/包名/ScanFramework    包名  I     [CreateBusinessError:57] CreateBusinessError exit
   ```

   错误流程示意图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/TTXun_cJSgG6OPeFKYu0mQ/zh-cn_image_0000002633436226.png "点击放大")

   出现该问题可能得原因有：

   * 封装异步函数，异步函数和同步方法一起执行，实际执行顺序可能是start先于init执行。
   * 多线程场景下，init、start方法可能不是按先后顺序执行的。
3. 排查start接口的第一个入参（即viewControl参数）是否正确。
   * 排查width和height是否正确设置。详细标准请参考[开发步骤](../harmonyos-guides/scan-customscan.md#开发步骤)中第4步的说明部分。如果日志中出现以下内容，则代表viewControl参数的高度不合理：

     ```txt
     C05506/包名/ScanFramework    包名  I     [CreateBusinessError:30] CreateBusinessError errCode: 401 errMsg: Parameter error. ViewControl's height range error.
     C05506/包名/ScanFramework    包名  I     [CreateBusinessError:57] CreateBusinessError exit
     ```

     **说明** 

     此处是高度异常，宽度异常对应ViewControl's width range error.。此时应用正常会闪退，如果应用自行抓取处理错误就不会闪退，但扫码区域会黑屏。
   * 排查surfaceId是否正确。筛选日志，如果出现以下日志，表示viewControl参数中的surfaceId不合法：

     ```txt
     C05506/包名/ScanFramework   包名  I     [CreateBusinessError:30] CreateBusinessError errCode: 401 errMsg: Parameter error. ViewControl's surfaceid range error.
     C05506/包名/ScanFramework   包名  I     [CreateBusinessError:57] CreateBusinessError exit
     ```

     以下日志代表surfaceId错误，surfaceId无效：

     ```txt
     C05506/包名/ScanFrameworkCustomScan    包名  E    [AdjustRenderFit:379] AdjustRenderFit failed, due to CreateNativeWindowFromSurfaceId fail, ret: 40001000
     ...
     C05506/包名/ScanFrameworkCustomScan    包名  E    [CreatePreviewOutput:744] Failed to get CreatePreviewOutput surface
     C05506/包名/ScanFrameworkCustomScan    包名  E    [CreateCaptureOutput:714] Create preview output failed, ret: -2
     ```

     **说明** 

     surfaceId错误时应用正常会闪退，如果应用自行抓取处理错误就不会闪退，但扫码区域会黑屏显示。

   排查流程图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/vIUAuey2SmuibTzmDkjHTQ/zh-cn_image_0000002663715357.png "点击放大")

   **说明** 

   流程图中置绿色背景部分是较新版本中宽高比不匹配时也能正常扫码，不会黑屏。在2025年5月之前的版本中，宽高比不匹配会有报错日志Internal error. The width and height of viewControl do not match the width and height supported by the camera.，并且扫码区域显示黑屏。后续版本已移除相关报错，可以正常显示画面，但会出现画面拉伸问题影响预览流体验，建议宽高比保持在16:9、4:3、1:1范围内。
4. 排查在应用退至后台/手机设备锁屏/退出页面等场景下，是否释放扫码相机流。流程图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/JtL9x9tIQKWMvuaw40oe8A/zh-cn_image_0000002633436874.png "点击放大")

   如果在返回扫码页面时出现以下日志，则代表相机重启失败，执行start方法前没有调用[customScan.stop](../harmonyos-references/scan-customscan-api.md#stop)、[customScan.release](../harmonyos-references/scan-customscan-api.md#release)接口释放扫码相机流：

   ```txt
   C05506/包名/ScanFramework  包名  I     [CreateBusinessError:30] CreateBusinessError errCode: 1000500001 errMsg: Internal error. Camera restart camera session failed.
   C05506/包名/ScanFramework  包名  I     [CreateBusinessError:57] CreateBusinessError exit
   ```

   **说明** 

   该场景下扫码区域会画面静止，重新进入扫码页面时扫码区域才会显示黑屏。

## 分析结论

1. 缺少相机权限。
   * 未声明相机权限。
   * 应用未向用户申请相机权限。
   * 用户未授权使用相机。
2. start接口的调用时序有问题，在init方法执行前调用。
3. start接口的参数异常。
   * viewControl参数中的宽高异常。
   * viewControl参数中surfaceId错误。
4. 退出扫码页面（包含设备锁屏、应用退至后台等场景）时，未及时调用stop和release接口释放扫码相机流。

## 修改建议

1. 申请相机权限ohos.permission.CAMERA。
   * 应用需要在[module.json5](../harmonyos-guides/module-configuration-file.md)配置文件中声明权限相机权限ohos.permission.CAMERA。
   * 参照[向用户申请授权](../harmonyos-guides/request-user-authorization.md)拉起弹窗向用户申请相机权限。
   * 参照[再次向用户申请授权](../harmonyos-guides/request-user-authorization-second.md)引导用户再次授权。
2. 调整[customScan.start](../harmonyos-references/scan-customscan-api.md#start)方法的执行时机，确保customScan.start方法在customScan.init方法之后执行。
3. 参考[开发步骤](../harmonyos-guides/scan-customscan.md#开发步骤)中第4步的说明部分，调整viewControl参数的宽高，确保在支持范围内。
4. 在锁屏、应用退至后台等退出页面的场景下，及时调用[customScan.stop](../harmonyos-references/scan-customscan-api.md#stop)、[customScan.release](../harmonyos-references/scan-customscan-api.md#release)方法释放扫码相机流。

示例代码可以参考[开发步骤](../harmonyos-guides/scan-customscan.md#开发步骤)以及[示例工程](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts)。
