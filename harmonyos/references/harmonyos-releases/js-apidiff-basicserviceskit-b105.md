---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-b105
title: Basic Services Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a1e9c0b07d0c86e8d03e3f70bf4ef534b2d0db6bffd9baba55dea3a843c9db12
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：settings；  API声明：function setValue(context: Context, name: string, value: string, domainName: string): Promise<boolean>;  差异内容：201 | 类名：settings；  API声明：function setValue(context: Context, name: string, value: string, domainName: string): Promise<boolean>;  差异内容：NA | api/@ohos.settings.d.ts |
| 错误码变更 | 类名：settings；  API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean;  差异内容：201 | 类名：settings；  API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean;  差异内容：NA | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：deviceInfo；  API声明：const distributionOSApiName: string;  差异内容：const distributionOSApiName: string; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：pasteboard；  API声明： enum Pattern  差异内容： enum Pattern | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：Pattern；  API声明：URL = 0  差异内容：URL = 0 | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：Pattern；  API声明：NUMBER = 1  差异内容：NUMBER = 1 | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：Pattern；  API声明：EMAIL\_ADDRESS = 2  差异内容：EMAIL\_ADDRESS = 2 | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：SystemPasteboard；  API声明：detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>;  差异内容：detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>; | api/@ohos.pasteboard.d.ts |
