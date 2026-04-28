---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes
title: 属性
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > 属性
category: harmonyos-references
scraped_at: 2026-04-28T08:05:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:853a596def3e97087fea45bb19ede72a510f7bea451b1b36853df6cf54c60f4c
---

通用属性仅支持[aspectRatio](ts-universal-attributes-layout-constraints.md#aspectratio)、[backdropBlur](ts-universal-attributes-background.md#backdropblur)、[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、[bindContentCover](ts-universal-attributes-modal-transition.md#bindcontentcover)、[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)、[bindMenu](ts-universal-attributes-menu.md#bindmenu) 、[bindSheet](ts-universal-attributes-sheet-transition.md#bindsheet)、[borderColor](ts-universal-attributes-border.md#bordercolor)、[borderRadius](ts-universal-attributes-border.md#borderradius)、[borderStyle](ts-universal-attributes-border.md#borderstyle)、[borderWidth](ts-universal-attributes-border.md#borderwidth)、[clip](ts-universal-attributes-sharp-clipping.md#clip12)、[constraintSize](ts-universal-attributes-size.md#constraintsize)、[defaultFocus](ts-universal-attributes-focus.md#defaultfocus9)、[focusable](ts-universal-attributes-focus.md#focusable)、[tabIndex](ts-universal-attributes-focus.md#tabindex9)、[groupDefaultFocus](ts-universal-attributes-focus.md#groupdefaultfocus9)、[displayPriority](ts-universal-attributes-layout-constraints.md#displaypriority)、[enabled](ts-universal-attributes-enable.md#enabled)、[flexBasis](ts-universal-attributes-flex-layout.md#flexbasis)、[flexShrink](ts-universal-attributes-flex-layout.md#flexshrink)、[layoutWeight](ts-universal-attributes-size.md#layoutweight)、[id](ts-universal-attributes-component-id.md#id)、[gridOffset](ts-universal-attributes-grid.md#属性)、[gridSpan](ts-universal-attributes-grid.md#属性)、[useSizeType](ts-universal-attributes-grid.md#属性)、[height](ts-universal-attributes-size.md#height)、[touchable](ts-universal-attributes-click.md#touchabledeprecated)、[margin](ts-universal-attributes-size.md#margin)、[markAnchor](ts-universal-attributes-location.md#markanchor)、[offset](ts-universal-attributes-location.md#offset)、[width](ts-universal-attributes-size.md#width)、[zIndex](ts-universal-attributes-z-order.md#zindex)、[visibility](ts-universal-attributes-visibility.md#visibility)、[scale](ts-universal-attributes-transformation.md#scale)、[translate](ts-universal-attributes-transformation.md#translate)、[responseRegion](ts-universal-attributes-touch-target.md#responseregion)、[size](ts-universal-attributes-size.md#size)、[opacity](ts-universal-attributes-opacity.md#opacity)、[shadow](ts-universal-attributes-image-effect.md#shadow)、[sharedTransition](ts-transition-animation-shared-elements.md)、[transition](ts-transition-animation-component.md)、[position](ts-universal-attributes-location.md#position)、[direction](ts-universal-attributes-location.md#direction)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 示例效果请以真机运行为准。

## domStorageAccess

PhonePC/2in1TabletTVWearable

domStorageAccess(domStorageAccess: boolean)

设置是否开启文档对象模型存储接口（DOM Storage API）权限，当属性没有显式调用时，默认不开启文档对象模型存储接口（DOM Storage API）权限。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domStorageAccess | boolean | 是 | 设置是否开启文档对象模型存储接口（DOM Storage API）权限。  true表示开启文档对象模型存储接口权限，false表示不开启文档对象模型存储接口权限。  传入undefined或null时为false。 |

说明

* 网页中使用到文档对象模型存储接口（DOM Storage API），需将其设置为true，才可正常加载网页。

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .domStorageAccess(true)
13. }
14. }
15. }
```

## fileAccess

PhonePC/2in1TabletTVWearable

fileAccess(fileAccess: boolean)

设置是否开启应用中文件系统的访问。[$rawfile(filepath/filename)](../harmonyos-guides/resource-categories-and-access.md#资源访问)中的文件不受该属性影响而被限制访问。API version 11及以前，当属性没有显式调用时，默认开启应用中文件系统的访问。API version 12及以后，当属性没有显式调用时，默认不开启应用中文件系统的访问。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileAccess | boolean | 是 | 设置是否开启应用中文件系统的访问。  true表示开启应用中文件系统的访问。false表示不开启应用中文件系统的访问。  同时，当fileAccess为false的时候，仅只读资源目录/data/storage/el1/bundle/entry/resources/resfile里面的资源依然可以通过file协议访问，不受fileAccess管控。  API version 11及以前，传入undefined或null时为true，API version 12及以后传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .fileAccess(true)
13. }
14. }
15. }
```

## imageAccess

PhonePC/2in1TabletTVWearable

imageAccess(imageAccess: boolean)

设置是否允许自动加载图片资源。当属性没有显式调用时，允许自动加载图片资源。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageAccess | boolean | 是 | 设置是否允许自动加载图片资源。  true表示设置允许自动加载图片资源，false表示设置不允许自动加载图片资源。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .imageAccess(true)
13. }
14. }
15. }
```

## javaScriptProxy

PhonePC/2in1TabletTVWearable

javaScriptProxy(javaScriptProxy: JavaScriptProxy)

将javaScriptProxy中的ArkTS对象注册到Web组件中，该对象将使用JavaScriptProxy中指定的名称注册到网页的所有框架中，包括所有iframe，这使得JavaScript可以调用javaScriptProxy中ArkTS对象的方法。当属性没有显式调用时，默认不将javaScriptProxy中的ArkTS对象注册到Web组件中。

说明

javaScriptProxy接口需要和[deleteJavaScriptRegister9+](arkts-apis-webview-webviewcontroller.md#deletejavascriptregister)接口配合使用，防止内存泄漏。

javaScriptProxy对象的所有参数不支持更新。

注册javaScriptProxy对象时，同步与异步列表请至少选择一项不为空，可同时注册两类方法。

此接口只支持注册一个对象，若需要注册多个对象请使用[registerJavaScriptProxy9+](arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| javaScriptProxy | [JavaScriptProxy](arkts-basic-components-web-i.md#javascriptproxy12) | 是 | 参与注册的对象。只能声明方法，不能声明属性。  传入undefined或null时不将javaScriptProxy中的ArkTS对象注册到Web组件中。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestObj {
6. constructor() {
7. }

9. test(data1: string, data2: string, data3: string): string {
10. console.info("data1:" + data1);
11. console.info("data2:" + data2);
12. console.info("data3:" + data3);
13. return "AceString";
14. }

16. asyncTest(data: string): void {
17. console.info("async data:" + data);
18. }

20. toString(): void {
21. console.info('toString' + "interface instead.");
22. }
23. }

25. @Entry
26. @Component
27. struct WebComponent {
28. controller: webview.WebviewController = new webview.WebviewController();
29. testObj = new TestObj();
30. build() {
31. Column() {
32. Button('deleteJavaScriptRegister')
33. .onClick(() => {
34. try {
35. this.controller.deleteJavaScriptRegister("objName");
36. } catch (error) {
37. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
38. }
39. })
40. Web({ src: 'www.example.com', controller: this.controller })
41. .javaScriptAccess(true)
42. .javaScriptProxy({
43. object: this.testObj,
44. name: "objName",
45. methodList: ["test", "toString"],
46. asyncMethodList: ["asyncTest"],
47. controller: this.controller,
48. })
49. }
50. }
51. }
```

## javaScriptAccess

PhonePC/2in1TabletTVWearable

javaScriptAccess(javaScriptAccess: boolean)

设置是否允许执行JavaScript脚本。当属性没有显式调用时，默认允许执行JavaScript脚本。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| javaScriptAccess | boolean | 是 | 是否允许执行JavaScript脚本。  true表示允许执行JavaScript脚本，false表示不允许执行JavaScript脚本。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .javaScriptAccess(true)
12. }
13. }
14. }
```

## overScrollMode11+

PhonePC/2in1TabletTVWearable

overScrollMode(mode: OverScrollMode)

设置Web过滚动模式。当过滚动模式开启时，当用户在Web根页面上滑动到边缘时，Web会通过弹性动画弹回界面，根页面上的内部页面不会触发回弹。该属性没有显式调用时，默认关闭过滚动模式。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [OverScrollMode](arkts-basic-components-web-e.md#overscrollmode11) | 是 | 设置Web的过滚动模式为关闭或开启。  传入undefined或null时为OverScrollMode.NEVER。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State mode: OverScrollMode = OverScrollMode.ALWAYS;
9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .overScrollMode(this.mode)
13. }
14. }
15. }
```

## mixedMode

PhonePC/2in1TabletTVWearable

mixedMode(mixedMode: MixedMode)

设定当安全源尝试从非安全源加载资源时的行为。当属性没有显式调用时，默认值为MixedMode.None，即禁止安全源从非安全源加载内容。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mixedMode | [MixedMode](arkts-basic-components-web-e.md#mixedmode) | 是 | 要设置的混合内容模式。  传入undefined或null时为MixedMode.All。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State mode: MixedMode = MixedMode.All;
9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .mixedMode(this.mode)
13. }
14. }
15. }
```

## onlineImageAccess

PhonePC/2in1TabletTVWearable

onlineImageAccess(onlineImageAccess: boolean)

设置是否允许从网络加载图片资源（通过HTTP和HTTPS访问的资源）。当属性没有显式调用时，默认允许从网络加载图片资源。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onlineImageAccess | boolean | 是 | 设置是否允许从网络加载图片资源。  true表示设置允许从网络加载图片资源，false表示设置不允许从网络加载图片资源。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onlineImageAccess(true)
13. }
14. }
15. }
```

## zoomAccess

PhonePC/2in1TabletTVWearable

zoomAccess(zoomAccess: boolean)

设置是否支持手势进行缩放。该属性没有显式调用时，默认支持手势进行缩放。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zoomAccess | boolean | 是 | 设置是否支持手势进行缩放。  true表示设置支持手势进行缩放，false表示设置不支持手势进行缩放。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .zoomAccess(true)
13. }
14. }
15. }
```

## overviewModeAccess

PhonePC/2in1TabletTVWearable

overviewModeAccess(overviewModeAccess: boolean)

设置是否使用概览模式加载网页，即缩小内容以适应屏幕宽度。当属性没有显式调用时，默认允许使用概览模式加载网页。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在PC/2in1设备中无效果，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| overviewModeAccess | boolean | 是 | 设置是否使用概览模式加载网页。  true表示设置使用概览模式加载网页，false表示设置不使用概览模式加载网页。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .overviewModeAccess(true)
13. }
14. }
15. }
```

## databaseAccess

PhonePC/2in1TabletTVWearable

databaseAccess(databaseAccess: boolean)

设置Web SQL数据库存储API权限，若未显式调用，此权限默认关闭。

说明

* 本接口在ArkWeb内核升级到M132版本后因内核废弃Web SQL，对Web SQL数据库的控制失效。ArkWeb内核版本参考ArkWeb简介[约束与限制](../harmonyos-guides/web-component-overview.md#约束与限制)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| databaseAccess | boolean | 是 | 设置是否开启Web SQL数据库存储API权限。  true表示开启，false表示关闭。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .databaseAccess(true)
13. }
14. }
15. }
```

## geolocationAccess

PhonePC/2in1TabletTVWearable

geolocationAccess(geolocationAccess: boolean)

设置是否开启获取地理位置权限。当属性没有显式调用时，默认开启获取地理位置权限。具体使用方式参考[管理位置权限](../harmonyos-guides/web-geolocation-permission.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| geolocationAccess | boolean | 是 | 设置是否开启获取地理位置权限。  true表示设置开启获取地理位置权限，false表示设置不开启获取地理位置权限。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .geolocationAccess(true)
13. }
14. }
15. }
```

## mediaPlayGestureAccess9+

PhonePC/2in1TabletTVWearable

mediaPlayGestureAccess(access: boolean)

设置有声视频的自动播放是否需要用户手动点击，静音视频播放不受该接口管控。当该属性未显式设置时，默认有声视频的自动播放需要用户手动点击。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access | boolean | 是 | 设置有声视频的自动播放是否需要用户手动点击。  true表示设置有声视频的自动播放需要用户手动点击，false表示设置有声视频的自动播放不需要用户手动点击，能自动播放。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State access: boolean = true;

