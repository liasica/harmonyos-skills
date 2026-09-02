---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller-type-h
title: game_controller_type.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件 > game_controller_type.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:679cbcc62c25aa5b879da0ce2d3008936a23b8a83649ed9eade05e28499509a3
---

## 概述

定义GameController模块的通用枚举类型。

**引用文件：** <GameControllerKit/game\_controller\_type.h>

**库：** libohgame\_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：** [GameController](capi-gamecontroller.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | GameController\_ErrorCode | 此枚举定义游戏控制器的错误码。 |

## 枚举类型说明

### GameController\_ErrorCode

```c
enum GameController_ErrorCode
```

**描述**

此枚举定义游戏控制器的错误码。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| GAME\_CONTROLLER\_SUCCESS = 0 | 成功。  **起始版本：** 21 |
| GAME\_CONTROLLER\_PARAM\_ERROR = 401 | 参数非法。  **起始版本：** 21 |
| GAME\_CONTROLLER\_MULTIMODAL\_INPUT\_ERROR = 32200001 | 查询多模输入中所有设备信息失败。  **起始版本：** 21 |
| GAME\_CONTROLLER\_NO\_MEMORY = 32200002 | 设备内存不足。  **起始版本：** 21 |
