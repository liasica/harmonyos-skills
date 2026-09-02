---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-950
title: 解决bindContextMenu长按菜单关闭时的事件穿透问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 解决bindContextMenu长按菜单关闭时的事件穿透问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:4b8eb3bb2ddd6166d4899af592ec7732165dbb208de244f7c715cde52ad6dd23
---

## 问题现象

当使用bindContextMenu为组件A配置长按菜单时，菜单弹出后，如果点击菜单区域外的任意位置可以关闭菜单，但组件A（或其他区域外的组件）的点击事件也会被触发。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/-jhsaGTyTmuYw73k-LYlfw/zh-cn_image_0000002658920459.gif "点击放大")

## 背景知识

* [bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu12)用于为组件绑定自定义菜单。菜单的显示和隐藏通过控制绑定的isShown属性实现：当isShown为true时，菜单弹出；为false时，菜单隐藏。
* [hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性可以实现在复杂的多层级场景下，一些组件能够响应手势和事件，而一些组件不能响应手势和事件。HitTestMode.Block自身会响应触摸测试，阻塞子节点和兄弟节点的触摸测试，从而导致子节点和兄弟节点的onTouch事件和手势均无法触发。

## 解决方案

为解决点击菜单区域外时事件穿透问题，当菜单显示时，在页面最外层组件上添加hitTestBehavior.Block属性以阻止事件传播。同时，在最外层组件的点击事件回调方法中加入一个if条件判断，判断是否是处于菜单显示的情况，若是则直接返回，不处理后面的点击逻辑。

```screen
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct BindContextMenuIndex {
  @State menuShow: boolean = false;
  @State flag: boolean = false;
  promptAction: PromptAction = new PromptAction();

  @Builder
  menu() {
    Menu() {
      MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单1' });
      MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单2' });
      MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单3' });
    };
  }

  build() {
    Column() {
      Text('第一层')
        .height('150vp');
      Column() {
        Text('第二层')
          .height('150vp');
        Column() {
          Text('第三层的兄弟层1')
            .height('150vp');
        }
        .width('100%')
        .backgroundColor('#0D5AF5')
        .onClick(() => {
          this.promptAction.showToast({ message: '第三层的兄弟层1' });
        })
        // 长按手势，将控制菜单显隐的值修改为true
        .gesture(LongPressGesture().onAction(() => {
          this.menuShow = true;
          this.flag = true;
        }))
        // 绑定菜单
        .bindContextMenu(!!this.menuShow, this.menu(), {
          onDisappear: () => {
            this.menuShow = false;
          }
        });

        Column() {
          Text('第三层的兄弟层2')
            .height('150vp');
        }
        .width('100%')
        .backgroundColor('#0D85F5')
        .onClick(() => {
          this.promptAction.showToast({ message: '第三层的兄弟层2' });
        });
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#65BA5F')
      .onClick(() => {
        this.promptAction.showToast({ message: '第二层' });
      });
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ECA724')
    .onClick(() => {
      console.info('onClick');
      if (this.flag) {
        this.flag = false;
        return;
      }
      this.promptAction.showToast({ message: '第一层' });
    })
    // 阻止事件穿透
    .hitTestBehavior(
      this.menuShow ?
      HitTestMode.Block :
      HitTestMode.Default
    );
  }
}
```
