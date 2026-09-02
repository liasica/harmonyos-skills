---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shared-element-transition
title: 共享元素转场 (一镜到底)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 转场动画 > 共享元素转场 (一镜到底)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b84210e024e4f8a88a38dc364584983777ab177ee94bdc1dc70e7d33e7c89725
---

共享元素转场是一种界面切换时对相同或者相似的两个元素做的一种位置和大小匹配的过渡动画效果，也称一镜到底动效。

如下例所示，在点击图片后，该图片消失，同时在另一个位置出现新的图片，二者之间内容相同，可以对它们添加一镜到底动效。左图为不添加一镜到底动效的效果，右图为添加一镜到底动效的效果，一镜到底的效果能够让二者的出现消失产生联动，使得内容切换过程显得灵动自然而不生硬。

| 一帧切换效果 | 一镜到底效果 |
| --- | --- |
|  |  |

一镜到底的动效有多种实现方式，在实际开发过程中，应根据具体场景选择合适的方法进行实现。

以下是不同实现方式的对比：

| 一镜到底实现方式 | 特点 | 适用场景 |
| --- | --- | --- |
| 不新建容器直接变化原容器 | 不发生路由跳转，需要在一个组件中实现展开及关闭两种状态的布局，展开后组件层级不变。 | 适用于转场开销小的简单场景，如点开页面无需加载大量数据及组件。 |
| 新建容器并跨容器迁移组件 | 通过使用[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)，将组件从一个容器迁移到另一个容器，在开始迁移时，需要根据前后两个布局的位置大小等信息对组件添加位移及缩放，确保迁移开始时组件能够对齐初始布局，避免出现视觉上的跳变现象。之后再添加动画将位移及缩放等属性复位，实现组件从初始布局到目标布局的一镜到底过渡效果。 | 适用于新建对象开销大的场景，如视频直播组件点击转为全屏等。 |
| 使用geometryTransition共享元素转场 | 利用系统能力，转场前后两个组件调用[geometryTransition](../harmonyos-references/ts-transition-animation-geometrytransition.md)接口绑定同一id，同时将转场逻辑置于[animateTo](../harmonyos-references/ts-explicit-animation.md)动画闭包内，这样系统侧会自动为二者添加一镜到底的过渡效果。 | 系统将调整绑定的两个组件的宽高及位置至相同值，并切换二者的透明度，以实现一镜到底过渡效果。因此，为了实现流畅的动画效果，需要确保对绑定geometryTransition的节点添加宽高动画不会有跳变。此方式适用于创建新节点开销小的场景。 |

## 不新建容器并直接变化原容器

该方法不新建容器，通过在已有容器上增删组件触发[transition](../harmonyos-references/ts-transition-animation-component.md)，搭配组件[属性动画](arkts-attribute-animation-apis.md)实现一镜到底效果。

对于同一个容器展开，容器内兄弟组件消失或者出现的场景，可通过对同一个容器展开前后进行宽高位置变化并配置属性动画，对兄弟组件配置出现消失转场动画实现一镜到底效果。基本步骤为：

1. 构建需要展开的页面，并通过状态变量构建好普通状态和展开状态的界面。
2. 将需要展开的页面展开，通过状态变量控制兄弟组件消失或出现，并通过绑定出现消失转场实现兄弟组件转场效果。

以点击卡片后显示卡片内容详情场景为例：

```typescript
import { common } from '@kit.AbilityKit';

class PostData {
  // 请将$r('app.media.flower')替换为实际资源文件
  avatar: Resource = $r('app.media.flower');
  name: string = '';
  message: ResourceStr = '';
  images: Resource[] = [];
}

@Entry
@Component
struct Index {
  @State isExpand: boolean = false;
  @State @Watch('onItemClicked') selectedIndex: number = -1;
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // 数组中图片均使用Resource资源，需用户自定义
  private allPostData: PostData[] = [
    {
      // 请将$r('app.media.flower')替换为实际资源文件
      avatar: $r('app.media.flower'),
      name: 'Alice',
      // 请将$r('app.string.shareTransition_text1')替换为实际资源文件，在本示例中该资源文件的value值为"天气晴朗"
      message: $r('app.string.shareTransition_text1'),
      // 请将$r('app.media.spring')替换为实际资源文件
      // 请将$r('app.media.tall_tree')替换为实际资源文件
      images: [$r('app.media.spring'), $r('app.media.tall_tree')]
    },
    {
      // 请将$r('app.media.sunset_sky')替换为实际资源文件
      avatar: $r('app.media.sunset_sky'),
      name: 'Bob',
      // 请将$r('app.string.shareTransition_text2')替换为实际资源文件，在本示例中该资源文件的value值为"你好世界"
      message: $r('app.string.shareTransition_text2'),
      // 请将$r('app.media.island')替换为实际资源文件
      images: [$r('app.media.island')]
    },
    {
      // 请将$r('app.media.tall_tree')替换为实际资源文件
      avatar: $r('app.media.tall_tree'),
      name: 'Carl',
      // 请将$r('app.string.shareTransition_text3')替换为实际资源文件，在本示例中该资源文件的value值为"万物生长"
      message: $r('app.string.shareTransition_text3'),
      // 请将$r('app.media.flower')替换为实际资源文件
      // 请将$r('app.media.sunset_sky')替换为实际资源文件
      // 请将$r('app.media.spring')替换为实际资源文件
      images: [$r('app.media.flower'), $r('app.media.sunset_sky'), $r('app.media.spring')]
    }];

  private onItemClicked(): void {
    if (this.selectedIndex < 0) {
      return;
    }
    this.getUIContext()?.animateTo({
      duration: 350,
      curve: Curve.Friction
    }, () => {
      this.isExpand = !this.isExpand;
    });
  }

  build() {
    Column({ space: 20 }) {
      ForEach(this.allPostData, (postData: PostData, index: number) => {
        // 当点击了某个post后，会使其余的post消失下树
        if (!this.isExpand || this.selectedIndex === index) {
          Column() {
            Post({ data: postData, selectedIndex: this.selectedIndex, index: index })
          }
          .width('100%')
          // 对出现消失的post添加透明度转场和位移转场效果
          .transition(TransitionEffect.OPACITY
            .combine(TransitionEffect.translate({ y: index < this.selectedIndex ? -250 : 250 }))
            .animation({ duration: 350, curve: Curve.Friction }))
        }
      }, (postData: PostData, index: number) => index.toString())
    }
    .size({ width: '100%', height: '100%' })
    .backgroundColor('#40808080')
  }
}

@Component
export default struct Post {
  @Link selectedIndex: number;
  @Prop data: PostData;
  @Prop index: number;
  @State itemHeight: number = 250;
  @State isExpand: boolean = false;
  @State expandImageSize: number = 100;
  @State avatarSize: number = 50;

  build() {
    Column({ space: 20 }) {
      Row({ space: 10 }) {
        Image(this.data.avatar)
          .size({ width: this.avatarSize, height: this.avatarSize })
          .borderRadius(this.avatarSize / 2)
          .clip(true)

        Text(this.data.name)
      }
      .justifyContent(FlexAlign.Start)

      Text(this.data.message)

      Row({ space: 15 }) {
        ForEach(this.data.images, (imageResource: Resource, index: number) => {
          Image(imageResource)
            .size({ width: this.expandImageSize, height: this.expandImageSize })
        }, (imageResource: Resource, index: number) => index.toString())
      }

      // 展开态下组件增加的内容
      if (this.isExpand) {
        Column() {
          // 请将$r('app.string.shareTransition_text4')替换为实际资源文件，在本示例中该资源文件的value值为"评论区"
          Text($r('app.string.shareTransition_text4'))
          // 对评论区文本添加出现消失转场效果
            .transition(TransitionEffect.OPACITY
              .animation({ duration: 350, curve: Curve.Friction }))
            .padding({ top: 10 })
        }
        .transition(TransitionEffect.asymmetric(
          TransitionEffect.opacity(0.99)
            .animation({ duration: 350, curve: Curve.Friction }),
          TransitionEffect.OPACITY.animation({ duration: 0 })
        ))
        .size({ width: '100%' })
      }
    }
    .backgroundColor(Color.White)
    .size({ width: '100%', height: this.itemHeight })
    .alignItems(HorizontalAlign.Start)
    .padding({ left: 10, top: 10 })
    .onClick(() => {
      this.selectedIndex = -1;
      this.selectedIndex = this.index;
      this.getUIContext()?.animateTo({
        duration: 350,
        curve: Curve.Friction
      }, () => {
        // 对展开的post做宽高动画，并对头像尺寸和图片尺寸加动画
        this.isExpand = !this.isExpand;
        this.itemHeight = this.isExpand ? 780 : 250;
        this.avatarSize = this.isExpand ? 75 : 50;
        this.expandImageSize = (this.isExpand && this.data.images.length > 0)
          ? (360 - (this.data.images.length + 1) * 15) / this.data.images.length : 100;
      })
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/9I4UbrP3SJiIf_0mH0qqAA/zh-cn_image_0000002706833780.gif)

## 新建容器并跨容器迁移组件

通过[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)[自定义占位节点](arkts-user-defined-place-holder.md)，利用[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)实现组件的跨节点迁移，配合属性动画给组件的迁移过程赋予一镜到底效果。这种一镜到底的实现方式可以结合多种转场方式使用，如导航转场（[Navigation](../harmonyos-references/ts-basic-components-navigation.md)）、半模态转场（[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)）等。

### 结合Stack使用

可以利用Stack内后定义组件位于最上方的特性，控制组件在跨节点迁移后的顺序位置最高。以展开收起卡片的场景为例，实现步骤为：

* 展开卡片时，获取被点击卡片A的位置信息，将被点击卡片A迁移到与卡片A位置一致的展开页B处，展开页B的层级高于被点击卡片A的层级。
* 对展开页B添加属性动画，使之展开并运动到展开后的位置，完成一镜到底的动画效果。
* 收起卡片时，对展开页B添加属性动画，使之收起并运动到收起时的位置，即被点击卡片A的位置，实现一镜到底的动画效果。
* 在动画结束回调函数中将展开页B中的组件迁移回被点击卡片A处。

```typescript
// Index.ets
import { createPostNode, getPostNode, PostNode } from './PostNode';
import { componentUtils, curves, UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  // 新建一镜到底动画类
  private uiContext: UIContext = this.getUIContext();
  @State animationProperties: AnimationProperties = new AnimationProperties(this.uiContext);
  private listArray: Array<number> = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  build() {
    // 卡片折叠态，展开态的共同父组件
    Stack() {
      List({ space: 20 }) {
        ForEach(this.listArray, (item: number) => {
          ListItem() {
            // 卡片折叠态
            PostItem({ index: item, animationProperties: this.animationProperties })
          }
        })
      }
      .clip(false)
      .alignListItem(ListItemAlign.Center)

      if (this.animationProperties.isExpandPageShow) {
        // 卡片展开态
        ExpandPage({ animationProperties: this.animationProperties })
      }
    }
    .key('rootStack')
    .enabled(this.animationProperties.isEnabled)
  }
}

@Component
struct PostItem {
  @Prop index: number
  @Link animationProperties: AnimationProperties;
  @State nodeController: PostNode | undefined = undefined;
  // 折叠时详细内容隐藏
  private showDetailContent: boolean = false;

  aboutToAppear(): void {
    this.nodeController = createPostNode(this.getUIContext(), this.index.toString(), this.showDetailContent);
    if (this.nodeController != undefined) {
      // 设置回调，当卡片从展开态回到折叠态时触发
      this.nodeController.setCallback(this.resetNode.bind(this));
    }
  }

  resetNode() {
    this.nodeController = getPostNode(this.index.toString());
  }

  build() {
    Stack() {
      NodeContainer(this.nodeController)
    }
    .width('100%')
    .height(100)
    .key(this.index.toString())
    .onClick(() => {
      if (this.nodeController != undefined) {
        // 卡片从折叠态节点下树
        this.nodeController.onRemove();
      }
      // 触发卡片从折叠到展开态的动画
      this.animationProperties.expandAnimation(this.index);
    })
  }
}

@Component
struct ExpandPage {
  @Link animationProperties: AnimationProperties;
  @State nodeController: PostNode | undefined = undefined;
  // 展开时详细内容出现
  private showDetailContent: boolean = true;

  aboutToAppear(): void {
    // 获取对应序号的卡片组件
    this.nodeController = getPostNode(this.animationProperties.curIndex.toString());
    // 更新为详细内容出现
    this.nodeController?.update(this.animationProperties.curIndex.toString(), this.showDetailContent);
  }

