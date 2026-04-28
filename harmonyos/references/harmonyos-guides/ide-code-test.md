---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-test
title: 代码测试
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 测试框架 > 代码测试
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:00+08:00
doc_updated_at: 2026-04-15
content_hash: sha256:97736bf0549c95b42fa57e5f904bf4370245e54fb3acc553c58dc1de62f99f06
---

DevEco Studio支持应用/元服务测试框架，提供测试用例执行能力，提供用例编写基础接口，输出测试结果，支持用户开发简洁易用的自动化测试脚本，支持代码覆盖率统计。

* **Instrument Test**：测试用例存放在ohosTest测试目录下，需要运行在设备或模拟器上。Instrument Test支持ArkTS/JS语言。
* **Local Test**：测试用例存放在test测试目录下，不需要运行在设备或模拟器上。Local Test支持ArkTS语言，仅支持Stage模型，不支持测试C/C++方法及系统API。

说明

覆盖率测试不支持开启混淆。

* **[Instrument Test](ide-instrument-test.md)**
* **[Local Test](ide-local-test.md)**
