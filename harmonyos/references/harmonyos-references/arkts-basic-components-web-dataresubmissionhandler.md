---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-dataresubmissionhandler
title: Class (DataResubmissionHandler)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (DataResubmissionHandler)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1ab7a38b0d057ac4c8b98b4389eddd19277bfa839661a031d80015395d81aeaa
---

通过DataResubmissionHandler可以重新提交表单数据或取消提交表单数据。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

PhonePC/2in1TabletTVWearable

constructor()

DataResubmissionHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## resend9+

PhonePC/2in1TabletTVWearable

resend(): void

重新发送表单数据。

**系统能力：** SystemCapability.Web.Webview.Core

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
12. .onDataResubmitted((event) => {
13. console.info('onDataResubmitted');
14. event.handler.resend();
15. })
16. }
17. }
18. }
```

## cancel9+

PhonePC/2in1TabletTVWearable

cancel(): void

取消重新发送表单数据。

**系统能力：** SystemCapability.Web.Webview.Core

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
12. .onDataResubmitted((event) => {
13. console.info('onDataResubmitted');
14. event.handler.cancel();
15. })
16. }
17. }
18. }
```
