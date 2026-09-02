---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-callservicekit-6112
title: Call Service Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Release引入的API > Call Service Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:3c2cab77b1dc5814f6a2f17e635978619dd4a33313fd7494906cfbc7eb625ac1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：CallerInfoQueryExtensionAbility；  API声明：onQueryBusinessServiceData(phoneNumber: string): Promise<Array<BusinessServiceData>>;  差异内容：onQueryBusinessServiceData(phoneNumber: string): Promise<Array<BusinessServiceData>>; | api/@hms.telephony.CallerInfoQueryExtensionAbility.d.ts |
| 新增API | NA | 类名：SwitchState；  API声明：isBusinessServiceDataEnabled: boolean;  差异内容：isBusinessServiceDataEnabled: boolean; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify；  API声明：export interface BusinessServiceData  差异内容：export interface BusinessServiceData | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：BusinessServiceData；  API声明：type: BusinessServiceType;  差异内容：type: BusinessServiceType; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：BusinessServiceData；  API声明：delivery?: DeliveryData;  差异内容：delivery?: DeliveryData; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify；  API声明：export enum BusinessServiceType  差异内容：export enum BusinessServiceType | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：BusinessServiceType；  API声明：DELIVERY = 0  差异内容：DELIVERY = 0 | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify；  API声明：export interface DeliveryData  差异内容：export interface DeliveryData | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：DeliveryData；  API声明：customerName: string;  差异内容：customerName: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：DeliveryData；  API声明：deliveryNumber: string;  差异内容：deliveryNumber: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：DeliveryData；  API声明：deliveryStatus: string;  差异内容：deliveryStatus: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：DeliveryData；  API声明：deliveryStatusColor: DeliveryStatusColor;  差异内容：deliveryStatusColor: DeliveryStatusColor; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：DeliveryData；  API声明：deliveryAddress: string;  差异内容：deliveryAddress: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：DeliveryData；  API声明：deliveryTimeout: string;  差异内容：deliveryTimeout: string; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify；  API声明：export enum DeliveryStatusColor  差异内容：export enum DeliveryStatusColor | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：DeliveryStatusColor；  API声明：BLUE = 0  差异内容：BLUE = 0 | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：DeliveryStatusColor；  API声明：GREEN = 1  差异内容：GREEN = 1 | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：DeliveryStatusColor；  API声明：RED = 2  差异内容：RED = 2 | api/@hms.telephony.numberIdentify.d.ts |
