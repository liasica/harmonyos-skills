---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-secure-shield-mode
title: JSVM-API 坚盾守护模式
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API典型使用场景指导 > JSVM-API 坚盾守护模式
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a69a2eae43b089cd3c372ce6aa3e7107893f9e23e9218fdde5d4f927eed32a22
---

坚盾守护模式是为高安全需求用户设计的系统级安全防护方案。该模式通过实施严格的功能限制，显著增强系统安全性，有效防范针对远程攻击面的各类威胁。在坚盾守护模式下，JSVM 增加了功能限制，需要开发者评估应用在坚盾守护模式下的可用性。

## 启用坚盾守护模式

要启用坚盾守护模式，请按以下路径操作：

1. 进入手机系统设置
2. 选择"隐私和安全"选项
3. 点击"坚盾守护模式"并开启

## 坚盾守护模式下的功能限制

为降低JSVM受攻击风险，坚盾守护模式将实施以下关键安全限制：

* 全面禁用即时编译(JIT)功能，包括已获取 ACL 权限的应用程序
* 暂停 WebAssembly 支持（当前版本中 WebAssembly 依赖 JIT 功能实现）

## 应用兼容性评估指南

在坚盾守护模式下运行应用程序时，建议进行以下兼容性检查：

1. JavaScript 性能评估：

   * 测试应用在限制环境中的运行效率
   * 优化可能存在的性能瓶颈
2. WebAssembly 兼容性检查：

   * 静态代码分析：检查项目中的 WebAssembly 相关API调用，与第三方库的 Wasm 依赖情况。
   * 运行时验证：在坚盾守护模式下执行全功能测试。
