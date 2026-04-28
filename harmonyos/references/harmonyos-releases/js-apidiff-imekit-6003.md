---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-6003
title: IME Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > IME Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:18+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:061bcb6ed4b2c7bf0dc5fc021d1e34f4ac02d2b354322ac6fe630e51a1cf24ed
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：InputClient；  API声明：getAttachOptions(): AttachOptions;  差异内容：801 | 类名：InputClient；  API声明：getAttachOptions(): AttachOptions;  差异内容：NA | api/@ohos.inputMethodEngine.d.ts |
| 删除错误码 | 类名：InputClient；  API声明：on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void;  差异内容：801 | 类名：InputClient；  API声明：on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void;  差异内容：NA | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明：function setSimpleKeyboardEnabled(enable: boolean): void;  差异内容：function setSimpleKeyboardEnabled(enable: boolean): void; | api/@ohos.inputMethod.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AttachOptions；  API声明：isSimpleKeyboardEnabled?: boolean;  差异内容：isSimpleKeyboardEnabled?: boolean; | api/@ohos.inputMethodEngine.d.ts |