10. build() {
11. Column() {
12. Web({ src: $rawfile('index.html'), controller: this.controller })
13. .mediaPlayGestureAccess(this.access)
14. }
15. }
16. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>视频播放页面</title>
6. </head>
7. <body>
8. <h1>视频播放</h1>
9. <video id="testVideo" controls autoplay>
10. // 需要在video标签中配置autoplay属性，允许视频自动播放
11. // 在resources的rawfile目录放置任意一个mp4媒体文件，并将其命名为example.mp4
12. <source src="example.mp4" type="video/mp4">
13. </video>
14. </body>
15. </html>
```

## multiWindowAccess9+

PhonePC/2in1TabletTVWearable

multiWindowAccess(multiWindow: boolean)

设置是否开启多窗口权限。

使能多窗口权限时，需要实现onWindowNew事件，示例代码参考[onWindowNew事件](arkts-basic-components-web-events.md#onwindownew9)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| multiWindow | boolean | 是 | 设置是否开启多窗口权限。  true表示设置开启多窗口权限，false表示设置不开启多窗口权限。  默认值：false。 |

## horizontalScrollBarAccess9+

PhonePC/2in1TabletTVWearable

horizontalScrollBarAccess(horizontalScrollBar: boolean)

设置是否显示横向滚动条，包括系统默认滚动条和用户自定义滚动条。该属性没有显式调用时，默认显示横向滚动条。

说明

* 通过@State变量控制横向滚动条的隐藏/显示后，需要调用[controller.refresh()](arkts-apis-webview-webviewcontroller.md#refresh)生效。
* 通过@State变量频繁动态改变时，建议切换开关变量和Web组件一一对应。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| horizontalScrollBar | boolean | 是 | 设置是否显示横向滚动条。  true表示设置显示横向滚动条，false表示设置不显示横向滚动条。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State isShow: boolean = true;
10. @State btnMsg: string ="隐藏滚动条";

12. build() {
13. Column() {
14. // 通过@State变量改变横向滚动条的隐藏/显示后，需调用this.controller.refresh()后生效
15. Button('refresh')
16. .onClick(() => {
17. if(this.isShow){
18. this.isShow = false;
19. this.btnMsg="显示滚动条";
20. }else{
21. this.isShow = true;
22. this.btnMsg="隐藏滚动条";
23. }
24. try {
25. this.controller.refresh();
26. } catch (error) {
27. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
28. }
29. }).height("10%").width("40%")
30. Web({ src: $rawfile('index.html'), controller: this.controller }).height("90%")
31. .horizontalScrollBarAccess(this.isShow)
32. }
33. }
34. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1.0">
6. <title>Demo</title>
7. <style>
8. body {
9. width:3000px;
10. height:6000px;
11. padding-right:170px;
12. padding-left:170px;
13. border:5px solid blueviolet;
14. }
15. </style>
16. </head>
17. <body>
18. Scroll Test
19. </body>
20. </html>
```

## verticalScrollBarAccess9+

PhonePC/2in1TabletTVWearable

verticalScrollBarAccess(verticalScrollBar: boolean)

设置是否显示纵向滚动条，包括系统默认滚动条和用户自定义滚动条。该属性没有显式调用时，默认显示纵向滚动条。

说明

* 通过@State变量控制纵向滚动条的隐藏/显示后，需要调用controller.refresh()生效。
* 通过@State变量频繁动态改变时，建议切换开关变量和Web组件一一对应。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| verticalScrollBar | boolean | 是 | 设置是否显示纵向滚动条。  true表示设置显示纵向滚动条，false表示设置不显示纵向滚动条。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State isShow: boolean = true;
10. @State btnMsg: string ="隐藏滚动条";

12. build() {
13. Column() {
14. // 通过@State变量改变纵向滚动条的隐藏/显示后，需调用this.controller.refresh()后生效
15. Button(this.btnMsg)
16. .onClick(() => {
17. if(this.isShow){
18. this.isShow = false;
19. this.btnMsg="显示滚动条";
20. }else{
21. this.isShow = true;
22. this.btnMsg="隐藏滚动条";
23. }
24. try {
25. this.controller.refresh();
26. } catch (error) {
27. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
28. }
29. }).height("10%").width("40%")
30. Web({ src: $rawfile('index.html'), controller: this.controller }).height("90%")
31. .verticalScrollBarAccess(this.isShow)
32. }
33. }
34. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1.0">
6. <title>Demo</title>
7. <style>
8. body {
9. width:3000px;
10. height:6000px;
11. padding-right:170px;
12. padding-left:170px;
13. border:5px solid blueviolet;
14. }
15. </style>
16. </head>
17. <body>
18. Scroll Test
19. </body>
20. </html>
```

## cacheMode

PhonePC/2in1TabletTVWearable

cacheMode(cacheMode: CacheMode)

设置缓存模式。当属性没有显式调用时，默认为CacheMode.Default。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cacheMode | [CacheMode](arkts-basic-components-web-e.md#cachemode) | 是 | 要设置的缓存模式。  传入undefined或null时为CacheMode.Default。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State mode: CacheMode = CacheMode.None;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .cacheMode(this.mode)
14. }
15. }
16. }
```

## copyOptions11+

PhonePC/2in1TabletTVWearable

copyOptions(value: CopyOptions)

设置剪贴板复制范围选项。该属性没有显式调用时，默认支持复制后在当前设备内所有应用内粘贴。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CopyOptions](ts-appendix-enums.md#copyoptions9) | 是 | 要设置的剪贴板复制范围选项。  传入undefined或null时为CopyOptions.None。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .copyOptions(CopyOptions.None)
13. }
14. }
15. }
```

## textZoomRatio9+

PhonePC/2in1TabletTVWearable

textZoomRatio(textZoomRatio: number)

设置页面的文本缩放百分比。当属性没有显式调用时，默认缩放百分比为100%。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textZoomRatio | number | 是 | 要设置的页面的文本缩放百分比。  取值为整数，范围为(0, 2147483647]。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State ratio: number = 150;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .textZoomRatio(this.ratio)
14. }
15. }
16. }
```

## initialScale9+

PhonePC/2in1TabletTVWearable

initialScale(percent: number)

设置整体页面的缩放百分比。该属性没有显式调用时，默认缩放百分比为100。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| percent | number | 是 | 要设置的整体页面的缩放百分比。  取值范围：(0, 1000]。  传入undefined或null时属性设置不生效。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State percent: number = 100;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .initialScale(this.percent)
14. }
15. }
16. }
```

## blockNetwork9+

PhonePC/2in1TabletTVWearable

blockNetwork(block: boolean)

设置Web组件是否阻止从网络加载资源。当属性没有显式调用时，默认允许从网络加载资源。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| block | boolean | 是 | 设置Web组件是否允许从网络加载资源。  true表示不允许从网络加载资源，false表示允许从网络加载资源。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State block: boolean = true;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .blockNetwork(this.block)
14. }
15. }
16. }
```

## defaultFixedFontSize9+

PhonePC/2in1TabletTVWearable

defaultFixedFontSize(size: number)

设置网页的默认等宽字体大小。对于html前端使用monospace字体且未指定font-size样式的元素，将按此值渲染字体大小。

当属性没有显式调用时，默认等宽字体大小为13。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 设置网页的默认等宽字体大小，单位px。  输入值的范围为[-2^31, 2^31-1]，实际渲染时超过72px的值按照72px进行渲染，低于1px的值按照1px进行渲染。  传入null或undefined时为13。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State fontSize: number = 16;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .defaultFixedFontSize(this.fontSize)
14. }
15. }
16. }
```

## defaultFontSize9+

PhonePC/2in1TabletTVWearable

defaultFontSize(size: number)

设置网页的默认字体大小。对于html前端使用非monospace字体且未指定font-size样式的元素，将按此值渲染字体大小。

当属性没有显式调用时，网页的默认字体大小为16。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 设置网页的默认字体大小，单位px。  输入值的范围为[-2^31, 2^31-1]，实际渲染时超过72px的值按照72px进行渲染，低于1px的值按照1px进行渲染。  传入null或undefined时为16。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State fontSize: number = 13;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .defaultFontSize(this.fontSize)
14. }
15. }
16. }
```

## minFontSize9+

PhonePC/2in1TabletTVWearable

minFontSize(size: number)

设置网页字体大小最小值。对于html前端元素，若元素字体大小低于该接口设置值，将采用接口设置值渲染字体大小。

当属性没有显式调用时，默认网页字体大小最小值为8。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 设置网页字体大小最小值，单位px。  输入值的范围为[-2^31, 2^31-1]，实际渲染时超过72px的值按照72px进行渲染，低于1px的值按照1px进行渲染。  传入null或undefined时为8。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State fontSize: number = 13;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .minFontSize(this.fontSize)
14. }
15. }
16. }
```

## minLogicalFontSize9+

PhonePC/2in1TabletTVWearable

minLogicalFontSize(size: number)

设置网页逻辑字体大小最小值。

对于html前端未指定font-size样式的元素：

1. 若元素字体大小低于该接口设置值，将采用接口设置值渲染字体大小。
2. 若minLogicalFontSize和minFontSize同时设置时，对于未指定font-size样式元素，将采用两者中的较大值。

当属性没有显式调用时，默认网页逻辑字体大小最小值为8。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 设置网页逻辑字体大小最小值，单位px。  输入值的范围为[-2^31, 2^31-1]，实际渲染时超过72px的值按照72px进行渲染，低于1px的值按照1px进行渲染。  传入null或undefined时为18。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State fontSize: number = 13;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .minLogicalFontSize(this.fontSize)
14. }
15. }
16. }
```

## webFixedFont9+

PhonePC/2in1TabletTVWearable

webFixedFont(family: string)

设置网页的fixed font字体库，用于渲染html前端使用monospace字体的元素。

当属性没有显式调用时，默认网页的fixed font字体库为monospace。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string | 是 | 设置网页的fixed font字体库。  传入null或undefined时为monospace。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State family: string = "monospace";

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .webFixedFont(this.family)
14. }
15. }
16. }
```

## webSansSerifFont9+

PhonePC/2in1TabletTVWearable

webSansSerifFont(family: string)

设置网页的sans-serif font字体库，用于渲染html前端使用sans-serif字体的元素。

当属性没有显式调用时，默认网页的sans-serif font字体库为sans-serif。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string | 是 | 设置网页的sans-serif font字体库。  传入null或undefined时为sans-serif。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State family: string = "sans-serif";

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .webSansSerifFont(this.family)
14. }
15. }
16. }
```

## webSerifFont9+

PhonePC/2in1TabletTVWearable

webSerifFont(family: string)

设置网页的serif font字体库，用于渲染html前端使用serif字体的元素。

当属性没有显式调用时，默认网页的serif font字体库为serif。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string | 是 | 设置网页的serif font字体库。  传入null或undefined时为serif。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State family: string = "serif";

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .webSerifFont(this.family)
14. }
15. }
16. }
```

## webStandardFont9+

PhonePC/2in1TabletTVWearable

webStandardFont(family: string)

设置网页的standard font字体库，用于渲染html前端未指定字体样式的元素。

当属性没有显式调用时，默认网页的standard font字体库为sans-serif。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string | 是 | 设置网页的standard font字体库。  传入null或undefined时为sans-serif。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State family: string = "sans-serif";

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .webStandardFont(this.family)
14. }
15. }
16. }
```

## webFantasyFont9+

PhonePC/2in1TabletTVWearable

webFantasyFont(family: string)

设置网页的fantasy font字体库，用于渲染html前端使用fantasy字体的元素。

当属性没有显式调用时，默认网页的fantasy font字体库为fantasy。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string | 是 | 设置网页的fantasy font字体库。  传入null或undefined时为fantasy。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();
7. @State family: string = "fantasy";

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .webFantasyFont(this.family)
13. }
14. }
15. }
```

## webCursiveFont9+

PhonePC/2in1TabletTVWearable

webCursiveFont(family: string)

设置网页的cursive font字体库，用于渲染html前端使用cursive字体的元素。

当属性没有显式调用时，默认网页的cursive font字体库为cursive。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string | 是 | 设置网页的cursive font字体库。  传入null或undefined时为cursive。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State family: string = "cursive";

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .webCursiveFont(this.family)
14. }
15. }
16. }
```

## darkMode9+

PhonePC/2in1TabletTVWearable

darkMode(mode: WebDarkMode)

设置Web深色模式。当属性没有显式调用时，默认Web深色模式关闭。

