---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-3
title: 运行测试用例时，结果树始终处于加载状态
breadcrumb: FAQ > DevEco Studio > 应用测试 > 运行测试用例时，结果树始终处于加载状态
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:00+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:7d87e6944944159ad9c99e8a105ba2a3a5012e4a0e7ec9a0df6f46a013792939
---

**问题现象**

如果多个模块（如entry和feature模块）同时依赖HSP，在设备上先运行entry和HSP模块，再执行feature模块下的测试用例时，任务结果树会一直处于加载状态，无法正常完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/YiynYMUVR7yHSAQUQP4w4Q/zh-cn_image_0000002654838137.png)

**解决措施**

1. 打开非entry模块的ohosTest/ets/testrunner/OpenHarmonyTestRunner.ts文件。
2. 在lMonitor与want中分别增加moduleName字段，该字段用于指定当前模块的名称（即该模块下的module.json5文件中module字段下name的值）。示例代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/5VfPCHo7RdupmKzBPFW44Q/zh-cn_image_0000002624478818.png)
