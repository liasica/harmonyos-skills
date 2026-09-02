---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-netfirewall
title: 使用网络防火墙
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 管理网络 > 使用网络防火墙
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2443adb9da37575c7aded7018288832d6d75558ccb56d17c9873c07a8a64e8d4
---

## 简介

网络防火墙提供如下功能：

* 防火墙的基础能力，包括防火墙的使能、规则的启用与禁用、审计能力。
* 防火墙规则的配置能力，包括规则的名称、描述、操作、生效应用、协议类型、地址、端口、出站/入站方向等。
* DNS策略的配置能力，包括配置禁止/允许解析的域名、解析使用的DNS服务器（主选/备选）（应用级）。

**说明** 

为了保证应用的运行效率，所有API调用都是异步的，对于异步调用的API均提供了Promise的方式，以下示例均采用Promise方式，更多方式可以查阅[@ohos.net.netFirewall (网络防火墙)](../harmonyos-references/js-apis-net-netfirewall.md)。

## 场景介绍

防火墙的典型场景有：

* 针对特定IP联网访问控制

1. 支持限制特定应用访问网络。
2. 支持限制对特定IP、特定协议、特定端口、特定物理网卡的网络通信。
3. 支持限制特定应用对特定IP、特定协议、特定端口、特定物理网卡的网络通信。
4. 支持拦截规则下发后立即生效（此点针对TCP协议：需断开已有被拦截的TCP连接）。

* 针对域名联网访问控制支持拦截

1. 支持限制应用对特定域名的DNS解析能力（仅限制非加密标准DNS协议，不限制加密、私有DNS协议）。
2. 支持限制特定应用对特定域名的DNS解析能力（仅限制非加密标准DNS协议，不限制加密、私有DNS协议）。
3. 支持拦截规则下发后立即生效（此点针对TCP协议：需断开已有被拦截的TCP连接）。

以下分别介绍具体开发方式。

## 针对特定IP联网访问控制

1. 设备通过硬件接口，插入网线。
2. 从@kit.NetworkKit中导入netfirewall命名空间。

   ```typescript
   // 从@kit.NetworkKit中导入netFirewall命名空间。
   import { netFirewall } from '@kit.NetworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
3. 用户调用setNetFirewallPolicy方法，打开防火墙。

   ```typescript
   // IP类型
   interface IpType{
     family:number;
     type:number;
     address?:string;
     mask?:number;
     startIp?:string;
     endIp?:string;
   }
   // IP端口
   interface IpPort{
     startPort:number;
     endPort:number;
   }
   // ...
       // 定义防火墙策略：打开，入站阻止，出站允许。
       let policy: netFirewall.NetFirewallPolicy = {
         isOpen: true,
         inAction: netFirewall.FirewallRuleAction.RULE_DENY,
         outAction: netFirewall.FirewallRuleAction.RULE_ALLOW
       };

       // 给用户100设置防火墙策略。
       netFirewall.setNetFirewallPolicy(100, policy).then(() => {
         hilog.info(0x0000, 'testTag', `set firewall policy success.`);
       }).catch((error : BusinessError) => {
         hilog.error(0x0000, 'testTag', `error: set firewall policy failed: ${JSON.stringify(error)}`);
       });
   ```
4. 用户通过addNetFirewallRule方法，添加防火墙规则。

   ```typescript
   // 初始化具体的防火墙ip类型规则。
   let ipRule: netFirewall.NetFirewallRule = {
     name: 'rule1',
     description: 'rule1 description',
     direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
     action: netFirewall.FirewallRuleAction.RULE_DENY,
     type: netFirewall.NetFirewallRuleType.RULE_IP,
     isEnabled: true,
     appUid: 20001,
     localIps: [
       {
         family: 1,
         type: 1,
         address: '10.10.1.1',
         mask: 32
       },{
       family: 1,
       type: 2,
       startIp: '10.20.1.1',
       endIp: '10.20.1.10'
     }] as IpType[],
     remoteIps:[
       {
         family: 1,
         type: 1,
         address: '20.10.1.1',
         mask: 32
       },{
       family: 1,
       type: 2,
       startIp: '20.20.1.1',
       endIp: '20.20.1.10'
     }] as IpType[],
     protocol: 6,
     localPorts: [
       {
         startPort: 1000,
         endPort: 1000
       },{
       startPort: 2000,
       endPort: 2001
     }] as IpPort[],
     remotePorts: [
       {
         startPort: 443,
         endPort: 443
       }] as IpPort[],
     userId: 100,
     interface:'wlan0' // 从API版本26.0.0开始支持
   };
   // 添加防火墙规则。
   netFirewall.addNetFirewallRule(ipRule).then((result: number) => {
     // ...
     hilog.info(0x0000, 'testTag', `rule Id: ${result}`);
   }, (reason: BusinessError) => {
     // ...
     hilog.error(0x0000, 'testTag', `error: add firewall rule failed:  ${JSON.stringify(reason)}`);
   });
   ```

## 针对域名联网访问控制支持拦截

1. 设备通过硬件接口，插入网线。
2. 从@kit.NetworkKit中导入netFirewall命名空间。

   ```typescript
   // 从@kit.NetworkKit中导入netFirewall命名空间。
   import { netFirewall } from '@kit.NetworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
3. 调用setNetFirewallPolicy方法，打开防火墙。

   ```typescript
   interface domain{
     isWildcard: boolean;
     domain: string;
   }
   // ...
       // 定义防火墙策略：打开，入站阻止，出站允许。
       let policy: netFirewall.NetFirewallPolicy = {
         isOpen: true,
         inAction: netFirewall.FirewallRuleAction.RULE_DENY,
         outAction: netFirewall.FirewallRuleAction.RULE_ALLOW
       };

       // 给用户100设置防火墙策略
       netFirewall.setNetFirewallPolicy(100, policy).then(() => {
         hilog.info(0x0000, 'testTag', `set firewall policy success.`);
       }).catch((error : BusinessError) => {
         hilog.error(0x0000, 'testTag', `error: set firewall policy failed: ${JSON.stringify(error)}`);
       });
   ```
4. 通过addNetFirewallRule方法，添加防火墙规则。

   ```typescript
   // 初始化具体的防火墙域名类型规则。
   let domainRule: netFirewall.NetFirewallRule = {
     name: 'rule2',
     description: 'rule2 description',
     direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
     action: netFirewall.FirewallRuleAction.RULE_DENY,
     type: netFirewall.NetFirewallRuleType.RULE_DOMAIN,
     isEnabled: true,
     appUid: 20002,
     domains: [
       {
         isWildcard: false,
         domain: 'www.HarmonyOS.cn'
       },{
         isWildcard: true,
         domain: '*.HarmonyOS.cn'
       },{
         isWildcard: true,
         domain: '*w.HarmonyOS.cn' // 从API版本26.0.0开始支持
       },{
         isWildcard: true,
         domain: 'www.HarmonyOS.*' // 从API版本26.0.0开始支持
       },{
         isWildcard: true,
         domain: 'www.HarmonyOS.c*' // 从API版本26.0.0开始支持
     }] as domain[],
     userId: 100,
     interface:'wlan0' // 从API版本26.0.0开始支持
   };

   // 添加防火墙规则。
   netFirewall.addNetFirewallRule(domainRule).then((result: number) => {
     // ...
     hilog.info(0x0000, 'testTag', `rule Id: ${result}`);
   }, (reason: BusinessError) => {
     // ...
     hilog.error(0x0000, 'testTag', `error: add firewall rule failed:  ${JSON.stringify(reason)}`);
   });
   ```
