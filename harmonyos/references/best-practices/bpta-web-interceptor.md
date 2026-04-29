---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-interceptor
title: Web组件拦截能力的使用
breadcrumb: 最佳实践 > 应用框架 > ArkWeb > Web组件拦截能力的使用
category: best-practices
scraped_at: 2026-04-29T14:11:04+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:16924bb81f19d5fb4843262921f68171fb233ba7b3944047879ee533ce4596bc
---

## 概述

[ArkWeb](../harmonyos-guides/web-component-overview.md)（方舟Web）提供的Web组件支持在应用嵌入网页访问功能。在实际使用过程中，网页内的大量图片、视频等静态资源容易造成用户流量消耗过快，同时，嵌入的恶意脚本也会拖慢网页加载速度，影响用户体验。为此，可以利用Web组件的拦截能力，使用本地资源副本替换高频访问的静态资源，并基于黑名单机制拦截恶意脚本的加载，从而有效提升网页加载效率，优化用户体验。

ArkWeb提供了多种拦截能力，使开发者能够监控、修改和记录网络请求及其响应，有助于实现业务功能的自定义与性能提升等。这些能力在拦截时机、拦截范围和拦截效果等方面存在差异，因此适用于不同的开发场景。本文将介绍三种基于Web组件的拦截方案，并提供各方案在典型应用场景中的实例，帮助开发者更好地掌握ArkWeb拦截能力的选择和使用。

## 原理介绍

应用可通过[onLoadIntercept()](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)接口拦截Web组件的页面跳转，或通过[onInterceptRequest()](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)接口和[WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)机制拦截Web组件发起的网络请求。这三种拦截方案存在一定的差异，以下为具体原理和使用场景介绍。

**表1** 三种Web组件的拦截方案

