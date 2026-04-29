---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme-font-c
title: 使用主题字体（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 字体管理 > 使用主题字体（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:44c98feb30c198b91ce6cef296e3f6bf579320d7657d35c1cf5f40ad9188414b
---

## 场景介绍

主题字体，特指系统**主题应用**中能使用的字体，属于一种特殊的自定义字体。可以通过相关接口调用使能主题应用中的主题字体。

## 实现机制

**图1** 主题字体的切换和使用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/eidUg1TwTKS_Wn5QgXiyKA/zh-cn_image_0000002558765170.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053613Z&HW-CC-Expire=86400&HW-CC-Sign=D5560CD8FE2DBA46A6321C5AA9B7EC84266F591E186754D8D3EFF9A4F964B3B2)

针对主题字的切换使用，应用方应确保订阅主题字变更事件，当接收字体变更事件后，由应用方主动调用页面刷新才能实现主题字的切换，否则主题字只能在重启应用后才生效；主题字的绘制需要使用OH\_Drawing\_GetFontCollectionGlobalInstance来获取全局字体集对象，仅该接口返回的对象拥有主题字体信息。

说明

由OH\_Drawing\_CreateSharedFontCollection创建的字体集对象不包含主题字信息，无法用于绘制主题字。

## 接口说明

注册使用主题字体的常用接口如下表所示，详细接口说明请参考[Drawing](../harmonyos-references/capi-drawing.md)。

| 接口名 | 描述 |
| --- | --- |
| OH\_Drawing\_FontCollection\* OH\_Drawing\_GetFontCollectionGlobalInstance(void) | 获取全局的字体集对象OH\_Drawing\_FontCollection。 |
| [onConfigurationUpdate()](../harmonyos-references/js-apis-app-ability-ability.md#abilityonconfigurationupdate) | 系统配置更新时调用。  主题应用当前仅提供ArkTS接口发布变更事件，需要应用自行处理进行跨语言调用。 |

## 开发步骤

1. 请确保在设备系统**主题应用**中，能成功应用一项主题字体。
2. 在应用入口文件（默认工程中为EntryAbility.ets）中重写onConfigurationUpdate函数，以响应fontId变更，适配主题字体的切换和页面刷新，重写方式可参考[主题字变更事件](theme-font-arkts.md#开发步骤)。

   系统配置信息（即示例中的newConfig）变化时，会自动触发onConfigurationUpdate函数。应用可从系统发送的配置信息获取fontId，通过判断是否与应用本地保存的fontId一致来识别主题字的切换。若不一致则刷新本地fontId，并调用C++代码刷新排版结果。从ArkTS到C++的调用通路需应用根据实际情况选取调用方式，本示例不作推荐。跨语言调用可参考[Node-API简介](napi-introduction.md)。
3. 导入C++侧依赖，本步骤及之后均为主题字体在C++侧的使用

   在工程的src/main/cpp/CMakeLists.txt文件中添加以下lib。

   ```
   1. libnative_drawing.so
   ```

   导入头文件。

   ```
   1. #include <native_drawing/drawing_font_collection.h>
   2. #include <native_drawing/drawing_text_typography.h>
   3. #include <native_drawing/drawing_register_font.h>
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L16-L20)
4. 创建字体管理器。

   说明

   注册主题字体作用于字体管理集全局对象，故必须使用OH\_Drawing\_GetFontCollectionGlobalInstance获取全局字体集对象进行绘制。如若使用OH\_Drawing\_CreateSharedFontCollection或OH\_Drawing\_CreateFontCollection创建字体集对象，无法使用主题字体。OH\_Drawing\_GetFontCollectionGlobalInstance获取的全局字体集不允许释放，释放会造成字体绘制紊乱问题。

   ```
   1. OH_Drawing_FontCollection *fontCollection = OH_Drawing_GetFontCollectionGlobalInstance();
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L395-L397)
5. OH\_Drawing\_SetTextStyleFontFamilies()接口可以用来指定字体家族名，从而实现使用指定字体。但使用主题字体，不需要使用OH\_Drawing\_SetTextStyleFontFamilies()接口指定字体，否则行为变更为优先使用指定字体，而不是主题字体。

   ```
   1. OH_Drawing_TextStyle *myTextStyle = OH_Drawing_CreateTextStyle();
   2. // const char* myFontFamilies[] = {"otherFontFamilyName"};
   3. // 注意不要使用此接口来指定字体
   4. // OH_Drawing_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L398-L403)
6. 设置段落文本内容为"Hello World. \nThis is the theme font."，此时该段落文本将应用主题字体。

   ```
   1. // 设置其他文本样式
   2. OH_Drawing_SetTextStyleColor(myTextStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
   3. // 设置字体大小为100.0
   4. OH_Drawing_SetTextStyleFontSize(myTextStyle, 100.0);
   5. // 创建一个段落样式对象，以设置排版风格
   6. OH_Drawing_TypographyStyle *typographyStyle = OH_Drawing_CreateTypographyStyle();
   7. OH_Drawing_SetTypographyTextAlign(typographyStyle, TEXT_ALIGN_LEFT); // 设置段落样式为左对齐
   8. // 创建一个段落生成器
   9. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typographyStyle, fontCollection);
   10. // 在段落生成器中设置文本样式
   11. OH_Drawing_TypographyHandlerPushTextStyle(handler, myTextStyle);
   12. // 在段落生成器中设置文本内容
   13. const char *text = "Hello World. \nThis is the theme font.";
   14. OH_Drawing_TypographyHandlerAddText(handler, text);
   15. // 通过段落生成器生成段落
   16. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L405-L422)

## 效果展示

以下展示了在系统**主题应用**中切换使用不同主题字体后，对应的文字渲染效果。

不同主题字体显示效果不同，此处仅示意。

**图2** 主题字体1的效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/U3BPylqxSS6eSdUkXFB9vw/zh-cn_image_0000002589244979.png?HW-CC-KV=V1&HW-CC-Date=20260429T053613Z&HW-CC-Expire=86400&HW-CC-Sign=A0201EF7E9FF4F46A327BBDD6A5FDDC978A72E11B975207A5B4109CFCAF4AFC0)

**图3** 主题字体2的效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/rst3ksQ1QDmJ1MBh6l6UOA/zh-cn_image_0000002558765174.png?HW-CC-KV=V1&HW-CC-Date=20260429T053613Z&HW-CC-Expire=86400&HW-CC-Sign=9439C7F7B18C66A93EB1A97520D27CC16AC65F6B84911885918C69AB068C089C)
