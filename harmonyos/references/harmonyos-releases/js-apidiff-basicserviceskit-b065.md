---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-b065
title: Basic Services Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5530c268ea2631ce224d0e25187db001f41e7401399ac426441e6d17cfed090a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：usbManager；  API声明：function controlTransfer(pipe: USBDevicePipe, controlparam: USBControlParams, timeout?: number): Promise<number>;  差异内容：NA | 类名：usbManager；  API声明：function controlTransfer(pipe: USBDevicePipe, controlparam: USBControlParams, timeout?: number): Promise<number>;  差异内容：12 | api/@ohos.usbManager.d.ts |
| 错误码变更 | 类名：usbManager；  API声明：function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number;  差异内容：NA | 类名：usbManager；  API声明：function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number;  差异内容：401 | api/@ohos.usbManager.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：getCode(callback: AsyncCallback<number>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：getCode(callback: AsyncCallback<number>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：setCode(code: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：setCode(code: number, callback: AsyncCallback<void>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：setCode(code: number): Promise<void>;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：setCode(code: number): Promise<void>;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：getData(callback: AsyncCallback<string>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：getData(callback: AsyncCallback<string>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：setData(data: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：setData(data: string, callback: AsyncCallback<void>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：setData(data: string): Promise<void>;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：setData(data: string): Promise<void>;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：setCodeAndData(code: number, data: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：setCodeAndData(code: number, data: string, callback: AsyncCallback<void>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：setCodeAndData(code: number, data: string): Promise<void>;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：setCodeAndData(code: number, data: string): Promise<void>;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：isOrderedCommonEvent(callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：isOrderedCommonEvent(callback: AsyncCallback<boolean>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：isStickyCommonEvent(callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：isStickyCommonEvent(callback: AsyncCallback<boolean>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：abortCommonEvent(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：abortCommonEvent(callback: AsyncCallback<void>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：clearAbortCommonEvent(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：clearAbortCommonEvent(callback: AsyncCallback<void>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：getAbortCommonEvent(callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：getAbortCommonEvent(callback: AsyncCallback<boolean>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 错误码变更 | 类名：CommonEventSubscriber；  API声明：finishCommonEvent(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：CommonEventSubscriber；  API声明：finishCommonEvent(callback: AsyncCallback<void>): void;  差异内容：401 | api/commonEvent/commonEventSubscriber.d.ts |
| 新增API | NA | 类名：usbManager；  API声明：function usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout?: number): Promise<number>;  差异内容：function usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout?: number): Promise<number>; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：usbManager；  API声明： interface USBDeviceRequestParams  差异内容： interface USBDeviceRequestParams | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBDeviceRequestParams；  API声明：bmRequestType: number;  差异内容：bmRequestType: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBDeviceRequestParams；  API声明：bRequest: number;  差异内容：bRequest: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBDeviceRequestParams；  API声明：wValue: number;  差异内容：wValue: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBDeviceRequestParams；  API声明：wIndex: number;  差异内容：wIndex: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBDeviceRequestParams；  API声明：wLength: number;  差异内容：wLength: number; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：USBDeviceRequestParams；  API声明：data: Uint8Array;  差异内容：data: Uint8Array; | api/@ohos.usbManager.d.ts |
| 新增API | NA | 类名：PasteData；  API声明：pasteStart(): void;  差异内容：pasteStart(): void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：PasteData；  API声明：pasteComplete(): void;  差异内容：pasteComplete(): void; | api/@ohos.pasteboard.d.ts |
