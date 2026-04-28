---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accountkit-b035
title: Account Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > Account Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:dfe731d3d9c340742ae9d5d4d6c0f1662ec551fa18e79374a1167097b96a93e6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：LoginPanelController；  API声明：onClickLoginWithHuaweiIDButton(callback: AsyncCallback<HuaweiIDCredential>): LoginPanelController;  差异内容：NA | 类名：LoginPanelController；  API声明：onClickLoginWithHuaweiIDButton(callback: AsyncCallback<HuaweiIDCredential>): LoginPanelController;  差异内容：1001500001,1001500002,1001500003,1001502001,1001502002,1001502003,1001502005,1001502009,1001502012,1001502014,1005300001,12300001,401 | api/@hms.core.account.LoginComponent.d.ets |
| 错误码变更 | 类名：LoginWithHuaweiIDButtonController；  API声明：onClickLoginWithHuaweiIDButton(callback: AsyncCallback<HuaweiIDCredential>): LoginWithHuaweiIDButtonController;  差异内容：NA | 类名：LoginWithHuaweiIDButtonController；  API声明：onClickLoginWithHuaweiIDButton(callback: AsyncCallback<HuaweiIDCredential>): LoginWithHuaweiIDButtonController;  差异内容：1001500001,1001500002,1001500003,1001502001,1001502002,1001502003,1001502005,1001502009,1001502012,1001502014,1005300001,12300001,401 | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明： export interface StateStyles  差异内容： export interface StateStyles | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：StateStyles；  API声明：normal?: ButtonStyle;  差异内容：normal?: ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：StateStyles；  API声明：pressed?: ButtonStyle;  差异内容：pressed?: ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：StateStyles；  API声明：disabled?: ButtonStyle;  差异内容：disabled?: ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：StateStyles；  API声明：focused?: ButtonStyle;  差异内容：focused?: ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：LoginWithHuaweiIDButtonParams；  API声明：extraStyle?: ExtraStyle;  差异内容：extraStyle?: ExtraStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明： export class ButtonStyle  差异内容： export class ButtonStyle | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：buttonSize(value: ButtonSize): ButtonStyle;  差异内容：buttonSize(value: ButtonSize): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：fontSize(value: Length): ButtonStyle;  差异内容：fontSize(value: Length): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：fontColor(value: ResourceColor | FontColor): ButtonStyle;  差异内容：fontColor(value: ResourceColor | FontColor): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：fontWeight(value: string | number | FontWeight): ButtonStyle;  差异内容：fontWeight(value: string | number | FontWeight): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：fontFamily(value: ResourceStr): ButtonStyle;  差异内容：fontFamily(value: ResourceStr): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：backgroundColor(value: ResourceColor): ButtonStyle;  差异内容：backgroundColor(value: ResourceColor): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：backgroundEffect(value: BackgroundEffectOptions): ButtonStyle;  差异内容：backgroundEffect(value: BackgroundEffectOptions): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：backgroundBrightness(value: BackgroundBrightnessOptions): ButtonStyle;  差异内容：backgroundBrightness(value: BackgroundBrightnessOptions): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：linearGradient(value: LinearGradient): ButtonStyle;  差异内容：linearGradient(value: LinearGradient): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：sweepGradient(value: SweepGradient): ButtonStyle;  差异内容：sweepGradient(value: SweepGradient): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：radialGradient(value: RadialGradient): ButtonStyle;  差异内容：radialGradient(value: RadialGradient): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：shadow(value: ShadowOptions | ShadowStyle): ButtonStyle;  差异内容：shadow(value: ShadowOptions | ShadowStyle): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：opacity(value: number | Resource): ButtonStyle;  差异内容：opacity(value: number | Resource): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：border(value: BorderOptions): ButtonStyle;  差异内容：border(value: BorderOptions): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：borderImage(value: BorderImageOption): ButtonStyle;  差异内容：borderImage(value: BorderImageOption): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：outline(value: OutlineOptions): ButtonStyle;  差异内容：outline(value: OutlineOptions): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：hoverEffect(value: HoverEffect): ButtonStyle;  差异内容：hoverEffect(value: HoverEffect): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：clickEffect(value: ClickEffect): ButtonStyle;  差异内容：clickEffect(value: ClickEffect): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonStyle；  API声明：loadingStyle(value: LoadingStyle): ButtonStyle;  差异内容：loadingStyle(value: LoadingStyle): ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明： export interface SweepGradient  差异内容： export interface SweepGradient | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：SweepGradient；  API声明：center: [  Length,  Length  ];  差异内容：center: [  Length,  Length  ]; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：SweepGradient；  API声明：start?: number | string;  差异内容：start?: number | string; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：SweepGradient；  API声明：end?: number | string;  差异内容：end?: number | string; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：SweepGradient；  API声明：rotation?: number | string;  差异内容：rotation?: number | string; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：SweepGradient；  API声明：colors: Array<[  ResourceColor,  number  ]>;  差异内容：colors: Array<[  ResourceColor,  number  ]>; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：SweepGradient；  API声明：repeating?: boolean;  差异内容：repeating?: boolean; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明： export interface RadialGradient  差异内容： export interface RadialGradient | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：RadialGradient；  API声明：center: [  Length,  Length  ];  差异内容：center: [  Length,  Length  ]; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：RadialGradient；  API声明：radius: number | string;  差异内容：radius: number | string; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：RadialGradient；  API声明：colors: Array<[  ResourceColor,  number  ]>;  差异内容：colors: Array<[  ResourceColor,  number  ]>; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：RadialGradient；  API声明：repeating?: boolean;  差异内容：repeating?: boolean; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明： export interface ExtraStyle  差异内容： export interface ExtraStyle | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ExtraStyle；  API声明：buttonStyle?: ButtonStyle;  差异内容：buttonStyle?: ButtonStyle; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ExtraStyle；  API声明：customButtonStateStyles?: StateStyles;  差异内容：customButtonStateStyles?: StateStyles; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ExtraStyle；  API声明：textAndIconButtonParams?: TextAndIconButtonParams;  差异内容：textAndIconButtonParams?: TextAndIconButtonParams; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ExtraStyle；  API声明：iconButtonParams?: IconButtonParams;  差异内容：iconButtonParams?: IconButtonParams; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明： export interface LoadingStyle  差异内容： export interface LoadingStyle | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：LoadingStyle；  API声明：show?: boolean;  差异内容：show?: boolean; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明： export interface IconButtonParams  差异内容： export interface IconButtonParams | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：IconButtonParams；  API声明：logoRadius?: number;  差异内容：logoRadius?: number; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明： export interface TextAndIconButtonParams  差异内容： export interface TextAndIconButtonParams | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：TextAndIconButtonParams；  API声明：textAndIconMargin?: number;  差异内容：textAndIconMargin?: number; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明： export interface ButtonSize  差异内容： export interface ButtonSize | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonSize；  API声明：width?: Length;  差异内容：width?: Length; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：ButtonSize；  API声明：height?: Length;  差异内容：height?: Length; | api/@hms.core.account.LoginComponent.d.ets |
