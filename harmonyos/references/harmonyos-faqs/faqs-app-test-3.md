---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-3
title: 运行测试用例时，结果树始终处于加载状态
breadcrumb: FAQ > DevEco Studio > 应用测试 > 运行测试用例时，结果树始终处于加载状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:c16d9c79894f842229229bb47a5bff05d5c5ff45b1a4dae953b612fcf38d01c2
---

**问题现象**

如果多个模块（如entry和feature模块）同时依赖HSP，在设备上先运行entry和HSP模块，再执行feature模块下的测试用例时，任务结果树会一直处于加载状态，无法正常完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/LzwjMHfATIm4mbkeiJkw5w/zh-cn_image_0000002654838137.png)

**解决措施**

1. 打开非entry模块的ohosTest/ets/testrunner/OpenHarmonyTestRunner.ts文件。
2. 在lMonitor与want中分别增加moduleName字段，该字段用于指定当前模块的名称（即该模块下的module.json5文件中module字段下name的值）。示例代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/vTiWZ04zQiSae8F4OdKLPw/zh-cn_image_0000002624478818.png)