  build() {
    Stack() {
      NodeContainer(this.nodeController)
    }
    .width('100%')
    .height(this.animationProperties.changedHeight ? '100%' : 100)
    .translate({ x: this.animationProperties.translateX, y: this.animationProperties.translateY })
    .position({ x: this.animationProperties.positionX, y: this.animationProperties.positionY })
    .onClick(() => {
      this.getUIContext()?.animateTo({
        curve: curves.springMotion(0.6, 0.9),
        onFinish: () => {
          if (this.nodeController != undefined) {
            // 执行回调，折叠态节点获取卡片组件
            this.nodeController.callCallback();
            // 当前展开态节点的卡片组件下树
            this.nodeController.onRemove();
          }
          // 卡片展开态节点下树
          this.animationProperties.isExpandPageShow = false;
          this.animationProperties.isEnabled = true;
        }
      }, () => {
        // 卡片从展开态回到折叠态
        this.animationProperties.isEnabled = false;
        this.animationProperties.translateX = 0;
        this.animationProperties.translateY = 0;
        this.animationProperties.changedHeight = false;
        // 更新为详细内容消失
        this.nodeController?.update(this.animationProperties.curIndex.toString(), false);
      })
    })
  }
}

class RectInfo {
  left: number = 0;
  top: number = 0;
  right: number = 0;
  bottom: number = 0;
  width: number = 0;
  height: number = 0;
}

// 封装的一镜到底动画类
@Observed
class AnimationProperties {
  public isExpandPageShow: boolean = false;
  // 控制组件是否响应点击事件
  public isEnabled: boolean = true;
  // 展开卡片的序号
  public curIndex: number = -1;
  public translateX: number = 0;
  public translateY: number = 0;
  public positionX: number = 0;
  public positionY: number = 0;
  public changedHeight: boolean = false;
  private calculatedTranslateX: number = 0;
  private calculatedTranslateY: number = 0;
  // 设置卡片展开后相对父组件的位置
  private expandTranslateX: number = 0;
  private expandTranslateY: number = 0;
  private uiContext: UIContext;

  constructor(uiContext: UIContext) {
    this.uiContext = uiContext
  }

  public expandAnimation(index: number): void {
    // 记录展开态卡片的序号
    if (index != undefined) {
      this.curIndex = index;
    }
    // 计算折叠态卡片相对父组件的位置
    this.calculateData(index.toString());
    // 展开态卡片上树
    this.isExpandPageShow = true;
    // 卡片展开的属性动画
    this.uiContext?.animateTo({
      curve: curves.springMotion(0.6, 0.9)
    }, () => {
      this.translateX = this.calculatedTranslateX;
      this.translateY = this.calculatedTranslateY;
      this.changedHeight = true;
    })
  }

  // 获取需要跨节点迁移的组件的位置，及迁移前后节点的公共父节点的位置，用以计算做动画组件的动画参数
  public calculateData(key: string): void {
    let clickedImageInfo = this.getRectInfoById(this.uiContext, key);
    let rootStackInfo = this.getRectInfoById(this.uiContext, 'rootStack');
    this.positionX = this.uiContext.px2vp(clickedImageInfo.left - rootStackInfo.left);
    this.positionY = this.uiContext.px2vp(clickedImageInfo.top - rootStackInfo.top);
    this.calculatedTranslateX = this.uiContext.px2vp(rootStackInfo.left - clickedImageInfo.left) +
      this.expandTranslateX;
    this.calculatedTranslateY = this.uiContext.px2vp(rootStackInfo.top - clickedImageInfo.top) + this.expandTranslateY;
  }

  // 根据组件的id获取组件的位置信息
  private getRectInfoById(context: UIContext, id: string): RectInfo {
    let componentInfo: componentUtils.ComponentInfo = context.getComponentUtils().getRectangleById(id);

    if (!componentInfo) {
      throw Error('object is empty');
    }

    let rstRect: RectInfo = new RectInfo();
    const widthScaleGap = componentInfo.size.width * (1 - componentInfo.scale.x) / 2;
    const heightScaleGap = componentInfo.size.height * (1 - componentInfo.scale.y) / 2;
    rstRect.left = componentInfo.translate.x + componentInfo.windowOffset.x + widthScaleGap;
    rstRect.top = componentInfo.translate.y + componentInfo.windowOffset.y + heightScaleGap;
    rstRect.right =
      componentInfo.translate.x + componentInfo.windowOffset.x + componentInfo.size.width - widthScaleGap;
    rstRect.bottom =
      componentInfo.translate.y + componentInfo.windowOffset.y + componentInfo.size.height - heightScaleGap;
    rstRect.width = rstRect.right - rstRect.left;
    rstRect.height = rstRect.bottom - rstRect.top;

    return {
      left: rstRect.left,
      right: rstRect.right,
      top: rstRect.top,
      bottom: rstRect.bottom,
      width: rstRect.width,
      height: rstRect.height
    }
  }
}
```

```typescript
// PostNode.ets
// 跨容器迁移能力
import { UIContext, curves, NodeController, BuilderNode, FrameNode } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

class Data {
  public item: string | null = null;
  public isExpand: boolean = false;
}
let context: undefined | common.UIAbilityContext = undefined;
@Builder
function postBuilder(data: Data) {
  // 跨容器迁移组件置于@Builder内
  Column() {
    Row() {
      Row()
        .backgroundColor(Color.Pink)
        .borderRadius(20)
        .width(80)
        .height(80)
      Column() {
        // 请在resources\base\element\string.json文件中配置name为'shareTransition_text5'，value为非空字符串的资源
        Text((context as common.UIAbilityContext)?.resourceManager.getStringByNameSync('shareTransition_text5') + data.item)
          .fontSize(20)
        // 请将$r('app.string.shareTransition_text6')替换为实际资源文件，在本示例中该资源文件的value值为"共享元素转场"
        Text($r('app.string.shareTransition_text6'))
          .fontSize(12)
          .fontColor(0x909399)
      }
      .alignItems(HorizontalAlign.Start)
      .justifyContent(FlexAlign.SpaceAround)
      .margin({ left: 10 })
      .height(80)
    }
    .width('90%')
    .height(100)

    // 展开后显示细节内容
    if (data.isExpand) {
      Row() {
        // 请将$r('app.string.shareTransition_text7')替换为实际资源文件，在本示例中该资源文件的value值为"展开态"
        Text($r('app.string.shareTransition_text7'))
          .fontSize(28)
          .fontColor(0x909399)
          .textAlign(TextAlign.Center)
          .transition(TransitionEffect.OPACITY.animation({ curve: curves.springMotion(0.6, 0.9) }))
      }
      .width('90%')
      .justifyContent(FlexAlign.Center)
    }
  }
  .width('90%')
  .height('100%')
  .alignItems(HorizontalAlign.Center)
  .borderRadius(10)
  .margin({ top: 15 })
  .backgroundColor(Color.White)
  .shadow({
    radius: 20,
    color: 0x909399,
    offsetX: 20,
    offsetY: 10
  })
}

class InternalValue {
  public flag: boolean = false;
};

export class PostNode extends NodeController {
  private node: BuilderNode<Data[]> | null = null;
  private isRemove: InternalValue = new InternalValue();
  private callback: Function | undefined = undefined;
  private data: Data | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.isRemove.flag === true) {
      return null;
    }
    if (this.node != null) {
      return this.node.getFrameNode();
    }

    return null;
  }

  init(uiContext: UIContext, id: string, isExpand: boolean) {
    if (this.node != null) {
      return;
    }
    // 创建节点，需要uiContext
    this.node = new BuilderNode(uiContext);
    context = uiContext.getHostContext() as common.UIAbilityContext;
    // 创建离线组件
    this.data = { item: id, isExpand: isExpand };
    this.node.build(wrapBuilder<Data[]>(postBuilder), this.data);
  }

  update(id: string, isExpand: boolean) {
    if (this.node !== null) {
      // 调用update进行更新。
      this.data = { item: id, isExpand: isExpand };
      this.node.update(this.data);
    }
  }

  setCallback(callback: Function | undefined) {
    this.callback = callback;
  }

  callCallback() {
    if (this.callback != undefined) {
      this.callback();
    }
  }

  onRemove() {
    this.isRemove.flag = true;
    // 组件迁移出节点时触发重建
    this.rebuild();
    this.isRemove.flag = false;
  }
}

let gNodeMap: Map<string, PostNode | undefined> = new Map();

export const createPostNode =
  (uiContext: UIContext, id: string, isExpand: boolean): PostNode | undefined => {
    let node = new PostNode();
    node.init(uiContext, id, isExpand);
    gNodeMap.set(id, node);
    return node;
  }

export const getPostNode = (id: string): PostNode | undefined => {
  if (!gNodeMap.has(id)) {
    return undefined;
  }
  return gNodeMap.get(id);
}

export const deleteNode = (id: string) => {
  gNodeMap.delete(id);
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/RUK2x85yQB-QBqy_69hPcw/zh-cn_image_0000002736312889.gif)

### 结合Navigation使用

