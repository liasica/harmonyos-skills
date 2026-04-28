---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-6002
title: ArkTS
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > ArkTS
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:26+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8190fe58f94973eb4197538bfacdf155c73ffd0b1fc42d3b26600dfd3ca684c0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：xml；  API声明：type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean;  差异内容：type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean; | api/@ohos.xml.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ParseOptions；  API声明：attributeWithTagCallbackFunction?: AttributeWithTagCb;  差异内容：attributeWithTagCallbackFunction?: AttributeWithTagCb; | api/@ohos.xml.d.ts |
