---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-remotecommunicationkit-b105
title: Remote Communication Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > Remote Communication Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:06+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6bb666038d8077b431a13571a3ce82458ff9ae61f232e3ef36f4a4bb5254ae15
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace urpc  差异内容： declare namespace urpc | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明：type FlowbufType = 'INT8' | 'UINT8' | 'INT16' | 'UINT16' | 'INT32' | 'UINT32' | 'INT64' | 'UINT64' | 'BOOL' | 'FLOAT' | 'DOUBLE' | 'STRING' | 'BYTES' | 'MESSAGE' | 'REPEATED\_INT8' | 'REPEATED\_UINT8' | 'REPEATED\_INT16' | 'REPEATED\_UINT16' | 'REPEATED\_INT32' | 'REPEATED\_UINT32' | 'REPEATED\_INT64' | 'REPEATED\_UINT64' | 'REPEATED\_BOOL' | 'REPEATED\_FLOAT' | 'REPEATED\_DOUBLE' | 'REPEATED\_STRING' | 'REPEATED\_BYTES' | 'REPEATED\_MESSAGE' | 'ARRAY\_INT8' | 'ARRAY\_UINT8' | 'ARRAY\_INT16' | 'ARRAY\_UINT16' | 'ARRAY\_INT32' | 'ARRAY\_UINT32' | 'ARRAY\_INT64' | 'ARRAY\_UINT64' | 'ARRAY\_BOOL' | 'ARRAY\_FLOAT' | 'ARRAY\_DOUBLE';  差异内容：type FlowbufType = 'INT8' | 'UINT8' | 'INT16' | 'UINT16' | 'INT32' | 'UINT32' | 'INT64' | 'UINT64' | 'BOOL' | 'FLOAT' | 'DOUBLE' | 'STRING' | 'BYTES' | 'MESSAGE' | 'REPEATED\_INT8' | 'REPEATED\_UINT8' | 'REPEATED\_INT16' | 'REPEATED\_UINT16' | 'REPEATED\_INT32' | 'REPEATED\_UINT32' | 'REPEATED\_INT64' | 'REPEATED\_UINT64' | 'REPEATED\_BOOL' | 'REPEATED\_FLOAT' | 'REPEATED\_DOUBLE' | 'REPEATED\_STRING' | 'REPEATED\_BYTES' | 'REPEATED\_MESSAGE' | 'ARRAY\_INT8' | 'ARRAY\_UINT8' | 'ARRAY\_INT16' | 'ARRAY\_UINT16' | 'ARRAY\_INT32' | 'ARRAY\_UINT32' | 'ARRAY\_INT64' | 'ARRAY\_UINT64' | 'ARRAY\_BOOL' | 'ARRAY\_FLOAT' | 'ARRAY\_DOUBLE'; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明： interface FlowbufElement  差异内容： interface FlowbufElement | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：FlowbufElement；  API声明：type: FlowbufType;  差异内容：type: FlowbufType; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：FlowbufElement；  API声明：value: T;  差异内容：value: T; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：FlowbufElement；  API声明：name: string;  差异内容：name: string; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明： interface FlowbufArrayElement  差异内容： interface FlowbufArrayElement | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：FlowbufArrayElement；  API声明：type: FlowbufType;  差异内容：type: FlowbufType; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：FlowbufArrayElement；  API声明：value: T[];  差异内容：value: T[]; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：FlowbufArrayElement；  API声明：length: number;  差异内容：length: number; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明：type UrpcMode = 'client';  差异内容：type UrpcMode = 'client'; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明：type UrpcProtocol = 'eat';  差异内容：type UrpcProtocol = 'eat'; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明： interface IpAndPort  差异内容： interface IpAndPort | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：IpAndPort；  API声明：ip: string;  差异内容：ip: string; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：IpAndPort；  API声明：port: number;  差异内容：port: number; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明： interface UrpcPromise  差异内容： interface UrpcPromise | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcPromise；  API声明：promise: Promise<Object>;  差异内容：promise: Promise<Object>; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcPromise；  API声明：callingId: number;  差异内容：callingId: number; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明： interface UrpcConnectConfiguration  差异内容： interface UrpcConnectConfiguration | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcConnectConfiguration；  API声明：node: IpAndPort;  差异内容：node: IpAndPort; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcConnectConfiguration；  API声明：protocol?: UrpcProtocol;  差异内容：protocol?: UrpcProtocol; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcConnectConfiguration；  API声明：multiPath?: boolean;  差异内容：multiPath?: boolean; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcConnectConfiguration；  API声明：flags?: number;  差异内容：flags?: number; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcConnectConfiguration；  API声明：host?: string;  差异内容：host?: string; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcConnectConfiguration；  API声明：caPath?: string;  差异内容：caPath?: string; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明： interface UrpcInitConfiguration  差异内容： interface UrpcInitConfiguration | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcInitConfiguration；  API声明：mode?: UrpcMode;  差异内容：mode?: UrpcMode; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcInitConfiguration；  API声明：connect: UrpcConnectConfiguration;  差异内容：connect: UrpcConnectConfiguration; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcInitConfiguration；  API声明：timeout: number;  差异内容：timeout: number; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明： interface CallingOption  差异内容： interface CallingOption | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：CallingOption；  API声明：priority?: number;  差异内容：priority?: number; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明：type UrpcCall = (funcName: string, request: object, returnValue: object, config?: CallingOption) => UrpcPromise;  差异内容：type UrpcCall = (funcName: string, request: object, returnValue: object, config?: CallingOption) => UrpcPromise; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明：type UrpcCancel = (callingId?: number | number[]) => void;  差异内容：type UrpcCancel = (callingId?: number | number[]) => void; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明：type UrpcDestroy = () => void;  差异内容：type UrpcDestroy = () => void; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明： class UrpcStub  差异内容： class UrpcStub | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcStub；  API声明：readonly id: number;  差异内容：readonly id: number; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcStub；  API声明：call: UrpcCall;  差异内容：call: UrpcCall; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcStub；  API声明：cancel: UrpcCancel;  差异内容：cancel: UrpcCancel; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：UrpcStub；  API声明：destroy: UrpcDestroy;  差异内容：destroy: UrpcDestroy; | api/@hms.collaboration.urpc.d.ts |
| 新增API | NA | 类名：urpc；  API声明：function urpcStubCreate(config: UrpcInitConfiguration, funcList: string | string[]): Promise<UrpcStub>;  差异内容：function urpcStubCreate(config: UrpcInitConfiguration, funcList: string | string[]): Promise<UrpcStub>; | api/@hms.collaboration.urpc.d.ts |
