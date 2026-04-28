---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-faq2
title: 401 参数检查失败的可能原因和解决办法
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > UI Design Kit常见问题 > 401 参数检查失败的可能原因和解决办法
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8dc4a968987c76d15d2730b4c48de9f1ee3fad7212c311a7156488eb96c114ed
---

**问题现象**

调用接口报错401 参数检查失败。

Parameter error. The value of bundleName is incorrect.

Parameter error. The value of layeredDrawableDescriptor is incorrect.

Parameter error. The value of size is incorrect.

Parameter error. The value of hasBorder is incorrect.

Parameter error. The value of pixelMap is incorrect.

Parameter error. The value of mask is incorrect.

Parameter error. The value of icons is incorrect.

Parameter error. The value of parallelNumber is incorrect.

Parameter error. The number of parameters is incorrect.

Parameter error. The type of ttf resource is error, the type must be resource.

Parameter error. The type of json resource is error, the type must be resource.

Parameter error. The ttf resource is null.

Parameter error. The json resource is null.

Parameter error. Load ttf resource failed.

Parameter error. Load json resource failed.

Parameter error. The ttf resource size is zero.

Parameter error. The json resource size is zero.

Parameter error. The json resource schema is incorrect.

**可能原因**

必选参数没有传入，或者参数类型错误。

**解决措施**

1. 请检查必选参数是否传入，或者传的参数类型是否错误。
2. 请检查传入的资源是否为空。
3. 请检查注册自定义的Symbol资源时传入的JSON资源格式是否正确。
