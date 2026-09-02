---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-env
title: 环境变量错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 环境变量错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:815b9f33d75be27d5e74bb61d204302faff79409e41ea240f015825d20143618
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 140000 @Env无效键

**错误信息**

Invalid key for @Env

**错误描述**

[@Env](ts-env-system-property.md#env)无效键。

**可能原因**

使用了@Env不支持的键。@Env仅接受预定义的[SystemProperties](ts-env-system-property.md#systemproperties)和[SystemEnvKey<T>](ts-env-system-property.md#systemenvkeyt)类型参数，传入不在支持范围内的键将触发此错误。详情见[@Env支持参数](../harmonyos-guides/arkts-env-system-property.md#env支持参数)。

**处理步骤**

确保@Env参数类型为[SystemProperties](ts-env-system-property.md#systemproperties) | [SystemEnvKey<T>](ts-env-system-property.md#systemenvkeyt)，详情见[@Env支持开发指南](../harmonyos-guides/arkts-env-system-property.md)。
