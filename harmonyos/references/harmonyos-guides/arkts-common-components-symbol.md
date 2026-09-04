---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-symbol
title: 图标小符号 (SymbolGlyph/SymbolSpan)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 图标小符号 (SymbolGlyph/SymbolSpan)
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:00+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:0b01314d3ccc77d7a709b38e3b5554e88e9979aec0edeec7fbd5525576bbac8b
---

SymbolGlyph是图标小符号组件，便于使用精美的图标，如渲染多色图标和使用动效图标。SymbolSpan作为Text组件的子组件，可在文本中穿插显示图标小符号。具体用法请参考[SymbolGlyph](../harmonyos-references/ts-basic-components-symbolglyph.md)和[SymbolSpan](../harmonyos-references/ts-basic-components-symbolspan.md)组件的API文档。

## 创建图标

SymbolGlyph通过$r引用Resource资源来创建，目前仅支持系统预置的Symbol资源名。

相关资源可参考[系统图标](../design-guides/system-icons-0000001929854962.md)。

```typescript
SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
  .fontSize(96)
  .renderingStrategy(SymbolRenderingStrategy.SINGLE)
  .fontColor([Color.Black, Color.Green, Color.White])
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/W1PoCOvLTvuBbV35NBvQ-Q/zh-cn_image_0000002742002775.png)

## 添加到文本中

[SymbolSpan](../harmonyos-references/ts-basic-components-symbolspan.md)可作为[Text](../harmonyos-references/ts-basic-components-text.md)的子组件用于显示图标小符号。可以在一个Text组件内添加多个SymbolSpan，从而展示一串连续的图标。

* 创建SymbolSpan。

  SymbolSpan组件需嵌入在Text组件中才能显示，单独使用不会呈现任何内容。

  ```typescript
  Text() {
    SymbolSpan($r('sys.symbol.ohos_trash'))
      .fontWeight(FontWeight.Normal)
      .fontSize(96)
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/K1UjWR13SEKSNv_TT7zWDQ/zh-cn_image_0000002712403788.png)
* 通过[fontSize](../harmonyos-references/ts-basic-components-symbolspan.md#fontsize)属性设置SymbolSpan的大小。

  ```typescript
  Row() {
    Column() {
      Text('48')
      Text() {
        SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
          .fontSize(48)
          .renderingStrategy(SymbolRenderingStrategy.SINGLE)
          .fontColor([Color.Black, Color.Green, Color.White])
      }
    }

    Column() {
      Text('72')
      Text() {
        SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
          .fontSize(72)
          .renderingStrategy(SymbolRenderingStrategy.SINGLE)
          .fontColor([Color.Black, Color.Green, Color.White])
      }
    }

    Column() {
      Text('96')
      Text() {
        SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
          .fontSize(96)
          .renderingStrategy(SymbolRenderingStrategy.SINGLE)
          .fontColor([Color.Black, Color.Green, Color.White])
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/w-jTEpXHRoSea6o98K90nw/zh-cn_image_0000002742122737.png)
* 通过[fontWeight](../harmonyos-references/ts-basic-components-symbolspan.md#fontweight)属性设置SymbolSpan组件的粗细。

  ```typescript
  Row() {
    Column() {
      Text('Light')
      Text() {
        SymbolSpan($r('sys.symbol.ohos_trash'))
          .fontWeight(FontWeight.Lighter)
          .fontSize(96)
      }
    }

    Column() {
      Text('Normal')
      Text() {
        SymbolSpan($r('sys.symbol.ohos_trash'))
          .fontWeight(FontWeight.Normal)
          .fontSize(96)
      }
    }

    Column() {
      Text('Bold')
      Text() {
        SymbolSpan($r('sys.symbol.ohos_trash'))
          .fontWeight(FontWeight.Bold)
          .fontSize(96)
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/ZV1EF24tTcOCAu3L009ukA/zh-cn_image_0000002712243824.png)
* 通过[fontColor](../harmonyos-references/ts-basic-components-symbolspan.md#fontcolor)属性设置SymbolSpan的颜色。

  ```typescript
  Row() {
    Column() {
      Text('Black')
      Text() {
        SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
          .fontSize(96)
          .fontColor([Color.Black])
      }
    }

    Column() {
      Text('Green')
      Text() {
        SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
          .fontSize(96)
          .fontColor([Color.Green])
      }
    }

    Column() {
      Text('Pink')
      Text() {
        SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
          .fontSize(96)
          .fontColor([Color.Pink])
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/KBZbgoF5QsGpApXvIdUjcA/zh-cn_image_0000002742002777.png)
* 通过[renderingStrategy](../harmonyos-references/ts-basic-components-symbolspan.md#renderingstrategy)属性设置SymbolSpan的渲染策略。

  ```typescript
  Row() {
    Column() {
      // 请将$r('app.string.single_color')替换为实际资源文件，在本示例中该资源文件的value值为"单色"
      Text($r('app.string.single_color'));
      Text() {
        SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
          .fontSize(96)
          .renderingStrategy(SymbolRenderingStrategy.SINGLE)
          .fontColor([Color.Black, Color.Green, Color.White])
      }
    }

    Column() {
      // 请将$r('app.string.multi_color')替换为实际资源文件，在本示例中该资源文件的value值为"多色"
      Text($r('app.string.multi_color'));
      Text() {
        SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
          .fontSize(96)
          .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
          .fontColor([Color.Black, Color.Green, Color.White])
      }
    }

    Column() {
      // 请将$r('app.string.hierarchical')替换为实际资源文件，在本示例中该资源文件的value值为"分层"
      Text($r('app.string.hierarchical'));
      Text() {
        SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
          .fontSize(96)
          .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
          .fontColor([Color.Black, Color.Green, Color.White])
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Fkyr7KQUQGqMbHOl9sVvXQ/zh-cn_image_0000002712403790.png)
* 通过[effectStrategy](../harmonyos-references/ts-basic-components-symbolspan.md#effectstrategy)属性设置SymbolSpan的动效策略。

  ```typescript
  Row() {
    Column() {
      // 请将$r('app.string.no_action')替换为实际资源文件，在本示例中该资源文件的value值为"无动效"
      Text($r('app.string.no_action'));
      Text() {
        SymbolSpan($r('sys.symbol.ohos_wifi'))
          .fontSize(96)
          .effectStrategy(SymbolEffectStrategy.NONE)
      }
    }

    Column() {
      // 请将$r('app.string.overall_scaling_animation_effect')替换为实际资源文件，在本示例中该资源文件的value值为"整体缩放动效"
      Text($r('app.string.overall_scaling_animation_effect'));
      Text() {
        SymbolSpan($r('sys.symbol.ohos_wifi'))
          .fontSize(96)
          .effectStrategy(SymbolEffectStrategy.SCALE)
      }
    }

    Column() {
      // 请将$r('app.string.hierarchical_animation')替换为实际资源文件，在本示例中该资源文件的value值为"层级动效"
      Text($r('app.string.hierarchical_animation'));
      Text() {
        SymbolSpan($r('sys.symbol.ohos_wifi'))
          .fontSize(96)
          .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/wePPHKIRQxOclLntahmQ7Q/zh-cn_image_0000002742122739.gif)
* SymbolSpan不支持通用事件。

## 自定义图标动效

相较于effectStrategy属性在启动时即触发动效，可以通过以下两种方式来控制动效的播放状态，以及选择更多样化的动效策略。

关于effectStrategy属性与symbolEffect属性的多种动态属性使用及生效原则，详情请参阅[SymbolGlyph.symbolEffect](../harmonyos-references/ts-basic-components-symbolglyph.md#symboleffect12-1)属性的说明。

* 通过设置symbolEffect属性，可以同时配置SymbolGlyph的动效策略和播放状态。

  ```typescript
  @State isActive: boolean = true;
  ```

  ```typescript
  Column() {
    // 请将$r('app.string.variable_color_animation')替换为实际资源文件，在本示例中该资源文件的value值为"可变颜色动效"
    Text($r('app.string.variable_color_animation'));
    SymbolGlyph($r('sys.symbol.ohos_wifi'))
      .fontSize(96)
      .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)
    // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
    // 请将$r('app.string.on')替换为实际资源文件，在本示例中该资源文件的value值为"播放"
    Button(this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {
      this.isActive = !this.isActive;
    })
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/03BS82LZSn2d195V3AYcBg/zh-cn_image_0000002712243826.gif)
* 通过设置symbolEffect属性，可以同时指定SymbolGlyph的动画效果策略及其播放触发条件。

  ```typescript
  @State triggerValueReplace: number = 0;
  ```

  ```typescript
  Column() {
    // 请将$r('app.string.bounce_animation')替换为实际资源文件，在本示例中该资源文件的value值为"弹跳动效"
    Text($r('app.string.bounce_animation'));
    SymbolGlyph($r('sys.symbol.ellipsis_message_1'))
      .fontSize(96)
      .fontColor([Color.Gray])
      .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE, EffectDirection.UP),
                    this.triggerValueReplace)
    Button('trigger').onClick(() => {
      this.triggerValueReplace = this.triggerValueReplace + 1;
    })
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/AXjI_DaCRLWFL7h3p1cYhA/zh-cn_image_0000002742002779.gif)
* 从API version 20开始，支持通过设置symbolEffect属性为[ReplaceSymbolEffect](../harmonyos-references/ts-basic-components-symbolglyph.md#replacesymboleffect12)，设置[ReplaceEffectType](../harmonyos-references/ts-basic-components-symbolglyph.md#replaceeffecttype20枚举说明)为ReplaceEffectType.SLASH\_OVERLAY，可以指定SymbolGlyph的禁用动画效果及其播放触发条件。

  ```typescript
  @State triggerValueReplace: number = 0;
  replaceFlag: boolean = true;
  @State renderMode: number = 1;
  ```

  ```typescript
  Column() {
    // 请将$r('app.string.disable_animation')替换为实际资源文件，在本示例中该资源文件的value值为"禁用动效"
    Text($r('app.string.disable_animation'));
    SymbolGlyph(this.replaceFlag ? $r('sys.symbol.eye_slash') : $r('sys.symbol.eye'))
      .fontSize(96)
      .renderingStrategy(this.renderMode)
      .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH_OVERLAY),
                    this.triggerValueReplace)
    Button('trigger').onClick(() => {
      this.replaceFlag = !this.replaceFlag;
      this.triggerValueReplace = this.triggerValueReplace + 1;
    })
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/tyl3Uca0S3yjfr8dDy-czw/zh-cn_image_0000002712403792.gif)
* 从API version 20开始，支持通过设置symbolEffect属性为[ReplaceSymbolEffect](../harmonyos-references/ts-basic-components-symbolglyph.md#replacesymboleffect12)，设置[ReplaceEffectType](../harmonyos-references/ts-basic-components-symbolglyph.md#replaceeffecttype20枚举说明)为ReplaceEffectType.CROSS\_FADE，可以指定SymbolGlyph的快速替换动画效果及其播放触发条件。

  ```typescript
  @State triggerValueReplace: number = 0;
  replaceFlag: boolean = true;
  ```

  ```typescript
  Column() {
    // 请将$r('app.string.quick_replacement_animation')替换为实际资源文件，在本示例中该资源文件的value值为"快速替换动效"
    Text($r('app.string.quick_replacement_animation'));
    SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))
      .fontSize(96)
      .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS_FADE),
                    this.triggerValueReplace)
    Button('trigger').onClick(() => {
      this.replaceFlag = !this.replaceFlag;
      this.triggerValueReplace = this.triggerValueReplace + 1;
    })
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/QeoAUrCtTJ6KxejFs3IhGQ/zh-cn_image_0000002742122741.gif)

## 设置阴影和渐变色

* 从API version 20开始，支持通过[symbolShadow](../harmonyos-references/ts-basic-components-symbolglyph.md#symbolshadow20)接口为SymbolGlyph组件设置阴影效果。

  ```typescript
  @State isActive: boolean = true;

  options: ShadowOptions = {
    radius: 10.0,
    color: Color.Blue,
    offsetX: 10,
    offsetY: 10,
  };
  ```

  ```typescript
  Column() {
    // 请将$r('app.string.shadow_ability')替换为实际资源文件，在本示例中该资源文件的value值为"阴影能力"
    Text($r('app.string.shadow_ability'));
    SymbolGlyph($r('sys.symbol.ohos_wifi'))
      .fontSize(96)
      .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), !this.isActive)
      .symbolShadow(this.options)
    // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
    // 请将$r('app.string.on')替换为实际资源文件，在本示例中该资源文件的value值为"播放"
    Button(!this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {
      this.isActive = !this.isActive;
    })
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/YbWSYSyyQ3-8m9tijBwPJw/zh-cn_image_0000002712243828.gif)
* 从API version 20开始，支持通过[shaderStyle](../harmonyos-references/ts-basic-components-symbolglyph.md#shaderstyle20)接口为SymbolGlyph组件设置渐变色效果。

  ```typescript
  radialGradientOptions: RadialGradientOptions = {
    center: ['50%', '50%'],
    radius: '20%',
    colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],
    repeating: true,
  };
  ```

  ```typescript
  Column() {
    // 请将$r('app.string.radial_gradient')替换为实际资源文件，在本示例中该资源文件的value值为"径向渐变"
    Text($r('app.string.radial_gradient'))
      .fontSize(18)
      .fontColor(0xCCCCCC)
      .textAlign(TextAlign.Center)
    SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
      .fontSize(96)
      .shaderStyle([new RadialGradientStyle(this.radialGradientOptions)])
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ngL8r6_HQ5mvsWN6xqxbYg/zh-cn_image_0000002742002781.jpg)

## 添加事件

SymbolGlyph组件可以添加通用事件，例如绑定[onClick](../harmonyos-references/ts-universal-events-click.md#onclick)、[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)等事件来响应操作。

```typescript
@State wifiColor: ResourceColor = Color.Black;
```

```typescript
SymbolGlyph($r('sys.symbol.ohos_wifi'))
  .fontSize(96)
  .fontColor([this.wifiColor])
  .onClick(() => {
    this.wifiColor = Color.Gray;
  })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/v6sqII0DS_2v-F-xwyKsaA/zh-cn_image_0000002712403794.gif)

## 场景示例

该示例通过symbolEffect、fontSize、fontColor属性展示了播放列表的效果。

```typescript
// resourceGetString封装工具，从资源中获取字符串
import resourceGetString from '../../common/resource';

@Entry
@Component
struct SymbolMusicDemo {
  @State triggerValueReplace: number = 0;
  @State symbolSources: Resource[] =
    [$r('sys.symbol.repeat'), $r('sys.symbol.repeat_1'), $r('sys.symbol.arrow_left_arrow_right')];
  @State symbolSourcesIndex: number = 0;
  @State symbolText: string[] = [
    // 请将$r('app.string.play_in_order')替换为实际资源文件，在本示例中该资源文件的value值为"顺序播放"
    resourceGetString.resourceToString($r('app.string.play_in_order')),
    // 请将$r('app.string.play_in_single_repeat')替换为实际资源文件，在本示例中该资源文件的value值为"单曲循环"
    resourceGetString.resourceToString($r('app.string.play_in_single_repeat')),
    // 请将$r('app.string.shuffle_play')替换为实际资源文件，在本示例中该资源文件的value值为"随机播放"
    resourceGetString.resourceToString($r('app.string.shuffle_play')),
  ];
  @State symbolTextIndex: number = 0;
  @State fontColorValue: ResourceColor = Color.Grey;
  @State fontColorValue1: ResourceColor = '#E8E8E8';

  build() {
    Column({ space: 10 }) {
      Row() {
        Text() {
          // 请将$r('app.string.current_playlist')替换为实际资源文件，在本示例中该资源文件的value值为"当前播放列表"
          Span(resourceGetString.resourceToString($r('app.string.current_playlist')))
            .fontSize(20)
            .fontWeight(FontWeight.Bolder)
          Span('（101）')
        }
      }

      Row() {
        Row({ space: 5 }) {
          SymbolGlyph(this.symbolSources[this.symbolSourcesIndex])
            .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE), this.triggerValueReplace)
            .fontSize(20)
            .fontColor([this.fontColorValue])
          Text(this.symbolText[this.symbolTextIndex])
            .fontColor(this.fontColorValue)
        }
        .onClick(() => {
          this.symbolTextIndex++;
          this.symbolSourcesIndex++;
          this.triggerValueReplace++;
          if (this.symbolSourcesIndex > (this.symbolSources.length - 1)) {
            this.symbolSourcesIndex = 0;
            this.triggerValueReplace = 0;
          }
          if (this.symbolTextIndex > (this.symbolText.length - 1)) {
            this.symbolTextIndex = 0;
          }
        })
        .width('75%')

        Row({ space: 5 }) {
          Text() {
            SymbolSpan($r('sys.symbol.arrow_down_circle_badge_vip_circle_filled'))
              .fontColor([this.fontColorValue])
              .fontSize(20)
          }

          Text() {
            SymbolSpan($r('sys.symbol.heart_badge_plus'))
              .fontColor([this.fontColorValue])
              .fontSize(20)
          }

          Text() {
            SymbolSpan($r('sys.symbol.ohos_trash'))
              .fontColor([this.fontColorValue])
              .fontSize(20)
          }
        }
        .width('25%')
      }

      Divider().color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲一"
          Text($r('app.string.song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song_again')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲二"
          Text($r('app.string.song_again'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.again_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲三"
          Text($r('app.string.again_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song_repeat')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲四"
          Text($r('app.string.song_repeat'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.repeat_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲五"
          Text($r('app.string.repeat_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.song_play')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲六"
          Text($r('app.string.song_play'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().color(this.fontColorValue1).width('98%')
      Row() {
        Row() {
          // 请将$r('app.string.play_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲七"
          Text($r('app.string.play_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Column() {
        // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
        Text($r('app.string.off'))
      }
      .alignItems(HorizontalAlign.Center)
      .width('98%')
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
    .height(400)
    .padding({
      left: 10,
      top: 10
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/havUaGu5SWKLtlmjQtTaKA/zh-cn_image_0000002742122743.gif)
