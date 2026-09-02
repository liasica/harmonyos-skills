---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-netfirewall
title: "@ohos.net.netFirewall (网络防火墙)"
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.netFirewall (网络防火墙)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3c052aa6e8d4c8120d42261d978399714a8c33d775776bfc4f241a491831a53f
---

本模块为应用程序提供网络防火墙能力。应用程序可以对机器进行防火墙拦截记录的查询。

**说明** 

本模块首批接口从API version 15开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { netFirewall } from '@kit.NetworkKit';
```

## netFirewall.setNetFirewallPolicy

setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>

设置系统用户ID的防火墙策略，包含防火墙开关状态，默认的出站/入站行为（允许/阻止）。支持不同的系统用户ID配置不同的防火墙策略。使用Promise异步回调。

**说明** 

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

```ts
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let policy: netFirewall.NetFirewallPolicy = {
  isOpen: true,
  inAction: netFirewall.FirewallRuleAction.RULE_DENY,
  outAction: netFirewall.FirewallRuleAction.RULE_ALLOW
};
netFirewall.setNetFirewallPolicy(100, policy).then(() => {
  console.info("set firewall policy success.");
}).catch((error : BusinessError) => {
  console.error("set firewall policy failed: " + JSON.stringify(error));
});
```

## netFirewall.getNetFirewallPolicy

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

```ts
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

netFirewall.getNetFirewallPolicy(100).then((result: netFirewall.NetFirewallPolicy) => {
  console.info('firewall policy: ', JSON.stringify(result));
}, (reason: BusinessError) => {
  console.error('get firewall policy failed: ', JSON.stringify(reason));
});
```

## netFirewall.addNetFirewallRule

addNetFirewallRule(rule: NetFirewallRule): Promise<number>

添加系统用户ID的防火墙规则，目前支持的规则类型有：IP、Domain、DNS。使用Promise异步回调。

**说明** 

1. 防火墙规则优先级说明（[setNetFirewallPolicy](js-apis-net-netfirewall.md#netfirewallsetnetfirewallpolicy)和[addNetFirewallRule](js-apis-net-netfirewall.md#netfirewalladdnetfirewallrule)无调用顺序要求）：

   * 调用[setNetFirewallPolicy](js-apis-net-netfirewall.md#netfirewallsetnetfirewallpolicy)设置默认策略为阻止，调用[addNetFirewallRule](js-apis-net-netfirewall.md#netfirewalladdnetfirewallrule)新增显式规则，规则优先级由高到低为：
     + 显式阻止规则
     + 显式允许规则
     + 默认阻止策略
   * 调用[setNetFirewallPolicy](js-apis-net-netfirewall.md#netfirewallsetnetfirewallpolicy)设置默认策略为允许，调用[addNetFirewallRule](js-apis-net-netfirewall.md#netfirewalladdnetfirewallrule)新增显式规则，规则优先级由高到低为：
     + 显式允许规则
     + 显式阻止规则
     + 默认允许策略
   * 防火墙IP规则和域名规则冲突时（域名解析的IP与IP规则的IP相同，规则行为冲突）：
     + 若以域名方式访问，则域名规则优先级高于IP规则，不受域名解析出的IP的规则影响。
     + 若以IP方式访问，遵循以下原则：
       - 域名规则放行时，IP规则或默认策略的拦截均不生效，最终以IP方式访问放行。
       - 域名规则拦截时，IP规则或默认策略的放行仍生效，最终以IP方式访问放行。
     + 系统侧识别域名访问与IP访问的方式：
       - 若目标IP与系统网络层域名缓存表中的IP地址匹配，则认为应用侧以域名形式访问；
       - 若目标IP未匹配上系统网络层域名缓存表中的任意IP地址，则认为应用侧以IP形式访问；
       - 其中，系统网络层会主动查询防火墙配置的DNS信息，并缓存对应的IP地址，使域名放行规则生效。
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

```ts
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ipRule: netFirewall.NetFirewallRule = {
  name: "rule1",
  description: "rule1 description",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_IP,
  isEnabled: true,
  appUid: 20001,
  localIps: [
    {
      family: 1,
      type: 1,
      address: "10.10.1.1",
      mask: 32
    },{
      family: 1,
      type: 2,
      startIp: "10.20.1.1",
      endIp: "10.20.1.10"
    }],
  remoteIps:[
    {
      family: 1,
      type: 1,
      address: "20.10.1.1",
      mask: 32
    },{
      family: 1,
      type: 2,
      startIp: "20.20.1.1",
      endIp: "20.20.1.10"
    }],
  protocol: 6,
  localPorts: [
    {
      startPort: 1000,
      endPort: 1000
    },{
      startPort: 2000,
      endPort: 2001
    }],
  remotePorts: [
    {
      startPort: 443,
      endPort: 443
    }],
  userId: 100,
  interface:"wlan0" // 从API版本26.0.0开始支持
};
netFirewall.addNetFirewallRule(ipRule).then((result: number) => {
  console.info('rule Id: ', result);
}, (reason: BusinessError) => {
  console.error('add firewall rule failed: ', JSON.stringify(reason));
});

