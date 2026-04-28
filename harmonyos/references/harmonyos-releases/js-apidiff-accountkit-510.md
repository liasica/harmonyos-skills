---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accountkit-510
title: Account Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Account Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6edbf298e7e4b18ea220582279f8f5a846edc71fd35431afdb62f9095e2feac3
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：HuaweiIDProvider；  API声明：getMobileNumberConsistency(request: ConsistencyRequest): Promise<ConsistencyResult>;  差异内容：NA | 类名：HuaweiIDProvider；  API声明：getMobileNumberConsistency(request: ConsistencyRequest): Promise<ConsistencyResult>;  差异内容：801 | api/@hms.core.authentication.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：LoginPanelParams；  API声明：riskLevel?: boolean;  差异内容：riskLevel?: boolean; | api/@hms.core.account.LoginComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：LoginWithHuaweiIDButtonParams；  API声明：riskLevel?: boolean;  差异内容：riskLevel?: boolean; | api/@hms.core.account.LoginComponent.d.ets |
