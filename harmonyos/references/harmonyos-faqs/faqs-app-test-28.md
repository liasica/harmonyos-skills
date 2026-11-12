---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-28
title: "Hypium中，执行脚本报错NameError: name 'UiParam' is not defined如何解决"
breadcrumb: "FAQ > DevEco Studio > 应用测试 > Hypium中，执行脚本报错NameError: name 'UiParam' is not defined如何解决"
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a08a94179bda4ed70c256dfd7d1d26f5553ea2fa3e09ddb85cf5bae54c463fa1
---

## 问题现象

使用driver.swipe(direction=UiParam.UP)方法执行上滑操作时，报错NameError: name 'UiParam' is not defined。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/ZBoYgtqOQL2J48yqitBoAQ/zh-cn_image_0000002628569514.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=507CB3F7E632DE07AD8801978492EFA91FBAB0394A280A85BBF5BD2C8E52358E "点击放大")

## 解决方案

1. 根据报错提示找到相关代码行，将鼠标光标移动到有波浪线报错的位置，会弹出如下提示：![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/vcPH3Y1DTzeUie4FkU09Xw/zh-cn_image_0000002658928837.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=6379D27AE49403C7E27F159EB004AC348AEB8C899B0EB9BD7FA4584D65314C6E)
2. 点击导入'hypium.model.UiParam'，此时查看代码页面顶端，自动导入了相关模块，如下图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/uNiInACQTNS_QejXd3XDgA/zh-cn_image_0000002628409624.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=AEBE4D7A90048DF84B499FA39344372458E6DBD09D67D9905719FC2DE675E4A8)

## 总结

当出现NameError: name 'XXX' is not defined，都可以尝试使用此方式导入相关模块来进行方法调用。
