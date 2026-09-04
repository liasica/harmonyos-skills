---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-transition
title: 转场样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 转场样式
category: harmonyos-references
scraped_at: 2026-09-05T06:17:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6065d9e55976befe6fe1a5eea987fe91a184877d33b73195c82573ec3d806df2
---

**说明** 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 共享元素转场

### 属性

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| shareid | string | 无 | 进行共享元素转场时使用，若不配置，则转场样式不生效。共享元素转场当前支持的组件：[list-item](js-components-container-list-item.md)、[image](js-components-basic-image.md)、[text](js-components-basic-text.md)、[button](js-components-basic-button.md)、[label](js-components-basic-label.md)。 |

### 样式

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| shared-transition-effect | string | exchange | 配置共享元素转场时的入场样式。  - exchange（默认值）：源页面元素移动到目的页元素位置，并进行适当缩放。  - static：目的页元素位置不变，用户可配置透明度动画。当前仅跳转目标页配置的static效果生效。 |
| shared-transition-name | string | - | 转场时，目的页配置的样式优先生效。该样式用于配置共享元素的动画效果，一个由@keyframes定义的动画序列，支持transform和透明度动画。若共享元素效果与自定义的动画冲突，以自定义动画为准。 |
| shared-transition-timing-function | string | friction | 转场时，目的页配置的样式优先生效。该属性定义了共享元素转场时的插值曲线。若不配置，默认使用friction曲线。 |

### 注意事项

1. 若同时配置了共享元素转场和自定义页面转场样式，页面转场效果以自定义效果为准。
2. 共享元素的exchange效果类似下图。

   **图1** 共享元素转场默认效果

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/gtyv6WbLSGeTG2biwPvqdw/zh-cn_image_0000002712246676.png)
3. 共享元素动画对元素的边框、背景色不生效。
4. 共享元素转场时，由于页面元素会被隐藏，故页面元素配置的动画样式/动画方法失效。
5. 动态修改shareid5+：若组件A的shareid被组件B的shareid覆盖，组件A的共享元素效果将失效。即使后续修改组件B的shareid，组件A的共享元素效果也不会恢复。

### 示例

PageA跳转到PageB，跳转的共享元素为image， shareid为“shareImage”。

```html
<!-- PageA -->
<!-- xxx.hml -->
<div>
  <list>
    <list-item type="description">
      <image src="item.jpg" shareid="shareImage" onclick="jump" class="shared-transition-style"></image>
    </list-item>
    <list-item>
      <text onclick="jump">Click on picture to jump to the details</text>
    </list-item>
  </list>
</div>
```

```js
// xxx.js
import router from '@ohos.router';
export default {
  jump() {
    router.push({
      // 路径要与config.json配置里面的相同
      url: 'pages/detailpage',
    });
  },
}
```

```css
/* xxx.css */
.shared-transition-style {
  shared-transition-effect: exchange;
  shared-transition-name: shared-transition;
}
@keyframes shared-transition {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

```html
<!-- PageB -->
<!-- xxx.hml -->
<div>
  <image src="itemDetail.jpg" shareid="shareImage" onclick="jumpBack" class="shared-transition-style"></image>
