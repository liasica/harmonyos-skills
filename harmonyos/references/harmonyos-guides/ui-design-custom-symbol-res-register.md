---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-custom-symbol-res-register
title: 应用加载自定义Symbol
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 应用加载自定义Symbol
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f923c34097bd636b3f1c52286ebf53e01856cb13e139aea968b640552a30ca24
---

## 场景介绍

从5.1.1 (19)版本开始，新增支持资源注册。

适用于需要快速定制应用内[Symbol图标](../harmonyos-references/ui-design-symbolregister.md)，不想强依赖于系统版本中预制的系统Symbol图标资源。

## 约束条件

资源注册支持Phone、Tablet、PC/2in1设备，并且从5.1.1(19)版本开始，新增支持TV设备。

## 开发步骤

1. 将UX设计师提供的Symbol图标资源（TTF文件）与动效参数资源（JSON文件）放入entry/src/main/resources/rawfile下，可新建目录。

   说明：[Symbol资源制作流程参考](../design-guides/system-icons-0000001929854962.md)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/wPYndkLAT4ewV9vsmIVVsQ/zh-cn_image_0000002583438395.png?HW-CC-KV=V1&HW-CC-Date=20260427T234156Z&HW-CC-Expire=86400&HW-CC-Sign=63C44C713E445B5EFD0FC787930156BDDE9DFDD7098578AB72EC95E83E34430B)
2. 多语言场景，在entry/src/main/resources目录中对应语言目录下的string.json文件中配置对应的Symbol图标Unicode值。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/jzV9e27USr2-lndL6TxUlQ/zh-cn_image_0000002552958350.png?HW-CC-KV=V1&HW-CC-Date=20260427T234156Z&HW-CC-Expire=86400&HW-CC-Sign=06EB094F23B3B8222E1D62DE99A27158236AEDCDF4C61358CC0ED60EEA6B0F55)

   ```
   1. {
   2. "string": [
   3. {
   4. "name": "symbol_custom_phone_fill_1",
   5. "value": "0x100016"
   6. }
   7. ]
   8. }
   ```
3. 导入相关模块。

   ```
   1. import { symbolRegister } from '@kit.UIDesignKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
4. 在通过SymbolGlyph/SymbolSpan组件展示自定义Symbol图标前，需要注册加载图标资源与动效参数资源。

   ```
   1. try {
   2. let result = symbolRegister.registerSymbol($rawfile("symbol/symbol_register.ttf"), $rawfile("symbol/symbol_register.json"));
   3. } catch (error) {
   4. let err = error as BusinessError;
   5. console.error("errCode: " + err.code)
   6. console.error("error: " + err.message);
   7. }
   ```
5. 在需要展示自定义Symbol图标的页面通过SymbolGlyph/SymbolSpan组件展示该图标。

   ```
   1. struct test {
   2. build() {
   3. Column(){
   4. SymbolGlyph($r('app.string.symbol_custom_phone_fill_1'))
   5. }
   6. }
   7. }
   ```

## 开发实例

```
1. import { symbolRegister } from '@kit.UIDesignKit';
2. import { BusinessError } from '@ohos.base';

4. @Entry
5. @Component
6. struct test {
7. aboutToAppear(): void {
8. try {
9. let result = symbolRegister.registerSymbol($rawfile("symbol/symbol_register.ttf"), $rawfile("symbol/symbol_register.json"));
10. } catch (error) {
11. let err = error as BusinessError;
12. console.error("errCode: " + err.code)
13. console.error("error: " + err.message);
14. }
15. }
16. build() {
17. Column(){
18. SymbolGlyph($r('app.string.symbol_custom_phone_fill_1'))
19. }
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/0RjlyFTqRFGY4dmcGBdVvw/zh-cn_image_0000002583478351.png?HW-CC-KV=V1&HW-CC-Date=20260427T234156Z&HW-CC-Expire=86400&HW-CC-Sign=A96A997497C818AF82DF80042E67581CA484EF8D2129BD445515593FF0AF43E0)
