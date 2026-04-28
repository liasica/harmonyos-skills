---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scenariofusionkit-510
title: Scenario Fusion Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Scenario Fusion Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:500518c4548e9585910f1ffa2c9db5586cebf3025407d4afb01bb83b7d52f635
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export declare struct FunctionalInput  差异内容：export declare struct FunctionalInput | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：FunctionalInput；  API声明：@Prop  params: functionalInputComponentManager.FunctionalInputParams;  差异内容：@Prop  params: functionalInputComponentManager.FunctionalInputParams; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：FunctionalInput；  API声明：controller: functionalInputComponentManager.FunctionalInputController;  差异内容：controller: functionalInputComponentManager.FunctionalInputController; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：FunctionalInput；  API声明：build(): void;  差异内容：build(): void; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare namespace functionalInputComponentManager  差异内容：export declare namespace functionalInputComponentManager | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：functionalInputComponentManager；  API声明：export enum InputType  差异内容：export enum InputType | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：InputType；  API声明：SELECT\_DISTRICT = 0  差异内容：SELECT\_DISTRICT = 0 | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：functionalInputComponentManager；  API声明：export interface FunctionalInputParams  差异内容：export interface FunctionalInputParams | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：FunctionalInputParams；  API声明：inputType: InputType;  差异内容：inputType: InputType; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：FunctionalInputParams；  API声明：textInputValue: TextInputOptions;  差异内容：textInputValue: TextInputOptions; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：FunctionalInputParams；  API声明：inputAttributeModifier?: TextInputModifier;  差异内容：inputAttributeModifier?: TextInputModifier; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：FunctionalInputParams；  API声明：icon?: Resource;  差异内容：icon?: Resource; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：FunctionalInputParams；  API声明：iconImgModifier?: ImageModifier;  差异内容：iconImgModifier?: ImageModifier; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：FunctionalInputParams；  API声明：iconSymbolModifier?: SymbolGlyphModifier;  差异内容：iconSymbolModifier?: SymbolGlyphModifier; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：functionalInputComponentManager；  API声明：export interface DistrictSelectResult  差异内容：export interface DistrictSelectResult | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：DistrictSelectResult；  API声明：inputContent: string;  差异内容：inputContent: string; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：DistrictSelectResult；  API声明：districtSelectResult: sceneMap.DistrictSelectResult;  差异内容：districtSelectResult: sceneMap.DistrictSelectResult; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：functionalInputComponentManager；  API声明：export class FunctionalInputController  差异内容：export class FunctionalInputController | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增API | NA | 类名：FunctionalInputController；  API声明：onSelectDistrict(callback: AsyncCallback<DistrictSelectResult>): FunctionalInputController;  差异内容：onSelectDistrict(callback: AsyncCallback<DistrictSelectResult>): FunctionalInputController; | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.core.atomicserviceComponent.atomicserviceInput.d.ets  差异内容：ScenarioFusionKit | api/@hms.core.atomicserviceComponent.atomicserviceInput.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：FunctionalButtonParams；  API声明：buttonModifier?: ButtonModifier;  差异内容：buttonModifier?: ButtonModifier; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：FunctionalButtonParams；  API声明：textModifier?: TextModifier;  差异内容：textModifier?: TextModifier; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：FunctionalButtonParams；  API声明：loadingProgressModifier?: LoadingProgressModifier;  差异内容：loadingProgressModifier?: LoadingProgressModifier; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
