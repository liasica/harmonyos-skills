---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-50
title: 升级至API 26后使用“DocumentViewPicker”拉起文件选择Picker的聚合视图模式时支持文件格式过滤
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 升级至API 26后使用“DocumentViewPicker”拉起文件选择Picker的聚合视图模式时支持文件格式过滤
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-18
content_hash: sha256:699baad2729d0da22ae5fd6c4a4b998693d4f837f8fc0092568c7f76ee471a95
---

**问题现象**

升级API 26后，使用“DocumentViewPicker”拉起文件选择Picker的聚合视图模式时（“mergeMode”参数设置为非“DEFAULT”），选择Picker可选择的文件格式变少，且界面提示“仅显示应用需要的文件格式”。

**根本原因**

从API 26开始，当“DocumentViewPicker”的“mergeMode”参数配置为非“DEFAULT”值时，“fileSuffixFilters”参数将生效。此时，文件选择器会根据“fileSuffixFilters”参数指定的后缀格式进行过滤。

**解决措施**

检查使用“DocumentViewPicker”拉起文件选择Picker的聚合视图模式时，是否传入了“fileSuffixFilters”参数。若已传值，请确认传入的“fileSuffixFilters”参数是否完整覆盖了业务所需的所有文件类型。
