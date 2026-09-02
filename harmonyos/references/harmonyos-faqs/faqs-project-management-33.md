---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-33
title: 如何解决编译时报错owns a higher api version问题
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何解决编译时报错owns a higher api version问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b0d8e3cf05581f92122fbdd249cf928921681dcd0e6709032673b8e0db918cc9
---

## 问题现象

项目编译时报错如下，请问该如何解决？

```log
> hvigor ERROR: ArkTS:ERROR Failed to execute es2abc.
Error Message: Error: The input abc file '/Users/xxx/Desktop/Git/KnowChat_Harmony/oh_modules/.ohpm/wrapper@xnnuf1xhgb6dfmf+4nqatekk3somopridtvlx+rvty0=/oh_modules/wrapper/ets/modules.abc' owns a higher api version or a higher sdkReleaseType compared to current compilation process. [/Users/xxx/Desktop/Git/KnowChat_Harmony/oh_modules/.ohpm/wrapper@xnnuf1xhgb6dfmf+4nqatekk3somopridtvlx+rvty0=/oh_modules/wrapper/ets/modules.abc]
Error: The input abc file '/Users/xxx/Desktop/Git/KnowChat_Harmony/oh_modules/.ohpm/@nertc+nertc_sdk@x07imzcfiusn4dyjfe46yg2t+btahwg70+p5ft9p+7y=/oh_modules/@nertc/nertc_sdk/ets/modules.abc' owns a higher api version or a higher sdkReleaseType compared to current compilation process. [/Users/xxx/Desktop/Git/KnowChat_Harmony/oh_modules/.ohpm/@nertc+nertc_sdk@x07imzcfiusn4dyjfe46yg2t+btahwg70+p5ft9p+7y=/oh_modules/@nertc/nertc_sdk/ets/modules.abc]
Error: The input abc file '/Users/xxx/Desktop/Git/KnowChat_Harmony/oh_modules/.ohpm/wrapper@xnnuf1xhgb6dfmf+4nqatekk3somopridtvlx+rvty0=/oh_modules/wrapper/ets/modules.abc' owns a higher api version or a higher sdkReleaseType compared to current compilation process.
The size of programs is expected to be 434, but is 432
```

## 背景知识

compatibleSdkVersionStage：用于控制不同beta版本的兼容，默认值为beta1。

## 解决方案

当字节码har打包的兼容版本高于工程的兼容版本时会出现以上问题。查看工程和har包的build-profile.json5文件中的‘compatibleSdkVersionStage’字段，选择以下任意一种解决方案：

* 将工程中的‘compatibleSdkVersionStage’字段调整至大于或者等于har包中的版本。
* 删除字节har和工程中的‘compatibleSdkVersionStage’字段。