可以利用[Navigation](../harmonyos-references/ts-basic-components-navigation.md)的自定义导航转场动画能力（[customNavContentTransition](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)，可参考Navigation[示例3](../harmonyos-references/ts-basic-components-navigation.md#示例3设置可交互转场动画)）实现一镜到底动效。共享元素转场期间，组件由消失页面迁移至出现页面。

以展开收起缩略图的场景为例，实现步骤为：

* 通过customNavContentTransition配置PageOne与PageTwo的自定义导航转场动画。
* 自定义的共享元素转场效果由属性动画实现，具体实现方式为抓取页面内组件相对窗口的位置信息从而正确匹配组件在PageOne与PageTwo的位置、缩放等，即动画开始和结束的属性信息。
* 点击缩略图后共享元素组件从PageOne被迁移至PageTwo，随后触发由PageOne至PageTwo的自定义转场动画，即PageTwo的共享元素组件从原来的缩略图状态做动画到全屏状态。
* 由全屏状态返回到缩略图时，触发由PageTwo至PageOne的自定义转场动画，即PageTwo的共享元素组件从全屏状态做动画到原PageOne的缩略图状态，转场结束后共享元素组件从PageTwo被迁移回PageOne。

```txt
├──entry/src/main/ets                 // 代码区
│  ├──CustomTransition
│  │  ├──AnimationProperties.ets      // 一镜到底转场动画封装
│  │  └──CustomNavigationUtils.ets    // Navigation自定义转场动画配置
│  ├──entryability
│  │  └──EntryAbility.ets             // 程序入口类
│  ├──NodeContainer
│  │  └──CustomComponent.ets          // 自定义占位节点
│  ├──pages
│  │  ├──Index.ets                    // 导航页面
│  │  ├──PageOne.ets                  // 缩略图页面
│  │  └──PageTwo.ets                  // 全屏展开页面
│  └──utils
│     ├──ComponentAttrUtils.ets       // 组件位置获取
│     └──WindowUtils.ets              // 窗口信息
└──entry/src/main/resources           // 资源文件
```

```typescript
// Index.ets
import { AnimateCallback, CustomTransition } from '../../../CustomTransition/CustomNavigationUtils';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'Index';
const DOMAIN = 0xF811;

@Entry
@Component
struct Index {
  private pageInfos: NavPathStack = new NavPathStack();
  // 允许进行自定义转场的页面名称
  private allowedCustomTransitionFromPageName: string[] = ['PageOne'];
  private allowedCustomTransitionToPageName: string[] = ['PageTwo'];

  aboutToAppear(): void {
    this.pageInfos.pushPath({ name: 'PageOne' });
  }

  private isCustomTransitionEnabled(fromName: string, toName: string): boolean {
    // 点击和返回均需要进行自定义转场，因此需要分别判断
    if ((this.allowedCustomTransitionFromPageName.includes(fromName) &&
      this.allowedCustomTransitionToPageName.includes(toName)) ||
      (this.allowedCustomTransitionFromPageName.includes(toName) &&
      this.allowedCustomTransitionToPageName.includes(fromName))) {
      return true;
    }
    return false;
  }

  build() {
    Navigation(this.pageInfos)
      .hideNavBar(true)
      .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
        if ((!from || !to) || (!from.name || !to.name)) {
          return undefined;
        }

        // 通过from和to的name对自定义转场路由进行管控
        if (!this.isCustomTransitionEnabled(from.name, to.name)) {
          return undefined;
        }

        // 需要对转场页面是否注册了animation进行判断，来决定是否进行自定义转场
        let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.index);
        let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.index);
        if (!fromParam.animation || !toParam.animation) {
          return undefined;
        }

        // 一切判断完成后，构造customAnimation给系统侧调用，执行自定义转场动画
        let customAnimation: NavigationAnimatedTransition = {
          onTransitionEnd: (isSuccess: boolean) => {
            hilog.info(DOMAIN, 'current transition result is', 'isSuccess: %s', isSuccess.toString());
          },
          timeout: 2000,
          transition: (transitionProxy: NavigationTransitionProxy) => {
            hilog.info(DOMAIN, TAG, 'trigger transition callback');
            if (fromParam.animation) {
              fromParam.animation(operation === NavigationOperation.PUSH, true, transitionProxy);
            }
            if (toParam.animation) {
              toParam.animation(operation === NavigationOperation.PUSH, false, transitionProxy);
            }
          }
        };
        return customAnimation;
      })
  }
}
```

```typescript
// PageOne.ets
import { CustomTransition } from '../../../CustomTransition/CustomNavigationUtils';
import { MyNodeController, createMyNode, getMyNode } from '../../../NodeContainer/CustomComponent';
import { ComponentAttrUtils, RectInfoInPx } from '../../../utils/ComponentAttrUtils';
import { WindowUtils } from '../../../utils/WindowUtils';

@Builder
export function PageOneBuilder() {
  PageOne();
}

@Component
export struct PageOne {
  private pageInfos: NavPathStack = new NavPathStack();
  private pageId: number = -1;
  @State myNodeController: MyNodeController | undefined = new MyNodeController(false);

  aboutToAppear(): void {
    let node = getMyNode();
    if (node === undefined) {
      // 新建自定义节点
      createMyNode(this.getUIContext());
    }
    this.myNodeController = getMyNode();
  }

  private doFinishTransition(): void {
    // PageTwo结束转场时将节点从PageTwo迁移回PageOne
    this.myNodeController = getMyNode();
  }

  private registerCustomTransition(): void {
    // 注册自定义动画协议
    CustomTransition.getInstance().registerNavParam(this.pageId,
      (isPush: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => {
      }, 500);
  }

  private onCardClicked(): void {
    let cardItemInfo: RectInfoInPx =
      ComponentAttrUtils.getRectInfoById(WindowUtils.window.getUIContext(), 'card');
    let param: Record<string, Object> = {};
    param['cardItemInfo'] = cardItemInfo;
    param['doDefaultTransition'] = (myController: MyNodeController) => {
      this.doFinishTransition();
    };
    this.pageInfos.pushPath({ name: 'PageTwo', param: param });
    // 自定义节点从PageOne下树
    if (this.myNodeController != undefined) {
      (this.myNodeController as MyNodeController).onRemove();
    }
  }

  build() {
    NavDestination() {
      Stack() {
        Column({ space: 20 }) {
          Row({ space: 10 }) {
            // 请将$r('app.media.avatar')替换为实际资源文件
            Image($r('app.media.avatar'))
              .size({ width: 50, height: 50 })
              .borderRadius(25)
              .clip(true)

            Text('Alice')
          }
          .justifyContent(FlexAlign.Start)

          // 请将$r('app.string.shareTransition_text2')替换为实际资源文件，在本示例中该资源文件的value值为"你好世界"
          Text($r('app.string.shareTransition_text2'))

          NodeContainer(this.myNodeController)
            .size({ width: 320, height: 250 })
            .onClick(() => {
              this.onCardClicked();
            })
        }
        .alignItems(HorizontalAlign.Start)
        .margin(30)
      }
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.pageId = this.pageInfos.getAllPathName().length - 1;
      this.registerCustomTransition();
    })
    .onDisAppear(() => {
      CustomTransition.getInstance().unRegisterNavParam(this.pageId);
      // 自定义节点从PageOne下树
      if (this.myNodeController != undefined) {
        (this.myNodeController as MyNodeController).onRemove();
      }
    })
  }
}
```

```typescript
// PageTwo.ets
import { CustomTransition } from '../../../CustomTransition/CustomNavigationUtils';
import { AnimationProperties } from '../../../CustomTransition/AnimationProperties';
import { RectInfoInPx } from '../../../utils/ComponentAttrUtils';
import { getMyNode, MyNodeController } from '../../../NodeContainer/CustomComponent';

@Builder
export function PageTwoBuilder() {
  PageTwo();
}

@Component
export struct PageTwo {
  @State pageInfos: NavPathStack = new NavPathStack();
  @State animationProperties: AnimationProperties = new AnimationProperties(this.getUIContext());
  @State myNodeController: MyNodeController | undefined = new MyNodeController(false);
  private pageId: number = -1;
  private shouldDoDefaultTransition: boolean = false;
  private prePageDoFinishTransition: () => void = () => {};
  private cardItemInfo: RectInfoInPx = new RectInfoInPx();
  @StorageProp('windowSizeChanged') @Watch('unRegisterNavParam') windowSizeChangedTime: number = 0;
  @StorageProp('onConfigurationUpdate') @Watch('unRegisterNavParam') onConfigurationUpdateTime: number = 0;

  aboutToAppear(): void {
    // 迁移自定义节点至当前页面
    this.myNodeController = getMyNode();
  }

  private unRegisterNavParam(): void {
    this.shouldDoDefaultTransition = true;
  }

  private onBackPressed(): boolean {
    if (this.shouldDoDefaultTransition) {
      CustomTransition.getInstance().unRegisterNavParam(this.pageId);
      this.pageInfos.pop();
      this.prePageDoFinishTransition();
      this.shouldDoDefaultTransition = false;
      return true;
    }
    this.pageInfos.pop();
    return true;
  }

  build() {
    NavDestination() {
      // Stack需要设置alignContent为TopStart，否则在高度变化过程中，截图和内容都会随高度重新布局位置
      Stack({ alignContent: Alignment.TopStart }) {
        Stack({ alignContent: Alignment.TopStart }) {
          Column({ space: 20 }) {
            NodeContainer(this.myNodeController);
            if (this.animationProperties.showDetailContent) {
              // 请将$r('app.string.shareTransition_text8')替换为实际资源文件，在本示例中该资源文件的value值为"展开态内容"
              Text($r('app.string.shareTransition_text8'))
                .fontSize(20)
                .transition(TransitionEffect.OPACITY)
                .margin(30)
            }
          }
          .alignItems(HorizontalAlign.Start)
        }
        .position({ y: this.animationProperties.positionValue });
      }
      .scale({ x: this.animationProperties.scaleValue, y: this.animationProperties.scaleValue })
      .translate({ x: this.animationProperties.translateX, y: this.animationProperties.translateY })
      .width(this.animationProperties.clipWidth)
      .height(this.animationProperties.clipHeight)
      .borderRadius(this.animationProperties.radius)
      // expandSafeArea使得Stack做沉浸式效果，向上扩到状态栏，向下扩到导航条
      .expandSafeArea([SafeAreaType.SYSTEM])
      // 对高度进行裁切
      .clip(true)
    }
    .backgroundColor(this.animationProperties.navDestinationBgColor)
    .hideTitleBar(true)
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.pageId = this.pageInfos.getAllPathName().length - 1;
      let param = context.pathInfo?.param as Record<string, Object>;
      this.prePageDoFinishTransition = param['doDefaultTransition'] as () => void;
      this.cardItemInfo = param['cardItemInfo'] as RectInfoInPx;
      CustomTransition.getInstance().registerNavParam(this.pageId,
        (isPush: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => {
          this.animationProperties.doAnimation(
            this.cardItemInfo, isPush, isExit, transitionProxy, 0,
            this.prePageDoFinishTransition, this.myNodeController);
        }, 500);
    })
    .onBackPressed(() => {
      return this.onBackPressed();
    })
    .onDisAppear(() => {
      CustomTransition.getInstance().unRegisterNavParam(this.pageId);
    })
  }
}
```

```typescript
// CustomNavigationUtils.ets
// 配置Navigation自定义转场动画
export interface AnimateCallback {
  animation: ((isPush: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => void | undefined)
    | undefined;
  timeout: (number | undefined) | undefined;
}

const customTransitionMap: Map<number, AnimateCallback> = new Map();

export class CustomTransition {
  private constructor() {
  };

  static delegate = new CustomTransition();

  static getInstance() {
    return CustomTransition.delegate;
  }

  // 注册页面的动画回调，name是注册页面的动画的回调
  // animationCallback是需要执行的动画内容，timeout是转场结束的超时时间
  registerNavParam(
    name: number,
    animationCallback: (operation: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => void,
    timeout: number): void {
    if (customTransitionMap.has(name)) {
      let param = customTransitionMap.get(name);
      if (param != undefined) {
        param.animation = animationCallback;
        param.timeout = timeout;
        return;
      }
    }
    let params: AnimateCallback = { timeout: timeout, animation: animationCallback };
    customTransitionMap.set(name, params);
  }

  unRegisterNavParam(name: number): void {
    customTransitionMap.delete(name);
  }

  getAnimateParam(name: number): AnimateCallback {
    let result: AnimateCallback = {
      animation: customTransitionMap.get(name)?.animation,
      timeout: customTransitionMap.get(name)?.timeout,
    };
    return result;
  }
}
```

```ts
// 工程配置文件module.json5中配置 {"routerMap": "$profile:route_map"}
// route_map.json
{
  "routerMap": [
    {
      "name": "PageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder"
    },
    {
      "name": "PageTwo",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "PageTwoBuilder"
    }
  ]
}
```

```typescript
// AnimationProperties.ets
// 一镜到底转场动画封装
import { curves, UIContext } from '@kit.ArkUI';
import { RectInfoInPx } from '../utils/ComponentAttrUtils';
import { WindowUtils } from '../utils/WindowUtils';
import { MyNodeController } from '../NodeContainer/CustomComponent';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'AnimationProperties';
const DOMAIN = 0xF811;
const DEVICE_BORDER_RADIUS: number = 34;

// 将自定义一镜到底转场动画进行封装，其他界面也需要做自定义一镜到底转场的话，可以直接复用，减少工作量
@Observed
export class AnimationProperties {
  public navDestinationBgColor: ResourceColor = Color.Transparent;
  public translateX: number = 0;
  public translateY: number = 0;
  public scaleValue: number = 1;
  public clipWidth: Dimension = 0;
  public clipHeight: Dimension = 0;
  public radius: number = 0;
  public positionValue: number = 0;
  public showDetailContent: boolean = false;
  private uiContext: UIContext;

  constructor(uiContext: UIContext) {
    this.uiContext = uiContext;
  }

  public doAnimation(cardItemInfoPx: RectInfoInPx, isPush: boolean, isExit: boolean,
    transitionProxy: NavigationTransitionProxy, extraTranslateValue: number,
    prePageOnFinish: (index: MyNodeController) => void, myNodeController: MyNodeController | undefined): void {
    // 首先计算卡片的宽高与窗口宽高的比例
    let widthScaleRatio = cardItemInfoPx.width / WindowUtils.windowWidthPx;
    let heightScaleRatio = cardItemInfoPx.height / WindowUtils.windowHeightPx;
    let isUseWidthScale = widthScaleRatio > heightScaleRatio;
    let initScale: number = isUseWidthScale ? widthScaleRatio : heightScaleRatio;

    let initTranslateX: number = 0;
    let initTranslateY: number = 0;
    let initClipWidth: Dimension = 0;
    let initClipHeight: Dimension = 0;
    // 使得PageTwo卡片向上扩到状态栏
    let initPositionValue: number = -this.uiContext.px2vp(WindowUtils.topAvoidAreaHeightPx + extraTranslateValue);

    if (isUseWidthScale) {
      initTranslateX = this.uiContext.px2vp(cardItemInfoPx.left -
        (WindowUtils.windowWidthPx - cardItemInfoPx.width) / 2);
      initClipWidth = '100%';
      initClipHeight = this.uiContext.px2vp((cardItemInfoPx.height) / initScale);
      initTranslateY = this.uiContext.px2vp(cardItemInfoPx.top - ((this.uiContext.vp2px(initClipHeight) -
        this.uiContext.vp2px(initClipHeight) * initScale) / 2));
    } else {
      initTranslateY = this.uiContext.px2vp(cardItemInfoPx.top -
        (WindowUtils.windowHeightPx - cardItemInfoPx.height) / 2);
      initClipHeight = '100%';
      initClipWidth = this.uiContext.px2vp((cardItemInfoPx.width) / initScale);
      initTranslateX = this.uiContext.px2vp(cardItemInfoPx.left -
        (WindowUtils.windowWidthPx / 2 - cardItemInfoPx.width / 2));
    }

    // 转场动画开始前通过计算scale、translate、position和clip height & width，确定节点迁移前后位置一致
    hilog.info(DOMAIN, TAG, 'initScale: ' + initScale + ' initTranslateX ' + initTranslateX +
      ' initTranslateY ' + initTranslateY + ' initClipWidth ' + initClipWidth +
      ' initClipHeight ' + initClipHeight + ' initPositionValue ' + initPositionValue);

    // 转场至新页面
    if (isPush && !isExit) {
      this.scaleValue = initScale;
      this.translateX = initTranslateX;
      this.clipWidth = initClipWidth;
      this.clipHeight = initClipHeight;
      this.translateY = initTranslateY;
      this.positionValue = initPositionValue;

      this.uiContext?.animateTo({
        curve: curves.interpolatingSpring(0, 1, 328, 36),
        onFinish: () => {
          if (transitionProxy) {
            transitionProxy.finishTransition();
          }
        }
      }, () => {
        this.scaleValue = 1.0;
        this.translateX = 0;
        this.translateY = 0;
        this.clipWidth = '100%';
        this.clipHeight = '100%';
        // 页面圆角与系统圆角一致
        this.radius = DEVICE_BORDER_RADIUS;
        this.showDetailContent = true;
      })

      this.uiContext?.animateTo({
        duration: 100,
        curve: Curve.Sharp,
      }, () => {
        // 页面由透明逐渐变为设置背景色
        this.navDestinationBgColor = '#00ffffff';
      })

      // 返回旧页面
    } else if (!isPush && isExit) {

      this.uiContext?.animateTo({
        duration: 350,
        curve: Curve.EaseInOut,
        onFinish: () => {
          if (transitionProxy) {
            transitionProxy.finishTransition();
          }
          prePageOnFinish(myNodeController);
          // 自定义节点从PageTwo下树
          if (myNodeController != undefined) {
            (myNodeController as MyNodeController).onRemove();
          }
        }
      }, () => {
        this.scaleValue = initScale;
        this.translateX = initTranslateX;
        this.translateY = initTranslateY;
        this.radius = 0;
        this.clipWidth = initClipWidth;
        this.clipHeight = initClipHeight;
        this.showDetailContent = false;
      })

      this.uiContext?.animateTo({
        duration: 200,
        delay: 150,
        curve: Curve.Friction,
      }, () => {
        this.navDestinationBgColor = Color.Transparent;
      })
    }
  }
}
```

```typescript
// ComponentAttrUtils.ets
// 获取组件相对窗口的位置
import { componentUtils, UIContext } from '@kit.ArkUI';
import { JSON } from '@kit.ArkTS';

export class ComponentAttrUtils {
  // 根据组件的id获取组件的位置信息
  public static getRectInfoById(context: UIContext, id: string): RectInfoInPx {
    if (!context || !id) {
      throw Error('object is empty');
    }
    let componentInfo: componentUtils.ComponentInfo = context.getComponentUtils().getRectangleById(id);

    if (!componentInfo) {
      throw Error('object is empty');
    }

    let rstRect: RectInfoInPx = new RectInfoInPx();
    const widthScaleGap = componentInfo.size.width * (1 - componentInfo.scale.x) / 2;
    const heightScaleGap = componentInfo.size.height * (1 - componentInfo.scale.y) / 2;
    rstRect.left = componentInfo.translate.x + componentInfo.windowOffset.x + widthScaleGap;
    rstRect.top = componentInfo.translate.y + componentInfo.windowOffset.y + heightScaleGap;
    rstRect.right =
      componentInfo.translate.x + componentInfo.windowOffset.x + componentInfo.size.width - widthScaleGap;
    rstRect.bottom =
      componentInfo.translate.y + componentInfo.windowOffset.y + componentInfo.size.height - heightScaleGap;
    rstRect.width = rstRect.right - rstRect.left;
    rstRect.height = rstRect.bottom - rstRect.top;
    return {
      left: rstRect.left,
      right: rstRect.right,
      top: rstRect.top,
      bottom: rstRect.bottom,
      width: rstRect.width,
      height: rstRect.height
    }
  }
}

export class RectInfoInPx {
  public left: number = 0;
  public top: number = 0;
  public right: number = 0;
  public bottom: number = 0;
  public width: number = 0;
  public height: number = 0;
}

export class RectJson {
  public $rect: Array<number> = [];
}
```

```typescript
// WindowUtils.ets
// 窗口信息
import { window } from '@kit.ArkUI';

export class WindowUtils {
  public static window: window.Window;
  public static windowWidthPx: number;
  public static windowHeightPx: number;
  public static topAvoidAreaHeightPx: number;
  public static navigationIndicatorHeightPx: number;
}
```

```typescript
// EntryAbility.ets
// 程序入口处的onWindowStageCreate增加对窗口宽高等的抓取

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { WindowUtils } from '../utils/WindowUtils';
import { display, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG: string = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  private currentBreakPoint: string = '';

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onWindowStageCreate');
    // ...
    // 获取窗口宽高
    WindowUtils.window = windowStage.getMainWindowSync();
    WindowUtils.windowWidthPx = WindowUtils.window.getWindowProperties().windowRect.width;
    WindowUtils.windowHeightPx = WindowUtils.window.getWindowProperties().windowRect.height;

    this.updateBreakpoint(WindowUtils.windowWidthPx);

    // 获取上方避让区(状态栏等)高度
    let avoidArea = WindowUtils.window.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
    WindowUtils.topAvoidAreaHeightPx = avoidArea.topRect.height;

    // 获取导航条高度
    let navigationArea = WindowUtils.window.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR);
    WindowUtils.navigationIndicatorHeightPx = navigationArea.bottomRect.height;

    hilog.info(DOMAIN, TAG, 'the width is ' + WindowUtils.windowWidthPx + '  ' + WindowUtils.windowHeightPx + '  ' +
    WindowUtils.topAvoidAreaHeightPx + '  ' + WindowUtils.navigationIndicatorHeightPx);

    // 监听窗口尺寸、状态栏高度及导航条高度的变化并更新
    try {
      WindowUtils.window.on('windowSizeChange', (data) => {
        hilog.info(DOMAIN, TAG, 'on windowSizeChange, the width is ' + data.width + ', the height is ' + data.height);
        WindowUtils.windowWidthPx = data.width;
        WindowUtils.windowHeightPx = data.height;
        this.updateBreakpoint(data.width);
        AppStorage.setOrCreate('windowSizeChanged', Date.now());
      })

      WindowUtils.window.on('avoidAreaChange', (data) => {
        if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
          let topRectHeight = data.area.topRect.height;
          hilog.info(DOMAIN, TAG, 'on avoidAreaChange, the top avoid area height is ' + topRectHeight);
          WindowUtils.topAvoidAreaHeightPx = topRectHeight;
        } else if (data.type === window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
          let bottomRectHeight = data.area.bottomRect.height;
          hilog.info(DOMAIN, TAG, 'on avoidAreaChange, the navigation indicator height is ' + bottomRectHeight);
          WindowUtils.navigationIndicatorHeightPx = bottomRectHeight;
        }
      })
    } catch (exception) {
      hilog.error(DOMAIN, TAG, `register failed. code: ${exception.code}, message: ${exception.message}`);
    }

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(DOMAIN, TAG, 'Succeeded in loading the content.');
    });
  }

  updateBreakpoint(width: number) {
    let windowWidthVp = width / (display.getDefaultDisplaySync().densityDPI / 160);
    let newBreakPoint: string = '';
    if (windowWidthVp < 400) {
      newBreakPoint = 'xs';
    } else if (windowWidthVp < 600) {
      newBreakPoint = 'sm';
    } else if (windowWidthVp < 800) {
      newBreakPoint = 'md';
    } else {
      newBreakPoint = 'lg';
    }
    if (this.currentBreakPoint !== newBreakPoint) {
      this.currentBreakPoint = newBreakPoint;
      // 使用状态变量记录当前断点值
      AppStorage.setOrCreate('currentBreakpoint', this.currentBreakPoint);
    }
  }
  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onBackground');
  }
}
```

```typescript
// CustomComponent.ets
// 自定义占位节点，跨容器迁移能力
import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

@Builder
function cardBuilder() {
  // 请将$r('app.media.card')替换为实际资源文件
  Image($r('app.media.card'))
    .width('100%')
    .id('card')
}

export class MyNodeController extends NodeController {
  private cardNode: BuilderNode<[]> | null = null;
  private wrapBuilder: WrappedBuilder<[]> = wrapBuilder(cardBuilder);
  private needCreate: boolean = false;
  private isRemove: boolean = false;

  constructor(create: boolean) {
    super();
    this.needCreate = create;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.isRemove === true) {
      return null;
    }
    if (this.needCreate && this.cardNode === null) {
      this.cardNode = new BuilderNode(uiContext);
      this.cardNode.build(this.wrapBuilder);
    }
    if (this.cardNode === null) {
      return null;
    }
    return this.cardNode!.getFrameNode()!;
  }

  getNode(): BuilderNode<[]> | null {
    return this.cardNode;
  }

  setNode(node: BuilderNode<[]> | null) {
    this.cardNode = node;
    this.rebuild();
  }

  onRemove() {
    this.isRemove = true;
    this.rebuild();
    this.isRemove = false;
  }

  init(uiContext: UIContext) {
    this.cardNode = new BuilderNode(uiContext);
    this.cardNode.build(this.wrapBuilder);
  }
}

let myNode: MyNodeController | undefined;

export const createMyNode =
  (uiContext: UIContext) => {
    myNode = new MyNodeController(false);
    myNode.init(uiContext);
  }

export const getMyNode = (): MyNodeController | undefined => {
  return myNode;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/IHlqofmjRPaRRhs1g7VvRg/zh-cn_image_0000002706673846.gif)

### 结合BindSheet使用

想实现半模态转场（[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)）的同时，组件从初始界面做一镜到底动画到半模态页面的效果，可以使用这样的设计思路。将[SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)中的mode设置为SheetMode.EMBEDDED，该模式下新起的页面可以覆盖在半模态弹窗上，页面返回后该半模态依旧存在，半模态面板内容不丢失。在半模态转场的同时设置一全模态转场（[bindContentCover](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover)）页面无转场出现，该页面仅有需要做共享元素转场的组件，通过属性动画，展示组件从初始界面至半模态页面的一镜到底动效，并在动画结束时关闭页面，并将该组件迁移至半模态页面。

以点击图片展开半模态页的场景为例，实现步骤为：

* 在初始界面挂载半模态转场和全模态转场两个页面，半模态页按需布局，全模态页面仅放置一镜到底动效需要的组件，抓取布局信息，使其初始位置为初始界面图片的位置。点击初始界面图片时，同时触发半模态和全模态页面出现，因设置为SheetMode.EMBEDDED模式，此时全模态页面层级最高。
* 设置不可见的占位图片置于半模态页上，作为一镜到底动效结束时图片的终止位置。利用[布局回调](../harmonyos-references/js-apis-arkui-inspector.md)监听该占位图片布局完成的时候，此时执行回调抓取占位图片的位置信息，随后全模态页面上的图片利用属性动画开始进行共享元素转场。
* 全模态页面的动画结束时触发结束回调，关闭全模态页面，将共享元素图片的节点迁移至半模态页面，替换占位图片。
* 需注意，半模态页面的弹起高度不同，其页面起始位置也有所不同，而全模态则是全屏显示，两者存在一高度差，做一镜到底动画时，需要计算差值并进行修正，具体可见demo。
* 还可以配合一镜到底动画，给初始界面图片也增加一个从透明到出现的动画，使得动效更为流畅。

```txt
├──entry/src/main/ets                 // 代码区
│  ├──entryability
│  │  └──EntryAbility.ets             // 程序入口类
│  ├──NodeContainer
│  │  └──CustomComponent.ets          // 自定义占位节点
│  ├──pages
│  │  └──Index.ets                    // 进行共享元素转场的主页面
│  └──utils
│     ├──ComponentAttrUtils.ets       // 组件位置获取
│     └──WindowUtils.ets              // 窗口信息
└──entry/src/main/resources           // 资源文件
```

```ts
// Index.ets
import { MyNodeController, createMyNode, getMyNode } from '../NodeContainer/CustomComponent';
import { ComponentAttrUtils, RectInfoInPx } from '../utils/ComponentAttrUtils';
import { WindowUtils } from '../utils/WindowUtils';
import { inspector } from '@kit.ArkUI'

class AnimationInfo {
  scale: number = 0;
  translateX: number = 0;
  translateY: number = 0;
  clipWidth: Dimension = 0;
  clipHeight: Dimension = 0;
}

@Entry
@Component
struct Index {
  @State isShowSheet: boolean = false;
  @State isShowImage: boolean = false;
  @State isShowOverlay: boolean = false;
  @State isAnimating: boolean = false;
  @State isEnabled: boolean = true;

  @State scaleValue: number = 0;
  @State translateX: number = 0;
  @State translateY: number = 0;
  @State clipWidth: Dimension = 0;
  @State clipHeight: Dimension = 0;
  @State radius: number = 0;
  // 原图的透明度
  @State opacityDegree: number = 1;

  // 抓取照片原位置信息
  private originInfo: AnimationInfo = new AnimationInfo;
  // 抓取照片在半模态页上位置信息
  private targetInfo: AnimationInfo = new AnimationInfo;
  // 半模态高度
  private bindSheetHeight: number = 450;
  // 半模态上图片圆角
  private sheetRadius: number = 20;

  // 设置半模态上图片的布局监听
  listener:inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('target');
  aboutToAppear(): void {
    // 设置半模态上图片的布局完成回调
    let onLayoutComplete:()=>void=():void=>{
      // 目标图片布局完成时抓取布局信息
      this.targetInfo = this.calculateData('target');
      // 仅半模态正确布局且此时无动画时触发一镜到底动画
      if (this.targetInfo.scale != 0 && this.targetInfo.clipWidth != 0 && this.targetInfo.clipHeight != 0 && !this.isAnimating) {
        this.isAnimating = true;
        // 用于一镜到底的模态页的属性动画
        this.getUIContext()?.animateTo({
          duration: 1000,
          curve: Curve.Friction,
          onFinish: () => {
            // 模态转场页（overlay）上的自定义节点下树
            this.isShowOverlay = false;
            // 半模态上的自定义节点上树，由此完成节点迁移
            this.isShowImage = true;
          }
        }, () => {
          this.scaleValue = this.targetInfo.scale;
          this.translateX = this.targetInfo.translateX;
          this.clipWidth = this.targetInfo.clipWidth;
          this.clipHeight = this.targetInfo.clipHeight;
          // 修正因半模态高度和缩放导致的高度差
          this.translateY = this.targetInfo.translateY +
            (this.getUIContext().px2vp(WindowUtils.windowHeightPx) - this.bindSheetHeight
              - this.getUIContext().px2vp(WindowUtils.navigationIndicatorHeightPx) - this.getUIContext().px2vp(WindowUtils.topAvoidAreaHeightPx));
          // 修正因缩放导致的圆角差异
          this.radius = this.sheetRadius / this.scaleValue
        })
        // 原图从透明到出现的动画
        this.getUIContext()?.animateTo({
          duration: 2000,
          curve: Curve.Friction,
        }, () => {
          this.opacityDegree = 1;
        })
      }
    }
    // 打开布局监听
    this.listener.on('layout', onLayoutComplete)
  }

  // 获取对应id的组件相对窗口左上角的属性
  calculateData(id: string): AnimationInfo {
    let itemInfo: RectInfoInPx =
      ComponentAttrUtils.getRectInfoById(WindowUtils.window.getUIContext(), id);
    // 首先计算图片的宽高与窗口宽高的比例
    let widthScaleRatio = itemInfo.width / WindowUtils.windowWidthPx;
    let heightScaleRatio = itemInfo.height / WindowUtils.windowHeightPx;
    let isUseWidthScale = widthScaleRatio > heightScaleRatio;
    let itemScale: number = isUseWidthScale ? widthScaleRatio : heightScaleRatio;
    let itemTranslateX: number = 0;
    let itemClipWidth: Dimension = 0;
    let itemClipHeight: Dimension = 0;
    let itemTranslateY: number = 0;

    if (isUseWidthScale) {
      itemTranslateX = this.getUIContext().px2vp(itemInfo.left - (WindowUtils.windowWidthPx - itemInfo.width) / 2);
      itemClipWidth = '100%';
      itemClipHeight = this.getUIContext().px2vp((itemInfo.height) / itemScale);
      itemTranslateY = this.getUIContext().px2vp(itemInfo.top - ((this.getUIContext().vp2px(itemClipHeight) - this.getUIContext().vp2px(itemClipHeight) * itemScale) / 2));
    } else {
      itemTranslateY = this.getUIContext().px2vp(itemInfo.top - (WindowUtils.windowHeightPx - itemInfo.height) / 2);
      itemClipHeight = '100%';
      itemClipWidth = this.getUIContext().px2vp((itemInfo.width) / itemScale);
      itemTranslateX = this.getUIContext().px2vp(itemInfo.left - (WindowUtils.windowWidthPx / 2 - itemInfo.width / 2));
    }

    return {
      scale: itemScale,
      translateX: itemTranslateX ,
      translateY: itemTranslateY,
      clipWidth: itemClipWidth,
      clipHeight: itemClipHeight,
    }
  }

  // 照片页
  build() {
    Column() {
      Text('照片')
        .textAlign(TextAlign.Start)
        .width('100%')
        .fontSize(30)
        .padding(20)
      // 图片使用Resource资源，需用户自定义
      Image($r("app.media.flower"))
        .opacity(this.opacityDegree)
        .width('90%')
        .id('origin')// 挂载半模态页
        .enabled(this.isEnabled)
        .onClick(() => {
          // 获取原始图像的位置信息，将模态页上图片移动缩放至该位置
          this.originInfo = this.calculateData('origin');
          this.scaleValue = this.originInfo.scale;
          this.translateX = this.originInfo.translateX;
          this.translateY = this.originInfo.translateY;
          this.clipWidth = this.originInfo.clipWidth;
          this.clipHeight = this.originInfo.clipHeight;
          this.radius = 0;
          this.opacityDegree = 0;
          // 启动半模态页和模态页
          this.isShowSheet = true;
          this.isShowOverlay = true;
          // 设置原图为不可交互抗打断
          this.isEnabled = false;
        })
    }
    .width('100%')
    .height('100%')
    .padding({ top: 20 })
    .alignItems(HorizontalAlign.Center)
    .bindSheet(this.isShowSheet, this.mySheet(), {
      // Embedded模式使得其他页面可以高于半模态页
      mode: SheetMode.EMBEDDED,
      height: this.bindSheetHeight,
      onDisappear: () => {
        // 保证半模态消失时状态正确
        this.isShowImage = false;
        this.isShowSheet = false;
        // 设置一镜到底动画又进入可触发状态
        this.isAnimating = false;
        // 原图重新变为可交互状态
        this.isEnabled = true;
      }
    }) // 挂载模态页作为一镜到底动画的实现页
    .bindContentCover(this.isShowOverlay, this.overlayNode(), {
      // 模态页面设置为无转场
      transition: TransitionEffect.IDENTITY,
    })
  }

  // 半模态页面
  @Builder
  mySheet() {
    Column({space: 20}) {
      Text('半模态页面')
        .fontSize(30)
      Row({space: 40}) {
        Column({space: 20}) {
          ForEach([1, 2, 3, 4], () => {
            Stack()
              .backgroundColor(Color.Pink)
              .borderRadius(20)
              .width(60)
              .height(60)
          })
        }
        Column() {
          if (this.isShowImage) {
            // 半模态页面的自定义图片节点
            ImageNode()
          }
          else {
            // 抓取布局和占位用，实际不显示
            // 图片使用Resource资源，需用户自定义
            Image($r("app.media.flower"))
              .visibility(Visibility.Hidden)
          }
        }
        .height(300)
        .width(200)
        .borderRadius(20)
        .clip(true)
        .id('target')
      }
      .alignItems(VerticalAlign.Top)
    }
    .alignItems(HorizontalAlign.Start)
    .height('100%')
    .width('100%')
    .margin(40)
  }

  @Builder
  overlayNode() {
    // Stack需要设置alignContent为TopStart，否则在高度变化过程中，截图和内容都会随高度重新布局位置
    Stack({ alignContent: Alignment.TopStart }) {
      ImageNode()
    }
    .scale({ x: this.scaleValue, y: this.scaleValue, centerX: undefined, centerY: undefined})
    .translate({ x: this.translateX, y: this.translateY })
    .width(this.clipWidth)
    .height(this.clipHeight)
    .borderRadius(this.radius)
    .clip(true)
  }
}

@Component
struct ImageNode {
  @State myNodeController: MyNodeController | undefined = new MyNodeController(false);

  aboutToAppear(): void {
    // 获取自定义节点
    let node = getMyNode();
    if (node == undefined) {
      // 新建自定义节点
      createMyNode(this.getUIContext());
    }
    this.myNodeController = getMyNode();
  }

  aboutToDisappear(): void {
    if (this.myNodeController != undefined) {
      // 节点下树
      this.myNodeController.onRemove();
    }
  }
  build() {
    NodeContainer(this.myNodeController)
  }
}
```

```typescript
// CustomComponent.ets
// 自定义占位节点，跨容器迁移能力
import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

@Builder
function flowerBuilder() {
  // 请将$r('app.media.longevity_flower')替换为实际资源文件
  Image($r('app.media.longevity_flower'))
  // 避免第一次加载图片时图片闪烁
    .syncLoad(true);
}

export class MyNodeController extends NodeController {
  private flowerNode: BuilderNode<[]> | null = null;
  private wrapBuilder: WrappedBuilder<[]> = wrapBuilder(flowerBuilder);
  private needCreate: boolean = false;
  private isRemove: boolean = false;

  constructor(create: boolean) {
    super();
    this.needCreate = create;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.isRemove === true) {
      return null;
    }
    if (this.needCreate && this.flowerNode === null) {
      this.flowerNode = new BuilderNode(uiContext);
      this.flowerNode.build(this.wrapBuilder);
    }
    if (this.flowerNode === null) {
      return null;
    }
    return this.flowerNode!.getFrameNode()!;
  }

  getNode(): BuilderNode<[]> | null {
    return this.flowerNode;
  }

  setNode(node: BuilderNode<[]> | null) {
    this.flowerNode = node;
    this.rebuild();
  }

  onRemove() {
    this.isRemove = true;
    this.rebuild();
    this.isRemove = false;
  }

  init(uiContext: UIContext) {
    this.flowerNode = new BuilderNode(uiContext);
    this.flowerNode.build(this.wrapBuilder);
  }
}

