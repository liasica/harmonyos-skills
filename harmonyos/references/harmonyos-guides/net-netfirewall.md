---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-netfirewall
title: 使用网络防火墙
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 管理网络 > 使用网络防火墙
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2fb7ade586feeec1a0f4692431b8a9dc71d2b00d902afdec1b9a0efb9fb019f5
---

## 简介

网络防火墙提供如下功能：

* 防火墙的基础能力，包括防火墙的使能、规则的启用与禁用、审计能力。
* 防火墙规则的配置能力，包括规则的名称、描述、操作、生效应用、协议类型、地址、端口、出站/入站方向等。
* DNS策略的配置能力，包括配置禁止/允许解析的域名、解析使用的DNS服务器（主选/备选）（应用级）。

说明

为了保证应用的运行效率，所有API调用都是异步的，对于异步调用的API均提供了Promise的方式，以下示例均采用Promise方式，更多方式可以查阅[@ohos.net.netFirewall (网络防火墙)](../harmonyos-references/js-apis-net-netfirewall.md)。

## 场景介绍

防火墙的典型场景有：

* 针对特定IP联网访问控制

1. 支持限制特定应用访问网络。
2. 支持限制对特定IP、特定协议、特定端口的网络通信。
3. 支持限制特定应用对特定IP、特定协议、特定端口的网络通信。
4. 支持拦截规则下发后立即生效（此点针对TCP协议：需断开已有被拦截的TCP连接）。

* 针对域名联网访问控制支持拦截

1. 支持限制应用对特定域名的DNS解析能力（仅限制非加密标准DNS协议，不限制加密、私有DNS协议）。
2. 支持限制特定应用对特定域名的DNS解析能力（仅限制非加密标准DNS协议，不限制加密、私有DNS协议）。
3. 支持拦截规则下发后立即生效（此点针对TCP协议：需断开已有被拦截的TCP连接）。

以下分别介绍具体开发方式。

## 针对特定IP联网访问控制

