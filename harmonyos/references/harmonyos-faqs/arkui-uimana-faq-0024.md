---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0024
title: 深浅色模式切换页面渲染失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 深浅色模式切换页面渲染失败
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:32+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:3924587ff02be0f8965eeeca4353554e9e45d592437de9017171db10946d4a70
---

**Q：在Tabs的tabBar中使用Canvas，当深浅色模式切换后，tabBar中的内容消失。**

**问题如图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/sBrKbdXGTDOigR9Njcl2NA/zh-cn_image_0000002772679746.png "点击放大")

**A**：出现上述问题是因为在切换深浅色模式时，Canvas组件会被销毁并重新创建，此时在tabBar中使用的Canvas组件会在短时间内重新渲染并重新加载到组件树中，从而使得CanvasRenderingContext2D被旧的Canvas组件绑定，而新的Canvas组件无法正确绘制内容。为了解决上述问题，可以将CanvasRenderingContext2D和Canvas组件封装为一个自定义组件，以避免这种情况，示例如下：

```ts
interface ITabs {
  name: string;
  currentName?: string;
  previousName?: string;
  canvasRenderingContext: CanvasRenderingContext2D;
}

const tabList: ITabs[] = [
  { name: 'home', canvasRenderingContext: new CanvasRenderingContext2D() },
  {
    name: 'category',
    canvasRenderingContext: new CanvasRenderingContext2D()
  },
  { name: 'cart', canvasRenderingContext: new CanvasRenderingContext2D() },
  { name: 'my', canvasRenderingContext: new CanvasRenderingContext2D() },
];

@Component
struct TabBuilderLottie {
  @Prop index: number;

  build() {
    Canvas(tabList[this.index].canvasRenderingContext)
      .onReady(() => {
        let path = new Path2D();
        path.moveTo(150, 50);
        path.lineTo(50, 150);
        path.lineTo(100, 250);
        path.lineTo(200, 250);
        path.lineTo(250, 150);
        path.closePath();
        // 设定填充色为蓝色
        tabList[this.index].canvasRenderingContext.fillStyle = '#0097D4';
        // 使用填充的方式，将Path2D描述的五边形绘制在canvas组件内部
        tabList[this.index].canvasRenderingContext.fill(path);
        tabList[this.index].canvasRenderingContext.fillStyle = '#0097D4';
        // 以(50,50)为左上顶点，画一个宽高200的矩形
        tabList[this.index].canvasRenderingContext.fillRect(50, 50, 200, 200);
        // 以(70,70)为左上顶点，清除宽150高100的区域
        tabList[this.index].canvasRenderingContext.clearRect(70, 70, 150, 100);
        tabList[this.index].canvasRenderingContext.restore();
      });
  }
}

@Entry
@Component
struct TabBuilderLottiePage {
  @State tabs: ITabs[] = tabList;

  build() {
    Tabs({ barPosition: BarPosition.End }) {
      ForEach(this.tabs, (item: ITabs, index: number) => {
        TabContent() {
          Text(item.name);
        }
        .tabBar(this.TabBuilderLottie(index));
      });
    }
    .width('100%')
    .height('100%')
    .barMode(BarMode.Fixed)
    .barHeight(60)
    .fadingEdge(false)
    .scrollable(false);
  }

  @Builder
  TabBuilderLottie(index: number) {
    TabBuilderLottie({ index: index });
  }
}
```

示例实现效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/IFlwiCxITsiqJu7cFq2InQ/zh-cn_image_0000002802119575.png "点击放大")
