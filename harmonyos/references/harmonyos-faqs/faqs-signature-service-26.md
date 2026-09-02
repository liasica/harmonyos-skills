---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-26
title: 打包后hap包安装失败，错误码：9568320
breadcrumb: FAQ > DevEco Studio > 签名服务 > 打包后hap包安装失败，错误码：9568320
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d6b25bd74f6aef87590523c822bc2ba9ff21b6d4c37b0b788d70293c88b9c4ba
---

## 问题现象

打包后的hap包安装失败，错误码：9568320。

```txt
install Failed: error: failed to install bundle.
code:9568320
error: no signature file.
```

## 背景知识

* [配置调试签名](../harmonyos-guides/ide-signing.md)：针对开发调试场景，DevEco Studio为开发者提供了自动签名方案，帮助开发者高效进行调试。此外，也可以选择手动签名方式生成调试签名。
* 9568320错误码参考：[9568320 签名文件不存在](../harmonyos-guides/bm-tool.md#section9568320-签名文件不存在)。

## 问题定位

* 根据报错信息可知，是签名文件或签名信息异常导致。可根据以下场景进行排查：
* 场景一：检查工程级build-profile.json5文件中是否配置signingConfigs签名配置，并且products中指定了对应的signingConfig。
* 场景二：DevEco Studio缓存异常可能导致签名失效，尝试清理缓存后重启是否正常。
* 场景三：排查证书是否使用正确。

## 分析结论

* 场景一：工程级build-profile.json5文件配置错误，例如：产品未配置signingConfig。
* 场景二：DevEco Studio缓存异常导致签名失效。
* 场景三：证书使用错误。

## 修改建议

* 场景一：工程级build-profile.json5文件配置准确，保证products中指定了对应的signingConfig。
* 场景二：
  1. 执行菜单栏操作：Build -> Clean Project -> File -> Invalidate Caches，然后重启DevEco Studio。
  2. 删除本地签名目录（路径在签名页面可见），重新运行自动签名。
* 场景三：保证证书类型使用正确，调试包使用调试证书，正式发布包使用发布证书，发布证书需要在AppGallery Connect创建获取。
