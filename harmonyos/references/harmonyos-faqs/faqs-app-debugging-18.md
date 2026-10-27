---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-18
title: entry引用本地library时，没有ASan日志输出
breadcrumb: FAQ > DevEco Studio > 应用调试 > entry引用本地library时，没有ASan日志输出
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:578362d99662eb1059ec80425dfbb8bd8923b1b731814e78326e56e594da5417
---

**问题现象**

entry引用本地library时，已经勾选ASan选择项，没有ASan日志输出。

**解决措施**

引用本地C++ library时，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

```json
{
  // ...
      "arguments": "-DOHOS_ENABLE_ASAN=ON",
      // ...
    }
  },
  // ...
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/C2A86jx7QhirZt4EFOwkHA/zh-cn_image_0000002654798149.png)
