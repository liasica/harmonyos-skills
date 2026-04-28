---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-155
title: 编译报错“Cannot depend on HAP modules outside of this project”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot depend on HAP modules outside of this project”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5725db5a08fb08203594ed92b2f7d167e2dbaedda38824448368f61aac991a20
---

**错误描述**

不要依赖项目外部的HAP模块。

**可能原因**

项目根目录下的build-profile.json5文件中，srcPath字段引用了项目外部的 HAP 模块。

**解决措施**

使用HSP或HAR模块来替代项目外的HAP模块。
