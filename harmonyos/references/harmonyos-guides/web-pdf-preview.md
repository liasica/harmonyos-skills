---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-pdf-preview
title: 使用Web组件的PDF文档预览能力
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 处理网页内容 > 使用Web组件的PDF文档预览能力
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f0ceb3fdf082d2ed814c8f6cbf415748f13550320644c78c8fbe5a2c353de990
---

[Web组件](../harmonyos-references/arkts-basic-components-web.md)支持在网页中预览PDF。应用通过[WebOptions](../harmonyos-references/arkts-basic-components-web-i.md#weboptions)的src参数和[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口加载PDF文档。具体场景包括：网络PDF文档、应用沙箱内PDF文档和本地PDF文档。

若涉及网络文档获取，需在module.json5中配置网络访问权限。添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

```
1. "requestPermissions":[
2. {
3. "name" : "ohos.permission.INTERNET"
4. }
5. ],
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ProcessWebPageCont/entry/src/main/module.json5#L66-L74)

## 通过不同的方式加载PDF文档

在下面的示例中，Web组件创建时指定默认加载的网络PDF文档https://www.example.com/test.pdf。使用时需替换为真实的可访问URL。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({
11. src:
12. 'https://www.example.com/test.pdf',                     // 方式一 加载网络PDF文档
13. // this.getUIContext().getHostContext()!.filesDir + '/test.pdf', // 方式二 加载本地应用沙箱内PDF文档
14. // 'resource://rawfile/test.pdf',                         // 方式三 本地PDF文档 (格式一)
15. // $rawfile('test.pdf'),                                 // 方式三 本地PDF文档 (格式二)
16. controller: this.controller
17. })
18. .domStorageAccess(true)
19. }
20. }
21. }
```

[PreviewPDF.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ProcessWebPageCont/entry/src/main/ets/pages/PreviewPDF.ets#L16-L38)

PDF预览页面会根据用户操作使用window.localStorage记录侧导航栏的展开状态，因此需要开启文档对象模型存储[domStorageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#domstorageaccess)权限:

```
1. Web().domStorageAccess(true)
```

在创建[Web组件](../harmonyos-references/arkts-basic-components-web.md)时，指定默认加载的PDF文档。默认PDF文档加载完成后，若需变更Web组件显示的PDF文档，通过调用[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口加载指定的PDF文档。[WebOptions](../harmonyos-references/arkts-basic-components-web-i.md#weboptions)的第一个参数变量src不能通过状态变量（例如：[@State](arkts-state.md)）动态更改地址，如需更改，请通过[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)重新加载。

包含三种PDF文档加载预览场景：

* 预览加载网络PDF文档。

  ```
  1. Web({
  2. src: "https://www.example.com/test.pdf",
  3. controller: this.controller
  4. })
  5. .domStorageAccess(true)
  ```
* 预览加载应用沙箱内PDF文档需要开启文件系统的[fileAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#fileaccess)权限。

  ```
  1. Web({
  2. src: this.getUIContext().getHostContext()!.filesDir + "/test.pdf",
  3. controller: this.controller
  4. })
  5. .domStorageAccess(true)
  6. .fileAccess(true)
  ```
* 预览加载本地PDF文档。

  ```
  1. Web({
  2. src: "resource://rawfile/test.pdf",            // 格式一 加载本地PDF文档
  3. // src: $rawfile('test.pdf'),                  // 格式二 加载本地PDF文档
  4. controller: this.controller
  5. })
  6. .domStorageAccess(true)
  ```

## 通过配置PDF文件预览参数，控制打开预览时页面状态

当前支持如下参数:

| 语法 | 描述 |
| --- | --- |
| nameddest=destination | 指定PDF文档中的命名目标。 |
| page=pagenum | 使用整数指定文档中的页码，文档第一页的pagenum值为1。 |
| zoom=scale,left,top | 使用浮点或整数值设置缩放和滚动系数。例如：缩放值100表示缩放值为100%。 向左和向上滚动值位于坐标系中，0,0 表示可见页面的左上角，无论文档如何旋转。scale为必选参数。left,top为非必选参数。 |
| toolbar=1 or 0 | 1表示打开顶部工具栏。0表示关闭顶部工具栏。 |
| navpanes=1 or 0 | 1表示打开侧边导航窗格。0表示关闭侧边导航窗格。 |
| pdfbackgroundcolor=color | 从HarmonyOS 6.0系统版本开始，支持指定PDF文档背景色，color为标准的六位十六进制RGB（取值范围为000000~ffffff，例如白色为：ffffff）。 |

URL示例:

```
1. https://example.com/test.pdf#nameddest=Chapter6
2. https://example.com/test.pdf#page=3
3. https://example.com/test.pdf#zoom=50
4. https://example.com/test.pdf#page=3&zoom=200,250,100
5. https://example.com/test.pdf#toolbar=0
6. https://example.com/test.pdf#navpanes=0
7. https://example.com/test.pdf#pdfbackgroundcolor=ffffff
```

## PDF文档预览回调功能

从API version 20开始，PDF文档预览支持两种回调功能：加载成功/失败回调和滚动到底部事件回调。

在下面的示例中，Web组件创建时指定默认加载的网络PDF文档https://www.example.com/test.pdf。使用时需替换为真实的可访问URL。

* 加载成功/失败回调。

  ```
  1. Web({
  2. src: 'https://www.example.com/test.pdf',
  3. controller: this.controller
  4. })
  5. .onPdfLoadEvent(
  6. (eventInfo: OnPdfLoadEvent) => {
  7. console.info(`Load event callback called. url: ${eventInfo.url}, result: ${eventInfo.result}.`)
  8. }
  9. )
  ```
* 滚动到底部事件回调。

  ```
  1. Web({
  2. src: 'https://www.example.com/test.pdf',
  3. controller: this.controller
  4. })
  5. .onPdfScrollAtBottom(
  6. (eventInfo: OnPdfScrollEvent) => {
  7. console.info(`Scroll at bottom callback called. url: ${eventInfo.url}.`)
  8. }
  9. )
  ```

## 示例代码

* [Web组件预览PDF文件](https://gitcode.com/harmonyos_samples/web-pdfviewer)
