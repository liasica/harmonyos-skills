---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-predictor
title: 加速Web页面的访问
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页加载与浏览记录 > 加速Web页面的访问
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:00+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9a1bc6e4525a6c2f13dffdb6849b5f6f24df2e1053b5c82952298c1141560a5e
---

当Web页面加载缓慢时，可以使用预连接、预加载和预获取POST请求的能力加速Web页面的访问。

针对Web页面加载性能优化的详细内容请参考[Web页面加载优化性能指导](../best-practices/bpta-web-develop-optimization.md#section128761465256)。

## 预解析和预连接

此方法可以针对域名级进行优化，通过[prepareForPageLoad()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prepareforpageload10)来预解析或者预连接将要加载的页面。该方式仅对url进行DNS解析以及建立tcp连接，但不会获取主资源子资源。

在下面的示例中，在Web组件的onAppear中对要加载的页面进行预连接。

```
1. import { webview } from '@kit.ArkWeb';
2. // ...

4. @Entry
5. @Component
6. struct WebComponent {
7. webviewController: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('loadData')
12. .onClick(() => {
13. if (this.webviewController.accessBackward()) {
14. this.webviewController.backward();
15. }
16. })
17. Web({ src: 'https://www.example.com/', controller: this.webviewController })
18. .onAppear(() => {
19. // 指定第二个参数为true，代表要进行预连接，如果为false该接口只会对网址进行dns预解析
20. // 第三个参数为要预连接socket的个数。最多允许6个。
21. webview.WebviewController.prepareForPageLoad('https://www.example.com/', true, 2);
22. })
23. }
24. }
25. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry1/src/main/ets/pages/Index.ets#L15-L45)

也可以通过[initializeWebEngine()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#initializewebengine)来提前初始化内核，然后在初始化内核后调用[prepareForPageLoad()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prepareforpageload10)对即将要加载的页面进行预解析、预连接。这种方式适合提前对首页进行预解析、预连接。

在下面的示例中，Ability的onCreate中提前初始化Web内核并对首页进行预连接。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info("EntryAbility onCreate");
8. webview.WebviewController.initializeWebEngine();
9. // 预连接时，需要将'https://www.example.com'替换成真实要访问的网站地址。
10. webview.WebviewController.prepareForPageLoad("https://www.example.com/", true, 2);
11. AppStorage.setOrCreate("abilityWant", want);
12. console.info("EntryAbility onCreate done");
13. }
14. }
```

## 预加载

此方法可针对资源级进行优化。如果能够预测到Web组件将要加载的页面或者即将要跳转的页面。可以通过[prefetchPage()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchpage10)来预加载即将要加载的页面。

预加载会提前下载页面所需的资源，包括主资源子资源，避免阻塞页面渲染。但不会执行网页JavaScript代码。预加载是WebviewController的实例方法，需要一个已经关联好Web组件的WebviewController实例。

在下面的示例中，在onPageEnd的时候触发下一个要访问的页面的预加载。

```
1. import { webview } from '@kit.ArkWeb';
2. // ...
3. @Entry
4. @Component
5. struct WebComponent {
6. webviewController: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'https://www.example.com/', controller: this.webviewController })
11. .onPageEnd(() => {
12. // 预加载https://www.iana.org/help/example-domains。
13. this.webviewController.prefetchPage('https://www.iana.org/help/example-domains');
14. })
15. }
16. }
17. }
```

[Prefetching.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry2/src/main/ets/pages/Prefetching.ets#L15-L37)

## 预获取POST请求

此方法可以针对请求级进行优化。可以通过[prefetchResource()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchresource12)预获取将要加载页面中的POST请求。在页面加载结束时，可以通过[clearPrefetchedResource()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#clearprefetchedresource12)清除后续不再使用的预获取资源缓存。

以下示例，在Web组件onAppear中，对要加载页面中的POST请求进行预获取。在onPageEnd中，可以清除预获取的POST请求缓存。

```
1. import { webview } from '@kit.ArkWeb';
2. // ...
3. @Entry
4. @Component
5. struct WebComponent {
6. webviewController: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'https://www.example.com/', controller: this.webviewController })
11. .onAppear(() => {
12. // 预获取时，需要将'https://www.example1.com/post?e=f&g=h'替换成真实要访问的网站地址。
13. webview.WebviewController.prefetchResource(
14. {
15. url: 'https://www.example1.com/post?e=f&g=h',
16. method: 'POST',
17. formData: 'a=x&b=y',
18. },
19. [{
20. headerKey: 'c',
21. headerValue: 'z',
22. },],
23. 'KeyX', 500);
24. })
25. .onPageEnd(() => {
26. // 清除后续不再使用的预获取资源缓存。
27. webview.WebviewController.clearPrefetchedResource(['KeyX',]);
28. })
29. }
30. }
31. }
```

[PrefetchingAPOSTRequest\_one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry2/src/main/ets/pages/PrefetchingAPOSTRequest_one.ets#L15-L51)

如果能够预测到Web组件将要加载页面或者即将要跳转页面中的POST请求。可以通过[prefetchResource()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchresource12)预获取即将要加载页面的POST请求。

以下示例，在onPageEnd中，触发预获取一个要访问页面的POST请求。

```
1. import { webview } from '@kit.ArkWeb';
2. // ...
3. @Entry
4. @Component
5. struct WebComponent {
6. webviewController: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'https://www.example.com/', controller: this.webviewController })
11. .onPageEnd(() => {
12. // 预获取时，需要将'https://www.example1.com/post?e=f&g=h'替换成真实要访问的网站地址。
13. webview.WebviewController.prefetchResource(
14. {
15. url: 'https://www.example1.com/post?e=f&g=h',
16. method: 'POST',
17. formData: 'a=x&b=y',
18. },
19. [{
20. headerKey: 'c',
21. headerValue: 'z',
22. },],
23. 'KeyX', 500);
24. })
25. }
26. }
27. }
```

[PrefetchingAPOSTRequest\_three.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry2/src/main/ets/pages/PrefetchingAPOSTRequest_three.ets#L15-L47)

也可以通过[initializeWebEngine()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#initializewebengine)提前初始化内核，然后在初始化内核后调用[prefetchResource()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchresource12)预获取将要加载页面中的POST请求。这种方式适合提前预获取首页的POST请求。

以下示例，在Ability的onCreate中，提前初始化Web内核并预获取首页的POST请求。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info("EntryAbility onCreate");
8. webview.WebviewController.initializeWebEngine();
9. // 预获取时，需要将"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
10. webview.WebviewController.prefetchResource(
11. {
12. url: "https://www.example1.com/post?e=f&g=h",
13. method: "POST",
14. formData: "a=x&b=y",
15. },
16. [{
17. headerKey: "c",
18. headerValue: "z",
19. },],
20. "KeyX", 500);
21. AppStorage.setOrCreate("abilityWant", want);
22. console.info("EntryAbility onCreate done");
23. }
24. }
```

## 预编译生成编译缓存

可以通过[precompileJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#precompilejavascript12)在页面加载前提前生成脚本文件的编译缓存。

推荐配合动态组件使用，使用离线的Web组件用于生成字节码缓存，并在适当的时机加载业务用Web组件使用这些字节码缓存。下方是代码示例：

1. 首先，在EntryAbility中将[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)存到[localStorage](arkts-localstorage.md)中。

   ```
   1. // EntryAbility.ets
   2. import { UIAbility } from '@kit.AbilityKit';
   3. import { window } from '@kit.ArkUI';

   5. const localStorage: LocalStorage = new LocalStorage('uiContext');

   7. export default class EntryAbility extends UIAbility {
   8. storage: LocalStorage = localStorage;

   10. onWindowStageCreate(windowStage: window.WindowStage) {
   11. windowStage.loadContent('pages/Index', this.storage, (err, data) => {
   12. if (err.code) {
   13. return;
   14. }

   16. this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
   17. });
   18. }
   19. }
   ```
2. 编写动态组件所需基础代码。

   ```
   1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

   3. export interface BuilderData {
   4. url: string;
   5. controller: WebviewController;
   6. context: UIContext;
   7. }

   9. let storage : LocalStorage | undefined = undefined;

   11. export class NodeControllerImpl extends NodeController {
   12. private rootNode: BuilderNode<BuilderData[]> | null = null;
   13. private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;

   15. constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>, context: UIContext) {
   16. storage = context.getSharedLocalStorage();
   17. super();
   18. this.wrappedBuilder = wrappedBuilder;
   19. }

   21. makeNode(): FrameNode | null {
   22. if (this.rootNode != null) {
   23. return this.rootNode.getFrameNode();
   24. }
   25. return null;
   26. }

   28. initWeb(url: string, controller: WebviewController) {
   29. if(this.rootNode != null) {
   30. return;
   31. }

   33. const uiContext: UIContext = storage!.get<UIContext>('uiContext') as UIContext;
   34. if (!uiContext) {
   35. return;
   36. }
   37. this.rootNode = new BuilderNode(uiContext);
   38. this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
   39. }
   40. }

   42. export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
   43. const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
   44. baseNode.initWeb(data.url, data.controller);
   45. return baseNode;
   46. }
   ```

   [DynamicComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry3/src/main/ets/pages/DynamicComponent.ets#L15-L63)
3. 编写用于生成字节码缓存的组件，本例中的本地JavaScript资源内容通过文件读取接口读取rawfile目录下的本地文件。

   ```
   1. import { BuilderData } from './DynamicComponent';
   2. import { Config, configs } from './PrecompileConfig';

   4. @Builder
   5. function webBuilder(data: BuilderData) {
   6. Web({ src: data.url, controller: data.controller })
   7. .onControllerAttached(() => {
   8. precompile(data.controller, configs, data.context);
   9. })
   10. .fileAccess(true)
   11. }

   13. export const precompileWebview = wrapBuilder<BuilderData[]>(webBuilder);

   15. export const precompile = async (controller: WebviewController, configs: Array<Config>, context: UIContext) => {
   16. for (const config of configs) {
   17. let content = await readRawFile(config.localPath, context);

   19. try {
   20. controller.precompileJavaScript(config.url, content, config.options)
   21. .then(errCode => {
   22. console.error('precompile successfully! ' + errCode);
   23. }).catch((errCode: number) => {
   24. console.error('precompile failed. ' + errCode);
   25. });
   26. } catch (err) {
   27. console.error('precompile failed. ' + err.code + ' ' + err.message);
   28. }
   29. }
   30. }

   32. async function readRawFile(path: string, context: UIContext) {
   33. try {
   34. return await context.getHostContext()!.resourceManager.getRawFileContent(path);
   35. } catch (err) {
   36. return new Uint8Array(0);
   37. }
   38. }
   ```

   [PrecompileWebview.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry3/src/main/ets/pages/PrecompileWebview.ets#L16-L56)

   JavaScript资源的获取方式也可通过[网络请求](../harmonyos-references/js-apis-http.md)的方式获取，但此方法获取到的HTTP响应头非标准HTTP响应头格式，需额外将响应头转换成标准HTTP响应头格式后使用。如通过网络请求获取到的响应头是e-tag，则需要将其转换成E-Tag后使用。
4. 编写业务用组件代码。

   ```
   1. import { BuilderData } from './DynamicComponent';

   3. @Builder
   4. function webBuilder(data: BuilderData) {
   5. // 此处组件可根据业务需要自行扩展
   6. Web({ src: data.url, controller: data.controller })
   7. .cacheMode(CacheMode.Default)
   8. }

   10. export const businessWebview = wrapBuilder<BuilderData[]>(webBuilder);
   ```

   [BusinessWebview.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry3/src/main/ets/pages/BusinessWebview.ets#L16-L28)
5. 编写资源配置信息。

   ```
   1. import { webview } from '@kit.ArkWeb'

   3. export interface Config {
   4. url:  string,
   5. localPath: string, // 本地资源路径
   6. options: webview.CacheOptions
   7. }

   9. export let configs: Config[] = [
   10. {
   11. url: 'https://www.example.com/example.js',
   12. localPath: 'example.js',
   13. options: {
   14. responseHeaders: [
   15. { headerKey: 'E-Tag', headerValue: 'aWO42N9P9dG/5xqYQCxsx+vDOoU='},
   16. { headerKey: 'Last-Modified', headerValue: 'Wed, 21 Mar 2025 10:38:41 GMT'}
   17. ]
   18. }
   19. }
   20. ]
   ```

   [PrecompileConfig.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry3/src/main/ets/pages/PrecompileConfig.ets#L16-L38)
6. 在页面中使用。

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import { NodeController } from '@kit.ArkUI';
   3. import { createNode } from './DynamicComponent';
   4. import { precompileWebview } from './PrecompileWebview';
   5. import { businessWebview } from './BusinessWebview';

   7. @Entry
   8. @Component
   9. struct Index {
   10. @State precompileNode: NodeController | undefined = undefined;
   11. precompileController: webview.WebviewController = new webview.WebviewController();

   13. @State businessNode: NodeController | undefined = undefined;
   14. businessController: webview.WebviewController = new webview.WebviewController();

   16. aboutToAppear(): void {
   17. // 初始化用于注入本地资源的Web组件
   18. this.precompileNode = createNode(precompileWebview,
   19. { url: 'https://www.example.com/empty.html', controller: this.precompileController, context: this.getUIContext()});
   20. }

   22. build() {
   23. Column() {
   24. // 在适当的时机加载业务用Web组件，本例以Button点击触发为例
   25. Button('加载页面')
   26. .onClick(() => {
   27. this.businessNode = createNode(businessWebview, {
   28. url: 'https://www.example.com/business.html',
   29. controller: this.businessController,
   30. context: this.getUIContext()
   31. });
   32. })
   33. // 用于业务的Web组件
   34. NodeContainer(this.businessNode);
   35. }
   36. }
   37. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry3/src/main/ets/pages/Index.ets#L16-L56)

当需要更新本地已经生成的编译字节码时，修改cacheOptions参数中responseHeaders中的E-Tag或Last-Modified响应头对应的值，再次调用接口即可。

## 离线资源免拦截注入

可以通过[injectOfflineResources()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#injectofflineresources12)在页面加载前提前将图片、样式表或脚本资源注入到应用的内存缓存中。

推荐配合动态组件使用，使用离线的Web组件用于将资源注入到内核的内存缓存中，并在适当的时机加载业务用Web组件使用这些资源。下方是代码示例：

1. 首先，在EntryAbility中将[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)存到[localStorage](arkts-localstorage.md)中。

   ```
   1. // EntryAbility.ets
   2. import { UIAbility } from '@kit.AbilityKit';
   3. import { window } from '@kit.ArkUI';

   5. const localStorage: LocalStorage = new LocalStorage('uiContext');

   7. export default class EntryAbility extends UIAbility {
   8. storage: LocalStorage = localStorage;

   10. onWindowStageCreate(windowStage: window.WindowStage) {
   11. windowStage.loadContent('pages/Index', this.storage, (err, data) => {
   12. if (err.code) {
   13. return;
   14. }

   16. this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
   17. });
   18. }
   19. }
   ```
2. 编写动态组件所需基础代码。

   ```
   1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

   3. export interface BuilderData {
   4. url: string;
   5. controller: WebviewController;
   6. context: UIContext;
   7. }

   9. let storage : LocalStorage | undefined = undefined;

   11. export class NodeControllerImpl extends NodeController {
   12. private rootNode: BuilderNode<BuilderData[]> | null = null;
   13. private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;

   15. constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>,  context: UIContext) {
   16. storage = context.getSharedLocalStorage();
   17. super();
   18. this.wrappedBuilder = wrappedBuilder;
   19. }

   21. makeNode(): FrameNode | null {
   22. if (this.rootNode != null) {
   23. return this.rootNode.getFrameNode();
   24. }
   25. return null;
   26. }

   28. initWeb(url: string, controller: WebviewController) {
   29. if(this.rootNode != null) {
   30. return;
   31. }

   33. const uiContext: UIContext = storage!.get<UIContext>('uiContext') as UIContext;
   34. if (!uiContext) {
   35. return;
   36. }
   37. this.rootNode = new BuilderNode(uiContext);
   38. this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
   39. }
   40. }

   42. export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
   43. const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
   44. baseNode.initWeb(data.url, data.controller);
   45. return baseNode;
   46. }
   ```

   [DynamicComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry4/src/main/ets/pages/DynamicComponent.ets#L15-L63)
3. 编写用于注入资源的组件代码，本例中的本地资源内容通过文件读取接口读取rawfile目录下的本地文件。

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import { resourceConfigs } from './Resource';
   3. import { BuilderData } from './DynamicComponent';

   5. @Builder
   6. function webBuilder(data: BuilderData) {
   7. Web({ src: data.url, controller: data.controller })
   8. .onControllerAttached(async () => {
   9. try {
   10. data.controller.injectOfflineResources(await getData (data.context));
   11. } catch (err) {
   12. console.error('error: ' + err.code + ' ' + err.message);
   13. }
   14. })
   15. .fileAccess(true)
   16. }

   18. export const injectWebview = wrapBuilder<BuilderData[]>(webBuilder);

   20. export async function getData(context: UIContext) {
   21. const resourceMapArr: webview.OfflineResourceMap[] = [];

   23. // 读取配置，从rawfile目录中读取文件内容
   24. for (let config of resourceConfigs) {
   25. let buf: Uint8Array = new Uint8Array(0);
   26. if (config.localPath) {
   27. buf = await readRawFile(config.localPath, context);
   28. }

   30. resourceMapArr.push({
   31. urlList: config.urlList,
   32. resource: buf,
   33. responseHeaders: config.responseHeaders,
   34. type: config.type,
   35. })
   36. }

   38. return resourceMapArr;
   39. }

   41. export async function readRawFile(url: string, context: UIContext) {
   42. try {
   43. return await context.getHostContext()!.resourceManager.getRawFileContent(url);
   44. } catch (err) {
   45. return new Uint8Array(0);
   46. }
   47. }
   ```

   [InjectWebview.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry4/src/main/ets/pages/InjectWebview.ets#L16-L65)
4. 编写业务用组件代码。

   ```
   1. import { BuilderData } from './DynamicComponent';

   3. @Builder
   4. function webBuilder(data: BuilderData) {
   5. // 此处组件可根据业务需要自行扩展
   6. Web({ src: data.url, controller: data.controller })
   7. .cacheMode(CacheMode.Default)
   8. }

   10. export const businessWebview = wrapBuilder<BuilderData[]>(webBuilder);
   ```

   [BusinessWebview.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry4/src/main/ets/pages/BusinessWebview.ets#L15-L27)
5. 编写资源配置信息。

   ```
   1. import { webview } from '@kit.ArkWeb';

   3. export interface ResourceConfig {
   4. urlList: Array<string>,
   5. type: webview.OfflineResourceType,
   6. responseHeaders: Array<Header>,
   7. localPath: string, // 本地资源存放在rawfile目录下的路径
   8. }

   10. export const resourceConfigs: ResourceConfig[] = [
   11. {
   12. localPath: 'example.png',
   13. urlList: [
   14. 'https://www.example.com/',
   15. 'https://www.example.com/path1/example.png',
   16. 'https://www.example.com/path2/example.png',
   17. ],
   18. type: webview.OfflineResourceType.IMAGE,
   19. responseHeaders: [
   20. { headerKey: 'Cache-Control', headerValue: 'max-age=1000' },
   21. { headerKey: 'Content-Type', headerValue: 'image/png' },
   22. ]
   23. },
   24. {
   25. localPath: 'example.js',
   26. urlList: [ // 仅提供一个url，这个url既作为资源的源，也作为资源的网络请求地址
   27. 'https://www.example.com/example.js',
   28. ],
   29. type: webview.OfflineResourceType.CLASSIC_JS,
   30. responseHeaders: [
   31. // 以<script crossorigin='anonymous' />方式使用，提供额外的响应头
   32. { headerKey: 'Cross-Origin', headerValue:'anonymous' }
   33. ]
   34. },
   35. ];
   ```

   [Resource.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry4/src/main/ets/pages/Resource.ets#L16-L53)
6. 在页面中使用。

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import { NodeController } from '@kit.ArkUI';
   3. import { createNode } from './DynamicComponent';
   4. import { injectWebview } from './InjectWebview';
   5. import { businessWebview } from './BusinessWebview';

   7. @Entry
   8. @Component
   9. struct Index {
   10. @State injectNode: NodeController | undefined = undefined;
   11. injectController: webview.WebviewController = new webview.WebviewController();

   13. @State businessNode: NodeController | undefined = undefined;
   14. businessController: webview.WebviewController = new webview.WebviewController();

   16. aboutToAppear(): void {
   17. // 初始化用于注入本地资源的Web组件, 提供一个空的html页面作为url即可
   18. this.injectNode = createNode(injectWebview,
   19. { url: 'https://www.example.com/empty.html', controller: this.injectController, context: this.getUIContext()});
   20. }

   22. build() {
   23. Column() {
   24. // 在适当的时机加载业务用Web组件，本例以Button点击触发为例
   25. Button('加载页面')
   26. .onClick(() => {
   27. this.businessNode = createNode(businessWebview, {
   28. url: 'https://www.example.com/business.html',
   29. controller: this.businessController,
   30. context: this.getUIContext()
   31. });
   32. })
   33. // 用于业务的Web组件
   34. NodeContainer(this.businessNode);
   35. }
   36. }
   37. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/AcceleratePageAccess/entry4/src/main/ets/pages/Index.ets#L16-L55)
7. 加载的HTML网页示例。

   ```
   1. <!DOCTYPE html>
   2. <html lang="en">
   3. <head></head>
   4. <body>
   5. <img src="https://www.example.com/path1/request.png" />
   6. <img src="https://www.example.com/path2/request.png" />
   7. <script src="https://www.example.com/example.js" crossorigin="anonymous"></script>
   8. </body>
   9. </html>
   ```
