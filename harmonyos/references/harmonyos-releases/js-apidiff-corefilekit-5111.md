---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-5111
title: Core File Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Core File Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:52+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f17da89030103bb42970f1f89c0f1a1724190d7899a380d02aa4f3fb04574c4f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：fileShare；  API声明：function checkPersistentPermission(policies: Array<PolicyInfo>): Promise<Array<boolean>>;  差异内容：201 | 类名：fileShare；  API声明：function checkPersistentPermission(policies: Array<PolicyInfo>): Promise<Array<boolean>>;  差异内容：NA | api/@ohos.fileshare.d.ts |
| 权限变更 | 类名：fileShare；  API声明：function checkPersistentPermission(policies: Array<PolicyInfo>): Promise<Array<boolean>>;  差异内容：ohos.permission.FILE\_ACCESS\_PERSIST | 类名：fileShare；  API声明：function checkPersistentPermission(policies: Array<PolicyInfo>): Promise<Array<boolean>>;  差异内容：NA | api/@ohos.fileshare.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：DocumentSelectOptions；  API声明：isEncryptionSupported?: boolean;  差异内容：isEncryptionSupported?: boolean; | api/@ohos.file.picker.d.ts |
