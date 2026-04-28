---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-formerror
title: @ohos.application.formError (formError)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > 已停止维护的接口 > @ohos.application.formError (formError)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6f74b990178bd9ffe1a4a815cbe183b2da5ee292981e18bfb70aa49c127b95a8
---

formError模块提供获取卡片错误码的能力。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始不再维护，建议使用[卡片错误码](errorcode-form.md)替代。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { formError } from '@kit.FormKit';
```

## 权限

PhonePC/2in1TabletTVWearable

无

## FormError

PhonePC/2in1TabletTVWearable

枚举，支持的卡片类型。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERR\_COMMON | 1 | 默认错误码。 |
| ERR\_PERMISSION\_DENY | 2 | 没有操作权限。 |
| ERR\_GET\_INFO\_FAILED | 4 | 查询卡片信息失败。 |
| ERR\_GET\_BUNDLE\_FAILED | 5 | 查询应用信息失败。 |
| ERR\_GET\_LAYOUT\_FAILED | 6 | 查询布局信息失败。 |
| ERR\_ADD\_INVALID\_PARAM | 7 | 无效参数。 |
| ERR\_CFG\_NOT\_MATCH\_ID | 8 | 卡片ID不匹配。 |
| ERR\_NOT\_EXIST\_ID | 9 | 卡片ID不存在。 |
| ERR\_BIND\_PROVIDER\_FAILED | 10 | 绑定卡片提供方失败。 |
| ERR\_MAX\_SYSTEM\_FORMS | 11 | 系统卡片实例数量超过限制。 |
| ERR\_MAX\_INSTANCES\_PER\_FORM | 12 | 每张卡片实例数量超过限制。 |
| ERR\_OPERATION\_FORM\_NOT\_SELF | 13 | 操作非自己应用申请的卡片。 |
| ERR\_PROVIDER\_DEL\_FAIL | 14 | 卡片提供方删除卡片失败。 |
| ERR\_MAX\_FORMS\_PER\_CLIENT | 15 | 使用方申请卡片实例数超过限制。 |
| ERR\_MAX\_SYSTEM\_TEMP\_FORMS | 16 | 临时卡片实例数超过限制。 |
| ERR\_FORM\_NO\_SUCH\_MODULE | 17 | 模块不存在。 |
| ERR\_FORM\_NO\_SUCH\_ABILITY | 18 | ability组件不存在。 |
| ERR\_FORM\_NO\_SUCH\_DIMENSION | 19 | 卡片尺寸不存在。 |
| ERR\_FORM\_FA\_NOT\_INSTALLED | 20 | 卡片所在FA未安装。 |
| ERR\_SYSTEM\_RESPONSES\_FAILED | 30 | 系统服务响应失败。 |
| ERR\_FORM\_DUPLICATE\_ADDED | 31 | 重复添加卡片。 |
| ERR\_IN\_RECOVERY | 36 | 卡片数据覆盖失败。 |
