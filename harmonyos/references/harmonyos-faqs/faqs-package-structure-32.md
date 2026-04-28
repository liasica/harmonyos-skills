---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-32
title: HAR包多账号如何上传
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HAR包多账号如何上传
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:31+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:657cf8ad8d96d8990328d78dc0f4aacf78fc75b13a5aa31e9bb6483ec914f3f8
---

HAR包建议第一任作者上传，如果是新建的包，想要多账号都能上传，需要在模块级oh-package.json5文件的name字段，配置<@group>/<package>类型的值，如"@hw-one/hhshs"。如果带有<@group>类型的值的包则需要在仓库上先新建组织，再添加用户进组织才能上传。