let domainRule: netFirewall.NetFirewallRule = {
  name: "rule2",
  description: "rule2 description",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_DOMAIN,
  isEnabled: true,
  appUid: 20002,
  domains: [
    {
      isWildcard: false,
      domain: "www.example.cn"
    },{
      isWildcard: true,
      domain: "*.example.cn"
    },{
      isWildcard: true,
      domain: "*w.example.cn"  // 从API版本26.0.0开始支持
    },{
      isWildcard: true,
      domain: "www.example.*"  // 从API版本26.0.0开始支持
    },{
      isWildcard: true,
      domain: "www.example.c*"  // 从API版本26.0.0开始支持
    }],
  userId: 100,
  interface:"wlan0" // 从API版本26.0.0开始支持
};
netFirewall.addNetFirewallRule(domainRule).then((result: number) => {
  console.info('rule Id: ', result);
}, (reason: BusinessError) => {
  console.error('add firewall rule failed: ', JSON.stringify(reason));
});

let dnsRule: netFirewall.NetFirewallRule = {
  name: "rule3",
  description: "rule3 description",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_DNS,
  isEnabled: true,
  appUid: 20003,
  dns:{
   primaryDns: "4.4.4.4",
   standbyDns: "8.8.8.8",
  },
  userId: 100,
  interface:"wlan0" // 从API版本26.0.0开始支持
};
netFirewall.addNetFirewallRule(dnsRule).then((result: number) => {
  console.info('rule Id: ', result);
}, (reason: BusinessError) => {
  console.error('add firewall rule failed: ', JSON.stringify(reason));
});
```

## netFirewall.removeNetFirewallRule

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

```ts
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

netFirewall.removeNetFirewallRule(100, 1).then(() => {
  console.info("delete firewall rule success.");
}).catch((error : BusinessError) => {
  console.error("delete firewall rule failed: " + JSON.stringify(error));
});
```

## netFirewall.updateNetFirewallRule

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

```ts
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ipRuleUpd: netFirewall.NetFirewallRule = {
  id: 1,
  name: "rule1",
  description: "rule1 description update",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_IP,
  isEnabled: false,
  appUid: 20001,
  localIps: [
    {
      family: 1,
      type: 1,
      address: "10.10.1.1",
      mask: 32
    },{
      family: 1,
      type: 2,
      startIp: "10.20.1.1",
      endIp: "10.20.1.10"
    }],
  userId: 100,
  interface:"wlan0" // 从API版本26.0.0开始支持
};
netFirewall.updateNetFirewallRule(ipRuleUpd).then(() => {
  console.info('update firewall rule success.');
}, (reason: BusinessError) => {
  console.error('update firewall rule failed: ', JSON.stringify(reason));
});
```

## netFirewall.getNetFirewallRules

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

```ts
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ruleParam: netFirewall.RequestParam = {
  page: 1,
  pageSize: 10,
  orderField: netFirewall.NetFirewallOrderField.ORDER_BY_RULE_NAME,
  orderType: netFirewall.NetFirewallOrderType.ORDER_ASC
};
netFirewall.getNetFirewallRules(100, ruleParam).then((result: netFirewall.FirewallRulePage) => {
  console.info("result:", JSON.stringify(result));
}, (error: BusinessError) => {
  console.error("get firewall rules failed: " + JSON.stringify(error));
});
```

## netFirewall.getNetFirewallRule

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

```ts
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

