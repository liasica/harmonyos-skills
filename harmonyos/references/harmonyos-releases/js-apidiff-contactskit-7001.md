---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-contactskit-7001
title: Contacts Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Contacts Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:982a6266e6bc034a04dff40dc9137f67c3f83c999ce43b3ba851cf008c9df450
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：contact；  API声明：function selectContact(callback: AsyncCallback<Array<Contact>>): void;  差异内容：ohos.permission.READ\_CONTACTS | 类名：contact；  API声明：function selectContact(callback: AsyncCallback<Array<Contact>>): void;  差异内容：NA | api/@ohos.contact.d.ts |
| 权限变更 | 类名：contact；  API声明：function selectContact(): Promise<Array<Contact>>;  差异内容：ohos.permission.READ\_CONTACTS | 类名：contact；  API声明：function selectContact(): Promise<Array<Contact>>;  差异内容：NA | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSelectionOptions；  API声明：isAutoDismissOnNavigation?: boolean;  差异内容：isAutoDismissOnNavigation?: boolean; | api/@ohos.contact.d.ts |