| 使用场景 | 页面跳转控制 | 网络请求拦截 | |
| --- | --- | --- | --- |
| 方案 | onLoadIntercept | onInterceptRequest | WebSchemeHandler |
| 典型应用场景 | * [应用的跳转与拉起](bpta-web-app-jump-and-pull-up.md) * [请求重定向](bpta-web-interceptor.md#section103591931490) * [页面白名单配置](bpta-web-interceptor.md#section1367693510110) | * [本地资源替换](bpta-web-interceptor.md#section29637307122) * [自定义资源加载策略](bpta-web-interceptor.md#section766911191316) * 提示恶意请求 | 除支持onInterceptRequest的应用场景外，还支持：   * [配置公共请求头](bpta-web-interceptor.md#section736313281410) * 跨域请求 * POST请求拦截 |
| 拦截时机 | Web组件加载url之前 | 请求发起前 | |
| 拦截范围 | 页面主URL的请求（包括页面中iframe的导航行为，不包括子资源的请求） | 页面主URL的请求和子资源的请求 | |
| 数据访问能力 | 支持获取请求的URL、是否为主frame等相关信息，具体参考[WebResourceRequest](../harmonyos-references/arkts-basic-components-web-webresourcerequest.md) | | 除支持获取请求的URL、是否为主frame等相关信息外，还支持获取POST请求体和buffer类型数据，具体参考[WebSchemeHandlerRequest](../harmonyos-references/arkts-apis-webview-webschemehandlerrequest.md) |
| 拦截效果 | 可以拦截或放行Web组件发起当前请求 | 可以拦截当前请求并返回自定义响应，或者放行当前请求并返回原始响应 | |

三种拦截方案的不同特性，对应着不同的使用场景。下面将分别提供这三种方案的使用指导，开发者可根据实际应用场景选择合适的拦截方案。

### 方案选择指导

**onLoadIntercept**

**定位**：用于拦截Web组件的URL加载行为，进行页面跳转控制。

**核心用法**：

* **[应用的跳转与拉起](bpta-web-app-jump-and-pull-up.md)**：拦截特定地址的请求，拉起指定应用或跳转其他页面处理，用于实现拦截支付类标签链接跳转到支付应用进行支付，或拦截地址类标签链接跳转到地图类应用进行导航等。

* **[请求重定向](bpta-web-interceptor.md#section103591931490)**：拦截特定地址的请求，并将访问重定向到新的目标地址，用于在域名更换或登录引导时，将用户访问跳转到正确的页面。

* **[页面白名单配置](bpta-web-interceptor.md#section1367693510110)**：配置链接黑名单/白名单，拦截/放行指定URL请求，确保Web组件的请求在信任范围内，用于实现阻止用户访问危险网页等功能。

**使用策略**：相较于其他两种拦截方案，onLoadIntercept的主要目标是拦截页面跳转行为，而非替换请求内容。因此，在需要中断页面跳转的情况下，可选择使用本方案。

**onInterceptRequest**

**定位**：用于拦截Web组件的URL加载行为，进行网络请求拦截。

**核心用法**

* **[本地资源替换](bpta-web-interceptor.md#section29637307122)**：将频繁使用的静态资源缓存至本地，在访问这些资源时，返回本地响应，用于提升页面的加载速度和响应性能。

* **[自定义资源加载策略](bpta-web-interceptor.md#section766911191316)**：拦截特定资源请求（如图片、视频等），在Wi-Fi和移动网络下分别加载高清资源和压缩资源，用于实现数据消耗与用户体验的平衡。
* **提示恶意请求**：拦截已知恶意请求，返回空数据或提示信息作为请求响应，用于阻止恶意脚本的加载。

**使用策略**：onInterceptRequest支持通过文件句柄、Resource资源、ByteBuffer或String的方式替换请求内容，要求开发者一次性提供完整的请求内容。在需要拦截网络请求并向Web组件返回特定响应的业务场景下，可选择本方案。相较于基于WebSchemeHandler的拦截方案，本方案的实现更加轻量。

**WebSchemeHandler**

**定位**：用于拦截Web组件的URL加载行为，进行网络请求拦截。

**核心用法**：

除支持onInterceptRequest的核心用法外，还支持：

* **[配置公共请求头](bpta-web-interceptor.md#section736313281410)**：拦截特定地址的网络请求，注入认证信息后转发给服务端，用于协助服务端识别请求的用户身份并验证其访问权限。
* **跨域请求**：拦截Web组件发起的跨域请求，转发至远端服务器，将跨域请求结果配置到自定义响应中，返回给Web组件，用于解决依赖多元数据交互的Web应用的跨域问题。
* **POST请求拦截**：拦截POST请求，根据请求内容动态生成响应，用于实现表单提交处理等功能。

**使用策略**：相较于基于onInterceptRequest的拦截方案，WebSchemeHandler不仅具备其全部功能，还提供了更灵活的流式处理能力，允许开发者通过ByteBuffer逐步提供请求内容，并且能够获取请求的上传内容，如POST请求的数据。在需要拦截网络请求，获取更多请求内容或进行流式处理等复杂业务场景下，建议采用本方案。

## 基于onLoadIntercept()拦截能力的使用

Web组件在加载URL前会触发[onLoadIntercept()](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)回调，用于判断是否拦截此次请求。基于该回调，可以实现[请求重定向](bpta-web-interceptor.md#section103591931490)或[页面白名单配置](bpta-web-interceptor.md#section1367693510110)功能。

**图1** 基于onLoadIntercept()的请求拦截流程图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/HaRqoWahTa-aTMjWFqjKrA/zh-cn_image_0000002547943201.png?HW-CC-KV=V1&HW-CC-Date=20260429T061102Z&HW-CC-Expire=86400&HW-CC-Sign=7DCB978CF07EA39000A72E0CE7E1F9FA5A695B72DB4A7E8F3D8D3F4A60CD5B72 "点击放大")

### 请求重定向

请求重定向的典型应用是在网站改版或登录状态管理等场景中，将用户访问自动跳转到正确的页面。

**运行效果**

**图2** 请求重定向  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/rbhFB4rDQx6UU05yaCm8Pg/zh-cn_image_0000002522768321.png?HW-CC-KV=V1&HW-CC-Date=20260429T061102Z&HW-CC-Expire=86400&HW-CC-Sign=BB5FEAFAE2CF143898BFAAD3851C0BC4AE6664554D687DD0CF49AF1278FA2E87 "点击放大")

**实现原理**

在Web组件的[onLoadIntercept()](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)回调中获取请求的URL，若URL满足重定向条件，则通过[WebviewController.loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)加载重定向页面。

**开发步骤**

1. 获取请求的URL。

   ```
   1. /**
   2. * Processes the load intercept event
   3. * Returns true if loading should be blocked (redirect performed), false to allow
   4. */
   5. processLoadIntercept(event: OnLoadInterceptEvent): boolean {
   6. const requestUrl = event.data.getRequestUrl();
   7. // ...
   8. }
   ```

   [RedirectRequestModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/RedirectRequestInterceptor/model/RedirectRequestModel.ets#L75-L96)
2. 判断URL是否满足重定向条件。

   ```
   1. /**
   2. * Checks if the URL needs to be intercepted and redirected
   3. */
   4. shouldInterceptUrl(requestUrl: string): boolean {
   5. if (!this.redirectUrl) {
   6. return false;
   7. }
   8. const normalizedRequest = this.normalizeUrl(requestUrl);
   9. const normalizedRedirect = this.normalizeUrl(this.redirectUrl);
   10. const isRedirectTarget = normalizedRequest === normalizedRedirect;
   11. return !isRedirectTarget;
   12. }

   14. /**
   15. * Normalizes the URL
   16. */
   17. private normalizeUrl(url: string): string {
   18. return url
   19. .replace(/^(?:[a-zA-Z]+:)?\/\//, '')
   20. .replace(/\/+$/, '')
   21. .trim();
   22. }
   ```

   [RedirectRequestModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/RedirectRequestInterceptor/model/RedirectRequestModel.ets#L49-L70)
3. 若满足重定向条件，通过[WebviewController.loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)加载重定向页面。

   ```
   1. /**
   2. * Processes the load intercept event
   3. * Returns true if loading should be blocked (redirect performed), false to allow
   4. */
   5. processLoadIntercept(event: OnLoadInterceptEvent): boolean {
   6. // ...

   8. if (this.shouldInterceptUrl(requestUrl)) {
   9. // Perform redirect
   10. const redirected = this.performRedirect();
   11. return redirected; // Block original URL if redirect successful
   12. }

   14. return false; // Allow loading
   15. }

   17. /**
   18. * Performs the redirect operation
   19. */
   20. performRedirect(): boolean {
   21. try {
   22. this.controller.loadUrl(this.redirectUrl);
   23. // ...
   24. return true;
   25. } catch (error) {
   26. // ...
   27. return false;
   28. }
   29. }
   ```

   [RedirectRequestModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/RedirectRequestInterceptor/model/RedirectRequestModel.ets#L74-L117)

### 页面白名单配置

页面白名单配置的典型应用是通过限制访问来源，仅允许可信来源接入系统，来防止非授权访问和网络攻击。

**运行效果**

**图3** 页面白名单配置  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/QzJYsq4wT6aHT-oEo5Fngw/zh-cn_image_0000002490848542.png?HW-CC-KV=V1&HW-CC-Date=20260429T061102Z&HW-CC-Expire=86400&HW-CC-Sign=44F2B2E8C63115218B3898BAB139F7443DF354F2E49D8F0CCB0803BFAFB7E4AB "点击放大")

**实现原理**

在Web组件的[onLoadIntercept()](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)回调中获取请求的URL，若URL不属于白名单链接，则跳转到浏览器打开请求页面。

**开发步骤**

1. 配置页面白名单链接。

   ```
   1. Web({ src: this.loadingUrl, controller: this.controller })
   2. .onLoadIntercept((event) => {
   3. // Update whitelist URLs before intercepting
   4. this.viewModel?.setWhitelistUrls(this.whitelistUrlArr.map(url => url.toString()));
   5. // ...
   6. })
   ```

   [PageWhitelistView.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/PageWhitelistInterceptor/view/PageWhitelistView.ets#L160-L168)

   ```
   1. /**
   2. * Updates the whitelist URLs
   3. */
   4. setWhitelistUrls(urls: string[]): void {
   5. this.whitelistDomains = urls
   6. .map(url => this.extractDomain(url))
   7. .filter(domain => domain.length > 0);
   8. }

   10. /**
   11. *  Extract the domain name from a URL
   12. */
   13. private extractDomain(url: string): string {
   14. let normalized = url.trim().toLowerCase();
   15. // ...
   16. normalized = normalized
   17. .replace(/^(?:[a-z0-9+.-]+:)?\/\//, '') // strip protocol-like prefixes
   18. .split(/[/?#]/)[0]; // drop everything after domain
   19. return normalized.replace(/:+$/, '').replace(/\/+$/, '');
   20. }
   ```

   [PageWhitelistModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/PageWhitelistInterceptor/model/PageWhitelistModel.ets#L33-L56)
2. 获取请求的URL。

   ```
   1. /**
   2. * Processes the load intercept event
   3. * Returns true if loading should be blocked, false to allow
   4. */
   5. processLoadIntercept(event: OnLoadInterceptEvent): boolean {
   6. const requestUrl = event.data.getRequestUrl();
   7. // ...
   8. }
   ```

   [PageWhitelistModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/PageWhitelistInterceptor/model/PageWhitelistModel.ets#L111-L133)
3. 判断URL是否属于白名单链接。

   ```
   1. /**
   2. * Checks if a URL is in the whitelist
   3. */
   4. isUrlInWhitelist(requestUrl: string): boolean {
   5. const requestDomain = this.extractDomain(requestUrl);
   6. if (!requestDomain) {
   7. return false;
   8. }
   9. return this.whitelistDomains.includes(requestDomain);
   10. }
   ```

   [PageWhitelistModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/PageWhitelistInterceptor/model/PageWhitelistModel.ets#L68-L77)
4. 若不属于白名单链接，通过弹窗提示是否跳转到浏览器打开。

   ```
   1. /**
   2. * Processes the load intercept event
   3. * Returns true if loading should be blocked, false to allow
   4. */
   5. processLoadIntercept(event: OnLoadInterceptEvent): boolean {
   6. // ...
   7. // Check if URL is in whitelist
   8. if (this.isUrlInWhitelist(requestUrl)) {
   9. this.allowAllForCurrentLoad = true;
   10. return false; // Allow loading and subsequent requests
   11. }

   13. // URL not in whitelist, show dialog
   14. this.showDialog(requestUrl);
   15. return true; // Block loading
   16. }
   ```

   [PageWhitelistModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/PageWhitelistInterceptor/model/PageWhitelistModel.ets#L110-L134)
5. 点击确认，在浏览器中加载请求页面。

   ```
   1. /**
   2. * Open URL in external browser
   3. */
   4. private openInBrowser(url: string): void {
   5. // ...

   7. const want: Want = {
   8. uri: url,
   9. action: 'ohos.want.action.viewData',
   10. entities: ['entity.system.browsable'],
   11. parameters: {
   12. 'ohos.ability.params.showDefaultPicker': true
   13. }
   14. };
   15. // ...
   16. const context: common.UIAbilityContext = this.uiContext.getHostContext()! as common.UIAbilityContext;
   17. context.startAbility(want)
   18. .then(() => {
   19. if (this.config?.onOk) {
   20. this.config?.onOk(this.targetUrl)
   21. }
   22. // ...
   23. })
   24. .catch((err: BusinessError) => {
   25. // ...
   26. });
   27. }
   ```

   [WhitelistDialog.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/component/WhitelistDialog.ets#L123-L163)

## 基于onInterceptRequest()拦截能力的使用

Web组件在加载URL之前会触发[onInterceptRequest()](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)回调，用于判断是否拦截此次请求并返回自定义响应数据。基于该回调，可以实现[本地资源替换](bpta-web-interceptor.md#section29637307122)或[自定义资源加载策略](bpta-web-interceptor.md#section766911191316)。

**图4** 基于onInterceptRequest()的请求拦截流程图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/16JEe1SZRl2tr9vDPbuVVA/zh-cn_image_0000002522888281.png?HW-CC-KV=V1&HW-CC-Date=20260429T061102Z&HW-CC-Expire=86400&HW-CC-Sign=8A53111EBAE932E5A37E7BE445A83CCEC5D203D2908EF7724E88BECE13E86375 "点击放大")

### 本地资源替换

本地资源替换的典型应用是将部分频繁使用且变动较小的远程静态资源缓存至本地，以提升页面的加载速度和响应性能。

**运行效果**

**图5** 本地资源替换  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/10HizdEGRrKTfL3rzHgMrA/zh-cn_image_0000002490688570.png?HW-CC-KV=V1&HW-CC-Date=20260429T061102Z&HW-CC-Expire=86400&HW-CC-Sign=7EDA214FB09EBBC2CED2895F8559A0522F916AD216EBB6924AF89CC065D45923 "点击放大")

**实现原理**

在Web组件的[onInterceptRequest()](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)回调中获取网络请求信息，通过网络请求资源与本地资源的映射关系，获取对应的本地资源并将其设置给[WebResourceResponse](../harmonyos-references/arkts-basic-components-web-webresourceresponse.md)作为请求响应。

**开发步骤**

1. 配置网络请求资源和本地资源的映射关系，以及本地资源与相应MIME类型的映射关系。

   ```
   1. // Map between domain names and local files
   2. schemeMap = new Map([
   3. ['https://www.example.com/', 'index.html'],
   4. ['https://www.example.com/mountain.png', 'mountain.png']
   5. ]);
   6. // Map between local files and format mimeType
   7. mimeTypeMap = new Map([
   8. ['index.html', 'text/html'],
   9. ['mountain.png', 'image/png']
   10. ]);
   11. Web({ src: this.requestUrl, controller: this.controller })
   12. .onInterceptRequest((event) => {
   13. // Update scheme map before intercepting
   14. this.viewModel?.updateMappings(this.schemeMap, this.mimeTypeMap);
   15. // ...
   16. })
   ```

   [LocalResourceView.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/LocalResourceInterceptor/view/LocalResourceView.ets#L37-L144)

   ```
   1. /**
   2. * Updates the scheme and mime type mappings
   3. */
   4. updateMappings(schemeMap: Map<string, string>, mimeTypeMap: Map<string, string>): void {
   5. this.schemeMap = schemeMap;
   6. this.mimeTypeMap = mimeTypeMap;
   7. }
   ```

   [LocalResourceModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/LocalResourceInterceptor/model/LocalResourceModel.ets#L29-L35)
2. 获取请求的URL。

   ```
   1. /**
   2. * Processes the intercepted request and returns local resource response if applicable
   3. * Returns null if request should be allowed through
   4. */
   5. processRequest(event: OnInterceptRequestEvent | null): WebResourceResponse | null {
   6. // ...
   7. const requestUrl = event.request.getRequestUrl();
   8. // ...
   9. }
   ```

   [LocalResourceModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/LocalResourceInterceptor/model/LocalResourceModel.ets#L41-L77)
3. 通过映射关系获取本地资源。

   ```
   1. /**
   2. * Processes the intercepted request and returns local resource response if applicable
   3. * Returns null if request should be allowed through
   4. */
   5. processRequest(event: OnInterceptRequestEvent | null): WebResourceResponse | null {
   6. // ...
   7. const key = this.getUrlSchemeFromMap(requestUrl);

   9. if (key.length === 0) {
   10. return null; // No match, allow original request
   11. }

   13. const rawfileName = this.schemeMap.get(key);
   14. if (!rawfileName) {
   15. return null;  // Invalid mapping, allow original request
   16. }

   18. const mimeType = this.mimeTypeMap.get(rawfileName);
   19. if (!mimeType) {
   20. return null; // Invalid mapping, allow original request
   21. }
   22. // ...
   23. }
   24. /**
   25. * Gets the matching URL scheme key from the map
   26. */
   27. getUrlSchemeFromMap(prefix: string): string {
   28. let matchedKey: string = '';
   29. let maxLength: number = 0;
   30. const urlOrigin = this.getUrlOrigin(prefix);
   31. const urlFileName = this.getFileName(prefix);

   33. // Find the longest matching key to prioritize specific paths over general ones
   34. for (let key of this.schemeMap.keys()) {
   35. // 1. Direct prefix match
   36. if (prefix.startsWith(key) && key.length > maxLength) {
   37. matchedKey = key;
   38. maxLength = key.length;
   39. continue;
   40. }

   42. // 2. Same-domain file name match
   43. const keyFileName = this.getFileName(key);
   44. if (keyFileName.length === 0) {
   45. continue;
   46. }
   47. if (key.startsWith(urlOrigin) && keyFileName === urlFileName && key.length > maxLength) {
   48. matchedKey = key;
   49. maxLength = key.length;
   50. }
   51. }

   53. return matchedKey;
   54. }
   ```

   [LocalResourceModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/LocalResourceInterceptor/model/LocalResourceModel.ets#L40-L133)
4. 构建[WebResourceResponse](../harmonyos-references/arkts-basic-components-web-webresourceresponse.md)，设置并返回本地资源作为请求响应。

   ```
   1. /**
   2. * Processes the intercepted request and returns local resource response if applicable
   3. * Returns null if request should be allowed through
   4. */
   5. processRequest(event: OnInterceptRequestEvent | null): WebResourceResponse | null {
   6. // ...
   7. // Create response with local file
   8. return this.createLocalResourceResponse(rawfileName, mimeType);
   9. }
   10. /**
   11. * Creates a response with local file data
   12. */
   13. createLocalResourceResponse(rawfileName: string, mimeType: string): WebResourceResponse {
   14. const response = new WebResourceResponse();
   15. response.setResponseHeader([{
   16. headerKey: 'Connection',
   17. headerValue: 'keep-alive'
   18. }]);
   19. response.setResponseData($rawfile(rawfileName));
   20. response.setResponseEncoding('utf-8');
   21. response.setResponseMimeType(mimeType);
   22. response.setResponseCode(200);
   23. response.setReasonMessage('OK');
   24. response.setResponseIsReady(true);
   25. return response;
   26. }
   ```

   [LocalResourceModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/LocalResourceInterceptor/model/LocalResourceModel.ets#L39-L99)

### 自定义资源加载策略

自定义资源加载策略的典型应用是在Wi-Fi网络环境下加载高清图片，而在非Wi-Fi网络环境下加载压缩图片或本地占位图，以实现数据消耗与体验优化的平衡。

**运行效果**

**图6** Wi-Fi网络环境下加载图片资源  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/q91TP8THT2C1dLoiaQ0aCQ/zh-cn_image_0000002522768323.png?HW-CC-KV=V1&HW-CC-Date=20260429T061102Z&HW-CC-Expire=86400&HW-CC-Sign=EECF57AACE6548358A9E08B604600B85792F7D94CADC783C94756FB424167FE6 "点击放大")

**图7** 非Wi-Fi网络环境下加载本地占位图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/4C7RsAmGTC-ZUWZn4blRrA/zh-cn_image_0000002490848546.png?HW-CC-KV=V1&HW-CC-Date=20260429T061102Z&HW-CC-Expire=86400&HW-CC-Sign=DEE5B65D6F3C48CDCADE78CCB9DA3E62B4E12558A73D4C8F7344F218E6BF931F "点击放大")

**实现原理**

在Web组件的[onInterceptRequest()](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)回调中获取网络请求信息，对于图片资源请求，判断当前是否处于Wi-Fi网络环境下。若非Wi-Fi网络环境，则将本地占位图设置给[WebResourceResponse](../harmonyos-references/arkts-basic-components-web-webresourceresponse.md)作为请求响应。

**开发步骤**

1. 判断当前网络环境，若处于Wi-Fi网络环境下，则直接返回原始请求响应。

   ```
   1. /**
   2. * Processes the intercepted request and returns appropriate response
   3. * Returns null if request should be allowed through
   4. */
   5. processRequest(event: OnInterceptRequestEvent | null): WebResourceResponse | null {
   6. // ...
   7. // If WiFi network, allow original network request
   8. if (this.isWifiNetwork()) {
   9. return null;
   10. }
   11. // ...
   12. }
   13. /**
   14. * Checks if currently connected to a Wi-Fi network
   15. */
   16. isWifiNetwork(): boolean {
   17. try {
   18. const netHandle = connection.getDefaultNetSync();
   19. const netData = connection.getNetCapabilitiesSync(netHandle);
   20. return netData.bearerTypes.includes(connection.NetBearType.BEARER_WIFI);
   21. } catch (error) {
   22. // ...
   23. return false;
   24. }
   25. }
   ```

   [CustomLoadingStrategyModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/CustomLoadingStrategyInterceptor/model/CustomLoadingStrategyModel.ets#L40-L99)
2. 获取请求的URL。

   ```
   1. /**
   2. * Processes the intercepted request and returns appropriate response
   3. * Returns null if request should be allowed through
   4. */
   5. processRequest(event: OnInterceptRequestEvent | null): WebResourceResponse | null {
   6. // ...
   7. const requestUrl = event.request.getRequestUrl();

   9. // ...
   10. }
   ```

   [CustomLoadingStrategyModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/CustomLoadingStrategyInterceptor/model/CustomLoadingStrategyModel.ets#L39-L78)
3. 判断请求类型，若非图片资源请求，则直接返回原始请求响应。

   ```
   1. /**
   2. * Processes the intercepted request and returns appropriate response
   3. * Returns null if request should be allowed through
   4. */
   5. processRequest(event: OnInterceptRequestEvent | null): WebResourceResponse | null {
   6. // ...
   7. // Only intercept image requests
   8. if (!this.isImageRequestUrl(requestUrl)) {
   9. return null; // Not an image, allow original request
   10. }
   11. // ...
   12. }
   13. /**
   14. * Checks if a URL request is for an image
   15. */
   16. isImageRequestUrl(url: string): boolean {
   17. for (let format of this.imageFormatList) {
   18. if (url.endsWith(format)) {
   19. return true;
   20. }
   21. }
   22. return false;
   23. }
   ```

   [CustomLoadingStrategyModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/CustomLoadingStrategyInterceptor/model/CustomLoadingStrategyModel.ets#L38-L113)
4. 构建[WebResourceResponse](../harmonyos-references/arkts-basic-components-web-webresourceresponse.md)，对于非Wi-fi网络环境下的图片资源请求，设置并返回本地占位图作为请求响应。

   ```
   1. /**
   2. * Processes the intercepted request and returns appropriate response
   3. * Returns null if request should be allowed through
   4. */
   5. processRequest(event: OnInterceptRequestEvent | null): WebResourceResponse | null {
   6. // ...
   7. // Replace with placeholder image
   8. return this.createPlaceholderResponse();
   9. }
   10. /**
   11. * Creates a placeholder image response for non-WiFi networks
   12. */
   13. createPlaceholderResponse(): WebResourceResponse {
   14. const response = new WebResourceResponse();
   15. response.setResponseHeader([{
   16. headerKey: 'Connection',
   17. headerValue: 'keep-alive'
   18. }]);
   19. response.setResponseData($rawfile(CommonConstants.IMAGE_NO_WLAN));
   20. response.setResponseEncoding('utf-8');
   21. response.setResponseMimeType('image/png');
   22. response.setResponseCode(200);
   23. response.setReasonMessage('OK');
   24. response.setResponseIsReady(true);
   25. return response;
   26. }
   ```

   [CustomLoadingStrategyModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/CustomLoadingStrategyInterceptor/model/CustomLoadingStrategyModel.ets#L37-L141)

## 基于WebSchemeHandler拦截能力的使用

为当前Web组件设置[WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)，可以拦截指定协议的请求，获得请求信息并返回自定义响应数据。基于[WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)机制，可以实现[配置公共请求头](bpta-web-interceptor.md#section736313281410)等场景。

**图8** 基于WebSchemeHandler的请求拦截流程图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/iVJE2InsQvm8PYxuWrlcTA/zh-cn_image_0000002522888283.png?HW-CC-KV=V1&HW-CC-Date=20260429T061102Z&HW-CC-Expire=86400&HW-CC-Sign=5000AAFF5F7C379C0C0DBFCD45985D90400288AA2835AEC45C5E4B230984C02D "点击放大")

### 配置公共请求头

配置公共请求头的典型应用是在网络访问的过程中，在请求头中携带认证信息，使服务端能够识别用户身份并验证其访问权限。

**运行效果**

**图9** 配置公共请求头  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/kN39XqXNTtaufv_NIVGr6w/zh-cn_image_0000002490688572.png?HW-CC-KV=V1&HW-CC-Date=20260429T061102Z&HW-CC-Expire=86400&HW-CC-Sign=9D35BFF915F8567F914AE813D823BE292708D501CE1620F25860A788603A0DA1 "点击放大")

**实现原理**

通过[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)将[WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)设置给当前Web组件后，在[WebSchemeHandler.onRequestStart()](../harmonyos-references/arkts-apis-webview-webschemehandler.md#onrequeststart12)回调中拦截网络请求，并为其添加公共请求头，然后通过[rcp](../harmonyos-references/remote-communication-rcp.md#section176881642192516)将请求转发到服务端。

**开发步骤**

1. 通过[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)将[WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)设置给Web组件。

   ```
   1. // Bind interceptor to HTTP
   2. controller.setWebSchemeHandler('http', this.schemeHandler);
   ```

   [CommonHeaderViewModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/CommonHeaderInterceptor/viewmodel/CommonHeaderViewModel.ets#L47-L48)
2. 在[WebSchemeHandler.onRequestStart()](../harmonyos-references/arkts-apis-webview-webschemehandler.md#onrequeststart12)回调中拦截网络请求。

   ```
   1. // Set up request interceptor
   2. this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest,
   3. resourceHandler: webview.WebResourceHandler) => {
   4. // Process request
   5. const handled = this.model.processRequest(request, resourceHandler);
   6. return handled;
   7. });
   ```

   [CommonHeaderViewModel.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/Interceptors/CommonHeaderInterceptor/viewmodel/CommonHeaderViewModel.ets#L52-L58)
3. 为网络请求添加自定义的公共请求头，并通过[rcp.createSession()](../harmonyos-references/remote-communication-rcp.md#section163819131811)创建HTTP会话。

   ```
   1. /**
   2. * Creates an RCP session for the next outbound request.
   3. */
   4. private createSession(headers: Record<string, string>): void {
   5. try {
   6. // Create RCP session
   7. const sessionConfig: rcp.SessionConfiguration = {
   8. headers: headers
   9. };

   11. this.session = rcp.createSession(sessionConfig);
   12. } catch (error) {
   13. // ...
   14. }
   15. }
   ```

   [RcpRequestForwarder.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/common/utils/RcpRequestForwarder.ets#L85-L102)
4. 通过[rcp](../harmonyos-references/remote-communication-rcp.md#section176881642192516)将请求转发到服务端获取请求响应。

   ```
   1. /**
   2. * Sends GET or HEAD requests via the RCP session.
   3. */
   4. private forwardGetRequest(
   5. targetUrl: string,
   6. headers: Record<string, string>,
   7. resourceHandler: webview.WebResourceHandler,
   8. ): void {
   9. try {
   10. // ...
   11. this.createSession(headers);

   13. this.session?.get(targetUrl).then((response: rcp.Response) => {
   14. // ...
   15. this.handleResponse(response, resourceHandler);
   16. this.session?.close();
   17. }).catch((error: BusinessError) => {
   18. // ...
   19. });
   20. } catch (error) {
   21. // ...
   22. }
   23. }
   ```

   [RcpRequestForwarder.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/common/utils/RcpRequestForwarder.ets#L106-L138)
5. 调用[didReceiveResponse()](../harmonyos-references/arkts-apis-webview-webresourcehandler.md#didreceiveresponse12)和[didReceiveResponseBody()](../harmonyos-references/arkts-apis-webview-webresourcehandler.md#didreceiveresponsebody12)将构造的响应头和响应体传递给拦截的请求。

   ```
   1. /**
   2. * Maps the RCP response to a WebSchemeHandlerResponse.
   3. */
   4. private handleResponse(
   5. response: rcp.Response,
   6. resourceHandler: webview.WebResourceHandler,
   7. ): void {
   8. try {
   9. const webResponse = new webview.WebSchemeHandlerResponse();
   10. webResponse.setStatus(response.statusCode || 200);
   11. webResponse.setStatusText('OK');
   12. // ...
   13. webResponse.setMimeType(mimeType);
   14. webResponse.setEncoding(encoding);
   15. webResponse.setNetErrorCode(WebNetErrorList.NET_OK);

   17. // Set CORS headers
   18. webResponse.setHeaderByName('Access-Control-Allow-Origin', '*', true);
   19. webResponse.setHeaderByName('Access-Control-Allow-Credentials', 'true', true);
   20. webResponse.setHeaderByName('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS', true);
   21. webResponse.setHeaderByName('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Custom-Header', true);

   23. // ...
   24. resourceHandler.didReceiveResponse(webResponse);
   25. resourceHandler.didReceiveResponseBody(response.body);
   26. // ...
   27. } catch (error) {
   28. // ...
   29. }
   30. }
   ```

   [RcpRequestForwarder.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/common/utils/RcpRequestForwarder.ets#L208-L279)
6. 调用[didFinish()](../harmonyos-references/arkts-apis-webview-webresourcehandler.md#didfinish12)通知Web组件被拦截的请求已经完成。

   ```
   1. /**
   2. * Maps the RCP response to a WebSchemeHandlerResponse.
   3. */
   4. private handleResponse(
   5. response: rcp.Response,
   6. resourceHandler: webview.WebResourceHandler,
   7. ): void {
   8. try {
   9. // ...
   10. resourceHandler.didFinish();
   11. } catch (error) {
   12. // ...
   13. }
   14. }
   ```

   [RcpRequestForwarder.ets](https://gitcode.com/HarmonyOS_Samples/web-interceptor/blob/master/entry/src/main/ets/common/utils/RcpRequestForwarder.ets#L207-L280)

## 常见问题

### Web组件是否支持拦截前端页面的router.push()方法？

不支持。Web组件目前仅提供网络请求的拦截方法，而前端页面的router.push()方法不会触发新的网络请求，因此无法被拦截。

### Web组件支持异步判断是否拦截网络请求吗？

不支持。Web组件不支持异步判断是否拦截网络请求，但是可以在拦截网络请求后，异步处理响应数据，具体可参考[onInterceptRequest()示例代码](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)。

### Web组件是否支持拦截Ajax原始响应？

不支持。Web组件目前仅提供网络请求的拦截方法，无法拦截请求的响应。然而，可以通过[onInterceptRequest()](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)回调或[WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)机制自定义响应。

## 示例代码

* [实现基于Web组件的请求拦截功能](https://gitcode.com/harmonyos_samples/web-interceptor)
