---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-ipckit-6101
title: IPC Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > IPC Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e5ac74ab61e3339cac316084ae1e4c95143183c10c93292e3f540cbd47a29fab
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：MessageSequence；  API声明：writeRemoteObject(object: IRemoteObject): void;  差异内容：object: IRemoteObject | 类名：MessageSequence；  API声明：writeRemoteObject(obj: IRemoteObject): void;  差异内容：obj: IRemoteObject | api/@ohos.rpc.d.ts |
| 函数变更 | 类名：MessageOption；  API声明：setAsync(async: boolean): void;  差异内容：async: boolean | 类名：MessageOption；  API声明：setAsync(isAsync: boolean): void;  差异内容：isAsync: boolean | api/@ohos.rpc.d.ts |
| 新增API | NA | 类名：rpc；  API声明：class CallingInfo  差异内容：class CallingInfo | api/@ohos.rpc.d.ts |
| 新增API | NA | 类名：CallingInfo；  API声明：readonly callerPid: number;  差异内容：readonly callerPid: number; | api/@ohos.rpc.d.ts |
| 新增API | NA | 类名：CallingInfo；  API声明：readonly callerUid: number;  差异内容：readonly callerUid: number; | api/@ohos.rpc.d.ts |
| 新增API | NA | 类名：CallingInfo；  API声明：readonly callerTokenId: number;  差异内容：readonly callerTokenId: number; | api/@ohos.rpc.d.ts |
| 新增API | NA | 类名：CallingInfo；  API声明：readonly remoteDeviceId: string;  差异内容：readonly remoteDeviceId: string; | api/@ohos.rpc.d.ts |
| 新增API | NA | 类名：CallingInfo；  API声明：readonly localDeviceId: string;  差异内容：readonly localDeviceId: string; | api/@ohos.rpc.d.ts |
| 新增API | NA | 类名：CallingInfo；  API声明：readonly isLocalCalling: boolean;  差异内容：readonly isLocalCalling: boolean; | api/@ohos.rpc.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：RemoteObject；  API声明：onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): boolean | Promise<boolean>;  差异内容：onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): boolean | Promise<boolean>; | 类名：RemoteObject；  API声明：onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callingInfo?: CallingInfo): boolean | Promise<boolean>;  差异内容：onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callingInfo?: CallingInfo): boolean | Promise<boolean>; | api/@ohos.rpc.d.ts |
