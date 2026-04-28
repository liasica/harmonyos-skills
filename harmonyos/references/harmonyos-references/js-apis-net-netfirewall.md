---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-netfirewall
title: @ohos.net.netFirewall (网络防火墙)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.netFirewall (网络防火墙)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c888d0a808b0d82ac0862c64077d732fd2a8c10d810f11af4d738e5fa4f9f46c
---

本模块为应用程序提供网络防火墙能力。应用程序可以对机器进行防火墙拦截记录的查询。

说明

本模块首批接口从API version 15开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PC/2in1

```
1. import { netFirewall } from '@kit.NetworkKit';
```

## netFirewall.setNetFirewallPolicy

PC/2in1

setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>

设置系统用户ID的防火墙策略，包含防火墙开关状态，默认的出站/入站行为（允许/阻止）。支持不同的系统用户ID配置不同的防火墙策略。使用Promise异步回调。

说明

同一系统用户下，多应用调用该接口下发策略，会以最新下发的策略为准。

**需要权限**：ohos.permission.MANAGE\_NET\_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 系统用户ID，只能是存在的用户ID。 |
| policy | [NetFirewallPolicy](js-apis-net-netfirewall.md#netfirewallpolicy) | 是 | 设置的防火墙策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[网络连接管理错误码](errorcode-net-connection.md)和[防火墙错误码](errorcode-net-netfirewall.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Operation failed. Cannot connect to service. |
| 2100003 | System internal error. |
| 29400000 | The specified user does not exist. |

**示例：**

```
1. import { netFirewall } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let policy: netFirewall.NetFirewallPolicy = {
5. isOpen: true,
6. inAction: netFirewall.FirewallRuleAction.RULE_DENY,
7. outAction: netFirewall.FirewallRuleAction.RULE_ALLOW
8. };
9. netFirewall.setNetFirewallPolicy(100, policy).then(() => {
10. console.info("set firewall policy success.");
11. }).catch((error : BusinessError) => {
12. console.error("set firewall policy failed: " + JSON.stringify(error));
13. });
```

## netFirewall.getNetFirewallPolicy

PC/2in1

getNetFirewallPolicy(userId: number): Promise<NetFirewallPolicy>

查询系统用户ID的防火墙策略，包含防火墙开关状态，默认出站入站行为（允许/阻止）。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NET\_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 系统用户ID，只能是存在的用户ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetFirewallPolicy](js-apis-net-netfirewall.md#netfirewallpolicy)> | 以Promise形式返回当前用户防火墙策略。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[网络连接管理错误码](errorcode-net-connection.md)和[防火墙错误码](errorcode-net-netfirewall.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Operation failed. Cannot connect to service. |
| 2100003 | System internal error. |
| 29400000 | The specified user does not exist. |

**示例：**

```
1. import { netFirewall } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. netFirewall.getNetFirewallPolicy(100).then((result: netFirewall.NetFirewallPolicy) => {
5. console.info('firewall policy: ', JSON.stringify(result));
6. }, (reason: BusinessError) => {
7. console.error('get firewall policy failed: ', JSON.stringify(reason));
8. });
```

## netFirewall.addNetFirewallRule

PC/2in1

addNetFirewallRule(rule: NetFirewallRule): Promise<number>

添加系统用户ID的防火墙规则，目前支持的规则类型有：IP、Domain、DNS。使用Promise异步回调。

说明

1. 防火墙规则优先级说明（[setNetFirePolicy](js-apis-net-netfirewall.md#netfirewallsetnetfirewallpolicy)和[addNetFirewallRule](js-apis-net-netfirewall.md#netfirewalladdnetfirewallrule)无调用顺序要求）：

   * 调用[setNetFirePolicy](js-apis-net-netfirewall.md#netfirewallsetnetfirewallpolicy)设置默认策略为阻止，调用[addNetFirewallRule](js-apis-net-netfirewall.md#netfirewalladdnetfirewallrule)新增显式规则，规则优先级由高到低为：

     + 显式阻止规则
     + 显式允许规则
     + 默认阻止策略
   * 调用[setNetFirePolicy](js-apis-net-netfirewall.md#netfirewallsetnetfirewallpolicy)设置默认策略为允许，调用[addNetFirewallRule](js-apis-net-netfirewall.md#netfirewalladdnetfirewallrule)新增显式规则，规则优先级由高到低为：

     + 显式允许规则
     + 显式阻止规则
     + 默认允许策略
   * 防火墙IP规则和域名规则冲突时（域名解析的IP与IP规则的IP相同，规则行为冲突）：

     + 若以域名方式访问，则域名规则优先级高于IP规则，不受域名解析出的IP的规则影响。
     + 若以IP方式访问，遵循以下原则：

       - 域名规则放行，若以IP方式访问之前经历过域名解析过程，则IP规则拦截或者默认策略拦截是不生效的，最终以IP方式访问是放行的。
       - 域名规则放行，若以IP方式访问之前未经历过域名解析过程，则IP规则拦截或者默认策略拦截是生效的，最终以IP方式访问是拦截的。
       - 域名规则拦截，则IP规则放行或者默认策略放行是生效的，最终以IP方式访问是放行的。
2. 规则类型补充说明：

   * 当addNetFirewallRule的入参rule.type配置为RULE\_IP时：

     + 若rule.action为RULE\_ALLOW，且rule.localIps、rule.remoteIps均不配置，规则生效为全IP段允许通行；
     + 若rule.action 为RULE\_DENY，且rule.localIps、rule.remoteIps均不配置，规则生效为全IP段拦截。
   * 当addNetFirewallRule的入参rule.type配置为RULE\_DOMAIN时，若rule.domains未配置，该规则不生效。
3. 防火墙规则添加上限说明：

   * 单个系统用户ID添加的防火墙规则上限是1000，若超过该上限，则报错29400001。
   * 所有的系统用户ID添加的防火墙规则总和的上限是2000，若超过该上限，则报错29400001。
   * 所有的系统用户ID添加的模糊域名规则总和的上限是100，若超过该上限，则报错29400005。

**需要权限**：ohos.permission.MANAGE\_NET\_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rule | [NetFirewallRule](js-apis-net-netfirewall.md#netfirewallrule) | 是 | 防火墙规则。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回防火墙规则ID，防火墙规则ID由系统自动生成。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[网络连接管理错误码](errorcode-net-connection.md)和[防火墙错误码](errorcode-net-netfirewall.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Operation failed. Cannot connect to service. |
| 2100003 | System internal error. |
| 29400000 | The specified user does not exist. |
| 29400001 | The number of firewall rules exceeds the maximum. |
| 29400002 | The number of IP address rules in the firewall rule exceeds the maximum. |
| 29400003 | The number of port rules in the firewall rule exceeds the maximum. |
| 29400004 | The number of domain rules in the firewall rule exceeds the maximum. |
| 29400005 | The number of domain rules exceeds the maximum. |
| 29400007 | The dns rule is duplication. |

**示例：**

```
1. import { netFirewall } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ipRule: netFirewall.NetFirewallRule = {
5. name: "rule1",
6. description: "rule1 description",
7. direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
8. action:netFirewall.FirewallRuleAction.RULE_DENY,
9. type: netFirewall.NetFirewallRuleType.RULE_IP,
10. isEnabled: true,
11. appUid: 20001,
12. localIps: [
13. {
14. family: 1,
15. type: 1,
16. address: "10.10.1.1",
17. mask: 32
18. },{
19. family: 1,
20. type: 2,
21. startIp: "10.20.1.1",
22. endIp: "10.20.1.10"
23. }],
24. remoteIps:[
25. {
26. family: 1,
27. type: 1,
28. address: "20.10.1.1",
29. mask: 32
30. },{
31. family: 1,
32. type: 2,
33. startIp: "20.20.1.1",
34. endIp: "20.20.1.10"
35. }],
36. protocol: 6,
37. localPorts: [
38. {
39. startPort: 1000,
40. endPort: 1000
41. },{
42. startPort: 2000,
43. endPort: 2001
44. }],
45. remotePorts: [
46. {
47. startPort: 443,
48. endPort: 443
49. }],
50. userId: 100
51. };
52. netFirewall.addNetFirewallRule(ipRule).then((result: number) => {
53. console.info('rule Id: ', result);
54. }, (reason: BusinessError) => {
55. console.error('add firewall rule failed: ', JSON.stringify(reason));
56. });

58. let domainRule: netFirewall.NetFirewallRule = {
59. name: "rule2",
60. description: "rule2 description",
61. direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
62. action:netFirewall.FirewallRuleAction.RULE_DENY,
63. type: netFirewall.NetFirewallRuleType.RULE_DOMAIN,
64. isEnabled: true,
65. appUid: 20002,
66. domains: [
67. {
68. isWildcard: false,
69. domain: "www.example.cn"
70. },{
71. isWildcard: true,
72. domain: "*.example.cn"
73. }],
74. userId: 100
75. };
76. netFirewall.addNetFirewallRule(domainRule).then((result: number) => {
77. console.info('rule Id: ', result);
78. }, (reason: BusinessError) => {
79. console.error('add firewall rule failed: ', JSON.stringify(reason));
80. });

82. let dnsRule: netFirewall.NetFirewallRule = {
83. name: "rule3",
84. description: "rule3 description",
85. direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
86. action:netFirewall.FirewallRuleAction.RULE_DENY,
87. type: netFirewall.NetFirewallRuleType.RULE_DNS,
88. isEnabled: true,
89. appUid: 20003,
90. dns:{
91. primaryDns: "4.4.4.4",
92. standbyDns: "8.8.8.8",
93. },
94. userId: 100
95. };
96. netFirewall.addNetFirewallRule(dnsRule).then((result: number) => {
97. console.info('rule Id: ', result);
98. }, (reason: BusinessError) => {
99. console.error('add firewall rule failed: ', JSON.stringify(reason));
100. });
```

## netFirewall.removeNetFirewallRule

PC/2in1

removeNetFirewallRule(userId: number, ruleId: number): Promise<void>

删除系统用户ID的指定防火墙规则。使用Promise异步回调。

**需要权限**：ohos.permission.MANAGE\_NET\_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 系统用户ID，只能是存在的用户ID。 |
| ruleId | number | 是 | 防火墙规则ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[网络连接管理错误码](errorcode-net-connection.md)和[防火墙错误码](errorcode-net-netfirewall.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Operation failed. Cannot connect to service. |
| 2100003 | System internal error. |
| 29400000 | The specified user does not exist. |
| 29400006 | The specified rule does not exist. |

**示例：**

```
1. import { netFirewall } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. netFirewall.removeNetFirewallRule(100, 1).then(() => {
5. console.info("delete firewall rule success.");
6. }).catch((error : BusinessError) => {
7. console.error("delete firewall rule failed: " + JSON.stringify(error));
8. });
```

## netFirewall.updateNetFirewallRule

PC/2in1

updateNetFirewallRule(rule: NetFirewallRule): Promise<void>

更新防火墙规则。使用Promise异步回调。

**需要权限**：ohos.permission.MANAGE\_NET\_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rule | [NetFirewallRule](js-apis-net-netfirewall.md#netfirewallrule) | 是 | 防火墙规则。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[网络连接管理错误码](errorcode-net-connection.md)和[防火墙错误码](errorcode-net-netfirewall.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Operation failed. Cannot connect to service. |
| 2100003 | System internal error. |
| 29400000 | The specified user does not exist. |
| 29400002 | The number of IP address rules in the firewall rule exceeds the maximum. |
| 29400003 | The number of port rules in the firewall rule exceeds the maximum. |
| 29400004 | The number of domain rules in the firewall rule exceeds the maximum. |
| 29400005 | The number of domain rules exceeds the maximum. |
| 29400006 | The specified rule does not exist. |
| 29400007 | The dns rule is duplication. |

**示例：**

```
1. import { netFirewall } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ipRuleUpd: netFirewall.NetFirewallRule = {
5. id: 1,
6. name: "rule1",
7. description: "rule1 description update",
8. direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
9. action:netFirewall.FirewallRuleAction.RULE_DENY,
10. type: netFirewall.NetFirewallRuleType.RULE_IP,
11. isEnabled: false,
12. appUid: 20001,
13. localIps: [
14. {
15. family: 1,
16. type: 1,
17. address: "10.10.1.1",
18. mask: 32
19. },{
20. family: 1,
21. type: 2,
22. startIp: "10.20.1.1",
23. endIp: "10.20.1.10"
24. }],
25. userId: 100
26. };
27. netFirewall.updateNetFirewallRule(ipRuleUpd).then(() => {
28. console.info('update firewall rule success.');
29. }, (reason: BusinessError) => {
30. console.error('update firewall rule failed: ', JSON.stringify(reason));
31. });
```

## netFirewall.getNetFirewallRules

PC/2in1

getNetFirewallRules(userId: number, requestParam: RequestParam): Promise<FirewallRulePage>

按用户ID获取防火墙规则，需要指定分页查询参数。目前支持根据防火墙规则名排序。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NET\_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 系统用户ID，只能是存在的用户ID。 |
| requestParam | [RequestParam](js-apis-net-netfirewall.md#requestparam) | 是 | 分页查询参数，其中orderField字段仅支持根据防火墙规则名排序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FirewallRulePage](js-apis-net-netfirewall.md#firewallrulepage)> | 以Promise形式返回防火墙分页规则列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[网络连接管理错误码](errorcode-net-connection.md)和[防火墙错误码](errorcode-net-netfirewall.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Operation failed. Cannot connect to service. |
| 2100003 | System internal error. |
| 29400000 | The specified user does not exist. |

**示例：**

```
1. import { netFirewall } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ruleParam: netFirewall.RequestParam = {
5. page: 1,
6. pageSize: 10,
7. orderField: netFirewall.NetFirewallOrderField.ORDER_BY_RULE_NAME,
8. orderType: netFirewall.NetFirewallOrderType.ORDER_ASC
9. };
10. netFirewall.getNetFirewallRules(100, ruleParam).then((result: netFirewall.FirewallRulePage) => {
11. console.info("result:", JSON.stringify(result));
12. }, (error: BusinessError) => {
13. console.error("get firewall rules failed: " + JSON.stringify(error));
14. });
```

## netFirewall.getNetFirewallRule

PC/2in1

getNetFirewallRule(userId: number, ruleId: number): Promise<NetFirewallRule>

通过userId和ruleId获取指定的防火墙规则。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NET\_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 系统用户ID，只能是存在的用户ID。 |
| ruleId | number | 是 | 防火墙规则ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetFirewallRule](js-apis-net-netfirewall.md#netfirewallrule)> | 以Promise形式返回防火墙规则。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[网络连接管理错误码](errorcode-net-connection.md)和[防火墙错误码](errorcode-net-netfirewall.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Operation failed. Cannot connect to service. |
| 2100003 | System internal error. |
| 29400000 | The specified user does not exist. |
| 29400006 | The specified rule does not exist. |

**示例：**

```
1. import { netFirewall } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. netFirewall.getNetFirewallRule(100, 1).then((rule: netFirewall.NetFirewallRule) => {
5. console.info("result:", JSON.stringify(rule));
6. }).catch((error : BusinessError) => {
7. console.error(" get firewall rules failed: " + JSON.stringify(error));
8. });
```

## NetFirewallRule

PC/2in1

防火墙规则信息结构。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| userId | number | 否 | 否 | 系统用户ID，只能是存在的用户ID。 |
| name | string | 否 | 否 | 规则名称，必填，最多128个字符。 |
| direction | [NetFirewallRuleDirection](js-apis-net-netfirewall.md#netfirewallruledirection) | 否 | 否 | 规则方向，包含入站和出站。 |
| action | [FirewallRuleAction](js-apis-net-netfirewall.md#firewallruleaction) | 否 | 否 | 行为，包含允许和阻止。 |
| type | [NetFirewallRuleType](js-apis-net-netfirewall.md#netfirewallruletype) | 否 | 否 | 规则类型，包含IP、Domain、DNS。 |
| isEnabled | boolean | 否 | 否 | 是否启用规则。true表示启用，false表示不启用。 |
| id | number | 否 | 是 | 防火墙规则的ID。 |
| description | string | 否 | 是 | 规则描述，可选，最多256个字符。 |
| appUid | number | 否 | 是 | 应用程序或服务UID。 |
| localIps | Array<[NetFirewallIpParams](js-apis-net-netfirewall.md#netfirewallipparams)> | 否 | 是 | 本地IP地址。当type=RULE\_IP时有效，否则将被忽略，最多10个。 |
| remoteIps | Array<[NetFirewallIpParams](js-apis-net-netfirewall.md#netfirewallipparams)> | 否 | 是 | 远端IP地址。当type=RULE\_IP时有效，否则将被忽略，最多10个。 |
| protocol | number | 否 | 是 | 协议，包含TCP：6，UDP：17。当type=RULE\_IP时有效。 |
| localPorts | Array<[NetFirewallPortParams](js-apis-net-netfirewall.md#netfirewallportparams)> | 否 | 是 | 本地端口。当type=RULE\_IP时有效，否则将被忽略，最多10个。 |
| remotePorts | Array<[NetFirewallPortParams](js-apis-net-netfirewall.md#netfirewallportparams)> | 否 | 是 | 远端端口。当type=RULE\_IP时有效，否则将被忽略。最多10个。 |
| domains | Array<[NetFirewallDomainParams](js-apis-net-netfirewall.md#netfirewalldomainparams)> | 否 | 是 | 域名列表，当type=RULE\_DOMAIN时有效，否则将被忽略，目前不支持中文域名。 |
| dns | [NetFirewallDnsParams](js-apis-net-netfirewall.md#netfirewalldnsparams) | 否 | 是 | DNS：当type=RULE\_DNS时有效，否则将被忽略。当type=RULE\_DNS时，该字段不能为空。 |

## RequestParam

PC/2in1

查询输入信息结构。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| page | number | 否 | 否 | 页码，值范围：[1, 1000]。 |
| pageSize | number | 否 | 否 | 页面大小，值范围：[1, 50]。 |
| orderField | [NetFirewallOrderField](js-apis-net-netfirewall.md#netfirewallorderfield) | 否 | 否 | 排序方法。 该字段仅支持根据防火墙规则名排序。 |
| orderType | [NetFirewallOrderType](js-apis-net-netfirewall.md#netfirewallordertype) | 否 | 否 | 排序顺序。 |

## FirewallRulePage

PC/2in1

防火墙规则页信息结构。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| page | number | 否 | 否 | 当前页码，值范围：[1,1000]。 |
| pageSize | number | 否 | 否 | 页大小，值范围：[1,50]。 |
| totalPage | number | 否 | 否 | 总页数，值范围：[1,1000]。 |
| data | Array<[NetFirewallRule](js-apis-net-netfirewall.md#netfirewallrule)> | 否 | 否 | 页面数据。 |

## NetFirewallPolicy

PC/2in1

防火墙策略，包含防火墙开关状态，默认的出站/入站行为（允许/阻止）。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isOpen | boolean | 否 | 否 | 是否开启防火墙。true表示开启防火墙，false表示关闭防火墙。 |
| inAction | [FirewallRuleAction](js-apis-net-netfirewall.md#firewallruleaction) | 否 | 否 | 入站行为。 |
| outAction | [FirewallRuleAction](js-apis-net-netfirewall.md#firewallruleaction) | 否 | 否 | 出站行为。 |

## NetFirewallRuleDirection

PC/2in1

枚举类型，防火墙规则方向，包含入站、出站。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RULE\_IN | 1 | 入站。 |
| RULE\_OUT | 2 | 出站。 |

## FirewallRuleAction

PC/2in1

枚举类型，防火墙规则行为，包含允许网络连接、阻止网络连接。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RULE\_ALLOW | 0 | 允许。 |
| RULE\_DENY | 1 | 阻止。 |

## NetFirewallRuleType

PC/2in1

枚举类型，防火墙规则类型，包含IP、Domain、DNS。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RULE\_IP | 1 | IP类规则。 |
| RULE\_DOMAIN | 2 | 域名类规则。 |
| RULE\_DNS | 3 | DNS规则。 |

## NetFirewallOrderField

PC/2in1

枚举类型，防火墙规则排序方法。

说明

[getNetFirewallRules](js-apis-net-netfirewall.md#netfirewallgetnetfirewallrules)接口，仅支持ORDER\_BY\_RULE\_NAME字段。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORDER\_BY\_RULE\_NAME | 1 | 根据防火墙规则名排序。 |
| ORDER\_BY\_RECORD\_TIME | 100 | 根据记录时间排序。 |

## NetFirewallOrderType

PC/2in1

枚举类型，防火墙规则排序顺序，包含升序或降序。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORDER\_ASC | 1 | 按防火墙规则排序类型升序排序。 |
| ORDER\_DESC | 100 | 按防火墙规则排序类型降序排序。 |

## NetFirewallIpParams

PC/2in1

防火墙规则的IP参数，IP类型包括IPv4、IPv6，支持单个IP或IP段。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | number | 否 | 否 | 1：IP地址或子网。该场景下必须指定address和mask字段，当使用单个IP时，mask字段需设置为32。  2：IP段，该场景下必须指定startIp和endIp字段。 |
| family | number | 否 | 是 | 1：表示family地址族设置为IPv4。  2：表示family地址族设置为IPv6。  默认IPv4，其他当前不支持。 |
| address | string | 否 | 是 | IP地址。当type等于1时需要设置，并且仅在type等于1时有效，否则将被忽略。 |
| mask | number | 否 | 是 | IPv4：子网掩码。  IPv6：前缀。  当type等于1时需要设置，并且仅在type等于1时有效，否则将被忽略。 |
| startIp | string | 否 | 是 | 起始IP。当type等于2时需要设置，并且仅在type等于2时有效，范围从0.0.0.1到255.255.255.254，否则将被忽略。 |
| endIp | string | 否 | 是 | 结束IP。当type等于2时需要设置，并且仅在type等于2时有效，范围从0.0.0.1到255.255.255.254，否则将被忽略。 |

## NetFirewallPortParams

PC/2in1

防火墙规则端口参数。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startPort | number | 否 | 否 | 开始端口。 |
| endPort | number | 否 | 否 | 结束端口。 |

## NetFirewallDomainParams

PC/2in1

防火墙规则域名参数，目前不支持中文域名。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isWildcard | boolean | 否 | 否 | 是否包含通配符。true表示包含，false表示不包含。 |
| domain | string | 否 | 否 | 当isWildcard为false时，需要确定的完整域， 例如"[www.example.cn"。](http://www.example.cn) |

## NetFirewallDnsParams

PC/2in1

防火墙规则DNS信息。

说明

当[addNetFirewallRule](js-apis-net-netfirewall.md#netfirewalladdnetfirewallrule)的入参rule.type配置为RULE\_DNS时，该字段不能为空。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primaryDns | string | 否 | 否 | 主域名服务器。 |
| standbyDns | string | 否 | 是 | 备份DNS。 |
| \*\* |  |  |  |  |
