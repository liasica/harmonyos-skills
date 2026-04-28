---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-115
title: 编译报错“java.io.IOException: DerValue.getOID, not an OID 49”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“java.io.IOException: DerValue.getOID, not an OID 49”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e02165618a517f0aa8e0f7afe19e755915670430585f1d6ed0dec5f6512af923
---

**问题现象**

编译构建时出现错误：java.io.IOException: DerValue.getOID, not an OID 49。

```
1. hap-sign-tool: error: ACCESS_ERROR, code: 109. Details: java.io.IOException: DerValue.getOID, not an OID 49 Detail: Please check the message from tools
```

**报错原因**

证书文件解析失败，找不到OID。

**场景**

1. 证书遭篡改。
2. appCertPath参数传入了非证书文件。

**解决方案**

检查证书文件的正确性。
