---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-default-useragent
title: User-Agent开发指导
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 设置基本属性和事件 > User-Agent开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b62942ed1a700dfafc7e3c6bf4357b9b5b253d934d8710f6c8d102b07d830ec3
---

User-Agent（简称UA）是一个特殊的字符串，包含设备类型、操作系统及版本等关键信息。在Web开发中，这个字符串使服务器能够识别请求的来源设备及其特性，从而根据这些信息提供定制化的内容和服务。如果页面无法正确识别UA，可能会导致多种异常情况。例如，为移动设备优化的页面布局可能会在桌面设备上显示错乱，反之亦然。此外，某些特定的浏览器功能或CSS样式可能仅在特定的浏览器版本中受支持，如果页面无法根据UA字符串做出正确的判断，就可能导致渲染问题或逻辑错误。

## 默认User-Agent结构

* 默认User-Agent定义

  ```
  1. Mozilla/5.0 ({DeviceType}; {OSName} {OSVersion}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ChromeCompatibleVersion}.0.0.0 Safari/537.36  ArkWeb/{ArkWeb VersionCode} {DeviceCompat} {扩展区}
  ```
* 举例说明

  ```
  1. Mozilla/5.0 (Phone; OpenHarmony 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36  ArkWeb/4.1.6.1 Mobile
  ```
