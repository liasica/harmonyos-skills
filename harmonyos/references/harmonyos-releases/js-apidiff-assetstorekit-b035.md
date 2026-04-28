---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-assetstorekit-b035
title: Asset Store Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > Asset Store Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:29+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:bc784bfe8c9fd4ea2a69b32d2675397909582fd09b17370ce86c3d398c8c5ff8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：asset；  API声明：function remove(query: AssetMap): Promise<void>;  差异内容：24000001,24000002,24000006,24000007,24000008,24000010,24000011,24000012,24000013,401 | 类名：asset；  API声明：function remove(query: AssetMap): Promise<void>;  差异内容：24000001,24000002,24000006,24000007,24000008,24000010,24000011,24000012,24000013,24000015,401 | api/@ohos.security.asset.d.ts |
| 错误码变更 | 类名：asset；  API声明：function removeSync(query: AssetMap): void;  差异内容：24000001,24000002,24000006,24000007,24000008,24000010,24000011,24000012,24000013,401 | 类名：asset；  API声明：function removeSync(query: AssetMap): void;  差异内容：24000001,24000002,24000006,24000007,24000008,24000010,24000011,24000012,24000013,24000015,401 | api/@ohos.security.asset.d.ts |
| 权限变更 | 类名：Tag；  API声明：IS\_PERSISTENT = TagType.BOOL | 0x11  差异内容：ohos.permission.STORE\_PERSISTENT\_DATA | 类名：Tag；  API声明：IS\_PERSISTENT = TagType.BOOL | 0x11  差异内容：NA | api/@ohos.security.asset.d.ts |
