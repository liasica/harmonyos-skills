---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-component-snapshot
title: 使用组件截图（ComponentSnapshot）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > UI系统场景化能力 > 使用组件截图（ComponentSnapshot）
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c7934fd75edf43b447a546fd5432fb41e57edfb28b8ef0bca131c485ffbc399
---

## 能力介绍

组件截图是将应用内一个组件节点树的渲染结果生成位图（[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)）的能力，支持两种方式：一种是对已挂树显示的组件进行截图，另一种是对通过Builder或ComponentContent实现的离线组件进行截图。

说明

组件截图依赖UI上下文，需要在具备明确上下文的环境中调用，因此请优先使用UIContext的getComponentSnapshot接口返回的[ComponentSnapshot](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md)对象的接口，不建议直接使用从@kit.ArkUI导入的componentSnapshot接口。

### 对挂树组件截图

对已明确挂树的组件进行截图，可通过[get](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#get12-1)或[getSync](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#getsync12)实现，传入组件标识（需提前通过.id通用属性配置）以指定组件根节点。系统在通过指定的ID查找待截图组件时，仅遍历已挂树的组件，不对cache或离屏组件进行查找。系统以首个查找到的结果为准，故应用需**确保组件标识ID的唯一性**。

从API version 15开始，在已知组件的[getUniqueId](../harmonyos-references/js-apis-arkui-framenode.md#getuniqueid12)的情况下，也可以使用[getWithUniqueId](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#getwithuniqueid15)或[getSyncWithUniqueId](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#getsyncwithuniqueid15)接口来实现截图，这可以省去查找组件的过程。

截图仅能获取最近一帧的绘制内容。若在组件触发更新的同时调用截图，更新的渲染内容不会被截取，截图将返回前一帧的绘制内容。

说明

尽量避免在使用截图时触发待截图组件的刷新，防止对截图内容的干扰。

### 对离线组件截图

离线组件是指通过Builder或ComponentContent封装的、尚未挂载到树上的组件，可以使用[createFromBuilder](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#createfrombuilder12-1)来实现。从API version 18开始，也可以使用[createFromComponent](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#createfromcomponent18)实现离线组件截图。

这些组件不参与真实渲染，因此对其截图需要更长的时间，因为系统必须先进行离线构建、布局及资源加载等操作，在这些操作完成前执行的截图所获位图不符合预期。因此，通常需要通过设置delay参数指定足够的时间，确保系统能够完成这些操作。对于图片资源的加载，建议将图片组件的[syncLoad](../harmonyos-references/ts-basic-components-image.md#syncload8)属性设为 true，以强制同步加载，确保离线组件构建时图片已加载、下载及解码完成，从而确保截图过程中能够正确呈现图片像素。

## 典型使用场景

以下通过几个典型场景来说明组件截图能力的常见使用方式。

### 截取长内容（滚动截图）

较长内容通常使用滚动类容器组件实现。截图时，仅能捕获容器内可见内容，超出边界部分无法截取。若使用LazyForEach或Repeat，超出显示范围内容亦不会被系统构建及截取。

可利用滚动类容器接口，模拟用户滑动逐页截图，之后按偏移量拼接各页PixelMap位图，以生成完整长图。关键点在于模拟滑动、维护位移与位图关系及实现PixelMap位图读写。

**步骤1：添加滚动控制器及事件监听**

为了能够模拟滚动，以及监听组件滚动的具体offset，需要为List（此处以列表为例）组件添加滚动控制器以及滚动监听。

```
1. // src/main/ets/view/ScrollSnapshot.ets
2. @Component
3. export struct ScrollSnapshot {
4. private scroller: Scroller = new Scroller();
5. private listComponentWidth: number = 0; // 组件宽度，默认值为0
6. private listComponentHeight: number = 0; // 组件高度，默认值为0
7. // list组件的当前偏移量
8. private curYOffset: number = 0;
9. // 每次滚动距离
10. private scrollHeight: number = 0;

12. // ...
13. build() {
14. // ...
15. Stack() {
16. // ...
17. // 1.1 绑定滚动控制器，并通过`.id`配置组件唯一标识。
18. List({ space: 12, scroller: this.scroller }) {
19. LazyForEach(this.dataSource, (item: number) => {
20. ListItem() {
21. NewsItem({ index: item })
22. }
23. }, (item: number) => item.toString())
24. }
25. // ...
26. .id(LIST_ID)
27. // 1.2 通过回调获取滚动偏移量。
28. .onDidScroll(() => {
29. this.curYOffset = this.scroller.currentOffset().yOffset;
30. })
31. .onAreaChange((oldValue, newValue) => {
32. // 1.3 获取组件的宽高。
33. this.listComponentWidth = newValue.width as number;
34. this.listComponentHeight = newValue.height as number;
35. this.scrollHeight = this.listComponentHeight;
36. })
37. // ...
38. }
39. }
40. }
```

[ScrollSnapshot.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentSnapshot/entry/src/main/ets/view/ScrollSnapshot.ets#L30-L331)

**步骤2：循环滚动截图并缓存**

通过实现一个递归方法滚动循环截图，并在滚动过程配合一些动效实现。

```
1. /**
2. * 递归滚动截图，直到滚动到底，最后合并所有截图
3. */
4. async scrollSnapAndMerge() {
5. try {
6. // 记录滚动偏移
7. this.scrollYOffsets.push(this.curYOffset - this.yOffsetBefore);
8. // 调用组件截图接口，获取list组件的截图
9. const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
10. // 获取位图像素字节，并保存在数组中
11. let area: image.PositionArea =
12. await ImageUtils.getSnapshotArea(pixelMap, this.scrollYOffsets, this.listComponentWidth,
13. this.listComponentHeight)
14. this.areaArray.push(area);

16. // 判断是否滚动到底以及用户是否已经强制停止
17. if (!this.scroller.isAtEnd() && !this.isClickStop) {
18. // 如果没有到底或被停止，则播放一个滚动动效，延迟一段时间后，继续递归截图
19. CommonUtils.scrollAnimation(this.scroller, 1000, this.scrollHeight);
20. await CommonUtils.sleep(1500);
21. await this.scrollSnapAndMerge();
22. } else {
23. // 当滚动到底时，调用`mergeImage`将所有保存的位图数据进行拼接，返回长截图位图对象
24. this.mergedImage =
25. await ImageUtils.mergeImage(this.areaArray, this.scrollYOffsets[this.scrollYOffsets.length - 1],
26. this.listComponentWidth, this.listComponentHeight);
27. }
28. } catch (err) {
29. let error = err as BusinessError;
30. Logger.error(TAG, `scrollSnapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
31. }
32. }
```

[ScrollSnapshot.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentSnapshot/entry/src/main/ets/view/ScrollSnapshot.ets#L137-L170)

```
1. // src/main/ets/common/CommonUtils.ets
2. static scrollAnimation(scroller: Scroller, duration: number, scrollHeight: number): void {
3. scroller.scrollTo({
4. xOffset: 0,
5. yOffset: (scroller.currentOffset().yOffset + scrollHeight),
6. animation: {
7. duration: duration,
8. curve: Curve.Smooth,
9. canOverScroll: false
10. }
11. });
12. }
```

[CommonUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentSnapshot/entry/src/main/ets/common/CommonUtils.ets#L20-L33)

**步骤3：拼接长截图**

使用image.createPixelMapSync()方法创建长截图longPixelMap，并遍历之前保存的图像片段数据（this.areaArray），构建image.PositionArea对象area，然后调用longPixelMap.writePixelsSync(area)方法将这些片段逐个写入到正确的位置，从而拼接成一个完整的长截图。

```
1. static async mergeImage(areaArray: image.PositionArea[], lastOffsetY: number, listWidth: number,
2. listHeight: number): Promise<PixelMap> {
3. // 创建一个长截图位图对象
4. let opts: image.InitializationOptions = {
5. editable: true,
6. pixelFormat: 4,
7. size: {
8. width: uiContext?.vp2px(listWidth) || 0,
9. height: uiContext?.vp2px(lastOffsetY + listHeight) || 0
10. }
11. };
12. let longPixelMap = image.createPixelMapSync(opts);
13. let imgPosition: number = 0;

15. for (let i = 0; i < areaArray.length; i++) {
16. let readArea = areaArray[i];
17. let area: image.PositionArea = {
18. pixels: readArea.pixels,
19. offset: 0,
20. stride: readArea.stride,
21. region: {
22. size: {
23. width: readArea.region.size.width,
24. height: readArea.region.size.height
25. },
26. x: 0,
27. y: imgPosition
28. }
29. }
30. imgPosition += readArea.region.size.height;
31. try {
32. longPixelMap.writePixelsSync(area);
33. } catch (err) {
34. let error = err as BusinessError;
35. Logger.error(TAG, `writePixelsSync err, code: ${error.code}, message: ${error.message}`);
36. }
37. }
38. return longPixelMap;
39. }
```

[ImageUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentSnapshot/entry/src/main/ets/common/ImageUtils.ets#L101-L142)

**步骤4：保存截图**

使用安全控件SaveButton实现截图保存到相册。

```
1. // src/main/ets/view/SnapshotPreview.ets
2. SaveButton({
3. icon: SaveIconStyle.FULL_FILLED,
4. text: SaveDescription.SAVE_IMAGE,
5. buttonType: ButtonType.Capsule
6. })
7. // ···
8. .onClick((event, result) => {
9. this.saveSnapshot(result);
10. })
```

[SnapshotPreview.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentSnapshot/entry/src/main/ets/view/SnapshotPreview.ets#L226-L245)

```
1. async saveSnapshot(result: SaveButtonOnClickResult): Promise<void> {
2. try {
3. if (result === SaveButtonOnClickResult.SUCCESS) {
4. const helper = photoAccessHelper.getPhotoAccessHelper(this.context);
5. const uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
6. const file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
7. const imagePackerApi: image.ImagePacker = image.createImagePacker();
8. const packOpts: image.PackingOption = {
9. format: 'image/png',
10. quality: 100,
11. };
12. imagePackerApi.packToData(this.mergedImage, packOpts).then((data) => {
13. fileIo.writeSync(file.fd, data);
14. fileIo.closeSync(file.fd);
15. Logger.info(TAG, `Succeeded in packToFile`);
16. this.getUIContext().getPromptAction().showToast({
17. // 请将$r('app.string.save_album_success')替换为实际资源文件，在本示例中该资源文件的value值为"Saved to album"
18. message: $r('app.string.save_album_success'),
19. duration: 1800
20. })
21. }).catch((error: BusinessError) => {
22. Logger.error(TAG, `Failed to packToFile. Error code is ${error.code}, message is ${error.message}`);
23. });
24. }
25. // ...
26. } catch (err) {
27. let error = err as BusinessError;
28. Logger.error(TAG, `saveSnapshot err, errCode: ${error.code}, error message: ${error.message}`);
29. }
30. }
```

[SnapshotPreview.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentSnapshot/entry/src/main/ets/view/SnapshotPreview.ets#L80-L113)

**步骤5：保存完成后释放位图**

当位图对象不再使用时，应及时将其赋值为空，例如：this.mergedImage = undefined;。

```
1. closeSnapPopup(): void {
2. // 关闭弹窗
3. this.isShowPreview = false;
4. // 释放位图对象
5. this.mergedImage = undefined;
6. // 重置相关参数
7. this.snapPopupWidth = 100;
8. this.snapPopupHeight = 200;
9. this.snapPopupPosition =
10. PopupUtils.calcPopupCenter(this.screenWidth, this.screenHeight, this.snapPopupWidth, this.snapPopupHeight);
11. this.isLargePreview = false;
12. }
```

[SnapshotPreview.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentSnapshot/entry/src/main/ets/view/SnapshotPreview.ets#L65-L78)

### 封装全局截图接口

如前文所述，截图接口必须在UI上下文明确的位置使用。然而，应用有时希望对不同模块封装统一的全局截图方法。例如，在下述示例中，awardBuilder构建的组件是固定结构的。GlobalStaticSnapshot提供了一个getAwardSnapshot全局方法，能够满足不同模块的需求，对同一固定模式的组件进行截图，从而实现全局截图接口的封装。本示例从API version 18开始支持。

```
1. import { image } from '@kit.ImageKit';
2. import { ComponentContent } from '@kit.ArkUI';

4. export class Params {
5. public text: string | undefined | null = '';

7. constructor(text: string | undefined | null) {
8. this.text = text;
9. }
10. }

12. @Builder
13. function awardBuilder(params: Params) {
14. Column() {
15. Text(params.text)
16. .fontSize(90)
17. .fontWeight(FontWeight.Bold)
18. .margin({ bottom: 36 })
19. .width('100%')
20. .height('100%')
21. }.backgroundColor('#FFF0F0F0')
22. }

24. export class GlobalStaticSnapshot {
25. /**
26. * 一个可以获取固定对象截图的静态方法
27. */
28. static async getAwardSnapshot(uiContext: UIContext, textParam: Params): Promise<image.PixelMap | undefined> {
29. let resultPixmap: image.PixelMap | undefined = undefined
30. let contentNode = new ComponentContent(uiContext, wrapBuilder(awardBuilder), textParam);
31. await uiContext.getComponentSnapshot()
32. .createFromComponent(contentNode, 320, true, { scale: 1, waitUntilRenderFinished: true })
33. .then((pixmap: image.PixelMap) => {
34. resultPixmap = pixmap;
35. })
36. .catch((err: Error) => {
37. console.error(`error: ${err}`);
38. })
39. return resultPixmap;
40. }
41. }
```

[GlobalScreenshot.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentSnapshot/entry/src/main/ets/view/GlobalScreenshot.ets#L16-L58)

**完整示例：**

完整示例请参考[长截图](../best-practices/bpta-long-snapshot-practice.md#section1566681910427)。

## 组件截图最佳实践

### 合理控制截图时机

在实现截图功能时，需注意组件的渲染过程非一次性完成。系统在构建与显示组件时，将经过测量、布局、提交指令等多个复杂步骤，最终在一次硬件刷新时呈现于屏幕上。因此，在特定情况下，若在组件刷新后立即调用截图，可能无法获取预期内容或出现截图失败报错。

为了确保截图结果准确，建议在组件完全渲染后再执行截图操作。

**了解组件的绘制状态**

为了确保截图内容符合预期，应该了解代码对界面状态的修改时机，并注意给系统预留处理时间，这通常可以通过增加一定延时来实现。

尽管可以通过inspector上的[ComponentObserver](../harmonyos-references/js-apis-arkui-inspector.md#componentobserver)感知应用组件绘制（draw）送显通知，但需要注意的是，ComponentObserver的组件绘制通知并不意味着系统已经真正将绘制指令执行，这取决于图形系统服务的负载情况。

**明确等待绘制完成**

影响截图预期的主要因素是截图时机与系统服务执行绘制指令的时间差。在发起截图调用时，应用侧之前提交的所有绘制指令可能尚未被图形服务真正执行。为此，可以通过指定[SnapshotOptions](../harmonyos-references/js-apis-arkui-componentsnapshot.md#snapshotoptions12)参数中的waitUntilRenderFinished为true，来确保系统在执行截图请求时等待所有之前的绘制指令均执行完毕，从而截取到更完整的内容。

说明

建议始终开启waitUntilRenderFinished参数。

**了解资源加载对截图的影响**

影响截图预期的另一个常见原因，是图片资源的加载。图片组件支持在线资源链接，也可指定本地资源，且绝大多数图片资源为PNG、JPEG等压缩格式。这些资源需要系统解码为可提交绘制的位图格式，此过程默认在异步IO线程上进行，因此可能由于该过程耗时的不确定性而导致截图不符合预期。

应用可通过以下几种方式进行优化：

1. 自行提前解析图片为PixelMap格式，将PixelMap配置给图片组件；建议优先以此方法进行优化。
2. 配置所使用的图片组件的syncLoad属性为true来强制同步加载，这样组件被构建时，即可确保资源可以直接被提交；
3. 通过指定延迟时长以及checkImageStatus设置为true，尝试截图，当返回160001错误后，重新加大时长进行截图；

### 及时保存和释放位图对象

为了及时释放资源，当截图接口返回的PixelMap对象不再使用时，应将其赋值为空。

### 合理控制采样精度

请不要截取过大尺寸的图片，截图不建议超过屏幕尺寸大小。当要截取的图片目标长宽超过底层限制时，截图会返回失败，不同设备的底层限制并不相同。可以通过控制SnapshotOptions中的scale参数，减小采样精度，这可以在很大程度上节省内存，并大幅度提高截图的效率。

### 使用其他能力对自渲染场景实现截图

尽管截图只需传入一个组件根节点即可实现对其下所有组件进行截图，但当子组件中存在[Video](../harmonyos-references/ts-media-components-video.md)、[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)或[Web](../harmonyos-references/arkts-basic-components-web.md)组件时，这并不是推荐的截图方式。建议直接使用[image.createPixelMapFromSurface](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmapfromsurface11)接口来实现。
