---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-adskit-b035
title: Ads Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > Ads Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8892e0fd889c1c9f5458930aeecf0dd760556a01eed66ffdd8e1cdda798eef6c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：AdLoader；  API声明：loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void;  差异内容：21800001,21800003,401 | 类名：AdLoader；  API声明：loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void;  差异内容：21800001,21800003,401,801 | api/@ohos.advertising.d.ts |
| 错误码变更 | 类名：AdLoader；  API声明：loadAdWithMultiSlots(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void;  差异内容：21800001,21800003,401 | 类名：AdLoader；  API声明：loadAdWithMultiSlots(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void;  差异内容：21800001,21800003,401,801 | api/@ohos.advertising.d.ts |
| 错误码变更 | 类名：advertising；  API声明：function getAdRequestBody(adParams: AdRequestParams[], adOptions: AdOptions): Promise<string>;  差异内容：21800001,401 | 类名：advertising；  API声明：function getAdRequestBody(adParams: AdRequestParams[], adOptions: AdOptions): Promise<string>;  差异内容：21800001,401,801 | api/@ohos.advertising.d.ts |
| 错误码变更 | 类名：advertising；  API声明：function parseAdResponse(adResponse: string, listener: MultiSlotsAdLoadListener, context: common.UIAbilityContext): void;  差异内容：21800001,21800005,401 | 类名：advertising；  API声明：function parseAdResponse(adResponse: string, listener: MultiSlotsAdLoadListener, context: common.UIAbilityContext): void;  差异内容：21800001,21800005,401,801 | api/@ohos.advertising.d.ts |
