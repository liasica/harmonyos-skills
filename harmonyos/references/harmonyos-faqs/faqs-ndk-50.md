---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-50
title: Cmake编译时如何显示不同级别的日志信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Cmake编译时如何显示不同级别的日志信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:38+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:07508c1b7e1d3fcf856dbb27dafc08f6069f43a9ed0cc7d4a2c2df7187db1067
---

在hvigor/hvigor-config.json5文件中修改"logging"字段的"level"字段值。级别有"debug"、"info"、 "warn"、"error"。修改完成后，可以在run窗口查看CMakeLists.txt文件中message方法打印的日志信息。
