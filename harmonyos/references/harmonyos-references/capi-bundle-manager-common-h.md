---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-bundle-manager-common-h
title: bundle_manager_common.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > bundle_manager_common.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a42d8d335d831632d527fb9fc8a5e7b691a8eed0e59089af13f454abc88cbaf1
---

## 概述

声明BundleManager定义的相关错误码。

**引用文件：** <bundle/bundle\_manager\_common.h>

**库：** libbundle\_ndk.z.so

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 21

**相关模块：** [Native\_Bundle](capi-native-bundle.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [BundleManager\_ErrorCode](capi-bundle-manager-common-h.md#bundlemanager_errorcode) | BundleManager\_ErrorCode | 枚举错误码。 |

## 枚举类型说明

### BundleManager\_ErrorCode

```c
enum BundleManager_ErrorCode
```

**描述**

枚举错误码，详细介绍请参见[通用错误码](errorcode-universal.md)。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR = 0 | 执行成功。 |
| BUNDLE\_MANAGER\_ERROR\_CODE\_PERMISSION\_DENIED = 201 | 权限被拒绝。 |
| BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID = 401 | 参数无效。 |
