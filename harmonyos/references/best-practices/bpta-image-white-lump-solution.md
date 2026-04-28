---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image-white-lump-solution
title: Image白块解决方案
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 专项问题解决方案 > Image白块解决方案
category: best-practices
scraped_at: 2026-04-28T08:22:35+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:a8753a5ec96e632c0cbba06021de1a9b440a2ff66ff8e962b3ad35882566aea2
---

## 概述

在通过Image组件加载网络图片时，整个过程可分为四个关键阶段：组件创建、图片资源下载、图片解码和最终刷新显示。当加载的图片资源过大时，组件需等待下载与解码完成后才进行刷新。由于下载阶段耗时较长（尤其在网络波动或大文件场景下），图片在完全渲染前会显示为空白或浅色占位图，这种现象被称为“Image白块”。它不仅影响视觉体验，还可能降低用户对应用性能的感知。

为减少白块出现，开发者可采用预下载与缓存机制：

* 预下载阶段：在组件创建前（如父页面初始化时），将网络图片通过[应用沙箱](../harmonyos-references/js-apis-file-fs.md)的方式进行提前缓存。
* 缓存复用阶段：当Image组件加载时，首先检查应用沙箱是否存在缓存。若存在，则直接读取缓存数据；若不存在，再发起网络请求。非首次请求时，该机制可避免重复下载，从而缩短白块持续时间。

**图1** Image加载网络图片两种方式对比  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/S706tgT_R3CyANBKiNcgBA/zh-cn_image_0000002429762245.png?HW-CC-KV=V1&HW-CC-Date=20260428T002233Z&HW-CC-Expire=86400&HW-CC-Sign=D289B060B3F518CA06122E5D92626C87F7BE5CF9E4141CBD1D240B7B5520BB31 "点击放大")

说明

1. 开发者在使用Image加载较大的网络图片时，网络下载推荐使用[HTTP](../harmonyos-guides/http-request.md)工具提前预下载。

2. 在预下载之后，开发者可根据业务自行选择数据处理方式，如将预下载后得到的ArrayBuffer转成BASE64、使用应用沙箱提前缓存、直接转PixelMap、或是业务上自行处理ArrayBuffer等多种方式灵活处理数据后，传给Image组件。

当子页面需要加载很大的网络图片时，可以在父页面提前将网络数据预下载到应用沙箱中，子组件加载时从沙箱中读取，减少白块出现时长。

## 场景案例

开发者使用Navigation组件时，通常会在主页引入子页面组件，在按钮中添加方法实现跳转子页面组件。当子页面中需展示一张较大的网络图片时，而Image未设置占位图时，会出现点击按钮后，子组件的Image组件位置出现长时间的Image白块现象。

本文将以应用沙箱提前缓存举例，给出减少Image白块出现时长的一种优化方案。

### 【优化前】：使用Image组件直接加载网络地址

使用Image组件直接加载网络地址。

```
1. @Builder
2. export function PageOneBuilder() {
3. PageOne();
4. }

6. @Component
7. export struct PageOne {
8. pageInfo: NavPathStack = new NavPathStack();
9. @State name: string = 'pageOne';
10. @LocalStorageLink('imageData') imageData: PixelMap | undefined = undefined;

12. build() {
13. NavDestination() {
14. Row() {
15. // Positive example: At this time, the Image has obtained the network image that has been loaded in advance,
16. // reducing the time for white blocks to appear.
17. Image(this.imageData)
18. .objectFit(ImageFit.Auto)
19. .width('100%')
20. .height('100%')
21. }
22. .width('100%')
23. .height('100%')
24. .justifyContent(FlexAlign.Center)
25. }
26. .title(this.name)
27. }
28. }
```

[PageOne.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/PreHttpRequestUseFiles/entry/src/main/ets/pages/PageOne.ets#L16-L43)

说明

* 使用Image直接加载网络图片时，可以使用.alt()的方式，在网络图片加载成功前使用占位图，避免白块出现时长过长，优化用户体验。

* 使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

### 【优化后】：通过预下载的方式

子页面PageOne中需展示一张较大的网络图片，在父组件的aboutToAppear()中提前发起网络请求，并做判断文件是否存在，已下载的不再重复请求，存储在应用沙箱中。当父页面点击按钮跳转子页面PageOne，此时触发pixMap请求读取应用沙箱中已缓存解码的网络图片并存储在LocalStorage中，通过在子页面的Image中传入被@StorageLink修饰的变量imageData进行数据刷新，图片送显。

**图2** 使用预下载的方式，由开发者灵活地处理网络图片，减少白块出现时长  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/UIzcZ7m_RDKN-b-18tTsrg/zh-cn_image_0000002429764493.png?HW-CC-KV=V1&HW-CC-Date=20260428T002233Z&HW-CC-Expire=86400&HW-CC-Sign=F8317311341A9F1F621725FE250B6316995C54C3E0D77F37C0C24C89E410772F "点击放大")

