---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-data-prevention-13
title: 关于关键资产信息问题
breadcrumb: FAQ > 系统开发 > 安全 > 数据安全存储（Data Prevention） > 关于关键资产信息问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0041aa63eeb8edfc3fd044bc1496feaacf9edd74f4e21def35b5c5779ebca5f3
---

## 问题现象

关于关键资产信息具体问题如下：

1. 对于关键资产的获取，会受到哪些因素的影响导致获取不到？
2. 关键资产删除的时机？关键资产是和设备还是账号绑定的？
3. 使用关键资产API需要添加ohos.permission.STORE\_PERSISTENT\_DATA和ohos.permission.ACCESS\_BIOMETRIC权限，需要更新我们应用的隐私政策吗？有没有合规风险？

## 解决方案

1. 跨设备、跨应用、非关键资产属主、未获取关键资产权限、应用卸载未保留关键资产数据和所查询关键资产不存在都会导致关键资产获取不到。
2. 关键资产删除时机可参考[约束与限制](../harmonyos-guides/asset-store-kit-overview.md#约束与限制)中的关键资产删除时机。关键资产和账号没有绑定，是和设备进行绑定的。
3. Asset提供应用数据卸载保留的通用能力，业务层面的隐私合规风险由业务自己评估。如果存储的数据涉及用户隐私，建议在隐私政策说明哪些数据保留和删除时机。
