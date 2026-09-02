---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-deveco-testing-faq-9
title: DevEco Testing在无网络情况下能否使用
breadcrumb: FAQ > DevEco Testing > 常见问题 > DevEco Testing在无网络情况下能否使用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2d5b5ccf76b420cbf67061c9f4c4a5b0d5755de9b197462163293b34833daf04
---

## 问题现象

在没有网络连接的情况下，DevEco Testing是否可以正常使用？

## 背景知识

* [DevEco Testing](../harmonyos-guides/deveco-testing.md)登录机制特性：
  + 首次启动必须联网登录华为账号，但本地会缓存登录状态。
  + 已登录状态下断网仍可正常使用核心功能。
* [DevEco Testing](../harmonyos-guides/deveco-testing.md)核心功能可用性解读：
  + 本地设备测试支持：核心测试功能包括应用稳定性测试、应用性能功耗测试、回归测试、应用基础质量测试、设备投屏、UIView App等不依赖网络即可执行，同时测试数据的采集、分析及报告生成均可在本地完成。
  + 自动化脚本执行：基于本地安装的测试客户端和已连接的设备，UI自动化测试、稳定性遍历等操作无需网络支持。

## 解决方案

* 场景一：根据DevEco Testing登录机制判断。

  | 场景 | 网络状态 | 使用能力 |
  | --- | --- | --- |
  | 新设备首次启动 | 无网络 | 完全不可用。 |
  | 已登录未退出账号 | 无网络 | 核心功能可用。 |

  + 场景二：根据网络依赖场景判断。
    - 被测应用依赖网络：若被测应用本身需要联网（如登录、数据加载），无网络可能导致测试用例执行失败，但这属于应用自身限制，而非工具问题。
    - 报告上传与更新：测试报告默认存储于本地，但若需将报告上传至组织空间或检查工具更新，则需联网。
