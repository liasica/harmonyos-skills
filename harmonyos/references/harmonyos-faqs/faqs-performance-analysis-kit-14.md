---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-14
title: 如何查询应用当前CPU占用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查询应用当前CPU占用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:eccc43a4fa4263237c4ca9c295aaca6f14b311ea05f0b6fb473fb616dbf46571
---

目前有两种方式查询当前CPU占用：

在代码中查询：

可以使用 `hidebug.getCpuUsage` 接口查询 CPU 占用。参考代码如下：

```typescript
let cpuUsage: number = hidebug.getCpuUsage();
```

在命令行中查询：

* 根据hdc命令行工具指导，完成[环境准备](../harmonyos-guides-V14/hdc-V14.md#环境准备)。
* 正常连接设备。

  ```powershell
  hidumper --cpuusage <pid>
  hidumper --cpuusage
  ```

**参考链接**

[hidebug.getCpuUsage](../harmonyos-references/js-apis-hidebug.md#hidebuggetcpuusage9)

[hidumper](../harmonyos-guides/hidumper.md)
