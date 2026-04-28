---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-6004
title: Telephony Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta5引入的API > Telephony Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:10+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d52c0eea879864715c1b3df4d71ed96429cae1a5600443d975fe1850a4a55b92
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：eSIM；  API声明：export interface AccessRule  差异内容：export interface AccessRule | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：AccessRule；  API声明：certificateHashHexStr: string;  差异内容：certificateHashHexStr: string; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：AccessRule；  API声明：packageName: string;  差异内容：packageName: string; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：AccessRule；  API声明：accessType: number;  差异内容：accessType: number; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：sim；  API声明：function getSimLabel(slotId: number, callback: AsyncCallback<SimLabel>): void;  差异内容：function getSimLabel(slotId: number, callback: AsyncCallback<SimLabel>): void; | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：sim；  API声明：function getSimLabel(slotId: number): Promise<SimLabel>;  差异内容：function getSimLabel(slotId: number): Promise<SimLabel>; | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：sim；  API声明：function getSimLabelSync(slotId: number): SimLabel;  差异内容：function getSimLabelSync(slotId: number): SimLabel; | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：sim；  API声明：export enum SimType  差异内容：export enum SimType | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：SimType；  API声明：PSIM = 0  差异内容：PSIM = 0 | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：SimType；  API声明：ESIM = 1  差异内容：ESIM = 1 | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：sim；  API声明：export interface SimLabel  差异内容：export interface SimLabel | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：SimLabel；  API声明：simType: SimType;  差异内容：simType: SimType; | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：SimLabel；  API声明：index: number;  差异内容：index: number; | api/@ohos.telephony.sim.d.ts |