当深色模式开启时，Web将启用媒体查询prefers-color-scheme中网页所定义的深色样式，若网页未定义深色样式，则保持原状。如需开启强制深色模式，建议配合[forceDarkAccess](arkts-basic-components-web-attributes.md#forcedarkaccess9)使用。深色模式具体用法可参考[Web深色模式适配](../harmonyos-guides/web-set-dark-mode.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebDarkMode](arkts-basic-components-web-e.md#webdarkmode9) | 是 | 设置Web的深色模式为关闭、开启或跟随系统。  传入null或undefined时为WebDarkMode.Off。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State mode: WebDarkMode = WebDarkMode.On;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .darkMode(this.mode)
14. }
15. }
16. }
```

## forceDarkAccess9+

PhonePC/2in1TabletTVWearable

forceDarkAccess(access: boolean)

设置网页是否开启强制深色模式。该属性仅在[darkMode](arkts-basic-components-web-attributes.md#darkmode9)开启深色模式时生效。当属性没有显式调用时，默认网页不开启强制深色模式。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access | boolean | 是 | 设置网页是否开启强制深色模式。  true表示设置网页开启强制深色模式，false表示设置网页不开启强制深色模式。  传入null或undefined时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State mode: WebDarkMode = WebDarkMode.On;
9. @State access: boolean = true;

11. build() {
12. Column() {
13. Web({ src: 'www.example.com', controller: this.controller })
14. .darkMode(this.mode)
15. .forceDarkAccess(this.access)
16. }
17. }
18. }
```

## pinchSmooth9+

PhonePC/2in1TabletTVWearable

pinchSmooth(isEnabled: boolean)

设置网页是否开启捏合流畅模式。该属性没有显式调用时，默认不开启捏合流畅模式。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 网页是否开启捏合流畅模式。  true表示设置网页开启捏合流畅模式，false表示设置网页不开启捏合流畅模式。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .pinchSmooth(true)
13. }
14. }
15. }
```

## allowWindowOpenMethod10+

PhonePC/2in1TabletTVWearable

allowWindowOpenMethod(flag: boolean)

设置网页是否可以通过JavaScript自动打开新窗口。

说明

* 该属性仅在[javaScriptAccess](arkts-basic-components-web-attributes.md#javascriptaccess)开启时生效。
* 该属性在[multiWindowAccess](arkts-basic-components-web-attributes.md#multiwindowaccess9)开启时打开新窗口，关闭时打开本地窗口。
* 该属性的默认值与系统属性persist.web.allowWindowOpenMethod.enabled保持一致，如果未设置系统属性则默认值为false。
* 通过hdc shell param get persist.web.allowWindowOpenMethod.enabled 检查是否开启系统属性persist.web.allowWindowOpenMethod.enabled。若属性值为1代表开启系统属性；若属性值为0或不存在，代表未开启系统属性，可通过命令hdc shell param set persist.web.allowWindowOpenMethod.enabled 1 开启系统属性。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | boolean | 是 | true表示网页可以通过JavaScript自动打开新窗口，该属性为false时，用户行为仍可通过JavaScript自动打开新窗口，但非用户行为不能通过JavaScript自动打开新窗口。  此处的用户行为是指，在用户对Web组件进行点击等操作后，同时在5秒内请求打开新窗口（window.open）的行为。  默认值与系统属性关联，当系统属性persist.web.allowWindowOpenMethod.enabled为true时，默认值为true，如果未设置系统属性则默认值为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. // 在同一界面有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
5. @CustomDialog
6. struct NewWebViewComp {
7. controller?: CustomDialogController;
8. webviewController1: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: "", controller: this.webviewController1 })
13. .javaScriptAccess(true)
14. .multiWindowAccess(false)
15. .onWindowExit(() => {
16. console.info("NewWebViewComp onWindowExit");
17. if (this.controller) {
18. this.controller.close();
19. }
20. })
21. .onActivateContent(() => {
22. // 该Web需要展示到前台，建议应用在这里进行tab或window切换的动作
23. console.info("NewWebViewComp onActivateContent")
24. })
25. }
26. }
27. }

29. @Entry
30. @Component
31. struct WebComponent {
32. controller: webview.WebviewController = new webview.WebviewController();
33. dialogController: CustomDialogController | null = null;

35. build() {
36. Column() {
37. Web({ src: $rawfile("index.html"), controller: this.controller })
38. .javaScriptAccess(true)
39. // 需要使能multiWindowAccess
40. .multiWindowAccess(true)
41. .allowWindowOpenMethod(true)
42. .onWindowNew((event) => {
43. if (this.dialogController) {
44. this.dialogController.close()
45. }
46. let popController: webview.WebviewController = new webview.WebviewController();
47. this.dialogController = new CustomDialogController({
48. builder: NewWebViewComp({ webviewController1: popController }),
49. // isModal设置为false，防止新窗口被销毁而无法触发onActivateContent回调
50. isModal: false
51. })
52. this.dialogController.open();
53. // 将新窗口对应WebviewController返回给Web内核。
54. // 若不调用event.handler.setWebController接口，会造成render进程阻塞。
55. // 如果没有创建新窗口，调用event.handler.setWebController接口时设置成null，通知Web没有创建新窗口。
56. event.handler.setWebController(popController);
57. })
58. }
59. }
60. }
```

**HTML示例：**

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <div>
6. <button type="button" onclick="delayOpenwindow(5000)">delayOpenwindow_5s</button>
7. </div>

9. <script>
10. function openwindowAll(){
11. open("https://www.example.com","_blank","height=400,width=600,top=100,left=100,scrollbars=no")
12. }
13. function delayOpenwindow(t){
14. setTimeout(openwindowAll, t);
15. }
16. </script>
17. </body>
18. </html>
```

## mediaOptions10+

PhonePC/2in1TabletTVWearable

mediaOptions(options: WebMediaOptions)

设置Web媒体播放的策略，其中包括：Web中的音频在重新获焦后能够自动续播的有效期、应用内多个Web实例的音频是否独占。当该属性未显式设置时，默认Web中的音频重新获焦后无法自动续播、应用内多个Web实例的音频是独占的。

说明

* 同一Web实例中的多个音频均视为同一音频。
* 该媒体播放策略将同时管控有声视频。
* 建议为所有Web组件设置相同的[audioExclusive](arkts-basic-components-web-i.md#webmediaoptions10)值。
* 音视频互相打断在应用内和应用间生效，续播只在应用间生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [WebMediaOptions](arkts-basic-components-web-i.md#webmediaoptions10) | 是 | 设置Web的媒体策略。  属性参数更新后需重新播放音频方可生效。  传入undefined或null时为{resumeInterval: 0, audioExclusive: true} |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State options: WebMediaOptions = {resumeInterval: 10, audioExclusive: true};

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .mediaOptions(this.options)
14. }
15. }
16. }
```

## javaScriptOnDocumentStart11+

PhonePC/2in1TabletTVWearable

javaScriptOnDocumentStart(scripts: Array<ScriptItem>)

将JavaScript脚本注入到Web组件中，当指定页面或者文档开始加载时，该脚本将在其来源与scriptRules匹配的任何页面中执行。当属性没有显式调用时，默认不将JavaScript脚本注入到Web组件中。

说明

