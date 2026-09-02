---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-15
title: 后台播放状态异常
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 后台播放状态异常
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:22+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:bf34d9cfdb60d59fc05f2a18ef4b045b91fed2325d189bc02af79db9d07b5637
---

## 问题现象

当应用从前台切换到后台或进入锁屏状态后，媒体的播放可能会出现不符合用户预期的情况，比如意外暂停等问题。

## 背景知识

* [AVSession Kit（音视频播控服务）](../harmonyos-guides/avsession-overview.md) ：AVSession会对后台的音频播放、VOIP通话做约束，当应用没有接入AVSession，那么系统会在检测到应用后台时，停止对应的音频播放，静音通话声音，以达到约束应用行为的目的。
* [BackgroundTasks Kit（后台任务开发服务）](../harmonyos-guides/background-task-kit.md)：当应用需要实现后台播放等功能时，需要使用后台任务管理的能力，申请对应的长时任务，避免进入挂起（Suspend）状态。
* 接入AVSession的目的是让应用接入[播控中心](../design-guides/broadcasting-control-0000001957017133.md)，应用上架前需进行[应用接入播控自检](../harmonyos-guides/playback-control-access-selfcheck.md)，以确保应用的基础体验。
* 只有使用了媒体会话服务（AVSession）的音视频应用，才能申请长时任务实现后台播放。对媒体类播放来说，需要申请[AUDIO\_PLAYBACK](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)的长时任务。
* 播控中心与应用的交互，详情可参考[播控中心控制应用播放](../best-practices/bpta-audio-cast.md#section769314507911)。
  1. 注册播控中心通知回调：当用户在锁屏或者其他界面时希望通过播控中心控制应用的播放状态，比如播放、暂停、下一首等，需要设置监听回调来对播控中心的通知做出对应的调整，只有设置了回调，播控中心侧的按钮才会亮起来，否则按钮将会置灰。
  2. 应用状态上报播控中心：当应用内音频信息发生改变时，如用户手动在应用内操作或应用响应播控中心通知进行调整后，通过[setAVPlaybackState](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)方法可以上报媒体播放状态，如暂停、播放、进度调整、循环模式、收藏状态等。

## 问题定位

1. 明确应用是否有后台播放的使用诉求并接入AVSession。通常长音频应用、听书类应用、长视频应用、VOIP类应用等都需要接入AVSession，可参考[应用接入AVSession场景介绍](../harmonyos-guides/avsession-access-scene.md)。
2. 对于有后台播放使用诉求的应用，检查对应音频是否创建（[createAVSession](../harmonyos-references/arkts-apis-avsession-f.md#avsessioncreateavsession10)）并激活（[activate](../harmonyos-references/arkts-apis-avsession-avsession.md#activate10)）AVSession会话对象，明确AVSession的接入情况。
3. 检查module.json文件的[requestPermissions](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)标签是否配置[ohos.permission.KEEP\_BACKGROUND\_RUNNING](../harmonyos-guides/permissions-for-all.md#ohospermissionkeep_background_running)权限。
4. 检查申请长时任务的实现，BackgroundTasks Kit的[startBackgroundRunning](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning)和[stopBackgroundRunning](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning)方法分别是申请和取消后台运行任务，长时任务类型选择AUDIO\_PLAYBACK，表示音视频后台播放，可参考[后台播放音乐](faqs-audio-1.md)。
5. 检查应用自身音频播放状态和AVSession播放状态的同步逻辑，参考背景知识的**播控中心与应用的交互**进行分析。

## 分析结论

* 场景一：

  应用有后台播放的使用诉求，但未接入AVSession，系统在检测到应用后台时，停止对应的音频播放。
* 场景二：

  应用有后台播放的使用诉求并接入了AVSession，但是未申请长时任务导致播放被挂起。
* 场景三：

  应用未正确注册播控中心通知回调，或者未及时将应用状态上报播控中心，导致后台播放状态异常。

## 修改建议

### 场景一

应用接入AVSession的流程：

1. 确定应用需要创建的会话类型，[创建对应的会话](../harmonyos-guides/avsession-access-scene.md#创建不同类型的会话)，不同类型决定了播控中心展示的控制模板样式。
2. 按需[创建后台任务](../harmonyos-guides/avsession-access-scene.md#创建后台任务)。
3. [设置必要的元数据（Metadata）](../harmonyos-guides/avsession-access-scene.md#设置元数据信息)，以在播控中心展示相应的信息，包括不限于：当前媒体的ID（assetId），上一首媒体的ID（previousAssetId），下一首媒体的ID（nextAssetId），标题（title），专辑作者（author），专辑名称（album），词作者（writer），媒体时长（duration）等属性。
4. [设置播放相关的状态](../harmonyos-guides/avsession-access-scene.md#设置播放状态)，包括不限于：当前媒体的播放状态（state）、播放位置（position）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体Id（activeItemId）、自定义媒体数据（extras）等属性。
5. 按需[注册不同的控制命令](../harmonyos-guides/avsession-access-scene.md#控制命令的处理)，包括不限于：播放/暂停、上下一首、快进快退、收藏、循环模式、进度条。
6. 应用退出或者无对应业务时，注销会话。

### 场景二

申请[AUDIO\_PLAYBACK](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)的长时任务，详情可参考[后台播放音乐](faqs-audio-1.md)。

### 场景三

检查音频状态和AVSession状态的实现逻辑，保持一致，可参考[播控中心控制应用播放](../best-practices/bpta-audio-cast.md#section769314507911)。
