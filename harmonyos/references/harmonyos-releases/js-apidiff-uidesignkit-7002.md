---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-uidesignkit-7002
title: UI Design Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > UI Design Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:aa5edbd2b6add633164a05a0667995d0ad4cc4e6f41831611342fd347b77e855
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export declare type HdsColorSelectedCallback = (selectedColor: string) => void;  差异内容：export declare type HdsColorSelectedCallback = (selectedColor: string) => void; | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare type HdsFavoritesUpdateCallback = (favoritesList: Array<string>) => void;  差异内容：export declare type HdsFavoritesUpdateCallback = (favoritesList: Array<string>) => void; | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare struct HdsColorPicker  差异内容：export declare struct HdsColorPicker | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsColorPicker；  API声明：@Param  initialColor?: string;  差异内容：@Param  initialColor?: string; | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsColorPicker；  API声明：@Event  onColorSelected: HdsColorSelectedCallback;  差异内容：@Event  onColorSelected: HdsColorSelectedCallback; | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsColorPicker；  API声明：@Param  @Once  initialFavoriteColors?: Array<string>;  差异内容：@Param  @Once  initialFavoriteColors?: Array<string>; | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsColorPicker；  API声明：@Event  onFavoriteColorsUpdate?: HdsFavoritesUpdateCallback;  差异内容：@Event  onFavoriteColorsUpdate?: HdsFavoritesUpdateCallback; | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsColorPicker；  API声明：@Param  options?: HdsColorPickerOptions;  差异内容：@Param  options?: HdsColorPickerOptions; | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum HdsColorPickerTabType  差异内容：export declare enum HdsColorPickerTabType | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsColorPickerTabType；  API声明：GRID = 0  差异内容：GRID = 0 | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsColorPickerTabType；  API声明：SPECTRUM = 1  差异内容：SPECTRUM = 1 | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsColorPickerTabType；  API声明：SLIDERS = 2  差异内容：SLIDERS = 2 | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface HdsColorPickerOptions  差异内容：export interface HdsColorPickerOptions | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsColorPickerOptions；  API声明：circleRadius?: number;  差异内容：circleRadius?: number; | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsColorPickerOptions；  API声明：tabs?: HdsColorPickerTabType[];  差异内容：tabs?: HdsColorPickerTabType[]; | api/@hms.hds.HdsColorPicker.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：onResult(callback: Optional<Callback<ESObject>>): HdsNavDestinationAttribute;  差异内容：onResult(callback: Optional<Callback<ESObject>>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsNavDestinationAttribute；  API声明：onNewParam(callback: Optional<Callback<ESObject>>): HdsNavDestinationAttribute;  差异内容：onNewParam(callback: Optional<Callback<ESObject>>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：CheckOptions；  API声明：radioStyle?: HdsRadioStyle;  差异内容：radioStyle?: HdsRadioStyle; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare interface HdsRadioStyle  差异内容：export declare interface HdsRadioStyle | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsRadioStyle；  API声明：indicatorType?: HdsRadioIndicatorType;  差异内容：indicatorType?: HdsRadioIndicatorType; | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare enum HdsRadioIndicatorType  差异内容：export declare enum HdsRadioIndicatorType | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsRadioIndicatorType；  API声明：TICK = 0  差异内容：TICK = 0 | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：HdsRadioIndicatorType；  API声明：CHECK\_MARK = 100  差异内容：CHECK\_MARK = 100 | api/@hms.hds.hdsBaseComponent.d.ets |
| 新增API | NA | 类名：SnackBarIconOptions；  API声明：iconBuilder?: CustomBuilder;  差异内容：iconBuilder?: CustomBuilder; | api/@hms.hds.HdsSnackBar.d.ets |
| 新增API | NA | 类名：SnackBarIconOptions；  API声明：iconBuilderWidth?: LengthMetrics;  差异内容：iconBuilderWidth?: LengthMetrics; | api/@hms.hds.HdsSnackBar.d.ets |
| 新增API | NA | 类名：SnackBarMessageOptions；  API声明：titleModifier?: TextModifier;  差异内容：titleModifier?: TextModifier; | api/@hms.hds.HdsSnackBar.d.ets |
| 新增API | NA | 类名：SnackBarMessageOptions；  API声明：contentModifier?: TextModifier;  差异内容：contentModifier?: TextModifier; | api/@hms.hds.HdsSnackBar.d.ets |
| 新增API | NA | 类名：SnackBarOperationOptions；  API声明：closeSymbolModifier?: SymbolGlyphModifier;  差异内容：closeSymbolModifier?: SymbolGlyphModifier; | api/@hms.hds.HdsSnackBar.d.ets |
| 新增API | NA | 类名：global；  API声明：export interface HdsListItemStateStylesOptions  差异内容：export interface HdsListItemStateStylesOptions | api/@hms.hds.HdsStyle.d.ets |
| 新增API | NA | 类名：HdsListItemStateStylesOptions；  API声明：selectedBackgroundColor?: ResourceColor;  差异内容：selectedBackgroundColor?: ResourceColor; | api/@hms.hds.HdsStyle.d.ets |
| 新增API | NA | 类名：HdsListItemStateStylesOptions；  API声明：normalBackgroundColor?: ResourceColor;  差异内容：normalBackgroundColor?: ResourceColor; | api/@hms.hds.HdsStyle.d.ets |
| 新增API | NA | 类名：HdsListItem；  API声明：@Prop  listItemStateStyles?: HdsListItemStateStylesOptions;  差异内容：@Prop  listItemStateStyles?: HdsListItemStateStylesOptions; | api/@hms.hds.HdsStyle.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.hds.HdsColorPicker.d.ets  差异内容：UIDesignKit | api/@hms.hds.HdsColorPicker.d.ets |