* 网页文档根元素（HTML Element）创建后、但尚未加载任何其他内容之前注入脚本。
* 该脚本按照字典序执行，非数组本身顺序，若需数组本身顺序，建议使用[runJavaScriptOnDocumentStart](arkts-basic-components-web-attributes.md#runjavascriptondocumentstart15)接口。
* 不建议与[runJavaScriptOnDocumentStart](arkts-basic-components-web-attributes.md#runjavascriptondocumentstart15)同时使用。
* 内容相同的脚本多次注入时将被静默去重，不展示，不提醒，使用首次注入时的scriptRules。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scripts | Array<[ScriptItem](arkts-basic-components-web-i.md#scriptitem11)> | 是 | 需要注入的ScriptItem数组。  传入undefined或null时不将JavaScript脚本注入到Web组件中。 |

**ets示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();
8. private localStorage: string =
9. "if (typeof(Storage) !== 'undefined') {" +
10. "   localStorage.setItem('color', 'Red');" +
11. "}";
12. @State scripts: Array<ScriptItem> = [
13. { script: this.localStorage, scriptRules: ["*"] }
14. ];

16. build() {
17. Column({ space: 20 }) {
18. Web({ src: $rawfile('index.html'), controller: this.controller })
19. .javaScriptAccess(true)
20. .domStorageAccess(true)
21. .backgroundColor(Color.Grey)
22. .javaScriptOnDocumentStart(this.scripts)
23. .width('100%')
24. .height('100%')
25. }
26. }
27. }
```

**HTML示例：**

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8">
6. </head>
7. <body style="font-size: 30px;" onload='bodyOnLoadLocalStorage()'>
8. Hello world!
9. <div id="result"></div>
10. </body>
11. <script type="text/javascript">
12. function bodyOnLoadLocalStorage() {
13. if (typeof(Storage) !== 'undefined') {
14. document.getElementById('result').innerHTML = localStorage.getItem('color');
15. } else {
16. document.getElementById('result').innerHTML = 'Your browser does not support localStorage.';
17. }
18. }
19. </script>
20. </html>
```

## javaScriptOnDocumentEnd11+

PhonePC/2in1TabletTVWearable

javaScriptOnDocumentEnd(scripts: Array<ScriptItem>)

将JavaScript脚本注入到Web组件中，当指定页面或者文档加载完成时，该脚本将在其来源与scriptRules匹配的任何页面中执行。当属性没有显式调用时，默认不将JavaScript脚本注入到Web组件中。

说明

* 该脚本将在页面的任何JavaScript代码之后运行，并且DOM树此时已经加载、渲染完毕。
* 该脚本按照字典序执行，非数组本身顺序。
* 不建议与[runJavaScriptOnDocumentEnd](arkts-basic-components-web-attributes.md#runjavascriptondocumentend15)同时使用。
* 内容相同的脚本多次注入时将被静默去重，不展示，不提醒，使用首次注入时的scriptRules。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scripts | Array<[ScriptItem](arkts-basic-components-web-i.md#scriptitem11)> | 是 | 需要注入的ScriptItem数组。  传入undefined或null时不将JavaScript脚本注入到Web组件中。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();
8. private jsStr: string =
9. "window.document.getElementById(\"result\").innerHTML = 'this is msg from javaScriptOnDocumentEnd'";
10. @State scripts: Array<ScriptItem> = [
11. { script: this.jsStr, scriptRules: ["*"] }
12. ];

14. build() {
15. Column({ space: 20 }) {
16. Web({ src: $rawfile('index.html'), controller: this.controller })
17. .javaScriptAccess(true)
18. .domStorageAccess(true)
19. .backgroundColor(Color.Grey)
20. .javaScriptOnDocumentEnd(this.scripts)
21. .width('100%')
22. .height('100%')
23. }
24. }
25. }
```

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8">
6. </head>
7. <body style="font-size: 30px;">
8. Hello world!
9. <div id="result">test msg</div>
10. </body>
11. </html>
```

## runJavaScriptOnDocumentStart15+

PhonePC/2in1TabletTVWearable

runJavaScriptOnDocumentStart(scripts: Array<ScriptItem>)

将JavaScript脚本注入到Web组件中，当指定页面或者文档开始加载时，该脚本将在其来源与scriptRules匹配的任何页面中执行。当属性没有显式调用时，默认不将JavaScript脚本注入到Web组件中。

说明

* 网页文档根元素（HTML Element）创建后、但尚未加载任何其他内容之前注入脚本。
* 该脚本按照数组本身顺序执行。
* 不建议与[javaScriptOnDocumentStart](arkts-basic-components-web-attributes.md#javascriptondocumentstart11)同时使用。
* 内容相同的脚本多次注入时将被静默去重，不展示，不提醒，使用首次注入时的scriptRules。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scripts | Array<[ScriptItem](arkts-basic-components-web-i.md#scriptitem11)> | 是 | 需要注入的ScriptItem数组。  传入undefined或null时不将JavaScript脚本注入到Web组件中。 |

**ets示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();
8. private localStorage: string =
9. "if (typeof(Storage) !== 'undefined') {" +
10. "   localStorage.setItem('color', 'Red');" +
11. "}";
12. private localStorage2: string =
13. "console.info('runJavaScriptOnDocumentStart urlRegexRules Matching succeeded.')";
14. @State scripts: Array<ScriptItem> = [
15. { script: this.localStorage, scriptRules: ["*"] },
16. { script: this.localStorage2, scriptRules: [], urlRegexRules: [{secondLevelDomain: "", rule: ".*index.html"}] }
17. ];

19. build() {
20. Column({ space: 20 }) {
21. Web({ src: $rawfile('index.html'), controller: this.controller })
22. .javaScriptAccess(true)
23. .domStorageAccess(true)
24. .backgroundColor(Color.Grey)
25. .runJavaScriptOnDocumentStart(this.scripts)
26. .width('100%')
27. .height('100%')
28. }
29. }
30. }
```

**HTML示例：**

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8">
6. </head>
7. <body style="font-size: 30px;" onload='bodyOnLoadLocalStorage()'>
8. Hello world!
9. <div id="result"></div>
10. </body>
11. <script type="text/javascript">
12. function bodyOnLoadLocalStorage() {
13. if (typeof(Storage) !== 'undefined') {
14. document.getElementById('result').innerHTML = localStorage.getItem('color');
15. } else {
16. document.getElementById('result').innerHTML = 'Your browser does not support localStorage.';
17. }
18. }
19. </script>
20. </html>
```

## runJavaScriptOnDocumentEnd15+

PhonePC/2in1TabletTVWearable

runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem>)

将JavaScript脚本注入到Web组件中，当指定页面或者文档加载完成时，该脚本将在其来源与scriptRules匹配的任何页面中执行。当属性没有显式调用时，默认不将JavaScript脚本注入到Web组件中。

说明

* 该脚本将在页面的任何JavaScript代码之后运行，并且DOM树此时已经加载、渲染完毕。
* 该脚本按照数组本身顺序执行。
* 不建议与[javaScriptOnDocumentEnd](arkts-basic-components-web-attributes.md#javascriptondocumentend11)同时使用。
* 内容相同的脚本多次注入时将被静默去重，不展示，不提醒，使用首次注入时的scriptRules。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scripts | Array<[ScriptItem](arkts-basic-components-web-i.md#scriptitem11)> | 是 | 需要注入的ScriptItem数组。  传入undefined或null时不将JavaScript脚本注入到Web组件中。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();
8. private jsStr: string =
9. "window.document.getElementById(\"result\").innerHTML = 'this is msg from runJavaScriptOnDocumentEnd'";
10. private jsStr2: string = "console.info('runJavaScriptOnDocumentEnd urlRegexRules Matching succeeded.')";
11. @State scripts: Array<ScriptItem> = [
12. { script: this.jsStr, scriptRules: ["*"] },
13. { script: this.jsStr2, scriptRules: [], urlRegexRules: [{secondLevelDomain: "", rule: ".*index.html"}] }
14. ];

16. build() {
17. Column({ space: 20 }) {
18. Web({ src: $rawfile('index.html'), controller: this.controller })
19. .javaScriptAccess(true)
20. .domStorageAccess(true)
21. .backgroundColor(Color.Grey)
22. .runJavaScriptOnDocumentEnd(this.scripts)
23. .width('100%')
24. .height('100%')
25. }
26. }
27. }
```

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8">
6. </head>
7. <body style="font-size: 30px;">
8. Hello world!
9. <div id="result">test msg</div>
10. </body>
11. </html>
```

## runJavaScriptOnHeadEnd15+

PhonePC/2in1TabletTVWearable

runJavaScriptOnHeadEnd(scripts: Array<ScriptItem>)

将JavaScript脚本注入到Web组件中，当页面DOM树head标签解析完成时，该脚本将在其来源与scriptRules匹配的任何页面中执行。当属性没有显式调用时，默认不将JavaScript脚本注入到Web组件中。

说明

* 该脚本按照数组本身顺序执行。
* 内容相同的脚本多次注入时将被静默去重，不展示，不提醒，使用首次注入时的scriptRules。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scripts | Array<[ScriptItem](arkts-basic-components-web-i.md#scriptitem11)> | 是 | 需要注入的ScriptItem数组。  传入undefined或null时不将JavaScript脚本注入到Web组件中。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();
8. private jsStr: string =
9. "window.document.getElementById(\"result\").innerHTML = 'this is msg from runJavaScriptOnHeadEnd'";
10. private jsStr2: string = "console.info('runJavaScriptOnHeadEnd urlRegexRules Matching succeeded.')";
11. @State scripts: Array<ScriptItem> = [
12. { script: this.jsStr, scriptRules: ["*"] },
13. { script: this.jsStr2, scriptRules: [], urlRegexRules: [{secondLevelDomain: "", rule: ".*index.html"}] }
14. ];

16. build() {
17. Column({ space: 20 }) {
18. Web({ src: $rawfile('index.html'), controller: this.controller })
19. .javaScriptAccess(true)
20. .domStorageAccess(true)
21. .backgroundColor(Color.Grey)
22. .runJavaScriptOnHeadEnd(this.scripts)
23. .width('100%')
24. .height('100%')
25. }
26. }
27. }
```

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="utf-8">
6. </head>
7. <body style="font-size: 30px;">
8. Hello world!
9. <div id="result">test msg</div>
10. </body>
11. </html>
```

## layoutMode11+

PhonePC/2in1TabletTVWearable

layoutMode(mode: WebLayoutMode)

设置Web布局模式。当属性没有显式调用时，默认Web布局跟随系统模式。常见问题请参考[Web组件大小自适应页面内容布局](../harmonyos-guides/web-fit-content.md)。

说明

目前只支持两种Web布局模式，分别为Web布局跟随系统（WebLayoutMode.NONE）和Web组件高度基于前端页面高度的自适应网页布局（WebLayoutMode.FIT\_CONTENT）。

Web组件高度基于前端页面自适应布局有如下限制：

* 如果Web组件宽或长度超过7680px，请在Web组件创建的时候指定RenderMode.SYNC\_RENDER模式，否则会整个白屏。
* Web组件创建后不支持动态切换layoutMode模式。
* Web组件宽高规格：指定RenderMode.ASYNC\_RENDER模式时，分别不超过7680px。
* 频繁更改页面宽高会触发Web组件重新布局，影响体验。
* 不支持瀑布流网页（下拉到底部加载更多）。
* 不支持宽度自适应，仅支持高度自适应。
* 由于高度自适应网页高度，您无法通过修改组件高度属性来修改组件高度。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebLayoutMode](arkts-basic-components-web-e.md#weblayoutmode11) | 是 | 设置web布局模式，跟随系统或自适应布局。  传入null或undefined时为WebLayoutMode.NONE |

**示例：**

1、指明layoutMode为WebLayoutMode.FIT\_CONTENT模式，为避免默认渲染模式下(RenderMode.ASYNC\_RENDER)视口高度超过7680px导致页面渲染出错，需要显式指明渲染模式(RenderMode.SYNC\_RENDER)。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. mode: WebLayoutMode = WebLayoutMode.FIT_CONTENT;

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller, renderMode: RenderMode.SYNC_RENDER })
13. .layoutMode(this.mode)
14. }
15. }
16. }
```

2、指明layoutMode为WebLayoutMode.FIT\_CONTENT模式，为避免嵌套滚动场景下，Web滚动到边缘时会优先触发过滚动的过界回弹效果影响用户体验，建议指定[overScrollMode](arkts-basic-components-web-attributes.md#overscrollmode11)为OverScrollMode.NEVER。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. layoutMode: WebLayoutMode = WebLayoutMode.FIT_CONTENT;
9. @State overScrollMode: OverScrollMode = OverScrollMode.NEVER;

11. build() {
12. Column() {
13. Web({ src: 'www.example.com', controller: this.controller, renderMode: RenderMode.SYNC_RENDER })
14. .layoutMode(this.layoutMode)
15. .overScrollMode(this.overScrollMode)
16. }
17. }
18. }
```

## nestedScroll11+

PhonePC/2in1TabletTVWearable

nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt)

调用以设置嵌套滚动选项。

说明

* 可以设置上下左右四个方向，或者设置向前、向后两个方向的嵌套滚动模式，实现与父组件的滚动联动。
* 支持嵌套滚动的容器：[Grid](ts-container-grid.md)、[List](ts-container-list.md)、[Scroll](ts-container-scroll.md)、[Swiper](ts-container-swiper.md)、[Tabs](ts-container-tabs.md)、[WaterFlow](ts-container-waterflow.md)、[Refresh](ts-container-refresh.md)、[bindSheet](ts-universal-attributes-sheet-transition.md#bindsheet)。
* 支持嵌套滚动的输入事件：使用手势、鼠标、触控板。
* 嵌套滚动场景下，由于Web滚动到边缘时会优先触发过滚动的过界回弹效果，建议设置[overScrollMode](arkts-basic-components-web-attributes.md#overscrollmode11)为OverScrollMode.NEVER，避免影响此场景的用户体验。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](ts-container-scrollable-common.md#nestedscrolloptions10对象说明) | [NestedScrollOptionsExt](arkts-basic-components-web-i.md#nestedscrolloptionsext14)14+ | 是 | 可滚动组件滚动时的嵌套滚动选项。  value为NestedScrollOptions（向前、向后两个方向）类型时，scrollForward、scrollBackward默认滚动选项为[NestedScrollMode.SELF\_FIRST](ts-appendix-enums.md#nestedscrollmode10)。  value为NestedScrollOptionsExt（上下左右四个方向）类型时，scrollUp、scrollDown、scrollLeft、scrollRight默认滚动选项为NestedScrollMode.SELF\_FIRST。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .nestedScroll({
12. scrollForward: NestedScrollMode.SELF_FIRST,
13. scrollBackward: NestedScrollMode.SELF_FIRST,
14. })
15. }
16. }
17. }
```

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController()
7. build() {
8. Scroll(){
9. Column() {
10. Text("嵌套Web")
11. .height("25%")
12. .width("100%")
13. .fontSize(30)
14. .backgroundColor(Color.Yellow)
15. Web({ src: $rawfile('index.html'),
16. controller: this.controller })
17. .nestedScroll({
18. scrollUp: NestedScrollMode.SELF_FIRST,
19. scrollDown: NestedScrollMode.PARENT_FIRST,
20. scrollLeft: NestedScrollMode.SELF_FIRST,
21. scrollRight: NestedScrollMode.SELF_FIRST,
22. })
23. }
24. }
25. }
26. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
6. <style>
7. .blue {
8. background-color: lightblue;
9. }
10. .green {
11. background-color: lightgreen;
12. }
13. .blue, .green {
14. font-size:16px;
15. height:200px;
16. text-align: center;       /* 水平居中 */
17. line-height: 200px;       /* 垂直居中（值等于容器高度） */
18. }
19. </style>
20. </head>
21. <body>
22. <div class="blue" >webArea</div>
23. <div class="green">webArea</div>
24. <div class="blue">webArea</div>
25. <div class="green">webArea</div>
26. <div class="blue">webArea</div>
27. <div class="green">webArea</div>
28. <div class="blue">webArea</div>
29. </body>
30. </html>
```

## bypassVsyncCondition20+

PhonePC/2in1TabletTVWearable

bypassVsyncCondition(condition: WebBypassVsyncCondition)

当开发者调用scrollBy接口进行页面滚动时，可以通过bypassVsyncCondition接口设置渲染流程跳过vsync（垂直同步）调度，直接触发绘制。该属性没有显式调用时，默认不跳过vsync调度。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| condition | [WebBypassVsyncCondition](arkts-basic-components-web-e.md#webbypassvsynccondition20) | 是 | 触发渲染流程跳过vsync调度的条件。  传入undefined或null时为NONE。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. condition: WebBypassVsyncCondition = WebBypassVsyncCondition.SCROLLBY_FROM_ZERO_OFFSET;

10. build() {
11. Column() {
12. Button('scrollBy')
13. .onClick(() => {
14. this.controller.scrollBy(0, 5);
15. })
16. Web({ src: 'www.example.com', controller: this.controller })
17. .bypassVsyncCondition(this.condition)
18. }
19. }
20. }
```

## enableNativeEmbedMode11+

PhonePC/2in1TabletTVWearable

enableNativeEmbedMode(enabled: boolean)

设置是否开启同层渲染功能。当该方法没有显式调用时，默认不开启同层渲染功能。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否开启同层渲染功能。  true表示开启同层渲染功能，false表示不开启同层渲染功能。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .enableNativeEmbedMode(true)
12. }
13. }
14. }
```

## forceDisplayScrollBar14+

PhonePC/2in1TabletTVWearable

forceDisplayScrollBar(enabled: boolean)

