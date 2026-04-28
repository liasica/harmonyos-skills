---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-h5
title: H5接入智能填充
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 三方框架+H5接入智能填充 > H5接入智能填充
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:348eb529ec4f11727ad121e55185527082dd515b3d0eff109e50275fea9320fe
---

本章节介绍在ArkWeb的Web组件加载H5文件如何实现智能填充功能。

## 前提条件

* 设备智能填充开关必须处于打开状态，请前往“设置 > 隐私和安全 > 智能填充”页面开启开关。
* 设备已连接互联网并且登录华为账号。
* 该应用需已接入[智能填充服务](scenario-fusion-introduction-to-smart-fill.md#申请接入智能填充服务)。

## 效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/4MU7egUqSUawx64WkX4UuA/zh-cn_image_0000002583479159.png?HW-CC-KV=V1&HW-CC-Date=20260427T235046Z&HW-CC-Expire=86400&HW-CC-Sign=7D8D2FA4CB9587875B750CC3104F1533F21278B9FB3504186C8149918615F1E5)

## 示例代码一

通过ArkWeb的[Web组件](../harmonyos-references/arkts-basic-components-web.md)加载H5文件。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index {
6. controller: webview.WebviewController = new webview.WebviewController();
7. build() {
8. Column() {
9. // 在组件创建过程中加载HTML5文件。
10. Web({ src: $rawfile("autofill_h5.html"), controller: this.controller })
11. }
12. }
13. }
```

## 示例代码二

autofill\_h5.html如下所示。其中通过给form表单的input输入框（form表单的子节点）配置[autocomplete](scenario-fusion-mappingrelationship.md#h5-autocomplete和harmonyos的contenttype的映射关系)属性来支持智能填充，action需要配置表单提交接口链接，当form表单提交后，页面导航发生变化时，满足历史表单输入保存的条件时会触发对应弹窗。参考下面示例：

```
1. <!DOCTYPE html>
2. <html>
3. <head>
4. <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0;" name="viewport"/>
5. <title>智能填充H5测试</title>
6. </head>
7. <body>
8. <h4>智能填充H5测试</h4>
9. <!--The link of the form submission interface must be configured for the value of the action tag.-->
10. <form method="POST" action="">
11. <label for="nickname" style="width: 90px; display: inline-block; text-align: end;">昵称:</label>
12. <!--Smart fill is supported by configuring the autocomplete attribute.-->
13. <input type="text" id="nickname" autocomplete="nickname"/><br/><br/>
14. <label for="name" style="width: 90px; display: inline-block; text-align: end;">姓名:</label>
15. <input type="text" id="name" autocomplete="name"/><br/><br/>
16. <label for="tel-national" style="width: 90px; display: inline-block; text-align: end;">手机号:</label>
17. <input type="number" id="tel-national" autocomplete="tel-national"/><br/><br/>
18. <label for="email" style="width: 90px; display: inline-block; text-align: end;">邮箱:</label>
19. <input type="text" id="email" autocomplete="email"/><br/><br/>
20. <label for="id-card-number" style="width: 90px; display: inline-block; text-align: end;">身份证号:</label>
21. <input type="number" id="id-card-number" autocomplete="id-card-number"/><br/><br/>
22. <label for="street-address" style="width: 90px; display: inline-block; text-align: end;">带街道地址:</label>
23. <input type="text" id="street-address" autocomplete="street-address"/><br/><br/>
24. <div align="center">
25. <button type="submit" style="width: 80px">提交</button>
26. </div>
27. </form>
28. </body>
29. </html>
```
