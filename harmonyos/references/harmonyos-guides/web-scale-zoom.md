---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-scale-zoom
title: 使用Web组件管理网页缩放
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页交互 > 使用Web组件管理网页缩放
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0dac915190d6b15be21057f63dfef33092db1ee8f18af895a094e2dd151a3dd7
---

Web组件支持手势缩放、鼠标滚轮、键盘缩放，以方便用户调整到舒适的显示大小。并对应用提供监听、控制页面缩放比例的功能，以便应用实现个性化的视觉效果。

## 启用/禁用网页缩放

### 启用/禁用网页手势缩放

通过属性[zoomAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#zoomaccess)控制网页缩放功能，当设置为false时，网页不允许手势缩放行为。

当html网页设置<meta name="viewport" id="viewport" content="user-scalable=no">时，网页不允许手势缩放。

仅当zoomAccess和viewport标签都设置为允许缩放时，才允许手势缩放。

**说明** 

在PC/2in1设备上，viewport标签不生效，仅能通过设置zoomAccess为false来禁用手势缩放。

以上方法仅能控制缩放功能的开关，但如果网页在viewport标签中设置了minimum-scale和maximum-scale，那么缩放的范围也会受到这两个属性的限制，当最大、最小值相等时，网页也是不能缩放的。

另外，网页的内容宽度也会限制缩小的比例。

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(false)
    }
  }
}
```

### 启用/禁用手势强制缩放

通过属性[forceEnableZoom](../harmonyos-references/arkts-basic-components-web-attributes.md#forceenablezoom21)控制网页强制缩放功能，当设置为true时，手势缩放行为不受minimum-scale和maximum-scale以及user-scalable=no的限制。

### 启用/禁用网页键盘鼠标缩放

ArkWeb默认支持通过Ctrl+按键'-'/'+' 或者 Ctrl+鼠标滚轮进行缩放。应用可以通过拦截键盘事件来阻止按键缩放。

通过拦截键盘事件来阻止按键缩放：

```typescript
import { webview } from '@kit.ArkWeb';
import { KeyCode } from '@kit.InputKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
        .onKeyPreIme((event) => {
          if (event.type === KeyType.Down &&
          event.getModifierKeyState &&
          event.getModifierKeyState(['Ctrl']) &&
            (event.keyCode === KeyCode.KEYCODE_MINUS || event.keyCode === KeyCode.KEYCODE_EQUALS ||
              event.keyCode === KeyCode.KEYCODE_NUMPAD_SUBTRACT || event.keyCode === KeyCode.KEYCODE_NUMPAD_ADD)) {
            return true;
          }
          return false;
        })
    }
  }
}
```

或者通过属性[zoomControlAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#zoomcontrolaccess22)设置是否允许通过组合按键（Ctrl+'-/+'或Ctrl+鼠标滚轮/触摸板）进行缩放。

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomControlAccess(false)
    }
  }
}
```

## 监听页面缩放比例变化

应用可以通过[onScaleChange](../harmonyos-references/arkts-basic-components-web-events.md#onscalechange9)接口监听页面缩放比例的变化。该接口事件对应手势事件（双指缩放），event.newScale对应网页属性visualViewport.scale。

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onScaleChange((event) => {
          console.info('onScaleChange changed from ' + event.oldScale + ' to ' + event.newScale);
        })
    }
  }
}
```

## 控制网页的缩放比例

应用可以通过设置[initialScale](../harmonyos-references/arkts-basic-components-web-attributes.md#initialscale9)属性设置页面初始缩放比例。

应用可以通过[zoom](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoom)、[zoomIn](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoomin)、[zoomOut](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoomout)接口控制页面缩放。

**说明** 

使用以上接口控制页面缩放时，必须设置属性zoomAccess为true。zoomAccess为false时，zoom类接口会抛出异常17100004。

### 以固定比例缩放页面

zoomIn将当前网页进行放大，比例为25%；zoomOut将当前网页进行缩小，比例为20%。

```typescript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Button('zoomIn')
        .onClick(() => {
          try {
            this.controller.zoomIn();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('zoomOut')
        .onClick(() => {
          try {
            this.controller.zoomOut();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
    }
  }
}
```

### 根据输入值控制页面缩放比例:

zoom基于当前网页比例进行缩放，入参要求大于0，当入参为1时为默认加载网页的缩放比例，入参小于1为缩小，入参大于1为放大。

```typescript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State factor: number = 1;

  build() {
    Column() {
      TextInput()
        .type(InputType.NUMBER_DECIMAL)
        .onChange((value)=>{
          this.factor = Number(value);
        })
      Button('zoom')
        .onClick(() => {
          try {
            this.controller.zoom(this.factor);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/g2quXkrlQJmyMlJGA1wWzA/zh-cn_image_0000002736433217.gif)

### 缩放页面到目标比例:

通过onScaleChange接口，应用可以得知当前网页的缩放比例，配合zoom接口即可实现将页面缩放至指定比例的功能。根据当前页面缩放比例pageFactor和目标比例targetFactor计算zoom入参的公式为：

```typescript
factor = 100 * targetFactor / pageFactor
```

```typescript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State targetFactor: number = 1;
  // This represents the page zoom level
  @State pageFactor: number = 100;
  // Represents the integer 100
  intNumber: number = 100;

  build() {
    Column() {
      TextInput()
        .type(InputType.NUMBER_DECIMAL)
        .onChange((value)=>{
          this.targetFactor = Number(value);
        })
      Button('zoom')
        .onClick(() => {
          try {
            let factor = this.targetFactor * this.intNumber / this.pageFactor;
            this.controller.zoom(factor);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
        .onScaleChange((event) => {
          console.info('onScaleChange changed from ' + event.oldScale + ' to ' + event.newScale);
          this.pageFactor = event.newScale;
        })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/esDEaKyaTU-aXhTWE04gzg/zh-cn_image_0000002706834062.gif)
