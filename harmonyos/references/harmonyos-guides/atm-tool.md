---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/atm-tool
title: atm工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > atm工具
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:42dba602dbae0d81e5a4ee8b0322d8b159db5fa081b6acbe5a473f5085f53c07
---

Access Token Manager (程序访问控制管理工具，简称atm工具)，是用于查询应用进程的权限、使用类型等信息的工具，为开发者提供了根据tokenid、包名、进程名等信息进行访问控制管理的能力。

## 环境说明

在使用本工具前，开发者需要先获取[hdc工具](hdc.md)，执行hdc shell。

## atm工具命令列表

| 命令 | 描述 |
| --- | --- |
| help | 帮助命令，显示atm支持的命令信息。 |
| dump | 查询命令，用于查询访问控制相关数据信息。 |

## 帮助命令

```
1. # 显示帮助信息
2. atm help
```

## 查询命令

```
1. atm dump [-h] [-t [-i <token-id>] [-b <bundle-name>] [-n <process-name>]] [-v [-i <token-id>] [-p <permission-name>]]
```

下表所列命令中，-t为必选参数，-i、-b、-n、-p为可选参数。对atm dump -t命令，-i、-b、-n参数只能单独使用。

| 参数 | 参数说明 |
| --- | --- |
| -d | 必选参数，查询系统中所有的权限定义。 |
| -d -p <permission-name> | 可选参数，通过权限名，查询权限定义。 |
| -h | 帮助信息。 |
| -t | 必选参数，查询系统中所有应用进程信息。 |
| -t -i <token-id> | 可选参数，通过应用进程的tokenid，查询该应用的基本信息以及对应的[权限信息](../harmonyos-references/js-apis-abilityaccessctrl.md#grantstatus)。 |
| -t -b <bundle-name> | 可选参数，通过应用进程的包名bundle-name，查询该应用的基本信息以及对应的[权限信息](../harmonyos-references/js-apis-abilityaccessctrl.md#grantstatus)。 |
| -t -n <process-name> | 可选参数，通过应用进程的进程名process-name，查询该应用的基本信息以及对应的[权限信息](../harmonyos-references/js-apis-abilityaccessctrl.md#grantstatus)。 |

示例：

```
1. #查询系统中所有的权限定义
2. atm dump -d

4. #按权限名查询权限定义
5. atm dump -d -p *********
6. # 执行结果
7. # {
8. #     "permissionName": "ohos.permission.KERNEL_ATM_SELF_USE",
9. #     "grantMode": "SYSTEM_GRANT",
10. #     "availableLevel": "SYSTEM_CORE",
11. #     "availableType": "SYSTEM",
12. #     "distributedSceneEnable": true,
13. #     "isKernelEffect": true,
14. #     "hasValue": true,
15. # }

17. #显示atm dump的帮助信息
18. atm dump -h

20. #查询系统中所有应用进程的tokenid和包名
21. atm dump -t

23. #按tokenid查询权限信息
24. atm dump -t -i *********
25. # 执行结果
26. # {
27. #   "tokenID": 672078897,
28. #   "processName": "samgr",
29. #   "apl": 2,
30. #   "permStateList": [
31. #     {
32. #       "permissionName": "ohos.permission.DISTRIBUTED_DATASYNC",
33. #       "grantStatus": 0,
34. #       "grantFlag": 4,
35. #     }
36. #   ]
37. # }

39. #按包名查询权限信息
40. atm dump -t -b ohos.telephony.resources
41. # 执行结果
42. # {
43. #   "tokenID": 537280686,
44. #   "tokenAttr": 1,
45. #   "ver": 1,
46. #   "userId": 100,
47. #   "bundleName": "ohos.telephony.resources",
48. #   "instIndex": 0,
49. #   "dlpType": 0,
50. #   "isRemote": false,
51. #   "isPermDialogForbidden": false,
52. #   "permStateList": [
53. #     {
54. #       "permissionName": "ohos.permission.DISTRIBUTED_DATASYNC",
55. #       "grantStatus": 0,
56. #       "grantFlag": 4,
57. #     }
58. #   ]
59. # }

61. #按进程名查询权限信息
62. atm dump -t -n *********
```
