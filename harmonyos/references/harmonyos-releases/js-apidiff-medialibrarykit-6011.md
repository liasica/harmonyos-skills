---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-6011
title: Media Library Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:00+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:64d88125ea8be90100780655b7ca7e70d786dbc635b785adf9cc8dc8a015c772
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export declare class PreselectedInfo  差异内容：export declare class PreselectedInfo | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PreselectedInfo；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PreselectedInfo；  API声明：preselectablePickerIndex?: number;  差异内容：preselectablePickerIndex?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class BadgeConfig  差异内容：export declare class BadgeConfig | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BadgeConfig；  API声明：badgeType?: BadgeType;  差异内容：badgeType?: BadgeType; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BadgeConfig；  API声明：uris?: Array<string>;  差异内容：uris?: Array<string>; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：DataType；  API声明：SET\_SELECTED\_INFO = 3  差异内容：SET\_SELECTED\_INFO = 3 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：DataType；  API声明：SET\_BADGE\_CONFIGS = 4  差异内容：SET\_BADGE\_CONFIGS = 4 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum BadgeType  差异内容：export declare enum BadgeType | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BadgeType；  API声明：BADGE\_UPLOADED = 0  差异内容：BADGE\_UPLOADED = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：PickerOptions；  API声明：pickerIndex?: number;  差异内容：pickerIndex?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：PickerOptions；  API声明：preselectedInfos?: Array<PreselectedInfo>;  差异内容：preselectedInfos?: Array<PreselectedInfo>; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：PickerOptions；  API声明：badgeConfig?: BadgeConfig;  差异内容：badgeConfig?: BadgeConfig; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：BaseItemInfo；  API声明：photoSubType?: photoAccessHelper.PhotoSubtype;  差异内容：photoSubType?: photoAccessHelper.PhotoSubtype; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：BaseItemInfo；  API声明：dynamicRangeType?: photoAccessHelper.DynamicRangeType;  差异内容：dynamicRangeType?: photoAccessHelper.DynamicRangeType; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：BaseItemInfo；  API声明：orientation?: number;  差异内容：orientation?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PickerController；  API声明：addData(dataType: DataType, data: Object): void;  差异内容：addData(dataType: DataType, data: Object): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：PickerController；  API声明：deleteData(dataType: DataType, data: Object): void;  差异内容：deleteData(dataType: DataType, data: Object): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增导出符号 | 类名：global；  API声明：export declare class PreselectedInfo  差异内容：NA | 类名：global；  API声明：  差异内容：export declare class PreselectedInfo | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增导出符号 | 类名：global；  API声明：export declare class BadgeConfig  差异内容：NA | 类名：global；  API声明：  差异内容：export declare class BadgeConfig | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增导出符号 | 类名：global；  API声明：export declare enum BadgeType  差异内容：NA | 类名：global；  API声明：  差异内容：export declare enum BadgeType | api/@ohos.file.PhotoPickerComponent.d.ets |
