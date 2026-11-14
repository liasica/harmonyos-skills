---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-adapt-faq
title: ArkTS卡片适配常见问题
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片适配常见问题
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:19+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:c8a0095445db5726ea74aadbd50ab8b0f9cdaa6c6307276d29c4ee6323a8ff47
---

## ArkTS卡片使用V2装饰器进行状态管理

ArkTS卡片开发支持V2装饰器语法(如[@ObservedV2](arkts-new-observedv2-and-trace.md)、[@ComponentV2](arkts-create-custom-components.md#componentv2))，建议开发者使用V2装饰器替代V1语法进行状态管理，以获得更优的组件渲染性能和状态同步能力。

完整的语法差异对比、迁移步骤及示例代码，请参见官方文档： [V1->V2迁移指导概述](arkts-v1-v2-migration.md)。

## 如何定位ArkTS卡片白屏问题？

ArkTS卡片白屏问题定位请参考[服务卡片显示问题定位指导](https://developer.huawei.com/consumer/cn/forum/topic/0202182083369423556)

## ArkTS卡片适配深色模式

当前系统存在深浅色两种显示模式，为了给用户更好的使用体验，保障卡片与页面视觉体验一致性，ArkTS卡片支持适配深浅色模式，具体请参考[应用深浅色适配](ui-dark-light-color-adaptation.md)。

## 导入particleAbility、audio、camera、media、backgroundTaskManager模块导致应用崩溃问题

### 问题现象

导入particleAbility、audio、camera、media、backgroundTaskManager后应用崩溃，FaultLog指向相关调用行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/3Y1gYWzURG-RCKWo1TrHEw/zh-cn_image_0000002817506745.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C7A87DD536ADAE649F08A6547C295C0E8E4A972399D1E6DFD2342F544A3BD34)

报错对应的代码行如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ytP9ZvhwS6iFgP48_1i1Eg/zh-cn_image_0000002788307314.png?HW-CC-KV=V1&HW-CC-Date=20261114T004719Z&HW-CC-Expire=31536000000&HW-CC-Sign=A14404BC542694B348C8318860E7B1672074087A5A26CB4DF6EDF1C14B328FCF)

### 原因

ArkTS卡片的FormExtensionAbility不支持加载上述模块，参考[@ohos.app.form.FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)。强行加载得到的对象是undefined，使用时就会产生JS crash。

### 解决措施

检查 FormExtensionAbility 的导入链，将涉及上述模块的文件与 ArkTS 卡片使用的文件拆分，避免被 FormExtensionAbility 加载。
