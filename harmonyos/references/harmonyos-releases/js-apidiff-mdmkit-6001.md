---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-6001
title: MDM Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > MDM Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:41+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9a943a1fc2e873b80d88c1310f1bbb1ec485d9597dad260421d29f527bb224c7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：bluetoothManager；  API声明：function turnOnBluetooth(admin: Want): void;  差异内容：function turnOnBluetooth(admin: Want): void; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bluetoothManager；  API声明：function turnOffBluetooth(admin: Want): void;  差异内容：function turnOffBluetooth(admin: Want): void; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bluetoothManager；  API声明：function addDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void;  差异内容：function addDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bluetoothManager；  API声明：function removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void;  差异内容：function removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bluetoothManager；  API声明：function getDisallowedBluetoothDevices(admin: Want): Array<string>;  差异内容：function getDisallowedBluetoothDevices(admin: Want): Array<string>; | api/@ohos.enterprise.bluetoothManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：interface Resource  差异内容：interface Resource | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：Resource；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：Resource；  API声明：moduleName: string;  差异内容：moduleName: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：Resource；  API声明：id: number;  差异内容：id: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：interface BundleInfo  差异内容：interface BundleInfo | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly name: string;  差异内容：readonly name: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly vendor: string;  差异内容：readonly vendor: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly versionCode: number;  差异内容：readonly versionCode: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly versionName: string;  差异内容：readonly versionName: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly minCompatibleVersionCode: number;  差异内容：readonly minCompatibleVersionCode: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly targetVersion: number;  差异内容：readonly targetVersion: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly appInfo: ApplicationInfo;  差异内容：readonly appInfo: ApplicationInfo; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly signatureInfo: SignatureInfo;  差异内容：readonly signatureInfo: SignatureInfo; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly installTime: number;  差异内容：readonly installTime: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly updateTime: number;  差异内容：readonly updateTime: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly appIndex: number;  差异内容：readonly appIndex: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：BundleInfo；  API声明：readonly firstInstallTime?: number;  差异内容：readonly firstInstallTime?: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：interface SignatureInfo  差异内容：interface SignatureInfo | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：SignatureInfo；  API声明：readonly appId: string;  差异内容：readonly appId: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：SignatureInfo；  API声明：readonly fingerprint: string;  差异内容：readonly fingerprint: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：SignatureInfo；  API声明：readonly appIdentifier: string;  差异内容：readonly appIdentifier: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：SignatureInfo；  API声明：readonly certificate?: string;  差异内容：readonly certificate?: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：interface ApplicationInfo  差异内容：interface ApplicationInfo | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly name: string;  差异内容：readonly name: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly description: string;  差异内容：readonly description: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly descriptionId: number;  差异内容：readonly descriptionId: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly enabled: boolean;  差异内容：readonly enabled: boolean; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly label: string;  差异内容：readonly label: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly labelId: number;  差异内容：readonly labelId: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly icon: string;  差异内容：readonly icon: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly iconId: number;  差异内容：readonly iconId: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly process: string;  差异内容：readonly process: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly codePath: string;  差异内容：readonly codePath: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly removable: boolean;  差异内容：readonly removable: boolean; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly accessTokenId: number;  差异内容：readonly accessTokenId: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly uid: number;  差异内容：readonly uid: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly iconResource: Resource;  差异内容：readonly iconResource: Resource; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly labelResource: Resource;  差异内容：readonly labelResource: Resource; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly descriptionResource: Resource;  差异内容：readonly descriptionResource: Resource; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly appDistributionType: string;  差异内容：readonly appDistributionType: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly appProvisionType: string;  差异内容：readonly appProvisionType: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly systemApp: boolean;  差异内容：readonly systemApp: boolean; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly debug: boolean;  差异内容：readonly debug: boolean; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly dataUnclearable: boolean;  差异内容：readonly dataUnclearable: boolean; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly nativeLibraryPath: string;  差异内容：readonly nativeLibraryPath: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly appIndex: number;  差异内容：readonly appIndex: number; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly installSource: string;  差异内容：readonly installSource: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：ApplicationInfo；  API声明：readonly releaseType: string;  差异内容：readonly releaseType: string; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：bundleManager；  API声明：function getInstalledBundleList(admin: Want, accountId: number): Promise<Array<BundleInfo>>;  差异内容：function getInstalledBundleList(admin: Want, accountId: number): Promise<Array<BundleInfo>>; | api/@ohos.enterprise.bundleManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function turnOnWifi(admin: Want, isForce: boolean): void;  差异内容：function turnOnWifi(admin: Want, isForce: boolean): void; | api/@ohos.enterprise.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager；  API声明：function turnOffWifi(admin: Want): void;  差异内容：function turnOffWifi(admin: Want): void; | api/@ohos.enterprise.wifiManager.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：OtaUpdatePolicy；  API声明：disableSystemOtaUpdate?: boolean;  差异内容：disableSystemOtaUpdate?: boolean; | api/@ohos.enterprise.systemManager.d.ts |
