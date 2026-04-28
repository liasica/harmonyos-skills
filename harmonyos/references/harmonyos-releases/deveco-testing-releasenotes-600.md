---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-testing-releasenotes-600
title: 新增和增强特性
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > DevEco Testing > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:45+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b73872a91284e8e61505de887da312a254076cbdd0aeeb353b54925ecd9eabbe
---

当前为 DevEco Testing 最新版本说明文档，如需查看 DevEco Testing 其它历史版本的功能新增、变更情况，请在左侧文档目录中选择相应版本。

## DevEco Testing 6.0.0 Release（6.0.7.100）

新增“应用上架预检（本地）”测试服务。具体请参考[应用上架预检](../harmonyos-guides/publish-testing.md#section214991410293)。

探索测试服务支持用户自定义场景进行压测。具体请参考[应用探索测试](../harmonyos-guides/exploratory-testing.md#section12324184817324)。

支持部分测试任务在模拟器上执行。

新增应用图谱管理工具、性能报告自动分析工具、性能测试报告对比工具。具体请参考[实用工具](../harmonyos-guides/tool.md)。

部分测试服务支持元服务创建任务。

**表1** **DevEco Testing测试服务应用兼容性配套关系**

| 模块 | 测试服务 | 模拟器 | 元服务 |
| --- | --- | --- | --- |
| [专项测试](../harmonyos-guides/specialized-testing.md) | 性能基础质量测试 | 不支持 | 支持 |
| 场景化性能测试 | 不支持 | 不支持 |
| UX基础质量测试 | 支持 | 支持 |
| 稳定性基础质量测试 | 支持 | 支持 |
| 安全基础质量测试 | 不支持 | 支持 |
| 功耗基础质量测试 | 不支持 | 支持 |
| 功能体验基础质量测试 | 支持 | 支持 |
| 性能指标监控测试 | 不支持 | 支持 |
| [上架预检](../harmonyos-guides/publish-testing.md) | 应用上架预检（本地） | 不支持 | 不支持 |
| [探索测试](../harmonyos-guides/exploratory-testing.md) | 应用探索测试 | 支持 | 支持 |
| [回归测试](../harmonyos-guides/regression-test.md) | 回归测试 | 支持 | 支持 |
| [实用工具](../harmonyos-guides/tool.md) | 设备投屏 | 不支持 | / |
| UIViewer | 不支持 | 支持 |
| 应用图谱管理工具 | 不支持 | 不支持 |
| 性能报告自动分析 | 不支持 | / |
| 性能测试报告对比 | 不支持 | / |

## DevEco Testing Hypium 6.0.0 Release（6.0.6.210）

测试框架支持被三方测试框架集成。

测试框架文本输入支持快速输入模式和追加输入模式。具体请参考[API使用方法](../harmonyos-guides/hypium-python-guidelines.md#section4598236435)。

测试框架长按支持指定长按时长，新增手表表冠操作接口。
