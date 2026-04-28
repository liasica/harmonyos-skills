---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-9
title: ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”
breadcrumb: FAQ > DevEco Studio > 应用测试 > ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fcd7d939b49deb5261a1a5ba404acaae8fa5fb151e780e1e544b06914613dbb2
---

**问题现象**

在测试文件中引用启动页的导出方法并拉起启动页面所在的Ability时，执行测试会抛出jscrash，错误信息为：“Load Page Failed: pages/Index”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/KIyDtJW_QeuUuG_03POvOw/zh-cn_image_0000002229604273.png?HW-CC-KV=V1&HW-CC-Date=20260428T003017Z&HW-CC-Expire=86400&HW-CC-Sign=C463B9F80DA26062625B781085A73655874230C595F80751ABE4726D18A5F54F)**解决措施**

拉起启动页面所在Ability时指定当前模块名称，执行测试，用例正常运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/KC18-EWKRCeC0ef-GA92cw/zh-cn_image_0000002194158896.png?HW-CC-KV=V1&HW-CC-Date=20260428T003017Z&HW-CC-Expire=86400&HW-CC-Sign=B0D544FF6B21E05AED716DFF9BE40FD02E697EC0B704056116702172F12FFEBB)
