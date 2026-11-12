---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-keep-alive-c
title: 设置游戏实况窗后台保活（C/C++）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导（C/C++） > 设置游戏实况窗后台保活（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:24+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5b377ad297defb141a72e16945ce9fd42e1f41b68a54b63d25dfb7d313753b78
---

从API版本26.0.0开始，游戏场景感知服务支持实况窗后台保活能力；从API版本26.0.1开始，游戏场景感知实况窗后台保活能力支持本地调试。当游戏切换到后台时，游戏继续运行并上报当前游戏场景信息，通过对应场景ID配置的实况窗内容展示当前游戏状态。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/ejOfgv7gSiSzaJ3S9xnlXA/zh-cn_image_0000002786360300.png)

1. 游戏启动后调用[HMS\_GamePerformance\_Init()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_init)接口对游戏场景感知进行初始化。
2. 初始化成功后，游戏调用[HMS\_GamePerformance\_UpdateSceneInfo()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatesceneinfo)接口向游戏场景感知上报游戏场景信息。
3. 游戏切换到后台时根据上报的游戏场景ID展示对应实况窗保活模板。

## 接口说明

具体API说明详见[GamePerformance](../harmonyos-references/gameservice-game-performance.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_GamePerformance\_Init()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_init) | 游戏初始化接口，对游戏场景感知进行初始化。 |
| [HMS\_GamePerformance\_UpdateSceneInfo()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatesceneinfo) | 更新游戏场景信息接口，用于上报游戏场景信息。 |

## 接入步骤

### 在 CMake 脚本中链接动态库

```c
target_include_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/include)
target_link_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos)
target_link_libraries(entry PUBLIC libgame_performance.z.so)
```

### 导入模块

导入Game Service Kit。

```c
#include <GameServiceKit/game_performance.h>
#include <cstdlib>
```

### 初始化游戏场景感知服务

导入相关模块后，需先调用[HMS\_GamePerformance\_Init()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_init)接口对游戏场景感知进行初始化。如果未初始化或初始化失败，将无法调用其他接口。

```c
// 创建初始化参数
GamePerformance_InitParameters *initParameters = NULL;
HMS_GamePerformance_CreateInitParameters(&initParameters);

// 设置参数，所有SetXXX接口的第二个参数均为示例，请替换成实际参数
GamePerformance_ErrorCode appVersionSetCode =
    HMS_GamePerformance_InitParameters_SetAppVersion(initParameters, "1.0");

// 所有SetXXX接口，如果参数设置错误，将会返回错误码401；为确保参数设置无误，建议接收返回值并判断错误码
if (appVersionSetCode != GAME_PERFORMANCE_SUCCESS) {
    // 异常处理
}
HMS_GamePerformance_InitParameters_SetBundleName(initParameters, "com.example.demo");

// 初始化
GamePerformance_ErrorCode ret = HMS_GamePerformance_Init(initParameters);
if (ret != GAME_PERFORMANCE_SUCCESS) {
    // 异常处理
}

// 使用完释放内存
HMS_GamePerformance_DestroyInitParameters(&initParameters);
```

### 上报游戏场景信息

