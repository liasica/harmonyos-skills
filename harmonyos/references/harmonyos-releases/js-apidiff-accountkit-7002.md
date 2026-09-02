---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accountkit-7002
title: Account Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Account Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:a03e4705a37620fae93d416ce41ec3c2fce62fd5de95ef4af597b98083a0437f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace intimate  差异内容：declare namespace intimate | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：intimate；  API声明：enum IntimateErrorCode  差异内容：enum IntimateErrorCode | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode；  API声明：ACCOUNT\_NOT\_LOGGED\_IN = 1026900001  差异内容：ACCOUNT\_NOT\_LOGGED\_IN = 1026900001 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode；  API声明：INTERNAL\_ERROR = 1026900003  差异内容：INTERNAL\_ERROR = 1026900003 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode；  API声明：SERVER\_ERROR = 1026900004  差异内容：SERVER\_ERROR = 1026900004 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode；  API声明：NETWORK\_ERROR = 1026900005  差异内容：NETWORK\_ERROR = 1026900005 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode；  API声明：PARAMETER\_ERROR = 1026900006  差异内容：PARAMETER\_ERROR = 1026900006 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode；  API声明：UNSUPPORTED\_REGION = 1026900007  差异内容：UNSUPPORTED\_REGION = 1026900007 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode；  API声明：USER\_CANCELED = 1026900008  差异内容：USER\_CANCELED = 1026900008 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimateErrorCode；  API声明：PERMISSION\_CHECK\_ERROR = 1026900009  差异内容：PERMISSION\_CHECK\_ERROR = 1026900009 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：intimate；  API声明：enum IdType  差异内容：enum IdType | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IdType；  API声明：OPEN\_ID = 1  差异内容：OPEN\_ID = 1 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IdType；  API声明：UNION\_ID = 2  差异内容：UNION\_ID = 2 | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：intimate；  API声明：interface IntimatesSelectionRequest  差异内容：interface IntimatesSelectionRequest | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionRequest；  API声明：maxSelectionCount?: number;  差异内容：maxSelectionCount?: number; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionRequest；  API声明：onlySelectIntimateWithHuaweiID?: boolean;  差异内容：onlySelectIntimateWithHuaweiID?: boolean; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionRequest；  API声明：idType: IdType;  差异内容：idType: IdType; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionRequest；  API声明：idValue: string;  差异内容：idValue: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：intimate；  API声明：interface IntimatesSelectionResponse  差异内容：interface IntimatesSelectionResponse | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionResponse；  API声明：openID?: string;  差异内容：openID?: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionResponse；  API声明：unionID?: string;  差异内容：unionID?: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionResponse；  API声明：anonymousAccount?: string;  差异内容：anonymousAccount?: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionResponse；  API声明：avatarUri: string;  差异内容：avatarUri: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：IntimatesSelectionResponse；  API声明：nickname: string;  差异内容：nickname: string; | api/@hms.core.account.intimate.d.ts |
| 新增API | NA | 类名：intimate；  API声明：function selectIntimates(context: common.Context, request: IntimatesSelectionRequest): Promise<IntimatesSelectionResponse[]>;  差异内容：function selectIntimates(context: common.Context, request: IntimatesSelectionRequest): Promise<IntimatesSelectionResponse[]>; | api/@hms.core.account.intimate.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.account.intimate.d.ts  差异内容：AccountKit | api/@hms.core.account.intimate.d.ts |
