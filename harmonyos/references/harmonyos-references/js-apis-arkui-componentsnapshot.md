---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentsnapshot
title: @ohos.arkui.componentSnapshot (组件截图)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.componentSnapshot (组件截图)
category: harmonyos-references
scraped_at: 2026-04-29T13:50:29+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:d58547d4939c1e14fa4396d6755d15ce48e63cde969ae5ea26b9dae50bc18a51
---

本模块提供获取组件截图的能力，包括已加载的组件的截图和没有加载的组件的截图。组件截图只能够截取组件大小的区域，如果组件的绘制超出了它的区域，或子组件的绘制超出了父组件的区域，这些在组件区域外绘制的内容不会在截图中呈现。兄弟节点堆叠在组件区域内，截图不会显示兄弟组件。

缩放、平移、旋转等图形变换属性只对被截图组件的子组件生效；对目标组件本身应用图形变换属性不生效，显示的仍然是图形变换前的效果。

组件截图典型使用场景（如长截图）及最佳实践请参考[使用组件截图](../harmonyos-guides/arkts-uicontext-component-snapshot.md)。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 对于使用[XComponent](ts-basic-components-xcomponent.md)的场景，例如：Video或者相机流媒体展示类组件，不建议使用组件截图相关接口，建议使用[createPixelMapFromSurface](arkts-apis-image-f.md#imagecreatepixelmapfromsurface11)直接获取图片。
* 如果组件自身内容不能填满组件大小区域，那么剩余位置截图返回的内容为透明像素。如果组件使用了[图像效果](ts-universal-attributes-image-effect.md)类属性或其他的效果类属性，则可能产生非用户预期的截图结果。请排查是否需要填充组件透明内容区域，或使用[窗口截图](arkts-apis-window-window.md#snapshot9)替代。
* 示例效果请以真机运行为准，当前 DevEco Studio预览器不支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { componentSnapshot } from '@kit.ArkUI';
```

## componentSnapshot.get(deprecated)

PhonePC/2in1TabletTVWearable

get(id: string, callback: AsyncCallback<image.PixelMap>, options?: SnapshotOptions): void

获取已加载的组件的截图，传入组件的[组件标识](ts-universal-attributes-component-id.md)，找到对应组件进行截图。通过回调返回结果。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[get](arkts-apis-uicontext-componentsnapshot.md#get12)替代。get需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)方法获取[ComponentSnapshot](arkts-apis-uicontext-componentsnapshot.md)对象，然后通过该对象进行调用。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)方法获取当前UI上下文关联的[ComponentSnapshot](arkts-apis-uicontext-componentsnapshot.md)对象。
* 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 目标组件的[组件标识](ts-universal-attributes-component-id.md)。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<image.[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 截图返回结果的回调。 |
| options12+ | [SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |

说明

直接使用componentSnapshot可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```
1. import { componentSnapshot } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';

4. @Entry
5. @Component
6. struct SnapshotExample {
7. @State pixmap: image.PixelMap | undefined = undefined

9. build() {
10. Column() {
11. Row() {
12. Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
13. // $r('app.media.img')需要替换为开发者所需的图像资源文件
14. Image($r('app.media.img'))
15. .autoResize(true)
16. .width(200)
17. .height(200)
18. .margin(5)
19. .id("root")
20. }

22. Button("click to generate UI snapshot")
23. .onClick(() => {
24. // 建议使用this.getUIContext().getComponentSnapshot().get()
25. componentSnapshot.get("root", (error: Error, pixmap: image.PixelMap) => {
26. if (error) {
27. console.error(`error:${JSON.stringify(error)}`)
28. return;
29. }
30. this.pixmap = pixmap
31. }, { scale: 2, waitUntilRenderFinished: true })
32. }).margin(10)
33. }
34. .width('100%')
35. .height('100%')
36. .alignItems(HorizontalAlign.Center)
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/dnuDKCpZQBq4QIHCvU_t0Q/zh-cn_image_0000002589325789.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055027Z&HW-CC-Expire=86400&HW-CC-Sign=53647B3629981E8C069B256F782A0B580D4291C619E8C4F9F2868579FC7EAA3A)

## componentSnapshot.get(deprecated)

PhonePC/2in1TabletTVWearable

get(id: string, options?: SnapshotOptions): Promise<image.PixelMap>

获取已加载的组件的截图，传入组件的[组件标识](ts-universal-attributes-component-id.md)，找到对应组件进行截图。通过Promise返回结果。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[get](arkts-apis-uicontext-componentsnapshot.md#get12-1)替代。get需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)方法获取[ComponentSnapshot](arkts-apis-uicontext-componentsnapshot.md)对象，然后通过该对象进行调用。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)方法获取当前UI上下文关联的[ComponentSnapshot](arkts-apis-uicontext-componentsnapshot.md)对象。
* 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 目标组件的[组件标识](ts-universal-attributes-component-id.md)。 |
| options12+ | [SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.[PixelMap](arkts-apis-image-pixelmap.md)> | 截图返回的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |

说明

直接使用componentSnapshot可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```
1. import { componentSnapshot } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';

4. @Entry
5. @Component
6. struct SnapshotExample {
7. @State pixmap: image.PixelMap | undefined = undefined

9. build() {
10. Column() {
11. Row() {
12. Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
13. // $r('app.media.img')需要替换为开发者所需的图像资源文件
14. Image($r('app.media.img'))
15. .autoResize(true)
16. .width(200)
17. .height(200)
18. .margin(5)
19. .id("root")
20. }

22. Button("click to generate UI snapshot")
23. .onClick(() => {
24. // 建议使用this.getUIContext().getComponentSnapshot().get()
25. componentSnapshot.get("root", { scale: 2, waitUntilRenderFinished: true })
26. .then((pixmap: image.PixelMap) => {
27. this.pixmap = pixmap
28. }).catch((err: Error) => {
29. console.error(`error:${err}`)
30. })
31. }).margin(10)
32. }
33. .width('100%')
34. .height('100%')
35. .alignItems(HorizontalAlign.Center)
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/igcO0Go_T1KGenMLDSHxxQ/zh-cn_image_0000002589325789.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055027Z&HW-CC-Expire=86400&HW-CC-Sign=4BEA1FFB230B5A1C427DAD2AD4D73ED7D984C03429760E9FBA9A9FF7B8622F1F)

## componentSnapshot.createFromBuilder(deprecated)

PhonePC/2in1TabletTVWearable

createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void

在应用后台渲染CustomBuilder自定义组件，并输出其截图。通过回调返回结果并支持在回调中获取离屏组件绘制区域坐标和大小。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[createFromBuilder](arkts-apis-uicontext-componentsnapshot.md#createfrombuilder12)替代。createFromBuilder需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)方法获取[ComponentSnapshot](arkts-apis-uicontext-componentsnapshot.md)对象，然后通过该对象进行调用。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)方法获取当前UI上下文关联的[ComponentSnapshot](arkts-apis-uicontext-componentsnapshot.md)对象。
* 由于需要等待组件构建、渲染成功，离屏截图的回调有500ms以内的延迟。
* builder中的组件不支持设置动画相关的属性，如[transition](ts-transition-animation-component.md)。
* 部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的[Image](ts-basic-components-image.md)组件、[Web](arkts-basic-components-web.md)组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 自定义组件构建函数。  **说明：** 不支持全局builder。  builder的根组件宽高为0时，截图操作会失败并抛出100001错误码。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<image.[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 截图返回结果的回调。支持在回调中获取离屏组件绘制区域坐标和大小。 |
| delay12+ | number | 否 | 指定触发截图指令的延迟时间。当布局中使用了图片组件时，需要指定延迟时间，以便系统解码图片资源。资源越大，解码需要的时间越长，建议尽量使用不需要解码的PixelMap资源。  当使用PixelMap资源或对Image组件设置syncLoad为true时，可以配置delay为0，强制不等待触发截图。该延迟时间并非指接口从调用到返回的时间，由于系统需要对传入的builder进行临时离屏构建，因此返回的时间通常要比该延迟时间长。  **说明：** 截图接口传入的builder中，不应使用状态变量控制子组件的构建，如果必须要使用，在调用截图接口时，也不应再有变化，以避免出现截图不符合预期的情况。  默认值：300  单位：毫秒  取值范围：[0, +∞)，小于0时按默认值处理。 |
| checkImageStatus12+ | boolean | 否 | 指定是否允许在截图之前，校验图片解码状态。如果为true，则会在截图之前检查所有Image组件是否已经解码完成。为false，则不会校验图片解码状态。如果没有完成检查，则会放弃截图并返回异常。  默认值：false |
| options12+ | [SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[截图错误码](errorcode-snapshot.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The builder is not a valid build function. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled. |

说明

直接使用componentSnapshot可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```
1. import { componentSnapshot } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';

4. @Entry
5. @Component
6. struct OffscreenSnapshotExample {
7. @State pixmap: image.PixelMap | undefined = undefined

9. @Builder
10. RandomBuilder() {
11. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
12. Text('Test menu item 1')
13. .fontSize(20)
14. .width(100)
15. .height(50)
16. .textAlign(TextAlign.Center)
17. Divider().height(10)
18. Text('Test menu item 2')
19. .fontSize(20)
20. .width(100)
21. .height(50)
22. .textAlign(TextAlign.Center)
23. }
24. .width(100)
25. .id("builder")
26. }

28. build() {
29. Column() {
30. Button("click to generate offscreen UI snapshot")
31. .onClick(() => {
32. // 建议使用this.getUIContext().getComponentSnapshot().createFromBuilder()
33. componentSnapshot.createFromBuilder(() => {
34. this.RandomBuilder()
35. },
36. (error: Error, pixmap: image.PixelMap) => {
37. if (error) {
38. console.error(`error:${JSON.stringify(error)}`)
39. return;
40. }
41. this.pixmap = pixmap
42. // 保存pixmap到文件中
43. // ....
44. // 获取组件大小和位置
45. let info = this.getUIContext().getComponentUtils().getRectangleById("builder")
46. console.info(info.size.width + ' ' + info.size.height + ' ' + info.localOffset.x + ' ' +
47. info.localOffset.y + ' ' + info.windowOffset.x + ' ' + info.windowOffset.y)
48. }, 320, true, { scale: 2, waitUntilRenderFinished: true })
49. })
50. Image(this.pixmap)
51. .margin(10)
52. .height(200)
53. .width(200)
54. .border({ color: Color.Black, width: 2 })
55. }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/G_oTHCvBTCWPJwdjaj_9BQ/zh-cn_image_0000002589245731.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055027Z&HW-CC-Expire=86400&HW-CC-Sign=064C7F9CDFEFF24365379F5409DDC96807593E1AB124F9B2B6987F98436807C3)

## componentSnapshot.createFromBuilder(deprecated)

PhonePC/2in1TabletTVWearable

createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>

在应用后台渲染CustomBuilder自定义组件，并输出其截图。通过Promise返回结果，支持获取离屏组件绘制区域的坐标和大小。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[createFromBuilder](arkts-apis-uicontext-componentsnapshot.md#createfrombuilder12-1)替代。createFromBuilder需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)方法获取[ComponentSnapshot](arkts-apis-uicontext-componentsnapshot.md)对象，然后通过该对象进行调用。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)方法获取当前UI上下文关联的[ComponentSnapshot](arkts-apis-uicontext-componentsnapshot.md)对象。
* 由于需要等待组件构建、渲染成功，离屏截图的回调有500ms以内的延迟。
* builder中的组件不支持设置动画相关的属性，如[transition](ts-transition-animation-component.md)。
* 部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的[Image](ts-basic-components-image.md)组件、[Web](arkts-basic-components-web.md)组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 自定义组件构建函数。  **说明：** 不支持全局builder。  builder的根组件宽高为0时，截图操作会失败并抛出100001错误码。 |
| delay12+ | number | 否 | 指定触发截图指令的延迟时间。当布局中使用了图片组件时，需要指定延迟时间，以便系统解码图片资源。资源越大，解码需要的时间越长，建议尽量使用不需要解码的PixelMap资源。  当使用PixelMap资源或对Image组件设置syncLoad为true时，可以配置delay为0，强制不等待触发截图。该延迟时间并非指接口从调用到返回的时间，由于系统需要对传入的builder进行临时离屏构建，因此返回的时间通常要比该延迟时间长。  **说明：** 截图接口传入的builder中，不应使用状态变量控制子组件的构建，如果必须要使用，在调用截图接口时，也不应再有变化，以避免出现截图不符合预期的情况。  默认值：300  单位：毫秒 |
| checkImageStatus12+ | boolean | 否 | 指定是否允许在截图之前，校验图片解码状态。如果为true，则会在截图之前检查所有Image组件是否已经解码完成。为false，则不会校验图片解码状态。如果没有完成检查，则会放弃截图并返回异常。  默认值：false |
| options12+ | [SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.[PixelMap](arkts-apis-image-pixelmap.md)> | 截图返回的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[截图错误码](errorcode-snapshot.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The builder is not a valid build function. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled. |

说明

直接使用componentSnapshot可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```
1. import { componentSnapshot } from '@kit.ArkUI'
2. import { image } from '@kit.ImageKit'

4. @Entry
5. @Component
6. struct OffscreenSnapshotExample {
7. @State pixmap: image.PixelMap | undefined = undefined

9. @Builder
10. RandomBuilder() {
11. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
12. Text('Test menu item 1')
13. .fontSize(20)
14. .width(100)
15. .height(50)
16. .textAlign(TextAlign.Center)
17. Divider().height(10)
18. Text('Test menu item 2')
19. .fontSize(20)
20. .width(100)
21. .height(50)
22. .textAlign(TextAlign.Center)
23. }
24. .width(100)
25. .id("builder")
26. }

28. build() {
29. Column() {
30. Button("click to generate offscreen UI snapshot")
31. .onClick(() => {
32. // 建议使用this.getUIContext().getComponentSnapshot().createFromBuilder()
33. componentSnapshot.createFromBuilder(() => {
34. this.RandomBuilder()
35. }, 320, true, { scale: 2, waitUntilRenderFinished: true })
36. .then((pixmap: image.PixelMap) => {
37. this.pixmap = pixmap
38. // 保存pixmap到文件中
39. // ....
40. // 获取组件大小和位置
41. let info = this.getUIContext().getComponentUtils().getRectangleById("builder")
42. console.info(`${info.size.width} ${info.size.height} ${info.localOffset.x} ${
43. info.localOffset.y} ${info.windowOffset.x} ${info.windowOffset.y}`)
44. }).catch((err: Error) => {
45. console.error(`error:${err}`)
46. })
47. })
48. Image(this.pixmap)
49. .margin(10)
50. .height(200)
51. .width(200)
52. .border({ color: Color.Black, width: 2 })
53. }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/FedRTtRuQF-eVEa06T846Q/zh-cn_image_0000002589245731.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055027Z&HW-CC-Expire=86400&HW-CC-Sign=FE75DC6D92FEA60003060AD53622C6C7D4D6FA3893551EDC6F8947AB4F98AD32)

## componentSnapshot.getSync12+

PhonePC/2in1TabletTVWearable

getSync(id: string, options?: SnapshotOptions): image.PixelMap

获取已加载的组件的截图，传入组件的[组件标识](ts-universal-attributes-component-id.md)，找到对应组件进行截图。同步等待截图完成返回[PixelMap](arkts-apis-image-pixelmap.md)。

说明

截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 目标组件的[组件标识](ts-universal-attributes-component-id.md)。 |
| options | [SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.[PixelMap](arkts-apis-image-pixelmap.md) | 截图返回的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[截图错误码](errorcode-snapshot.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |
| 160002 | Timeout. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |

说明

直接使用componentSnapshot可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```
1. import { componentSnapshot } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';

4. @Entry
5. @Component
6. struct SnapshotExample {
7. @State pixmap: image.PixelMap | undefined = undefined

9. build() {
10. Column() {
11. Row() {
12. Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
13. // $r('app.media.img')需要替换为开发者所需的图像资源文件
14. Image($r('app.media.img'))
15. .autoResize(true)
16. .width(200)
17. .height(200)
18. .margin(5)
19. .id("root")
20. }

22. Button("click to generate UI snapshot")
23. .onClick(() => {
24. try {
25. // 建议使用this.getUIContext().getComponentSnapshot().getSync()
26. let pixelmap = componentSnapshot.getSync("root", { scale: 2, waitUntilRenderFinished: true })
27. this.pixmap = pixelmap
28. } catch (error) {
29. console.error(`getSync errorCode:${error.code} message:${error.message}`)
30. }
31. }).margin(10)
32. }
33. .width('100%')
34. .height('100%')
35. .alignItems(HorizontalAlign.Center)
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/He5Zd6jcRk6QXNVQfZ9n6Q/zh-cn_image_0000002589325789.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055027Z&HW-CC-Expire=86400&HW-CC-Sign=91EC7F02B69CD3949B0DFE7F28E7DD86567503925914C375EFA9689002CEC5E8)

## SnapshotOptions12+

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scale | number | 否 | 是 | 指定截图时图形侧绘制pixelmap的缩放比例，比例过大时截图时间会变长，或者截图可能会失败。  取值范围：[0, +∞)，当小于等于0时按默认情况处理。  默认值：1  **说明：**  请不要截取过大尺寸的图片，截图不建议超过屏幕尺寸的大小。当要截取的图片目标长宽超过底层限制时，截图会返回失败，不同设备的底层限制不同。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| waitUntilRenderFinished | boolean | 否 | 是 | 设置是否强制系统在截图前等待所有绘制指令执行完毕。true表示强制系统在截图前等待所有绘制指令执行完毕，false表示不强制系统在截图前等待所有绘制指令执行完毕。该选项可尽可能确保截图内容是最新的状态，应尽量开启。需要注意的是，开启后接口可能需要更长的时间返回，具体的时间依赖页面当时时刻需要重绘区域的大小。  默认值：false  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| region15+ | [SnapshotRegionType](js-apis-arkui-componentsnapshot.md#snapshotregiontype15) | 否 | 是 | 指定截图的矩形区域范围，默认为整个组件。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| colorMode23+ | [ColorModeOptions](js-apis-arkui-componentsnapshot.md#colormodeoptions23) | 否 | 是 | 指定截图使用的色彩空间。  默认值：{colorSpace: SRGB, isAuto: false}  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| dynamicRangeMode23+ | [DynamicRangeModeOptions](js-apis-arkui-componentsnapshot.md#dynamicrangemodeoptions23) | 否 | 是 | 指定截图使用的动态范围模式。  默认值：{dynamicRangeMode: STANDARD, isAuto: false}  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## ColorModeOptions23+

PhonePC/2in1TabletTVWearable

定义截图时所使用的色彩空间。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colorSpace | [colorSpaceManager.ColorSpace](js-apis-colorspacemanager.md#colorspace) | 否 | 是 | 指定截图使用的色彩空间。  如果知道被截图组件使用的色彩空间，可以通过colorSpace字段指定，并将isAuto设置为false，以达到预期的截图效果。  取值范围：[colorSpaceManager.ColorSpace](js-apis-colorspacemanager.md#colorspace)中DISPLAY\_P3、SRGB、DISPLAY\_BT2020\_SRGB。  默认值：SRGB  如果值为undefined、null或未设置，则使用默认值截图；其他异常值会导致截图失败，返回错误码160003。 |
| isAuto | boolean | 否 | 是 | 是否由系统自动决定所使用的色彩空间。  支持取值为：true表示系统自动决定所使用的色彩空间；false表示使用通过colorSpace字段设置的色彩空间类型进行截图。取非法值时，按默认值false处理。  默认值：false  离屏截图仅支持设置为false，否则会返回错误码160004。  当isAuto设置为true时，建议将[SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12)中的waitUntilRenderFinished字段也设置为true，以便确保系统可以正常检测到所用的模式。  在不确定组件使用的色彩空间时，建议将isAuto设置为true，让系统根据实际情况自动决定使用的色彩空间。  当isAuto为true时，colorSpace字段设置的值会被忽略。此时，如果被截图组件同时包含不同色彩空间的子组件时，截图的色彩空间为优先级最高的色彩空间类型，优先级排序为DISPLAY\_BT2020\_SRGB > DISPLAY\_P3 > SRGB。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { colorSpaceManager } from '@kit.ArkGraphics2D';

4. @Entry
5. @Component
6. struct SnapshotColorModeExample {
7. @State pixmap: image.PixelMap | undefined = undefined;

9. build() {
10. Column() {
11. Row() {
12. Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
13. // $r('app.media.img')需要替换为开发者所需的图像资源文件
14. Image($r('app.media.img'))
15. .autoResize(true)
16. .width(200)
17. .height(200)
18. .margin(5)
19. .id("root")
20. }

22. Button("click to generate UI snapshot")
23. .onClick(() => {
24. this.getUIContext().getComponentSnapshot().get("root", (error: Error, pixmap: image.PixelMap) => {
25. if (error) {
26. console.error(`error:${JSON.stringify(error)}`)
27. return;
28. }
29. this.pixmap = pixmap
30. }, {
31. scale: 2,
32. waitUntilRenderFinished: true,
33. // 设置色彩空间为：DISPLAY_P3
34. colorMode: { colorSpace: colorSpaceManager.ColorSpace.DISPLAY_P3, isAuto: false }
35. })
36. }).margin(10)
37. }
38. .width('100%')
39. .height('100%')
40. .alignItems(HorizontalAlign.Center)
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/hnI1VPmISniu16SGwaANkg/zh-cn_image_0000002589325789.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055027Z&HW-CC-Expire=86400&HW-CC-Sign=1B226E0D4126170D37D9DA361C53F7FF4C88A44B2A54CC3A18BD0BF62B6B7839)

## DynamicRangeModeOptions23+

PhonePC/2in1TabletTVWearable

定义截图所使用的动态范围模式。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dynamicRangeMode | [DynamicRangeMode](ts-basic-components-image.md#dynamicrangemode12枚举说明) | 否 | 是 | 指定截图使用的动态范围模式。  默认情况下，系统以[STANDARD](ts-basic-components-image.md#dynamicrangemode12枚举说明)模式进行截图。如果知道被截图组件使用的动态范围模式，可通过dynamicRangeMode字段指定具体的动态范围模式，并将isAuto设置为false，以达到预期的截图效果。  虽然动态范围模式有三种，但是HIGH和CONSTRAINT的表现均为HDR（高动态范围）。STANDARD模式对应表现为SDR（标准动态范围）。  在指定了合法的动态范围模式之后，截图实际采用的动态范围会受到被截图组件和设置值的双重影响，具体如下：  1. 当被截图组件的动态范围为SDR时，即使指定动态范围模式为HIGH，截图实际采用的动态范围为SDR。  2. 当被截图组件的动态范围为HDR时，截图实际采用的动态范围为指定的动态范围模式。  3. 当配置[色彩空间](js-apis-arkui-componentsnapshot.md#colormodeoptions23)为SRGB或DISPLAY\_P3时，截图实际采用的动态范围为SDR。  4. 如果被截图组件同时包含SDR和HDR两种动态范围的子组件时，则当作HDR处理。  5. 如果3和4的条件同时被满足，则截图实际采用的动态范围为SDR。  取值范围：[DynamicRangeMode](ts-basic-components-image.md#dynamicrangemode12枚举说明) 枚举值。  默认值：STANDARD  如果值为undefined、null或未设置，则使用默认值截图；其他异常值会导致截图失败，返回错误码160003。 |
| isAuto | boolean | 否 | 是 | 是否由系统自动决定所使用的动态范围模式。  支持取值为：true表示系统自动决定所使用的动态范围模式；false表示使用通过dynamicRangeMode字段设置的动态范围类型进行截图。取非法值时，按默认值false处理。  默认值：false  离屏截图仅支持设置为false，否则会返回错误码160004。  当isAuto设置为true时，建议将[SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12)中的waitUntilRenderFinished字段也设置为true，以便确保系统可以正常检测到所用的模式。  在不确定组件使用的动态范围模式时，建议将isAuto设置为true，让系统根据实际情况自动决定使用的动态范围模式。  当isAuto为true时，dynamicRangeMode字段设置的值会被忽略。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';

3. @Entry
4. @Component
5. struct SnapshotDynamicRangeExample {
6. @State pixmap: image.PixelMap | undefined = undefined;

8. build() {
9. Column() {
10. Row() {
11. Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
12. // $r('app.media.img')需要替换为开发者所需的图像资源文件
13. Image($r('app.media.img'))
14. .autoResize(true)
15. .width(200)
16. .height(200)
17. .margin(5)
18. .id("root")
19. }

21. Button("click to generate UI snapshot")
22. .onClick(() => {
23. this.getUIContext().getComponentSnapshot().get("root", (error: Error, pixmap: image.PixelMap) => {
24. if (error) {
25. console.error(`error:${JSON.stringify(error)}`)
26. return;
27. }
28. this.pixmap = pixmap
29. }, {
30. scale: 2,
31. waitUntilRenderFinished: true,
32. // 设置动态范围为自动模式
33. dynamicRangeMode: { dynamicRangeMode: DynamicRangeMode.STANDARD, isAuto: true }
34. })
35. }).margin(10)
36. }
37. .width('100%')
38. .height('100%')
39. .alignItems(HorizontalAlign.Center)
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/upxbZyN1Tj6Kgz5T5MNVSQ/zh-cn_image_0000002589325789.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055027Z&HW-CC-Expire=86400&HW-CC-Sign=1870B0375C2EC0B64D8E69A8D5E8DF2B4B903FC37F5D7D72CD29C2DE695AFDBF)

## SnapshotRegionType15+

PhonePC/2in1TabletTVWearable

type SnapshotRegionType = SnapshotRegion | LocalizedSnapshotRegion

表示组件截图区域，取值类型为下表中的任一类型。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [SnapshotRegion](js-apis-arkui-componentsnapshot.md#snapshotregion15) | 表示组件截图的矩形区域。 |
| [LocalizedSnapshotRegion](js-apis-arkui-componentsnapshot.md#localizedsnapshotregion15) | 表示组件截图的矩形区域，根据布局方向确定是否对矩形区域水平翻转，若布局方向为RTL，则把指定的截图区域做左右翻转处理以适应RTL布局方向。 |

## SnapshotRegion15+

PhonePC/2in1TabletTVWearable

定义组件截图的矩形区域。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 截图区域矩形左上角的x轴坐标。  单位：px  取值范围：[0, 组件宽度] |
| top | number | 否 | 否 | 截图区域矩形左上角的y轴坐标。  单位：px  取值范围：[0, 组件高度] |
| right | number | 否 | 否 | 截图区域矩形右下角的x轴坐标。  单位：px  取值范围：[0, 组件宽度] |
| bottom | number | 否 | 否 | 截图区域矩形右下角的y轴坐标。  单位：px  取值范围：[0, 组件高度] |

## LocalizedSnapshotRegion15+

PhonePC/2in1TabletTVWearable

定义组件截图的矩形区域，start和end的值在布局方向为LTR时指定为left和right，在布局方向为RTL时指定为right和left。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 否 | 布局方向为LTR时表示截图区域矩形左上角的x轴坐标，布局方向为RTL时表示截图区域矩形右上角的x轴坐标。  单位：px  取值范围：[0, 组件宽度] |
| top | number | 否 | 否 | 布局方向为LTR时表示截图区域矩形左上角的y轴坐标，布局方向为RTL时表示截图区域矩形右上角的y轴坐标。  单位：px  取值范围：[0, 组件高度] |
| end | number | 否 | 否 | 布局方向为LTR时表示截图区域矩形右下角的x轴坐标，布局方向为RTL时表示截图区域矩形左下角的x轴坐标。  单位：px  取值范围：[0, 组件宽度] |
| bottom | number | 否 | 否 | 布局方向为LTR时表示截图区域矩形右下角的y轴坐标，布局方向为RTL时表示截图区域矩形左下角的y轴坐标。  单位：px  取值范围：[0, 组件高度] |

说明

直接使用componentSnapshot可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getComponentSnapshot](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```
1. import { image } from '@kit.ImageKit';

3. @Entry
4. @Component
5. struct SnapshotExample {
6. @State pixmap: image.PixelMap | undefined = undefined

8. build() {
9. Column() {
10. Row() {
11. Column() {
12. TextClock()
13. Button("Button ABCDE").type(ButtonType.Normal)
14. Row() {
15. Checkbox()
16. Text("√")
17. Text(" | ")
18. Checkbox()
19. Text("×")
20. }.align(Alignment.Start)

22. TextInput()
23. }
24. .align(Alignment.Start)
25. .id("component1")
26. .width("600px")
27. .height("600px")
28. .borderRadius(6)
29. .borderWidth(2)
30. .borderColor(Color.Green)

32. }

34. Button("get capture")
35. .onClick(() => {
36. try {
37. let pixelmap = this.getUIContext().getComponentSnapshot().getSync("component1",
38. {
39. scale: 2,
40. waitUntilRenderFinished: true,
41. region: {
42. start: 20,
43. top: 20,
44. end: 200,
45. bottom: 240
46. }
47. })
48. this.pixmap = pixelmap
49. } catch (error) {
50. console.error(`getSync errorCode:${error.code} message:${error.message}`)
51. }
52. }).margin(10)
53. Image(this.pixmap).border({ color: Color.Black, width: 2 }).width("600px")
54. }.width("100%").align(Alignment.Center)
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/gofn1j2QQzaDShv9YWB1Tg/zh-cn_image_0000002558765920.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055027Z&HW-CC-Expire=86400&HW-CC-Sign=96463165FEEC87A4E1ABBDDAB0D4F8AC68D41D3B36069A3F43E93F4AB39EAFCB)
