---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-51
title: 应用打包成.app时其中的HAP包没有签名
breadcrumb: FAQ > DevEco Studio > 编译构建 > 应用打包成.app时其中的HAP包没有签名
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:291f4a5ef8761da1685ac9367306480bdb2746d35b2a5022b78cbc295c2b3074
---

上架时应用市场会拆包并重新签名，对应用签名后即可上架。应用市场在验证应用签名后，会解压获取所有HAP，再对HAP进行签名，因此无需在DevEco Studio中签名。
