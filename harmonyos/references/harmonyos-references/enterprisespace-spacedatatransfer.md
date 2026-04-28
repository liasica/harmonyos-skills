---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisespace-spacedatatransfer
title: spaceDataTransfer (空间数据传输)
breadcrumb: API参考 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > ArkTS API > spaceDataTransfer (空间数据传输)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:35+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:6c36c5397bc59a6d12ac53d6f6cb9f60d9d8ecee47af7f37c64de38703d27dec
---

空间数据传输为企业安全管控类[MDM](../harmonyos-guides/mdm-kit.md)应用提供下发空间互传策略能力，提供设置审批信息、获取审批信息的能力。

供企业安全管控类MDM应用申请权限后使用。

**起始版本：** 6.0.0(20)

## 导入模块

PC/2in1

```
1. import { fileTransfer } from '@kit.EnterpriseSpaceKit';
```

## AuditInfo

PC/2in1

审批信息。

**系统能力**：SystemCapability.EnterpriseSpace.SpaceDataTransfer

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| auditId | string | 否 | 否 | 表示在发起审批时由数据库自动生成的审批ID，通常为由9位数字组成的字符串。不能为空字符串。 |
| userId | string | 否 | 否 | 表示用户ID。 |
| userName | string | 否 | 否 | 表示用户名称。 |
| time | number | 否 | 否 | 表示整型转换后的审批时间戳，以ms为单位。 |
| comments | string | 否 | 否 | 表示审批评论。无位数限制。 |
| status | string | 否 | 否 | 表示文件审批状态。其中，"1"表示等待审批，"2"表示取消审批，"3"表示拒绝审批，"4"表示同意审批。 |

## setAuditInfo

PC/2in1

setAuditInfo(transactionNum: string, info: AuditInfo): number

设置审批信息，将审批结果返回给空间互传应用。

**需要权限：** ohos.permission.ENTERPRISE\_FILE\_TRANSFER\_AUDIT\_POLICY\_MANAGEMENT

