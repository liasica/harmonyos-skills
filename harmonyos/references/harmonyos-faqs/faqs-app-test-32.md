---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-32
title: UI测试中如何在feature模块启动当前模块的ability
breadcrumb: FAQ > DevEco Studio > 应用测试 > UI测试中如何在feature模块启动当前模块的ability
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a850adbb352efaa1e2ce50e227741410630380d0d97392f3b2d3196abc17c8f8
---

## 问题现象

使用DevEco Studio进行UI测试，在feature模块下启动ability如何实现？

## 背景知识

UI测试框架（UITest）为开发者提供UI界面查找和模拟操作能力，可覆盖UI自动化测试的关键场景，包括界面控件精准查找、UI交互操作（如点击、滑动、文本输入等），参考：[UI测试框架使用指导](../harmonyos-guides/uitest-guidelines.md)。

## 解决方案

1. 在项目工程中新建feature模块：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/BZrTzMaOTXyFMhaDRays0A/zh-cn_image_0000002658808887.png "点击放大")
2. 打开feature\src\main\module.json5，查看abilities标签的name属性值，确认需要启动的abilityName：

   ```json
   "abilities": [
     {
     "name": "FeatureAbility",
     "srcEntry": "./ets/featureability/FeatureAbility.ets",
     "description": "$string:FeatureAbility_desc",
     "icon": "$media:layered_image",
     "label": "$string:FeatureAbility_label",
     "startWindowIcon": "$media:startIcon",
     "startWindowBackground": "$color:start_window_background",
     "exported": true
     }
   ],
   ```
3. 在feature\src\ohosTest\ets\test\Ability.test.ets编写测试用例启动测试页面，代码示例如下：

   ```ts
   import { describe, it, expect } from '@ohos/hypium';
   import { abilityDelegatorRegistry } from '@kit.TestKit';
   import { Want } from '@kit.AbilityKit';

   const delegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
   const bundleName = abilityDelegatorRegistry.getArguments().bundleName;

   function sleep(time: number) {
     return new Promise<void>((resolve: Function) => setTimeout(resolve, time));
   }

   export default function abilityTest() {
     describe('AbilityTest', () => {

       it('testStartFeatureTest', 0, async (done: Function) => {
         const want: Want = {
           bundleName: bundleName,
           abilityName: 'FeatureAbility'
         };
         try {
           await delegator.startAbility(want);
           await sleep(1000);

           const ability = await delegator.getCurrentTopAbility();
           expect(ability.context.abilityInfo.name).assertEqual('FeatureAbility');

           done();
         } catch (error) {
           console.error(`startAbility error. Code is ${error.code}, message is ${error.message}.`);
         }
       });
     });
   }
   ```
