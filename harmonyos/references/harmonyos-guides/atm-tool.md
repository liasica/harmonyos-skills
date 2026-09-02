---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/atm-tool
title: atm工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > atm工具
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:13+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:555557b287d0ca6e0ac78717e332f926405d2642fac50878bed5b37ef82e36ec
---

Access Token Manager (程序访问控制管理工具，简称atm工具)，是用于查询或设置应用进程的权限、使用类型等信息的工具，为开发者提供了根据tokenId、包名、进程名等信息进行访问控制管理的能力。

## 环境说明

在使用本工具前，开发者需要先获取[hdc工具](hdc.md)，执行hdc shell。

## atm工具命令列表

| 命令 | 描述 |
| --- | --- |
| help | 帮助命令，显示atm支持的命令信息。 |
| perm | 权限命令，为应用进程授予、取消权限或重置user\_grant权限状态。从API版本26.0.0开始，支持对debug签名应用执行上述操作。 |
| dump | 查询命令，用于查询访问控制相关数据信息。 |

## 帮助命令

```bash
# 显示帮助信息
atm help
```

## 权限命令

```bash
atm perm [-h] [-g -i <token-id> -p <permission-name>] [-c -i <token-id> -p <permission-name>] [-r -i <token-id>] [-r -b <bundle-name>]
```

下表所列命令中，-g、-c、-r为必选参数，且只能单独使用。对atm perm -g和atm perm -c命令，-i和-p为必选参数；对atm perm -r命令，-i和-b参数只能单独使用，且不支持-p参数；-b参数仅支持和-r参数组合使用。

**权限命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -h | 帮助信息。atm perm支持的命令集合。 |
| -g -i <token-id> -p <permission-name> | -g、-i、-p均为必选参数，通过应用进程的tokenId授予指定权限。返回是否成功。 |
| -c -i <token-id> -p <permission-name> | -c、-i、-p均为必选参数，通过应用进程的tokenId取消指定权限。返回是否成功。 |
| -r -i <token-id> | -r、-i均为必选参数，通过应用进程的tokenId重置user\_grant权限状态。返回是否成功。  **说明**：从API版本26.0.0开始，支持该参数。 |
| -r -b <bundle-name> | -r、-b均为必选参数，通过应用进程的包名重置同包名应用的user\_grant权限状态。返回是否成功。  **说明**：从API版本26.0.0开始，支持该参数。 |

示例：

```bash
# 显示atm perm的帮助信息
atm perm -h

# 为应用进程授予相机权限
atm perm -g -i ********* -p ohos.permission.CAMERA

# 为应用进程取消相机权限
atm perm -c -i ********* -p ohos.permission.CAMERA

# 重置指定应用进程的user_grant权限状态
atm perm -r -i *********

# 重置指定包名下应用进程的user_grant权限状态
atm perm -r -b com.ohos.bundlename
```

## 查询命令

```bash
atm dump [-h] [-d [-p <permission-name>]] [-t [-i <token-id>] [-b <bundle-name>] [-n <process-name>] [-p <permission-name>]]
```

下表所列命令中，-d、-t为必选参数，-i、-b、-n、-p为可选参数。对atm dump -t命令，-i、-b、-n、-p参数只能单独使用。

| 参数 | 参数说明 |
| --- | --- |
| -h | 帮助信息。 |
| -d | 必选参数，查询系统中所有的权限定义。 |
| -d -p <permission-name> | 可选参数，通过权限名，查询权限定义。 |
| -t | 必选参数，查询系统中所有进程的tokenId。 |
| -t -i <token-id> | 可选参数，通过进程的tokenId，查询该进程的基本信息以及对应的[GrantStatus](../harmonyos-references/js-apis-abilityaccessctrl.md#grantstatus)。 |
| -t -b <bundle-name> | 可选参数，通过应用进程的包名bundle-name，查询该应用的基本信息以及对应的[GrantStatus](../harmonyos-references/js-apis-abilityaccessctrl.md#grantstatus)。 |
| -t -n <process-name> | 可选参数，通过进程名process-name，查询该进程的基本信息以及对应的[GrantStatus](../harmonyos-references/js-apis-abilityaccessctrl.md#grantstatus)。 |
| -t -p <permission-name> | 可选参数，通过权限名，查询申请该权限的应用进程的tokenId。  **说明**：从API版本26.0.0开始，支持该参数。 |

示例：

```bash
#查询系统中所有的权限定义
atm dump -d

#按权限名查询权限定义
atm dump -d -p *********
# 执行结果
# {
#     "permissionName": "ohos.permission.KERNEL_ATM_SELF_USE",
#     "grantMode": "SYSTEM_GRANT",
#     "availableLevel": "SYSTEM_CORE",
#     "availableType": "SYSTEM",
#     "distributedSceneEnable": true,
#     "isKernelEffect": true,
#     "hasValue": true,
# }

#显示atm dump的帮助信息
atm dump -h

#查询系统中所有进程的tokenId
atm dump -t

#按tokenId查询权限信息
atm dump -t -i *********
# 执行结果
# {
#   "tokenId": 672078897,
#   "processName": "samgr",
#   "apl": 2,
#   "permStateList": [
#     {
#       "permissionName": "ohos.permission.DISTRIBUTED_DATASYNC",
#       "grantStatus": 0,
#       "grantFlag": 4,
#     }
#   ]
# }

#按包名查询权限信息
atm dump -t -b ohos.telephony.resources
# 执行结果
# {
#   "tokenId": 537280686,
#   "tokenAttr": 1,
#   "ver": 1,
#   "userId": 100,
#   "bundleName": "ohos.telephony.resources",
#   "instIndex": 0,
#   "dlpType": 0,
#   "isRemote": false,
#   "isPermDialogForbidden": false,
#   "permStateList": [
#     {
#       "permissionName": "ohos.permission.DISTRIBUTED_DATASYNC",
#       "grantStatus": 0,
#       "grantFlag": 4,
#     }
#   ]
# }

#按权限名查询申请该权限的所有应用进程的tokenId和包名
atm dump -t -p ohos.permission.CAMERA
# 执行结果
# Permission: ohos.permission.CAMERA
# Total Tokens: 1

# 537538306: com.ohos.camera

#按进程名查询权限信息
atm dump -t -n *********
```
