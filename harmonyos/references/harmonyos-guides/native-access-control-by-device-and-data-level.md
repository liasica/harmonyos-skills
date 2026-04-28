---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-access-control-by-device-and-data-level
title: 基于设备分类和数据分级的访问控制 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 数据可靠性与安全性 > 基于设备分类和数据分级的访问控制 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7bd5025810a129f77c0532159c497615d6e8e8ddbaa9b3004e97ce19d898555b
---

## 场景介绍

分布式数据库的访问控制机制确保了数据存储和同步时的安全能力。在创建数据库时，应当基于数据分类分级规范合理地设置数据库的安全标签，确保数据库内容和数据标签的一致性。

当前仅支持使用关系型数据库（C/C++）进行分级访问控制。

## 基本概念

分布式数据管理对数据实施分类分级保护，提供基于数据安全标签和设备安全等级的访问控制。

数据安全标签和设备安全等级越高，加密措施和访问控制措施越严格，数据安全性越高。

### 数据安全标签

按照数据分类分级规范要求，可将数据分为S1、S2、S3、S4四个安全等级，安全等级具体可见[OH\_Rdb\_SecurityLevel](../harmonyos-references/capi-relational-store-h.md#oh_rdb_securitylevel)枚举。

| 风险等级 | 风险标准 | 定义 | 样例 |
| --- | --- | --- | --- |
| 严重 | S4 | 业界法律法规定义的特殊数据类型，涉及个人的最私密领域的信息或一旦泄露、篡改、破坏、销毁可能会给个人或组织造成重大的不利影响的数据。 | 政治观点、宗教和哲学信仰、工会成员资格、基因数据、生物信息、健康和性生活状况，性取向等或设备认证鉴权、个人信用卡等财务信息等。 |
| 高 | S3 | 数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严峻的不利影响。 | 个人实时精确定位信息、运动轨迹等。 |
| 中 | S2 | 数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严重的不利影响。 | 个人的详细通信地址、姓名昵称等。 |
| 低 | S1 | 数据的泄露、篡改、破坏、销毁可能会给个人或组织导致有限的不利影响。 | 性别、国籍、用户申请记录等。 |

### 设备安全等级

根据设备安全能力，比如是否有TEE、是否有安全存储芯片等，将设备安全等级分为SL1、SL2、SL3、SL4、SL5五个等级。例如，手表通常为低安全的SL1设备，手机、平板通常为高安全的SL4设备。

在设备组网时可以通过hidumper -s 3511查看设备安全等级。

## 跨设备同步访问控制机制

数据跨设备同步时，基于数据安全标签和设备安全等级进行访问控制。数据库的数据安全标签不高于对端设备的设备安全等级时，数据才能同步。具体访问控制矩阵如下：

| 设备安全级别 | 可同步的数据安全标签 |
| --- | --- |
| SL1 | S1 |
| SL2 | S1~S2 |
| SL3 | S1~S3 |
| SL4 | S1~S4 |
| SL5 | S1~S4 |

例如，手表通常为低安全的SL1设备。若创建数据安全标签为S1的数据库，则此数据库数据可以在这些设备间同步；若创建的数据库标签为S2-S4，则不能在这些设备间同步。

## 开发步骤

关系型数据库，通过OH\_Rdb\_SetSecurityLevel接口设置数据库的安全等级。此处以创建安全等级为S3的数据库为例。

1. CMakeLists.txt中添加以下lib。

   ```
   1. libnative_rdb_ndk.z.so
   ```
2. 导入头文件。

   ```
   1. #include <cstring>
   2. #include "database/rdb/relational_store.h"
   3. #include "hilog/log.h"
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/cpp/napi_init.cpp#L18-L20)
3. 调用OH\_Rdb\_SetSecurityLevel接口设置数据库的安全等级。

   ```
   1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
   2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el2/database");
   3. OH_Rdb_SetStoreName(config, "RdbTest.db");
   4. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
   5. OH_Rdb_SetModuleName(config, "entry");
   6. // 数据库文件安全等级
   7. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
   8. OH_Rdb_SetEncrypted(config, false);
   9. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL2);

   11. int errCode = 0;
   12. OH_Rdb_Store *store_ = OH_Rdb_CreateOrOpen(config, &errCode);
   13. OH_Rdb_CloseStore(store_);
   14. store_ = nullptr;
   15. OH_Rdb_DestroyConfig(config);
   16. config = nullptr;
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/cpp/napi_init.cpp#L163-L180)
