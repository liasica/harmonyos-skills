---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accessorykit-7001
title: Accessory Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Accessory Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c7a9c66036999b40e31d893f8a94a72be2ae9f33efeb6c2868e9fc5e98e30372
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace accessoryAccessManager  差异内容：declare namespace accessoryAccessManager | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：enum DiscoveryType  差异内容：enum DiscoveryType | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：DiscoveryType；  API声明：PARTNER\_BLE\_CONNECT = 0  差异内容：PARTNER\_BLE\_CONNECT = 0 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：enum ServiceName  差异内容：enum ServiceName | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ServiceName；  API声明：PARTNER\_APP\_ACCESSORY\_COLLABORATION = 'P\_AppAccessoryCollaboration'  差异内容：PARTNER\_APP\_ACCESSORY\_COLLABORATION = 'P\_AppAccessoryCollaboration' | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ServiceName；  API声明：PARTNER\_SHARE\_SERVICE = 'P\_ShareService'  差异内容：PARTNER\_SHARE\_SERVICE = 'P\_ShareService' | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ServiceName；  API声明：PARTNER\_DISTRIBUTED\_CAMERA\_SERVICE = 'P\_DCameraService'  差异内容：PARTNER\_DISTRIBUTED\_CAMERA\_SERVICE = 'P\_DCameraService' | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：enum WakeupType  差异内容：enum WakeupType | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：WakeupType；  API声明：START\_ABILITY\_BY\_CALL = 0  差异内容：START\_ABILITY\_BY\_CALL = 0 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：interface StringResourceInfo  差异内容：interface StringResourceInfo | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：StringResourceInfo；  API声明：moduleName: string;  差异内容：moduleName: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：StringResourceInfo；  API声明：stringResourceId: number;  差异内容：stringResourceId: number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：StringResourceInfo；  API声明：bundleName?: string;  差异内容：bundleName?: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：interface WakeupInfo  差异内容：interface WakeupInfo | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：WakeupInfo；  API声明：wakeupType: WakeupType;  差异内容：wakeupType: WakeupType; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：WakeupInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：WakeupInfo；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：WakeupInfo；  API声明：briefDesc: StringResourceInfo;  差异内容：briefDesc: StringResourceInfo; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：interface ServiceInfo  差异内容：interface ServiceInfo | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ServiceInfo；  API声明：serviceName: ServiceName;  差异内容：serviceName: ServiceName; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ServiceInfo；  API声明：parameters?: Record<string, Object>;  差异内容：parameters?: Record<string, Object>; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：interface PickerItemInfo  差异内容：interface PickerItemInfo | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：PickerItemInfo；  API声明：discoveryType: DiscoveryType;  差异内容：discoveryType: DiscoveryType; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：PickerItemInfo；  API声明：displayName: string;  差异内容：displayName: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：PickerItemInfo；  API声明：displayImage: image.PixelMap;  差异内容：displayImage: image.PixelMap; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：PickerItemInfo；  API声明：requestAttachServiceInfo: Array<ServiceInfo>;  差异内容：requestAttachServiceInfo: Array<ServiceInfo>; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：PickerItemInfo；  API声明：hasScreen?: boolean;  差异内容：hasScreen?: boolean; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：PickerItemInfo；  API声明：bleAddress?: string;  差异内容：bleAddress?: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：PickerItemInfo；  API声明：bleMtuSize?: number;  差异内容：bleMtuSize?: number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：PickerItemInfo；  API声明：productId?: string;  差异内容：productId?: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：PickerItemInfo；  API声明：subProductId?: string;  差异内容：subProductId?: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：interface AccessoryInfo  差异内容：interface AccessoryInfo | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessoryInfo；  API声明：displayName: string;  差异内容：displayName: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessoryInfo；  API声明：accessoryId?: string;  差异内容：accessoryId?: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessoryInfo；  API声明：bleAddress?: string;  差异内容：bleAddress?: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessoryInfo；  API声明：productId?: string;  差异内容：productId?: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：enum AccessEvent  差异内容：enum AccessEvent | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEvent；  API声明：PICKER\_PRESENT = 0  差异内容：PICKER\_PRESENT = 0 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEvent；  API声明：PICKER\_DISMISS = 1  差异内容：PICKER\_DISMISS = 1 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEvent；  API声明：PICKER\_END\_SUCC = 2  差异内容：PICKER\_END\_SUCC = 2 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEvent；  API声明：PICKER\_END\_FAIL = 3  差异内容：PICKER\_END\_FAIL = 3 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEvent；  API声明：SERVICE\_ATTACHING = 300  差异内容：SERVICE\_ATTACHING = 300 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEvent；  API声明：SERVICE\_ATTACH\_SUCC = 301  差异内容：SERVICE\_ATTACH\_SUCC = 301 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEvent；  API声明：SERVICE\_ATTACH\_FAIL = 302  差异内容：SERVICE\_ATTACH\_FAIL = 302 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：interface AttachServiceInfo  差异内容：interface AttachServiceInfo | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AttachServiceInfo；  API声明：attachId: number;  差异内容：attachId: number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AttachServiceInfo；  API声明：accessoryInfo: AccessoryInfo;  差异内容：accessoryInfo: AccessoryInfo; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AttachServiceInfo；  API声明：serviceInfo: ServiceInfo;  差异内容：serviceInfo: ServiceInfo; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：interface AccessEventInfo  差异内容：interface AccessEventInfo | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEventInfo；  API声明：accessEvent: AccessEvent;  差异内容：accessEvent: AccessEvent; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEventInfo；  API声明：attachServiceInfo?: AttachServiceInfo;  差异内容：attachServiceInfo?: AttachServiceInfo; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEventInfo；  API声明：errorCode?: number;  差异内容：errorCode?: number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessEventInfo；  API声明：errorDesc?: string;  差异内容：errorDesc?: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：enum DetachServiceEvent  差异内容：enum DetachServiceEvent | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：DetachServiceEvent；  API声明：SERVICE\_DETACH\_SUCC = 0  差异内容：SERVICE\_DETACH\_SUCC = 0 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：DetachServiceEvent；  API声明：SERVICE\_DETACH\_FAIL = 1  差异内容：SERVICE\_DETACH\_FAIL = 1 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：class AccessManager  差异内容：class AccessManager | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessManager；  API声明：showAccessPicker(items: Array<PickerItemInfo>, callback: Callback<AccessEventInfo>): number;  差异内容：showAccessPicker(items: Array<PickerItemInfo>, callback: Callback<AccessEventInfo>): number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessManager；  API声明：modifyDisplayName(accessoryId: string, displayName: string): number;  差异内容：modifyDisplayName(accessoryId: string, displayName: string): number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessManager；  API声明：queryAttachedService(): Array<AttachServiceInfo>;  差异内容：queryAttachedService(): Array<AttachServiceInfo>; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：AccessManager；  API声明：detachService(attachId: number, callback: Callback<DetachServiceEvent>): number;  差异内容：detachService(attachId: number, callback: Callback<DetachServiceEvent>): number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：enum ChannelType  差异内容：enum ChannelType | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelType；  API声明：PARTNER\_WIFI\_CHANNEL = 1  差异内容：PARTNER\_WIFI\_CHANNEL = 1 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：enum ChannelEvent  差异内容：enum ChannelEvent | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelEvent；  API声明：CONNECTING = 0  差异内容：CONNECTING = 0 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelEvent；  API声明：CONNECTED = 1  差异内容：CONNECTED = 1 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelEvent；  API声明：CONNECT\_FAIL = 2  差异内容：CONNECT\_FAIL = 2 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelEvent；  API声明：DISCONNECTED = 3  差异内容：DISCONNECTED = 3 | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：interface ChannelEventInfo  差异内容：interface ChannelEventInfo | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelEventInfo；  API声明：channelEvent: ChannelEvent;  差异内容：channelEvent: ChannelEvent; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelEventInfo；  API声明：attachId: number;  差异内容：attachId: number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelEventInfo；  API声明：channelType: ChannelType;  差异内容：channelType: ChannelType; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelEventInfo；  API声明：ip?: string;  差异内容：ip?: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelEventInfo；  API声明：errorCode?: number;  差异内容：errorCode?: number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ChannelEventInfo；  API声明：reason?: string;  差异内容：reason?: string; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：interface ConnectRequestInfo  差异内容：interface ConnectRequestInfo | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ConnectRequestInfo；  API声明：attachId: number;  差异内容：attachId: number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ConnectRequestInfo；  API声明：channelType: ChannelType;  差异内容：channelType: ChannelType; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ConnectRequestInfo；  API声明：serviceDesc: StringResourceInfo;  差异内容：serviceDesc: StringResourceInfo; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：accessoryAccessManager；  API声明：class ConnectManager  差异内容：class ConnectManager | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ConnectManager；  API声明：registerConnectListener(attachId: number, stateCallback: Callback<ChannelEventInfo>): number;  差异内容：registerConnectListener(attachId: number, stateCallback: Callback<ChannelEventInfo>): number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ConnectManager；  API声明：unregisterConnectListener(attachId: number): number;  差异内容：unregisterConnectListener(attachId: number): number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ConnectManager；  API声明：connect(connectRequestInfo: ConnectRequestInfo): number;  差异内容：connect(connectRequestInfo: ConnectRequestInfo): number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增API | NA | 类名：ConnectManager；  API声明：disconnect(attachId: number): number;  差异内容：disconnect(attachId: number): number; | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.collaboration.accessoryAccessManager.d.ts  差异内容：AccessoryKit | api/@hms.collaboration.accessoryAccessManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：kits@kit.AccessoryKit.d.ts  差异内容：AccessoryKit | kits/@kit.AccessoryKit.d.ts |