1. 在父组件里aboutToAppear()中提前发起网络请求，当父页面点击按钮跳转子页面PageOne，此时触发pixMap请求读取应用沙箱中已缓存解码的网络图片并存储在localStorage中。非首次点击时，不再重复调用getPixMap()，避免每次点击都从沙箱里读取文件。

   ```
   1. import { fileIo as fs } from '@kit.CoreFileKit';
   2. import { image } from '@kit.ImageKit';
   3. import { common } from '@kit.AbilityKit';
   4. import { httpRequest } from '../utils/NetRequest';
   5. import Logger from '../utils/Logger';

   7. // Obtain the path of the application file
   8. const uiContext: UIContext | undefined = AppStorage.get('uiContext');
   9. let context: common.UIAbilityContext = uiContext?.getHostContext() as common.UIAbilityContext;
   10. let filesDir: string = context.filesDir;
   11. let fileUrl: string = filesDir + '/xxx.png'; // The image's network address suffix needs to be replaced by the real url.
   12. let para: Record<string, PixelMap | undefined> = { 'imageData': undefined };
   13. let localStorage: LocalStorage = new LocalStorage(para);
   14. const TAG: string = '[GetPixMapFunc]';

   16. @Entry(localStorage)
   17. @Component
   18. struct MainPage {
   19. @State childNavStack: NavPathStack = new NavPathStack();
   20. @LocalStorageLink('imageData') imageData: PixelMap | undefined = undefined;

   22. getPixMap() { // Read files from the application sandbox
   23. try {
   24. let file: fs.File = fs.openSync(fileUrl, fs.OpenMode.READ_WRITE); // Open the file in a synchronous manner
   25. const imageSource: image.ImageSource = image.createImageSource(file.fd);
   26. const options: image.InitializationOptions = {
   27. 'alphaType': 0, // transparency
   28. 'editable': false, // Editable or not
   29. 'pixelFormat': 3, // Pixel format
   30. 'scaleMode': 1, // Abbreviated value
   31. 'size': { height: 100, width: 100 }
   32. };
   33. fs.close(file)
   34. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
   35. this.imageData = pixelMap;
   36. });
   37. } catch (e) {
   38. Logger.error(TAG, 'Resource loading error, file or does not exist!');
   39. }
   40. }

   42. aboutToAppear(): void {
   43. httpRequest(); // Initiate a network request ahead of the parent component
   44. }

   46. build() {
   47. Navigation(this.childNavStack) {
   48. Column() {
   49. Button('push Path to pageOne', { stateEffect: true, type: ButtonType.Capsule })
   50. .width('80%')
   51. .height(40)
   52. .margin({ bottom: '36vp' })
   53. .onClick(() => {
   54. // Do not call getPixMap() repeatedly except for the first click to avoid reading files from the sandbox with each click.
   55. if (!localStorage.get('imageData')) {
   56. this.getPixMap();
   57. }
   58. this.childNavStack.pushPath({ name: 'pageOne' });
   59. })
   60. }
   61. .width('100%')
   62. .height('100%')
   63. .justifyContent(FlexAlign.End)
   64. }
   65. .backgroundColor(Color.Transparent)
   66. .title('ParentNavigation')
   67. }
   68. }
   ```

   [MainPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/PreHttpRequestUseFiles/entry/src/main/ets/pages/MainPage.ets#L16-L83)
2. 在NetRequest.ets中定义网络请求httpRequest()，通过fs.access()检查文件是否存在，当文件存在时不再重复请求，并写入沙箱中。

   ```
   1. import { http } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { fileIo as fs } from '@kit.CoreFileKit';
   4. import { common } from '@kit.AbilityKit';

   6. // Obtain the path of the application file
   7. const uiContext: UIContext | undefined = AppStorage.get('uiContext');
   8. let context: common.UIAbilityContext = uiContext?.getHostContext() as common.UIAbilityContext;
   9. let filesDir: string = context.filesDir;
   10. let fileUrl: string = filesDir + '/xxx.png'; // The image's network address suffix needs to be replaced by the real url.

   12. export async function httpRequest() {
   13. fs.access(fileUrl, fs.AccessModeType.READ).then((res) => { // Check whether files exist
   14. if (!res) { // If the address does not exist in the sandbox, re-request the network image resource
   15. http.createHttp()
   16. // Please fill in a specific network image address here, example: https://img.picui.cn/free/2024/09/09/66deb127cf1c0.png
   17. // If you fill in the real address, you need to replace the global fileUrl with the real address suffix.
   18. .request('https://example.com/xxx.png',
   19. (error: BusinessError, data: http.HttpResponse) => {
   20. if (error) {
   21. // If the download fails, no subsequent logic is executed
   22. return;
   23. }
   24. // Processing data returned by network requests
   25. if (http.ResponseCode.OK === data.responseCode) {
   26. const imageData: ArrayBuffer = data.result as ArrayBuffer;
   27. // Save the image to the app sandbox
   28. readWriteFileWithStream(imageData);
   29. }
   30. }
   31. )
   32. }
   33. })
   34. }

   36. // Write to the sandbox
   37. async function readWriteFileWithStream(imageData: ArrayBuffer): Promise<void> {
   38. let outputStream: fs.Stream = fs.createStreamSync(fileUrl, 'w+');
   39. await outputStream.write(imageData);
   40. outputStream.closeSync();
   41. }
   ```

   [NetRequest.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/PreHttpRequestUseFiles/entry/src/main/ets/utils/NetRequest.ets#L16-L56)
3. 在子组件中通过在子页面的Image中传入被@StorageLink修饰的变量imageData进行数据刷新，图片送显。

   ```
   1. @Builder
   2. export function PageOneBuilder() {
   3. PageOne();
   4. }

   6. @Component
   7. export struct PageOne {
   8. pageInfo: NavPathStack = new NavPathStack();
   9. @State name: string = 'pageOne';
   10. @LocalStorageLink('imageData') imageData: PixelMap | undefined = undefined;

   12. build() {
   13. NavDestination() {
   14. Row() {
   15. // Positive example: At this time, the Image has obtained the network image that has been loaded in advance,
   16. // reducing the time for white blocks to appear.
   17. Image(this.imageData)
   18. .objectFit(ImageFit.Auto)
   19. .width('100%')
   20. .height('100%')
   21. }
   22. .width('100%')
   23. .height('100%')
   24. .justifyContent(FlexAlign.Center)
   25. }
   26. .title(this.name)
   27. }
   28. }
   ```

   [PageOne.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/PreHttpRequestUseFiles/entry/src/main/ets/pages/PageOne.ets#L16-L43)

## 性能分析

下面使用trace对优化前后性能进行对比分析。开发者可以通过使用[DevEco Profiler](bpta-optimization-overview.md#section2012922312284)工具来抓捕trace图并识别分析应用中的性能问题。

【优化前】

分析阶段的起点为父页面点击按钮开始计时即trace的H:DispatchTouchEvent，结束点为子页面图片渲染的首帧出现即H:CreateImagePixelMap标签后的第一个Vsync，记录白块出现时间为1.3s，其中以H:HttpRequestInner的标签起始为起点到H:DownloadImageSuccess标签结束为终点记录时间，即为网络下载耗时1.2s，因此使用Image直接加载网络图片时，出现长时间Image白块，其原因是需要等待网络下载资源完成。

**图3** 直接使用Image加载网络数据  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/gTwBIu9zRSKuu-lman0e5w/zh-cn_image_0000002229337465.png?HW-CC-KV=V1&HW-CC-Date=20260428T002233Z&HW-CC-Expire=86400&HW-CC-Sign=829D0D8610FC30AFDFBA570C70BBDA616293BA35A7251763C402945651341E59 "点击放大")

【优化后】

分析阶段的起点为父页面点击按钮开始计时即trace的H:DispatchTouchEvent，结束点为子页面图片渲染的首帧出现即H:CreateImagePixelMap标签后的第一个Vsync，记录白块出现时间为32.6ms，其中记录H:HttpRequestInner的标签耗时即为提前网络下载的耗时1.16s，对比白块时长可知提前预下载可以减少白块出现时长。

**图4** 使用预下载的方式  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/m3cDVrbrTi-sPAMeSeHidg/zh-cn_image_0000002229451957.png?HW-CC-KV=V1&HW-CC-Date=20260428T002233Z&HW-CC-Expire=86400&HW-CC-Sign=C173B37220C936E54D4B5086DEDF793D40DFB28B4DD8F11D9067EE973028FD52 "点击放大")

说明

网络下载耗时实际受到网络波动影响，优化前后的网络下载耗时数据总体差异在1s内，提供的性能数值仅供参考。

## 效果对比

| （优化前）直接使用Image加载网络数据，未使用预下载 | （优化后）使用预下载 |
| --- | --- |
|  |  |

## 性能对比

对比数据如下：

| 方案 | 白块出现时长(毫秒) | 白块出现时长 |
| --- | --- | --- |
| （优化前）直接使用Image加载网络数据，未使用预下载 | 1300 | 图片位置白块出现时间较长 |
| （优化后）使用预下载 | 32.6 | 图片位置白块出现时间较短 |

说明

1.测试数据仅限于示例程序，不同设备特性和具体应用场景的多样性，所获得的性能数据存在差异，提供的数值仅供参考。

2.由于该方案仅将下载解码网络图片的步骤提前，不会影响内存等应用数据。开发者可自行管理解码后的PixelMap，主动实现图片的复用和缓存。

由此可见，加载网络图片时，使用预下载，提前处理网络请求并从应用沙箱中读取缓存数据的方式，可以减少用户可见Image白屏或白块出现时长，提升用户体验。

## 示例代码

* [Image白块解决指导](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/PreHttpRequestUseFiles)