初始化成功后，可以通过调用[HMS\_GamePerformance\_UpdateSceneInfo()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatesceneinfo)接口上报游戏场景信息。当游戏切换至后台时，游戏场景感知服务将根据上报的场景ID展示对应ID下配置的实况窗内容，实况窗配置内容请参考[实况窗配置模板](gameservice-gameperformance-keep-alive-c.md#实况窗配置模板)。

```c
// HMS_GamePerformance_SceneInfo_SetXXX接口的第二个参数均为示例，请替换成实际参数
GamePerformance_SceneInfo *sceneInfo = NULL;
HMS_GamePerformance_CreateSceneInfo(&sceneInfo);

// 如需多次上报，若使用同一个实例上报，只需通过set方法更新参数即可（同一个实例将保留上一次设置的数据）
// 设置必选字段
HMS_GamePerformance_SceneInfo_SetSceneID(sceneInfo, 1);
HMS_GamePerformance_SceneInfo_SetImportanceLevel(sceneInfo, GAME_PERFORMANCE_SIL_LEVEL1);

// 按需设置下列可选字段
HMS_GamePerformance_SceneInfo_SetDescription(sceneInfo, "this is description of scene");
HMS_GamePerformance_SceneInfo_SetSubSceneID(sceneInfo, "20101020304");
HMS_GamePerformance_SceneInfo_SetSubDescription(sceneInfo, "this is description of subScene");
HMS_GamePerformance_SceneInfo_SetSceneFrequency(sceneInfo, 2);
HMS_GamePerformance_SceneInfo_SetSceneTime(sceneInfo, 15);
HMS_GamePerformance_SceneInfo_SetRecommendedCpuLevel(sceneInfo, GAME_PERFORMANCE_CPU_LEVEL_HIGH);
HMS_GamePerformance_SceneInfo_SetRecommendedGpuLevel(sceneInfo, GAME_PERFORMANCE_GPU_LEVEL_HIGH);
HMS_GamePerformance_SceneInfo_SetRecommendedDdrLevel(sceneInfo, GAME_PERFORMANCE_DDR_LEVEL_HIGH);
HMS_GamePerformance_SceneInfo_SetKeyThread(sceneInfo, "render");
HMS_GamePerformance_SceneInfo_SetDrawCallCount(sceneInfo, 100);
HMS_GamePerformance_SceneInfo_SetVertexCount(sceneInfo, 100);
HMS_GamePerformance_SceneInfo_SetTriangleCount(sceneInfo, 100);
HMS_GamePerformance_SceneInfo_SetShaderCount(sceneInfo, 100);
HMS_GamePerformance_SceneInfo_SetTextureCount(sceneInfo, 100);
HMS_GamePerformance_SceneInfo_SetMeshCount(sceneInfo, 100);
HMS_GamePerformance_SceneInfo_SetChannelCount(sceneInfo, 100);
HMS_GamePerformance_SceneInfo_SetParticipantCount(sceneInfo, 5);

// 上报游戏场景信息
GamePerformance_ErrorCode ret = HMS_GamePerformance_UpdateSceneInfo(sceneInfo);
if (ret != GAME_PERFORMANCE_SUCCESS) {
    // 异常处理
}

// 使用完释放内存
HMS_GamePerformance_DestroySceneInfo(&sceneInfo);
```

## 本地调试

游戏场景感知服务接入[hidumper](hidumper.md)，支持通过hidumper命令设置本地保活模板，方便开发进行本地调试。游戏场景同时存在本地模板和云侧模板时，将优先使用本地模板的样式展示实况窗，当游戏服务重启后，本地模板将自动清除。

本地调试时所使用的hidumper命令基本格式如下：

```shell
hdc shell hidumper -s 66006 -a "<命令参数>"
```

**说明** 

“-a”后的命令参数需要用引号包裹。

本地调试步骤如下：

1. 在设备的“/data/local/tmp/”目录下准备一个JSON配置文件，使用本地保活配置时会读取该文件。文件所需的内容如下所示，更多场景配置模板请参见[实况窗配置模板](gameservice-gameperformance-keep-alive-c.md#实况窗配置模板)。

   ```json
    [
      {
        "enterSceneId": 1,
        "templateId": 0,
        "maxKeepAliveTime": 300,
        "enterTitle": {"zh": "游戏运行中", "en": "Game Running"},
        "enterDesc": {"zh": "正在%key1%", "en": "%key1% in progress"},
        "exitTitle": {"zh": "游戏已退出", "en": "Game Exited"},
        "exitDesc": {"zh": "已退出游戏", "en": "Game exited"},
        "exitExtendData": {"zh": "扩展数据", "en": "Extend data"},
        "isAlarmOnExit": false
      }
    ]
   ```

   | 字段名称 | 类型 | 可选 | 说明 |
   | --- | --- | --- | --- |
   | enterSceneId | int64 | 否 | 进入场景的场景ID。 |
   | templateId | int32 | 否 | 使用的实况窗模板类型，取值如下：  0：普通实况窗，场景切换更新时自动停止，依靠游戏上报更新进行场景内容更新，可用于游戏匹配场景。  1：倒计时实况窗，场景切换或倒计时结束时自动停止，倒计时由系统更新，可用于角色复活倒计时场景。  2：正计时实况窗，场景切换时自动停止，计时由系统更新，可用于游戏匹配场景。  3：进度实况窗，进度为从0到100，到达100或场景切换时自动停止，可用于游戏资源更新场景。 |
   | maxKeepAliveTime | int32 | 否 | 最大保活时间，单位：min。 |
   | enterTitle | map | 否 | 进入场景的实况窗标题，以key:value的格式传入，其中key为语言代码，如“zh”、“en”等。 |
   | enterDesc | map | 是 | 进入场景的实况窗内容，以key:value的格式传入，其中key为语言代码，如“zh”、“en”等。 |
   | exitTitle | map | 否 | 退出场景的实况窗标题，以key:value的格式传入，其中key为语言代码，如“zh”、“en”等。 |
   | exitDesc | map | 是 | 退出场景的实况窗内容，以key:value的格式传入，其中key为语言代码，如“zh”、“en”等。 |
   | exitExtendData | map | 是 | 退出场景的辅助区内容，以key:value的格式传入，其中key为语言代码，如“zh”、“en”等。 |
   | isAlarmOnExit | boolean | 否 | 游戏退出场景时是否提醒玩家，取值如下：  - true：提醒。  - false：不提醒。 |
2. 将本地设置的JSON配置文件推送到设备。

   ```shell
   hdc file send config.json /data/local/tmp/config.json
   ```
3. 使能本地保活模板，将使用的配置从云侧配置切换为本地配置。

   ```shell
   hdc shell hidumper -s 66006 -a "-se keepLiveTemplate <bundleName> -f <fileName>"
   ```

   使用样例如下：

   ```shell
   # 使能com.game.test的本地保活模板，配置文件为config.json
   hdc shell hidumper -s 66006 -a "-se keepLiveTemplate com.game.test -f config.json"
   ```

   返回结果说明如下：

   | 结果 | 说明 |
   | --- | --- |
   | Enable local template success for com.game.test | 本地保活模板使能成功。 |
   | bundleName invalid | bundleName格式不合法。 |
   | fileName invalid | 文件名含“/”、“\”和“..”，不合法。 |
   | Failed to read or parse config file | 本地保活模板文件不存在或JSON格式错误。 |

   **说明** 

   * 配置文件大小不能超过512KB。
   * 使能后会优先使用本地配置，去使能后将恢复使用云侧配置。
   * 使能操作会覆盖同一包名的已有本地配置。
4. 将游戏切到后台，通过观察设备上是否展示对应场景的实况窗以确认保活是否生效。
5. 您可以选择将当前包内生效的保活模板导出到指定的JSON文件内用于检查。

   ```shell
   hdc shell hidumper -s 66006 -a "-xp keepLiveTemplate <bundleName> -f <fileName>"
   ```

   使用样例如下：

   ```shell
   # 导出com.game.test内当前生效的保活模板到output.json
   hdc shell hidumper -s 66006 -a "-xp keepLiveTemplate com.game.test -f output.json"
   ```

   返回结果说明如下：

   | 结果 | 说明 |
   | --- | --- |
   | Export keepalive template success to /data/local/tmp/output.json | 保活模板导出成功。 |
   | bundleName invalid | bundleName格式不合法。 |
   | fileName invalid | 文件名含路径分隔符或“..”，不合法。 |
   | No effective keepalive template for com.game.test | 本地配置和DB数据库缓存均无该包名的有效配置。 |
   | File already exists: /data/local/tmp/output.json | 目标文件已存在，防止覆盖。 |

   保活模板导出成功后，您还可以使用以下命令将导出后的JSON文件拉取到本地。

   ```shell
   hdc file recv /data/local/tmp/output.json ./output.json
   ```
6. 如果本地保活模板有更新，您可以选择将导出后的本地保活模板配置刷新到云侧。

   ```shell
   hdc shell hidumper -s 66006 -a "-sr keepLiveTemplate <bundleName>"
   ```

   使用样例如下：

   ```shell
   # 刷新com.game.test的云侧保活配置
   hdc shell hidumper -s 66006 -a "-sr keepLiveTemplate com.game.test"
   ```

   返回结果说明如下：

   | 结果 | 说明 |
   | --- | --- |
   | Refresh cloud config success | 云侧保活配置刷新成功 |
   | bundleName invalid | bundleName格式不合法。 |
   | Operation too frequent, please try again later | 1分钟内重复操作，请延长等待时间后再次尝试。 |
   | Refresh cloud config failed for com.game.test | 云侧刷新请求失败。 |
   | Refresh cloud config failed for com.game.test: no local config and cloud request failed | 云侧没有当前游戏的保活配置。 |

   **说明** 

   * 刷新操作限制的时间间隔为1分钟，频繁操作会返回限频提示。
   * 刷新的保活配置为云侧配置，若存在本地模板，依旧优先使用本地模板。
   * 如果需要使用刷新后的云侧配置，需要先去使能本地模板。
7. 调试完毕，去使能本地模板，恢复使用云侧配置。

   ```shell
   hdc shell hidumper -s 66006 -a "-sd keepLiveTemplate <bundleName>"
   ```

   使用样例如下：

   ```shell
   # 去使能com.game.test的本地保活模板，恢复使用云侧配置
   hdc shell hidumper -s 66006 -a "-sd keepLiveTemplate com.game.test"
   ```

   返回结果说明如下：

   | 结果 | 说明 |
   | --- | --- |
   | Disable local template success for com.game.test | 去使能成功。 |
   | bundleName invalid | bundleName格式不合法。 |
   | No local template found for com.game.test | 该包名无本地配置。 |

## 实况窗配置模板

### 游戏匹配

```json
{
  "enterDesc": {
    "en": "%key1% finding a match ...",
    "zh": "%key1%开始匹配，请稍后..."
  },
  "enterSceneId": "0",
  "enterTitle": {
    "en": "Matching",
    "zh": "正在匹配中"
  },
  "exitDesc": {
    "en": "Match complete",
    "zh": "匹配完成"
  },
  "exitTitle": {
    "en": "Match complete",
    "zh": "已匹配到玩家"
  },
  "isAlarmOnExit": true,
  "keys": [
    "key1"
  ],
  "exitExtendData": {
    "en": "",
    "zh": ""
  },
  "maxKeepAliveTime": 30,
  "templateId": 0
}
```

### 复活倒计时

```json
{
  "enterDesc": {
    "zh": "%39%"
  },
  "enterSceneId": "7",
  "enterTitle": {
    "zh": "复活中"
  },
  "exitTitle": {
    "zh": "已复活"
  },
  "isAlarmOnExit": true,
  "keys": [
    "39"
  ],
  "exitExtendData": {
    "zh": "返回游戏"
  },
  "maxKeepAliveTime": 30,
  "templateId": 1
}
```

### 游戏进行中

```json
{
  "enterDesc": {
    "en": "%key1% in game1...",
    "zh": "%key1%正在对局中，请继续..."
  },
  "enterSceneId": "3",
  "enterTitle": {
    "en": "In game",
    "zh": "正在对局中"
  },
  "exitDesc": {
    "en": "game over",
    "zh": "对局结束"
  },
  "exitTitle": {
    "en": "Game over",
    "zh": "退出对局"
  },
  "isAlarmOnExit": false,
  "keys": [
    "key1"
  ],
  "maxKeepAliveTime": 1,
  "templateId": 2
}
```

### 资源更新

```json
{
  "enterDesc": {
    "en": "%key1% downloading...",
    "zh": "%key1%正在下载中，请稍后..."
  },
  "enterSceneId": "4",
  "enterTitle": {
    "en": "Downloading",
    "zh": "资源下载中"
  },
  "exitDesc": {
    "en": "download complete",
    "zh": "资源已下载完成，可打开游戏"
  },
  "exitTitle": {
    "en": "Download complete",
    "zh": "资源下载完成"
  },
  "isAlarmOnExit": true,
  "keys": [
    "key1"
  ],
  "maxKeepAliveTime": 30,
  "templateId": 3
}
```
