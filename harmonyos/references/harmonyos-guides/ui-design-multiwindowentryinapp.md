---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-multiwindowentryinapp
title: 应用内多窗
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 应用内多窗
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8da6882791d3408c5a4c62e10f08f1808cfd40e996f04036aeea6ff784c435c7
---

## 场景介绍

从6.0.0(20)Beta3版本开始，新增支持应用内多窗。

通过应用内多窗组件[MultiWindowEntryInAPP](../harmonyos-references/ui-design-multiwindowentryinapp-api.md)提供的单应用多窗口接口，实现一个应用多个窗口并行运行的体验。并且可以设置图标大小颜色、背板大小颜色、文字大小颜色等。

如果开发者未集成HdsNavigation组件，可使用应用内多窗组件实现应用内多窗体验。

## 约束条件

依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备形态有：

* 双折叠：展开态。
* 三折叠：双屏态，三屏态的横屏态。
* 平板：横屏态。

对于不支持的设备形态，该组件不可交互，不响应点击事件。

## 开发步骤

1. 导入模块。

   ```
   1. // 从6.0.2(22)版本开始，无需手动导入MultiWindowEntryInAPPAttribute。具体请参考MultiWindowEntryInAPP的导入模块说明。
   2. import { MultiWindowEntryInAPP, MultiWindowEntryInAPPAttribute } from '@kit.UIDesignKit';
   3. import { Want } from '@kit.AbilityKit';
   4. import { TextModifier }  from '@kit.ArkUI';
   ```
2. 使用MultiWindowEntryInAPP组件，并且设置组件参数。

   ```
   1. @Entry
   2. @Component
   3. struct MultiWindowEntryInAPPTest {
   4. @State textModifier: TextModifier = new TextModifier();
   5. private want: Want = {
   6. // 修改为当前应用的bundleName、moduleName、abilityName，启动应用内的UIAbility
   7. bundleName: "com.example.myapplication",
   8. moduleName: "entry",
   9. abilityName: "FuncAbility",
   10. };

   12. build() {
   13. Row() {
   14. MultiWindowEntryInAPP({
   15. want: this.want, isShowSubtitle: true, multiWindowEntryInAPPStyle: {
   16. iconOptions: {
   17. iconSize: 24,
   18. iconColor: $r('sys.color.font_primary'),
   19. iconWeight: FontWeight.Normal,
   20. backgroundColor: $r('sys.color.comp_background_tertiary')
   21. },
   22. subtitleOptions: {
   23. modifier: this.textModifier.fontColor(Color.Black)
   24. }
   25. }
   26. })
   27. .size({ width: 48, height: 48 })
   28. .position({ x: 400, y: 30 })
   29. }
   30. }
   31. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/X9zVxLSfS_SNEhYtxvfhSA/zh-cn_image_0000002558605196.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053025Z&HW-CC-Expire=86400&HW-CC-Sign=19C7B8E1F983BAFB4FF4C227A81AB2AFE4B14FD03E50B717631A76DD1242E756)
