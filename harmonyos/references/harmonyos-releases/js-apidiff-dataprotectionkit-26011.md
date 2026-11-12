---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataprotectionkit-26011
title: Data Protection Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Data Protection Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e714a28f7305657c78cdf5740b30cb68270d8d67c16e1970ce2ad3db6c33d9a6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：dlpPermission；  API声明：function isDLPFile(fd: number): Promise<boolean>;  差异内容：NA | 类名：dlpPermission；  API声明：function isDLPFile(fd: number): Promise<boolean>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function isDLPFile(fd: number, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function isDLPFile(fd: number, callback: AsyncCallback<boolean>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getDLPPermissionInfo(): Promise<DLPPermissionInfo>;  差异内容：NA | 类名：dlpPermission；  API声明：function getDLPPermissionInfo(): Promise<DLPPermissionInfo>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getOriginalFileName(fileName: string): string;  差异内容：NA | 类名：dlpPermission；  API声明：function getOriginalFileName(fileName: string): string;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getDLPSuffix(): string;  差异内容：NA | 类名：dlpPermission；  API声明：function getDLPSuffix(): string;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function on(type: 'openDLPFile', listener: Callback<AccessedDLPFileInfo>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function on(type: 'openDLPFile', listener: Callback<AccessedDLPFileInfo>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function off(type: 'openDLPFile', listener?: Callback<AccessedDLPFileInfo>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function off(type: 'openDLPFile', listener?: Callback<AccessedDLPFileInfo>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function isInSandbox(): Promise<boolean>;  差异内容：NA | 类名：dlpPermission；  API声明：function isInSandbox(): Promise<boolean>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function isInSandbox(callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function isInSandbox(callback: AsyncCallback<boolean>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getDLPSupportedFileTypes(): Promise<Array<string>>;  差异内容：NA | 类名：dlpPermission；  API声明：function getDLPSupportedFileTypes(): Promise<Array<string>>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getDLPSupportedFileTypes(callback: AsyncCallback<Array<string>>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function getDLPSupportedFileTypes(callback: AsyncCallback<Array<string>>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function setRetentionState(docUris: Array<string>): Promise<void>;  差异内容：NA | 类名：dlpPermission；  API声明：function setRetentionState(docUris: Array<string>): Promise<void>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function cancelRetentionState(docUris: Array<string>): Promise<void>;  差异内容：NA | 类名：dlpPermission；  API声明：function cancelRetentionState(docUris: Array<string>): Promise<void>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>;  差异内容：NA | 类名：dlpPermission；  API声明：function getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>;  差异内容：NA | 类名：dlpPermission；  API声明：function getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void;  差异内容：NA | 类名：dlpPermission；  API声明：function getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function startDLPManagerForResult(context: common.UIAbilityContext, want: Want): Promise<DLPManagerResult>;  差异内容：NA | 类名：dlpPermission；  API声明：function startDLPManagerForResult(context: common.UIAbilityContext, want: Want): Promise<DLPManagerResult>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function setSandboxAppConfig(configInfo: string): Promise<void>;  差异内容：NA | 类名：dlpPermission；  API声明：function setSandboxAppConfig(configInfo: string): Promise<void>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function cleanSandboxAppConfig(): Promise<void>;  差异内容：NA | 类名：dlpPermission；  API声明：function cleanSandboxAppConfig(): Promise<void>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function getSandboxAppConfig(): Promise<string>;  差异内容：NA | 类名：dlpPermission；  API声明：function getSandboxAppConfig(): Promise<string>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function isDLPFeatureProvided(): Promise<boolean>;  差异内容：NA | 类名：dlpPermission；  API声明：function isDLPFeatureProvided(): Promise<boolean>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise<void>;  差异内容：NA | 类名：dlpPermission；  API声明：function generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise<void>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function queryDlpPolicy(dlpFd: number): Promise<string>;  差异内容：NA | 类名：dlpPermission；  API声明：function queryDlpPolicy(dlpFd: number): Promise<string>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function decryptDlpFile(dlpFd: number, plaintextFd: number): Promise<void>;  差异内容：NA | 类名：dlpPermission；  API声明：function decryptDlpFile(dlpFd: number, plaintextFd: number): Promise<void>;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：dlpPermission；  API声明：function setEnterprisePolicy(policy: EnterprisePolicy): void;  差异内容：NA | 类名：dlpPermission；  API声明：function setEnterprisePolicy(policy: EnterprisePolicy): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：DlpConnPlugin；  API声明：connectServer(requestId: string, requestData: string, callback: Callback<string>): void;  差异内容：NA | 类名：DlpConnPlugin；  API声明：connectServer(requestId: string, requestData: string, callback: Callback<string>): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：DlpConnManager；  API声明：static registerPlugin(plugin: DlpConnPlugin): number;  差异内容：NA | 类名：DlpConnManager；  API声明：static registerPlugin(plugin: DlpConnPlugin): number;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增错误码 | 类名：DlpConnManager；  API声明：static unregisterPlugin(): void;  差异内容：NA | 类名：DlpConnManager；  API声明：static unregisterPlugin(): void;  差异内容：801 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace privacyComputation  差异内容：declare namespace privacyComputation | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：function genPrivacyTarget(targetElement: TargetElement, privacyProtocol: PrivacyProtocol): Promise<Uint8Array>;  差异内容：function genPrivacyTarget(targetElement: TargetElement, privacyProtocol: PrivacyProtocol): Promise<Uint8Array>; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：function privacySearch(privacyTarget: Uint8Array, elements: Element[], privacyProtocol: PrivacyProtocol): Promise<PrivacySearchResult>;  差异内容：function privacySearch(privacyTarget: Uint8Array, elements: Element[], privacyProtocol: PrivacyProtocol): Promise<PrivacySearchResult>; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：function getSearchResult(privacySearchResult: PrivacySearchResult, privacyProtocol: PrivacyProtocol): Promise<SearchResult>;  差异内容：function getSearchResult(privacySearchResult: PrivacySearchResult, privacyProtocol: PrivacyProtocol): Promise<SearchResult>; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：enum HashAlg  差异内容：enum HashAlg | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：HashAlg；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：HashAlg；  API声明：SHA256 = 1  差异内容：SHA256 = 1 | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：HashAlg；  API声明：SHA384 = 2  差异内容：SHA384 = 2 | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：HashAlg；  API声明：SHA512 = 3  差异内容：SHA512 = 3 | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：enum DataSetSize  差异内容：enum DataSetSize | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：DataSetSize；  API声明：SIZE\_128 = 0  差异内容：SIZE\_128 = 0 | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：DataSetSize；  API声明：SIZE\_256 = 1  差异内容：SIZE\_256 = 1 | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：DataSetSize；  API声明：SIZE\_512 = 2  差异内容：SIZE\_512 = 2 | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：enum ProtocolType  差异内容：enum ProtocolType | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：ProtocolType；  API声明：PSI\_PROTOCOL = 0  差异内容：PSI\_PROTOCOL = 0 | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：ProtocolType；  API声明：PIR\_PROTOCOL = 1  差异内容：PIR\_PROTOCOL = 1 | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：interface PrivacyProtocol  差异内容：interface PrivacyProtocol | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：PrivacyProtocol；  API声明：dataSetSize: DataSetSize;  差异内容：dataSetSize: DataSetSize; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：PrivacyProtocol；  API声明：protocolType: ProtocolType;  差异内容：protocolType: ProtocolType; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：interface TargetElement  差异内容：interface TargetElement | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：TargetElement；  API声明：elemData: Uint8Array;  差异内容：elemData: Uint8Array; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：TargetElement；  API声明：hashAlg?: HashAlg;  差异内容：hashAlg?: HashAlg; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：interface Element  差异内容：interface Element | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：Element；  API声明：elemKey: Uint8Array;  差异内容：elemKey: Uint8Array; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：Element；  API声明：hashAlg?: HashAlg;  差异内容：hashAlg?: HashAlg; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：Element；  API声明：elemValue?: Uint8Array;  差异内容：elemValue?: Uint8Array; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：interface PrivacySearchResult  差异内容：interface PrivacySearchResult | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：PrivacySearchResult；  API声明：resultCipherText: Uint8Array[];  差异内容：resultCipherText: Uint8Array[]; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：PrivacySearchResult；  API声明：valueCipherText?: Uint8Array[];  差异内容：valueCipherText?: Uint8Array[]; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：privacyComputation；  API声明：interface SearchResult  差异内容：interface SearchResult | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：SearchResult；  API声明：matchedResult: boolean;  差异内容：matchedResult: boolean; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：SearchResult；  API声明：attachedValues?: Uint8Array[];  差异内容：attachedValues?: Uint8Array[]; | api/@ohos.security.privacyComputation.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：export enum PluginCmd  差异内容：export enum PluginCmd | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：PluginCmd；  API声明：CMD\_BASE\_INSTALL\_PLUGIN = 0x1001  差异内容：CMD\_BASE\_INSTALL\_PLUGIN = 0x1001 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：PluginCmd；  API声明：CMD\_BASE\_INSTALL\_CONFIG\_FILE = 0x1002  差异内容：CMD\_BASE\_INSTALL\_CONFIG\_FILE = 0x1002 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：PluginCmd；  API声明：CMD\_BASE\_INSTALL\_SUFFIX\_FILTER\_FILE = 0x1003  差异内容：CMD\_BASE\_INSTALL\_SUFFIX\_FILTER\_FILE = 0x1003 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：PluginCmd；  API声明：CMD\_BASE\_UNINSTALL\_PLUGIN = 0x1004  差异内容：CMD\_BASE\_UNINSTALL\_PLUGIN = 0x1004 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：PluginCmd；  API声明：CMD\_BASE\_QUERY\_TRANSPARENT\_CRYPTO\_STATUS = 0x1005  差异内容：CMD\_BASE\_QUERY\_TRANSPARENT\_CRYPTO\_STATUS = 0x1005 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：PluginCmd；  API声明：CMD\_EVENT\_REPORT\_COMMON = 0x2001  差异内容：CMD\_EVENT\_REPORT\_COMMON = 0x2001 | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission；  API声明：function processPluginCommand(code: PluginCmd, message: string): Promise<string>;  差异内容：function processPluginCommand(code: PluginCmd, message: string): Promise<string>; | api/@ohos.dlpPermission.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.security.privacyComputation.d.ts  差异内容：DataProtectionKit | api/@ohos.security.privacyComputation.d.ts |
