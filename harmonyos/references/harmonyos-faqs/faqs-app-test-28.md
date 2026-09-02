---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-28
title: "Hypium中，执行脚本报错NameError: name 'UiParam' is not defined如何解决"
breadcrumb: "FAQ > DevEco Studio > 应用测试 > Hypium中，执行脚本报错NameError: name 'UiParam' is not defined如何解决"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cf9e966fe4a1ec63f808c1369a0d1b29c279e97b15e0e6d680098f4714dd49f6
---

## 问题现象

使用driver.swipe(direction=UiParam.UP)方法执行上滑操作时，报错NameError: name 'UiParam' is not defined。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Nls-yt1yRsmbGVm7bK5jZA/zh-cn_image_0000002628569514.png "点击放大")

## 解决方案

1. 根据报错提示找到相关代码行，将鼠标光标移动到有波浪线报错的位置，会弹出如下提示：![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/LSyhfsZhRpejvDjPLZ6EVQ/zh-cn_image_0000002658928837.png)
2. 点击导入'hypium.model.UiParam'，此时查看代码页面顶端，自动导入了相关模块，如下图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/P0C7nCC4Rrq1m2Lhzt_cCA/zh-cn_image_0000002628409624.png)

## 总结

当出现NameError: name 'XXX' is not defined，都可以尝试使用此方式导入相关模块来进行方法调用。
