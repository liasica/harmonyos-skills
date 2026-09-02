---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-nearlinkkit-6111
title: NearLink Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > NearLink Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c9e2a1bdd8a4c2e78cfbfa81e20551abfbff48757220c776f61dfe97e50ca574
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace cdsm  差异内容：declare namespace cdsm | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：cdsm；  API声明：function createCdsmClient(address: string): CdsmClient;  差异内容：function createCdsmClient(address: string): CdsmClient; | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：cdsm；  API声明：interface CdsmClient  差异内容：interface CdsmClient | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmClient；  API声明：getCdsmInfo(): CdsmInfo;  差异内容：getCdsmInfo(): CdsmInfo; | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmClient；  API声明：onCdsmInfoChange(callback: Callback<CdsmInfo>): void;  差异内容：onCdsmInfoChange(callback: Callback<CdsmInfo>): void; | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmClient；  API声明：offCdsmInfoChange(callback?: Callback<CdsmInfo>): void;  差异内容：offCdsmInfoChange(callback?: Callback<CdsmInfo>): void; | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：cdsm；  API声明：interface CdsmInfo  差异内容：interface CdsmInfo | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmInfo；  API声明：members: Array<CdsmMemberInfo>;  差异内容：members: Array<CdsmMemberInfo>; | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：cdsm；  API声明：interface CdsmMemberInfo  差异内容：interface CdsmMemberInfo | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmMemberInfo；  API声明：address: string;  差异内容：address: string; | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmMemberInfo；  API声明：state: CdsmConnectionState;  差异内容：state: CdsmConnectionState; | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：cdsm；  API声明：enum CdsmConnectionState  差异内容：enum CdsmConnectionState | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmConnectionState；  API声明：DISCONNECTED = 0  差异内容：DISCONNECTED = 0 | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmConnectionState；  API声明：CONNECTED = 1  差异内容：CONNECTED = 1 | api/@hms.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：RemoteDevice；  API声明：getDeviceInformation(): DeviceInformation;  差异内容：getDeviceInformation(): DeviceInformation; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice；  API声明：interface DeviceInformation  差异内容：interface DeviceInformation | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：DeviceInformation；  API声明：manufacturerData: string;  差异内容：manufacturerData: string; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：DeviceInformation；  API声明：modelData: string;  差异内容：modelData: string; | api/@hms.nearlink.remoteDevice.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.nearlink.cdsm.d.ts  差异内容：NearLinkKit | api/@hms.nearlink.cdsm.d.ts |