let myNode: MyNodeController | undefined;

export const createMyNode =
  (uiContext: UIContext) => {
    myNode = new MyNodeController(false);
    myNode.init(uiContext);
  }

export const getMyNode = (): MyNodeController | undefined => {
  return myNode;
}
```

```typescript
// ComponentAttrUtils.ets
// 获取组件相对窗口的位置
import { componentUtils, UIContext } from '@kit.ArkUI';
import { JSON } from '@kit.ArkTS';

export class ComponentAttrUtils {
  // 根据组件的id获取组件的位置信息
  public static getRectInfoById(context: UIContext, id: string): RectInfoInPx {
    if (!context || !id) {
      throw Error('object is empty');
    }
    let componentInfo: componentUtils.ComponentInfo = context.getComponentUtils().getRectangleById(id);

    if (!componentInfo) {
      throw Error('object is empty');
    }

    let rstRect: RectInfoInPx = new RectInfoInPx();
    const widthScaleGap = componentInfo.size.width * (1 - componentInfo.scale.x) / 2;
    const heightScaleGap = componentInfo.size.height * (1 - componentInfo.scale.y) / 2;
    rstRect.left = componentInfo.translate.x + componentInfo.windowOffset.x + widthScaleGap;
    rstRect.top = componentInfo.translate.y + componentInfo.windowOffset.y + heightScaleGap;
    rstRect.right =
      componentInfo.translate.x + componentInfo.windowOffset.x + componentInfo.size.width - widthScaleGap;
    rstRect.bottom =
      componentInfo.translate.y + componentInfo.windowOffset.y + componentInfo.size.height - heightScaleGap;
    rstRect.width = rstRect.right - rstRect.left;
    rstRect.height = rstRect.bottom - rstRect.top;
    return {
      left: rstRect.left,
      right: rstRect.right,
      top: rstRect.top,
      bottom: rstRect.bottom,
      width: rstRect.width,
      height: rstRect.height
    }
  }
}

