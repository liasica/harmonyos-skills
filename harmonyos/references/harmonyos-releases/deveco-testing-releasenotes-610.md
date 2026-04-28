---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-testing-releasenotes-610
title: 新增和增强特性
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > DevEco Testing > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e4bf4d5e40280bd783d5efea22c10e640a3a8a7b5a7d8276e16345517c68c3e
---

当前为 DevEco Testing 最新版本说明文档，如需查看 DevEco Testing 其它历史版本的功能新增、变更情况，请在左侧文档目录中选择相应版本。

## DevEco Testing 6.1.0 Release（6.1.0.211）

优化投屏工具兼容性，修复部分设备屏幕录制及应用安装异常问题。

## DevEco Testing 6.1.0 Release（6.1.0.200）

修复已知问题，优化用户体验。

## DevEco Testing 6.1.0 Beta（6.1.0.100）

1. 上架预检能力新增 10 项检测项，覆盖更多兼容性与稳定性标准实现自动化测试。
2. 性能测试服务问题定界定位能力增强，支持对接DevEco Studio 定位故障代码。
3. 针对部分已知的偶现bug，任务异常等问题完成修复，提升测试流程的稳定性和准确性。

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

## DevEco Testing Hypium 6.1.0 Release（6.1.0.210）

修复已知问题，优化用户体验。

## DevEco Testing Hypium 6.1.0 Release（6.1.0.200）

修复已知问题，优化用户体验。

## DevEco Testing Hypium 6.1.0 Beta（6.1.0.100）

Hypium 支持一键安装与更新，简化框架部署流程。