设置滚动条是否常驻。在常驻状态下，当页面大小超过一页时，滚动条出现且不消失。该属性没有显式调用时，默认设置滚动条不常驻。

全量展开模式下不支持滚动条常驻，即layoutMode为WebLayoutMode.FIT\_CONTENT模式时，参数enabled为false。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 滚动条是否常驻。  true表示滚动条常驻，false表示滚动条不常驻。  传入undefined或null时属性设置不生效。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile('index.html'), controller: this.controller })
12. .forceDisplayScrollBar(true)
13. }
14. }
15. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" content="width=device-width, initial-scale=1.0">
6. <title>Demo</title>
7. <style>
8. body {
9. width:2560px;
10. height:2560px;
11. padding-right:170px;
12. padding-left:170px;
13. border:5px solid blueviolet;
14. }
15. </style>
16. </head>
17. <body>
18. Scroll Test
19. </body>
20. </html>
```

## registerNativeEmbedRule12+

PhonePC/2in1TabletTVWearable

registerNativeEmbedRule(tag: string, type: string)

注册使用同层渲染的HTML标签名和类型。标签名仅支持使用<object>和<embed>。标签类型只能使用ASCII可显示字符。

若指定类型与W3C定义的<object>或<embed>标准类型重合，ArkWeb内核将其识别为非同层标签。

本接口同样受enableNativeEmbedMode接口控制，在未使能同层渲染时本接口无效。在不使用本接口的情况下，ArkWeb内核默认将"native/"前缀类型的<embed>标签识别为同层标签。

具体使用详情请参考[同层渲染](../harmonyos-guides/web-same-layer.md#web页面中同层渲染输入框)指南。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tag | string | 是 | 标签名。 |
| type | string | 是 | 标签类型，内核使用前缀匹配此参数。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from '@kit.ArkUI';

5. declare class Params {
6. text: string;
7. width: number;
8. height: number;
9. }

11. declare class NodeControllerParams {
12. surfaceId: string;
13. renderType: NodeRenderType;
14. width: number;
15. height: number;
16. }

18. class MyNodeController extends NodeController {
19. private rootNode: BuilderNode<[Params]> | undefined | null;
20. private surfaceId_: string = "";
21. private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
22. private width_: number = 0;
23. private height_: number = 0;

25. setRenderOption(params: NodeControllerParams) {
26. this.surfaceId_ = params.surfaceId;
27. this.renderType_ = params.renderType;
28. this.width_ = params.width;
29. this.height_ = params.height;
30. }

32. makeNode(uiContext: UIContext): FrameNode | null {
33. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
34. this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
35. return this.rootNode.getFrameNode();
36. }

38. postInputEvent(event: TouchEvent | MouseEvent | undefined): boolean {
39. return this.rootNode?.postInputEvent(event) as boolean;
40. }
41. }

43. @Component
44. struct ButtonComponent {
45. @Prop params: Params;
46. @State bkColor: Color = Color.Red;

48. build() {
49. Column() {
50. Button(this.params.text)
51. .height(50)
52. .width(200)
53. .border({ width: 2, color: Color.Red })
54. .backgroundColor(this.bkColor)
55. }
56. .width(this.params.width)
57. .height(this.params.height)
58. }
59. }

61. @Builder
62. function ButtonBuilder(params: Params) {
63. ButtonComponent({ params: params })
64. .backgroundColor(Color.Green)
65. }

67. @Entry
68. @Component
69. struct WebComponent {
70. controller: webview.WebviewController = new webview.WebviewController();
71. private nodeController: MyNodeController = new MyNodeController();
72. uiContext: UIContext = this.getUIContext();

74. build() {
75. Column() {
76. Stack() {
77. NodeContainer(this.nodeController)
78. Web({ src: $rawfile('index.html'), controller: this.controller })
79. // 配置同层渲染开关开启。
80. .enableNativeEmbedMode(true)
81. // 注册同层标签为<object>，类型为"native"前缀。
82. .registerNativeEmbedRule("object", "native")
83. // 获取<object>标签的生命周期变化数据。
84. .onNativeEmbedLifecycleChange((object) => {
85. if (object.status == NativeEmbedStatus.CREATE) {
86. this.nodeController.setRenderOption({
87. surfaceId: object.surfaceId as string,
88. renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
89. width: this.uiContext!.px2vp(object.info?.width),
90. height: this.uiContext!.px2vp(object.info?.height)
91. });
92. this.nodeController.rebuild();
93. }
94. })
95. }
96. }
97. }
98. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>同层渲染测试</title>
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. </head>
8. <body>
9. <div>
10. <div id="bodyId">
11. <object id="nativeButton" type ="native/button" width="300" height="300" style="background-color:red">
12. </object>
13. </div>
14. </div>
15. </body>
16. </html>
```

## defaultTextEncodingFormat12+

PhonePC/2in1TabletTVWearable

defaultTextEncodingFormat(textEncodingFormat: string)

设置网页的默认字符编码。当属性没有显式调用时，网页的默认字符编码为"UTF-8"。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textEncodingFormat | string | 是 | 默认字符编码。  传入null或undefined时为"UTF-8"。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile('index.html'), controller: this.controller })
12. // 设置高
13. .height(500)
14. .defaultTextEncodingFormat("UTF-8")
15. .javaScriptAccess(true)
16. }
17. }
18. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" content="width=device-width" />
6. <title>My test html5 page</title>
7. </head>
8. <body>
9. <p>hello world, 你好世界!</p>
10. </body>
11. </html>
```

## metaViewport12+

PhonePC/2in1TabletTVWearable

metaViewport(enabled: boolean)

设置meta标签的viewport属性是否可用。当属性没有显式调用时，默认支持meta标签的viewport属性。

说明

* 当前通过User-Agent中是否含有"Mobile"字段来判断是否开启前端HTML页面中meta标签的viewport属性。当User-Agent中不含有"Mobile"字段时，meta标签中viewport属性默认关闭，此时可通过显性设置metaViewport属性为true来覆盖关闭状态。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在Phone、Wearable、TV设备中可正常调用，在PC/2in1设备中无效果，在Tablet设备中，设置为true或false均会解析meta标签viewport-fit属性。当viewport-fit=cover时，可通过CSS属性获取安全区域大小。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否支持meta标签的viewport属性。  true表示支持meta标签的viewport属性，将解析viewport属性，并根据viewport属性布局。  false表示不支持meta标签的viewport属性，将不解析viewport属性，进行默认布局。  传入null或undefined时为true。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile('index.html'), controller: this.controller })
12. .metaViewport(true)
13. }
14. }
15. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" content="width=device-width, initial-scale=1.0">
6. </head>
7. <body>
8. <p>hello world, 你好世界!</p>
9. </body>
10. </html>
```

## textAutosizing12+

PhonePC/2in1TabletTVWearable

textAutosizing(textAutosizing: boolean)

设置Web组件是否开启文本字体大小自动调整。当属性没有显式调用时，Web组件默认开启文本字体大小自动调整。

文本字体大小自动调整生效后，对于字号过小的文本将自动加大字号至16px~32px，避免屏幕较小（默认视口宽度 < 980px）的设备因为缺少移动端适配出现字体过小的可读性问题。

说明

* 文本字体大小自动调整生效需要满足的前置条件：
  + 设备形态为：Phone、Tablet、Wearable、TV。
  + Web组件视口宽度 < 980px。
  + 页面文本量大，页面文本的字号\*字符数 ≥ 3920。
  + 前端无metaViewport设置，或metaViewport设置中无"width"和"initial-scale"属性。

**系统能力：** SystemCapability.Web.Webview.Core

**设备行为差异：** 该接口在PC/2in1设备中无效果，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textAutosizing | boolean | 是 | 文本自动调整大小。  true表示文本自动调整大小，false表示文本不自动调整大小。  传入undefined或null时为true。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .textAutosizing(false)
13. }
14. }
15. }
```

## enableNativeMediaPlayer12+

PhonePC/2in1TabletTVWearable

enableNativeMediaPlayer(config: NativeMediaPlayerConfig)

开启[应用接管网页媒体播放功能](../harmonyos-guides/app-takeovers-web-media.md)。当属性没有显式调用时，默认不开启接管网页媒体播放功能。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [NativeMediaPlayerConfig](arkts-basic-components-web-i.md#nativemediaplayerconfig12) | 是 | enable: 是否开启该功能。  shouldOverlay: 该功能开启后， 应用接管网页视频的播放器画面是否覆盖网页内容。  传入undefined或null时为{enable: false, shouldOverlay: false}。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .enableNativeMediaPlayer({enable: true, shouldOverlay: false})
13. }
14. }
15. }
```

## onAdsBlocked12+

PhonePC/2in1TabletTVWearable

onAdsBlocked(callback: OnAdsBlockedCallback)

一个页面发生广告过滤后，通过此回调接口通知过滤的详细信息。由于页面可能随时发生变化并不断产生网络请求，为了减少通知频次、降低对页面加载过程的影响，仅在页面加载完成时进行首次通知，此后发生的过滤将间隔1秒钟上报，无广告过滤则无通知。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnAdsBlockedCallback](arkts-basic-components-web-t.md#onadsblockedcallback12) | 是 | 广告过滤的回调。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. @State totalAdsBlockCounts: number = 0;
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: 'https://www.example.com', controller: this.controller })
13. .onAdsBlocked((details: AdsBlockedDetails) => {
14. if (details) {
15. console.info(' Blocked ' + details.adsBlocked.length + ' in ' + details.url);
16. let adList: Array<string> = Array.from(new Set(details.adsBlocked));
17. this.totalAdsBlockCounts += adList.length;
18. console.info('Total blocked counts :' + this.totalAdsBlockCounts);
19. }
20. })
21. }
22. }
23. }
```

## keyboardAvoidMode12+

PhonePC/2in1TabletTVWearable

keyboardAvoidMode(mode: WebKeyboardAvoidMode)

Web组件自定义软件键盘避让模式。

当UIContext设置的键盘避让模式为[KeyboardAvoidMode.RESIZE](arkts-apis-uicontext-e.md#keyboardavoidmode11)模式时，该接口功能不生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebKeyboardAvoidMode](arkts-basic-components-web-e.md#webkeyboardavoidmode12) | 是 | Web软键盘避让模式。  嵌套滚动场景下不推荐使用web软键盘避让，包括RESIZE\_VISUAL与RESIZE\_CONTENT。  默认值：WebKeyboardAvoidMode.RESIZE\_CONTENT避让行为。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State avoidMode: WebKeyboardAvoidMode = WebKeyboardAvoidMode.RESIZE_VISUAL;

10. build() {
11. Column() {
12. Web({ src: $rawfile("index.html"), controller: this.controller })
13. .keyboardAvoidMode(this.avoidMode)
14. }
15. }
16. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <input type="text" placeholder="Text">
9. </body>
10. </html>
```

## editMenuOptions12+

PhonePC/2in1TabletTVWearable

editMenuOptions(editMenu: EditMenuOptions)

设置Web组件自定义文本选择菜单。

用户可以通过该属性设置自定义的文本菜单。

