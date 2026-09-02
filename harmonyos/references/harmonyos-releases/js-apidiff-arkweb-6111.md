---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-6111
title: ArkWeb
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:7578b353ca2926cd1f8e9f1b5ae2a57776d4d6ddb0e76871524d1038cbb18883
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：WebviewController；  API声明：runJavaScript(script: string): Promise<string>;  差异内容：NA | 类名：WebviewController；  API声明：runJavaScript(script: string): Promise<string>;  差异内容：17100003 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：runJavaScript(script: string, callback: AsyncCallback<string>): void;  差异内容：NA | 类名：WebviewController；  API声明：runJavaScript(script: string, callback: AsyncCallback<string>): void;  差异内容：17100003 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：static setUserAgentClientHintsEnabled(enabled: boolean): void;  差异内容：static setUserAgentClientHintsEnabled(enabled: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：static getUserAgentClientHintsEnabled(): boolean;  差异内容：static getUserAgentClientHintsEnabled(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void;  差异内容：setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：getUserAgentMetadata(userAgent: string): UserAgentMetadata;  差异内容：getUserAgentMetadata(userAgent: string): UserAgentMetadata; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：enum UserAgentFormFactor  差异内容：enum UserAgentFormFactor | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentFormFactor；  API声明：AUTOMOTIVE = 'Automotive'  差异内容：AUTOMOTIVE = 'Automotive' | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentFormFactor；  API声明：DESKTOP = 'Desktop'  差异内容：DESKTOP = 'Desktop' | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentFormFactor；  API声明：MOBILE = 'Mobile'  差异内容：MOBILE = 'Mobile' | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentFormFactor；  API声明：EINK = 'EInk'  差异内容：EINK = 'EInk' | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentFormFactor；  API声明：TABLET = 'Tablet'  差异内容：TABLET = 'Tablet' | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentFormFactor；  API声明：WATCH = 'Watch'  差异内容：WATCH = 'Watch' | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentFormFactor；  API声明：XR = 'XR'  差异内容：XR = 'XR' | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：class UserAgentBrandVersion  差异内容：class UserAgentBrandVersion | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentBrandVersion；  API声明：setBrand(brand: string): void;  差异内容：setBrand(brand: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentBrandVersion；  API声明：getBrand(): string;  差异内容：getBrand(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentBrandVersion；  API声明：setMajorVersion(majorVersion: string): void;  差异内容：setMajorVersion(majorVersion: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentBrandVersion；  API声明：getMajorVersion(): string;  差异内容：getMajorVersion(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentBrandVersion；  API声明：setFullVersion(fullVersion: string): void;  差异内容：setFullVersion(fullVersion: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentBrandVersion；  API声明：getFullVersion(): string;  差异内容：getFullVersion(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：class UserAgentMetadata  差异内容：class UserAgentMetadata | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：setBrandVersionList(brandVersionList: Array<UserAgentBrandVersion>): void;  差异内容：setBrandVersionList(brandVersionList: Array<UserAgentBrandVersion>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：getBrandVersionList(): Array<UserAgentBrandVersion>;  差异内容：getBrandVersionList(): Array<UserAgentBrandVersion>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：setArchitecture(arch: string): void;  差异内容：setArchitecture(arch: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：getArchitecture(): string;  差异内容：getArchitecture(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：setBitness(bitness: string): void;  差异内容：setBitness(bitness: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：getBitness(): string;  差异内容：getBitness(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：setFormFactors(formFactors: Array<UserAgentFormFactor>): void;  差异内容：setFormFactors(formFactors: Array<UserAgentFormFactor>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：getFormFactors(): Array<UserAgentFormFactor>;  差异内容：getFormFactors(): Array<UserAgentFormFactor>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：setFullVersion(fullVersion: string): void;  差异内容：setFullVersion(fullVersion: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：getFullVersion(): string;  差异内容：getFullVersion(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：setMobile(isMobile: boolean): void;  差异内容：setMobile(isMobile: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：getMobile(): boolean;  差异内容：getMobile(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：setModel(model: string): void;  差异内容：setModel(model: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：getModel(): string;  差异内容：getModel(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：setPlatform(platform: string): void;  差异内容：setPlatform(platform: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：getPlatform(): string;  差异内容：getPlatform(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：setPlatformVersion(platformVersion: string): void;  差异内容：setPlatformVersion(platformVersion: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：getPlatformVersion(): string;  差异内容：getPlatformVersion(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：setWow64(isWow64: boolean): void;  差异内容：setWow64(isWow64: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：UserAgentMetadata；  API声明：getWow64(): boolean;  差异内容：getWow64(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebContextMenuResult；  API声明：saveImage(): void;  差异内容：saveImage(): void; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：enableDefaultContextMenu(enable: boolean): WebAttribute;  差异内容：enableDefaultContextMenu(enable: boolean): WebAttribute; | component/web.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WebviewController；  API声明：refresh(): void;  差异内容：refresh(): void; | 类名：WebviewController；  API声明：refresh(ignoreCache: boolean): void;  差异内容：refresh(ignoreCache: boolean): void; | api/@ohos.web.webview.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WebviewController；  API声明：setUrlTrustList(urlTrustList: string): void;  差异内容：setUrlTrustList(urlTrustList: string): void; | 类名：WebviewController；  API声明：setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void;  差异内容：setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void; | api/@ohos.web.webview.d.ts |