export class RectInfoInPx {
  public left: number = 0;
  public top: number = 0;
  public right: number = 0;
  public bottom: number = 0;
  public width: number = 0;
  public height: number = 0;
}

export class RectJson {
  public $rect: Array<number> = [];
}
```

```typescript
// WindowUtils.ets
// 窗口信息
import { window } from '@kit.ArkUI';

export class WindowUtils {
  public static window: window.Window;
  public static windowWidthPx: number;
  public static windowHeightPx: number;
  public static topAvoidAreaHeightPx: number;
  public static navigationIndicatorHeightPx: number;
}
```

```typescript
// EntryAbility.ets
// 程序入口处的onWindowStageCreate增加对窗口宽高等的抓取

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { WindowUtils } from '../utils/WindowUtils';
import { display, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG: string = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  private currentBreakPoint: string = '';

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onWindowStageCreate');
    // ...
    // 获取窗口宽高
    WindowUtils.window = windowStage.getMainWindowSync();
    WindowUtils.windowWidthPx = WindowUtils.window.getWindowProperties().windowRect.width;
    WindowUtils.windowHeightPx = WindowUtils.window.getWindowProperties().windowRect.height;

    this.updateBreakpoint(WindowUtils.windowWidthPx);

    // 获取上方避让区(状态栏等)高度
    let avoidArea = WindowUtils.window.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
    WindowUtils.topAvoidAreaHeightPx = avoidArea.topRect.height;

    // 获取导航条高度
    let navigationArea = WindowUtils.window.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR);
    WindowUtils.navigationIndicatorHeightPx = navigationArea.bottomRect.height;

    hilog.info(DOMAIN, TAG, 'the width is ' + WindowUtils.windowWidthPx + '  ' + WindowUtils.windowHeightPx + '  ' +
    WindowUtils.topAvoidAreaHeightPx + '  ' + WindowUtils.navigationIndicatorHeightPx);

    // 监听窗口尺寸、状态栏高度及导航条高度的变化并更新
    try {
      WindowUtils.window.on('windowSizeChange', (data) => {
        hilog.info(DOMAIN, TAG, 'on windowSizeChange, the width is ' + data.width + ', the height is ' + data.height);
        WindowUtils.windowWidthPx = data.width;
        WindowUtils.windowHeightPx = data.height;
        this.updateBreakpoint(data.width);
        AppStorage.setOrCreate('windowSizeChanged', Date.now());
      })

      WindowUtils.window.on('avoidAreaChange', (data) => {
        if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
          let topRectHeight = data.area.topRect.height;
          hilog.info(DOMAIN, TAG, 'on avoidAreaChange, the top avoid area height is ' + topRectHeight);
          WindowUtils.topAvoidAreaHeightPx = topRectHeight;
        } else if (data.type === window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
          let bottomRectHeight = data.area.bottomRect.height;
          hilog.info(DOMAIN, TAG, 'on avoidAreaChange, the navigation indicator height is ' + bottomRectHeight);
          WindowUtils.navigationIndicatorHeightPx = bottomRectHeight;
        }
      })
    } catch (exception) {
      hilog.error(DOMAIN, TAG, `register failed. code: ${exception.code}, message: ${exception.message}`);
    }

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(DOMAIN, TAG, 'Succeeded in loading the content.');
    });
  }

  updateBreakpoint(width: number) {
    let windowWidthVp = width / (display.getDefaultDisplaySync().densityDPI / 160);
    let newBreakPoint: string = '';
    if (windowWidthVp < 400) {
      newBreakPoint = 'xs';
    } else if (windowWidthVp < 600) {
      newBreakPoint = 'sm';
    } else if (windowWidthVp < 800) {
      newBreakPoint = 'md';
    } else {
      newBreakPoint = 'lg';
    }
    if (this.currentBreakPoint !== newBreakPoint) {
      this.currentBreakPoint = newBreakPoint;
      // 使用状态变量记录当前断点值
      AppStorage.setOrCreate('currentBreakpoint', this.currentBreakPoint);
    }
  }
  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onBackground');
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/xA5EbF8KTcaiaVv86EN3PQ/zh-cn_image_0000002736432937.gif)