在[onCreateMenu](ts-text-common.md#oncreatemenu12)中，可以修改、增加、删除菜单选项，如果希望不显示文本菜单，需要返回空数组。

在[onMenuItemClick](ts-text-common.md#onmenuitemclick12)中，可以自定义菜单选项的回调函数。该函数在菜单选项被点击后触发，并根据返回值决定是否执行系统默认的回调。返回true不执行系统回调，返回false继续执行系统回调。

在[onPrepareMenu20+](ts-text-common.md#属性-1)中，当文本选择区域变化后显示菜单之前触发该回调，可在该回调中进行修改、增加、删除菜单选项，实现动态更新菜单。

本接口在与[selectionMenuOptions(deprecated)](arkts-basic-components-web-attributes.md#selectionmenuoptionsdeprecated)同时使用时，会使selectionMenuOptions(deprecated)不生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| editMenu | [EditMenuOptions](ts-text-common.md#editmenuoptions) | 是 | Web自定义文本菜单选项。  菜单项数量，及菜单的content大小、icon图标尺寸，与ArkUI [Menu](ts-basic-components-menu.md)组件保持一致。  菜单中系统自带的id枚举值（[TextMenuItemId](ts-text-common.md#textmenuitemid12)）在Web中仅支持CUT、COPY、PASTE、SELECT\_ALL、TRANSLATE、SEARCH、AI\_WRITER七项。  onMenuItemClick函数中textRange参数在web中无意义，传入值为-1。 |

**示例**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. let selectText:string = '';
5. class TestClass {
6. setSelectText(param: String) {
7. selectText = param.toString();
8. }
9. }

11. @Entry
12. @Component
13. struct WebComponent {
14. controller: webview.WebviewController = new webview.WebviewController();
15. @State testObj: TestClass = new TestClass();

17. onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem> {
18. let items = menuItems.filter((menuItem) => {
19. // 过滤用户需要的系统按键
20. return (
21. menuItem.id.equals(TextMenuItemId.CUT) ||
22. menuItem.id.equals(TextMenuItemId.COPY) ||
23. menuItem.id.equals((TextMenuItemId.PASTE)) ||
24. menuItem.id.equals((TextMenuItemId.TRANSLATE)) ||
25. menuItem.id.equals((TextMenuItemId.SEARCH)) ||
26. menuItem.id.equals((TextMenuItemId.AI_WRITER))
27. )
28. });
29. let customItem1: TextMenuItem = {
30. content: 'customItem1',
31. id: TextMenuItemId.of('customItem1'),
32. icon: $r('app.media.icon')
33. };
34. let customItem2: TextMenuItem = {
35. content: $r('app.string.customItem2'),
36. id: TextMenuItemId.of('customItem2'),
37. icon: $r('app.media.icon')
38. };
39. items.push(customItem1);// 在选项列表后添加新选项
40. items.unshift(customItem2);// 在选项列表前添加选项

42. return items;
43. }

45. onMenuItemClick(menuItem: TextMenuItem, textRange: TextRange): boolean {
46. if (menuItem.id.equals(TextMenuItemId.CUT)) {
47. // 用户自定义行为
48. console.info("拦截 id：CUT")
49. return true; // 返回true不执行系统回调
50. } else if (menuItem.id.equals(TextMenuItemId.COPY)) {
51. // 用户自定义行为
52. console.info("不拦截 id：COPY")
53. return false; // 返回false执行系统回调
54. } else if (menuItem.id.equals(TextMenuItemId.of('customItem1'))) {
55. // 用户自定义行为
56. console.info("拦截 id：customItem1")
57. return true;// 用户自定义菜单选项返回true时点击后不关闭菜单，返回false时关闭菜单
58. } else if (menuItem.id.equals((TextMenuItemId.of($r('app.string.customItem2'))))){
59. // 用户自定义行为
60. console.info("拦截 id：app.string.customItem2")
61. return true;
62. }
63. return false;// 返回默认值false
64. }

66. onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
67. let item1: TextMenuItem = {
68. content: 'prepare1',
69. id: TextMenuItemId.of('prepareMenu1'),
70. };
71. let item2: TextMenuItem = {
72. content: 'prepare2' + selectText,
73. id: TextMenuItemId.of('prepareMenu2'),
74. };
75. menuItems.push(item1);// 在选项列表后添加新选项
76. menuItems.unshift(item2);// 在选项列表前添加选项

78. return menuItems;
79. }

81. @State EditMenuOptions: EditMenuOptions =
82. { onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick, onPrepareMenu:this.onPrepareMenu }

84. build() {
85. Column() {
86. Web({ src: $rawfile("index.html"), controller: this.controller })
87. .editMenuOptions(this.EditMenuOptions)
88. .javaScriptProxy({
89. object: this.testObj,
90. name: "testObjName",
91. methodList: ["setSelectText"],
92. controller: this.controller,
93. })
94. }
95. }
96. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <h1>editMenuOptions Demo</h1>
9. <span>edit menu options</span>
10. <script>
11. document.addEventListener('selectionchange', () => {
12. var selection = window.getSelection();
13. if (selection.rangeCount > 0) {
14. var selectedText = selection.toString();
15. testObjName.setSelectText(selectedText);
16. }
17. });
18. </script>
19. </body>
20. </html>
```

## enableHapticFeedback13+

PhonePC/2in1TabletTVWearable

enableHapticFeedback(enabled: boolean)

设置Web组件长按文本选择是否开启振动。需配置"ohos.permission.VIBRATE"。该属性没有显式调用时，默认开启振动。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否开启振动。  true表示开启振动，false表示不开启振动。  传入undefined或null时属性设置不生效。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .enableHapticFeedback(true)
13. }
14. }
15. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <h1>enableHapticFeedback Demo</h1>
9. <span>enable haptic feedback</span>
10. </body>
11. </html>
```

## bindSelectionMenu13+

PhonePC/2in1TabletTVWearable

bindSelectionMenu(elementType: WebElementType, content: CustomBuilder, responseType: WebResponseType, options?: SelectionMenuOptionsExt)

设置自定义选择菜单。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementType | [WebElementType](arkts-basic-components-web-e.md#webelementtype13) | 是 | 菜单的类型。 |
| content | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 菜单的内容。 |
| responseType | [WebResponseType](arkts-basic-components-web-e.md#webresponsetype13) | 是 | 菜单的响应类型。 |
| options | [SelectionMenuOptionsExt](arkts-basic-components-web-i.md#selectionmenuoptionsext13) | 否 | 菜单的选项。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { pasteboard } from '@kit.BasicServicesKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. interface PreviewBuilderParam {
7. width: number;
8. height: number;
9. url:Resource | string | undefined;
10. }

12. interface PreviewBuilderParamForImage {
13. previewImage: Resource | string | undefined;
14. width: number;
15. height: number;
16. }

19. @Builder function PreviewBuilderGlobalForImage($$: PreviewBuilderParamForImage) {
20. Column() {
21. Image($$.previewImage)
22. .objectFit(ImageFit.Fill)
23. .autoResize(true)
24. }.width($$.width).height($$.height)
25. }

27. @Entry
28. @Component
29. struct SelectionMenuLongPress {
30. controller: webview.WebviewController = new webview.WebviewController();
31. previewController: webview.WebviewController = new webview.WebviewController();
32. @Builder PreviewBuilder($$: PreviewBuilderParam){
33. Column() {
34. Stack(){
35. Text("") // 可选择是否展示url
36. .padding(5)
37. .width('100%')
38. .textAlign(TextAlign.Start)
39. .backgroundColor(Color.White)
40. .copyOption(CopyOptions.LocalDevice)
41. .maxLines(1)
42. .textOverflow({overflow:TextOverflow.Ellipsis})
43. Progress({ value: this.progressValue, total: 100, type: ProgressType.Linear }) // 展示进度条
44. .style({ strokeWidth: 3, enableSmoothEffect: true })
45. .backgroundColor(Color.White)
46. .opacity(this.progressVisible?1:0)
47. .backgroundColor(Color.White)
48. }.alignContent(Alignment.Bottom)
49. Web({src:$$.url,controller: new webview.WebviewController()})
50. .javaScriptAccess(true)
51. .fileAccess(true)
52. .onlineImageAccess(true)
53. .imageAccess(true)
54. .domStorageAccess(true)
55. .onPageBegin(()=>{
56. this.progressValue = 0;
57. this.progressVisible = true;
58. })
59. .onProgressChange((event)=>{
60. this.progressValue = event.newProgress;
61. })
62. .onPageEnd(()=>{
63. this.progressVisible = false;
64. })
65. .hitTestBehavior(HitTestMode.None) // 使预览Web不响应手势
66. }.width($$.width).height($$.height) // 设置预览宽高
67. }

69. private result: WebContextMenuResult | undefined = undefined;
70. @State previewImage: Resource | string | undefined = undefined;
71. @State previewWidth: number = 1;
72. @State previewHeight: number = 1;
73. @State previewWidthImage: number = 1;
74. @State previewHeightImage: number = 1;
75. @State linkURL:string = "";
76. @State progressValue:number = 0;
77. @State progressVisible:boolean = true;
78. uiContext: UIContext = this.getUIContext();
79. enablePaste = false;

81. clearSelection() {
82. try {
83. this.controller.runJavaScript(
84. 'clearSelection()',
85. (error, result) => {
86. if (error) {
87. console.error(`run clearSelection JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
88. return;
89. }
90. if (result) {
91. console.info(`The clearSelection() return value is: ${result}`);
92. }
93. });
94. } catch (error) {
95. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
96. }
97. }

100. @Builder
101. LinkMenuBuilder() {
102. Menu() {
103. MenuItem({ content: '复制链接', })
104. .onClick(() => {
105. const pasteboardData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, this.linkURL);
106. const systemPasteboard = pasteboard.getSystemPasteboard();
107. systemPasteboard.setData(pasteboardData);
108. })
109. MenuItem({content:'打开链接'})
110. .onClick(()=>{
111. this.controller.loadUrl(this.linkURL);
112. })
113. }
114. }
115. @Builder
116. ImageMenuBuilder() {
117. Menu() {
118. MenuItem({ content: '复制图片', })
119. .onClick(() => {
120. this.result?.copyImage();
121. this.result?.closeContextMenu();
122. })
123. }
124. }
125. @Builder
126. TextMenuBuilder() {
127. Menu() {
128. MenuItem({ content: '复制', })
129. .onClick(() => {
130. try {
131. this.controller.runJavaScript(
132. 'copySelectedText()',
133. (error, result) => {
134. if (error) {
135. console.error(`run copySelectedText JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
136. return;
137. }
138. if (result) {
139. console.info(`The copySelectedText() return value is: ${result}`);
140. }
141. });
142. } catch (error) {
143. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
144. }
145. this.clearSelection()
146. }).backgroundColor(Color.Pink)
147. }
148. }
149. build() {
150. Column() {
151. Web({ src: $rawfile("index.html"), controller: this.controller })
152. .javaScriptAccess(true)
153. .fileAccess(true)
154. .onlineImageAccess(true)
155. .imageAccess(true)
156. .domStorageAccess(true)
157. .bindSelectionMenu(WebElementType.TEXT, this.TextMenuBuilder, WebResponseType.LONG_PRESS,
158. {
159. onAppear: () => {},
160. onDisappear: () => {},
161. menuType: MenuType.SELECTION_MENU,
162. })
163. .bindSelectionMenu(WebElementType.LINK, this.LinkMenuBuilder, WebResponseType.LONG_PRESS,
164. {
165. onAppear: () => {},
166. onDisappear: () => {
167. this.result?.closeContextMenu();
168. },
169. preview: this.PreviewBuilder({
170. width: 500,
171. height: 400,
172. url:this.linkURL
173. }),
174. menuType: MenuType.PREVIEW_MENU
175. })
176. .bindSelectionMenu(WebElementType.IMAGE, this.ImageMenuBuilder, WebResponseType.LONG_PRESS,
177. {
178. onAppear: () => {},
179. onDisappear: () => {
180. this.result?.closeContextMenu();
181. },
182. preview: PreviewBuilderGlobalForImage({
183. previewImage: this.previewImage,
184. width: this.previewWidthImage,
185. height: this.previewHeightImage,
186. }),
187. menuType: MenuType.PREVIEW_MENU,
188. })
189. .zoomAccess(true)
190. .onContextMenuShow((event) => {
191. if (event) {
192. this.result = event.result;
193. this.previewWidthImage = this.uiContext!.px2vp(event.param.getPreviewWidth());
194. this.previewHeightImage = this.uiContext!.px2vp(event.param.getPreviewHeight());
195. if (event.param.getSourceUrl().indexOf("resource://rawfile/") == 0) {
196. this.previewImage = $rawfile(event.param.getSourceUrl().substring(19));
197. } else {
198. this.previewImage = event.param.getSourceUrl();
199. }
200. this.linkURL = event.param.getLinkUrl()
201. return true;
202. }
203. return false;
204. })
205. }

207. }
208. // 侧滑返回
209. onBackPress(): boolean | void {
210. if (this.controller.accessStep(-1)) {
211. this.controller.backward();
212. return true;
213. } else {
214. return false;
215. }
216. }
217. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html lang="zh-CN">
4. <head>
5. <meta charset="UTF-8">
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. <title>长按复制文本</title>
8. <style>
9. .container {
10. background-color: white;
11. padding: 30px;
12. margin: 20px 0;
13. }

15. .context {
16. line-height: 1.8;
17. font-size: 18px;
18. }

20. .context span {
21. border-radius: 8px;
22. background-color: #f8f9fa;
23. }

25. .context a {
26. color: #3498db;
27. text-decoration: none;
28. font-size: 18px;
29. font-weight: 600;
30. padding: 12px 24px;
31. border: 2px solid #3498db;
32. border-radius: 30px;
33. display: inline-block;
34. position: relative;
35. overflow: hidden;
36. margin-bottom: 20px;
37. }

39. .context img {
40. max-width: 100%;
41. height: auto;
42. display: block;
43. margin-bottom: 20px;
44. }

46. .context:hover img {
47. transform: scale(1.05);
48. }
49. </style>
50. </head>
51. <body>
52. <div class="container">

54. <div class="context">
55. <!--img.png为html同目录下图片-->
56. <img src="img.png">
57. </div>

59. <div class="context">
60. <a  href="https://www.example.com">长按链接唤起菜单</a>
61. </div>

63. <div class="context">
64. <span>在这个数字时代，文本复制功能变得日益重要。无论是引用名言、保存重要信息，还是分享有趣的内容，复制文本都是我们日常操作的一部分。</span>
65. </div>

67. </div>
68. <br>

70. <script>
71. function copySelectedText() {
72. const selectedText = window.getSelection().toString();
73. if (selectedText.length > 0) {
74. // 使用Clipboard API复制文本
75. navigator.clipboard.writeText(selectedText)
76. .then(() => {
77. showNotification();
78. })
79. .catch(err => {
80. console.error('复制失败:', err);
81. });
82. }
83. }
84. function clearSelection() {
85. if (window.getSelection) {
86. window.getSelection().removeAllRanges();
87. }
88. }
89. </script>
90. </body>
91. </html>
```

## blurOnKeyboardHideMode14+

PhonePC/2in1TabletTVWearable

blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode)

设置当软键盘收起时Web元素失焦模式。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [BlurOnKeyboardHideMode](arkts-basic-components-web-e.md#bluronkeyboardhidemode14) | 是 | 设置当软键盘收起时Web元素失焦关闭或开启。默认值：BlurOnKeyboardHideMode.SILENT。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State blurMode: BlurOnKeyboardHideMode = BlurOnKeyboardHideMode.BLUR;
9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .blurOnKeyboardHideMode(this.blurMode)
13. }
14. }
15. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <h1>blurOnKeyboardHideMode Demo</h1>
9. <input type="text" id="input_a">
10. <script>
11. const inputElement = document.getElementById('input_a');
12. inputElement.addEventListener('blur', function() {
13. console.info('Input has lost focus');
14. });
15. </script>
16. </body>
17. </html>
```

## enableFollowSystemFontWeight18+

PhonePC/2in1TabletTVWearable

enableFollowSystemFontWeight(follow: boolean)

设置Web组件是否开启字重跟随系统设置变化。当属性没有显式调用时，Web组件默认开启字重跟随系统设置变化。

说明

目前该能力只支持前端文本元素跟随变化，暂不支持canvas元素、内嵌docx和pdf格式中的文本跟随变化。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| follow | boolean | 是 | 设置Web组件是否开启字重跟随系统设置变化。  true表示字重跟随系统设置中的字体粗细变化，系统设置改变时字重跟随变化。false表示字重不再跟随系统设置中的字体粗细变化，系统设置改变时维持当前字重不变。  传入undefined或null时为true。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. build() {
9. Column() {
10. Web({ src: "www.example.com", controller: this.controller })
11. .enableFollowSystemFontWeight(true)
12. }
13. }
14. }
```

## optimizeParserBudget15+

PhonePC/2in1TabletTVWearable

optimizeParserBudget(optimizeParserBudget: boolean)

设置是否开启分段解析HTML优化。当属性没有显式调用时，默认使用解析时间作为HTML分段解析的分段点。

ArkWeb内核在解析HTML文档结构时采取分段解析策略，旨在避免过多占用主线程资源，并使网页具有渐进式加载能力。ArkWeb内核默认使用解析时间作为分段点，当单次解析时间超过阈值时，会中断解析，随后进行布局和渲染操作。

开启优化后，ArkWeb内核将不仅检查解析时间是否超出限制，还会额外判断解析的Token（HTML文档的最小解析单位，例如<div>、attr="xxx"等）数量是否超过内核规定的阈值，并下调此阈值。当页面的FCP（First Contentful Paint 首次内容绘制）触发时会恢复成默认的中断判断逻辑。这将使得网页在FCP到来之前的解析操作更频繁，从而提高首帧内容被提前解析完成并进入渲染阶段的可能性，同时有效缩减首帧渲染的工作量，最终实现FCP时间提前。

由于页面的FCP触发时会恢复成默认分段解析逻辑，因此分段解析HTML优化仅对每个Web组件加载的首个页面生效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| optimizeParserBudget | boolean | 是 | 设置开启分段解析HTML优化。  true表示使用解析个数代替解析时间作为HTML分段解析的分段点，并减少每段解析的个数上限。false表示使用解析时间作为HTML分段解析的分段点。  传入undefined或null时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController()
8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .optimizeParserBudget(true)
12. }
13. }
14. }
```

## enableWebAVSession18+

PhonePC/2in1TabletTVWearable

enableWebAVSession(enabled: boolean)

设置是否支持应用对接到播控中心。当属性没有显式设置时，默认支持应用对接到播控中心。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否支持应用对接到播控中心。  true表示支持应用对接到播控中心，false表示不支持应用对接到播控中心。  传入undefined或null时为true。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. build() {
9. Column() {
10. Web({ src: $rawfile('index.html'), controller: this.controller })
11. .enableWebAVSession(true)
12. }
13. }
14. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>视频播放页面</title>
6. </head>
7. <body>
8. <h1>视频播放</h1>
9. <video id="testVideo" controls>
10. <!--在resources的rawfile目录中放置任意一个mp4媒体文件，并将其命名为example.mp4-->
11. <source src="example.mp4" type="video/mp4">
12. </video>
13. </body>
14. </html>
```

## nativeEmbedOptions16+

PhonePC/2in1TabletTVWearable

nativeEmbedOptions(options?: EmbedOptions)

设置同层渲染相关配置，该属性仅在[enableNativeEmbedMode](arkts-basic-components-web-attributes.md#enablenativeembedmode11)开启时生效，不支持动态修改。当属性没有显式调用时，默认为{supportDefaultIntrinsicSize: false}。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [EmbedOptions](arkts-basic-components-web-i.md#embedoptions16) | 否 | 同层渲染相关配置。  传入undefined或null时为{supportDefaultIntrinsicSize: false}。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. options: EmbedOptions = {supportDefaultIntrinsicSize: true};

10. build() {
11. Column() {
12. Web({ src: $rawfile("index.html"), controller: this.controller })
13. .enableNativeEmbedMode(true)
14. .nativeEmbedOptions(this.options)
15. }
16. }
17. }
```

加载的html文件

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>同层渲染固定大小测试html</title>
6. </head>
7. <body>
8. <div>
9. <embed id="input" type = "native/view" style = "background-color:red"/>
10. </div>
11. </body>
12. </html>
```

## enableDataDetector20+

PhonePC/2in1TabletTVWearable

enableDataDetector(enable: boolean)

设置是否识别网页文本特殊实体，如邮件、电话、网址等。该接口依赖设备底层具备文本识别能力，否则设置无效。该属性没有显式调用时，默认不启用。

当enableDataDetector设置为true，同时不设置[dataDetectorConfig](arkts-basic-components-web-attributes.md#datadetectorconfig20)属性时，默认识别所有类型的实体，所识别实体的color和decoration会被更改为如下样式：

```
1. color: '#ff0a59f7',
2. decoration:{
3. type: TextDecorationType.Underline,
4. color: '#ff0a59f7',
5. style: TextDecorationStyle.SOLID
6. }
```

当enableDataDetector设置为true且[copyOptions](arkts-basic-components-web-attributes.md#copyoptions11)设置为CopyOptions.LocalDevice时，AI菜单功能将被激活。此时，在网页中选中文本后，文本选择菜单能够展示对应的AI菜单项，包括[TextMenuItemId](ts-text-common.md#textmenuitemid12)中的url（打开链接）、email（新建邮件）、phoneNumber（呼叫）、address（导航至该位置）、dateTime（新建日程提醒）。

AI菜单生效时，需在选中范围内，包括一个完整的AI实体，才能展示对应的选项。该菜单项与[TextMenuItemId](ts-text-common.md#textmenuitemid12)中的askAI菜单项不同时出现。

示例使用场景详见[使用Web组件的智能分词能力](../harmonyos-guides/web-data-detector.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用Web文本识别，true表示启用，false表示不启用。  传入undefined或null时属性设置不生效。 |

说明

动态更新enableDataDetector的启用状态不会即时影响当前页面，需通过刷新页面来使新配置生效。

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .enableDataDetector(true)
13. }
14. }
15. }
```

加载的html文件

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>enableDataDetector示例</title>
6. </head>
7. <body>
8. <p> 电话：400-123-4567 </p>
9. <p> 邮箱：example@example.com </p>
10. </body>
11. </html>
```

## dataDetectorConfig20+

PhonePC/2in1TabletTVWearable

dataDetectorConfig(config: TextDataDetectorConfig)

设置文本识别配置。

需配合[enableDataDetector](arkts-basic-components-web-attributes.md#enabledatadetector20)一起使用，设置enableDataDetector为true时，dataDetectorConfig的配置才能生效。

当两个实体A、B重叠时，按以下规则保留实体：

1. 若A ⊂ B，则保留B，反之则保留A。
2. 当A ⊄ B且B ⊄ A时，若A.start < B.start，则保留A，反之则保留B。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [TextDataDetectorConfig](ts-text-common.md#textdatadetectorconfig11对象说明) | 是 | 文本识别配置。 |

说明

TextDataDetectorConfig中的onDetectResultUpdate在Web组件中不支持，设置的回调不会调用。

[copyOptions](arkts-basic-components-web-attributes.md#copyoptions11)设置为CopyOptions.None时，TextDataDetectorConfig中的enablePreviewMenu配置项无效。

动态更新TextDataDetectorConfig的配置不会即时影响当前页面，需通过刷新页面来使新配置生效。

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .enableDataDetector(true)
13. .dataDetectorConfig({
14. types: [
15. TextDataDetectorType.PHONE_NUMBER,
16. TextDataDetectorType.EMAIL
17. ],
18. color: Color.Red,
19. decoration: {
20. type: TextDecorationType.LineThrough,
21. color: Color.Green,
22. style: TextDecorationStyle.WAVY
23. }
24. })
25. }
26. }
27. }
```

加载的html文件

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>dataDetectorConfig示例</title>
6. </head>
7. <body>
8. <p> 电话：400-123-4567 </p>
9. <p> 邮箱：12345678901@example.com </p>
10. <p> 网址：www.example.com（此项不识别）</p>
11. </body>
12. </html>
```

## enableSelectedDataDetector22+

PhonePC/2in1TabletTVWearable

enableSelectedDataDetector(enable: boolean)

设置是否启用文本选择的AI菜单功能，启用后可识别选区中的邮件、电话、网址、日期、地址等，并在文本选择菜单中展示对应的AI菜单项。默认启用AI菜单功能。

AI菜单功能启用时，在网页中选中文本后，文本选择菜单能够展示对应的AI菜单项，包括[TextMenuItemId](ts-text-common.md#textmenuitemid12)中的url（打开链接）、email（新建邮件）、phoneNumber（呼叫）、address（导航前往）、dateTime（新建日程）。

AI菜单生效时，需在选中范围内，包括一个完整的AI实体，才能展示对应的选项。该菜单项与[TextMenuItemId](ts-text-common.md#textmenuitemid12)中的askAI菜单项不同时出现。

示例使用场景详见[使用Web组件的智能分词能力](../harmonyos-guides/web-data-detector.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用Web文本识别，true表示启用，false表示不启用。  传入undefined或null时属性重置为默认值。 |

说明

当enableSelectedDataDetector未配置或设置为true时，将遵循[dataDetectorConfig](arkts-basic-components-web-attributes.md#datadetectorconfig20)中types的配置；若[dataDetectorConfig](arkts-basic-components-web-attributes.md#datadetectorconfig20)也未配置，则默认识别所有类型。

当enableSelectedDataDetector设置为false时，不激活实体文本选择AI菜单项。

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .enableSelectedDataDetector(true)
13. }
14. }
15. }
```

加载的html文件

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>enableSelectedDataDetector示例</title>
6. </head>
7. <body>
8. <p> 电话：400-123-4567 </p>
9. <p> 邮箱：example@example.com </p>
10. </body>
11. </html>
```

## gestureFocusMode20+

PhonePC/2in1TabletTVWearable

gestureFocusMode(mode: GestureFocusMode)

设置Web组件手势获焦模式。该属性没有显式调用时，默认表示手势按下时，任何手势均会使Web组件获焦。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [GestureFocusMode](arkts-basic-components-web-e.md#gesturefocusmode20) | 是 | 设置Web组件手势获焦模式。传入undefined或null时为GestureFocusMode.DEFAULT。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State mode: GestureFocusMode = GestureFocusMode.DEFAULT;
9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .gestureFocusMode(this.mode)
13. }
14. }
15. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <input type="text" placeholder="Text">
9. </body>
10. </html>
```

## rotateRenderEffect22+

PhonePC/2in1TabletTVWearable

rotateRenderEffect(effect: WebRotateEffect)

设置Web组件旋转时，宽高动画过程中组件内容的填充方式。若未显式调用属性，默认保持动画终态的内容大小，内容始终与组件左上角对齐。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [WebRotateEffect](arkts-basic-components-web-e.md#webrotateeffect22) | 是 | 设置Web组件旋转时，宽高动画过程中组件内容的填充方式。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State effect: WebRotateEffect = WebRotateEffect.TOPLEFT_EFFECT;
9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .rotateRenderEffect(this.effect)
13. }
14. }
15. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <p>测试网页</p>
9. </body>
10. </html>
```

## forceEnableZoom21+

PhonePC/2in1TabletTVWearable

forceEnableZoom(enable: boolean)

设置Web组件是否启用强制缩放功能。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 设置是否遵从网页中<meta name="viewport">标签设置的缩放限制。  设置为true时，不遵从网页缩放限制；设置为false时，遵从网页缩放限制。  传入undefined与null时属性设置不生效。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .forceEnableZoom(true)
13. }
14. }
15. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
6. <title>测试网页</title>
7. </head>
8. <body>
9. <h1>forceEnableZoom Demo</h1>
10. <span>You can scale page when forceEnableZoom is true.</span>
11. </body>
12. </html>
```

## backToTop22+

PhonePC/2in1TabletTVWearable

backToTop(backToTop: boolean)

设置Web组件是否启用点击状态栏网页回到顶部功能。当属性没有显式调用时，默认开启状态栏网页回到顶部功能。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backToTop | boolean | 是 | 是否启用Web点击状态栏回顶，true表示启用，false表示不启用。  传入undefined或null时为true。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .backToTop(true)
13. }
14. }
15. }
```

加载的html文件：

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
6. <style>
7. .blue {
8. background-color: lightblue;
9. }
10. .green {
11. background-color: lightgreen;
12. }
13. .blue, .green {
14. font-size:16px;
15. height:200px;
16. text-align: center;       /* 水平居中 */
17. line-height: 200px;       /* 垂直居中（值等于容器高度） */
18. }
19. </style>
20. </head>
21. <body>
22. <div class="blue" >webArea</div>
23. <div class="green">webArea</div>
24. <div class="blue">webArea</div>
25. <div class="green">webArea</div>
26. <div class="blue">webArea</div>
27. <div class="green">webArea</div>
28. <div class="blue">webArea</div>
29. <div class="green">webArea</div>
30. <div class="blue">webArea</div>
31. </body>
32. </html>
```

