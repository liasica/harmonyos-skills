---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-6001
title: Basic Services Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5e2e9704607982c7842628328cb3a9b391dedd699bfa1ba8ab27a9d048e283dc
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：power；  API声明：function isActive(): boolean;  差异内容：4900101 | 类名：power；  API声明：function isActive(): boolean;  差异内容：NA | api/@ohos.power.d.ts |
| 删除错误码 | 类名：power；  API声明：function getPowerMode(): DevicePowerMode;  差异内容：4900101 | 类名：power；  API声明：function getPowerMode(): DevicePowerMode;  差异内容：NA | api/@ohos.power.d.ts |
| 删除错误码 | 类名：RunningLock；  API声明：hold(timeout: number): void;  差异内容：4900101 | 类名：RunningLock；  API声明：hold(timeout: number): void;  差异内容：NA | api/@ohos.runningLock.d.ts |
| 删除错误码 | 类名：RunningLock；  API声明：isHolding(): boolean;  差异内容：4900101 | 类名：RunningLock；  API声明：isHolding(): boolean;  差异内容：NA | api/@ohos.runningLock.d.ts |
| 删除错误码 | 类名：RunningLock；  API声明：unhold(): void;  差异内容：4900101 | 类名：RunningLock；  API声明：unhold(): void;  差异内容：NA | api/@ohos.runningLock.d.ts |
| 删除错误码 | 类名：runningLock；  API声明：function isSupported(type: RunningLockType): boolean;  差异内容：4900101 | 类名：runningLock；  API声明：function isSupported(type: RunningLockType): boolean;  差异内容：NA | api/@ohos.runningLock.d.ts |
| 删除错误码 | 类名：thermal；  API声明：function registerThermalLevelCallback(callback: Callback<ThermalLevel>): void;  差异内容：4800101 | 类名：thermal；  API声明：function registerThermalLevelCallback(callback: Callback<ThermalLevel>): void;  差异内容：NA | api/@ohos.thermal.d.ts |
| 删除错误码 | 类名：thermal；  API声明：function unregisterThermalLevelCallback(callback?: Callback<void>): void;  差异内容：4800101 | 类名：thermal；  API声明：function unregisterThermalLevelCallback(callback?: Callback<void>): void;  差异内容：NA | api/@ohos.thermal.d.ts |
| 删除错误码 | 类名：thermal；  API声明：function getLevel(): ThermalLevel;  差异内容：4800101 | 类名：thermal；  API声明：function getLevel(): ThermalLevel;  差异内容：NA | api/@ohos.thermal.d.ts |
| 错误码变更 | 类名：commonEventManager；  API声明：function publish(event: string, callback: AsyncCallback<void>): void;  差异内容：1500007,1500008,1500009,401 | 类名：commonEventManager；  API声明：function publish(event: string, callback: AsyncCallback<void>): void;  差异内容：1500003,1500007,1500008,1500009 | api/@ohos.commonEventManager.d.ts |
| 错误码变更 | 类名：commonEventManager；  API声明：function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void;  差异内容：1500007,1500008,1500009,401 | 类名：commonEventManager；  API声明：function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void;  差异内容：1500003,1500007,1500008,1500009 | api/@ohos.commonEventManager.d.ts |
| 错误码变更 | 类名：commonEventManager；  API声明：function subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void;  差异内容：1500007,1500008,401,801 | 类名：commonEventManager；  API声明：function subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void;  差异内容：1500007,1500008,1500010,801 | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：commonEventManager；  API声明：function subscribeToEvent(subscriber: CommonEventSubscriber, callback: Callback<CommonEventData>): Promise<void>;  差异内容：function subscribeToEvent(subscriber: CommonEventSubscriber, callback: Callback<CommonEventData>): Promise<void>; | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：deviceInfo；  API声明：enum DeviceTypes  差异内容：enum DeviceTypes | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：DeviceTypes；  API声明：TYPE\_DEFAULT = 'default'  差异内容：TYPE\_DEFAULT = 'default' | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：DeviceTypes；  API声明：TYPE\_PHONE = 'phone'  差异内容：TYPE\_PHONE = 'phone' | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：DeviceTypes；  API声明：TYPE\_TABLET = 'tablet'  差异内容：TYPE\_TABLET = 'tablet' | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：DeviceTypes；  API声明：TYPE\_2IN1 = '2in1'  差异内容：TYPE\_2IN1 = '2in1' | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：DeviceTypes；  API声明：TYPE\_TV = 'tv'  差异内容：TYPE\_TV = 'tv' | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：DeviceTypes；  API声明：TYPE\_WEARABLE = 'wearable'  差异内容：TYPE\_WEARABLE = 'wearable' | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：DeviceTypes；  API声明：TYPE\_CAR = 'car'  差异内容：TYPE\_CAR = 'car' | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：deviceInfo；  API声明：const sdkMinorApiVersion: number;  差异内容：const sdkMinorApiVersion: number; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：deviceInfo；  API声明：const sdkPatchApiVersion: number;  差异内容：const sdkPatchApiVersion: number; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：agent；  API声明：enum WaitingReason  差异内容：enum WaitingReason | api/@ohos.request.d.ts |
| 新增API | NA | 类名：WaitingReason；  API声明：TASK\_QUEUE\_FULL = 0x00  差异内容：TASK\_QUEUE\_FULL = 0x00 | api/@ohos.request.d.ts |
| 新增API | NA | 类名：WaitingReason；  API声明：NETWORK\_NOT\_MATCH = 0x01  差异内容：NETWORK\_NOT\_MATCH = 0x01 | api/@ohos.request.d.ts |
| 新增API | NA | 类名：WaitingReason；  API声明：APP\_BACKGROUND = 0x02  差异内容：APP\_BACKGROUND = 0x02 | api/@ohos.request.d.ts |
| 新增API | NA | 类名：WaitingReason；  API声明：USER\_INACTIVATED = 0x03  差异内容：USER\_INACTIVATED = 0x03 | api/@ohos.request.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function resetUsbDevice(pipe: USBDevicePipe): boolean;  差异内容：function resetUsbDevice(pipe: USBDevicePipe): boolean; | api/@ohos.usbManager.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Task；  API声明：on(event: 'faultOccur', callback: Callback<Faults>): void;  差异内容：on(event: 'faultOccur', callback: Callback<Faults>): void; | api/@ohos.request.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Task；  API声明：off(event: 'faultOccur', callback?: Callback<Faults>): void;  差异内容：off(event: 'faultOccur', callback?: Callback<Faults>): void; | api/@ohos.request.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Task；  API声明：on(event: 'wait', callback: Callback<WaitingReason>): void;  差异内容：on(event: 'wait', callback: Callback<WaitingReason>): void; | api/@ohos.request.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：Task；  API声明：off(event: 'wait', callback?: Callback<WaitingReason>): void;  差异内容：off(event: 'wait', callback?: Callback<WaitingReason>): void; | api/@ohos.request.d.ts |
