---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-componentsnapshot
title: Class (ComponentSnapshot)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (ComponentSnapshot)
category: harmonyos-references
scraped_at: 2026-04-29T13:50:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9ce87258c996e51909a1aec20ce66912085951d609b17651d944318ed87cf3dd
---

提供获取组件截图的能力，包括已加载的组件的截图和没有加载的组件的截图。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 以下API需先使用UIContext中的[getComponentSnapshot()](arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12)方法获取ComponentSnapshot对象，再通过此实例调用对应方法。
* 缩放、平移、旋转等图形变换属性只对被截图组件的子组件生效；对目标组件本身应用图形变换属性不生效，显示的还是图形变换前的效果。

## get12+

PhonePC/2in1TabletTVWearable

get(id: string, callback: AsyncCallback<image.PixelMap>, options?: componentSnapshot.SnapshotOptions): void

获取已加载的组件的截图，传入组件的[组件标识](ts-universal-attributes-component-id.md)，找到对应组件进行截图。使用callback异步回调。

说明

截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 目标组件的[组件标识](ts-universal-attributes-component-id.md)。  **说明：** 不支持未挂树组件，当传入的组件标识是离屏或缓存未挂树的节点时，系统不会对其进行截图。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<image.[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数。当截图返回结果成功，err为undefined，data为获取到的image.[PixelMap](arkts-apis-image-pixelmap.md)；否则为错误对象。 |
| options | [componentSnapshot.SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[截图错误码](errorcode-snapshot.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { UIContext } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SnapshotExample {
7. @State pixmap: image.PixelMap | undefined = undefined;
8. uiContext: UIContext = this.getUIContext();

10. build() {
11. Column() {
12. Row() {
13. Image(this.pixmap).width(150).height(150).border({ color: Color.Black, width: 2 }).margin(5)
14. // $r('app.media.img')需要替换为开发者所需的图像资源文件
15. Image($r('app.media.img'))
16. .autoResize(true)
17. .width(150)
18. .height(150)
19. .margin(5)
20. .id("root")
21. }

23. Button("click to generate UI snapshot")
24. .onClick(() => {
25. this.uiContext.getComponentSnapshot().get("root", (error: Error, pixmap: image.PixelMap) => {
26. if (error) {
27. console.error(`error: ${JSON.stringify(error)}`);
28. return;
29. }
30. this.pixmap = pixmap;
31. }, { scale: 2, waitUntilRenderFinished: true });
32. }).margin(10)
33. }
34. .width('100%')
35. .height('100%')
36. .alignItems(HorizontalAlign.Center)
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ZPVS6K8jTe-Q3YhRElvHIw/zh-cn_image_0000002589245737.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055031Z&HW-CC-Expire=86400&HW-CC-Sign=4BD322DF5D62DC5CF51F697354C29402603C45902FDBC4A9B4148FAF7BB4FC98)

## get12+

PhonePC/2in1TabletTVWearable

get(id: string, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>

获取已加载的组件的截图，传入组件的[组件标识](ts-universal-attributes-component-id.md)，找到对应组件进行截图。使用Promise异步回调。

说明

截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 目标组件的[组件标识](ts-universal-attributes-component-id.md)。  **说明：** 不支持未挂树组件，当传入的组件标识是离屏或缓存未挂树的节点时，系统不会对其进行截图。 |
| options | [componentSnapshot.SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回组件截图对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[截图错误码](errorcode-snapshot.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { UIContext } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SnapshotExample {
7. @State pixmap: image.PixelMap | undefined = undefined;
8. uiContext: UIContext = this.getUIContext();

10. build() {
11. Column() {
12. Row() {
13. Image(this.pixmap).width(150).height(150).border({ color: Color.Black, width: 2 }).margin(5)
14. // $r('app.media.icon')需要替换为开发者所需的图像资源文件
15. Image($r('app.media.icon'))
16. .autoResize(true)
17. .width(150)
18. .height(150)
19. .margin(5)
20. .id("root")
21. }

23. Button("click to generate UI snapshot")
24. .onClick(() => {
25. this.uiContext.getComponentSnapshot()
26. .get("root", { scale: 2, waitUntilRenderFinished: true })
27. .then((pixmap: image.PixelMap) => {
28. this.pixmap = pixmap;
29. })
30. .catch((err: Error) => {
31. console.error(`error: ${err}`);
32. })
33. }).margin(10)
34. }
35. .width('100%')
36. .height('100%')
37. .alignItems(HorizontalAlign.Center)
38. }
39. }
```

## createFromBuilder12+

PhonePC/2in1TabletTVWearable

createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): void

传入[CustomBuilder](ts-types.md#custombuilder8)自定义组件，系统对其进行离屏构建后进行截图。使用callback异步回调。

说明

* 由于需要等待组件构建、渲染成功，离屏截图的回调有500ms以内的延迟，不适宜使用在对性能敏感的场景。
* 部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的[Image](ts-basic-components-image.md)组件、[Web](arkts-basic-components-web.md)组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 自定义组件构建函数。  **说明：** 不支持全局builder。  builder的根组件宽高为0时，截图操作会失败并抛出100001错误码。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<image.[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数。当截图返回结果成功，err为undefined，data为获取到的image.[PixelMap](arkts-apis-image-pixelmap.md)；否则为错误对象。支持在回调中获取离屏组件绘制区域坐标和大小。 |
| delay | number | 否 | 指定触发截图指令的延迟时间。当布局中使用了图片组件时，需要指定延迟时间，以便系统解码图片资源。资源越大，解码需要的时间越长，建议尽量使用不需要解码的PixelMap资源。  当使用PixelMap资源或对Image组件设置[syncLoad](ts-basic-components-image.md#syncload8)为true时，可以配置delay为0，强制不等待触发截图。该延迟时间并非指接口从调用到返回的时间，由于系统需要对传入的builder进行临时离屏构建，因此返回的时间通常要比该延迟时间长。  **说明：** 截图接口传入的builder中，不应使用状态变量控制子组件的构建，如果必须要使用，在调用截图接口时，也不应再有变化，以避免出现截图不符合预期的情况。  默认值：300  单位：毫秒  取值范围：[0, +∞)，小于0时按默认值处理。 |
| checkImageStatus | boolean | 否 | 指定是否允许在截图之前，校验图片解码状态。如果为true，则会在截图之前检查所有Image组件是否已经解码完成，如果没有完成检查，则会放弃截图并返回异常。  默认值：false |
| options | [componentSnapshot.SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[截图错误码](errorcode-snapshot.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The builder is not a valid build function. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |
| 160004 | isAuto(true) is not supported for offscreen node snapshots. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { UIContext } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ComponentSnapshotExample {
7. @State pixmap: image.PixelMap | undefined = undefined;
8. uiContext: UIContext = this.getUIContext();

10. @Builder
11. RandomBuilder() {
12. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
13. Text('Test menu item 1')
14. .fontSize(20)
15. .width(100)
16. .height(50)
17. .textAlign(TextAlign.Center)
18. Divider().height(10)
19. Text('Test menu item 2')
20. .fontSize(20)
21. .width(100)
22. .height(50)
23. .textAlign(TextAlign.Center)
24. }
25. .width(100)
26. .id("builder")
27. }

29. build() {
30. Column() {
31. Button("click to generate UI snapshot")
32. .onClick(() => {
33. this.uiContext.getComponentSnapshot().createFromBuilder(() => {
34. this.RandomBuilder()
35. },
36. (error: Error, pixmap: image.PixelMap) => {
37. if (error) {
38. console.error(`error: ${JSON.stringify(error)}`);
39. return;
40. }
41. this.pixmap = pixmap;
42. }, 320, true, { scale: 2, waitUntilRenderFinished: true });
43. })
44. Image(this.pixmap)
45. .margin(10)
46. .height(200)
47. .width(200)
48. .border({ color: Color.Black, width: 2 })
49. }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
50. }
51. }
```

## createFromBuilder12+

PhonePC/2in1TabletTVWearable

createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>

传入[CustomBuilder](ts-types.md#custombuilder8)自定义组件，系统对其进行离屏构建后进行截图。使用Promise异步回调。

说明

* 由于需要等待组件构建、渲染成功，离屏截图的回调有500ms以内的延迟，不适宜使用在对性能敏感的场景。
* 部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的[Image](ts-basic-components-image.md)组件、[Web](arkts-basic-components-web.md)组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 自定义组件构建函数。  **说明：** 不支持全局builder。  builder的根组件宽高为0时，截图操作会失败并抛出100001错误码。 |
| delay | number | 否 | 指定触发截图指令的延迟时间。当布局中使用了图片组件时，需要指定延迟时间，以便系统解码图片资源。资源越大，解码需要的时间越长，建议尽量使用不需要解码的PixelMap资源。  当使用PixelMap资源或对Image组件设置[syncLoad](ts-basic-components-image.md#syncload8)为true时，可以配置delay为0，强制不等待触发截图。该延迟时间并非指接口从调用到返回的时间，由于系统需要对传入的builder进行临时离屏构建，因此返回的时间通常要比该延迟时间长。  **说明：** 截图接口传入的builder中，不应使用状态变量控制子组件的构建，如果必须要使用，在调用截图接口时，也不应再有变化，以避免出现截图不符合预期的情况。  默认值：300  单位：毫秒  取值范围：[0, +∞)，小于0时按默认值处理。 |
| checkImageStatus | boolean | 否 | 指定是否允许在截图之前，校验图片解码状态。如果为true，则会在截图之前检查所有Image组件是否已经解码完成，如果没有完成检查，则会放弃截图并返回异常。  默认值：false |
| options | [componentSnapshot.SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回组件截图对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[截图错误码](errorcode-snapshot.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The builder is not a valid build function. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |
| 160004 | isAuto(true) is not supported for offscreen node snapshots. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { UIContext } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ComponentSnapshotExample {
7. @State pixmap: image.PixelMap | undefined = undefined;
8. uiContext: UIContext = this.getUIContext();

10. @Builder
11. RandomBuilder() {
12. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
13. Text('Test menu item 1')
14. .fontSize(20)
15. .width(100)
16. .height(50)
17. .textAlign(TextAlign.Center)
18. Divider().height(10)
19. Text('Test menu item 2')
20. .fontSize(20)
21. .width(100)
22. .height(50)
23. .textAlign(TextAlign.Center)
24. }
25. .width(100)
26. .id("builder")
27. }

29. build() {
30. Column() {
31. Button("click to generate UI snapshot")
32. .onClick(() => {
33. this.uiContext.getComponentSnapshot()
34. .createFromBuilder(() => {
35. this.RandomBuilder()
36. }, 320, true, { scale: 2, waitUntilRenderFinished: true })
37. .then((pixmap: image.PixelMap) => {
38. this.pixmap = pixmap;
39. })
40. .catch((err: Error) => {
41. console.error(`error: ${err}`);
42. })
43. })
44. Image(this.pixmap)
45. .margin(10)
46. .height(200)
47. .width(200)
48. .border({ color: Color.Black, width: 2 })
49. }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
50. }
51. }
```

## getSync12+

PhonePC/2in1TabletTVWearable

getSync(id: string, options?: componentSnapshot.SnapshotOptions): image.PixelMap

获取已加载的组件的截图。传入组件的[组件标识](ts-universal-attributes-component-id.md)，找到对应组件进行截图，同步等待截图完成返回[PixelMap](arkts-apis-image-pixelmap.md)。本方法会阻塞主线程，请谨慎使用。接口的最大等待时间为3s，如果3s后未返回将会抛出异常。

说明

截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 目标组件的[组件标识](ts-universal-attributes-component-id.md)。  **说明：** 不支持未挂树组件，当传入的组件标识是离屏或缓存未挂树的节点时，系统不会对其进行截图。 |
| options | [componentSnapshot.SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

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

**示例：**

```
1. import { image } from '@kit.ImageKit';

3. @Entry
4. @Component
5. struct SnapshotExample {
6. @State pixmap: image.PixelMap | undefined = undefined;

8. build() {
9. Column() {
10. Row() {
11. Image(this.pixmap).width(150).height(150).border({ color: Color.Black, width: 2 }).margin(5)
12. // $r('app.media.img')需要替换为开发者所需的图像资源文件
13. Image($r('app.media.img'))
14. .autoResize(true)
15. .width(150)
16. .height(150)
17. .margin(5)
18. .id("root")
19. }

21. Button("click to generate UI snapshot")
22. .onClick(() => {
23. try {
24. let pixelmap =
25. this.getUIContext().getComponentSnapshot().getSync("root", { scale: 2, waitUntilRenderFinished: true });
26. this.pixmap = pixelmap;
27. } catch (error) {
28. console.error(`getSync errorCode: ${error.code} message: ${error.message}`);
29. }
30. }).margin(10)
31. }
32. .width('100%')
33. .height('100%')
34. .alignItems(HorizontalAlign.Center)
35. }
36. }
```

## getWithUniqueId15+

PhonePC/2in1TabletTVWearable

getWithUniqueId(uniqueId: number, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>

获取已加载的组件的截图，传入组件的uniqueId，找到对应组件进行截图。使用Promise异步回调。

说明

截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uniqueId | number | 是 | 目标组件的uniqueId。FrameNode节点的uniqueId可通过[getUniqueId](js-apis-arkui-framenode.md#getuniqueid12)接口获取。  **说明：** 不支持未挂树组件，当传入的组件标识是离屏或缓存未挂树的节点时，系统不会对其进行截图。 |
| options | [componentSnapshot.SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回组件截图对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[截图错误码](errorcode-snapshot.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { UIContext } from '@kit.ArkUI';

5. class MyNodeController extends NodeController {
6. public node: FrameNode | null = null;
7. public imageNode: FrameNode | null = null;

9. makeNode(uiContext: UIContext): FrameNode | null {
10. this.node = new FrameNode(uiContext);
11. this.node.commonAttribute.width('100%').height('100%');

13. let image = typeNode.createNode(uiContext, 'Image');
14. // $r('app.media.img')需要替换为开发者所需的图像资源文件
15. image.initialize($r('app.media.img')).width('100%').height('100%').autoResize(true);
16. this.imageNode = image;

18. this.node.appendChild(image);
19. return this.node;
20. }
21. }

23. @Entry
24. @Component
25. struct SnapshotExample {
26. private myNodeController: MyNodeController = new MyNodeController();
27. @State pixmap: image.PixelMap | undefined = undefined;

29. build() {
30. Column() {
31. Row() {
32. Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
33. NodeContainer(this.myNodeController).width(200).height(200).margin(5)
34. }

36. Button("UniqueId get snapshot")
37. .onClick(() => {
38. try {
39. this.getUIContext()
40. .getComponentSnapshot()
41. .getWithUniqueId(this.myNodeController.imageNode?.getUniqueId(),
42. { scale: 2, waitUntilRenderFinished: true })
43. .then((pixmap: image.PixelMap) => {
44. this.pixmap = pixmap;
45. })
46. .catch((err: Error) => {
47. console.error(`error: ${err}`);
48. })
49. } catch (error) {
50. console.error(`UniqueId get snapshot Error: ${JSON.stringify(error)}`);
51. }
52. }).margin(10)
53. }
54. .width('100%')
55. .height('100%')
56. .alignItems(HorizontalAlign.Center)
57. }
58. }
```

## getSyncWithUniqueId15+

PhonePC/2in1TabletTVWearable

getSyncWithUniqueId(uniqueId: number, options?: componentSnapshot.SnapshotOptions): image.PixelMap

获取已加载的组件的截图，传入组件的uniqueId，找到对应组件进行截图。同步等待截图完成返回[PixelMap](arkts-apis-image-pixelmap.md)。

说明

截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uniqueId | number | 是 | 目标组件的uniqueId。FrameNode节点的uniqueId可通过[getUniqueId](js-apis-arkui-framenode.md#getuniqueid12)接口获取。  **说明：** 不支持未挂树组件，当传入的组件标识是离屏或缓存未挂树的节点时，系统不会对其进行截图。 |
| options | [componentSnapshot.SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。 |

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

**示例：**

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { UIContext } from '@kit.ArkUI';
4. // 自定义节点控制器，创建包含Image的FrameNode节点
5. class MyNodeController extends NodeController {
6. public node: FrameNode | null = null;
7. public imageNode: FrameNode | null = null;
8. // 构建自定义节点，创建根FrameNode并添加Image子节点，配置Image资源与样式
9. makeNode(uiContext: UIContext): FrameNode | null {
10. this.node = new FrameNode(uiContext);
11. this.node.commonAttribute.width('100%').height('100%');

13. let image = typeNode.createNode(uiContext, 'Image');
14. // $r('app.media.img')需要替换为开发者所需的图像资源文件
15. image.initialize($r('app.media.img')).width('100%').height('100%').autoResize(true);
16. this.imageNode = image;

18. this.node.appendChild(image);
19. return this.node;
20. }
21. }

23. @Entry
24. @Component
25. struct SnapshotExample {
26. private myNodeController: MyNodeController = new MyNodeController();
27. @State pixmap: image.PixelMap | undefined = undefined;

29. build() {
30. Column() {
31. Row() {
32. Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
33. NodeContainer(this.myNodeController).width(200).height(200).margin(5)
34. }

36. Button("UniqueId getSync snapshot")
37. .onClick(() => {
38. try {
39. // 通过节点唯一ID同步生成组件快照，缩放比例为2倍，等待渲染完成后生成
40. this.pixmap = this.getUIContext()
41. .getComponentSnapshot()
42. .getSyncWithUniqueId(this.myNodeController.imageNode?.getUniqueId(),
43. { scale: 2, waitUntilRenderFinished: true });
44. } catch (error) {
45. console.error(`UniqueId getSync snapshot Error: ${JSON.stringify(error)}`);
46. }
47. }).margin(10)
48. }
49. .width('100%')
50. .height('100%')
51. .alignItems(HorizontalAlign.Center)
52. }
53. }
```

## createFromComponent18+

PhonePC/2in1TabletTVWearable

createFromComponent<T extends Object>(content: ComponentContent<T>, delay?: number, checkImageStatus?: boolean, options?: componentSnapshot.SnapshotOptions): Promise<image.PixelMap>

将传入的content对象进行截图。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | 当前UIContext显示的组件内容。 |
| delay | number | 否 | 指定触发截图指令的延迟时间。当布局中使用了图片组件时，需要指定延迟时间，以便系统解码图片资源。资源越大，解码需要的时间越长，建议尽量使用不需要解码的PixelMap资源。  当使用PixelMap资源或对Image组件设置[syncLoad](ts-basic-components-image.md#syncload8)为true时，可以配置delay为0，强制不等待触发截图。该延迟时间并非指接口从调用到返回的时间，由于系统需要对传入的builder进行临时离屏构建，因此返回的时间通常要比该延迟时间长。  **说明：** 截图接口传入的builder中，不应使用状态变量控制子组件的构建，如果必须要使用，在调用截图接口时，也不应再有变化，以避免出现截图不符合预期的情况。  取值范围：[0,+∞) ，小于0时按默认值处理。  默认值：300  单位：毫秒 |
| checkImageStatus | boolean | 否 | 指定是否允许在截图之前，校验图片解码状态。如果为true，则会在截图之前检查所有Image组件是否已经解码完成，如果没有完成检查，则会放弃截图并返回异常。  默认值：false |
| options | [componentSnapshot.SnapshotOptions](js-apis-arkui-componentsnapshot.md#snapshotoptions12) | 否 | 截图相关的自定义参数。可以指定截图时图形侧绘制pixelmap的缩放比例与是否强制等待系统执行截图指令前所有绘制指令都执行完成之后再截图。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回组件截图对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[截图错误码](errorcode-snapshot.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The builder is not a valid build function. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |
| 160004 | isAuto(true) is not supported for offscreen node snapshots. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { ComponentContent } from '@kit.ArkUI';

4. class Params {
5. text: string | undefined | null = "";

7. constructor(text: string | undefined | null) {
8. this.text = text;
9. }
10. }

12. @Builder
13. function buildText(params: Params) {
14. ReusableChildComponent({ text: params.text })
15. }

17. @Component
18. struct ReusableChildComponent {
19. @Prop text: string | undefined | null = "";

21. aboutToReuse(params: Record<string, object>) {
22. console.info(`ReusableChildComponent Reusable ${JSON.stringify(params)}`);
23. }

25. aboutToRecycle(): void {
26. console.info(`ReusableChildComponent aboutToRecycle ${this.text}`);
27. }

29. build() {
30. Column() {
31. Text(this.text)
32. .fontSize(90)
33. .fontWeight(FontWeight.Bold)
34. .margin({ bottom: 36 })
35. .width('100%')
36. .height('100%')
37. }.backgroundColor('#FFF0F0F0')
38. }
39. }

41. @Entry
42. @Component
43. struct Index {
44. @State pixmap: image.PixelMap | undefined = undefined;
45. @State message: string | undefined | null = "hello";
46. uiContext: UIContext = this.getUIContext();

48. build() {
49. Row() {
50. Column() {
51. Button("点击生成组件截图")
52. .onClick(() => {
53. let uiContext = this.getUIContext();
54. let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(this.message));
55. this.uiContext.getComponentSnapshot()
56. .createFromComponent(contentNode
57. , 320, true, { scale: 2, waitUntilRenderFinished: true })
58. .then((pixmap: image.PixelMap) => {
59. this.pixmap = pixmap;
60. })
61. .catch((err: Error) => {
62. console.error(`error: ${err}`);
63. })
64. })
65. Image(this.pixmap)
66. .margin(10)
67. .height(200)
68. .width(200)
69. .border({ color: Color.Black, width: 2 })
70. }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
71. }
72. .width('100%')
73. .height('100%')
74. }
75. }
```
