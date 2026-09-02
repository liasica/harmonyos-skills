---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-free-flow-1
title: 应用接续功能使用失败
breadcrumb: FAQ > 多设备场景 > 自由流转 > 常见问题 > 应用接续功能使用失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:4cf8e9fe10bb15330d2826520bde3f63a1aa0c8098e35520623c882c3b57b050
---

## 问题现象

应用进行功能接力（应用接续），在弹出的选择弹窗中选择设备后，提示“设备状态异常，请稍后再试！”。

## 背景知识

[应用接续](../best-practices/bpta-continue-cast.md)：指当用户在一个设备上操作某个应用时，可以在另一个设备的同一个应用中快速切换，并无缝衔接上一个设备的应用体验。比如在用户使用过程中，使用情景发生了变化，之前使用的设备不再适合继续当前任务，或者周围有更合适的设备，此时用户可以选择使用新的设备来继续当前的任务。接续完成后，之前设备的应用可退出或保留，用户可以将注意力集中在被拉起的设备上，继续执行任务。应用接续的运作机制如下：

1. 在源端，通过UIAbility的onContinue()回调，开发者可以保存待接续的业务数据。例如，浏览器应用完成应用接续，在源端浏览一个页面，到对端继续浏览。系统将自动保存页面状态，如当前页面的浏览进度；开发者需要通过onContinue接口保存页面url等业务内容。
2. 分布式框架提供跨设备应用界面、页面栈以及业务数据的保存和恢复机制，负责将数据从源端发送到对端。
3. 在对端，同一UIAbility通过onCreate/onNewWant接口恢复业务数据。

## 问题定位

1. 需要进行前序检查：
   * 双端设备需要登录同一华为账号。
   * 双端设备需要打开WLAN和蓝牙开关，或者在设置中的“多设备协同>高级”中启用“多设备协同增强服务”功能。
   * 双端设备需要在“设置”应用中开启“多设备协同>接续”功能。
   * 双端设备都需要安装该应用。
   * 为了接续体验，在onContinue回调中使用wantParam传输的数据需要控制在100KB以下，大数据量请使用分布式数据对象进行同步。
2. 若前序检查均无误，需进一步查看在应用的module.json5文件的abilities中，是否将continuable标签配置为“true”。配置为false的UIAbility将被系统识别为无法迁移且该配置默认值为false。
3. 进一步，需要检查应用在源端UIAbility中是否实现onContinue()接口。全局搜索关键词onContinue，查看应用是否成功实现该接口，具体可参考[应用接续开发步骤](../best-practices/bpta-continue-cast.md#section49581955132610)。

## 分析结论

在前序检查无误的情况下，分析结论如下。

| 场景 | 结论 |
| --- | --- |
| module.json5文件配置问题 | 应用未进行正确的文件配置，被系统识别为无法迁移 |
| 未调用onContinue()接口，或者错误实现该接口 | 应用未成功实现onContinue()接口，导致任务跨设备迁移失败 |

## 修改建议

* 对于module.json5文件配置问题，建议在module.json5文件的abilities中，将continuable标签配置为“true”，表示该UIAbility可被迁移。配置为false的UIAbility将被系统识别为无法迁移且该配置默认值为false。
* 对于onContinue()接口的调用错误，建议在源端UIAbility中实现onContinue()接口，同时在目的端的UIAbility中实现onCreate()与onNewWant()接口，恢复迁移数据，具体可参考[应用接续开发步骤](../best-practices/bpta-continue-cast.md#section49581955132610)。
