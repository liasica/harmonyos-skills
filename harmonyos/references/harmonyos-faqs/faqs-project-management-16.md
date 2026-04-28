---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-16
title: .h文件中uint8_t无法使用如何解决
breadcrumb: FAQ > DevEco Studio > 工程管理 > .h文件中uint8_t无法使用如何解决
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ce2b8a9756e109d7c36d7d57819e44281dbe2d79c80a78910f1e730e2dd07235
---

**解决措施**

1. 在CPP导入头文件修改如下：

   ```
   1. #ifdef __cplusplus
   2. extern “C” {
   3. #endif
   4. #include “MGDolphinTOTP.h”
   5. #include “MGDolphinTOTPsha1.h”
   6. #ifdef __cplusplus}
   7. #endif
   ```

   [MGDolphinTOTP.h](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ProjectManagement/entry/src/main/ets/cpp/MGDolphinTOTP.h#L8-L14)
2. CMakeLists.txt 中需要增加 .c 文件进行编译 ：

   add\_library(entry SHARED hello.cpp NapiTest.cpp MGDolphinTOTP.c MGDolphinTOTPSha1.c)
