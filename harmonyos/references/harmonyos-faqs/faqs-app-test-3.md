---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-3
title: 运行测试用例时，结果树始终处于加载状态
breadcrumb: FAQ > DevEco Studio > 应用测试 > 运行测试用例时，结果树始终处于加载状态
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d555697b3fc8ed1e7ee3d517df829ce686eeb53e1b357b5366ca3fec873dacf3
---

**问题现象**

如果多个模块（如entry和feature模块）同时依赖HSP，在设备上先运行entry和HSP模块，再执行feature模块下的测试用例时，任务结果树会一直处于加载状态，无法正常完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/oCNCCRxbT32g3YkIsUHpkQ/zh-cn_image_0000002229758525.png?HW-CC-KV=V1&HW-CC-Date=20260428T003017Z&HW-CC-Expire=86400&HW-CC-Sign=EBCD867713D4AAB03FE2563E4F51084A7FEA9BE9527E97A6E711219521309832)

**解决措施**

1. 打开非entry模块的ohosTest/ets/testrunner/OpenHarmonyTestRunner.ts文件。
2. 在lMonitor与want中分别增加moduleName字段，该字段用于指定当前模块的名称（即该模块下的module.json5文件中module字段下name的值）。示例代码如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Ks7jX4KhSAOJPBBz9AQ9hQ/zh-cn_image_0000002194158652.png?HW-CC-KV=V1&HW-CC-Date=20260428T003017Z&HW-CC-Expire=86400&HW-CC-Sign=1357EFD0046033C1A66D8C8B5CF1FC4D34C263A659FB26001218027BD9B4901A)
