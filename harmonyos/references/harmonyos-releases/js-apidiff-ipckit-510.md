---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-ipckit-510
title: IPC Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > IPC Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:11+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d6bb9086b6f5eb973787bd9713e949ba1d4af60f8f292654170a583b7f0808ea
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：MessageSequence；  API声明：setSize(size: number): void;  差异内容：NA | 类名：MessageSequence；  API声明：setSize(size: number): void;  差异内容：1900009 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：MessageSequence；  API声明：setCapacity(size: number): void;  差异内容：NA | 类名：MessageSequence；  API声明：setCapacity(size: number): void;  差异内容：1900009 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：MessageSequence；  API声明：rewindRead(pos: number): void;  差异内容：NA | 类名：MessageSequence；  API声明：rewindRead(pos: number): void;  差异内容：1900010 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：MessageSequence；  API声明：rewindWrite(pos: number): void;  差异内容：NA | 类名：MessageSequence；  API声明：rewindWrite(pos: number): void;  差异内容：1900009 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：MessageSequence；  API声明：readAshmem(): Ashmem;  差异内容：NA | 类名：MessageSequence；  API声明：readAshmem(): Ashmem;  差异内容：1900010 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：IRemoteObject；  API声明：registerDeathRecipient(recipient: DeathRecipient, flags: number): void;  差异内容：NA | 类名：IRemoteObject；  API声明：registerDeathRecipient(recipient: DeathRecipient, flags: number): void;  差异内容：1900005 | api/@ohos.rpc.d.ts |
| 新增错误码 | 类名：IRemoteObject；  API声明：unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void;  差异内容：NA | 类名：IRemoteObject；  API声明：unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void;  差异内容：1900005 | api/@ohos.rpc.d.ts |
| 删除错误码 | 类名：MessageSequence；  API声明：readByteArray(): number[];  差异内容：401 | 类名：MessageSequence；  API声明：readByteArray(): number[];  差异内容：NA | api/@ohos.rpc.d.ts |
| 删除错误码 | 类名：MessageSequence；  API声明：readAshmem(): Ashmem;  差异内容：1900004,401 | 类名：MessageSequence；  API声明：readAshmem(): Ashmem;  差异内容：NA | api/@ohos.rpc.d.ts |
| 错误码变更 | 类名：MessageSequence；  API声明：writeAshmem(ashmem: Ashmem): void;  差异内容：1900003,401 | 类名：MessageSequence；  API声明：writeAshmem(ashmem: Ashmem): void;  差异内容：1900009,401 | api/@ohos.rpc.d.ts |
