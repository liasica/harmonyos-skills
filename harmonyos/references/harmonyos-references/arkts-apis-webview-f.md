---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-f
title: Functions
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Functions
category: harmonyos-references
scraped_at: 2026-04-28T08:05:00+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:af7980fdfe78282c182115ecccd0f7dac1fb8425cb15c14e68c7be5915bfbf00
---

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 示例效果请以真机运行为准。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## webview.once

PhonePC/2in1TabletTVWearable

once(type: string, callback: Callback<void>): void

订阅一次指定类型Web事件的回调，Web事件的类型目前仅支持"webInited"，在Web引擎初始化完成时触发。

当应用中开始加载第一个Web组件时，Web引擎初始化，且后续再在同一应用中继续加载其他Web组件时不会再触发once回调。当应用销毁最后一个Web组件时，若再加载第一个Web组件，应用重新进入Web引擎初始化流程。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | Web事件的类型，目前支持："webInited"（Web引擎初始化完成）。 |
| callback | Callback<void> | 是 | 所订阅的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码 | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. webview.once("webInited", () => {
5. console.info("configCookieSync");
6. webview.WebCookieManager.configCookieSync("https://www.example.com", "a=b");
7. })

9. @Entry
10. @Component
11. struct WebComponent {
12. controller: webview.WebviewController = new webview.WebviewController();

14. build() {
15. Column() {
16. Web({ src: 'www.example.com', controller: this.controller })
17. }
18. }
19. }
```
