---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-configuration-parameter
title: DevEco Studio配置参数列表
breadcrumb: 指南 > 编写与调试应用 > 附录 > DevEco Studio配置参数列表
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:09+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0530fa87400a1cfda75934f8c8abd894e3b5c856a59f2d79b7c8d03da3e38c1c
---

DevEco Studio基于IntelliJ平台开发，在原生的IntelliJ参数的基础上新增了部分参数，这些参数可在idea.properties中进行配置，参数列表如下：

| 参数 | 参数说明 |
| --- | --- |
| grs\_url | 设置DevEco Studio连接的云端环境。 |
| npm\_config\_strict\_ssl | 设置是否开启npm的https证书校验。默认为true，表示开启证书校验。 |
| ohpm\_config\_strict\_ssl | 设置是否开启ohpm的https证书校验。默认为true，表示开启证书校验。 |

说明

关闭证书校验，可能会带来安全风险，请谨慎使用。
