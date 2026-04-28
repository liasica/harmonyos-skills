---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-cookie-and-data-storage-mgmt
title: 管理Cookie及数据存储
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 设置基本属性和事件 > 管理Cookie及数据存储
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eebf6a876326892d08c049f59dc31fac1c355541af4663c2556109e3a774453e
---

Cookie是服务端生成并发送到客户端的数据。客户端持有Cookie，便于服务端快速识别身份和状态。

当Cookie的SameSite属性未指定时，默认值为SameSite=Lax。这种设置下，Cookie仅在用户导航到其源站点时发送，不会在跨站请求中发送。

## Cookie管理

Web组件提供[WebCookieManager](../harmonyos-references/arkts-apis-webview-webcookiemanager.md)类来管理Cookie信息。Cookie信息存储在应用沙箱路径下/proc/{pid}/root/data/storage/el2/base/cache/web/Cookies的文件中。

下面以[configCookieSync()](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookiesync11)接口为例，为“www.example.com”设置单个Cookie的值“value=test”。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('configCookieSync')
12. .onClick(() => {
13. try {
14. webview.WebCookieManager.configCookieSync('https://www.example.com', 'value=test');
15. } catch (error) {
16. console.error(
17. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller });
21. }
22. }
23. }
```

[CookieManagement.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsTwo/entry/src/main/ets/pages/CookieManagement.ets#L16-L40)

从API version 22开始，开发者可以通过[setLazyInitializeWebEngine()](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#setlazyinitializewebengine22)，为“www.example.com”设置单个Cookie的值“value=test”时跳过初始化ArkWeb内核，以节省[configCookieSync()](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookiesync11)接口耗时。其他Cookie的相关功能及使用，请参考[WebCookieManager()](../harmonyos-references/arkts-apis-webview-webcookiemanager.md)接口文档。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. webview.WebCookieManager.setLazyInitializeWebEngine(true);

6. @Entry
7. @Component
8. struct WebComponent {
9. controller: webview.WebviewController = new webview.WebviewController();

11. aboutToAppear(): void {
12. try {
13. webview.WebCookieManager.configCookieSync('https://www.example.com', 'value=test');
14. } catch (error) {
15. console.error(
16. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
17. }
18. }

20. build() {
21. Column() {
22. Web({ src: 'www.example.com', controller: this.controller })
23. }
24. }
25. }
```

[CookieManagement\_LazyInitializeWebEngine.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsTwo/entry/src/main/ets/pages/CookieManagement_LazyInitializeWebEngine.ets#L16-L42)

说明

Cookie每30s周期性保存到磁盘中，也可以使用接口[saveCookieAsync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#savecookieasync)进行强制落盘（PC/2in1和Tablet设备不会持久化session cookie，即使调用saveCookieAsync，也不会将session cookie写入磁盘）。

## 缓存与存储管理

在访问网站时，网络资源请求通常需要较长的时间。开发者可以通过Cache和Dom Storage等手段将资源保存到本地，以提高访问同一网站的速度。

### Cache

使用[cacheMode()](../harmonyos-references/arkts-basic-components-web-attributes.md#cachemode)配置页面资源的缓存模式，Web组件为开发者提供四种缓存模式，分别为：

* Default：优先使用未过期的缓存。如果缓存不存在，则从网络获取。
* None：加载资源使用缓存。如果缓存中无该资源，则从网络中获取。
* Online：加载资源不使用缓存。全部从网络中获取。
* Only：只从缓存中加载资源。

在下面的示例中，缓存设置为None模式。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. @State mode: CacheMode = CacheMode.None;
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .cacheMode(this.mode)
13. }
14. }
15. }
```

[Cache\_one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsTwo/entry/src/main/ets/pages/Cache_one.ets#L16-L32)

为了获取最新资源，开发者可以通过[removeCache()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#removecache)接口清除已经缓存的资源，示例代码如下：

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. @State mode: CacheMode = CacheMode.None;
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Button('removeCache')
13. .onClick(() => {
14. try {
15. // 设置为true时同时清除rom和ram中的缓存，设置为false时只清除ram中的缓存
16. this.controller.removeCache(true);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. });
21. Web({ src: 'www.example.com', controller: this.controller })
22. .cacheMode(this.mode)
23. }
24. }
25. }
```

[Cache\_two.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsTwo/entry/src/main/ets/pages/Cache_two.ets#L16-L42)

### DOM Storage

DOM Storage包含了Session Storage和Local Storage两类。Session Storage为临时数据，其存储与释放跟随会话生命周期；Local Storage为持久化数据，保存在应用目录下。两者的数据均通过Key-Value的形式存储，在访问需要客户端存储的页面时使用。开发者可以通过Web组件的属性接口[domStorageAccess()](../harmonyos-references/arkts-basic-components-web-attributes.md#domstorageaccess)进行使能配置，示例如下：

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .domStorageAccess(true)
12. }
13. }
14. }
```

[DomStorage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsTwo/entry/src/main/ets/pages/DomStorage.ets#L16-L31)

## 常见问题

### ArkWeb组件对静态资源文件缓存的大小限制是多少？

ArkWeb对于单个应用静态资源缓存的大小限制是100M。
