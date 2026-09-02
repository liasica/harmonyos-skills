---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-healthservice-1
title: 无法连接穿戴类设备
breadcrumb: FAQ > 应用服务开发 > 运动健康数据服务（Health Service Kit） > 无法连接穿戴类设备
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-07-02
content_hash: sha256:694332733b6382d3fbcb872a71b0cd8451d7782ce80dad2ea015be0940d060de
---

## 问题现象

用户在使用应用时，无法正常连接智能手表/手环等穿戴设备。

## 背景知识

穿戴服务错误码：[1008500006](../harmonyos-references/errorcode-wearengine.md#section1008500006-用户未同意隐私授权)用户未同意隐私授权。

用户在设备上首次使用运动健康服务时，需要用户同意运动健康服务隐私协议，当前隐私授权依赖运动健康App，需引导用户打开运动健康App并完成隐私授权。

## 问题定位

复现问题后，在日志中查找关键字CheckOrRequestPermission fail。

```txt
E  CheckOrRequestPermission fail, error code:1608580086, message:User privacy is not agreed.
```

## 分析结论

错误信息“User privacy is not agreed”说明用户未同意运动健康隐私授权，导致无法连接到穿戴设备。

## 修改建议

1. 在module.json5文件中增加querySchemes字段，并在列表中配置"huaweischeme"。

   "huaweischeme"为需要跳转到的运动健康App首页的scheme。

   具体写法参考module.json5[配置文件标签](../harmonyos-guides/module-configuration-file.md#配置文件标签)中querySchemes属性介绍。
2. 调用[bundleManager.canOpenLink](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagercanopenlink12)判断运动健康App是否安装。
   * 已安装则调用[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口拉起运动健康App；
   * 未安装则拉起[应用详情页展示](../harmonyos-guides/appgallery-productview-loadproduct.md)接口，引导用户下载运动健康App。

     ```ts
     import { bundleManager } from '@kit.AbilityKit';
     import { common } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';

     @Entry
     @Component
     struct Demo {
       build() {
         Button('拉起运动健康')
           .onClick(async () => {
             try {
               const result = bundleManager.canOpenLink('huaweischeme://healthapp/home/main');
               const ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
               if (result) {
                 await ctx.openLink('huaweischeme://healthapp/home/main');
               } else {
                 await ctx.startAbility({
                   bundleName: 'com.huawei.appmarket',
                   abilityName: 'com.huawei.appmarket.detail',
                   parameters: { 'appId': 'com.huawei.hmos.health' }
                 });
               }
             } catch (err) {
               hilog.error(0x0000, 'testTag', JSON.stringify(err));
             }
           });
       }
     }
     ```
