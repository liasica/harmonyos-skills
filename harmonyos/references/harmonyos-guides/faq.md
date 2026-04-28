---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faq
title: 常见问题
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2d1b6b1fd7ce8479692b792f40a87276f809e91a065a30b9a18e2efb1846782
---

**Q1：执行过程中，设备断连重连后，任务能否继续执行？**

A1：如果发生设备断连情况，测试会终止，并生成测试报告，由于测试执行不充分，会导致生成的报告数据不完整，请确保设备在测试的过程中正常连接。

**Q2：设备已连接，为什么设备列表中未显示该设备？**

A2：需满足以下条件，才能使用DevEco Testing识别设备并进行测试：

1. 设备系统版本为HarmonyOS 5.0及以上。
2. PC与本地设备通过USB连接，设备需要进入设置-系统-开发者模式，开启开发者模式和USB调试权限。
3. 将 DevEco Testing 安装目录下的 hdc 路径配置至系统环境变量中。
4. 在CMD窗口中执行hdc list targets命令，可以识别到设备。

**Q3：为什么在测试任务执行过程中，结束客户端进程后手机端还会继续执行至完成？**

A3：若DevEco Testing客户端非正常关闭，有可能会出现这种情况：被测设备的测试任务依然在执行。原因是测试任务已下发到测试设备中，客户端非正常关闭后无法操作设备停止任务。

**Q4：Mac版DevEco Testing客户端使用性能基础质量测试、上架预检等卡片出现“AI模型暂未启动，请稍后再试”。为什么排查后找不到原因？**

A4：请确认Mac版DevEco Testing客户端是否按照以下步骤安装：

步骤1：DevEco Testing 客户端下载完成后将出现下图弹框。将下载的 DevEco\_Testing\_for\_App 文件拖拽至 Applications 文件夹。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/eH6jSLInSG-ssc2EKbmelw/zh-cn_image_0000002524623351.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=67C7478252F2B723E5174687E382D7E76FE2060A097551F592D16120A360B01F "点击放大")

步骤2：在启动台找到 DevEco Testing 图标则表示 DevEco Testing 已正常安装。

**Q5：Mac版本客户端使用覆盖安装后进入客户端后报错，如何解决？**

A5：点击取消报错弹框，进入客户端设置选项，关闭"开启登录状态保活"；最后点击“关于”退出登录。完成以上操作后重新登录即可恢复。

**Q6：Mac版本客户端如果覆盖安装后，报错****“‘DecEco\_Testing\_for\_App’ 已损坏，无法打开。你应该将它移到废纸篓。”****，如何解决？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/C2TENNhfQcOMTjBy8xoJBA/zh-cn_image_0000002537783290.png?HW-CC-KV=V1&HW-CC-Date=20260427T235755Z&HW-CC-Expire=86400&HW-CC-Sign=FACBDB6A1C0EDA752DD68572802035AEDD8F53D19AFEAF5828D0D1151E21B797)

更多问题详见[FAQ](../harmonyos-faqs/faqs-deveco-testing.md)
