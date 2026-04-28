---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-5032
title: Network Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:2cc7b008286be38dc06740cf7127a16276ef263b0e55d49e01db9ed89ed54099
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace netFirewall  差异内容： declare namespace netFirewall | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明：function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>;  差异内容：function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明：function getNetFirewallPolicy(userId: number): Promise<NetFirewallPolicy>;  差异内容：function getNetFirewallPolicy(userId: number): Promise<NetFirewallPolicy>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明：function addNetFirewallRule(rule: NetFirewallRule): Promise<number>;  差异内容：function addNetFirewallRule(rule: NetFirewallRule): Promise<number>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明：function updateNetFirewallRule(rule: NetFirewallRule): Promise<void>;  差异内容：function updateNetFirewallRule(rule: NetFirewallRule): Promise<void>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明：function removeNetFirewallRule(userId: number, ruleId: number): Promise<void>;  差异内容：function removeNetFirewallRule(userId: number, ruleId: number): Promise<void>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明：function getNetFirewallRules(userId: number, requestParam: RequestParam): Promise<FirewallRulePage>;  差异内容：function getNetFirewallRules(userId: number, requestParam: RequestParam): Promise<FirewallRulePage>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明：function getNetFirewallRule(userId: number, ruleId: number): Promise<NetFirewallRule>;  差异内容：function getNetFirewallRule(userId: number, ruleId: number): Promise<NetFirewallRule>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： enum NetFirewallRuleDirection  差异内容： enum NetFirewallRuleDirection | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRuleDirection；  API声明：RULE\_IN = 1  差异内容：RULE\_IN = 1 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRuleDirection；  API声明：RULE\_OUT = 2  差异内容：RULE\_OUT = 2 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： enum FirewallRuleAction  差异内容： enum FirewallRuleAction | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：FirewallRuleAction；  API声明：RULE\_ALLOW = 0  差异内容：RULE\_ALLOW = 0 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：FirewallRuleAction；  API声明：RULE\_DENY = 1  差异内容：RULE\_DENY = 1 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： enum NetFirewallRuleType  差异内容： enum NetFirewallRuleType | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRuleType；  API声明：RULE\_IP = 1  差异内容：RULE\_IP = 1 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRuleType；  API声明：RULE\_DOMAIN = 2  差异内容：RULE\_DOMAIN = 2 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRuleType；  API声明：RULE\_DNS = 3  差异内容：RULE\_DNS = 3 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： enum NetFirewallOrderField  差异内容： enum NetFirewallOrderField | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallOrderField；  API声明：ORDER\_BY\_RULE\_NAME = 1  差异内容：ORDER\_BY\_RULE\_NAME = 1 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallOrderField；  API声明：ORDER\_BY\_RECORD\_TIME = 100  差异内容：ORDER\_BY\_RECORD\_TIME = 100 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： enum NetFirewallOrderType  差异内容： enum NetFirewallOrderType | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallOrderType；  API声明：ORDER\_ASC = 1  差异内容：ORDER\_ASC = 1 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallOrderType；  API声明：ORDER\_DESC = 100  差异内容：ORDER\_DESC = 100 | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： interface NetFirewallPolicy  差异内容： interface NetFirewallPolicy | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallPolicy；  API声明：isOpen: boolean;  差异内容：isOpen: boolean; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallPolicy；  API声明：inAction: FirewallRuleAction;  差异内容：inAction: FirewallRuleAction; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallPolicy；  API声明：outAction: FirewallRuleAction;  差异内容：outAction: FirewallRuleAction; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： interface NetFirewallIpParams  差异内容： interface NetFirewallIpParams | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallIpParams；  API声明：type: number;  差异内容：type: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallIpParams；  API声明：family?: number;  差异内容：family?: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallIpParams；  API声明：address?: string;  差异内容：address?: string; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallIpParams；  API声明：mask?: number;  差异内容：mask?: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallIpParams；  API声明：startIp?: string;  差异内容：startIp?: string; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallIpParams；  API声明：endIp?: string;  差异内容：endIp?: string; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： interface NetFirewallPortParams  差异内容： interface NetFirewallPortParams | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallPortParams；  API声明：startPort: number;  差异内容：startPort: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallPortParams；  API声明：endPort: number;  差异内容：endPort: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： interface NetFirewallDomainParams  差异内容： interface NetFirewallDomainParams | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallDomainParams；  API声明：isWildcard: boolean;  差异内容：isWildcard: boolean; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallDomainParams；  API声明：domain: string;  差异内容：domain: string; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： interface NetFirewallDnsParams  差异内容： interface NetFirewallDnsParams | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallDnsParams；  API声明：primaryDns: string;  差异内容：primaryDns: string; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallDnsParams；  API声明：standbyDns?: string;  差异内容：standbyDns?: string; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： interface NetFirewallRule  差异内容： interface NetFirewallRule | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：userId: number;  差异内容：userId: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：name: string;  差异内容：name: string; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：direction: NetFirewallRuleDirection;  差异内容：direction: NetFirewallRuleDirection; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：action: FirewallRuleAction;  差异内容：action: FirewallRuleAction; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：type: NetFirewallRuleType;  差异内容：type: NetFirewallRuleType; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：isEnabled: boolean;  差异内容：isEnabled: boolean; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：id?: number;  差异内容：id?: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：description?: string;  差异内容：description?: string; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：appUid?: number;  差异内容：appUid?: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：localIps?: Array<NetFirewallIpParams>;  差异内容：localIps?: Array<NetFirewallIpParams>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：remoteIps?: Array<NetFirewallIpParams>;  差异内容：remoteIps?: Array<NetFirewallIpParams>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：protocol?: number;  差异内容：protocol?: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：localPorts?: Array<NetFirewallPortParams>;  差异内容：localPorts?: Array<NetFirewallPortParams>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：remotePorts?: Array<NetFirewallPortParams>;  差异内容：remotePorts?: Array<NetFirewallPortParams>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：domains?: Array<NetFirewallDomainParams>;  差异内容：domains?: Array<NetFirewallDomainParams>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：NetFirewallRule；  API声明：dns?: NetFirewallDnsParams;  差异内容：dns?: NetFirewallDnsParams; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： interface RequestParam  差异内容： interface RequestParam | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：RequestParam；  API声明：page: number;  差异内容：page: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：RequestParam；  API声明：pageSize: number;  差异内容：pageSize: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：RequestParam；  API声明：orderField: NetFirewallOrderField;  差异内容：orderField: NetFirewallOrderField; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：RequestParam；  API声明：orderType: NetFirewallOrderType;  差异内容：orderType: NetFirewallOrderType; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：netFirewall；  API声明： interface FirewallRulePage  差异内容： interface FirewallRulePage | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：FirewallRulePage；  API声明：page: number;  差异内容：page: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：FirewallRulePage；  API声明：pageSize: number;  差异内容：pageSize: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：FirewallRulePage；  API声明：totalPage: number;  差异内容：totalPage: number; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：FirewallRulePage；  API声明：data: Array<NetFirewallRule>;  差异内容：data: Array<NetFirewallRule>; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：http；  API声明： export enum AddressFamily  差异内容： export enum AddressFamily | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：AddressFamily；  API声明：DEFAULT = 'CURL\_IPRESOLVE\_WHATEVER'  差异内容：DEFAULT = 'CURL\_IPRESOLVE\_WHATEVER' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：AddressFamily；  API声明：ONLY\_V4 = 'CURL\_IPRESOLVE\_V4'  差异内容：ONLY\_V4 = 'CURL\_IPRESOLVE\_V4' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：AddressFamily；  API声明：ONLY\_V6 = 'CURL\_IPRESOLVE\_V6'  差异内容：ONLY\_V6 = 'CURL\_IPRESOLVE\_V6' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions；  API声明：addressFamily?: AddressFamily;  差异内容：addressFamily?: AddressFamily; | api/@ohos.net.http.d.ts |
| kit变更 | NA | NetworkKit | api/@ohos.net.netFirewall.d.ts |
