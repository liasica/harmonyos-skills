---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-scan
title: ArkTS API错误码
breadcrumb: API参考 > 媒体 > Scan Kit（统一扫码服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:39+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3aca40dea0ac00da2f550d7d0fd4a3877bf0651c2aadc3fb3785cc3abac25031
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1000500001 内部错误

根据实际错误原因的不同，Scan Kit会上报不同的错误信息，具体如下。

### Failed to encode

**错误信息**

Internal error. Failed to encode.

**错误描述**

码图生成失败。

**可能原因**

码图生成时算法出现错误。

**处理步骤**

尝试重新调用码图生成接口[createBarcode](scan-generatebarcode.md#createbarcode)。

### Failed to decode

**错误信息**

Internal error. Failed to decode.

**错误描述**

图片识码失败。

**可能原因**

图片识码时算法出现错误。

**处理步骤**

尝试重新调用图片识码接口[decode](scan-imagedecode.md#decode)。

### Failed to decode image

**错误信息**

Internal error. Failed to decode image.

**错误描述**

图像数据识码失败。

**可能原因**

图像数据识码时算法出现错误。

**处理步骤**

尝试重新调用图像数据识码接口[decodeImage](scan-imagedecode.md#decodeimage)。

### Failed to create pixelMap

**错误信息**

Internal error. Failed to create pixelMap.

**错误描述**

码图生成时创建pixelMap失败。

**可能原因**

系统创建图像逻辑异常。

**处理步骤**

尝试重新调用码图生成接口[createBarcode](scan-generatebarcode.md#createbarcode)。

### Failed to read file

**错误信息**

Internal error. Failed to read file.

**错误描述**

图片识码时读取传入的图片路径失败。

**可能原因**

开发者传入uri无效。

**处理步骤**

检查传入的uri。

### Get context failed

**错误信息**

Internal error. Get context failed.

**错误描述**

默认界面扫码时获取系统context失败。

**可能原因**

传入的context错误。

**处理步骤**

参考[UIAbilityContext获取方式](../harmonyos-guides/application-context-stage.md#获取uiabilitycontextuiability组件的上下文)排查context入参。

### Get UI content failed

**错误信息**

Internal error. Get UI content failed.

**错误描述**

默认界面扫码时获取UI内容失败。

**可能原因**

传入的context错误，导致获取UI内容失败。

**处理步骤**

参考[UIAbilityContext获取方式](../harmonyos-guides/application-context-stage.md#获取uiabilitycontextuiability组件的上下文)排查context入参。

### Get callback failed

**错误信息**

Internal error. Get callback failed.

**错误描述**

获取Callback失败。

**可能原因**

外部传入Callback异常。

**处理步骤**

排查Callback入参。

### This interface must be invoked after the customScan.start interface

**错误信息**

Internal error. This interface must be invoked after the customScan.start interface.

**错误描述**

接口调用顺序错误，调用当前接口时没有先调用start接口。

**可能原因**

未按业务流程调用接口，如未调用start接口，直接调用getFlashLightStatus。

**处理步骤**

调整接口调用顺序，可参考自定义界面扫码的[业务流程](../harmonyos-guides/scan-customscan.md#业务流程)。例如：先调用[start](scan-customscan-api.md#start)接口，再调用[getFlashLightStatus](scan-customscan-api.md#getflashlightstatus)。

### This interface cannot be used after the camera session is paused

**错误信息**

Internal error. This interface cannot be used after the camera session is paused.

**错误描述**

接口调用顺序错误，调用当前接口时先调用了stop接口。

**可能原因**

未按业务流程调用接口，如调用了stop接口后，又调用getFlashLightStatus。

**处理步骤**

调整接口调用顺序，可参考自定义界面扫码的[业务流程](../harmonyos-guides/scan-customscan.md#业务流程)。例如：在调用[getFlashLightStatus](scan-customscan-api.md#getflashlightstatus)接口前，确保没有调用[stop](scan-customscan-api.md#stop)。

### ScanOption is null, please call customScan.init first

**错误信息**

Internal error. ScanOption is null, please call customScan.init first.

**错误描述**

接口调用顺序错误，调用start接口时没有先调用init。

**可能原因**

未调用init接口，直接调用start。

**处理步骤**

调整接口调用顺序，可参考自定义界面扫码的[业务流程](../harmonyos-guides/scan-customscan.md#业务流程)。先调用[init](scan-customscan-api.md#init)接口，再调用[start](scan-customscan-api.md#start)。

### The interface can't be used in promise interface

**错误信息**

Internal error. The interface can't be used in promise interface.

**错误描述**

该接口不允许在start的Promise方式中调用。

**可能原因**

start的Promise方式中调用了rescan接口。

**处理步骤**

使用[start](scan-customscan-api.md#start-1)的Callback方式再调用[rescan](scan-customscan-api.md#rescan)接口。

### CustomScan stop session failed

**错误信息**

Internal error. CustomScan stop session failed.

**错误描述**

相机错误。

**可能原因**

扫码相机流暂停失败。

**处理步骤**

检查扫码相机流是否已启动，若未启动，尝试重新创建扫码相机流；检查扫码相机流是否已暂停。

### CustomScan release failed

**错误信息**

Internal error. CustomScan release failed.

**错误描述**

相机错误。

**可能原因**

扫码相机流释放失败。

**处理步骤**

检查扫码相机流是否已启动，若未启动，尝试重新创建扫码相机流；检查扫码相机流是否已释放。

### Open camera flash failed, flashlight is not available

**错误信息**

Internal error. Open camera flash failed, flashlight is not available.

**错误描述**

开启闪光灯失败。

**可能原因**

闪光灯不可用。

**处理步骤**

检查设备闪光灯是否正常。

### Close camera flash failed, flashlight is not available

**错误信息**

Internal error. Close camera flash failed, flashlight is not available.

**错误描述**

关闭闪光灯失败。

**可能原因**

闪光灯不可用。

**处理步骤**

检查设备闪光灯是否正常。

### Camera setZoom failed

**错误信息**

Internal error. Camera setZoom failed.

**错误描述**

设置变焦比失败。

**可能原因**

相机异常。

**处理步骤**

检查扫码相机流是否已启动，若未启动，尝试重新创建扫码相机流。

### Camera getZoom failed

**错误信息**

Internal error. Camera getZoom failed.

**错误描述**

获取变焦比失败。

**可能原因**

相机异常。

**处理步骤**

检查扫码相机流是否已启动，若未启动，尝试重新创建扫码相机流。

### Camera setFocusPoint failed

**错误信息**

Internal error. Camera setFocusPoint failed.

**错误描述**

设置相机焦点失败。

**可能原因**

相机异常。

**处理步骤**

检查扫码相机流是否已启动，若未启动，尝试重新创建扫码相机流。

### Reset focus mode failed

**错误信息**

Internal error. Reset focus mode failed.

**错误描述**

设置连续自动对焦模式失败。

**可能原因**

相机异常。

**处理步骤**

检查扫码相机流是否已启动，若未启动，尝试重新创建扫码相机流。

### Camera config captureSession failed

**错误信息**

Internal error. Camera config captureSession failed.

**错误描述**

相机异常。

**可能原因**

相机配流失败。

**处理步骤**

建议尝试释放扫码相机流，然后重新创建业务。

### Camera create cameraManager failed

**错误信息**

Internal error. Camera create cameraManager failed.

**错误描述**

相机异常。

**可能原因**

相机创建cameraManager失败。

**处理步骤**

建议尝试释放扫码相机流，然后重新创建业务。

### Camera create camera session failed

**错误信息**

Internal error. Camera create camera session failed.

**错误描述**

相机异常。

**可能原因**

相机创建session失败。

**处理步骤**

建议尝试释放扫码相机流，然后重新创建业务。

### Camera restart camera session failed

**错误信息**

Internal error. Camera restart camera session failed.

**错误描述**

相机异常。

**可能原因**

相机重启失败。

**处理步骤**

建议尝试释放扫码相机流，然后重新创建业务。

### Camera create preview output failed

**错误信息**

Internal error. Camera create preview output failed.

**错误描述**

相机异常。

**可能原因**

相机创建预览流失败。

**处理步骤**

建议尝试释放扫码相机流，然后重新创建业务。

### Camera get supported output capability failed

**错误信息**

Internal error. Camera get supported output capability failed.

**错误描述**

相机异常。

**可能原因**

查询指定相机支持的输出能力失败。

**处理步骤**

建议尝试释放扫码相机流，然后重新创建业务。

### Capability not supported. Failed to call the API due to limited device capabilities

**错误信息**

Internal error. Capability not supported. Failed to call the API due to limited device capabilities.

**错误描述**

该设备不支持此API，因此无法正常调用。

**可能原因**

可能出现该错误码的场景为：该设备已支持该API所属的Syscap，但是并不支持此API。

**处理步骤**

应避免在该设备上使用此API，或在代码中通过判断来规避异常场景下应用在不同设备上运行所产生的影响。

## 1000500002 用户取消扫码

**错误信息**

The user canceled the barcode scanning.

**错误描述**

用户取消扫码。

**可能原因**

用户点击关闭按钮或侧滑取消默认界面扫码。

**处理步骤**

使用[startScanForResult](scan-scanbarcode-api.md#startscanforresult)会返回此错误码，请根据使用场景处理用户取消默认界面扫码后的业务流程。