</div>
```

```js
// xxx.js
import router from '@ohos.router';
export default {
  jumpBack() {
    router.back();
  },
}
```

```css
/* xxx.css */
.shared-transition-style {
  shared-transition-effect: exchange;
  shared-transition-name: shared-transition;
}
@keyframes shared-transition {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

## 卡片转场样式

**说明** 

卡片转场无法和其他转场（包括共享元素转场和自定义转场）共同使用。

### 样式

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| transition-effect | string | - | 用于配置当前页面中的某个组件在卡片转场过程中是否进行转场动效，当前支持如下配置：  - unfold：配置这个属性的组件，如在卡片的上方，则向上移动一个卡片的高度，如在卡片的下方，则向下移动一个卡片的高度。  - none：转场过程中没有动效。 |

### 示例

source\_page包含顶部内容以及卡片列表，点击卡片可以跳转到target\_page。

```html
<!-- source_page -->
<!-- xxx.hml -->
<div class="container">
  <div class="outer">
    <text style="font-size: 23px; margin-bottom: 20px" >MAIN TITLE</text>
  </div>
  <list style="width:340px;height:600px;flex-direction:column;justify-content:center;align-items:center">
    <list-item type="listItem" class="item" card="true" for="list" id="{{$item.id}}" onclick="jumpPage({{$item.id}}, {{$item.url}})">
      <text style="margin-left: 10px; font-size: 23px;">{{$item.title}}</text>
    </list-item>
  </list>
</div>
```

```js
// xxx.js
import router from '@ohos.router';
export default {
  data: { list: [] },
  onInit() {
    for(var i = 0; i < 10; i++) {
      var item = { url: "pages/card_transition/target_page/index",
                   title: "this is title" + i, id: "item_" + i }
      this.list.push(item);
    }
  },
  jumpPage(id, url) {
    var cardId = this.$element(id).ref;
    router.push({ url: url, params : { ref : cardId } });
  }
}
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  background-color: #ABDAFF;
}
.item {
  height: 80px;
  background-color: #FAFAFA;
  margin-top: 2px;
}
.outer {
  width: 300px;
  height: 100px;
  align-items: flex-end;
  transition-effect: unfold;
}
```

```html
<!-- target_page -->
<!-- xxx.hml -->
<div class="container">
  <div class="div">
    <text style="font-size: 30px">this is detail</text>
  </div>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  background-color: #EBFFD7;
}
.div {
  height: 600px;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/3d8Dij3iSzCfEg7ganhuSg/zh-cn_image_0000002742005625.gif)

## 页面转场样式

### 样式

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| transition-enter | string | - | 与@keyframes配套使用，支持transform和透明度动画，详见[动画样式 表2 @keyframes属性说明](js-components-common-animation.md)。 |
| transition-exit | string | - | 与@keyframes配套使用，支持transform和透明度动画，详见[动画样式 表2 @keyframes属性说明](js-components-common-animation.md)。 |
| transition-duration | string | 跟随设备默认的页面转场时间 | 支持的单位为[s(秒)|ms(毫秒) ]，默认单位为ms，未配置时使用系统默认值。 |
| transition-timing-function | string | friction | 描述转场动画执行的速度曲线，用于使转场更为平滑。详细参数见[动画样式](js-components-common-animation.md)中“animation-timing-function”有效值说明。 |

### 注意事项

1. 配置自定义转场时，建议配置页面背景色为不透明颜色，否则在转场过程中可能会出现衔接不自然的现象。
2. transition-enter和transition-exit可单独配置，没有配置时使用系统默认的参数。
3. transition-enter/transition-exit说明如下：

   a. push场景下：进入页面栈的Page2.js应用transition-enter描述的动画配置；进入页面栈第二位置的Page1.js应用transition-exit描述的动画配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/lZlfWqjNR_yhjLMlZdiUbg/zh-cn_image_0000002712406638.png)

   b. back场景下：退出页面栈的Page2.js应用transition-enter描述的动画配置，并进行倒播；从页面栈第二位置进入栈顶位置的Page1.js应用transition-exit描述的动画配置，并进行倒播。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/c3OEkoWBRHe6cJhkfyJ1wg/zh-cn_image_0000002742125585.png)

### 示例

Page1有一个不透明盒子，点击盒子会跳转到Page2，当点击Page2中的盒子，会回退到Page1页面。

1. Page1

   ```html
   <!-- xxx.hml -->
   <div class="container">
       <text>index</text>
       <div class="move_page" onclick="jump"></div>
   </div>
   ```

   ```js
   // xxx.js
   import router from '@ohos.router';
   export default {
       data: {

       },
       jump() {
           router.push({
               url:'pages/transition2/transition2'
           })
       }
   }
   ```

   ```css
   /* xxx.css */
   .container {
       flex-direction: column;
       justify-content: center;
       align-items: center;
       width: 100%;
       height: 100%;
   }
   .move_page {
       width: 100px;
       height: 100px;
       background-color: #72d3fa;
       transition-enter: go_page;
       transition-exit: exit_page;
       transition-duration: 5s;
       transition-timing-function: friction;
   }

   @keyframes go_page {
       from {
           opacity: 0;
           transform: translate(0px) rotate(60deg) scale(1.0);
       }

       to {
           opacity: 1;
           transform: translate(100px) rotate(360deg) scale(1.0);
       }
   }
   @keyframes exit_page {
       from {
           opacity: 1;
           transform: translate(200px) rotate(60deg) scale(2);
       }

       to {
           opacity: 0;
           transform: translate(200px) rotate(360deg) scale(2);
       }
   }
   ```
2. Page2

   ```html
   <!-- xxx.hml -->
   <div class="container">
       <text>transition</text>
       <div class="move_page" onclick="jumpBack"></div>
   </div>
   ```

   ```js
   // xxx.js
   import router from '@ohos.router';
   export default {
       data: {

       },
       jumpBack() {
           router.back()
       }
   }
   ```

   ```css
   /* xxx.css */
   .container {
       flex-direction: column;
       justify-content: center;
       align-items: center;
       width: 100%;
       height: 100%;
   }

   .move_page {
       width: 100px;
       height: 100px;
       background-color: #f172fa;
       transition-enter: go_page;
       transition-exit: exit_page;
       transition-duration: 5s;
       transition-timing-function: ease;
   }

   @keyframes go_page {
       from {
           opacity: 0;
           transform:translate(100px) rotate(0deg) scale(1.0);
       }
       to {
           opacity: 1;
           transform:translate(100px) rotate(180deg) scale(2.0);
       }
   }

   @keyframes exit_page {
       from {
           opacity: 1;
           transform: translate(0px) rotate(60deg) scale(1);
       }
       to {
           opacity: 0;
           transform: translate(0px) rotate(360deg) scale(1);
       }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/YhQBIYz3SeOkB0MCl-ok9w/zh-cn_image_0000002712246678.gif)
