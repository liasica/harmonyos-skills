---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-entity-type-api
title: EntityType（实体类型）
breadcrumb: API参考 > AI > Natural Language Kit（自然语言理解服务） > ArkTS API > EntityType（实体类型）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1604ec032f4eb878ac29dfaf9096d30a58ccd661d66d4a2ae5b6d75883173a15
---

实体类别的枚举类。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { EntityType } from '@kit.NaturalLanguageKit';
```

## EntityType

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATETIME | 'datetime' | 时间实体 |
| EMAIL | 'email' | 邮箱实体 |
| EXPRESS\_NO | 'expressNo' | 快递单号实体 |
| FLIGHT\_NO | 'flightNo' | 航班号实体 |
| LOCATION | 'location' | 地点实体 |
| NAME | 'name' | 姓名实体 |
| PHONE\_NO | 'phoneNo' | 手机号实体 |
| URL | 'url' | url实体 |
| VERIFICATION\_CODE | 'verificationCode' | 验证码实体 |
| ID\_NO | 'idNo' | 身份证号实体 |
