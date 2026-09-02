---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-204
title: 打包App报错：input module vendor is different
breadcrumb: FAQ > DevEco Studio > 编译构建 > 打包App报错：input module vendor is different
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:828603f133ca22362a38e6ff85b04c43d6b510b8f4c0442330031217c15997fd
---

## 问题现象

打包App时报错。

```screen
hvigor ERROR: Failed ::PackageApp...
> hvigor ERROR: Tools execution failed.
2024/03/03 11:31:45.825 - Ohos BundleTool [Error]: input module vendor is different.
2024/03/03 11:31:45.827 - Ohos BundleTool [Error]: some app variable is different.
2024/03/03 11:31:45.827 - Ohos BundleTool [Error]: Compressor::compressAppMode compress failed.
2024/03/03 11:31:45.840 - Ohos BundleTool [Error]: Compressor::compressProcess Bundle exception.
2024/03/03 11:31:45.840 - Ohos BundleTool [Error]: Compressor::compressProcess compress failed.
2024/03/03 11:31:45.841 - Ohos BundleTool [Error]: CompressEntrance::main exit, compress failed
```

## 背景知识

vendor标识对应用开发厂商的描述，取值为长度不超过255字节的字符串。该字段可用于展示开发厂商信息，如在应用的关于页面，取该字段展示开发厂商信息。

## 问题定位

报错提示：input module vendor is different，打包模块的vendor不一致。检查各模块的vendor字段是否存在且一致。

## 分析结论

* **场景一**： 打包模块的vendor不一致。
* **场景二**： app.json5文件缺失了vendor字段。

## 修改建议

* **场景一**：打包时检查应用了哪些模块，使各模块的vendor配置保持一致。排查方法如下：
  1. File->Settings->Build, Execution, Deployment->Build Tools->Hvigor中将Use log level改成Debug。
  2. 重新执行Build apps。
  3. Build日志中搜索“app\_packing\_tool”，查看入参：--hap-path、--hsp-path的对应信息，可得构建app时所有依赖的hsp和hap。
  4. hsp和hap的vendor要一致。
* **场景二**： 在app.json5中补全vendor字段信息。

  ```screen
  {
    "app": {
      "vendor": "example",
      // ...
    }
  }
  ```

## 常见FAQ

Q：打包App时报错：input module minAPIVersion is different，该如何解决？

A：出现该报错原因是模块间minAPIVersion配置不一致或app.json5中未统一声明minAPIVersion。可手动检查并统一各模块的minAPIVersion字段，同时确保在app.json5中声明该字段，然后重新打包App即可。

## 总结

vendor是标识应用供应商的核心字段，需在应用配置文件和模块配置文件中统一设置，且不同模块间的值必须完全一致以确保安装成功。
