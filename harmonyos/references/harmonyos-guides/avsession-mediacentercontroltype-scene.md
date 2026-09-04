---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-mediacentercontroltype-scene
title: 自定义播控中心控制按钮显示布局
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 自定义播控中心控制按钮显示布局
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:26fc8340dd329def4737050d3343c29d4424c5563eb277045acbd5af6731a6bb
---

从API版本26.0.0开始，系统支持自定义播控中心控制按钮的显示布局。本文档介绍播控中心控制按钮的默认显示规则，以及应用如何自定义控制按钮的显示。

## 基本概念

播控中心常见的控制按钮类型有：播放/暂停、上一首、下一首、快进、快退等。不同的播控页面会显示不同的控制按钮布局，目前主要有以下两种布局方式：

* **五元组**：显示五个控制按钮，如播控中心二级界面会使用五元组进行显示。如下图所示，五元组从左到右显示的位置分别称为4号位、2号位、1号位、3号位、5号位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/uX1BuW5GQfGA8-aAcv3Mkg/zh-cn_image_0000002712244766.png)

* **三元组**：显示三个控制按钮，如播控中心一级界面会使用三元组进行显示。如下图所示，三元组从左到右显示的位置分别称为2号位、1号位、3号位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/h5afVxjJQyCrPk_CZ3iKkg/zh-cn_image_0000002742003719.png)

