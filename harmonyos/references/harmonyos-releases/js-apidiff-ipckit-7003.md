---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-ipckit-7003
title: IPC Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > IPC Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3531145a2f2eac303e3687dcb14646fd6303c3e242f25cdd074263d011504a79
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace rpc  差异内容：NA | 类名：global；  API声明：declare namespace rpc  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：rpc；  API声明：class MessageSequence  差异内容：NA | 类名：rpc；  API声明：class MessageSequence  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageSequence；  API声明：writeInt(val: number): void;  差异内容：NA | 类名：MessageSequence；  API声明：writeInt(val: number): void;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageSequence；  API声明：writeString(val: string): void;  差异内容：NA | 类名：MessageSequence；  API声明：writeString(val: string): void;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageSequence；  API声明：readInt(): number;  差异内容：NA | 类名：MessageSequence；  API声明：readInt(): number;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageSequence；  API声明：readString(): string;  差异内容：NA | 类名：MessageSequence；  API声明：readString(): string;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：rpc；  API声明：class MessageOption  差异内容：NA | 类名：rpc；  API声明：class MessageOption  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageOption；  API声明：static readonly TF\_SYNC: number;  差异内容：NA | 类名：MessageOption；  API声明：static readonly TF\_SYNC: number;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageOption；  API声明：static readonly TF\_ASYNC: number;  差异内容：NA | 类名：MessageOption；  API声明：static readonly TF\_ASYNC: number;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageOption；  API声明：static readonly TF\_ACCEPT\_FDS: number;  差异内容：NA | 类名：MessageOption；  API声明：static readonly TF\_ACCEPT\_FDS: number;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageOption；  API声明：static readonly TF\_WAIT\_TIME: number;  差异内容：NA | 类名：MessageOption；  API声明：static readonly TF\_WAIT\_TIME: number;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageOption；  API声明：getFlags(): number;  差异内容：NA | 类名：MessageOption；  API声明：getFlags(): number;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageOption；  API声明：setFlags(flags: number): void;  差异内容：NA | 类名：MessageOption；  API声明：setFlags(flags: number): void;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageOption；  API声明：isAsync(): boolean;  差异内容：NA | 类名：MessageOption；  API声明：isAsync(): boolean;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageOption；  API声明：setAsync(isAsync: boolean): void;  差异内容：NA | 类名：MessageOption；  API声明：setAsync(isAsync: boolean): void;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageOption；  API声明：getWaitTime(): number;  差异内容：NA | 类名：MessageOption；  API声明：getWaitTime(): number;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：MessageOption；  API声明：setWaitTime(waitTime: number): void;  差异内容：NA | 类名：MessageOption；  API声明：setWaitTime(waitTime: number): void;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：rpc；  API声明：class RemoteObject  差异内容：NA | 类名：rpc；  API声明：class RemoteObject  差异内容：atomicservice | api/@ohos.rpc.d.ts |
| API从不支持元服务到支持元服务 | 类名：RemoteObject；  API声明：onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): boolean | Promise<boolean>;  差异内容：NA | 类名：RemoteObject；  API声明：onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): boolean | Promise<boolean>;  差异内容：atomicservice | api/@ohos.rpc.d.ts |