* 字段说明

  | 字段 | 含义 |
  | --- | --- |
  | DeviceType | 当前的设备类型。  取值范围：  - Phone：[手机](../design-guides/phone-0000001776694632.md)设备  - Tablet：[平板](../design-guides/pad-0000001823654157.md)设备  - PC：[2in1](../design-guides/2in1-0000001777531700.md)设备 |
  | OSName | 基础[操作系统名称](glossary.md#section15569823194110)。  默认取值：OpenHarmony |
  | OSVersion | 基础操作系统版本，两位数字，M.S。  例如HarmonyOS-6.1.0.31取值为6.1 |
  | ChromeCompatibleVersion | 兼容Chrome主版本的版本号，从114版本开始演进。  对应取值参考[约束与限制](web-component-overview.md#约束与限制)，例如HarmonyOS 6.0上默认的Chrome版本为132 |
  | ArkWeb | HarmonyOS版本Web内核名称。  默认取值：ArkWeb |
  | ArkWeb VersionCode | ArkWeb版本号，格式a.b.c.d。  例如4.1.6.1 |
  | DeviceCompat | 前向兼容字段。  手机设备默认取值为Mobile  其他设备默认取值为空 |
  | 扩展区 | 三方应用可以扩展的字段。  三方应用使用ArkWeb组件时，可以做UA扩展，例如加入APP相关信息标识。 |

说明

* 当前默认User-Agent的ArkWeb字段前有两个空格。
* 当前通过User-Agent中是否含有"Mobile"字段来判断是否开启前端HTML页面中meta标签的viewport属性。当User-Agent中不含有"Mobile"字段时，meta标签中viewport属性默认关闭，此时可通过显性设置[metaViewport](../harmonyos-references/arkts-basic-components-web-attributes.md#metaviewport12)属性为true来覆盖关闭状态。
* 建议通过OpenHarmony关键字识别是否是HarmonyOS设备，同时可以通过DeviceType识别设备类型用于不同设备上的页面显示（ArkWeb关键字表示设备使用的web内核，OpenHarmony关键字表示设备使用的操作系统，因此推荐通过OpenHarmony关键字识别是否是HarmonyOS设备）。
* {DistributionOSName}和{DistributionOSVersion}字段在API version 15之前的版本中未启用，从API version 15版本开始不在默认User-Agent中体现。

注意

为了确保兼容性，部分浏览器可能会在用户代理（User-Agent）中增加非OpenHarmony的操作系统名称。针对用户代理中同时包含“OpenHarmony”和非OpenHarmony操作系统名称的场景，建议网页将OpenHarmony的处理逻辑放置在其他操作系统处理逻辑之前。

## 自定义User-Agent结构

在下面的示例中，通过调用[getUserAgent()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getuseragent)接口获取当前默认的用户代理（User-Agent）字符串。这一接口提供的默认User-Agent信息为开发者提供了基础，使开发者能够基于这个默认信息进行定制或扩展。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Button('getUserAgent')
13. .onClick(() => {
14. try {
15. let userAgent = this.controller.getUserAgent();
16. console.info("userAgent: " + userAgent);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

以下示例通过[setCustomUserAgent()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)接口设置自定义用户代理，但请注意，此操作会覆盖系统的用户代理。因此，我们建议将扩展字段追加在默认用户代理的末尾，比如三方应用程序的开发场景，可以在系统默认用户代理字符串的末尾追加特定的APP标识，这样既能保留原有用户代理信息，又能增加自定义的应用识别信息。

当Web组件src设置了url时，建议在[onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)回调事件中设置User-Agent，设置方式请参考示例。不建议将User-Agent设置在[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)回调事件中，会概率性出现设置失败。若未在onControllerAttached回调事件中设置User-Agent，后续调用setCustomUserAgent方法时，可能会出现加载的页面与实际设置User-Agent不符的异常现象。

当Web组件src设置为空字符串时，建议先调用setCustomUserAgent方法设置User-Agent，再通过loadUrl加载具体页面。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. // 三方应用相关信息标识
10. @State customUserAgent: string = ' DemoApp';

12. build() {
13. Column() {
14. Web({ src: 'www.example.com', controller: this.controller })
15. .onControllerAttached(() => {
16. console.info("onControllerAttached");
17. try {
18. let userAgent = this.controller.getUserAgent() + this.customUserAgent;
19. this.controller.setCustomUserAgent(userAgent);
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. })
24. }
25. }
26. }
```

从API version 20开始，可通过[setAppCustomUserAgent()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setappcustomuseragent20)接口设置应用级自定义用户代理，或者通过[setUserAgentForHosts()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setuseragentforhosts20)对特定网站设置应用级自定义用户代理，覆盖系统的用户代理，应用内所有Web组件生效。

建议在Web组件创建前先调用静态接口[getDefaultUserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getdefaultuseragent14)获取默认的用户代理（User-Agent）字符串，然后调用setAppCustomUserAgent，setUserAgentForHosts方法设置User-Agent，再创建指定src的Web组件或通过loadUrl加载具体页面。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. aboutToAppear(): void {
11. try {
12. webview.WebviewController.initializeWebEngine();
13. let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
14. let appUA = defaultUserAgent + " appUA";
15. webview.WebviewController.setAppCustomUserAgent(appUA);
16. webview.WebviewController.setUserAgentForHosts(
17. appUA,
18. [
19. "www.example.com",
20. "www.baidu.com"
21. ]
22. );
23. } catch (error) {
24. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
25. }
26. }

28. build() {
29. Column() {
30. Web({ src: 'www.example.com', controller: this.controller })
31. }
32. }
33. }
```

在下面的示例中，通过[getCustomUserAgent()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getcustomuseragent10)接口获取自定义用户代理。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. @State userAgent: string = '';

11. build() {
12. Column() {
13. Button('getCustomUserAgent')
14. .onClick(() => {
15. try {
16. this.userAgent = this.controller.getCustomUserAgent();
17. console.info("userAgent: " + this.userAgent);
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. Web({ src: 'www.example.com', controller: this.controller })
23. }
24. }
25. }
```

## 相关User-Agent接口优先级

| 接口名称 | 优先级 | 说明 |
| --- | --- | --- |
| setCustomUserAgent | 最高 | 对调用的Web组件生效。 |
| setUserAgentForHosts | 低于setCustomUserAgent | 对应用中所有Web组件访问指定网站生效。 |
| setAppCustomUserAgent | 低于setUserAgentForHosts | 对应用中所有Web组件生效。 |
| ArkWeb默认UA | 最低 | 对应用中所有Web组件生效，只读，通过getDefaultUserAgent获取。 |

## 常见问题

### 如何通过User-Agent来识别HarmonyOS操作系统中不同设备

HarmonyOS设备的识别主要通过User-Agent中的系统、系统版本和设备类型三个维度来判断。建议同时检查上述信息，以确保更准确的设备识别。

1. 系统识别

   通过User-Agent中的{OSName}字段识别HarmonyOS系统。

   ```
   1. const isHarmonyOS = () => /OpenHarmony/i.test(navigator.userAgent);
   ```
2. 系统版本识别

   通过User-Agent中的{OSName}和{OSVersion}字段识别HarmonyOS NEXT系统及系统版本。格式为：OpenHarmony + 版本号。

   ```
   1. // 检测是否是HarmonyOS NEXT系统
   2. const matches = navigator.userAgent.match(/OpenHarmony (\d+\.?\d*)/);
   3. matches?.length && Number(matches[1]) >= 5;
   ```
3. 设备类型识别

   通过deviceType字段来识别不同设备类型。

   ```
   1. // 检测是否为手机设备
   2. const isPhone = () => /Phone/i.test(navigator.userAgent);

   4. // 检测是否为平板设备
   5. const isTablet = () => /Tablet/i.test(navigator.userAgent);

   7. // 检测是否为2in1设备
   8. const is2in1 = () => /PC/i.test(navigator.userAgent);
   ```

### 如何模拟HarmonyOS操作系统的User-Agent进行前端调试

在Windows/Mac/Linux等操作系统中，可以通过Chrome/Edge/Firefox等浏览器DevTools提供的User-Agent复写能力，模拟HarmonyOS User-Agent。

### 如何在HarmonyOS中自定义User-Agent以实现H5兼容性

HarmonyOS提供[setCustomUserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)接口以支持User-Agent的自定义设置。为适配移动端H5页面通常依赖的UA标识检测（如Mobile、OpenHarmony等），并确保不覆盖系统默认UA信息，推荐按如下方式操作：首先通过[getDefaultUserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getdefaultuseragent14)接口获取系统默认User-Agent字符串，随后将H5兼容所需的自定义标识字段追加至该字符串末尾，最后调用setCustomUserAgent接口设置修改后的完整UA字符串。

### 如何解决H5页面的UA兼容性问题

**Q：移动设备上网页呈现电脑版样式或电脑设备上网页呈现移动样式展示**

A：网站会针对不同UA展示不同样式页面。需要移动设备UA设置DeviceCompat为"Mobile"，DeviceType为"Phone"，PC设备UA设置DeviceCompat为""，DeviceType为"PC"，平板设备UA设置DeviceCompat为""，DeviceType则为"Tablet"。

**Q：部分网页打不开或显示“不支持的浏览器”**

A：网页未适配OpenHarmony UA，需要网页对"OpenHarmony"标识作兼容处理。

**Q：页面循环跳转**

A：应用端对存在跳转关系的两个页面设置了冲突的UA标识‌，导致服务端重定向逻辑陷入死循环。确保应用端在调用setUserAgentForHosts对关联网站设置兼容UA时保持逻辑一致， 避免因UA差异触发网页跳转逻辑循环。

**Q：网页提供的下载链接与设备平台不匹配，如OpenHarmony设备上下载安装包为apk等**

A：UA 中的“兼容性字段”干扰了服务端识别。为了保障网页兼容性，部分浏览器可能会在用户代理（User-Agent）中增加非OpenHarmony的操作系统名称，如果服务端的解析逻辑顺序不当，可能会忽略掉真正的设备标识。针对这种场景，建议网页将OpenHarmony的处理逻辑放置在其他操作系统处理逻辑之前。

## 示例代码

* [Web用户代理](https://gitcode.com/harmonyos_samples/web-user-agent)
