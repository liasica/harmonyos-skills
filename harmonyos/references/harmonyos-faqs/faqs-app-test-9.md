---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-9
title: ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”
breadcrumb: FAQ > DevEco Studio > 应用测试 > ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e95184f1f5b8b73b2ed9d67cfb29fdf9a28c1250508d2d85458e4d2098750a87
---

**问题现象**

在测试文件中引用启动页的导出方法并拉起启动页面所在的Ability时，执行测试会抛出jscrash，错误信息为：“Load Page Failed: pages/Index”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/KIyDtJW_QeuUuG_03POvOw/zh-cn_image_0000002229604273.png?HW-CC-KV=V1&HW-CC-Date=20260429T062135Z&HW-CC-Expire=86400&HW-CC-Sign=B11C6BAF8CB0C40DD6FAE3168A2E37F367F6E257C42D8638A257EF3247EB4245)**解决措施**

拉起启动页面所在Ability时指定当前模块名称，执行测试，用例正常运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/KC18-EWKRCeC0ef-GA92cw/zh-cn_image_0000002194158896.png?HW-CC-KV=V1&HW-CC-Date=20260429T062135Z&HW-CC-Expire=86400&HW-CC-Sign=161C326D06B13B2F6A13978387D869B52C888F0524AA5E57BE9B806224E5BC70)
