---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-9
title: "ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”"
breadcrumb: "FAQ > DevEco Studio > 应用测试 > ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”"
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:01+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:cf2f39517c54d524aba31342cbb549b2a06abf46c4340b2c6de94098efc4941c
---

**问题现象**

在测试文件中引用启动页的导出方法并拉起启动页面所在的Ability时，执行测试会抛出jscrash，错误信息为：“Load Page Failed: pages/Index”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/PKp5IA4iTCSsrwHjlRdwxQ/zh-cn_image_0000002624478826.png)**解决措施**

拉起启动页面所在Ability时指定当前模块名称，执行测试，用例正常运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/LKny_8iPRF6EpluQDFw5pw/zh-cn_image_0000002654798191.png)