## 使用geometryTransition共享元素转场

[geometryTransition](../harmonyos-references/ts-transition-animation-geometrytransition.md)用于组件内隐式共享元素转场，在视图状态切换过程中提供丝滑的上下文继承过渡体验。

geometryTransition的使用方式为对需要添加一镜到底动效的两个组件使用geometryTransition接口绑定同一id，这样在其中一个组件消失同时另一个组件创建出现的时候，系统会对二者添加一镜到底动效。

geometryTransition绑定两个对象的实现方式使得geometryTransition区别于其他方法，最适合用于两个不同对象之间完成一镜到底。

### geometryTransition的简单使用

对于同一个页面中的两个元素的一镜到底效果，geometryTransition接口的简单使用示例如下：

```typescript
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct IfElseGeometryTransition {
  @State isShow: boolean = false;

  build() {
    Stack({ alignContent: Alignment.Center }) {
      if (this.isShow) {
        // 请将$r('app.media.spring')替换为实际资源文件
        Image($r('app.media.spring'))
          .autoResize(false)
          .clip(true)
          .width(200)
          .height(200)
          .borderRadius(100)
          .geometryTransition('picture')
          .transition(TransitionEffect.OPACITY)
          // 在打断场景下，即动画过程中点击页面触发下一次转场，如果不加id，则会出现重影
          // 加了id之后，新建的spring图片会复用之前的spring图片节点，不会重新创建节点，也就不会有重影问题
          // 加id的规则为加在if和else下的第一个节点上，有多个并列节点则也需要进行添加
          .id('item1')
      } else {
        // geometryTransition此处绑定的是容器，那么容器内的子组件需设为相对布局跟随父容器变化，
        // 套多层容器为了说明相对布局约束传递
        Column() {
          Column() {
            // 请将$r('app.media.sunset_sky')替换为实际资源文件
            Image($r('app.media.sunset_sky'))
              .size({ width: '100%', height: '100%' })
          }
          .size({ width: '100%', height: '100%' })
        }
        .width(100)
        .height(100)
        // geometryTransition会同步圆角，但仅限于geometryTransition绑定处，此处绑定的是容器
        // 则对容器本身有圆角同步而不会操作容器内部子组件的borderRadius
        .borderRadius(50)
        .clip(true)
        .geometryTransition('picture')
        // transition保证节点离场不被立即析构，设置通用转场效果
        .transition(TransitionEffect.OPACITY)
        .position({ x: 40, y: 40 })
        .id('item2')
      }
    }
    .onClick(() => {
      this.getUIContext()?.animateTo({
        curve: curves.springMotion()
      }, () => {
        this.isShow = !this.isShow;
      })
    })
    .size({ width: '100%', height: '100%' })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/TI7RnDjHSRCTXBA0zEtmSA/zh-cn_image_0000002706833782.gif)

### geometryTransition结合模态转场使用

更多的场景中，需要对一个页面的元素与另一个页面的元素添加一镜到底动效。可以通过geometryTransition搭配模态转场接口实现。以点击头像弹出个人信息页的demo为例：

```typescript
import { common } from '@kit.AbilityKit';

class PostData {
  // 请将$r('app.media.flower')替换为实际资源文件
  avatar: Resource = $r('app.media.flower');
  name: string = '';
  message: ResourceStr = '';
  images: Resource[] = [];
}

@Entry
@Component
struct Index {
  @State isPersonalPageShow: boolean = false;
  @State selectedIndex: number = 0;
  @State alphaValue: number = 1;
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  // 数组中图片均使用Resource资源，需用户自定义
  private allPostData: PostData[] = [
    {
      // 请将$r('app.media.flower')替换为实际资源文件
      avatar: $r('app.media.flower'),
      name: 'Alice',
      // 请将$r('app.string.shareTransition_text1')替换为实际资源文件，在本示例中该资源文件的value值为"天气晴朗"
      message: $r('app.string.shareTransition_text1'),
      // 请将$r('app.media.spring')替换为实际资源文件
      // 请将$r('app.media.tall_tree')替换为实际资源文件
      images: [$r('app.media.spring'), $r('app.media.tall_tree')]
    },
    {
      // 请将$r('app.media.sunset_sky')替换为实际资源文件
      avatar: $r('app.media.sunset_sky'),
      name: 'Bob',
      // 请将$r('app.string.shareTransition_text2')替换为实际资源文件，在本示例中该资源文件的value值为"你好世界"
      message: $r('app.string.shareTransition_text2'),
      // 请将$r('app.media.island')替换为实际资源文件
      images: [$r('app.media.island')]
    },
    {
      // 请将$r('app.media.tall_tree')替换为实际资源文件
      avatar: $r('app.media.tall_tree'),
      name: 'Carl',
      // 请将$r('app.string.shareTransition_text3')替换为实际资源文件，在本示例中该资源文件的value值为"万物生长"
      message: $r('app.string.shareTransition_text3'),
      // 请将$r('app.media.flower')替换为实际资源文件
      // 请将$r('app.media.sunset_sky')替换为实际资源文件
      // 请将$r('app.media.spring')替换为实际资源文件
      images: [$r('app.media.flower'), $r('app.media.sunset_sky'), $r('app.media.spring')]
    }];

  private onAvatarClicked(index: number): void {
    this.selectedIndex = index;
    this.getUIContext()?.animateTo({
      duration: 350,
      curve: Curve.Friction
    }, () => {
      this.isPersonalPageShow = !this.isPersonalPageShow;
      this.alphaValue = 0;
    });
  }

  private onPersonalPageBack(index: number): void {
    this.getUIContext()?.animateTo({
      duration: 350,
      curve: Curve.Friction
    }, () => {
      this.isPersonalPageShow = !this.isPersonalPageShow;
      this.alphaValue = 1;
    });
  }

  @Builder
  PersonalPageBuilder(index: number) {
    Column({ space: 20 }) {
      Image(this.allPostData[index].avatar)
        .size({ width: 200, height: 200 })
        .borderRadius(100)
        // 头像配置共享元素效果，与点击的头像的id匹配
        .geometryTransition(index.toString())
        .clip(true)
        .transition(TransitionEffect.opacity(0.99))

      Text(this.allPostData[index].name)
        .font({ size: 30, weight: 600 })
        // 对文本添加出现转场效果
        .transition(TransitionEffect.asymmetric(
          TransitionEffect.OPACITY
            .combine(TransitionEffect.translate({ y: 100 })),
          TransitionEffect.OPACITY.animation({ duration: 0 })
        ))

      // 请在resources\base\element\string.json文件中配置name为'shareTransition_text11'，value为非空字符串的资源
      Text(this.context.resourceManager.getStringByNameSync('shareTransition_text11') + this.allPostData[index].name)
      // 对文本添加出现转场效果
        .transition(TransitionEffect.asymmetric(
          TransitionEffect.OPACITY
            .combine(TransitionEffect.translate({ y: 100 })),
          TransitionEffect.OPACITY.animation({ duration: 0 })
        ))
    }
    .padding({ top: 20 })
    .size({ width: 360, height: 780 })
    .backgroundColor(Color.White)
    .onClick(() => {
      this.onPersonalPageBack(index);
    })
    .transition(TransitionEffect.asymmetric(
      TransitionEffect.opacity(0.99),
      TransitionEffect.OPACITY
    ))
  }

  build() {
    Column({ space: 20 }) {
      ForEach(this.allPostData, (postData: PostData, index: number) => {
        Column() {
          Post({
            data: postData, index: index, onAvatarClicked: (index: number) => {
              this.onAvatarClicked(index);
            }
          })
        }
        .width('100%')
      }, (postData: PostData, index: number) => index.toString())
    }
    .size({ width: '100%', height: '100%' })
    .backgroundColor('#40808080')
    .bindContentCover(this.isPersonalPageShow,
      this.PersonalPageBuilder(this.selectedIndex), { modalTransition: ModalTransition.NONE })
    .opacity(this.alphaValue)
  }
}

@Component
export default struct Post {
  @Prop data: PostData;
  @Prop index: number;
  @State expandImageSize: number = 100;
  @State avatarSize: number = 50;
  private onAvatarClicked: (index: number) => void = (index: number) => { };

