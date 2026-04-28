---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-gameservicekit-b031
title: Game Service Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Game Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:39+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a7005764877ca42f08c1cf7fb479832b23ee41d3a8ffbba98ab78d747d2c069f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：gamePlayer；  API声明：function getLocalPlayer(context: common.UIAbilityContext): Promise<GSKLocalPlayer>;  差异内容：1002000001,1002000002,1002000003,1002000004,1002000005,1002000006,1002000011,1002000014,401 | 类名：gamePlayer；  API声明：function getLocalPlayer(context: common.UIAbilityContext): Promise<GSKLocalPlayer>;  差异内容：1002000001,1002000002,1002000003,1002000004,1002000005,1002000006,1002000011,1002000014,1002000017,401 | api/@hms.core.gameservice.gameplayer.d.ts |
| 错误码变更 | 类名：gamePlayer；  API声明：function getLocalPlayer(context: common.UIAbilityContext, callback: AsyncCallback<GSKLocalPlayer>): void;  差异内容：1002000001,1002000002,1002000003,1002000004,1002000005,1002000006,1002000011,1002000014,401 | 类名：gamePlayer；  API声明：function getLocalPlayer(context: common.UIAbilityContext, callback: AsyncCallback<GSKLocalPlayer>): void;  差异内容：1002000001,1002000002,1002000003,1002000004,1002000005,1002000006,1002000011,1002000014,1002000017,401 | api/@hms.core.gameservice.gameplayer.d.ts |
| 错误码变更 | 类名：gamePlayer；  API声明：function bindPlayer(context: common.UIAbilityContext, thirdOpenId: string, teamPlayerId: string): Promise<void>;  差异内容：1002000001,1002000002,1002000003,1002000005,1002000010,1002000011,1002000012,401 | 类名：gamePlayer；  API声明：function bindPlayer(context: common.UIAbilityContext, thirdOpenId: string, teamPlayerId: string): Promise<void>;  差异内容：1002000001,1002000002,1002000003,1002000005,1002000010,1002000011,1002000012,1002000017,401 | api/@hms.core.gameservice.gameplayer.d.ts |
| 错误码变更 | 类名：gamePlayer；  API声明：function unbindPlayer(context: common.UIAbilityContext, thirdOpenId: string, teamPlayerId: string): Promise<void>;  差异内容：1002000001,1002000002,1002000003,1002000005,1002000010,1002000011,1002000013,401 | 类名：gamePlayer；  API声明：function unbindPlayer(context: common.UIAbilityContext, thirdOpenId: string, teamPlayerId: string): Promise<void>;  差异内容：1002000001,1002000002,1002000003,1002000005,1002000010,1002000011,1002000013,1002000017,401 | api/@hms.core.gameservice.gameplayer.d.ts |
| 错误码变更 | 类名：gamePlayer；  API声明：function verifyLocalPlayer(context: common.UIAbilityContext, thirdUserInfo: ThirdUserInfo): Promise<void>;  差异内容：1002000001,1002000002,1002000003,1002000004,1002000005,1002000006,1002000008,1002000011,1002000015,401 | 类名：gamePlayer；  API声明：function verifyLocalPlayer(context: common.UIAbilityContext, thirdUserInfo: ThirdUserInfo): Promise<void>;  差异内容：1002000001,1002000002,1002000003,1002000004,1002000005,1002000006,1002000008,1002000011,1002000015,1002000017,401 | api/@hms.core.gameservice.gameplayer.d.ts |
| 错误码变更 | 类名：gamePlayer；  API声明：function unionLogin(context: common.UIAbilityContext, loginParam: UnionLoginParam): Promise<UnionLoginResult>;  差异内容：1002000001,1002000002,1002000003,1002000004,1002000005,1002000008,1002000011,1002000014,1002000016,401 | 类名：gamePlayer；  API声明：function unionLogin(context: common.UIAbilityContext, loginParam: UnionLoginParam): Promise<UnionLoginResult>;  差异内容：1002000001,1002000002,1002000003,1002000004,1002000005,1002000008,1002000011,1002000014,1002000016,1002000017,401 | api/@hms.core.gameservice.gameplayer.d.ts |
| 新增API | NA | 类名：GameErrorCode；  API声明：ILLEGAL\_APPLICATION = 1002000017  差异内容：ILLEGAL\_APPLICATION = 1002000017 | api/@hms.core.gameservice.gameplayer.d.ts |