netFirewall.getNetFirewallRule(100, 1).then((rule: netFirewall.NetFirewallRule) => {
  console.info("result:", JSON.stringify(rule));
}).catch((error : BusinessError) => {
  console.error(" get firewall rules failed: " + JSON.stringify(error));
});
```

## NetFirewallRule

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
| interface | string | 否 | 是 | 物理网卡名称，例如wlan0。当type=RULE\_IP时有效，否则将被忽略。可选，最多16个字符。  **起始版本**：26.0.0  **模型约束**：此接口仅可在Stage模型下使用。 |

## RequestParam

查询输入信息结构。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| page | number | 否 | 否 | 页码，值范围：[1, 1000]。 |
| pageSize | number | 否 | 否 | 页面大小，值范围：[1, 50]。 |
| orderField | [NetFirewallOrderField](js-apis-net-netfirewall.md#netfirewallorderfield) | 否 | 否 | 排序方法。 该字段仅支持根据防火墙规则名排序。 |
| orderType | [NetFirewallOrderType](js-apis-net-netfirewall.md#netfirewallordertype) | 否 | 否 | 排序顺序。 |

## FirewallRulePage

防火墙规则页信息结构。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| page | number | 否 | 否 | 当前页码，值范围：[1,1000]。 |
| pageSize | number | 否 | 否 | 页大小，值范围：[1,50]。 |
| totalPage | number | 否 | 否 | 总页数，值范围：[1,1000]。 |
| data | Array<[NetFirewallRule](js-apis-net-netfirewall.md#netfirewallrule)> | 否 | 否 | 页面数据。 |

## NetFirewallPolicy

防火墙策略，包含防火墙开关状态，默认的出站/入站行为（允许/阻止）。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isOpen | boolean | 否 | 否 | 是否开启防火墙。true表示开启防火墙，false表示关闭防火墙。 |
| inAction | [FirewallRuleAction](js-apis-net-netfirewall.md#firewallruleaction) | 否 | 否 | 入站行为。 |
| outAction | [FirewallRuleAction](js-apis-net-netfirewall.md#firewallruleaction) | 否 | 否 | 出站行为。 |

## NetFirewallRuleDirection

枚举类型，防火墙规则方向，包含入站、出站。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RULE\_IN | 1 | 入站。 |
| RULE\_OUT | 2 | 出站。 |

## FirewallRuleAction

枚举类型，防火墙规则行为，包含允许网络连接、阻止网络连接。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RULE\_ALLOW | 0 | 允许。 |
| RULE\_DENY | 1 | 阻止。 |

## NetFirewallRuleType

枚举类型，防火墙规则类型，包含IP、Domain、DNS。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RULE\_IP | 1 | IP类规则。 |
| RULE\_DOMAIN | 2 | 域名类规则。 |
| RULE\_DNS | 3 | DNS规则。 |

## NetFirewallOrderField

枚举类型，防火墙规则排序方法。

**说明** 

[getNetFirewallRules](js-apis-net-netfirewall.md#netfirewallgetnetfirewallrules)接口，仅支持ORDER\_BY\_RULE\_NAME字段。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORDER\_BY\_RULE\_NAME | 1 | 根据防火墙规则名排序。 |
| ORDER\_BY\_RECORD\_TIME | 100 | 根据记录时间排序。 |

## NetFirewallOrderType

枚举类型，防火墙规则排序顺序，包含升序或降序。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORDER\_ASC | 1 | 按防火墙规则排序类型升序排序。 |
| ORDER\_DESC | 100 | 按防火墙规则排序类型降序排序。 |

## NetFirewallIpParams

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

防火墙规则端口参数。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startPort | number | 否 | 否 | 开始端口。 |
| endPort | number | 否 | 否 | 结束端口。 |

## NetFirewallDomainParams

防火墙规则域名参数，目前不支持中文域名。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isWildcard | boolean | 否 | 否 | 是否包含通配符。true表示包含，false表示不包含。 |
| domain | string | 否 | 否 | 当isWildcard为false时，需要确定的完整域， 例如"[www.example.cn"；当isWildcard为true时，支持通配符规则，具体格式见下文说明。](http://www.example.cn) |

当isWildcard为true时，domain支持使用通配符""，""可出现在域名的首部、尾部或首尾同时出现，表示匹配任意长度（包括零）的任意字符。支持以下通配符格式：

* "\*.xxx.xxx"：前缀通配，匹配xxx.xxx及其所有子域名。例如"\*.example.com"可匹配"example.com"、"[www.example.com"、"a.b.example.com"。（从API版本21开始支持）](http://www.example.com)
* "\*xx.xxx.xxx"：前缀通配，匹配以"xx.xxx.xxx"结尾的域名。例如"\*a.example.com"可匹配"a.example.com"、"[www.a.example.com"。（从API版本26.0.0开始支持）](http://www.a.example.com)
* "xxx.xxx.xxx.\*"：后缀通配，匹配以"xxx.xxx.xxx."开头的域名。例如"www.example.\*"可匹配"www.example.com"、"www.example.cn"。（从API版本26.0.0开始支持）
* "xxx.xxx.xxx.xx\*"：后缀通配，匹配以"xxx.xxx.xxx.xx"开头的域名。例如"www.example.co\*"可匹配"www.example.com"、"www.example.com.cn"。（从API版本26.0.0开始支持）

## NetFirewallDnsParams

防火墙规则DNS信息。

**说明** 

当[addNetFirewallRule](js-apis-net-netfirewall.md#netfirewalladdnetfirewallrule)的入参rule.type配置为RULE\_DNS时，该字段不能为空。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primaryDns | string | 否 | 否 | 主域名服务器。 |
| standbyDns | string | 否 | 是 | 备份DNS。 |