**系统能力：** SystemCapability.EnterpriseSpace.SpaceDataTransfer

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transactionNum | string | 是 | 在传输文件时由数据库自动生成的传输编号，通常为由19位数字组成的字符串。不能为空字符串。 |
| info | [AuditInfo](enterprisespace-spacedatatransfer.md#auditinfo) | 是 | 表示审批信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回设置审批信息的结果。结果为0代表设置审批信息成功。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 1020300001 | System service exception. |
| 1020300002 | Parameter error. |

**示例：**

```
1. import { fileTransfer } from '@kit.EnterpriseSpaceKit';

3. const transactionNum: string = '1111111';
4. const info: fileTransfer.AuditInfo = {
5. auditId: '123456',
6. userId: '100',
7. userName: 'test',
8. time: Date.now(),
9. comments: 'Waiting approval',
10. status: '1'
11. };
12. try {
13. const ret: number = fileTransfer.setAuditInfo(transactionNum, info);
14. console.info(`Succeeded in setting audit info, number:`, ret);
15. } catch (err) {
16. console.error(`Failed to set audit info. Code: ${err.code}, message: ${err.message}`);
17. }
```

## getAuditInfo

PC/2in1

getAuditInfo(transactionNum: string): AuditInfo

获取审批信息。

**需要权限：** ohos.permission.ENTERPRISE\_FILE\_TRANSFER\_AUDIT\_POLICY\_MANAGEMENT

**系统能力：** SystemCapability.EnterpriseSpace.SpaceDataTransfer

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transactionNum | string | 是 | 在传输文件时由数据库自动生成的传输编号，通常为由19位数字组成的字符串。不能为空字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuditInfo](enterprisespace-spacedatatransfer.md#auditinfo) | 表示审批信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 1020300001 | System service exception. |
| 1020300002 | Parameter error. |

**示例：**

```
1. import { fileTransfer } from '@kit.EnterpriseSpaceKit';

3. const transactionNum: string = '1111111';
4. try {
5. const auditInfo: fileTransfer.AuditInfo = fileTransfer.getAuditInfo(transactionNum);
6. console.info(`Succeeded in getting audit info:` + JSON.stringify(auditInfo));
7. } catch (err) {
8. console.error(`Failed to get audit info. Code: ${err.code}, message: ${err.message}`);
9. }
```

## policyPush

PC/2in1

policyPush(policyContext: string): void

配置工作空间互传单双通策略。具体而言，分别配置是否允许个人工作空间和企业工作空间向对端空间发送文件。

**需要权限：** ohos.permission.ENTERPRISE\_FILE\_TRANSFER\_AUDIT\_POLICY\_MANAGEMENT或ohos.permission.FILE\_TRANSFER\_OPERATION

**系统能力：** SystemCapability.EnterpriseSpace.SpaceDataTransfer

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policyContext | string | 是 | 下发单双通策略的内容。一级节点为**config**，其有6个二级节点，分别为**inEnable**、**incoming\_check**、**outEnable**、**outgoing\_check**、**checkpoint\_config**和**approvalpoint\_config**。每个节点负责不同的功能，共同构成了完整的策略配置。详细内容参考下表。  - **inEnable**：控制企业空间接收文件的权限。  - **incoming\_check**：定义个人空间向企业空间发送文件时的检测规则。参数格式为字符串，内容会在后续详细解释。  - **outEnable**：控制企业空间外发文件的权限。  - **outgoing\_check**：定义企业空间向个人空间发送文件时的检测规则。参数格式为字符串，内容会在后续详细解释。  - **checkpoint\_config**：配置检测应用的信息，包括应用的包名、组件名、参数、检测函数编码。参数格式为字符串，内容会在后续详细解释。  - **approvalpoint\_config**：配置审批点的信息，包括应用的包名和组件名。 |

**二级节点详细说明**

* **inEnable**：控制企业空间接收文件的权限。其值为“0”时，表示禁止；为“1”时，表示允许。
* **outEnable**：控制企业空间外发文件的权限。其值为“0”时，表示禁止；为“1”时，表示允许。
* **incoming\_check**

| **参数名称** | **功能描述** | **示例值** |
| --- | --- | --- |
| data\_list | 定义个人空间向企业空间发送文件时的检测规则。 | [ { "allow": "VirusCheck.result == 0", "approval": "", "check\_point": "VirusCheck", "check\_point\_name": "VirusCheck\_in", "is\_enable": "true", "forbidden": "VirusCheck.result == 1", "order": "0" } ] |

* **outgoing\_check**

| **参数名称** | **功能描述** | **示例值** |
| --- | --- | --- |
| data\_list | 定义企业空间向个人空间发送文件时的检测规则。 | [ { "allow": "SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7", "approval": "SecurityCheck.Result == 10", "check\_point": "SecurityCheck", "check\_point\_name": "SecurityCheck\_out", "is\_enable": "true", "forbidden": "SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11", "order": "0" } ] |

* **checkpoint\_config**

| **参数名称** | **功能描述** | **示例值** |
| --- | --- | --- |
| data\_list | 配置检测应用的信息，包括应用的包名、组件名、参数、检测函数编码。 | [ { "check\_point": "VirusCheck", "check\_point\_name": "VirusCheck\_in", "check\_sequence": "Serial", "order": "0", "allow": "VirusCheck.result == 0", "forbidden": "VirusCheck.result == 1" } ] |

* **approvalpoint\_config**

| **参数名称** | **功能描述** | **示例值** |
| --- | --- | --- |
| data\_list | 定义个人空间向企业空间发送文件时的检测规则。 | [ { "bundle\_name": "com.example.enterprisespacekit\_samplecode\_clientdemo\_arkts", "ability\_name": "TestApprovalAbility" } ] |

**三级节点详细说明**

* **incoming\_check**下的**data\_list**

| **参数名称** | **功能描述** | **示例值** |
| --- | --- | --- |
| allow | 放通动作配置，通过表达式配置。 | "VirusCheck.result == 0" |
| approval | 审批动作配置，个人空间向企业空间发送文件时的审批不生效，不需要配置。 | "VirusCheck.Result == 10" |
| check\_point | 检测点类型。  SecurityCheck：安全检查  VirusCheck：病毒检查 | "SecurityCheck" |
| check\_point\_name | 检测点名称。 | "VirusCheck\_in" |
| is\_enable | 配置个人空间向企业空间发送文件时检测的规则是否生效。可选参数。  true：生效  false：不生效  默认值：true | "true" |
| forbidden | 拦截动作配置信息，通过“VirusCheck.Result == xx”样式表达拦截动作，当用“or”连接多个表达式时，多个拦截动作组合配置。“xx”具体取值由业务决定。 | "VirusCheck.result == 1 or VirusCheck.result == 2" |
| order | 检测点顺序号，编号从0开始。空间互传服务会根据编号顺序依次处理检测点。 | "0" |

* **outgoing\_check**下的**data\_list**

| **参数名称** | **功能描述** | **示例值** |
| --- | --- | --- |
| allow | 放通动作配置，通过表达式配置。 | "SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7" |
| approval | 审批动作配置，通过表达式配置。 | "SecurityCheck.Result == 10" |
| check\_point | 检测点类型。  SecurityCheck：安全检查  VirusCheck：病毒检查 | "SecurityCheck" |
| check\_point\_name | 检测点名称。 | "SecurityCheck\_out" |
| is\_enable | 配置个人空间向企业空间发送文件时检测的规则是否生效。可选参数。  true：生效  false：不生效  默认值：true | "true" |
| forbidden | 拦截动作配置信息，通过“SecurityCheck.Result == xx”样式表达拦截动作，当用“or”连接多个表达式时，多个拦截动作组合配置。“xx”具体取值由业务决定。 | "SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11" |
| order | 检测点顺序号，编号从0开始。空间互传服务会根据编号顺序依次处理检测点。 | "0" |

* **checkpoint\_config**下的**data\_list**

| **参数名称** | **功能描述** | **示例值** |
| --- | --- | --- |
| check\_point\_name | 检测点名称。 | "SecurityCheck" 或 "VirusCheck" |
| bundle\_name | 包名。 | "com.example.enterprisespacekit\_samplecode\_clientdemo\_arkts" |
| ability\_name | 组件名。 | "TestScanAbility" |
| func\_code | 检测函数编码。 | "2" 或 "3" |
| type | 检测点类型。  1：病毒检测  2：资产检测，检测资产能否外发  3：其他类型  当前仅支持病毒检测和资产检测类型。 | “1” |

* **approvalpoint\_config**下的**data\_list**

| **参数名称** | **功能描述** | **示例值** |
| --- | --- | --- |
| bundle\_name | 包名。 | "com.example.enterprisespacekit\_samplecode\_clientdemo\_arkts" |
| ability\_name | 组件名。 | "TestApprovalAbility" |

policyContext内容可参考如下：

```
1. {
2. "config": {
3. "inEnable": "1",
4. "incoming_check": {
5. "data_list": [
6. {
7. "allow": "VirusCheck.result == 0",
8. "approval": "",
9. "check_point": "VirusCheck",
10. "check_point_name": "VirusCheck_in",
11. "is_enable": "true",
12. "forbidden": "VirusCheck.result == 1",
13. "order": "0"
14. }
15. ]
16. },
17. "outEnable": "1",
18. "outgoing_check": {
19. "data_list": [
20. {
21. "allow": "SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7",
22. "approval": "SecurityCheck.Result == 10",
23. "check_point": "SecurityCheck",
24. "check_point_name": "SecurityCheck_out",
25. "is_enable": "true",
26. "forbidden": "SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11",
27. "order": "0"
28. }
29. ]
30. },
31. "checkpoint_config": {
32. "data_list": [
33. {
34. "check_point_name": "SecurityCheck",
35. "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",
36. "ability_name": "TestScanAbility",
37. "func_code": "2",
38. "type": "2"
39. },
40. {
41. "check_point_name": "VirusCheck",
42. "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",
43. "ability_name": "TestScanAbility",
44. "func_code": "3",
45. "type": "1"
46. }
47. ]
48. },
49. "approvalpoint_config": {
50. "data_list": [
51. {
52. "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",
53. "ability_name": "TestApprovalAbility"
54. }
55. ]
56. }
57. }
58. }
```

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](enterprisespace-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 1020300001 | System service exception. |
| 1020300002 | Parameter error. |

**示例：**

```
1. import { fileTransfer } from '@kit.EnterpriseSpaceKit';

3. const policyContext: string =
4. '{\"config\":{\"inEnable\":\"1\",\"incoming_check\":{\"data_list\":[{\"allow\":\"VirusCheck.result == 0\",\"approval\":\"\",\"check_point\":\"VirusCheck\",\"check_point_name\":\"VirusCheck_in\",\"check_sequence\":\"Serial\",\"forbidden\":\"VirusCheck.result == 1\",\"order\":\"0\"}]},\"outEnable\":\"0\",\"outgoing_check\":{\"data_list\":[{\"allow\":\"SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7\",\"approval\":\"SecurityCheck.Result == 10\",\"check_point\":\"SecurityCheck\",\"check_point_name\":\"SecurityCheck_out\",\"check_sequence\":\"Serial\",\"forbidden\":\"SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11\",\"order\":\"0\"}]},\"checkpoint_config\":{\"data_list\":[{\"check_point_name\":\"SecurityCheck\",\"bundle_name\":\"com.example.enterprisespacekit_samplecode_clientdemo_arkts\",\"ability_name\":\"TestScanAbility\",\"func_code\":\"2\",\"type\":\"2\"},{\"check_point_name\":\"VirusCheck\",\"bundle_name\":\"com.example.enterprisespacekit_samplecode_clientdemo_arkts\",\"ability_name\":\"TestScanAbility\",\"func_code\":\"3\",\"type\":\"1\"}]},\"approvalpoint_config\":{\"data_list\":[{\"bundle_name\":\"com.example.enterprisespacekit_samplecode_clientdemo_arkts\",\"ability_name\":\"TestApprovalAbility\"}]}}}';
5. try {
6. fileTransfer.policyPush(policyContext);
7. console.info(`Succeeded in pushing policy`);
8. } catch (err) {
9. console.error(`Failed to push policy. Code: ${err.code}, message: ${err.message}`);
10. }
```
