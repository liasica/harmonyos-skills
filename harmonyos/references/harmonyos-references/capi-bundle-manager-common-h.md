---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-bundle-manager-common-h
title: bundle_manager_common.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > bundle_manager_common.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:00+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:18834579f4767be50fe14538461d080b172779cf65043b6694d315674aa626fe
---

## 概述

PhonePC/2in1TabletTVWearable

声明BundleManager定义的相关错误码。

**引用文件：** <bundle/bundle\_manager\_common.h>

**库：** libbundle\_ndk.z.so

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 21

**相关模块：** [Native\_Bundle](capi-native-bundle.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [BundleManager\_ErrorCode](capi-bundle-manager-common-h.md#bundlemanager_errorcode) | BundleManager\_ErrorCode | 枚举错误码。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### BundleManager\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum BundleManager_ErrorCode
```

**描述**

枚举错误码，详细介绍请参见[通用错误码](errorcode-universal.md)。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR = 0 | 执行成功。 |
| BUNDLE\_MANAGER\_ERROR\_CODE\_PERMISSION\_DENIED = 201 | 权限被拒绝。 |
| BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID = 401 | 参数无效。 |
