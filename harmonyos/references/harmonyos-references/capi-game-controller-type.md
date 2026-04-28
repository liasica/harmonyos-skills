---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller-type
title: game_controller_type.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件和结构体 > 头文件 > game_controller_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:16:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:78d19feeb5a5ae56b93070180260337a8d6f9b30b8d599269e7439a544a3e428
---

## 概述

PhonePC/2in1TabletTV

定义GameController模块的通用枚举类型。

**库：** libohgame\_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：**[GameController](capi-game-controller.md)

## 汇总

PhonePC/2in1TabletTV

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef enum [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) | 此枚举定义游戏控制器的错误码。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) {  GAME\_CONTROLLER\_SUCCESS = 0,  GAME\_CONTROLLER\_PARAM\_ERROR = 401,  GAME\_CONTROLLER\_MULTIMODAL\_INPUT\_ERROR = 32200001,  GAME\_CONTROLLER\_NO\_MEMORY = 32200002  } | 游戏控制器错误码。 |
