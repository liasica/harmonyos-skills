---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxycontroller
title: Class (ProxyController)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (ProxyController)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:05+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:f4fc5fc61daf49120489459a13f49e7de7ee87c5b78524644cee140474dc0a20
---

此类用于为应用程序设置代理。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 15开始支持。
* 示例效果请以真机运行为准。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## applyProxyOverride15+

PhonePC/2in1TabletTVWearable

static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void

设置应用中所有Web使用的代理配置，与[insertBypassRule](arkts-apis-webview-proxyconfig.md#insertbypassrule15)中插入的bypass规则匹配的URL将不会使用代理，而是直接向URL指定的源地址发起请求。代理设置成功后，不保证网络连接后会立即使用新的代理设置，在加载页面之前请等待监听器触发，这个监听器将在UI线程上被调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxyConfig | [ProxyConfig](arkts-apis-webview-proxyconfig.md) | 是 | 对代理的配置。 |
| callback | [OnProxyConfigChangeCallback](arkts-apis-webview-t.md#onproxyconfigchangecallback15) | 是 | 代理设置成功的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

完整示例代码参考[removeProxyOverride](arkts-apis-webview-proxycontroller.md#removeproxyoverride15)。

## removeProxyOverride15+

PhonePC/2in1TabletTVWearable

static removeProxyOverride(callback: OnProxyConfigChangeCallback): void

移除代理配置。移除代理配置后，不保证网络连接后会立即使用新的代理设置，在加载页面之前等待监听器，这个监听器将在UI线程上被调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnProxyConfigChangeCallback](arkts-apis-webview-t.md#onproxyconfigchangecallback15) | 是 | 代理配置变更的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. proxyRules: webview.ProxyRule[] = [];

11. build() {
12. Row() {
13. Column() {
14. Button("applyProxyOverride").onClick(()=>{
15. let proxyConfig:webview.ProxyConfig = new webview.ProxyConfig();
16. //优先使用第一个代理配置https://proxy.XXX.com
17. //代理失败后会回落到直连服务器insertDirectRule
18. try {
19. proxyConfig.insertProxyRule("https://proxy.XXX.com", webview.ProxySchemeFilter.MATCH_ALL_SCHEMES);
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. try {
24. proxyConfig.insertDirectRule(webview.ProxySchemeFilter.MATCH_HTTP);
25. } catch (error) {
26. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
27. }
28. try {
29. proxyConfig.insertBypassRule("*.example.com");
30. } catch (error) {
31. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
32. }
33. proxyConfig.clearImplicitRules();
34. proxyConfig.bypassHostnamesWithoutPeriod();
35. try {
36. proxyConfig.enableReverseBypass(true);
37. } catch (error) {
38. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
39. }
40. let bypassRules = proxyConfig.getBypassRules();
41. for (let i = 0; i < bypassRules.length; i++) {
42. console.info("bypassRules: " + bypassRules[i]);
43. }
44. this.proxyRules = proxyConfig.getProxyRules();
45. for (let i = 0; i < this.proxyRules.length; i++) {
46. console.info("SchemeFilter: " + this.proxyRules[i].getSchemeFilter());
47. console.info("Url: " + this.proxyRules[i].getUrl());
48. }
49. let isReverseBypassRule = proxyConfig.isReverseBypassEnabled();
50. console.info("isReverseBypassRules: " + isReverseBypassRule);
51. try {
52. webview.ProxyController.applyProxyOverride(proxyConfig, () => {
53. console.info("PROXYCONTROLLER proxy changed");
54. });
55. } catch (error) {
56. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
57. }
58. })
59. Button("loadUrl-https").onClick(()=>{
60. this.controller.loadUrl("https://www.example.com")
61. })
62. Button("loadUrl-http").onClick(()=>{
63. this.controller.loadUrl("http://www.example.com")
64. })
65. Button("removeProxyOverride").onClick(()=>{
66. try {
67. webview.ProxyController.removeProxyOverride(() => {
68. console.info("PROXYCONTROLLER proxy changed");
69. });
70. } catch (error) {
71. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
72. }
73. })
74. Web({ src: 'www.example.com', controller: this.controller})
75. }
76. .width('100%')
77. }
78. .height('100%')
79. }
80. }
```
