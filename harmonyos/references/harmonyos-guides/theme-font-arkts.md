---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme-font-arkts
title: 使用主题字体（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 字体管理 > 使用主题字体（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c5248f36169a670adc0f61e39ed269b73e9d1416c2d5bfa5d622994934a810f0
---

## 场景介绍

主题字体，特指系统**主题应用**中能使用的字体，属于一种特殊的自定义字体，可以通过相关接口调用使能主题应用中的主题字体。

## 实现机制

**图1** 主题字体的切换和使用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/MxuqWLWxTxe281FJgP7Jbg/zh-cn_image_0000002552958670.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234713Z&HW-CC-Expire=86400&HW-CC-Sign=C9B60DF61205015511CD57E43380E4E496A69AEAF91FCB05677CBC5CB29B3A51)

针对主题字的切换使用，应用方应确保订阅主题字体变更事件，当接收到字体变更事件后，由应用方主动调用页面刷新才能实现主题字的切换，否则主题字只能在重启应用后才生效。

## 接口说明

注册使用主题字体的常用接口如下表所示，详细接口说明请见[@ohos.graphics.text (文本模块)](../harmonyos-references/js-apis-graphics-text.md)。

| 接口 | 描述 |
| --- | --- |
| getGlobalInstance(): FontCollection | 获取应用全局字体集的实例。 |

## 开发步骤

1. 请确保在设备系统**主题应用**中，能成功应用一项主题字体。
2. 导入依赖的相关模块。

   ```
   1. import { text } from '@kit.ArkGraphics2D';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ThemeFont/entry/src/main/ets/pages/Index.ets#L19-L21)
3. 使用getGlobalInstance()接口获取全局字体集对象，系统框架在注册主题字体过程中仅会将主题字体信息传入全局字体集对象中。

   ```
   1. // 获取字体管理器全局FontCollection实例
   2. let fontCollection = text.FontCollection.getGlobalInstance();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ThemeFont/entry/src/main/ets/pages/Index.ets#L28-L31)
4. 创建段落样式，并使用字体管理器实例构造段落生成器ParagraphBuilder实例，用于生成段落。

   说明

   在生成段落对象设置段落样式入参时，不能指定fontFamilies属性，否则会变为优先使用指定字体而非主题字体。

   若未在系统**主题应用**中设置一项主题字体，则将使用系统默认字体进行绘制。

   ```
   1. // 设置文本样式
   2. let myTextStyle: text.TextStyle = {
   3. color: { alpha: 255, red: 255, green: 0, blue: 0 },
   4. fontSize: 33
   5. };
   6. // 创建一个段落样式对象，以设置排版风格
   7. let myParagraphStyle: text.ParagraphStyle = {
   8. textStyle: myTextStyle,
   9. align: 3,
   10. wordBreak:text.WordBreak.NORMAL
   11. };
   12. // 创建一个段落生成器
   13. let paragraphGraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ThemeFont/entry/src/main/ets/pages/Index.ets#L32-L46)
5. 设置文本样式，添加文本内容，并生成段落文本用于后续文本的绘制显示。

   ```
   1. // 在段落生成器中设置文本样式
   2. paragraphGraphBuilder.pushStyle(myTextStyle);
   3. // 在段落生成器中设置文本内容
   4. paragraphGraphBuilder.addText("Hello World. \nThis is the theme font.");
   5. // 通过段落生成器生成段落
   6. let paragraph = paragraphGraphBuilder.build();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ThemeFont/entry/src/main/ets/pages/Index.ets#L47-L54)
6. 创建渲染节点，并保存到数组。（此处示例代码为简化逻辑，采用数组作为容器，实际开发中应结合应用情况选择更恰当的容器来保证节点的添加与删除对应。）

   ```
   1. // 创建渲染节点数组
   2. const renderNodeMap: Array<RenderNode> = new Array();
   3. // 创建节点控制器
   4. class MyNodeController extends NodeController {
   5. private rootNode: FrameNode | null = null;
   6. makeNode(uiContext: UIContext): FrameNode {
   7. this.rootNode = new FrameNode(uiContext);
   8. if (this.rootNode == null) {
   9. return this.rootNode;
   10. }
   11. const renderNode = this.rootNode.getRenderNode();
   12. if (renderNode != null) {
   13. renderNode.frame = { x: 0, y: 0, width: 300, height: 50 };
   14. renderNode.pivot = { x: 0, y: 0 };
   15. }
   16. return this.rootNode;
   17. }
   18. addNode(node: RenderNode): void {
   19. if (this.rootNode == null) {
   20. return;
   21. }
   22. const renderNode = this.rootNode.getRenderNode();
   23. if (renderNode != null) {
   24. renderNode.appendChild(node);
   25. // 将节点添加到渲染节点数组中
   26. renderNodeMap.push(node);
   27. }
   28. }
   29. clearNodes(): void {
   30. if (this.rootNode == null) {
   31. return;
   32. }
   33. const renderNode = this.rootNode.getRenderNode();
   34. if (renderNode != null) {
   35. renderNode.clearChildren();
   36. // 将节点从渲染节点数组中移除
   37. renderNodeMap.pop();
   38. }
   39. }
   40. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ThemeFont/entry/src/main/ets/pages/Index.ets#L61-L102)
7. 创建渲染节点更新函数，并导出函数，供其他文件（如：EntryAbility.ets）使用；重绘制节点目的为更新排版中字体信息，若不更新字体信息，使用之前残留结果，可能造成文字乱码。

   ```
   1. // 导出渲染节点更新函数
   2. export function updateRenderNodeData() {
   3. renderNodeMap.forEach((node) => {
   4. // 主动触发节点重绘制
   5. node.invalidate();
   6. });
   7. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ThemeFont/entry/src/main/ets/pages/Index.ets#L103-L111)
8. 在EntryAbility.ets中接收主题字变更事件，并调用渲染节点更新函数。

   ```
   1. import { AbilityConstant, Configuration, UIAbility, Want } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { window } from '@kit.ArkUI';
   4. import { updateRenderNodeData } from '../pages/Index';

   6. // ...

   8. export default class EntryAbility extends UIAbility {
   9. preFontId = "";
   10. // ...

   12. onConfigurationUpdate(newConfig: Configuration): void {
   13. let fontId = newConfig.fontId;
   14. if (fontId && fontId !== this.preFontId) {
   15. this.preFontId = fontId;
   16. updateRenderNodeData();
   17. // ...
   18. }
   19. }
   20. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/ThemeFont/entry/src/main/ets/entryability/EntryAbility.ets#L15-L55)

## 效果展示

以下展示了在系统**主题应用**中切换使用不同主题字体后，对应的文字渲染效果。

不同主题字体显示效果不同，此处仅示意。

**图2** 主题字体1的效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/KC_g63umR6W5xWXRDSsKAw/zh-cn_image_0000002583478671.png?HW-CC-KV=V1&HW-CC-Date=20260427T234713Z&HW-CC-Expire=86400&HW-CC-Sign=6FAE18996F80031569F730D0AA5919D33C7771022DE5281C39C8A1B11DD17E52)

**图3** 主题字体2的效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/Y1zpG85fTDaPXFijy37p4g/zh-cn_image_0000002552799022.png?HW-CC-KV=V1&HW-CC-Date=20260427T234713Z&HW-CC-Expire=86400&HW-CC-Sign=37E57FC10D74594FB5DFA91B4B0B812BB83A8735008FF55D620EC2F2332E65F6)
