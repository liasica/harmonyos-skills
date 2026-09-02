---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accountkit-7001
title: Account Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Account Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:3df6560970c54924d658c84d15b4ab7fee3fbac6b0001e0ba5df307e5f95159b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：AuthenticationController；  API声明：executeRequest(request: AuthenticationRequest, callback: AsyncCallback<AuthenticationResponse, Record<string, Object>>): void;  差异内容：NA | 类名：AuthenticationController；  API声明：executeRequest(request: AuthenticationRequest, callback: AsyncCallback<AuthenticationResponse, Record<string, Object>>): void;  差异内容：12300002 | api/@hms.core.authentication.d.ts |
| 新增错误码 | 类名：AuthenticationController；  API声明：executeRequest(request: AuthenticationRequest): Promise<AuthenticationResponse>;  差异内容：NA | 类名：AuthenticationController；  API声明：executeRequest(request: AuthenticationRequest): Promise<AuthenticationResponse>;  差异内容：12300002 | api/@hms.core.authentication.d.ts |
| 新增API | NA | 类名：ExtraStyle；  API声明：canvasAnimationParams?: CanvasAnimationParams;  差异内容：canvasAnimationParams?: CanvasAnimationParams; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：loginComponentManager；  API声明：export interface CanvasAnimationParams  差异内容：export interface CanvasAnimationParams | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：CanvasAnimationParams；  API声明：canvasRenderingContext: CanvasRenderingContext2D;  差异内容：canvasRenderingContext: CanvasRenderingContext2D; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：CanvasAnimationParams；  API声明：onReady: Callback<void>;  差异内容：onReady: Callback<void>; | api/@hms.core.account.LoginComponent.d.ets |
| 新增API | NA | 类名：LoginWithHuaweiIDButtonController；  API声明：setLocale(locale: string): LoginWithHuaweiIDButtonController;  差异内容：setLocale(locale: string): LoginWithHuaweiIDButtonController; | api/@hms.core.account.LoginComponent.d.ets |
| 新增装饰器 | 类名：LoginPanel；  API声明：params: loginComponentManager.LoginPanelParams;  差异内容：NA | 类名：LoginPanel；  API声明：@Require  params: loginComponentManager.LoginPanelParams;  差异内容：Require | api/@hms.core.account.LoginComponent.d.ets |
| 新增装饰器 | 类名：LoginPanel；  API声明：controller: loginComponentManager.LoginPanelController;  差异内容：NA | 类名：LoginPanel；  API声明：@Require  controller: loginComponentManager.LoginPanelController;  差异内容：Require | api/@hms.core.account.LoginComponent.d.ets |
| 新增装饰器 | 类名：LoginWithHuaweiIDButton；  API声明：params: loginComponentManager.LoginWithHuaweiIDButtonParams;  差异内容：NA | 类名：LoginWithHuaweiIDButton；  API声明：@Require  params: loginComponentManager.LoginWithHuaweiIDButtonParams;  差异内容：Require | api/@hms.core.account.LoginComponent.d.ets |
| 新增装饰器 | 类名：LoginWithHuaweiIDButton；  API声明：controller: loginComponentManager.LoginWithHuaweiIDButtonController;  差异内容：NA | 类名：LoginWithHuaweiIDButton；  API声明：@Require  controller: loginComponentManager.LoginWithHuaweiIDButtonController;  差异内容：Require | api/@hms.core.account.LoginComponent.d.ets |
