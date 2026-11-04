---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-14
title: 如何查询应用当前CPU占用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查询应用当前CPU占用
category: harmonyos-faqs
scraped_at: 2026-11-04T08:38:16+08:00
doc_updated_at: 2026-11-03
content_hash: sha256:5c13caf2968946809bdce78e0f201bba06e52fea69c6d4a79b6a6e4b79629b06
---

目前有两种方式查询当前CPU占用：

在代码中查询：

可以使用 `hidebug.getCpuUsage` 接口查询 CPU 占用。参考代码如下：

```typescript
let cpuUsage: number = hidebug.getCpuUsage();
```

在命令行中查询：

* 根据hdc命令行工具指导，完成[环境准备](../doccenter-capabilities/hdc.md#环境准备)。
* 正常连接设备。

  ```powershell
  hidumper --cpuusage <pid>
  hidumper --cpuusage
  ```

**参考链接**

[hidebug.getCpuUsage](../harmonyos-references/js-apis-hidebug.md#hidebuggetcpuusage9)

[hidumper](../harmonyos-guides/hidumper.md)