播控中心根据应用设置的[AVSessionType](../harmonyos-references/arkts-apis-avsession-t.md#avsessiontype10)会话类型（本文提到的会话类型均指应用设置的AVSessionType）决定三元组/五元组控制按钮的显示：

* **通话类型的应用**：如voice\_call、video\_call类型，只涉及在播控中心的三元组界面显示，且固定显示为：2号位显示置灰的上一首、1号位显示置灰的播放、3号位显示置灰的下一首。
* **音视频类型的应用**：涉及播控中心的三元组和五元组界面显示，主要分为audio和video两种类型显示规则，具体的显示规则下文详细介绍。

## 音视频类应用默认显示规则

播控中心默认三元组/五元组显示规则如下：

* **五元组**：

  + audio类型：循环模式、上一首、播放/暂停、下一首、收藏。

    当应用[支持倍速](avsession-mediacentercontroltype-scene.md#speedSupportExplain)时，五元组的4号位和5号位显示如下：

    - 应用既[支持循环模式](avsession-mediacentercontroltype-scene.md#loopSupportExplain)也支持收藏（注册了是否收藏的监听）：4号位显示循环模式，5号位显示收藏。
    - 应用支持收藏但不支持循环模式：4号位显示收藏，5号位显示倍速。
    - 应用支持循环模式但不支持收藏：4号位显示循环模式，5号位显示倍速。
    - 应用不支持循环模式和收藏：4号位显示空白，5号位显示倍速。
  + video类型：快退、上一首、播放/暂停、下一首、快进。
* **三元组**：

  + 应用如果[注册](avsession-access-scene.md#支持的控制命令)了上一首或下一首的监听，且没有注册快进和快退的监听，显示上一首、播放/暂停、下一首。
  + 应用如果注册了快进或快退的监听，且没有注册上一首和下一首的监听，显示快退、播放/暂停、快进。
  + 应用如果既注册了上一首或下一首，又注册了快进或快退的监听：
    - audio类型：上一首、播放/暂停、下一首。
    - video类型：快退、播放/暂停、快进。

### 说明

* 以上为控制按钮是否显示的规则，具体高亮还是置灰显示取决于应用是否[注册](avsession-access-scene.md#支持的控制命令)了对应控制指令的回调监听；如果应用没有注册任何控制指令的回调监听（即不支持所有控制指令），播控中心不会展示应用信息。
* 对于audio类型的应用，循环模式、收藏、倍速都不支持时，五元组对应的4号、5号位会显示为空白（而不是置灰显示）。

## 应用自定义显示规则

应用可以通过[setMediaCenterControlType](../harmonyos-references/arkts-apis-avsession-avsession.md#setmediacentercontroltype)接口自定义设置三元组/五元组控制按钮的显示，可设置的控制类型详见[AVMediaCenterControlType](../harmonyos-references/arkts-apis-avsession-t.md#avmediacentercontroltype)。系统根据应用设置的[AVMediaCenterControlType](../harmonyos-references/arkts-apis-avsession-t.md#avmediacentercontroltype)列表，结合系统显示优先级进行最终的三元组/五元组控制按钮显示，详细规则如下：

### 三元组自定义规则

| 编号 | audio类型显示优先级（从左往右优先级依次降低） | video类型显示优先级（从左往右优先级依次降低） |
| --- | --- | --- |
| 1号位 | 播放/暂停 | 播放/暂停 |
| 2号位 | 上一首 > 快退 > 循环模式 > 收藏 | 快退 > 上一首 > 循环模式 > 收藏 |
| 3号位 | 下一首 > 快进 > 收藏 > 倍速 | 快进 > 下一首 > 收藏 > 倍速 |

### 五元组自定义规则

| 编号 | 显示优先级（不区分audio和video类型，从左往右优先级依次降低） |
| --- | --- |
| 1号位 | 播放/暂停 |
| 2号位 | 上一首 > 快退 > 循环模式 > 收藏 |
| 3号位 | 下一首 > 快进 > 收藏 > 倍速 |
| 4号位 | 快退 > 循环模式 > 收藏 |
| 5号位 | 快进 > 收藏 > 倍速 |

### 说明

* 对于上一首/下一首、快进/快退，系统建议应用成对设置。如果应用设置的[AVMediaCenterControlType](../harmonyos-references/arkts-apis-avsession-t.md#avmediacentercontroltype)列表仅包含其中一个，如快进/下一首，系统会默认将对称的快退/上一首在对应的位置显示出来。例如：应用设置的控制类型为{上一首、快进}，播控中心显示如下：
  + 三元组：对于audio类型，1号位显示播放/暂停、2号位显示上一首、3号位显示下一首；对于video类型，1号位显示播放/暂停、2号位显示快退、3号位显示快进。
  + 五元组：1号位显示播放/暂停、2号位显示上一首、3号位显示下一首、4号位显示快退、5号位显示快进。
* 循环模式：有空余槽位的情况下，如果应用设置的[AVMediaCenterControlType](../harmonyos-references/arkts-apis-avsession-t.md#avmediacentercontroltype)列表包含循环模式，需要满足下面两个条件之一，循环模式按钮才会显示：
  + 条件1：应用注册了[on('setLoopMode')](../harmonyos-references/arkts-apis-avsession-avsession.md#onsetloopmode10)监听。
  + 条件2：应用注册了[on('setTargetLoopMode')](../harmonyos-references/arkts-apis-avsession-avsession.md#onsettargetloopmode18)监听，且使用[setSupportedLoopModes](../harmonyos-references/arkts-apis-avsession-avsession.md#setsupportedloopmodes)设置了非空的循环模式列表。
* 倍速：有空余槽位的情况下，如果应用设置的[AVMediaCenterControlType](../harmonyos-references/arkts-apis-avsession-t.md#avmediacentercontroltype)列表包含倍速，应用需要使用[setSupportedPlaySpeeds](../harmonyos-references/arkts-apis-avsession-avsession.md#setsupportedplayspeeds)设置非空的倍速列表，倍速按钮才会显示。
* 收藏：当收藏与倍速、循环模式共同存在时，收藏按钮优先显示在循环模式的右侧、显示在倍速按钮的左侧；当仅有收藏时，收藏按钮优先显示在3号位。
* 1号位固定显示播放/暂停；当某一位置没有任何控制按钮需要显示时，该位置会显示为空白；如果设置的列表为空，系统会按照[默认显示规则](avsession-mediacentercontroltype-scene.md#音视频类应用默认显示规则)处理。
* [setMediaCenterControlType](../harmonyos-references/arkts-apis-avsession-avsession.md#setmediacentercontroltype)接口仅用于是否显示控制按钮，具体高亮还是置灰显示取决于应用是否[注册](avsession-access-scene.md#支持的控制命令)了对应控制指令的回调监听。

## 参考案例

以下示例代码展示了应用如何在播控中心五元组上从左到右依次显示循环模式、上一首、播放/暂停、下一首、倍速。

```typescript
import { avSession as AVSessionManager } from '@kit.AVSessionKit';

// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          try {
            let context = this.getUIContext().getHostContext() as Context;
            // 假设已经创建了一个session，如何创建session可以参考之前的案例。
            let type: AVSessionManager.AVSessionType = 'audio';
            let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
            // 设置必要的媒体信息和监听。
            let metadata: AVSessionManager.AVMetadata = {
              assetId: '0',
              title: 'TITLE',
            };
            await session.setAVMetadata(metadata);
            session.on('play', () => {
              console.info(`onPlay`);
            });
            session.on('playNext', () => {
              console.info(`onPlayNext`);
            });
            // 注册'setTargetLoopMode'监听并设置支持的循环模式范围，以支持播控中心显示循环模式按钮
            session.on('setTargetLoopMode', (loopMode: AVSessionManager.LoopMode) => {
              console.info(`targetLoopMode change: ${loopMode}`);
            });
            session.setSupportedLoopModes(
              [AVSessionManager.LoopMode.LOOP_MODE_SINGLE, AVSessionManager.LoopMode.LOOP_MODE_LIST,
                AVSessionManager.LoopMode.LOOP_MODE_SHUFFLE]);
            // 注册'setSpeed'监听并设置支持的倍速范围，以支持播控中心显示倍速按钮
            session.on('setSpeed', (speed: number) => {
              console.info(`speed change: ${speed}`);
            });
            session.setSupportedPlaySpeeds([0.5, 1.0, 2]);
            // 调用接口设置支持的控制命令类型列表
            session.setMediaCenterControlType(['playNext', 'setLoopMode', 'setSpeed']);
            // 设置完成后，播控中心三元组会显示上一首、播放/暂停、下一首；五元组会显示循环模式、上一首、播放/暂停、下一首、倍速
            // ...
          } catch (err) {
            console.error(`Failed to setMediaCenterControlType. Code: ${err.code}, message: ${err.message}`);
          }

        })
    }
    .width('100%')
    .height('100%')
  }
}
```
