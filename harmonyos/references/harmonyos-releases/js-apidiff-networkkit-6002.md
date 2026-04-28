---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-6002
title: Network Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Network Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:31+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:eae1acd4e4ff001457d10255e1d7ff9f1d68c4ef2effe68bb0f160f27fd2c0fd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace eap  差异内容：declare namespace eap | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void;  差异内容：function regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function unregCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void;  差异内容：function unregCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function replyCustomEapData(result: CustomResult, data: EapData): void;  差异内容：function replyCustomEapData(result: CustomResult, data: EapData): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function startEthEap(netId: number, profile: EthEapProfile): void;  差异内容：function startEthEap(netId: number, profile: EthEapProfile): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：function logOffEthEap(netId: number): void;  差异内容：function logOffEthEap(netId: number): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：interface EapData  差异内容：interface EapData | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapData；  API声明：msgId: number;  差异内容：msgId: number; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapData；  API声明：eapBuffer: Uint8Array;  差异内容：eapBuffer: Uint8Array; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapData；  API声明：bufferLen: number;  差异内容：bufferLen: number; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：enum CustomResult  差异内容：enum CustomResult | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：CustomResult；  API声明：RESULT\_FAIL  差异内容：RESULT\_FAIL | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：CustomResult；  API声明：RESULT\_NEXT  差异内容：RESULT\_NEXT | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：CustomResult；  API声明：RESULT\_FINISH  差异内容：RESULT\_FINISH | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：enum EapMethod  差异内容：enum EapMethod | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_NONE  差异内容：EAP\_NONE | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_PEAP  差异内容：EAP\_PEAP | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_TLS  差异内容：EAP\_TLS | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_TTLS  差异内容：EAP\_TTLS | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_PWD  差异内容：EAP\_PWD | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_SIM  差异内容：EAP\_SIM | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_AKA  差异内容：EAP\_AKA | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_AKA\_PRIME  差异内容：EAP\_AKA\_PRIME | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod；  API声明：EAP\_UNAUTH\_TLS  差异内容：EAP\_UNAUTH\_TLS | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：enum Phase2Method  差异内容：enum Phase2Method | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_NONE  差异内容：PHASE2\_NONE | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_PAP  差异内容：PHASE2\_PAP | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_MSCHAP  差异内容：PHASE2\_MSCHAP | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_MSCHAPV2  差异内容：PHASE2\_MSCHAPV2 | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_GTC  差异内容：PHASE2\_GTC | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_SIM  差异内容：PHASE2\_SIM | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_AKA  差异内容：PHASE2\_AKA | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method；  API声明：PHASE2\_AKA\_PRIME  差异内容：PHASE2\_AKA\_PRIME | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap；  API声明：interface EthEapProfile  差异内容：interface EthEapProfile | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：eapMethod: EapMethod;  差异内容：eapMethod: EapMethod; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：phase2Method: Phase2Method;  差异内容：phase2Method: Phase2Method; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：identity: string;  差异内容：identity: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：anonymousIdentity: string;  差异内容：anonymousIdentity: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：password: string;  差异内容：password: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：caCertAliases: string;  差异内容：caCertAliases: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：caPath: string;  差异内容：caPath: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：clientCertAliases: string;  差异内容：clientCertAliases: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：certEntry: Uint8Array;  差异内容：certEntry: Uint8Array; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：certPassword: string;  差异内容：certPassword: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：altSubjectMatch: string;  差异内容：altSubjectMatch: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：domainSuffixMatch: string;  差异内容：domainSuffixMatch: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：realm: string;  差异内容：realm: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：plmn: string;  差异内容：plmn: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile；  API声明：eapSubId: number;  差异内容：eapSubId: number; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：connection；  API声明：function setNetExtAttribute(netHandle: NetHandle, netExtAttribute: string): Promise<void>;  差异内容：function setNetExtAttribute(netHandle: NetHandle, netExtAttribute: string): Promise<void>; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function setNetExtAttributeSync(netHandle: NetHandle, netExtAttribute: string): void;  差异内容：function setNetExtAttributeSync(netHandle: NetHandle, netExtAttribute: string): void; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getNetExtAttribute(netHandle: NetHandle): Promise<string>;  差异内容：function getNetExtAttribute(netHandle: NetHandle): Promise<string>; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getNetExtAttributeSync(netHandle: NetHandle): string;  差异内容：function getNetExtAttributeSync(netHandle: NetHandle): string; | api/@ohos.net.connection.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.net.eap.d.ts  差异内容：NetworkKit | api/@ohos.net.eap.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：WebSocketRequestOptions；  API声明：skipServerCertVerification?: boolean;  差异内容：skipServerCertVerification?: boolean; | api/@ohos.net.webSocket.d.ts |