## blankScreenDetectionConfig22+

PhonePC/2in1TabletTVWearable

blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig)

设置白屏检测的策略配置，如使能开关、检测时间和检测策略等。当属性没有显式调用时，默认关闭白屏检测。

说明

* 根据detectConfig的配置，在网页加载后检测到白屏或者近似白屏现象，可触发回调[onDetectedBlankScreen](arkts-basic-components-web-events.md#ondetectedblankscreen22)。
* 设置后下次导航生效。
* 当用户与网页发生交互后，不再会继续检查是否白屏。
* 不支持layoutMode为WebLayoutMode.FIT\_CONTENT的场景。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| detectConfig | [BlankScreenDetectionConfig](arkts-basic-components-web-i.md#blankscreendetectionconfig22) | 是 | 白屏检测的策略配置。 |

**示例：**

```
1. // blankScreenDetectionConfig.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .blankScreenDetectionConfig({
13. enable: true,
14. detectionTiming: [2, 4, 6, 8],
15. contentfulNodesCountThreshold: 4,
16. detectionMethods:[BlankScreenDetectionMethod.DETECTION_CONTENTFUL_NODES_SEVENTEEN]
17. })
18. .onDetectedBlankScreen((event: BlankScreenDetectionEventInfo)=>{
19. console.info(`Found blank screen on ${event.url}.`);
20. console.info(`The blank screen reason is ${event.blankScreenReason}.`);
21. console.info(`The blank screen detail is ${event.blankScreenDetails?.detectedContentfulNodesCount}.`);
22. })
23. }
24. }
25. }
```

## enableImageAnalyzer23+

PhonePC/2in1TabletTVWearable

enableImageAnalyzer(enable: boolean)

设置是否启用网页图片AI分析，当前支持图片文字识别功能，该功能默认开启。

说明

长按或鼠标悬停在图片文字上时，触发图片AI分析，可以选中图片中的文字。能够触发分析的图片规格如下。

* 图片的原始长宽均不小于100px。
* 在[设备类型](../harmonyos-guides/module-configuration-file.md#devicetypes标签)不为2in1的设备上，需要图片渲染宽度超过网页宽度的80%。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用网页图片AI分析，true表示启用，false表示不启用。  传入undefined或null时重置为true。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .enableImageAnalyzer(true) // 如果需要关闭图片分析能力，需要显式设置为false
13. }
14. }
15. }
```

加载的html文件：

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <head>
4. <meta charset="UTF-8">
5. <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
6. <style>
7. .image-container {
8. width: 90%;
9. }
10. .image-container img {
11. width: 100%;
12. height: auto;
13. }
14. </style>
15. </head>
16. <body>
17. <div class="image-container">
18. <!--example.jpg为html同目录下图片-->
19. <img src="example.jpg" alt="待AI分析的图片">
20. </div>
21. </body>
22. </html>
```

