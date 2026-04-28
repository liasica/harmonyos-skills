---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-dev-guides
title: 跨设备互通开发指导
breadcrumb: 指南 > 系统 > 网络 > Service Collaboration Kit（协同服务） > 跨设备互通（ArkTS） > 跨设备互通开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:10+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0e2886279408bd4f77eb782de3c80611732844f243212ad4618af8312c265fb1
---

跨设备互通提供相机、扫描以及图库（图片和视频）的跨设备调用能力，例如：平板或2in1设备可以调用手机的相机、扫描、图库等功能。从API 6.1.0(23)开始，TV、手机、平板或2in1设备可调用具备如下能力的远程设备：支持拍照、扫描及图库（图片与视频）能力的手机和平板，支持图库（图片与视频）能力的2in1设备。

## 场景介绍

您通过此能力实现跨设备交互，可以使用其他设备的相机、扫描和图库功能。

## 约束与限制

需同时满足以下条件，才能使用该功能：

* **设备限制**

  + 本端设备：HarmonyOS版本为HarmonyOS NEXT及以上的平板或2in1设备。
  + 远端设备：HarmonyOS版本为HarmonyOS NEXT及以上、具有相机能力的手机或平板设备。
* **使用限制**

  + 双端设备需要登录同一华为账号。
  + 跨设备互通API支持根据特定调用策略调用设备。调用策略：2in1设备可以调用平板和手机，平板可以调用手机，并且在6.1.0(23)之后支持TV、手机、平板或2in1设备调用支持拍照、扫描、选择图库中图片与视频能力的手机，支持拍照、扫描、选择图库中图片与视频能力的平板，以及支持选择图库中图片与视频能力的2in1设备。
  + 本端和远端设备需要打开WLAN和蓝牙开关。条件允许时，推荐本端和远端设备接入同一个局域网，可提升唤醒相机的速度。
  + 若在跨设备调用视频选择器时遇到资源加载异常，建议在调用前确认本端和远端的设备调用能力是否匹配、系统状态是否正常，并在稳定环境下重试操作。

## 接口说明

在开发具体功能前，请先查阅[参考文档](../harmonyos-references/servicecollaboration-collaborationservice.md)。

| 接口名 | 描述 |
| --- | --- |
| [createCollaborationServiceMenuItems](../harmonyos-references/servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems) | 设备列表选择器，用于获取组网内具有对应跨设备互通能力的设备列表。 |
| [CollaborationServiceStateDialog](../harmonyos-references/servicecollaboration-collaborationservice.md#collaborationservicestatedialog) | 弹窗组件，用于提示对端业务状态。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { createCollaborationServiceMenuItems, CollaborationServiceStateDialog, CollaborationServiceFilter } from '@kit.ServiceCollaborationKit';
   ```

   [createCollaborationServiceMenuItems](../harmonyos-references/servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems)是设备列表菜单项模块，传入[CollaborationServiceFilter](../harmonyos-references/servicecollaboration-collaborationservice.md#collaborationservicefilter)的能力枚举值；[CollaborationServiceStateDialog](../harmonyos-references/servicecollaboration-collaborationservice.md#collaborationservicestatedialog)是状态提示框模块。
2. 在Menu中调用createCollaborationServiceMenuItems添加设备列表选择器，在菜单项内显示设备列表。

   说明

   在调用[createCollaborationServiceMenuItems](../harmonyos-references/servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems)前，需了解：

   * 该方法需要在[Menu](../harmonyos-references/ts-basic-components-menu.md)组件内调用。
   * 该方法是自定义构建函数，您在使用前需要先了解[@Builder](arkts-builder.md)。
3. 传入Array类型的[CollaborationServiceFilter](../harmonyos-references/servicecollaboration-collaborationservice.md#collaborationservicefilter)枚举值即可使用对应能力，目前支持ALL、TAKE\_PHOTO、SCAN\_DOCUMENT、IMAGE\_PICKER、VIDEO\_PICKER和IMAGE\_VIDEO\_PICKER。

   ALL为预留值，匹配跨端拍照、文档扫描和图库选择器，功能将在后续拓展，TAKE\_PHOTO匹配跨设备拍照能力，SCAN\_DOCUMENT匹配跨设备扫描能力，IMAGE\_PICKER匹配跨设备图库能力，VIDEO\_PICKER匹配视频选择器，IMAGE\_VIDEO\_PICKER匹配图片和视频选择器。

   ```
   1. @Builder
   2. MyTestMenu() {
   3. Menu() {
   4. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL])
   5. }
   6. }
   ```
4. 在build方法中添加弹窗组件[CollaborationServiceStateDialog](../harmonyos-references/servicecollaboration-collaborationservice.md#collaborationservicestatedialog)，用于提示远端相机拍摄状态和回传数据，需要实现其中的[onState](../harmonyos-references/servicecollaboration-collaborationservice.md#onstate)方法。[CollaborationServiceStateDialog](../harmonyos-references/servicecollaboration-collaborationservice.md#collaborationservicestatedialog)是全局的提示框，不会对原有布局产生影响。
5. 为弹窗组件绑定和实现[onState](../harmonyos-references/servicecollaboration-collaborationservice.md#onstate)方法，用于接收和处理照片数据。

   回调函数的传入参数stateCode是完成状态，buffer是回传的数据内容，可通过状态和数据内容结合自身的业务逻辑实现[onState](../harmonyos-references/servicecollaboration-collaborationservice.md#onstate)方法。

   ```
   1. CollaborationServiceStateDialog({
   2. onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer):void => this.doInsertPicture(stateCode, bufferType, buffer)
   3. })
   ```

## 跨设备互通完整示例

通过以下示例，您可以完成一次调用对端相机拍摄的操作。

```
1. import {
2. createCollaborationServiceMenuItems,
3. CollaborationServiceStateDialog,
4. CollaborationServiceFilter
5. } from '@kit.ServiceCollaborationKit';
6. import { image } from '@kit.ImageKit';
7. import { hilog } from '@kit.PerformanceAnalysisKit';

9. @Entry
10. @Component
11. struct Index {
12. @State picture: PixelMap | undefined = undefined;

14. @Builder
15. MyTestMenu() {
16. Menu() {
17. createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL])
18. }
19. }

21. build() {
22. Column({ space: 20 }) {
23. CollaborationServiceStateDialog({
24. onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer): void => this.doInsertPicture(stateCode, bufferType, buffer)
25. })
26. Button('使用远端设备进行拍照')
27. .type(ButtonType.Normal)
28. .borderRadius(10)
29. .bindMenu(this.MyTestMenu)

31. if (this.picture) {
32. Image(this.picture)
33. .borderStyle(BorderStyle.Dotted)
34. .borderWidth(1)
35. .objectFit(ImageFit.Contain)
36. .height('80%')
37. .onComplete((event) => {
38. if (event != undefined) {
39. hilog.info(0, "MEMOMOCK", "onComplete " + event.loadingStatus)
40. }
41. })
42. }
43. }
44. .padding(20)
45. .width('100%')
46. .alignItems(HorizontalAlign.Center)
47. }

49. doInsertPicture(stateCode: number, bufferType: string, buffer: ArrayBuffer): void {
50. if (stateCode != 0) {
51. return
52. }
53. if (bufferType == "general.image") {
54. let imageSource = image.createImageSource(buffer)
55. imageSource.createPixelMap().then((pixelMap) => {
56. this.picture = pixelMap;
57. })
58. }
59. }
60. }
```

## 示例代码

[跨设备互通](https://gitcode.com/harmonyos_samples/service-collaboration-kit-sample-code-arkts)
