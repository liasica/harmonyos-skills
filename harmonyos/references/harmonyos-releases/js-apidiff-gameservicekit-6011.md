---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-gameservicekit-6011
title: Game Service Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Game Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:59+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:bdf43e5d889a9fd458bc83b6c173dd224d5e38f8b7c5c1e48a299039009bb0cf
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：GameErrorCode；  API声明：NOT\_MINI\_GAME\_ERROR = 1002000018  差异内容：NOT\_MINI\_GAME\_ERROR = 1002000018 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode；  API声明：PARAM\_ERROR = 1002000019  差异内容：PARAM\_ERROR = 1002000019 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode；  API声明：USER\_CANCELED = 1002000020  差异内容：USER\_CANCELED = 1002000020 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode；  API声明：CALLS\_FREQUENT = 1002000021  差异内容：CALLS\_FREQUENT = 1002000021 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode；  API声明：PAY\_PRODUCT\_INVALID = 1002000050  差异内容：PAY\_PRODUCT\_INVALID = 1002000050 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode；  API声明：PAY\_PRODUCT\_OWNED = 1002000051  差异内容：PAY\_PRODUCT\_OWNED = 1002000051 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode；  API声明：PAY\_PRODUCT\_NOT\_OWNED = 1002000052  差异内容：PAY\_PRODUCT\_NOT\_OWNED = 1002000052 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode；  API声明：PAY\_PRODUCT\_CONSUMED = 1002000053  差异内容：PAY\_PRODUCT\_CONSUMED = 1002000053 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode；  API声明：PAY\_ACCOUNT\_REGION\_UNSUPPORTED = 1002000054  差异内容：PAY\_ACCOUNT\_REGION\_UNSUPPORTED = 1002000054 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode；  API声明：PAY\_DEAL\_REJECTED = 1002000056  差异内容：PAY\_DEAL\_REJECTED = 1002000056 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer；  API声明：interface MiniGameLoginParam  差异内容：interface MiniGameLoginParam | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGameLoginParam；  API声明：gameAppId: string;  差异内容：gameAppId: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGameLoginParam；  API声明：extraData?: string;  差异内容：extraData?: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer；  API声明：interface MiniGamePlayer  差异内容：interface MiniGamePlayer | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer；  API声明：playerId: string;  差异内容：playerId: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer；  API声明：playerLevel: number;  差异内容：playerLevel: number; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer；  API声明：playerSign: string;  差异内容：playerSign: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer；  API声明：signTs: string;  差异内容：signTs: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer；  API声明：isAdult: boolean;  差异内容：isAdult: boolean; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：MiniGamePlayer；  API声明：extraData?: string;  差异内容：extraData?: string; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer；  API声明：function miniGameLogin(context: common.Context, loginParam: MiniGameLoginParam): Promise<MiniGamePlayer>;  差异内容：function miniGameLogin(context: common.Context, loginParam: MiniGameLoginParam): Promise<MiniGamePlayer>; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer；  API声明：function miniGamePay(context: common.Context, parameter: PurchaseParameter): Promise<CreatePurchaseResult>;  差异内容：function miniGamePay(context: common.Context, parameter: PurchaseParameter): Promise<CreatePurchaseResult>; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer；  API声明：function on(type: 'miniGameAddictionPrevented', callback: Callback<string>): void;  差异内容：function on(type: 'miniGameAddictionPrevented', callback: Callback<string>): void; | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：gamePlayer；  API声明：function off(type: 'miniGameAddictionPrevented', callback?: Callback<string>): void;  差异内容：function off(type: 'miniGameAddictionPrevented', callback?: Callback<string>): void; | api/@hms.core.gameservice.gameplayer.d.ts |
