---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-663
title: 应用退出到后台如何正确自动启动画中画
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 应用退出到后台如何正确自动启动画中画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:e0f7edc70ba54c1ef38722917df0aa4ede31ce82b6703f7f4ad8d22abe3cf0a9
---

## 问题现象

实现应用退后台自动启动画中画窗口，在onBackground生命周期中[startPiP](../harmonyos-references/js-apis-pipwindow.md#startpip)启动画中画会偶现启动失败，那么，应用退出到后台如何正确的自动启动画中画呢？

## 背景知识

* [画中画](../harmonyos-guides/pipwindow-overview.md)：应用在视频播放、视频会议、视频通话等场景下，可以使用画中画能力将视频内容以小窗（画中画）模式呈现。切换为小窗（画中画）模式后，用户可以进行其他界面操作，提升使用体验。
* [setAutoStartEnabled](../harmonyos-references/js-apis-pipwindow.md#setautostartenabled)：基于安全考虑，应用处于后台时不允许通过startPiP启动画中画。针对应用返回后台时需要启动画中画的场景，建议使用setAutoStartEnabled(true)实现自动启动。
* [onBackground](../harmonyos-guides/uiability-lifecycle.md#onbackground)：在UIAbility的UI完全不可见之后，系统触发onBackground回调，将UIAbility实例切换至后台状态。开发者可以在该回调中释放UI不可见时的无用资源，例如停止定位功能，以节省系统的资源消耗。

## 解决方案

在应用进入后台应用会被挂起，onBackground()执行时间较短，无法提供足够的时间做一些耗时动作。[PiPWindow.create](../harmonyos-references/js-apis-pipwindow.md#pipwindowcreate)、setAutoStartEnabled应当应用在前台时就执行，因此在进入页面或者组件的时候就创建画中画窗口并将setAutoStartEnabled设置为true，在不需要自动启动画中的时候将setAutoStartEnabled设置为false。

示例代码如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { BuilderNode, FrameNode, NodeController, PiPWindow, UIContext } from '@kit.ArkUI';

class Params {
  text: string = '';

  constructor(text: string) {
    this.text = text;
  }
}

// 可以通过@Builder装饰器实现布局构建
@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(20)
      .fontColor(Color.Red);
  }
  .width('100%') // 宽度方向充满画中画窗口
  .height('100%'); // 高度方向充满画中画窗口
}

// 可通过继承NodeController实现自定义UI控制器
class TextNodeController extends NodeController {
  private message: string;
  private textNode: BuilderNode<[Params]> | null = null;

  constructor(message: string) {
    super();
    this.message = message;
  }

  // 通过BuilderNode加载自定义布局
  makeNode(context: UIContext): FrameNode | null {
    this.textNode = new BuilderNode(context);
    this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
    return this.textNode.getFrameNode();
  }

  // 可自定义该方法实现布局更新
  update(message: string) {
    console.log(`update message: ${message}`);
    if (this.textNode !== null) {
      this.textNode.update(new Params(message));
    }
  }
}

@Entry
@Component
struct Index {
  private message: string = 'Hello World';
  private pipController: PiPWindow.PiPController | undefined = undefined;
  private mXComponentController: XComponentController =
    new XComponentController(); // 应使用该mXComponentController初始化XComponent: XComponent( {id: 'video', type: 'surface', controller: mXComponentController} )，保证XComponent的内容可以被迁移到画中画窗口。
  private nodeController: TextNodeController = new TextNodeController('this is custom UI');
  private contentWidth: number = 800; // 假设当前内容宽度800px。
  private contentHeight: number = 600; // 假设当前内容高度600px。
  private para: Record<string, number> = { 'PropA': 47 };
  private localStorage: LocalStorage = new LocalStorage(this.para);
  private config: PiPWindow.PiPConfiguration = {
    context: this.getUIContext().getHostContext() as Context,
    componentController: this.mXComponentController,
    templateType: PiPWindow.PiPTemplateType.VIDEO_CALL,
    contentWidth: this.contentWidth,
    contentHeight: this.contentHeight,
    customUIController: this.nodeController, // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
    localStorage: this.localStorage, // 可选，如果需要跟踪主窗实例，可设置此参数。
  };

  aboutToAppear(): void {
    let promise: Promise<PiPWindow.PiPController> = PiPWindow.create(this.config);
    promise.then((data: PiPWindow.PiPController) => {
      this.pipController = data;
      // 开启画中画自动拉起开关
      this.pipController.setAutoStartEnabled(true);
      // 首次启动开启画中画,若不想开启,可注释掉startPiP逻辑,就会仅后台开启
      let promise: Promise<void> = this.pipController.startPiP();
      promise.then(() => {
        console.info(`Succeeded in starting pip.`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to start pip. Cause:${err.code}, message:${err.message}`);
      });
      console.info(`Succeeded in creating pip controller. Data:${data}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
    });
  }

  // 仅用于功能测试，实际开发过程中按功能需求设计组件
  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：画中画窗口的位置是否支持自定义设置？

A：暂时未开放画中画窗口位置的自定义接口，暂时无法自定义位置。

Q：使用XComponent实现画中画功能，通过contentWidth和contentHeight设置窗口大小为什么无效？

A：画中画不支持自定义窗口大小，contentWidth和contentHeight是用来确定画中画窗口比例的，系统会根据该比例自动适配窗口大小。详情请参考：[画中画窗口尺寸](../design-guides/pip-0000001927422624.md#section1282919574120)。

Q：后台启动画中画报错1300013是什么原因？

A：出现[1300013](../harmonyos-references/errorcode-window.md#section1300013-创建画中画窗口失败)报错可能是应用处于后台时不允许通过[startPiP](../harmonyos-references/js-apis-pipwindow.md#startpip)启动画中画，建议使用setAutoStartEnabled(true)实现自动启动。排查设置->智慧多窗->自动启动画中画开关是否打开。

Q：画中画退后台使用退后台前一个的Surface宽高如何确定？

A：画中画窗口的大小使用的是Surface的宽高比，和Surface渲染没有关系，给大一点或者小一点都可以渲染；XComponent管理了一个Surface负责显示，XComponent的大小和Surface是独立的，如果没有设置过Surface的大小，默认和XComponent是同步等大的。如果单独设置过Surface的大小，则XComponent就会将设置的值记录下来，大小更新的时候按照该值设置Surface；如果只是创建了Surface但没有渲染任务会导致获取不到宽高，建议主动触发一次buffer的申请，申请到之后再查询Surface宽高。
