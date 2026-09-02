---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-16
title: .h文件中uint8_t无法使用如何解决
breadcrumb: FAQ > DevEco Studio > 工程管理 > .h文件中uint8_t无法使用如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:bf60ad3ccf9a5a0fa1a20ff6847c5a378cfc881b4f78a3d37198c0573d7e9282
---

**解决措施**

1. 在CPP导入头文件修改如下：

   ```cpp
   #ifdef __cplusplus
   extern “C” {
   #endif
   #include “MGDolphinTOTP.h”
   #include “MGDolphinTOTPsha1.h”
   #ifdef __cplusplus}
   #endif
   ```
2. CMakeLists.txt 中需要增加 .c 文件进行编译 ：

   add\_library(entry SHARED hello.cpp NapiTest.cpp MGDolphinTOTP.c MGDolphinTOTPSha1.c)