## enableAutoFill23+

PhonePC/2in1TabletTVWearable

enableAutoFill(value: boolean)

设置是否启用网页自动填充，默认开启。

说明

网页使用智能填充和密码填充前，需要网页接入对应的填充服务。具体接入方法请查看[网页接入智能填充](../harmonyos-guides/scenario-fusion-h5.md)、[网页接入密码填充](../harmonyos-guides/arkweb-access-password-safe.md)

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否启用网页自动填充，true表示启用，false表示不启用。  传入undefined或null时为true。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .enableAutoFill(true)
13. }
14. }
15. }
```

加载的html文件：

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0;" name="viewport"/>
6. <title>自动填充测试</title>
7. </head>
8. <body>
9. <h4 align="center">自动填充测试</h4>
10. <form method="post" action="">
11. <div align="center">
12. <label for="name" style="width: 120px; display: inline-block; text-align: end;">姓名:</label>
13. <input type="text" id="name" autocomplete="name"/><br/><br/>
14. <label for="tel-national" style="width: 120px; display: inline-block; text-align: end;">手机号:</label>
15. <input type="text" id="tel-national" autocomplete="tel-national"/><br/><br/>
16. </div>
17. <div align="center">
18. <button type="submit" style="width: 80px">提交</button>
19. </div>
20. </form>
21. </body>
22. </html>
```

## password(deprecated)

PhonePC/2in1TabletTVWearable

password(password: boolean)

设置是否应保存密码。该接口为空接口。

说明

从API version 8开始支持，从API version 10开始废弃，建议使用[enableAutoFill23+](arkts-basic-components-web-attributes.md#enableautofill23)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| password | boolean | 是 | 设置为true时，表示允许Web保存密码。  设置为false时，表示不允许Web保存密码。 |

## textZoomAtio(deprecated)

PhonePC/2in1TabletTVWearable

textZoomAtio(textZoomAtio: number)

设置页面的文本缩放百分比。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[textZoomRatio9+](arkts-basic-components-web-attributes.md#textzoomratio9)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textZoomAtio | number | 是 | 要设置的页面的文本缩放百分比。  取值范围为正整数。  默认值：100。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WebComponent {
5. controller: WebController = new WebController()
6. @State ratio: number = 150
7. build() {
8. Column() {
9. Web({ src: 'www.example.com', controller: this.controller })
10. .textZoomAtio(this.ratio)
11. }
12. }
13. }
```

## userAgent(deprecated)

PhonePC/2in1TabletTVWearable

userAgent(userAgent: string)

设置用户代理。

说明

从API version 8开始支持，从API version 10开始废弃。建议使用[setCustomUserAgent](arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)10+替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | 要设置的用户代理。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State userAgent:string = 'Mozilla/5.0 (Phone; OpenHarmony 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 ArkWeb/4.1.6.1 Mobile DemoApp';

10. build() {
11. Column() {
12. Web({ src: 'www.example.com', controller: this.controller })
13. .userAgent(this.userAgent)
14. }
15. }
16. }
```

## tableData(deprecated)

PhonePC/2in1TabletTVWearable

tableData(tableData: boolean)

设置是否应保存表单数据。当属性没有显式调用时，默认允许Web保存表单数据。该接口为空接口。

说明

从API version 8开始支持，从API version 10开始废弃，建议使用[enableAutoFill23+](arkts-basic-components-web-attributes.md#enableautofill23)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tableData | boolean | 是 | 设置为true时，表示允许Web保存表单数据。  设置为false时，表示不允许Web保存表单数据。 |

## wideViewModeAccess(deprecated)

PhonePC/2in1TabletTVWearable

wideViewModeAccess(wideViewModeAccess: boolean)

设置Web是否支持html中meta标签的viewport属性。该接口为空接口。

说明

从API version 8开始支持，从API version 10开始废弃，建议使用[metaViewport12+](arkts-basic-components-web-attributes.md#metaviewport12)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wideViewModeAccess | boolean | 是 | 设置Web是否支持html中meta标签的viewport属性。  true表示支持html中meta标签的viewport属性，false表示不支持html中meta标签的viewport属性。 |

## selectionMenuOptions(deprecated)

PhonePC/2in1TabletTVWearable

selectionMenuOptions(expandedMenuOptions: Array<ExpandedMenuItemOptions>)

Web组件自定义菜单扩展项接口，允许用户设置扩展项的文本内容、图标、回调方法。

该接口只支持选中纯文本，当选中内容包含图片及其他非文本内容时，action信息中会显示乱码。

说明

从API version 12开始支持，从API version 20开始废弃。建议使用[editMenuOptions12+](arkts-basic-components-web-attributes.md#editmenuoptions12)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| expandedMenuOptions | Array<[ExpandedMenuItemOptions](arkts-basic-components-web-i.md#expandedmenuitemoptionsdeprecated)> | 是 | 扩展菜单选项。  菜单项数量，及菜单的content大小、startIcon图标尺寸，与ArkUI [Menu](ts-basic-components-menu.md)组件保持一致。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. @State menuOptionArray: Array<ExpandedMenuItemOptions> = [
9. {content: 'Apple', startIcon: $r('app.media.icon'), action: (selectedText) => {
10. console.info('select info ' + selectedText.toString());
11. }},
12. {content: '香蕉', startIcon: $r('app.media.icon'), action: (selectedText) => {
13. console.info('select info ' + selectedText.toString());
14. }}
15. ];

17. build() {
18. Column() {
19. Web({ src: $rawfile("index.html"), controller: this.controller })
20. .selectionMenuOptions(this.menuOptionArray)
21. }
22. }
23. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <h1>selectionMenuOptions Demo</h1>
9. <span>selection menu options</span>
10. </body>
11. </html>
```

## zoomControlAccess22+

PhonePC/2in1TabletTVWearable

zoomControlAccess(zoomControlAccess: boolean)

设置是否允许通过组合按键（Ctrl+'-/+'或Ctrl+鼠标滚轮/触摸板）进行缩放。

当属性没有显式调用时，默认允许通过组合按键进行缩放。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zoomControlAccess | boolean | 是 | 设置是否允许通过组合按键进行缩放。true表示支持，false表示不支持。传入null或undefined时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: $rawfile("index.html"), controller: this.controller })
12. .zoomControlAccess(true)
13. }
14. }
15. }
```

加载的html文件。

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta name="viewport" content="width=device-width, initial-scale=1.0">
6. <title>测试网页</title>
7. </head>
8. <body>
9. <h1>zoomControlAccess Demo</h1>
10. <span>You can zoom in/out page when zoomControlAccess is true.</span>
11. </body>
12. </html>
```