1. 设备通过硬件接口，插入网线。
2. 从@kit.NetworkKit中导入netfirewall命名空间。

   ```
   1. // 从@kit.NetworkKit中导入netFirewall命名空间。
   2. import { netFirewall } from '@kit.NetworkKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetFireWall_case/entry/src/main/ets/pages/Index.ets#L16-L21)
3. 用户调用setNetFirewallPolicy方法，打开防火墙。

   ```
   1. // IP类型
   2. interface IpType{
   3. family:number;
   4. type:number;
   5. address?:string;
   6. mask?:number;
   7. startIp?:string;
   8. endIp?:string;
   9. }
   10. // IP端口
   11. interface IpPort{
   12. startPort:number;
   13. endPort:number;
   14. }
   15. // ...
   16. // 定义防火墙策略：打开，入站阻止，出站允许。
   17. let policy: netFirewall.NetFirewallPolicy = {
   18. isOpen: true,
   19. inAction: netFirewall.FirewallRuleAction.RULE_DENY,
   20. outAction: netFirewall.FirewallRuleAction.RULE_ALLOW
   21. };

   23. // 给用户100设置防火墙策略。
   24. netFirewall.setNetFirewallPolicy(100, policy).then(() => {
   25. hilog.info(0x0000, 'testTag', `set firewall policy success.`);
   26. }).catch((error : BusinessError) => {
   27. hilog.error(0x0000, 'testTag', `error: set firewall policy failed: ${JSON.stringify(error)}`);
   28. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetFireWall_case/entry/src/main/ets/pages/Index.ets#L25-L113)
4. 用户通过addNetFirewallRule方法，添加防火墙规则。

   ```
   1. // 初始化具体的防火墙ip类型规则。
   2. let ipRule: netFirewall.NetFirewallRule = {
   3. name: 'rule1',
   4. description: 'rule1 description',
   5. direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
   6. action: netFirewall.FirewallRuleAction.RULE_DENY,
   7. type: netFirewall.NetFirewallRuleType.RULE_IP,
   8. isEnabled: true,
   9. appUid: 20001,
   10. localIps: [
   11. {
   12. family: 1,
   13. type: 1,
   14. address: '10.10.1.1',
   15. mask: 32
   16. },{
   17. family: 1,
   18. type: 2,
   19. startIp: '10.20.1.1',
   20. endIp: '10.20.1.10'
   21. }] as IpType[],
   22. remoteIps:[
   23. {
   24. family: 1,
   25. type: 1,
   26. address: '20.10.1.1',
   27. mask: 32
   28. },{
   29. family: 1,
   30. type: 2,
   31. startIp: '20.20.1.1',
   32. endIp: '20.20.1.10'
   33. }] as IpType[],
   34. protocol: 6,
   35. localPorts: [
   36. {
   37. startPort: 1000,
   38. endPort: 1000
   39. },{
   40. startPort: 2000,
   41. endPort: 2001
   42. }] as IpPort[],
   43. remotePorts: [
   44. {
   45. startPort: 443,
   46. endPort: 443
   47. }] as IpPort[],
   48. userId: 100
   49. };
   50. // 添加防火墙规则。
   51. netFirewall.addNetFirewallRule(ipRule).then((result: number) => {
   52. // ...
   53. hilog.info(0x0000, 'testTag', `rule Id: ${result}`);
   54. }, (reason: BusinessError) => {
   55. // ...
   56. hilog.error(0x0000, 'testTag', `error: add firewall rule failed:  ${JSON.stringify(reason)}`);
   57. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetFireWall_case/entry/src/main/ets/pages/Index.ets#L115-L188)

## 针对域名联网访问控制支持拦截

1. 设备通过硬件接口，插入网线。
2. 从@kit.NetworkKit中导入netFirewall命名空间。

   ```
   1. // 从@kit.NetworkKit中导入netFirewall命名空间。
   2. import { netFirewall } from '@kit.NetworkKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetFireWall_case/entry/src/main/ets/pages/Index.ets#L16-L21)
3. 调用setNetFirewallPolicy方法，打开防火墙。

   ```
   1. interface domain{
   2. isWildcard: boolean;
   3. domain: string;
   4. }
   5. // ...
   6. // 定义防火墙策略：打开，入站阻止，出站允许。
   7. let policy: netFirewall.NetFirewallPolicy = {
   8. isOpen: true,
   9. inAction: netFirewall.FirewallRuleAction.RULE_DENY,
   10. outAction: netFirewall.FirewallRuleAction.RULE_ALLOW
   11. };

   13. // 给用户100设置防火墙策略
   14. netFirewall.setNetFirewallPolicy(100, policy).then(() => {
   15. hilog.info(0x0000, 'testTag', `set firewall policy success.`);
   16. }).catch((error : BusinessError) => {
   17. hilog.error(0x0000, 'testTag', `error: set firewall policy failed: ${JSON.stringify(error)}`);
   18. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetFireWall_case/entry/src/main/ets/pages/Index.ets#L42-L207)
4. 通过addNetFirewallRule方法，添加防火墙规则。

   ```
   1. // 初始化具体的防火墙域名类型规则。
   2. let domainRule: netFirewall.NetFirewallRule = {
   3. name: 'rule2',
   4. description: 'rule2 description',
   5. direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
   6. action: netFirewall.FirewallRuleAction.RULE_DENY,
   7. type: netFirewall.NetFirewallRuleType.RULE_DOMAIN,
   8. isEnabled: true,
   9. appUid: 20002,
   10. domains: [
   11. {
   12. isWildcard: false,
   13. domain: 'www.HarmonyOS.cn'
   14. },{
   15. isWildcard: true,
   16. domain: '*.HarmonyOS.cn'
   17. }] as domain[],
   18. userId: 100
   19. };

   21. // 添加防火墙规则。
   22. netFirewall.addNetFirewallRule(domainRule).then((result: number) => {
   23. // ...
   24. hilog.info(0x0000, 'testTag', `rule Id: ${result}`);
   25. }, (reason: BusinessError) => {
   26. // ...
   27. hilog.error(0x0000, 'testTag', `error: add firewall rule failed:  ${JSON.stringify(reason)}`);
   28. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetFireWall_case/entry/src/main/ets/pages/Index.ets#L209-L252)
