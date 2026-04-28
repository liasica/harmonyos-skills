---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-504
title: Connectivity Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.4(16) > OS平台能力 > API变更清单 > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8f8fc75ed257a657b480eeb7a1f70b367014688983a5bca838b5e007258e809d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace opp  差异内容： declare namespace opp | api/@ohos.bluetooth.opp.d.ts |
| 新增API | NA | 类名：opp；  API声明：function createOppServerProfile(): OppServerProfile;  差异内容：function createOppServerProfile(): OppServerProfile; | api/@ohos.bluetooth.opp.d.ts |
| 新增API | NA | 类名：opp；  API声明： interface OppServerProfile  差异内容： interface OppServerProfile | api/@ohos.bluetooth.opp.d.ts |
| 新增API | NA | 类名：connection；  API声明：function getRemoteDeviceName(deviceId: string, alias?: boolean): string;  差异内容：function getRemoteDeviceName(deviceId: string, alias?: boolean): string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function connectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void;  差异内容：function connectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection；  API声明：function connectAllowedProfiles(deviceId: string): Promise<void>;  差异内容：function connectAllowedProfiles(deviceId: string): Promise<void>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：access；  API声明：function addPersistentDeviceId(deviceId: string): Promise<void>;  差异内容：function addPersistentDeviceId(deviceId: string): Promise<void>; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access；  API声明：function deletePersistentDeviceId(deviceId: string): Promise<void>;  差异内容：function deletePersistentDeviceId(deviceId: string): Promise<void>; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access；  API声明：function getPersistentDeviceIds(): string[];  差异内容：function getPersistentDeviceIds(): string[]; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access；  API声明：function isValidRandomDeviceId(deviceId: string): boolean;  差异内容：function isValidRandomDeviceId(deviceId: string): boolean; | api/@ohos.bluetooth.access.d.ts |
| kit变更 | NA | ConnectivityKit | api/@ohos.bluetooth.opp.d.ts |
