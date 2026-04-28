---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-remotecommunicationkit-6001
title: Remote Communication Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Remote Communication Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d154d31dcceea13cd96283973e2c86b92c40c695614924df911b35df1637f115
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 自定义类型变更 | 类名：rcp；  API声明：export type DebugEvent = 'text' | 'headerIn' | 'headerOut' | 'dataIn' | 'dataOut' | 'sslDataIn' | 'sslDataOut';  差异内容：'text' | 'headerIn' | 'headerOut' | 'dataIn' | 'dataOut' | 'sslDataIn' | 'sslDataOut' | 类名：rcp；  API声明：export type DebugEvent = 'text' | 'headerIn' | 'headerOut' | 'dataIn' | 'dataOut' | 'sslDataIn' | 'sslDataOut' | 'srcAddr' | 'dstAddr';  差异内容：'text' | 'headerIn' | 'headerOut' | 'dataIn' | 'dataOut' | 'sslDataIn' | 'sslDataOut' | 'srcAddr' | 'dstAddr' | api/@hms.collaboration.rcp.d.ts |
| 自定义类型变更 | 类名：rcp；  API声明：export type OnDataReceive = (incomingData: ArrayBuffer) => number | void | Promise<void>;  差异内容：NA | 类名：rcp；  API声明：export type OnDataReceive = (incomingData: ArrayBuffer, request?: Request) => number | void | Promise<void>;  差异内容：request?: Request | api/@hms.collaboration.rcp.d.ts |
| 自定义类型变更 | 类名：rcp；  API声明：export type OnUploadProgress = (totalSize: number, transferredSize: number) => void;  差异内容：NA | 类名：rcp；  API声明：export type OnUploadProgress = (totalSize: number, transferredSize: number, request?: Request) => void;  差异内容：request?: Request | api/@hms.collaboration.rcp.d.ts |
| 自定义类型变更 | 类名：rcp；  API声明：export type OnDownloadProgress = (totalSize: number, transferredSize: number) => void;  差异内容：NA | 类名：rcp；  API声明：export type OnDownloadProgress = (totalSize: number, transferredSize: number, request?: Request) => void;  差异内容：request?: Request | api/@hms.collaboration.rcp.d.ts |
| 自定义类型变更 | 类名：rcp；  API声明：export type OnHeaderReceive = (headers: ResponseHeaders) => void;  差异内容：NA | 类名：rcp；  API声明：export type OnHeaderReceive = (headers: ResponseHeaders, request?: Request) => void;  差异内容：request?: Request | api/@hms.collaboration.rcp.d.ts |
| 自定义类型变更 | 类名：rcp；  API声明：export type OnDataEnd = () => void;  差异内容：NA | 类名：rcp；  API声明：export type OnDataEnd = (request?: Request) => void;  差异内容：request?: Request | api/@hms.collaboration.rcp.d.ts |
| 自定义类型变更 | 类名：rcp；  API声明：export type OnCanceled = () => void;  差异内容：NA | 类名：rcp；  API声明：export type OnCanceled = (request?: Request) => void;  差异内容：request?: Request | api/@hms.collaboration.rcp.d.ts |
| 自定义类型变更 | 类名：rcp；  API声明：export type OnTimeInfo = (timeInfo: TimeInfo) => void;  差异内容：NA | 类名：rcp；  API声明：export type OnTimeInfo = (timeInfo: TimeInfo, request?: Request) => void;  差异内容：request?: Request | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface TcpConfiguration  差异内容：export interface TcpConfiguration | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：TcpConfiguration；  API声明：keepIdleSec?: number;  差异内容：keepIdleSec?: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：TcpConfiguration；  API声明：userTimeoutMs?: number;  差异内容：userTimeoutMs?: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：TcpConfiguration；  API声明：keepCnt?: number;  差异内容：keepCnt?: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：TcpConfiguration；  API声明：keepIntervalSec?: number;  差异内容：keepIntervalSec?: number; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export type OnStatusCodeReceive = (statusCode: number, request?: Request) => void;  差异内容：export type OnStatusCodeReceive = (statusCode: number, request?: Request) => void; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export interface TlsVersionRangeOptions  差异内容：export interface TlsVersionRangeOptions | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：TlsVersionRangeOptions；  API声明：min?: TlsVersion;  差异内容：min?: TlsVersion; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：TlsVersionRangeOptions；  API声明：max?: TlsVersion;  差异内容：max?: TlsVersion; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：TlsVersionRangeOptions；  API声明：cipherSuite?: CipherSuite[];  差异内容：cipherSuite?: CipherSuite[]; | api/@hms.collaboration.rcp.d.ts |
| 新增API | NA | 类名：rcp；  API声明：export type TlsVersion = 'TlsV1.0' | 'TlsV1.1' | 'TlsV1.2' | 'TlsV1.3';  差异内容：export type TlsVersion = 'TlsV1.0' | 'TlsV1.1' | 'TlsV1.2' | 'TlsV1.3'; | api/@hms.collaboration.rcp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：InfoToCollect；  API声明：srcAddr?: boolean;  差异内容：srcAddr?: boolean; | api/@hms.collaboration.rcp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：InfoToCollect；  API声明：dstAddr?: boolean;  差异内容：dstAddr?: boolean; | api/@hms.collaboration.rcp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TransferConfiguration；  API声明：tcp?: TcpConfiguration;  差异内容：tcp?: TcpConfiguration; | api/@hms.collaboration.rcp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：DnsConfiguration；  API声明：happyEyeballOnDnsRule?: boolean;  差异内容：happyEyeballOnDnsRule?: boolean; | api/@hms.collaboration.rcp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SecurityConfiguration；  API声明：tlsRange?: TlsVersionRangeOptions;  差异内容：tlsRange?: TlsVersionRangeOptions; | api/@hms.collaboration.rcp.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：HttpEventsHandler；  API声明：onStatusCodeReceive?: OnStatusCodeReceive;  差异内容：onStatusCodeReceive?: OnStatusCodeReceive; | api/@hms.collaboration.rcp.d.ts |
