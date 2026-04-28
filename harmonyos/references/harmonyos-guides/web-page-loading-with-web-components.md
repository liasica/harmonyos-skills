---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-page-loading-with-web-components
title: 使用Web组件加载页面
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页加载与浏览记录 > 使用Web组件加载页面
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:70bf081f58117e715626e7c5fab405aad81644decc3ea89469f7fa6094408a7b
---

页面加载是Web组件的基本功能。根据页面加载数据来源可以分为三种常用场景，包括加载网络页面、加载本地页面、加载HTML格式的富文本数据。

页面加载过程中，若涉及网络资源获取，请在module.json5中配置网络访问权限，添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

```
1. "requestPermissions":[
2. {
3. "name" : "ohos.permission.INTERNET"
4. }
5. ]
```

## 加载网络页面

开发者可以在Web组件创建时，指定默认加载的网络页面。在默认页面加载完成后，如果需要变更此Web组件显示的网络页面，可以通过调用[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口加载指定的网页。[Web组件](../harmonyos-references/arkts-basic-components-web.md)的第一个参数变量src不能通过状态变量（例如：[@State](arkts-state.md)）动态更改地址，如需更改，请通过[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)重新加载。

在下面的示例中，在Web组件加载完“www.example.com”页面后，开发者可通过loadUrl接口将此Web组件显示页面变更为“www.example1.com”。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('loadUrl')
12. .onClick(() => {
13. try {
14. // 点击按钮时，通过loadUrl，跳转到www.example1.com
15. this.controller.loadUrl('www.example1.com');
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. // 组件创建时，加载www.example.com
21. Web({ src: 'www.example.com', controller: this.controller });
22. }
23. }
24. }
```

[LoadingWebPages.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/LoadPages/entry/src/main/ets/pages/LoadingWebPages.ets#L16-L41)

## 加载本地页面

为了在启动、跳转、弱网等场景下减少用户等待感知，同时为动态内容加载争取时间，可以加载本地页面优化用户体验。

在下面的示例中展示加载本地页面文件的方法：

将本地页面文件放在应用的rawfile目录下，开发者可以在Web组件创建的时候指定默认加载的本地页面，并且加载完成后可通过调用[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口变更当前Web组件的页面。

加载本地html文件时引用本地css样式文件可以通过以下方法实现。

```
1. <link rel="stylesheet" href="resource://rawfile/xxx.css">
2. <link rel="stylesheet" href="file:///data/storage/el2/base/haps/entry/cache/xxx.css">// 加载沙箱路径下的本地css文件。
```

* 将资源文件放置在应用的resources/rawfile目录下。

  **图1** 资源文件路径

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/nBkTsHaPQDuHpeS05kcClQ/zh-cn_image_0000002583438271.png?HW-CC-KV=V1&HW-CC-Date=20260427T233804Z&HW-CC-Expire=86400&HW-CC-Sign=3C6CC915D866AB6B14E7499B7C4EC418ACD7229297BB8929324A21810902B08B)
* 应用侧代码。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();

  9. build() {
  10. Column() {
  11. Button('loadUrl')
  12. .onClick(() => {
  13. try {
  14. // 点击按钮时，通过loadUrl，跳转到local1.html
  15. this.controller.loadUrl($rawfile('local1.html'));
  16. } catch (error) {
  17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  18. }
  19. })
  20. // 组件创建时，通过$rawfile加载本地文件local.html
  21. Web({ src: $rawfile('local.html'), controller: this.controller });
  22. }
  23. }
  24. }
  ```

  [LoadingLocalPages.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/LoadPages/entry/src/main/ets/pages/LoadingLocalPages.ets#L17-L42)
* local.html页面代码。

  ```
  1. <!-- local.html -->
  2. <!DOCTYPE html>
  3. <html>
  4. <body>
  5. <p>Hello World</p>
  6. </body>
  7. </html>
  ```
* local1.html页面代码。

  ```
  1. <!-- local1.html -->
  2. <!DOCTYPE html>
  3. <html>
  4. <body>
  5. <p>This is local1 page</p>
  6. </body>
  7. </html>
  ```

加载沙箱路径下的本地页面文件。

1. 通过构造的单例对象GlobalContext获取沙箱路径。需要开启应用中文件系统的访问[fileAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#fileaccess)权限。

   ```
   1. export class GlobalContext {
   2. private constructor() {}
   3. private static instance: GlobalContext;
   4. private _objects = new Map<string, Object>();

   6. public static getContext(): GlobalContext {
   7. if (!GlobalContext.instance) {
   8. GlobalContext.instance = new GlobalContext();
   9. }
   10. return GlobalContext.instance;
   11. }

   13. getObject(value: string): Object | undefined {
   14. return this._objects.get(value);
   15. }

   17. setObject(key: string, objectClass: Object): void {
   18. this._objects.set(key, objectClass);
   19. }
   20. }
   ```

   [GlobalContext.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/LoadPages/entry/src/main/ets/pages/GlobalContext.ets#L16-L37)

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import { GlobalContext } from './GlobalContext';

   4. let url = 'file://' + GlobalContext.getContext().getObject('filesDir') + '/index.html';

   6. @Entry
   7. @Component
   8. struct WebComponent {
   9. controller: webview.WebviewController = new webview.WebviewController();

   11. build() {
   12. Column() {
   13. // ···
   14. // 加载沙箱路径文件。
   15. Web({ src: url, controller: this.controller })
   16. .fileAccess(true);
   17. }
   18. }
   19. }
   ```

   [LoadLocalPageFileInSandboxPath\_one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/LoadPages/entry/src/main/ets/pages/LoadLocalPageFileInSandboxPath_one.ets#L16-L38)
2. 修改EntryAbility.ets文件。

   以filesDir为例，获取沙箱路径。若想获取其他路径，请参考[应用文件路径](application-context-stage.md#获取应用文件路径)。

   ```
   1. // xxx.ets
   2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   3. import { webview } from '@kit.ArkWeb';
   4. import { GlobalContext } from '../GlobalContext';

   6. export default class EntryAbility extends UIAbility {
   7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
   8. // 通过在GlobalContext对象上绑定filesDir，可以实现UIAbility组件与UI之间的数据同步。
   9. GlobalContext.getContext().setObject("filesDir", this.context.filesDir);
   10. console.info("Sandbox path is " + GlobalContext.getContext().getObject("filesDir"));
   11. }
   12. }
   ```

   加载的html文件。

   ```
   1. <!-- index.html -->
   2. <!DOCTYPE html>
   3. <html>
   4. <body>
   5. <p>Hello World</p>
   6. </body>
   7. </html>
   ```

## 加载HTML格式的文本数据

Web组件可以通过[loadData()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loaddata)接口实现加载HTML格式的文本数据。当开发者不需要加载整个页面，只需要显示一些页面片段时，可通过此功能来快速加载页面，当加载大量html文件时，需设置第四个参数baseUrl为"data"。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('loadData')
12. .onClick(() => {
13. try {
14. // 点击按钮时，通过loadData，加载HTML格式的文本数据
15. this.controller.loadData(
16. '<html><body bgcolor=\'white\'>Source:<pre>source</pre></body></html>',
17. 'text/html',
18. 'UTF-8'
19. );
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. })
24. // 组件创建时，加载www.example.com
25. Web({ src: 'www.example.com', controller: this.controller })
26. }
27. }
28. }
```

[LoadingHTMLRichTextData.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/LoadPages/entry/src/main/ets/pages/LoadingHTMLRichTextData.ets#L15-L44)

Web组件可以通过data url方式直接加载HTML字符串。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. htmlStr: string = 'data:text/html, <html><body bgcolor=\'white\'>Source:<pre>source</pre></body></html>';

10. build() {
11. Column() {
12. // 组件创建时，加载htmlStr
13. Web({ src: this.htmlStr, controller: this.controller });
14. }
15. }
16. }
```

[LoadLocalPageFileInSandboxPath\_two.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/LoadPages/entry/src/main/ets/pages/LoadLocalPageFileInSandboxPath_two.ets#L15-L32)

## resource协议加载本地资源

resource协议允许访问应用资源目录中的文件。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct ResourceWebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Button('LoadResource')
11. .onClick(() => {
12. try {
13. // 通过resource加载resources/rawfile目录下的index1.html文件。
14. this.controller.loadUrl('resource://rawfile/index1.html');
15. } catch (error) {
16. console.error(`ErrorCode: ${error.code}, Message: ${error.message}`);
17. }
18. })

20. // 组件创建时直接使用resource协议加载资源。
21. Web({ src: 'resource://rawfile/index.html', controller: this.controller });
22. }
23. }
24. }
```

[ResourceLoadPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/LoadPages/entry/src/main/ets/pages/ResourceLoadPage.ets#L15-L40)

在“src\main\resources\rawfile”文件夹下创建index.html：

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <p>Hello World</p>
6. </body>
7. </html>
```

在“src\main\resources\rawfile”文件夹下创建index1.html：

```
1. <!-- index1.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <p>Hello World Again</p>
6. </body>
7. </html>
```