  build() {
    Column({ space: 20 }) {
      Row({ space: 10 }) {
        Image(this.data.avatar)
          .size({ width: this.avatarSize, height: this.avatarSize })
          .borderRadius(this.avatarSize / 2)
          .clip(true)
          .onClick(() => {
            this.onAvatarClicked(this.index);
          })
          // 对头像绑定共享元素转场的id
          .geometryTransition(this.index.toString(), { follow: true })
          .transition(TransitionEffect.OPACITY.animation({ duration: 350, curve: Curve.Friction }))

        Text(this.data.name)
      }
      .justifyContent(FlexAlign.Start)

      Text(this.data.message)

      Row({ space: 15 }) {
        ForEach(this.data.images, (imageResource: Resource, index: number) => {
          Image(imageResource)
            .size({ width: 100, height: 100 })
        }, (imageResource: Resource, index: number) => index.toString())
      }
    }
    .backgroundColor(Color.White)
    .size({ width: '100%', height: 250 })
    .alignItems(HorizontalAlign.Start)
    .padding({ left: 10, top: 10 })
  }
}
```

效果为点击主页的头像后，弹出模态页面显示个人信息，并且两个页面之间的头像做一镜到底动效：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/D7btXkT-RA6SMz_hYB08kQ/zh-cn_image_0000002736312891.gif)

## 元素转场案例

### 图片展开一镜到底

* 双指放大转场

  图片使用双指放大转场显示图片详情页。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/rDmDz_CIQMazpARw0zBb2Q/zh-cn_image_0000002706673848.gif)

  通过NodeContainer组件实现跨节点迁移，通过手势捏合来控制节点的上下树，达成一镜到底动效。

  1. 小图模式和大图模式分别为两个页面，通过监听expand值来进行页面切换。

     ```ts
     @StorageProp('expand') @Watch('goToPageTwo') num1: number = 0;
     // ...

     aboutToAppear(): void {
       if (!getMyNode()) {
         createMyNode(this.getUIContext(), false);
       }
       this.imageGalleryNodeController = getMyNode();
     }
     ```
  2. 创建NodeContainer节点类。

     ```ts
     export class ImageGalleryNodeController extends NodeController {
       private rootNode: BuilderNode<[Params]> | null = null;
       private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(ImageGalleryBuilder);
       private isExpand: boolean = false;

       constructor(isExpand: boolean) {
         super();
         this.isExpand = isExpand;
       }

       makeNode(uiContext: UIContext): FrameNode | null {
         if (this.rootNode === null) {
           this.rootNode = new BuilderNode(uiContext);
           this.rootNode.build(this.wrapBuilder, { isExpand: this.isExpand });
         }
         return this.rootNode.getFrameNode();
       }

       init(uiContext: UIContext) {
         this.rootNode = new BuilderNode(uiContext);
         this.rootNode.build(this.wrapBuilder, { isExpand: this.isExpand });
       }

       update(isExpand: boolean) {
         if (this.rootNode !== null) {
           this.rootNode.update({ isExpand });
         }
       }
     }
     ```
  3. 在小图界面当对图片进行双指捏合操作时，改变isExpand值。

     ```ts
     PinchGesture()
       .onActionStart((event: GestureEvent) => {
         this.offsetY = getTranslateToFullScreen(this.getUIContext(), 'swiper')?.offsetY || 0
         this.imageHeight = this.getUIContext().vp2px(Number(event.target.area.height))
         this.imageWidth = this.getUIContext().vp2px(Number(event.target.area.width))
         this.status = Status.PINCHING;
         this.updateCenter([this.getUIContext().vp2px(event.pinchCenterX),
           this.getUIContext().vp2px(event.pinchCenterY)])
         this.updateTranslateAccordingToCenter();
         this.startGestureScale = this.imageScale;
         this.gestureCount++;
       })
       .onActionUpdate((event: GestureEvent) => {
         this.imageScale = this.startGestureScale * event.scale;
         if (!this.isExpand && this.imageScale >= 1) {
           this.onExpand();
         }
         this.updateExtremeOffset();
       })
     ```
  4. 当expand值更改时，页面进行切换到大图页面，完成一镜到底页面切换。

     ```ts
     NavDestination() {
       NodeContainer(this.imageGalleryNodeController)
     }
     .mode(NavDestinationMode.DIALOG)
     .height('100%')
     .width('100%')
     .hideTitleBar(true)
     .onReady((context: NavDestinationContext) => {
       this.pageInfo = context.pathStack;
       const param = context.pathInfo?.param as Record<string, Object>;
       this.onBack = param['onBack'] as () => void;
     })
     .onBackPressed(() => {
       AppStorage.setOrCreate('reset', new Date());
       this.getUIContext().animateTo({ duration: 300, curve: Curve.EaseIn }, () => {
         this.backToPageOne();
       })
       return true;
     })
     ```
* 查看大图转场

  比如图片在九宫格中显示，点击查看大图，同时还支持手势下拉返回到九宫格。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/0eKDimTiQ4W72NzWtm9l1g/zh-cn_image_0000002736432939.gif)

  设置geometryTransition属性将图片首页和大图页面的图片绑定同一id值，结合属性动画效果实现一镜到底效果。核心代码如下：

  1. 首页通过网格布局实现三行三列图片布局，并给每个图片设置geometryTransition属性，绑定唯一id值，绑定共享的两个图片组件。

     ```ts
     NavDestination() {
       Column() {
         Grid(this.scroller) {
           ForEach(this.data, (item: number) => {
             GridItem() {
               if (this.clickedIndex !== item || (this.isFirstPageShow)) {
                 Image($r(`app.media.img_${item % 9}`))
                   .width('100%')
                   .height('100%')
                   .objectFit(ImageFit.Cover)
                   .id('item2_' + item)
                   .onClick(() => {
                     this.onItemClick(item);
                   })
                   .geometryTransition(this.clickedIndex === item ? 'app.media.img_' + item.toString() : '')
                   .transition(TransitionEffect.opacity(0.99))
               }
             }
             .width(this.getUIContext().px2vp(381))
             .height(this.getUIContext().px2vp(381))
           }, (item: number) => item + '')
         }
         .rowsTemplate('1fr 1fr 1fr')
         .columnsTemplate('1fr 1fr 1fr')
         .columnsGap(2)
         .rowsGap(2)
         .size({
           width: this.getUIContext().px2vp(1169),
           height: this.getUIContext().px2vp(1169)
         })
         .margin({ top: 16 })
       }
     }
     .title('View larger picture')
     .height('100%')
     .width('100%')
     .onReady((context: NavDestinationContext) => {
       this.pageInfo = context.pathStack;
     })
     ```
  2. 通过属性动画来进行小图和大图页面的切换，同时为了避免触发Navigation的转场动画，在pushPath()的时候把动画选项设置成了false。

     ```ts
     onItemClick(index: number): void {
       let param: Record<string, Object> = {};
       this.needFollow = false;
       this.clickedIndex = index;
       param['selectedIndex'] = this.clickedIndex;
       param['onIndexChange'] = (index: number) => {
         this.onIndexChange(index);
       };
       param['onBackToFirstPage'] = () => {
         this.onBack();
       }

       this.getUIContext().animateTo({
         duration: 250,
         curve: Curve.EaseIn,
       }, () => {
         this.pageInfo.pushPath({ name: 'ShowLargeImageWithGesturePageTwo', param: param }, false);
         this.isFirstPageShow = false;
       })
     }
     ```
* 半模态转场

  图片从页面向半模态弹窗中转场显示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/wiwwIrDSQhGZu3sPGiU92Q/zh-cn_image_0000002706833784.gif)

  利用NodeContainer组件实现跨节点迁移，将半模态SheetOptions()中的mode设置为SheetMode.EMBEDDED，该模式下新起的页面可以覆盖在半模态弹窗上，页面返回后该半模态依旧存在，半模态面板内容不丢失。通过属性动画，展示组件从初始界面至半模态页面的一镜到底动效，并在动画结束时关闭页面，并将该组件迁移至半模态页面。

  1. 创建NodeContainer节点类。

     ```ts
     export class MyNodeController extends NodeController {
       // ...
     }
     ```
  2. 首页图片绑定半模态弹窗，并通过bindContentCover设置模态转场动画。

     ```ts
     NavDestination() {
       Column() {
         Image($r('app.media.flower'))
           .opacity(this.opacityDegree)
           .width('90%')
           .id('origin')
           .enabled(this.isEnabled)
           .onClick(() => {
             this.originInfo = this.calculateData('origin');
             this.scaleValue = this.originInfo.scale;
             this.translateX = this.originInfo.translateX;
             this.translateY = this.originInfo.translateY;
             this.clipWidth = this.originInfo.clipWidth;
             this.clipHeight = this.originInfo.clipHeight;
             this.radius = 0;
             this.opacityDegree = 0;
             this.isShowSheet = true;
             this.isShowOverlay = true;
             this.isEnabled = false;
           })
       }
       .width('100%')
       .height('100%')
       .padding({ top: 16 })
       .alignItems(HorizontalAlign.Center)
       .bindSheet(this.isShowSheet, this.mySheet(), {
         mode: SheetMode.EMBEDDED,
         height: this.bindSheetHeight,
         onDisappear: () => {
           this.isShowImage = false;
           this.isShowSheet = false;
           this.isAnimating = false;
           this.isEnabled = true;
         }
       })
       .bindContentCover(this.isShowOverlay, this.overlayNode(), {
         transition: TransitionEffect.IDENTITY
       })
     }
     .backgroundColor('#F1F3F5')
     .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
     .title('half mode')
     ```
  3. 点击首页图片后将图片节点迁移至半模态，当半模态完成布局之后，触发onLayoutComplete()函数，获取到图片初始位置和半模态位置，通过自定义显示动画完成一镜到底的效果。

     ```ts
     aboutToAppear(): void {
       let onLayoutComplete: () => void = (): void => {
         this.targetInfo = this.calculateData('target');
         if (this.targetInfo.scale !== 0 && this.targetInfo.clipWidth !== 0 && this.targetInfo.clipHeight !== 0 &&
           !this.isAnimating) {
           this.isAnimating = true;
           this.getUIContext().animateTo({
             duration: 1000,
             curve: Curve.Friction,
             onFinish: () => {
               this.isShowOverlay = false;
               this.isShowImage = true;
             }
           }, () => {
             this.scaleValue = AppStorage.get('currentBreakpoint') === 'md' ? 0.382 : this.targetInfo.scale;
             this.translateX = AppStorage.get('currentBreakpoint') === 'md' ? 93.5 : this.targetInfo.translateX;
             this.clipWidth = AppStorage.get('currentBreakpoint') === 'md' ? 525 : this.targetInfo.clipWidth;
             this.clipHeight = AppStorage.get('currentBreakpoint') === 'md' ? 785 : this.targetInfo.clipHeight;
             this.translateY = this.targetInfo.translateY +
               (this.getUIContext().px2vp(WindowUtils.windowHeight_px) - this.bindSheetHeight -
               this.getUIContext().px2vp(WindowUtils.navigationIndicatorHeight_px) -
               this.getUIContext().px2vp(WindowUtils.topAvoidAreaHeight_px)) -
               (AppStorage.get('currentBreakpoint') === 'md' ? 134.3 : 0);
             this.radius = this.sheetRadius / this.scaleValue;
           })
           this.getUIContext().animateTo({
             duration: 2000,
             curve: Curve.Friction,
           }, () => {
             this.opacityDegree = 1;
           })
         }
       };
       this.listener.on('layout', onLayoutComplete);
     }
     ```

### 图标（搜索框、头像等）展开一镜到底

搜索框点击后，转场到搜索结果页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/FkigJadwSgW407vNhwAyWA/zh-cn_image_0000002736312893.gif)

将搜索框首页与搜索框页面的Search组件同时设置geometryTransition属性，并绑定同一id值。设置显式动画和transition属性的转场效果，实现搜索框的一镜到底效果。

1. 搜索框首页在Search组件添加geometryTransition属性，并绑定id值，禁用掉Navigation本身转场的动画。

   ```ts
   private showSearchPage(): void {
     this.transitionEffect = TransitionEffect.OPACITY;
     this.getUIContext().animateTo({
       curve: curves.interpolatingSpring(0, 1, 342, 38)
     }, () => {
       this.pageInfos.pushPath({ name: 'SearchLongTakeTransitionPageTwo' }, false);
     })
   }
   ```
2. 搜索页面中的Search组件添加geometryTransition()，并添加与搜索框首页中的同一id值。

   ```ts
   Search({ placeholder: 'Search' })
     .height(40)
     .placeholderColor($r('sys.color.mask_secondary'))
     .width('100%')
     .geometryTransition('SEARCH_ONE_SHOT_DEMO_TRANSITION_ID', { follow: true })
     .backgroundColor('#0D000000')
     .defaultFocus(false)
     .focusOnTouch(false)
     .focusable(false)
   ```

## 容器转场案例

### 卡片、列表展开一镜到底

在瀑布流或列表流布局中，当用户点击其中一个卡片或列表项时，应用将执行平滑的转场动画，引导用户从概览页面切换到详情页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/7Qb_wl80ThKjIDiJ0SjM3A/zh-cn_image_0000002706673850.gif)

使用WaterFlow()和LazyForEach()实现卡片列表瀑布流。利用Navigation的自定义导航转场动画能力，通过customNavContentTransition()配置列表页与详情页的自定义导航转场动画，结合componentSnapshot()将卡片进行截图避免跳转页面白屏。

1. 卡片列表页使用WaterFlow和LazyForEach实现页面布局。

   ```ts
   private onColumnClicked(indexValue: string): void {
     let param: Record<string, Object> = {};
     let clickedIndex = parseInt(indexValue);
     param['indexValue'] = clickedIndex;
     this.clickedIndex = clickedIndex;
     this.getUIContext()
       .getComponentSnapshot()
       .get('FlowItem_' + indexValue, (error: BusinessError, pixelMap: image.PixelMap) => {
         if (error) {
           hilog.error(0x0000, 'CardLongTakePageOne',
             `componentSnapshot.get error, reason: Code is ${error.code}, message is ${error.message}`);
           this.pageInfos.pushPath({ name: 'CardLongTakeTransitionPageTwo', param: param });
           return;
         } else {
           hilog.info(0x0000, 'CardLongTakePageOne', 'componentSnapshot.get success!');
           param['clickedComponentId'] = CardUtil.getFlowItemIdByIndex(indexValue);
           param['doDefaultTransition'] = () => {
             this.doFinishTransition();
           };
           SnapShotImage.pixelMap = pixelMap;
           this.pageInfos.pushPath({ name: 'CardLongTakeTransitionPageTwo', param: param });
           this.dataSource.getData(this.clickedIndex).isVisible = Visibility.Hidden;
         }
       })
   }
   ```
2. 卡片详情页通过Navigation自定义动画实现一镜到底。这里套了两层Stack()，因为要放截图，以及把原来的详情页内容转移过来。缩放、translate属性设置在Stack()这层上实现边界动画，透明度属性设置在截图上实现内容过渡。在onReady()里面注册自定义动画，通过id对动画属性进行初始化。

   ```ts
   tryRegisterCustomTransition(clickedCardId: string): void {
     try {
       this.longTakeAnimationProperties.init(clickedCardId, this.prePageDoFinishTransition);
       CustomTransition.getInstance().registerNavParam(this.pageId, 2000,
         (transitionProxy: NavigationTransitionProxy) => {
           this.longTakeAnimationProperties.doAnimation(transitionProxy);
         });
       hilog.info(0x0000, 'CardLongTakePageTwo', 'register successes');
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, 'CardLongTakePageTwo', `this is error:code=${err.code}, message=${err.message}`);
       this.longTakeAnimationProperties.setFinalStatus();
     }
   }

   // ...

   build() {
     NavDestination() {
       Stack({ alignContent: Alignment.TopStart }) {
         Stack({ alignContent: Alignment.TopStart }) {
           Image(this.snapShotImage)
             .size(this.longTakeAnimationProperties.snapShotSize)
             .objectFit(ImageFit.Auto)
             .opacity(this.longTakeAnimationProperties.snapShotOpacity)
             .syncLoad(true)
             .position({
               x: this.longTakeAnimationProperties.snapShotPositionX,
               y: this.longTakeAnimationProperties.snapShotPositionY
             })

           DetailPageContent({
             indexValue: this.indexValue,
             pageInfos: this.pageInfos,
             onBackPressed: () => {
               this.onBackPressed()
             },
             SharedComponentId: CardUtil.getPostPageImageId(this.clickedCardId)
           })
             .size({
               width: '100%',
               height: '100%'
             })
             .opacity(this.longTakeAnimationProperties.postPageOpacity)
         }
         .width('100%')
         .position({
           x: this.longTakeAnimationProperties.positionXValue,
           y: this.longTakeAnimationProperties.positionYValue
         })
       }
       .scale({
         x: this.longTakeAnimationProperties.scaleValue,
         y: this.longTakeAnimationProperties.scaleValue
       })
       .translate({
         x: this.longTakeAnimationProperties.translateX,
         y: this.longTakeAnimationProperties.translateY
       })
       .width(this.longTakeAnimationProperties.clipWidth)
       .height(this.longTakeAnimationProperties.clipHeight)
       .borderRadius(this.longTakeAnimationProperties.radius)
       .expandSafeArea([SafeAreaType.SYSTEM])
       .backgroundColor($r('app.color.water_flow_background_color'))
       .clip(true)
     }
     .backgroundColor(this.longTakeAnimationProperties.navDestinationBgColor)
     .GestureStyles()
     .hideTitleBar(true)
     .onReady((context: NavDestinationContext) => {
       this.pageInfos = context.pathStack;
       let param = context.pathInfo?.param as Record<string, Object>;
       let clickedCardId = param['clickedComponentId'] as string;
       this.indexValue = param['indexValue'] as number;
       this.prePageDoFinishTransition = param['doDefaultTransition'] as () => void;
       if (context.navDestinationId && clickedCardId) {
         this.pageId = context.navDestinationId;
         this.clickedCardId = clickedCardId;
         this.tryRegisterCustomTransition(clickedCardId);
       }
     })
     .onBackPressed(() => {
       return this.onBackPressed();
     })
     .onDisAppear(() => {
       CustomTransition.getInstance().unRegisterNavParam(this.pageId);
     })
   }

   // ...
   ```

列表一镜到底效果图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/fVv0gpLGTue9ZR4M030mQA/zh-cn_image_0000002736432941.gif)

将列表项与详情页面同时设置geometryTransition属性，并绑定同一id值。每个列表项设置显式动画和transition属性的转场效果，实现列表展开的一镜到底效果。

1. 列表页面中每一个列表项设置geometryTransition属性，并绑定当前列表的id值。

   ```ts
   @Component
   export struct MyButton {
     @Prop listContent: ListContent;
     @Prop indexValue: string;
     @State scaleValue: number = 1;

     build() {
       Column({ space: 10 }) {
         Row({ space: 5 }) {
           Line()
             .startPoint([0, 0])
             .endPoint([0, 20])
             .strokeWidth(5)
             .stroke(Color.Yellow)
             .strokeLineCap(LineCapStyle.Round)
           Text(this.listContent.title)
             .fontWeight(FontWeight.Medium)
             .fontSize(16)
         }

         Text(this.listContent.content)
           .fontColor(Color.Grey)
           .maxLines(1)
           .textOverflow({ overflow: TextOverflow.Ellipsis })
           .fontSize(14)
       }
       .alignItems(HorizontalAlign.Start)
       .padding({
         left: 20,
         right: 20,
         top: 20,
         bottom: 20
       })
       .width('91%')
       .backgroundColor(Color.White)
       .clip(true)
       .borderRadius(20)
       .scale({
         x: this.scaleValue,
         y: this.scaleValue
       })
       .geometryTransition(this.indexValue, { follow: true })
       .onTouch((event?: TouchEvent) => {
         this.onTouchProcess(event);
       })
       .onClick(() => {
         this.onButtonClicked?.(this.indexValue);
       })
     }

     onButtonClicked: (index: string) => void = (_index: string) => {
     };

     private onTouchProcess(event?: TouchEvent): void {
       if (!event) {
         return;
       }
       if (event.type === TouchType.Down) {
         this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 350, 35) }, () => {
           this.scaleValue = 0.95;
         })
       } else if (event.type === TouchType.Up) {
         this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 350, 35) }, () => {
           this.scaleValue = 1;
         })
       } else if (event.type === TouchType.Cancel) {
         this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 350, 35) }, () => {
           this.scaleValue = 1;
         })
       }
     }
   }
   ```
2. 列表详情页中的容器组件Column组件设置geometryTransition属性，并绑定对应列表项的id值，完成一镜到底效果。

   ```ts
   NavDestination() {
     Column({ space: 20 }) {
       Text(this.param.title)
         .fontSize(30)
         .fontWeight(FontWeight.Medium)
       Text(this.param.content)
         .fontColor($r('sys.color.password_icon_focus_color'))
         .lineHeight(28)
         .fontSize(16)
     }
     .alignItems(HorizontalAlign.Start)
     .clip(true)
     .size({
       width: '100%',
       height: '100%'
     })
     .geometryTransition(this.param.geometryId)
   }
   .padding({
     top: 46,
     left: 16,
     right: 16
   })
   .backgroundColor(Constants.DEFAULT_BG_COLOR)
   .transition(TransitionEffect.OPACITY)
   .hideTitleBar(true)
   .backgroundColor(Color.Transparent)
   .onReady((context: NavDestinationContext) => {
     this.pageInfos = context.pathStack;
     this.param = (context.pathInfo.param as ListDetailPageExtraInfo);
   })
   .onBackPressed(() => {
     this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 342, 38) }, () => {
       this.pageInfos.pop(false);
     })
     return true;
   })
   ```

### “图书”翻页展开一镜到底

阅读类应用中，点击一本“图书”的图标后，模拟图书翻页展开的效果，转场到书本内容页面，同时支持手势返回。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/65gdNBhCSTuQsdKJ39X7mQ/zh-cn_image_0000002706833786.gif)

利用Navigation的自定义导航转场动画能力，通过customNavContentTransition()配置书籍页与详情页的自定义导航转场动画实现图书翻页一镜到底效果。使用rotate属性实现书籍翻页的旋转效果。

1. 书架页面通过Grid组件实现书架第一行书籍布局，使用Swiper()组件实现书架第一行书籍布局。

   ```ts
   build() {
     NavDestination() {
       Scroll() {
         Column({ space: 12 }) {
           Grid() {
             ForEach(this.dataSource, (item: BookItem, index: number) => {
               GridItem() {
                 Image($r(item.coverImageUrl))
                   .id(item.id)
                   .width('100%')
                   .onClick(() => {
                     this.onColumnClicked(item.id, item.coverImageUrl, this.dataSource[0].id, () => {
                       this.dataSource.sort((a, b) => b.timestamp - a.timestamp);
                     })
                     this.dataSource[index].timestamp = Number(new Date());
                   })
               }
               .width(this.columnWidth)
             }, (item: BookItem) => JSON.stringify(item))
           }
           .padding({
             left: 12,
             right: 12,
             top: 12
           })
           .columnsTemplate(this.columnType)
           .columnsGap(10)
           .rowsGap(10)

           Column({ space: 12 }) {
             Text('Recently read')
               .fontSize(16)
               .fontWeight(FontWeight.Medium)
               .fontColor(Color.Gray)
             Swiper(this.swiperController) {
               ForEach(this.recentData, (item: BookItem) => {
                 GridItem() {
                   Image($r(item.coverImageUrl))
                     .id(item.id)
                     .onClick(() => {
                       this.onColumnClicked(item.id, item.coverImageUrl);
                     })
                 }
               }, (item: BookItem) => JSON.stringify(item))
             }
             .indicator(false)
             .displayCount(3)
             .loop(false)
             .itemSpace(10)
           }
           .padding({
             left: 12,
             right: 12
           })
           .alignItems(HorizontalAlign.Start)
         }
       }
     }
     // ...
   }

   // ...

   private onColumnClicked(bookId: string, bookCoverUrl: string, toBookId?: string, prePageCallback?: () => void): void {
     try {
       CustomTransition.getInstance().unRegisterNavParam(this.pageId);
       const fromCardItemInfo: RectInfoInPx =
         ComponentAttrUtils.getRectInfoById(WindowUtils.window.getUIContext(), bookId);
       let param: Record<string, Object> = {};
       param['fromCardItemInfo'] = fromCardItemInfo;
       param['bookCoverUrl'] = bookCoverUrl;
       if (toBookId) {
         const toCardItemInfo: RectInfoInPx =
           ComponentAttrUtils.getRectInfoById(WindowUtils.window.getUIContext(), toBookId);
         param['toCardItemInfo'] = toCardItemInfo;
       }
       if (prePageCallback) {
         param['prePageCallback'] = prePageCallback;
       }
       this.pageInfos.pushPath({ name: 'BookFlipLongTakeTransitionPageTwo', param: param });
     } catch (err) {
       let error = err as BusinessError;
       hilog.error(0x0000, 'BookFlipLongTakeTransitionPageOne',
         `onColumnClicked failed. error code=${error.code}, message=${error.message}`);
     }
   }
   ```
2. 书籍详情页通过Navigation自定义动画实现一镜到底。

   ```ts
   NavDestination() {
     Stack() {
       Column() {
         Text($r('app.string.DetailPage_text'))
           .fontColor($r('sys.color.password_icon_focus_color'))
           .lineHeight(28)
           .fontSize(16)
       }
       .width(AppStorage.get('currentBreakpoint') === 'md' ? '75%' : '100%')
       .height('100%')
       .alignItems(HorizontalAlign.Start)
       .padding({
         left: 16,
         right: 16,
         top: 46
       })

       if (!this.doDefaultTransition) {
         Image($r(this.bookCoverUrl))
           .objectFit(ImageFit.Cover)
           .syncLoad(true)
           .rotate({
             x: 0,
             y: 1,
             z: 0,
             angle: this.bookFlipLongTakeTransitionProperties.coverRotateAngle,
             centerX: 0,
             centerY: '50%'
           })
           .scale({
             x: this.bookFlipLongTakeTransitionProperties.coverScale,
             centerX: 0,
             centerY: '50%'
           })
       }
     }
     .scale({
       x: this.bookFlipLongTakeTransitionProperties.scaleValue,
       y: this.bookFlipLongTakeTransitionProperties.scaleValue
     })
     .translate({
       x: this.bookFlipLongTakeTransitionProperties.translateX,
       y: this.bookFlipLongTakeTransitionProperties.translateY
     })
     .width(this.bookFlipLongTakeTransitionProperties.clipWidth)
     .height(this.bookFlipLongTakeTransitionProperties.clipHeight)
     .backgroundColor('#DEDFDF')
   }
   .backgroundColor(this.bookFlipLongTakeTransitionProperties.navDestinationBgColor)
   .GestureStyles()
   .hideTitleBar(true)
   .onReady((context: NavDestinationContext) => {
     this.pageInfos = context.pathStack;
     let param = context.pathInfo?.param as Record<string, Object>;
     this.bookCoverUrl = param['bookCoverUrl'] as string;
     this.fromCardItemInfo = param['fromCardItemInfo'] as RectInfoInPx;
     this.toCardItemInfo = (param['toCardItemInfo'] || param['fromCardItemInfo']) as RectInfoInPx;
     this.prePageCallback = param['prePageCallback'] as () => void;
     if (context.navDestinationId) {
       this.pageId = context.navDestinationId;
     }
     CustomTransition.getInstance()
       .registerNavParam(this.pageId, 500, (transitionProxy: NavigationTransitionProxy) => {
         this.bookFlipLongTakeTransitionProperties.doAnimation(transitionProxy, this.fromCardItemInfo,
           this.toCardItemInfo);
       }, () => {
         this.bookFlipLongTakeTransitionProperties.onInteractiveFinish();
       }, () => {
         this.bookFlipLongTakeTransitionProperties.onInteractive(
           this.fromCardItemInfo, this.toCardItemInfo);
       });
   })
   .onBackPressed(() => {
     return this.onBackPressed();
   })
   .onDisAppear(() => {
     CustomTransition.getInstance().unRegisterNavParam(this.pageId);
   })
   ```

### 视频展开一镜到底

视频组件从一个页面向目标页面的转场，在一镜到底的过程中，视频需要持续播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/WEKXIso3SyqhdmtiDuR5iQ/zh-cn_image_0000002736312895.gif)

使用WaterFlow()和LazyForEach()实现卡片列表瀑布流。利用NodeController实现组件的跨节点迁移，通过customNavContentTransition配置概览页与视频详情的自定义导航转场动画，给节点的迁移过程赋予一镜到底效果。

1. 创建NodeController节点类。

   ```ts
   export class MyNodeController extends NodeController {
     // ...
   }
   ```
2. 视频首页使用WaterFlow()和LazyForEach()实现页面布局，点击视频后将视频节点迁移至视频播放页面，通过Navigation自定义动画完成一镜到底的效果。

   ```ts
   NavDestination() {
     WaterFlow() {
       LazyForEach(this.dataSource, (_: CardAttr, index: number) => {
         FlowItem() {
           VideoCardComponent({
             isPlaying: false,
             index,
             onColumnClicked: (prePageCallback) => {
               this.onColumnClicked(`xComponent_${index}`, prePageCallback)
             }
           })
         }
         .width('100%')
         .borderRadius(10)
         .clip(true)
         .id('FlowItem_' + index.toString())
       }, (item: string) => item)
     }
     .edgeEffect(EdgeEffect.Spring)
     .onScrollIndex((first: number) => {
       this.scrollFirstIndex = first;
     })
     .padding(12)
     .columnsTemplate(this.columnType)
     .columnsGap(12)
     .rowsGap(10)
     .width('100%')
     .height('100%')
   }
   .backgroundColor(Constants.DEFAULT_BG_COLOR)
   .title(getResourceString(this.getUIContext(), $r('app.string.video_title'), this))
   .onReady((context: NavDestinationContext) => {
     this.pageInfos = context.pathStack;
     if (context.navDestinationId) {
       this.pageId = context.navDestinationId;
     }
   })
   .onDisAppear(() => {
     CustomTransition.getInstance().unRegisterNavParam(this.pageId);
   })
   ```
